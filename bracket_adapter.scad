// CNC Steel L-Bracket Adapter for 2x36 Belt Grinder
// Replicates the OEM red platen bracket. Holds either the flat platen
// or the new radius platen (each platen is a separate cassette).
//
//   Top plate:    where platen sits + 4 through-holes for screws from below
//   Front plate:  vertical face, 2 holes for grinder OEM mounting bolts
//
// ALL DIMS PARAMETERIZED — verify the **** GRINDER-FACING **** numbers
// against your actual machine before cutting steel.

// ============ MEASURE THESE ON YOUR GRINDER ============
GR_BOLT_SPACING = 80;   // ★ center-to-center of the 2 visible bolts (mm)
GR_BOLT_DIA     = 8;    // ★ M8 = 8, M6 = 6, 1/4" = 6.35
GR_BOLT_CSK_DIA = 16;   // ★ countersink diameter for flush head (or set 0 for socket cap)
FRONT_HEIGHT    = 50;   // ★ vertical face height (mm)
FRONT_BOLT_Z    = 25;   // ★ height of grinder bolts up from bottom edge
// =======================================================

// Bracket geometry
TOP_LEN   = 140;        // length of top plate (platen overhangs ±30 mm)
TOP_WID   = 49;         // matches platen width
TOP_THK   = 10;         // thickness of horizontal top plate
FRONT_THK = 10;         // thickness of vertical front plate

// Pattern for the 4 screws that bolt platen down (matches platen tapped holes)
PL_DX = 40;
PL_DY = 15;
SCREW_CLR  = 5.5;       // M5 clearance
SCREW_CBORE_D = 9;      // M5 SHCS head ⌀ ~8.5, use 9 for clean drop-in
SCREW_CBORE_H = 5.5;    // counterbore depth (from BOTTOM of top plate)

$fn = 192;

// ---- Build L-bracket ----
difference() {
    union() {
        // Top plate
        translate([-TOP_LEN/2, -TOP_WID/2, 0])
            cube([TOP_LEN, TOP_WID, TOP_THK]);
        // Front plate (vertical, hangs down from rear edge of top plate)
        translate([-TOP_LEN/2, -TOP_WID/2 - FRONT_THK, -FRONT_HEIGHT + TOP_THK])
            cube([TOP_LEN, FRONT_THK, FRONT_HEIGHT]);
        // Optional small fillet/gusset where top meets front (skipped for CNC simplicity)
    }

    // ---- 4 platen mounting holes (clearance + counterbore from BOTTOM) ----
    for (dx = [-PL_DX, PL_DX], dy = [-PL_DY, PL_DY]) {
        translate([dx, dy, -0.01])
            cylinder(h = TOP_THK + 0.02, d = SCREW_CLR);     // through clearance
        translate([dx, dy, -0.01])
            cylinder(h = SCREW_CBORE_H, d = SCREW_CBORE_D);  // bottom counterbore
    }

    // ---- 2 grinder mounting holes through the FRONT plate ----
    for (dx = [-GR_BOLT_SPACING/2, GR_BOLT_SPACING/2]) {
        // Y = through the front plate thickness
        translate([dx, -TOP_WID/2 - FRONT_THK - 0.01, -FRONT_HEIGHT + TOP_THK + FRONT_BOLT_Z])
            rotate([-90, 0, 0])
                cylinder(h = FRONT_THK + 0.02, d = GR_BOLT_DIA);
        // Countersink on the OUTSIDE (grinder-facing side) so heads sit flush
        if (GR_BOLT_CSK_DIA > 0)
            translate([dx, -TOP_WID/2 - FRONT_THK - 0.01, -FRONT_HEIGHT + TOP_THK + FRONT_BOLT_Z])
                rotate([-90, 0, 0])
                    cylinder(h = (GR_BOLT_CSK_DIA - GR_BOLT_DIA)/2 + 0.5,
                             d1 = GR_BOLT_CSK_DIA, d2 = GR_BOLT_DIA);
    }
}
