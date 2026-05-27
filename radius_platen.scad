// Radius Platen — 36" wheel profile
// Length 200 mm × Width 49 mm × Base 15 mm
// Total max height (crown): 26.07 mm
//
// Render: F6 in OpenSCAD, then File > Export > STL for printing/CAM.

L     = 200;        // length along belt travel (mm)
W     = 49;         // width across belt (mm)
BASE  = 15;         // flat base thickness (mm)
R     = 457.2;      // wheel radius = 36"/2 = 18" = 457.2 mm
$fn   = 256;        // smoothness

SAG   = R - sqrt(R*R - (L/2)*(L/2));   // ≈ 11.07 mm
TOP   = BASE + SAG;                     // ≈ 26.07 mm
echo(str("Sagitta = ", SAG, " mm"));
echo(str("Total max height = ", TOP, " mm"));

// Subtractive approach: solid block, then carve the cylinder out of the top.
difference() {
    // Block sized to total max height
    translate([-L/2, -W/2, 0])
        cube([L, W, TOP]);

    // Wheel cylinder positioned so its lowest point sits at z = TOP
    // (i.e. carves a Ø36" concave-into-the-block... but we want CONVEX top)
    // So instead, position cylinder center ABOVE the block by R so it
    // removes everything above the arc — leaving a convex crown.
    translate([0, 0, TOP + R - SAG])   // center at z = TOP + R - SAG  => bottom of cyl at TOP - SAG = BASE
        rotate([90, 0, 0])
            cylinder(h = W + 10, r = R, center = true);
}

// --- Optional: mounting holes (uncomment + tune to your grinder) ---
// MOUNT_HOLE_D = 6.2;      // M6 clearance
// MOUNT_SPACING = 60;      // distance between holes along length
// for (x = [-MOUNT_SPACING/2, MOUNT_SPACING/2])
//     translate([x, 0, -0.1])
//         cylinder(h = BASE + 0.2, d = MOUNT_HOLE_D);
