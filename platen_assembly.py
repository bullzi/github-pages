"""3D assembly sketch: radius platen + CNC steel L-bracket cassette.

Shows the platen mounted to the bracket with 4 M5 SHCS from underneath,
and the 2 OEM grinder mounting bolts through the bracket front plate.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---- Platen ----
L, W, TOP = 200.0, 49.0, 15.0
R = 457.2
SAG = R - np.sqrt(R**2 - (L/2)**2)
BASE = TOP - SAG

# ---- Bracket ----
TOP_LEN, TOP_WID, TOP_THK = 140.0, 49.0, 10.0
FRONT_THK, FRONT_HEIGHT = 10.0, 50.0
GR_BOLT_SPACING, GR_BOLT_DIA = 80.0, 8.0
PL_DX, PL_DY = 40.0, 15.0          # platen bolt pattern half-spacing

# Bracket sits with top face at z = 0; platen sits on top of bracket
# So platen z range: 0 .. TOP, with arc on top.
# Bracket top plate z range: -TOP_THK .. 0
# Bracket front plate hangs down from rear edge in -Y direction.

fig = plt.figure(figsize=(13, 8))
ax = fig.add_subplot(111, projection='3d')

# ----- platen (curved top) -----
nx, ny = 90, 14
xx = np.linspace(-L/2, L/2, nx)
yy = np.linspace(-W/2, W/2, ny)
X, Y = np.meshgrid(xx, yy)
Zt = TOP - (R - np.sqrt(R**2 - X**2))
ax.plot_surface(X, Y, Zt, color='#90caf9', edgecolor='#1565c0',
                linewidth=0.25, alpha=0.92, shade=True)

def quad(verts, color, alpha=0.92, edge='#263238', lw=0.8):
    p = Poly3DCollection([verts], alpha=alpha, facecolor=color, edgecolor=edge, linewidths=lw)
    ax.add_collection3d(p)

# Platen sides
xs_fine = np.linspace(-L/2, L/2, 80)
zs_arc  = TOP - (R - np.sqrt(R**2 - xs_fine**2))
# Front (-Y) wall
front = [(xx, -W/2, 0) for xx in xs_fine] + [(xx, -W/2, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(front, '#bbdefb')
back  = [(xx,  W/2, 0) for xx in xs_fine] + [(xx,  W/2, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(back, '#bbdefb')
# Platen end caps (z 0 -> BASE since arc reaches BASE at ends)
for xe in (-L/2, L/2):
    quad([(xe, -W/2, 0), (xe, W/2, 0), (xe, W/2, BASE), (xe, -W/2, BASE)], '#bbdefb')

# ----- bracket top plate -----
bx0, bx1 = -TOP_LEN/2, TOP_LEN/2
by0, by1 = -TOP_WID/2, TOP_WID/2
bz0, bz1 = -TOP_THK, 0
# 6 faces of bracket top plate
quad([(bx0,by0,bz0),(bx1,by0,bz0),(bx1,by1,bz0),(bx0,by1,bz0)], '#ef5350')  # bottom
quad([(bx0,by0,bz0),(bx1,by0,bz0),(bx1,by0,bz1),(bx0,by0,bz1)], '#e53935')  # front
quad([(bx0,by1,bz0),(bx1,by1,bz0),(bx1,by1,bz1),(bx0,by1,bz1)], '#e53935')  # back
quad([(bx0,by0,bz0),(bx0,by1,bz0),(bx0,by1,bz1),(bx0,by0,bz1)], '#e53935')  # left
quad([(bx1,by0,bz0),(bx1,by1,bz0),(bx1,by1,bz1),(bx1,by0,bz1)], '#e53935')  # right
# (top of bracket hidden under platen — skip)

# ----- bracket front (vertical) plate -----
fx0, fx1 = -TOP_LEN/2, TOP_LEN/2
fy0, fy1 = by0 - FRONT_THK, by0   # hangs in -Y from bracket rear edge... actually keep at -Y front
fz0, fz1 = bz0 - (FRONT_HEIGHT - TOP_THK), bz0
# Place front plate at the FRONT (-Y) of the bracket — matches photo (bolts face grinder)
quad([(fx0,fy0,fz0),(fx1,fy0,fz0),(fx1,fy0,fz1),(fx0,fy0,fz1)], '#c62828')
quad([(fx0,fy1,fz0),(fx1,fy1,fz0),(fx1,fy1,fz1),(fx0,fy1,fz1)], '#c62828')
quad([(fx0,fy0,fz0),(fx0,fy1,fz0),(fx0,fy1,fz1),(fx0,fy0,fz1)], '#c62828')
quad([(fx1,fy0,fz0),(fx1,fy1,fz0),(fx1,fy1,fz1),(fx1,fy0,fz1)], '#c62828')
quad([(fx0,fy0,fz0),(fx1,fy0,fz0),(fx1,fy1,fz0),(fx0,fy1,fz0)], '#c62828')  # bottom

# ----- 4 platen-to-bracket M5 screws (visible heads on bracket bottom) -----
def screw(x, y, head_z=bz0, head_d=8.5, head_h=4, shaft_top=BASE+5):
    """Draw a simple SHCS — cylinder head on bracket bottom + shaft up into platen."""
    # head (below bracket bottom)
    theta = np.linspace(0, 2*np.pi, 24)
    hz0, hz1 = head_z - head_h, head_z
    for z in [hz0, hz1]:
        circ = [(x + head_d/2*np.cos(t), y + head_d/2*np.sin(t), z) for t in theta]
        quad(circ, '#424242', alpha=0.95)
    # sides of head
    for i in range(len(theta)-1):
        v = [(x+head_d/2*np.cos(theta[i]),   y+head_d/2*np.sin(theta[i]),   hz0),
             (x+head_d/2*np.cos(theta[i+1]), y+head_d/2*np.sin(theta[i+1]), hz0),
             (x+head_d/2*np.cos(theta[i+1]), y+head_d/2*np.sin(theta[i+1]), hz1),
             (x+head_d/2*np.cos(theta[i]),   y+head_d/2*np.sin(theta[i]),   hz1)]
        quad(v, '#424242', alpha=0.95, lw=0.2)
    # shaft (5mm dia, runs through bracket and into platen)
    ax.plot([x,x],[y,y],[head_z, shaft_top], color='#212121', lw=1.5)

for dx in (-PL_DX, PL_DX):
    for dy in (-PL_DY, PL_DY):
        screw(dx, dy)

# ----- 2 grinder-mount bolts on front plate -----
front_y_outer = fy0
for dx in (-GR_BOLT_SPACING/2, GR_BOLT_SPACING/2):
    bz_center = fz0 + 25   # FRONT_BOLT_Z = 25 from bottom of front plate
    theta = np.linspace(0, 2*np.pi, 24)
    head_d = 16
    head_y_outer = front_y_outer - 4   # head sticks out 4 mm
    for yv in [front_y_outer, head_y_outer]:
        circ = [(dx + head_d/2*np.cos(t), yv, bz_center + head_d/2*np.sin(t)) for t in theta]
        quad(circ, '#37474f', alpha=0.95)
    for i in range(len(theta)-1):
        v = [(dx+head_d/2*np.cos(theta[i]),   front_y_outer,  bz_center+head_d/2*np.sin(theta[i])),
             (dx+head_d/2*np.cos(theta[i+1]), front_y_outer,  bz_center+head_d/2*np.sin(theta[i+1])),
             (dx+head_d/2*np.cos(theta[i+1]), head_y_outer,   bz_center+head_d/2*np.sin(theta[i+1])),
             (dx+head_d/2*np.cos(theta[i]),   head_y_outer,   bz_center+head_d/2*np.sin(theta[i]))]
        quad(v, '#37474f', alpha=0.95, lw=0.2)

# ----- Annotations -----
def lbl(p, txt, color='#1a237e', size=9):
    ax.text(*p, txt, color=color, fontsize=size, weight='bold')

lbl((0, W/2+12, TOP+6), 'RADIUS PLATEN  (steel, 200 × 49, 15 mm crown)', color='#0d47a1')
lbl((TOP_LEN/2 + 5, 0, -TOP_THK/2), 'L-BRACKET\n(CNC steel)', color='#b71c1c')
lbl((0, fy0-30, fz0 + 25), '2× OEM bolts\n(grinder mount)', color='#37474f')
lbl((-L/2 - 30, 0, -TOP_THK - 10), '4× M5 SHCS\nfrom below', color='#212121')

# Cosmetics
ax.set_xlabel('X — length (mm)')
ax.set_ylabel('Y — width (mm)')
ax.set_zlabel('Z — height (mm)')
ax.set_title('Cassette Assembly — Radius Platen + L-Bracket Adapter',
             fontsize=13, weight='bold')
ax.set_box_aspect((L, W*3, (TOP + FRONT_HEIGHT)*1.8))
ax.view_init(elev=20, azim=-60)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/user/github-pages/platen_assembly.png', dpi=160, bbox_inches='tight')
print("Saved: /home/user/github-pages/platen_assembly.png")
