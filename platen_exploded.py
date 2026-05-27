"""Exploded view: shows the 4 M5 screws separated from bracket and platen,
plus the 2 OEM bolts coming out of the front plate.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

L, W, TOP = 200.0, 49.0, 15.0
R = 457.2
SAG = R - np.sqrt(R**2 - (L/2)**2)
BASE = TOP - SAG

TOP_LEN, TOP_WID, TOP_THK = 140.0, 49.0, 10.0
FRONT_THK, FRONT_HEIGHT = 10.0, 50.0
GR_BOLT_SPACING = 80.0
PL_DX, PL_DY = 40.0, 15.0

EXPLODE = 35   # mm offset for exploded view

fig = plt.figure(figsize=(13, 9))
ax = fig.add_subplot(111, projection='3d')

def quad(verts, color, alpha=0.92, edge='#263238', lw=0.6):
    p = Poly3DCollection([verts], alpha=alpha, facecolor=color, edgecolor=edge, linewidths=lw)
    ax.add_collection3d(p)

# ---------- Platen (exploded UP by EXPLODE) ----------
PZ = EXPLODE   # platen sits this much higher than nominal
nx, ny = 90, 14
xx = np.linspace(-L/2, L/2, nx)
yy = np.linspace(-W/2, W/2, ny)
X, Y = np.meshgrid(xx, yy)
Zt = PZ + TOP - (R - np.sqrt(R**2 - X**2))
ax.plot_surface(X, Y, Zt, color='#90caf9', edgecolor='#1565c0', linewidth=0.25, alpha=0.92)

xs_fine = np.linspace(-L/2, L/2, 80)
zs_arc  = PZ + TOP - (R - np.sqrt(R**2 - xs_fine**2))
front = [(xx, -W/2, PZ) for xx in xs_fine] + [(xx, -W/2, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(front, '#bbdefb')
back  = [(xx,  W/2, PZ) for xx in xs_fine] + [(xx,  W/2, zz) for xx, zz in zip(xs_fine[::-1], zs_arc[::-1])]
quad(back, '#bbdefb')
for xe in (-L/2, L/2):
    quad([(xe, -W/2, PZ), (xe, W/2, PZ), (xe, W/2, PZ+BASE), (xe, -W/2, PZ+BASE)], '#bbdefb')

# Platen bottom (showing the 4 tapped holes as dark circles)
bottom_face = [(-L/2, -W/2, PZ), (L/2, -W/2, PZ), (L/2, W/2, PZ), (-L/2, W/2, PZ)]
quad(bottom_face, '#90caf9', alpha=0.85)
# Draw the tapped holes (dark)
for dx in (-PL_DX, PL_DX):
    for dy in (-PL_DY, PL_DY):
        theta = np.linspace(0, 2*np.pi, 24)
        circle = [(dx + 2.5*np.cos(t), dy + 2.5*np.sin(t), PZ + 0.05) for t in theta]
        quad(circle, '#0d47a1', alpha=1.0, lw=0.2)

# ---------- 4 screws (between platen and bracket, hovering) ----------
SCREW_Z_BASE = PZ - 15   # heads sit here
for dx in (-PL_DX, PL_DX):
    for dy in (-PL_DY, PL_DY):
        # head
        theta = np.linspace(0, 2*np.pi, 20)
        head_d, head_h = 8.5, 4
        z0, z1 = SCREW_Z_BASE - head_h, SCREW_Z_BASE
        for z in [z0, z1]:
            circ = [(dx + head_d/2*np.cos(t), dy + head_d/2*np.sin(t), z) for t in theta]
            quad(circ, '#424242', alpha=1.0, lw=0.2)
        for i in range(len(theta)-1):
            v = [(dx+head_d/2*np.cos(theta[i]),   dy+head_d/2*np.sin(theta[i]),   z0),
                 (dx+head_d/2*np.cos(theta[i+1]), dy+head_d/2*np.sin(theta[i+1]), z0),
                 (dx+head_d/2*np.cos(theta[i+1]), dy+head_d/2*np.sin(theta[i+1]), z1),
                 (dx+head_d/2*np.cos(theta[i]),   dy+head_d/2*np.sin(theta[i]),   z1)]
            quad(v, '#424242', alpha=1.0, lw=0.15)
        # shaft (upward, into floating platen)
        ax.plot([dx,dx],[dy,dy],[z1, PZ + 5], color='#212121', lw=1.5)

# ---------- Bracket top plate (at z = 0) ----------
bx0, bx1 = -TOP_LEN/2, TOP_LEN/2
by0, by1 = -TOP_WID/2, TOP_WID/2
bz0, bz1 = -TOP_THK, 0
quad([(bx0,by0,bz0),(bx1,by0,bz0),(bx1,by1,bz0),(bx0,by1,bz0)], '#ef5350')
quad([(bx0,by0,bz1),(bx1,by0,bz1),(bx1,by1,bz1),(bx0,by1,bz1)], '#e53935')  # top
quad([(bx0,by0,bz0),(bx1,by0,bz0),(bx1,by0,bz1),(bx0,by0,bz1)], '#e53935')
quad([(bx0,by1,bz0),(bx1,by1,bz0),(bx1,by1,bz1),(bx0,by1,bz1)], '#e53935')
quad([(bx0,by0,bz0),(bx0,by1,bz0),(bx0,by1,bz1),(bx0,by0,bz1)], '#e53935')
quad([(bx1,by0,bz0),(bx1,by1,bz0),(bx1,by1,bz1),(bx1,by0,bz1)], '#e53935')

# Show the 4 through-holes on top face (dark)
for dx in (-PL_DX, PL_DX):
    for dy in (-PL_DY, PL_DY):
        theta = np.linspace(0, 2*np.pi, 24)
        circ = [(dx + 2.75*np.cos(t), dy + 2.75*np.sin(t), bz1 + 0.05) for t in theta]
        quad(circ, '#1b1b1b', alpha=1.0, lw=0.2)

# ---------- Bracket front plate ----------
fy0, fy1 = by0 - FRONT_THK, by0
fz0, fz1 = bz0 - (FRONT_HEIGHT - TOP_THK), bz0
quad([(bx0,fy0,fz0),(bx1,fy0,fz0),(bx1,fy0,fz1),(bx0,fy0,fz1)], '#c62828')
quad([(bx0,fy1,fz0),(bx1,fy1,fz0),(bx1,fy1,fz1),(bx0,fy1,fz1)], '#c62828')
quad([(bx0,fy0,fz0),(bx0,fy1,fz0),(bx0,fy1,fz1),(bx0,fy0,fz1)], '#c62828')
quad([(bx1,fy0,fz0),(bx1,fy1,fz0),(bx1,fy1,fz1),(bx1,fy0,fz1)], '#c62828')
quad([(bx0,fy0,fz0),(bx1,fy0,fz0),(bx1,fy1,fz0),(bx0,fy1,fz0)], '#c62828')

# ---------- 2 OEM bolts (exploded outward in -Y) ----------
BOLT_EXPLODE = 30
for dx in (-GR_BOLT_SPACING/2, GR_BOLT_SPACING/2):
    bz_c = fz0 + 25
    head_d = 16
    y_head = fy0 - BOLT_EXPLODE
    y_back = y_head - 5
    theta = np.linspace(0, 2*np.pi, 24)
    for yv in [y_head, y_back]:
        circ = [(dx + head_d/2*np.cos(t), yv, bz_c + head_d/2*np.sin(t)) for t in theta]
        quad(circ, '#37474f', alpha=1.0, lw=0.2)
    for i in range(len(theta)-1):
        v = [(dx+head_d/2*np.cos(theta[i]),   y_head,  bz_c+head_d/2*np.sin(theta[i])),
             (dx+head_d/2*np.cos(theta[i+1]), y_head,  bz_c+head_d/2*np.sin(theta[i+1])),
             (dx+head_d/2*np.cos(theta[i+1]), y_back,  bz_c+head_d/2*np.sin(theta[i+1])),
             (dx+head_d/2*np.cos(theta[i]),   y_back,  bz_c+head_d/2*np.sin(theta[i]))]
        quad(v, '#37474f', alpha=1.0, lw=0.15)
    # shaft
    ax.plot([dx,dx],[y_head, fy0],[bz_c, bz_c], color='#212121', lw=1.5)

# Labels
ax.text(0,  W/2+15, PZ + TOP + 8, 'RADIUS PLATEN', color='#0d47a1', fontsize=11, weight='bold')
ax.text(-L/2-40, 0, PZ - 12, '4× M5×25 SHCS', color='#212121', fontsize=10, weight='bold')
ax.text(0, W/2+15, -2, 'L-BRACKET (CNC steel)', color='#b71c1c', fontsize=11, weight='bold')
ax.text(0, fy0 - BOLT_EXPLODE - 20, fz0+25, '2× OEM bolts → grinder', color='#37474f', fontsize=10, weight='bold')

ax.set_xlabel('X (mm)'); ax.set_ylabel('Y (mm)'); ax.set_zlabel('Z (mm)')
ax.set_title('Cassette — Exploded View', fontsize=13, weight='bold')
ax.set_box_aspect((L, W*3.5, (TOP + FRONT_HEIGHT + EXPLODE)*1.6))
ax.view_init(elev=18, azim=-62)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/user/github-pages/platen_exploded.png', dpi=160, bbox_inches='tight')
print("Saved: /home/user/github-pages/platen_exploded.png")
