# Levitating Knife — Universal Magnetic Puck (v2: smaller, dual-puck default)

A small wall-mounted magnetic knife holder, designed so the wood backing is **invisible behind the knife**. Each knife gets **two tiny Ø18 mm pucks** hidden behind its blade, so the knife looks like it's floating on the wall.

**This is v2.** v1 used a single Ø25 mm puck; v2 shrinks to **Ø18 mm** and defaults to two pucks per knife. Smaller individual footprint, more even support, redundancy if one fails.

See [assembly-diagram.svg](./assembly-diagram.svg) for an exploded view of all three mount options on one page.

---

## TL;DR

- **Universal Ø18 × 12 mm hardwood puck** with a leather face.
- **Single ring-magnet SKU**: N52 12 × 5 × 4 mm. ~2–2.5 kg pull per puck through 2 mm wood + 1 mm leather.
- **Two pucks per knife** is the default (3 for 270 mm+, 4 for the heaviest 300 mm yanagiba).
- Three mounts, **same puck body**: VHB tape, hidden dowel, or M3 screw.
- Hand-tool buildable with Forstner bits.

**Why "most hidden":**
- Ø18 mm fits entirely behind even a 25 mm petty blade. No part of the puck pokes out past the blade silhouette.
- Two small pucks distributed along the spine look less obtrusive than one big block at the heel.
- The dowel mount (B) makes the back panel itself disappear too — only the pucks ever come close to being visible.

---

## Design drawings

All drawings are SVG at 1:1 mm scale. Print with "100% / Actual Size", no "fit to page". Every template has a 50 mm reference bar — **verify with a ruler** before drilling.

| Drawing | Purpose |
|---|---|
| [puck-drawing.svg](./puck-drawing.svg) | Dimensioned multi-view of the puck body (front / side section / back) |
| [puck-drilling-template.svg](./puck-drilling-template.svg) | 1:1 printable template: front pocket + through-hole centers |
| [mount-b-dowel-detail.svg](./mount-b-dowel-detail.svg) | Mount B — back-face 8 mm dowel socket + section |
| [mount-c-screw-detail.svg](./mount-c-screw-detail.svg) | Mount C — back-face 7 mm countersink + section with M3 screw path |
| [wall-panel-drilling-guide.svg](./wall-panel-drilling-guide.svg) | Mount B — grid for laying out multiple puck positions on the back panel |
| [assembly-diagram.svg](./assembly-diagram.svg) | Exploded stack-up for all three mounts |
| [assembly-mount-a-vhb.svg](./assembly-mount-a-vhb.svg) | **3D step-by-step assembly for Mount A (VHB tape)** |
| [assembly-mount-b-dowel.svg](./assembly-mount-b-dowel.svg) | **3D step-by-step assembly for Mount B (hidden dowel)** |
| [assembly-mount-c-screw.svg](./assembly-mount-c-screw.svg) | **3D step-by-step assembly for Mount C (M3 screw)** |

---

## Puck specification

| Property | Value |
|---|---|
| Outer diameter | **18 mm** |
| Thickness | **12 mm** wood + 1 mm leather = **13 mm** installed |
| Front magnet pocket | 12 mm Ø × 5 mm deep (drilled from front) |
| Front wall (wood between magnet and knife) | 2 mm |
| Center through-hole | 4 mm Ø (full depth) |
| Front facing | 1 mm veg-tan leather disc, Ø18 mm, contact-cemented |
| Wood species | Walnut, white oak, maple, or any dense hardwood |

**Magnet (single SKU, enables all three mounts):**
N52 neodymium **ring magnet**, **12 mm OD × 5 mm thick × 4 mm ID**, axially magnetized, Ni-Cu-Ni plated.
Raw pull on thick steel ≈ 3–3.5 kg. Real pull through 2 mm wood + 1 mm leather onto a typical ~2 mm knife blade ≈ **2–2.5 kg per puck**.

### Stacking guide (how many pucks per knife — default is 2)

| Knife class | Examples | Pucks |
|---|---|---|
| Light paring / petty | petty 120 mm, small utility | 1 (or 2 for symmetry) |
| Standard daily | nakiri 165, santoku 180, gyuto 180–240, deba 165 | **2** |
| Large | gyuto 270, sujihiki 240–270 | 3 |
| Heavy / long | gyuto 300, sujihiki 300, yanagiba 270–300, deba 210 | 4 |

Space pucks along the spine/heel side of the blade, **30–50 mm apart**, roughly centered on the blade's length. First puck ~25 mm below the bolster.

---

## Materials (per puck unless noted)

| Item | Spec | Qty |
|---|---|---|
| Hardwood blank | Ø18 mm × 12 mm (or 18×18×12 mm offcut to be rounded) | 1 |
| N52 ring magnet | 12 mm OD × 5 mm × 4 mm ID, Ni-plated | 1 |
| Leather disc | Ø18 mm, ~1 mm thick veg-tan | 1 |
| 5-min epoxy | 2-part | ~0.5 ml |
| Contact cement | | ~0.3 ml |

