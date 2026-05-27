"""Side profile (true scale) of the platen — shows the actual curvature."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

L = 200.0
BASE = 15.0
R = 457.2
SAG = R - np.sqrt(R**2 - (L/2)**2)

fig, ax = plt.subplots(figsize=(12, 4.5))

# Arc top
xs = np.linspace(-L/2, L/2, 400)
zs = BASE + SAG - (R - np.sqrt(R**2 - xs**2))

# Filled cross-section
poly_x = np.concatenate([[-L/2], xs, [L/2, -L/2]])
poly_z = np.concatenate([[0],    zs, [0,    0]])
ax.fill(poly_x, poly_z, facecolor='#cfd8dc', edgecolor='#263238', lw=1.5)

# Centerline
ax.axvline(0, color='#9e9e9e', ls=':', lw=0.8)

# Dimension lines
def hdim(x1, x2, y, txt, off=4):
    ax.annotate('', xy=(x2, y), xytext=(x1, y),
                arrowprops=dict(arrowstyle='<->', color='#d32f2f', lw=1.2))
    ax.text((x1+x2)/2, y-off, txt, ha='center', va='top',
            color='#d32f2f', fontsize=10, weight='bold')

def vdim(y1, y2, x, txt, off=4, ha='left'):
    ax.annotate('', xy=(x, y2), xytext=(x, y1),
                arrowprops=dict(arrowstyle='<->', color='#d32f2f', lw=1.2))
    ax.text(x+off, (y1+y2)/2, txt, ha=ha, va='center',
            color='#d32f2f', fontsize=10, weight='bold')

hdim(-L/2, L/2, -4, "L = 200 mm  (chord)")
vdim(0, BASE, -L/2 - 6, "Base\n15 mm", off=-6, ha='right')
vdim(BASE, BASE+SAG, L/2 + 6, "Sagitta\n11.07 mm")
vdim(0, BASE+SAG, L/2 + 40, "Max H\n26.07 mm")

# Edge thickness callout
ax.annotate('Edge thickness = 15 mm', xy=(-L/2+5, BASE/2),
            xytext=(-L/2+25, BASE/2 - 12),
            arrowprops=dict(arrowstyle='->', color='#1565c0'),
            color='#1565c0', fontsize=9)

# Radius arc reference (the full wheel, small fraction)
theta = np.linspace(np.pi/2 - 0.25, np.pi/2 + 0.25, 200)
cx, cz = 0, BASE + SAG - R
ax.plot(R*np.cos(theta) + cx, R*np.sin(theta) + cz, '--', color='#1565c0', lw=0.9, alpha=0.6)
ax.annotate('R = 457.2 mm\n(Ø 36" wheel)', xy=(0, BASE+SAG+1),
            xytext=(60, BASE+SAG+8),
            arrowprops=dict(arrowstyle='->', color='#1565c0'),
            color='#1565c0', fontsize=10, weight='bold')

ax.set_xlim(-L/2 - 35, L/2 + 90)
ax.set_ylim(-22, 45)
ax.set_aspect('equal')
ax.set_title('Radius Platen — true-scale side profile (mm)', fontsize=12, weight='bold')
ax.set_xlabel('mm')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/user/github-pages/platen_profile.png', dpi=160, bbox_inches='tight')
print("Saved: /home/user/github-pages/platen_profile.png")
