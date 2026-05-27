// Radius Platen — 36" wheel profile, with 4 blind tapped holes
// for mounting to a CNC steel L-bracket adapter from below.
//
// Spec:
//   Platen 200 × 49 × 15 mm (max H at center crown)
//   Edge thickness:   3.93 mm
//   Sagitta:         11.07 mm
//   Top arc R:      457.2 mm  (= 36"/2)
//   4× M5 blind tapped holes, 8 mm deep, in the thick center region
//   Hole pattern: ±40 mm along length × ±15 mm across width
//
// Material: 4140, mild steel, or 6061 aluminum.

L           = 200;      // platen length (mm)
W           = 49;       // platen width  (mm)
TOP         = 15;       // total max height at center (mm)
R           = 457.2;    // wheel radius = 36"/2

// Mounting hole pattern (bottom of platen, blind tapped)
HOLE_DX     = 40;       // half-spacing along length  -> 80 mm pitch
HOLE_DY     = 15;       // half-spacing across width  -> 30 mm pitch
TAP_DRILL   = 4.2;      // M5 tap drill ⌀ (use M5 tap after machining)
TAP_DEPTH   = 9;        // blind tap depth (mm)

$fn = 256;

SAG  = R - sqrt(R*R - (L/2)*(L/2));   // 11.07
BASE = TOP - SAG;                      // 3.93

echo(str("Sagitta:        ", SAG,  " mm"));
echo(str("Edge thickness: ", BASE, " mm"));
echo(str("Total max H:    ", TOP,  " mm"));
// Sanity check thickness at each hole location
for (dx = [-HOLE_DX, HOLE_DX])
    echo(str("Platen thickness at x=", dx, ": ",
             TOP - (R - sqrt(R*R - dx*dx)), " mm"));

difference() {
    // Solid block sized to total max height
    translate([-L/2, -W/2, 0])
        cube([L, W, TOP]);

    // Carve the convex top arc by subtracting the wheel cylinder
    // positioned above with its low point at z = TOP
    translate([0, 0, TOP + R - SAG])
        rotate([90, 0, 0])
            cylinder(h = W + 20, r = R, center = true);

    // 4 blind tap-drill holes from the BOTTOM (will be tapped M5 by hand)
    for (dx = [-HOLE_DX, HOLE_DX], dy = [-HOLE_DY, HOLE_DY])
        translate([dx, dy, -0.01])
            cylinder(h = TAP_DEPTH, d = TAP_DRILL);
}