**Plus, per chosen mount:**

| Mount | Additional materials |
|---|---|
| A. VHB | 15 × 15 mm square of 3M VHB 4941 (or equivalent 1 mm acrylic foam tape) |
| B. Dowel | 8 mm hardwood dowel × 10 mm long; wood glue; a shared wall panel (min 15 mm hardwood/ply) |
| C. Screw | M3 × 25 mm countersunk stainless wood screw; plastic wall anchor for drywall |

---

## Tools

Core (all builds):
- 12 mm Forstner bit
- 4 mm twist bit (through-hole)
- Drill press (strongly preferred) or hand drill with depth collar
- 18 mm hole saw **or** a file/rasp to round 18 × 18 mm stock
- Bench vise / clamp
- Utility knife (leather)
- Sandpaper 120 / 220 / 400

Per mount:
- Mount B: 8 mm Forstner or brad-point bit
- Mount C: 7 mm Forstner bit, Phillips or Torx driver (matching the M3 screw head)

Optional: danish oil or wax for finishing the wood before leather is glued on.

---

## Assembly — puck body (common to all three mounts)

1. **Prepare the blank.** Start with a Ø18 mm × 12 mm hardwood disc. If you only have square stock, clamp an 18 × 18 × 12 mm blank in a vise, mark the center on both faces, and round with an 18 mm hole saw (use a sacrificial board) or file/rasp + sandpaper.
2. **Mark centers.** On both the front and back faces, mark dead center with a punch — use the [puck-drilling-template.svg](./puck-drilling-template.svg) if you want a printed guide.
3. **Drill the through-hole first.** With a 4 mm twist bit, drill straight through from the front. This gives every later drill a natural pilot and keeps concentricity.
4. **Drill the magnet pocket.** With a 12 mm Forstner bit from the front face, drill **5 mm deep**. A depth collar or piece of tape on the bit shaft prevents going too deep. You should be left with 2 mm of wood between the pocket floor and the front face — that front wall is critical for pull strength; don't make it thinner.
5. **Test-fit the magnet.** The N52 ring magnet should drop in with slight wiggle room. If it's tight, do not force it — sand the pocket wall with a rolled bit of 220 paper.
6. **Epoxy the magnet in.** Mix a drop of 5-min epoxy, apply a thin film to the magnet's edge and the pocket side wall, press in so the magnet sits flush or 0.1 mm below the wood's front rim. Wipe squeeze-out with a toothpick. Let cure 30 min.
7. **Finish the wood (optional).** Light sand to 400 grit, one wipe of danish oil on the outer cylinder and back face. Keep oil **out of the magnet pocket rim** — it can interfere with leather glue-up.
8. **Glue the leather face.** Cut a Ø18 mm disc from 1 mm veg-tan leather (an 18 mm hole punch or a knife around a coin works). Contact-cement both the leather back and the puck's front face, let tack off 3–5 min, press together firmly with a clamp or heavy book for 10 min. Trim any overhang with a sharp blade.

The puck body is now complete. Build a second one — you'll be using them in pairs. Then pick a mount.

---

## Mount A — VHB tape (easiest, low commitment)

Best for: smooth painted drywall, tile, glass splashbacks, cabinet sides.
Worst for: textured paint, wallpaper, flaky surfaces.

1. Clean both surfaces (puck back + wall spot) with isopropyl alcohol. Let dry.
2. Cut a ~15 × 15 mm square of 3M VHB 4941. Peel one liner, stick to the back of the puck (centered — the 4 mm hole is irrelevant; VHB bridges it fine).
3. Peel the second liner, press the puck onto the wall. **Press hard for 20 seconds.** VHB develops ~50% strength in 20 min, full strength in 72 h.
4. Repeat for the second puck of the pair, ~30–50 mm above the first along the blade's spine line.
5. Wait 24 h before hanging a knife. Then test with a knife *that you don't mind dropping* before trusting it with your good blade.

If a puck pops off within 24 h, the wall surface is unsuitable — switch to Mount C.

---

## Mount B — Hidden wood panel with dowels (cleanest "levitating" look)

This is the design from the original sketches. The wall panel is whatever shape and wood you like — it becomes a subtle feature strip. Pucks friction-fit onto short dowels glued into the panel, so there's nothing visible on the front of the panel except the pucks (which themselves disappear behind the knives).

**Wall panel prep:**

1. Cut the back panel — minimum 15 mm thick hardwood or good-quality plywood. Size and shape per your knife layout.
2. Plan the puck positions. Each knife takes 2–4 pucks along the blade's spine, 30–50 mm apart. See [wall-panel-drilling-guide.svg](./wall-panel-drilling-guide.svg).
3. Drill 8 mm dowel holes in the panel, **5–7 mm deep**. Use a drill press and depth stop.
4. Mount the panel to the wall — French cleat, construction adhesive (for permanent), or screws through the panel into studs.

**Puck back prep (Mount B):**

