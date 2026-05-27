"""3D isometric sketch of a radius platen for a belt grinder.

Specs:
  - Length (along belt travel):     200 mm (20 cm)
  - Width  (across belt):            49 mm (4.9 cm)
  - Base slab thickness:             15 mm (1.5 cm)
  - Top arc: 36" (914.4 mm) diameter wheel  ->  R = 457.2 mm
  - Sagitta (crown rise above slab): 11.07 mm
  - Max total height (center):       26.07 mm
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# -------- Dimensions (mm) --------
L = 200.0          # length (X)
W = 49.0           # width  (Y)
BASE = 15.0        # base slab thickness
R = 457.2          # 36" diameter / 2
SAG = R - np.sqrt(R**2 - (L/2)**2)   # ≈ 11.07 mm
TOP_MAX = BASE + SAG

print(f"Sagitta:     {SAG:.3f} mm")
print(f"Total max H: {TOP_MAX:.3f} mm")

# -------- Build the curved top surface --------
nx, ny = 80, 12
x = np.linspace(-L/2, L/2, nx)
y = np.linspace(0, W, ny)
X, Y = np.meshgrid(x, y)
# z of arc: center high, edges low
Z_top = BASE + (R - np.sqrt(R**2 - X**2))   # this is base + (sag at edges - drop)
# Re-derive correctly so center is highest:
Z_top = BASE + SAG - (R - np.sqrt(R**2 - X**2))

# -------- Plot --------
fig = plt.figure(figsize=(11, 7))
ax = fig.add_subplot(111, projection='3d')

# Curved top surface
ax.plot_surface(X, Y, Z_top, color='#cfd8dc', edgecolor='#37474f',
                linewidth=0.3, alpha=0.95, shade=True)

# Base slab (5 rectangular faces — top of slab is hidden under arc)
def quad(verts, color, alpha=0.9, edge='#263238'):
    p = Poly3DCollection([verts], alpha=alpha, facecolor=color, edgecolor=edge, linewidths=0.8)
    ax.add_collection3d(p)

# Bottom of base
quad([(-L/2, 0, 0), ( L/2, 0, 0), ( L/2, W, 0), (-L/2, W, 0)], '#90a4ae')
# Front (y=0) wall up to base top
quad([(-L/2, 0, 0), ( L/2, 0, 0), ( L/2, 0, BASE), (-L/2, 0, BASE)], '#b0bec5')
# Back (y=W) wall
quad([(-L/2, W, 0), ( L/2, W, 0), ( L/2, W, BASE), (-L/2, W, BASE)], '#b0bec5')

# End caps (curved profile) at x = -L/2 and x = +L/2
# The arc reaches BASE at the ends (sag drop = SAG, so top = BASE)
# Build polygon: bottom edge + vertical sides + top edge (which is just the base height at ends)
for x_end in (-L/2, L/2):
    # at ends the arc height = BASE (since drop equals sag)
    verts = [(x_end, 0, 0), (x_end, W, 0), (x_end, W, BASE), (x_end, 0, BASE)]
    quad(verts, '#b0bec5')

# Front/back curved side walls (between base top and arc top)
xs_fine = np.linspace(-L/2, L/2, 60)
zs_arc = BASE + SAG - (R - np.sqrt(R**2 - xs_fine**2))
# Front wall (y=0): polygon from base top up to arc
front = [(xx, 0, BASE) for xx in xs_fine] + [(xx, 0, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(front, '#b0bec5', alpha=0.95)
back  = [(xx, W, BASE) for xx in xs_fine] + [(xx, W, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(back, '#b0bec5', alpha=0.95)

# -------- Dimension annotations --------
def dim(p1, p2, txt, offset=(0,0,3), color='#d32f2f'):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color=color, lw=1.5)
    mid = ((p1[0]+p2[0])/2 + offset[0],
           (p1[1]+p2[1])/2 + offset[1],
           (p1[2]+p2[2])/2 + offset[2])
    ax.text(*mid, txt, color=color, fontsize=9, weight='bold')

# Length
dim((-L/2, -8, 0), (L/2, -8, 0), f"L = 200 mm", offset=(0,-6,0))
# Width
dim((L/2+8, 0, 0), (L/2+8, W, 0), f"W = 49 mm", offset=(8,0,0))
# Base height
dim((-L/2-8, 0, 0), (-L/2-8, 0, BASE), f"Base = 15 mm", offset=(-30,0,-2))
# Sagitta
dim((0, W+6, BASE), (0, W+6, BASE+SAG), f"Sagitta = 11.07 mm", offset=(0,8,2))
# Total max height
dim((L/2+8, W, 0), (L/2+8, W, BASE+SAG), f"Max H = 26.07 mm", offset=(15,0,4))

# Radius callout
ax.text(0, W/2, BASE+SAG+6, "Top arc: R = 457.2 mm  (Ø 36\" wheel)",
        color='#1565c0', fontsize=10, ha='center', weight='bold')

# Cosmetics
ax.set_xlabel('X — length (mm)')
ax.set_ylabel('Y — width (mm)')
ax.set_zlabel('Z — height (mm)')
ax.set_title('Radius Platen — 36" wheel profile, 200 × 49 mm, 15 mm base',
             fontsize=12, weight='bold')
ax.set_box_aspect((L, W*2.5, (BASE+SAG)*4))   # exaggerate Z so curve is visible
ax.view_init(elev=22, azim=-55)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/user/github-pages/platen_sketch.png', dpi=160, bbox_inches='tight')
print("Saved: /home/user/github-pages/platen_sketch.png")