1. On the back face of the completed puck, drill an **8 mm Ø × 5 mm deep** Forstner pocket, centered (the pilot of the Forstner lands in the 4 mm through-hole you drilled in step 3 of the puck assembly).
2. Light sand the inside of this socket — it should be a **firm friction fit** on the dowel, requiring ~1–2 kg of pull to remove.

**Assemble:**

1. Cut 8 mm dowels into 10 mm lengths.
2. Glue each dowel into its wall-panel hole with wood glue. Leave ~5 mm projecting.
3. Let glue cure overnight.
4. Press each puck onto its dowel. Done.

If the fit is loose, dip the dowel in glue before the puck — they become permanent but still discreet. If too tight, sand a thou off the dowel.

---

## Mount C — M3 screw (most secure)

Best for: rental walls where you're okay with two tiny screw holes per knife; situations where VHB is unreliable; users who want zero worry.

**Puck back prep (Mount C):**

1. On the back face, drill a **7 mm Ø × 1.5 mm deep countersink** with a 7 mm Forstner, centered on the existing 4 mm through-hole. This recess catches the screw head flush with the back surface.
2. Dry-fit an M3 × 25 mm countersunk wood screw through the puck: the head should sit flush with the back face, the shaft should extend ~14 mm past the back. If the head sits proud, deepen the countersink 0.3 mm at a time.

**Install:**

1. Mark the wall at each puck's position (2 marks per knife, 30–50 mm apart along the blade line).
2. **If hitting drywall only:** pre-drill a 4 mm hole, push in a plastic expansion anchor rated for M3.
   **If hitting a stud or wood panel:** pre-drill a 2.5 mm pilot hole.
3. Feed the screw through the puck (head seated in the countersink, shaft protruding through the magnet's 4 mm bore — steel in the magnetic circuit actually boosts the pull slightly).
4. Drive the screw in until the puck is snug against the wall. **Do not overtighten** — the wood around the countersink will crack. Stop at "firm, no wobble".

If the puck spins freely when you try to tighten it, the anchor has failed — remove, step up anchor size, or relocate to a stud.

---

## Safety notes

- **N52 magnets pinch hard.** Even these small 12×5 mm rings can bite skin between themselves or with ferrous steel. Keep loose pucks separated by ≥30 mm in storage.
- **Pacemakers / implanted electronics:** keep pucks >20 cm from these devices.
- **Children:** swallowed neodymium magnets are a medical emergency. Treat loose magnets like button batteries — out of reach.
- **Knife retention is passive.** Earthquake, heavy door slam, or a knife bumped hard may dislodge a blade. Don't mount over a baby's crib, dining chair, or pet bed.
- **Test every build** with a cheap knife before trusting the puck(s) with an expensive blade.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Knife slides down slowly | Not enough magnet per knife weight | Add a third puck along the spine |
| Knife falls off immediately | Front wall too thick (>3 mm), or leather too thick | Sand front face thinner, or replace leather with 0.5 mm |
| Blade gets scratched over time | Leather worn through | Replace leather disc |
| VHB puck pops off wall | Surface not clean / textured / flaky paint | Clean with IPA and retry; if still failing, switch to Mount C |
| Dowel puck pulls off with the knife | Friction fit too loose | Dip dowel in wood glue before pressing puck on |
| Screw puck spins when tightening | Wall anchor stripped or missing | Pull out, install larger anchor, or relocate to a stud |
| Puck cracks when tightening screw | Overtightened, or wood grain weak | Back off ¼ turn; cracked pucks still work — epoxy fix |
| Magnet pops out of pocket | Epoxy failure or pocket oversized | Re-epoxy with thin shim of paper around magnet edge |

---

## Why dual-puck Ø18 instead of single Ø25

- A Ø25 puck peeks past the silhouette of any blade narrower than ~30 mm at the bolster — visible on petty knives and even some narrower nakiris/sujihikis.
- Ø18 fits behind every blade in your set, including a 25 mm petty.
- Two pucks distribute the load: lighter shear stress on each magnet/VHB pad, lower chance of "blade rotation" if the knife is bumped.
- Two failure points: if one VHB pad slowly loses bond, the other still catches the knife.
- Per-puck magnet is smaller (12 × 5 ring vs 20 × 5 ring), but the **sum** of two 12×5 rings has comparable total pull to a single 20×5 ring, while spreading it more usefully.

---

## Design files

Source of truth for geometry:

- [puck-drawing.svg](./puck-drawing.svg) — master dimensioned drawing
- [puck-drilling-template.svg](./puck-drilling-template.svg) — print this, stick on the blank, punch the centers
- [mount-b-dowel-detail.svg](./mount-b-dowel-detail.svg)
- [mount-c-screw-detail.svg](./mount-c-screw-detail.svg)
- [wall-panel-drilling-guide.svg](./wall-panel-drilling-guide.svg)
- [assembly-diagram.svg](./assembly-diagram.svg)
- [assembly-mount-a-vhb.svg](./assembly-mount-a-vhb.svg)
- [assembly-mount-b-dowel.svg](./assembly-mount-b-dowel.svg)
- [assembly-mount-c-screw.svg](./assembly-mount-c-screw.svg)
