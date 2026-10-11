"""Generate the synthetic Sahyadri Motors data set used in Months 3-6."""
import csv, json, os, sys

OUT = sys.argv[1]
os.makedirs(os.path.join(OUT, "docs"), exist_ok=True)

DOCS = [
dict(id="SPEC-E3-001", title="E3 cargo three-wheeler: product specification", type="specification", rev="C", status="released", date="2026-01-20", text="""
The E3 is Sahyadri Motors' electric cargo three-wheeler for urban logistics. It is built at the Chakan plant, at about 1,500 vehicles a month; the Hosur plant builds battery packs and cell modules.

Key figures: rated payload 500 kg, gross vehicle weight 990 kg, top speed 50 km/h, certified range 120 km per charge on the city cycle. The traction motor is a 7 kW peak permanent-magnet motor driving the rear axle through a single-speed differential. The battery pack holds four cell modules of 24 cylindrical 21700 lithium-ion cells each, 96 cells in total, in a sealed enclosure rated IP67.

The vehicle is homologated through ARAI. Any change to the battery, braking, lighting or structure that affects homologation is a Class A change under SOP-ECM-001 and must be reviewed with the homologation team before release.

Design life is 7 years or 150,000 km. Warranty is 3 years or 80,000 km on the vehicle and 5 years or 100,000 km on the battery pack.
"""),
dict(id="DS-FAST-001", title="Fastener torque standard", type="design standard", rev="C", status="released", date="2026-03-02", text="""
This standard sets tightening torques for threaded fasteners on the E3 platform. It replaces revision B. All values are for zinc-flake coated property class 8.8 bolts with a lightly oiled thread, tightened with a calibrated torque wrench.

Main frame joints, M10 (bolt E3-9001 with nut E3-9002): 45 Nm plus or minus 3 Nm.
Motor mount bracket to frame, M10: 50 Nm plus or minus 3 Nm, with medium-strength thread locker (C-0101) applied to the bolt thread.
Battery enclosure lid, M8: 22 Nm plus or minus 2 Nm.
Busbar terminals, M6: 9 Nm plus or minus 1 Nm, followed by a torque stripe.
Rear axle U-bolts, M12: 60 Nm plus or minus 4 Nm, tightened in a cross pattern in two passes.

Torque wrenches must be calibrated at least every 6 months. After the 50 km end-of-line test drive, a 10% sample of main frame and motor mount joints is re-checked; any joint below the lower limit stops the line and is escalated to the quality head.

Change from revision B: the main frame M10 torque was raised from 40 Nm to 45 Nm after joint-slip findings in durability testing.
"""),
dict(id="DS-FAST-001-B", title="Fastener torque standard (revision B, superseded)", type="design standard", rev="B", status="superseded", date="2024-06-10", text="""
This standard sets tightening torques for threaded fasteners on the E3 platform.

Main frame joints, M10: 40 Nm plus or minus 3 Nm.
Motor mount bracket to frame, M10: 50 Nm plus or minus 3 Nm.
Battery enclosure lid, M8: 22 Nm plus or minus 2 Nm.
Busbar terminals, M6: 9 Nm plus or minus 1 Nm.
Rear axle U-bolts, M12: 60 Nm plus or minus 4 Nm.

Torque wrenches must be calibrated at least every 12 months.
"""),
dict(id="WI-ASM-012", title="Work instruction: fit rear axle to main frame", type="work instruction", rev="D", status="released", date="2026-03-15", text="""
Station: chassis line, station 4, Chakan. Takt time 6 minutes. Operators: 2.

Parts: main frame weldment E3-1100, rear axle assembly E3-1300, leaf springs E3-1320 (2), U-bolt kit from fastener kit M-KIT-01.

Step 1. Check the frame weldment carries a green weld inspection tag. Do not fit an axle to an untagged frame.
Step 2. Lift the axle with the station hoist and locate the leaf spring centre bolts in the frame pockets.
Step 3. Fit the U-bolts hand-tight. Tighten in a cross pattern in two passes to the torque in DS-FAST-001 (currently 60 Nm for M12 U-bolts).
Step 4. Apply a yellow torque stripe across each nut and thread.
Step 5. Record the torque wrench ID in the traveller. The wrench must show a calibration label within the last 6 months.

Quality checks: axle square to the frame centre line within 2 mm, measured with the station jig. Any deviation goes to the line leader before the frame moves on.

Safety: wear safety shoes and gloves; never stand under a suspended axle.
"""),
dict(id="WI-BAT-004", title="Work instruction: install battery pack", type="work instruction", rev="B", status="released", date="2025-11-04", text="""
Station: final assembly, station 9, Chakan. Only operators trained and authorised for high-voltage work may perform this task.

PPE: class 0 insulating gloves (tested within the last 6 months), face shield, insulated tools.

Step 1. Verify the battery pack serial number against the vehicle traveller.
Step 2. Measure insulation resistance between each high-voltage terminal and the enclosure at 500 V DC. Minimum acceptable value is 100 megaohms. Reject the pack if any reading is lower and quarantine it with a red tag.
Step 3. Lower the pack into the cradle and fit the enclosure mounting bolts.
Step 4. Connect the busbars and tighten M6 terminals to 9 Nm per DS-FAST-001; apply a torque stripe.
Step 5. Replace the enclosure lid gasket every time the lid is opened. Never reuse a gasket. Tighten the M8 lid bolts to 22 Nm in a cross pattern.
Step 6. Run the battery management board self-test from the end-of-line tester and record the result.

A loose busbar joint can overheat; see FMEA-E3-BAT for the controls.
"""),
dict(id="DS-WELD-002", title="Weld quality standard for frame weldments", type="design standard", rev="A", status="released", date="2025-08-21", text="""
Applies to the main frame weldment E3-1100 and all welded brackets on the E3 platform.

Process: MIG welding with ER70S-6 wire, 1.0 mm, with argon and CO2 shielding gas (82/18).

Acceptance criteria: cracks of any size are not permitted. Visible surface porosity: no single pore larger than 1 mm, and no more than 3 pores in any 100 mm of weld. Undercut no deeper than 0.5 mm. Weld leg length at least the design value shown on the drawing.

Inspection: 100% visual inspection of every frame by a certified inspector, who applies a green tag when the frame passes. In addition, one frame per shift is cut for macro-etch examination of penetration. Results are recorded in the weld quality log.

Frames that fail are tagged red and sent to the repair bay; a repaired weld must be re-inspected by a different inspector.
"""),
dict(id="DS-COAT-003", title="Paint and corrosion protection standard", type="design standard", rev="B", status="released", date="2025-05-30", text="""
Applies to the frame, cargo body panels and cabin shell.

Process sequence: degrease, phosphate, cathodic electro-deposition (CED) primer of 20 to 25 micrometres, then polyester powder top coat of 60 to 80 micrometres. Frames are coated after welding and before assembly.

Requirements: neutral salt spray test of 500 hours with no red rust and creep from scribe below 2 mm. Cross-hatch adhesion class 0 or 1. Film thickness checked on 5 points per part, one part per hour.

Masking: threaded holes and earth points must be masked before CED so that electrical earth continuity is preserved.
"""),
dict(id="SOP-ECM-001", title="Engineering change management procedure", type="procedure", rev="E", status="released", date="2026-02-12", text="""
Purpose: control every change to released parts, drawings, BOMs and documents of the E3 platform.

Flow: anyone may raise an engineering change request (ECR). Design engineering assesses technical feasibility. Manufacturing engineering completes the impact analysis within 5 working days, covering affected parts and assemblies (where-used), plants, open orders and stock, tooling, work instructions and suppliers. The change control board (CCB) meets every Thursday and decides. An approved change is released as an engineering change notice (ECN) with an effectivity date or vehicle serial number.

Change classes:
Class A: affects safety, homologation, regulatory compliance, or form, fit or function seen by the customer. Requires CCB approval and sign-off by the CTO, and homologation review.
Class B: affects form, fit or function internally, cost, or a supplier. Requires CCB approval.
Class C: documentation only, no effect on the physical part. Approved by the design lead.

Interchangeability rule: if the new part is not interchangeable with the old one in every use, it must get a new part number. If it is fully interchangeable, the revision letter is incremented.

Stock disposition must be stated on every ECN: use as is, rework, or scrap. Suppliers must receive released ECNs within 2 working days.
"""),
dict(id="QM-SUP-003", title="Supplier quality manual", type="procedure", rev="D", status="released", date="2025-12-01", text="""
Applies to all suppliers of production parts to Sahyadri Motors.

New parts and changed parts require a production part approval process (PPAP) submission. Level 3 is the default. Safety-critical parts, including cells, battery management boards, brake parts and steering parts, require level 3 plus a run-at-rate audit at the supplier's site.

Suppliers must notify Sahyadri at least 90 days before any change of process, material, sub-supplier or manufacturing location. No change may ship before PPAP approval.

When a non-conformance is raised, the supplier must contain suspect stock within 24 hours, submit root cause analysis within 10 working days, and close the corrective action with an 8D report within 30 days.

Incoming inspection: cells are sampled per lot for open-circuit voltage and internal resistance; any lot with more than 0.1% out of tolerance is rejected in full.
"""),
dict(id="ECN-2026-0131", title="ECN: second source for Li-ion cell E3-3110", type="change notice", rev="-", status="released", date="2026-07-14", text="""
Change: approve VoltCell as a second source for the 21700 Li-ion cell E3-3110, alongside the current supplier CellCo. Reason: supply risk; CellCo lead time has grown to 22 weeks.

Class: A (battery, safety and homologation). Approved by the CCB on 2026-07-09 and by the CTO on 2026-07-11. Homologation team confirmed no re-certification is needed because cell chemistry, format and pack configuration are unchanged.

Affected parts: E3-3110 (revision C to D, interchangeable, so the part number is unchanged), cell module E3-3100 (no change to drawing). Affected documents: approved supplier list, incoming inspection plan.

Validation: thermal and cycle test report TR-2026-012, passed. PPAP level 3 with run-at-rate audit completed at VoltCell.

Effectivity: Hosur plant, from cell module lot 26-M-0450. Stock disposition: use as is (both sources may be used, but never mixed within one module).
"""),
dict(id="ECN-2026-0139", title="ECN: thicker motor mount bracket", type="change notice", rev="-", status="in review", date="2026-09-03", text="""
Change: increase the motor mount bracket plate thickness from 5 mm to 6 mm. Reason: three warranty claims for fatigue cracks at the bracket bend, all on vehicles used above rated payload on rough roads.

Class: B. Status: impact analysis complete, waiting for the CCB on 2026-09-17.

Affected parts: motor mount bracket E3-2400 is replaced by new part E3-2401. The new bracket is not interchangeable, because the thicker plate needs longer bolts, so a new part number is required. Linked change: ECN-2026-0147 replaces the bolts.

Impact found so far: bracket press tool needs new strip layout (tool cost 3.2 lakh rupees); mass increase 0.4 kg per vehicle; work instruction for motor fitting to be updated. 1,150 brackets E3-2400 in stock at Chakan.

Proposed stock disposition: scrap the remaining E3-2400 stock at effectivity. Quality rejected a proposal to use it on low-payload vehicles, because duty cannot be controlled after sale.
"""),
dict(id="ECN-2026-0147", title="ECN: longer bolts for motor mount", type="change notice", rev="-", status="draft", date="2026-09-08", text="""
Change: replace bolt M10x40 (E3-9001) with bolt M10x45 (new part E3-9003) at the motor mount bracket joints only. Main frame joints keep E3-9001.

Reason: the 6 mm motor mount bracket from ECN-2026-0139 needs a longer bolt to keep full thread engagement.

Class: B. Status: draft, to be reviewed together with ECN-2026-0139.

Affected: powertrain assembly E3-2000 (8 bolts per vehicle change from E3-9001 to E3-9003). E3-9001 remains in use on the main frame E3-1100, so it is not obsoleted. The fastener kit M-KIT-01 contents must be updated. Torque stays at 50 Nm per DS-FAST-001.

Open point: the supplier of E3-9001 also quotes E3-9003; PPAP level 3 required.
"""),
dict(id="TR-2026-012", title="Test report: VoltCell 21700 cell qualification", type="test report", rev="-", status="released", date="2026-06-28", text="""
Purpose: qualify VoltCell 21700 cells for the E3 battery pack as a second source.

Tests and results:
Thermal: full pack discharge at 1C in 45 degrees C ambient. Maximum cell temperature 52 degrees C against a limit of 60 degrees C. Pass.
Cycle life: 500 cycles at 25 degrees C, capacity retention 96.8% against a requirement of at least 95%. Pass.
Internal resistance spread within one module: 1.9 milliohms against a limit of 3 milliohms. Pass.
Nail penetration and crush: per AIS-156 requirements, no fire, no explosion. Pass.

Conclusion: VoltCell cells meet all requirements. Mixing VoltCell and CellCo cells within one module is not recommended because their internal resistance curves differ with age.
"""),
dict(id="FMEA-E3-BAT", title="Process FMEA extract: battery pack assembly", type="FMEA", rev="F", status="released", date="2026-01-08", text="""
Failure mode 1: busbar joint under-torqued. Effect: high contact resistance, local overheating, possible thermal event. Severity 9, occurrence 3, detection 4, RPN 108. Controls: torque-controlled nutrunner with recorded torque, torque stripe, thermal imaging of every pack during end-of-line discharge test. Action owner: Hosur manufacturing engineering.

Failure mode 2: enclosure gasket reused or damaged. Effect: water ingress, insulation failure. Severity 8, occurrence 4, detection 5, RPN 160. Controls: gasket replaced on every opening (WI-BAT-004), IP67 leak test on 100% of packs. Recommended action: add gasket presence sensor at lid station, due 2026-12.

Failure mode 3: wrong cell lot mixed in one module. Effect: imbalance, reduced life. Severity 6, occurrence 2, detection 3, RPN 36. Controls: lot scan at module build station; system blocks mixing.
"""),
dict(id="MAINT-PRS-007", title="Maintenance plan: 400 tonne press line, Chakan", type="maintenance plan", rev="C", status="released", date="2025-10-10", text="""
Equipment: 400 tonne mechanical press, line P2, which stamps frame cross members and brackets, including motor mount brackets.

Daily: check lubrication levels, clutch air pressure, and the die clamp indicators.
Weekly: inspect the brake lining wear and clean the bolster.
Monthly: check ram parallelism, maximum deviation 0.1 mm over the bolster.
Every 4,000 operating hours: change the hydraulic overload oil and replace filters.

Condition monitoring: main motor bearing vibration is monitored online. Warning at 4.5 mm/s RMS, alarm at 7.1 mm/s RMS. On alarm, the maintenance manager decides within one shift whether to stop the press.

Spare parts held: clutch friction plates, overload valve, main motor bearing set.
"""),
dict(id="LL-2025-04", title="Lessons learned: harness chafing on frame cross member", type="lessons learned", rev="-", status="released", date="2025-04-22", text="""
Problem: 41 warranty claims in 2024 for intermittent lighting faults. Root cause: the lighting harness E3-6200 rubbed against a sharp edge of the frame cross member E3-1120, wearing through the insulation after about 15,000 km.

Why it was missed: the harness route was only shown in the 3D model and not checked on a physical vehicle before launch; the cross member edge was within drawing tolerance but not deburred.

Fix: grommet added at the cross member pass-through, harness clips at a maximum spacing of 150 mm, and the cross member edge deburred. Implemented through ECN-2025-0088.

Lesson: for every new harness route, run a physical routing check on a prototype and add clip spacing to the work instruction.
"""),
]

PARTS = [
# part_no, description, rev, lifecycle, make_buy, material, mass_kg, unit_cost_inr, supplier
("E3-0000","Electric cargo three-wheeler","C","released","make","",990,0,""),
("E3-1000","Chassis assembly","C","released","make","",182,0,""),
("E3-1100","Main frame weldment","D","released","make","Steel S355",64.0,14200,""),
("E3-1110","Frame long member","C","released","make","Steel S355",18.5,3100,""),
("E3-1120","Frame cross member","D","released","make","Steel S355",3.2,640,""),
("E3-1130","Mounting bracket","B","released","make","Steel S355",0.45,95,""),
("E3-1200","Front suspension","B","released","make","",14.0,0,""),
("E3-1210","Front fork","B","released","buy","",9.8,5200,"Deccan Forge"),
("E3-1220","Shock absorber","A","released","buy","",2.1,1850,"RideTech"),
("E3-1300","Rear axle assembly","C","released","make","",48.0,0,""),
("E3-1310","Axle beam","C","released","make","Steel EN19",31.0,8800,""),
("E3-1320","Leaf spring","B","released","buy","Spring steel",8.4,2300,"Pune Springs"),
("E3-1400","Wheel assembly","B","released","make","",11.5,0,""),
("E3-1410","Rim","A","released","buy","Steel",5.2,1450,"Chakan Wheels"),
("E3-1420","Tyre","A","released","buy","Rubber",6.3,2200,"Kaveri Tyres"),
("E3-2000","Powertrain assembly","C","released","make","",58.0,0,""),
("E3-2100","Traction motor","B","released","buy","",24.0,38500,"Volta Drives"),
("E3-2200","Motor controller","C","released","buy","",4.1,21000,"Volta Drives"),
("E3-2300","Differential","A","released","buy","",17.0,12400,"GearCraft"),
("E3-2400","Motor mount bracket","B","released","make","Steel S355, 5 mm",1.9,420,""),
("E3-2401","Motor mount bracket, 6 mm","A","in work","make","Steel S355, 6 mm",2.1,470,""),
("E3-3000","Battery pack assembly","D","released","make","",62.0,0,""),
("E3-3100","Cell module","C","released","make","",10.5,0,""),
("E3-3110","Li-ion cell 21700","D","released","buy","NMC",0.07,310,"CellCo; VoltCell"),
("E3-3200","Battery management board","C","released","buy","",0.6,9800,"Volta Drives"),
("E3-3300","Battery enclosure","B","released","make","Aluminium 6061",9.5,7400,""),
("E3-3400","Busbar","A","released","buy","Copper",0.12,260,"Nashik Electricals"),
("E3-4000","Cabin assembly","B","released","make","",71.0,0,""),
("E3-4100","Cabin shell","B","released","make","Steel",46.0,11800,""),
("E3-4200","Windshield glass","A","released","buy","Laminated glass",7.5,3400,"ClearView Glass"),
("E3-4300","Driver seat","A","released","buy","",9.0,2900,"SeatCo"),
("E3-4400","Dashboard assembly","B","released","make","",4.2,0,""),
("E3-4410","Instrument cluster","B","released","buy","",0.8,4100,"Volta Drives"),
("E3-5000","Cargo body assembly","B","released","make","",88.0,0,""),
("E3-5100","Cargo floor panel","B","released","make","Steel",34.0,4900,""),
("E3-5200","Cargo side panel","B","released","make","Steel",14.0,2100,""),
("E3-5300","Tail gate","A","released","make","Steel",12.0,1900,""),
("E3-5400","Hinge","A","released","buy","Steel",0.5,120,"Pune Hardware"),
("E3-6000","Electrical harness kit","C","released","make","",7.8,0,""),
("E3-6100","Main wiring harness","C","released","buy","",3.9,6200,"Nashik Electricals"),
("E3-6200","Lighting harness","D","released","buy","",1.4,1800,"Nashik Electricals"),
("E3-6300","Headlamp","A","released","buy","",0.9,1250,"Shivneri Lighting"),
("E3-6400","Tail lamp","A","released","buy","",0.4,560,"Shivneri Lighting"),
("E3-9001","Bolt M10x40","A","released","buy","Steel 8.8",0.04,9,"Pune Hardware"),
("E3-9002","Nut M10","A","released","buy","Steel 8",0.01,3,"Pune Hardware"),
("E3-9003","Bolt M10x45","A","in work","buy","Steel 8.8",0.045,10,"Pune Hardware"),
]

CHANGES = [
# id, title, class, status, affected_parts, reason, owner, created
("ECN-2026-0131","Second source for Li-ion cell","A","released","E3-3110;E3-3100","Supply risk: CellCo lead time 22 weeks","Hosur ME","2026-06-02"),
("ECN-2026-0139","Thicker motor mount bracket","B","in review","E3-2400;E3-2401","Fatigue cracks in 3 warranty claims","Priya Deshmukh","2026-08-20"),
("ECN-2026-0147","Longer bolts for motor mount","B","draft","E3-9001;E3-9003;E3-2000","Thread engagement with 6 mm bracket","Priya Deshmukh","2026-09-08"),
("ECR-2026-0152","LED headlamp to replace halogen headlamp","","new","E3-6300","Customer complaints about night visibility; fleet customer request","Farhan Shaikh","2026-09-29"),
("ECR-2026-0155","Change cargo floor panel to 1.6 mm steel","","new","E3-5100","Cost reduction of 410 rupees per vehicle; weight saving 3.1 kg","Anjali Rao","2026-10-02"),
]

with open(os.path.join(OUT, "docs.json"), "w") as f:
    json.dump([{**d, "text": d["text"].strip()} for d in DOCS], f, indent=1, ensure_ascii=False)
for d in DOCS:
    with open(os.path.join(OUT, "docs", d["id"] + ".md"), "w") as f:
        f.write(f"# {d['id']}: {d['title']}\n\nType: {d['type']} | Revision: {d['rev']} | Status: {d['status']} | Date: {d['date']}\n\n{d['text'].strip()}\n")
STOCK = {"E3-2400": 1150, "E3-2401": 0, "E3-9001": 18000, "E3-9002": 21000, "E3-9003": 0, "E3-6300": 2400,
         "E3-6400": 1900, "E3-5100": 610, "E3-3110": 52000, "E3-6200": 950, "E3-1120": 3100, "E3-4200": 420}
with open(os.path.join(OUT, "parts.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["part_no","description","rev","lifecycle","make_buy","material","mass_kg","unit_cost_inr","supplier","stock_chakan"])
    for p in PARTS:
        w.writerow(list(p) + [STOCK.get(p[0], 0 if p[7] == 0 else 300)])
with open(os.path.join(OUT, "changes.csv"), "w", newline="") as f:
    w = csv.writer(f); w.writerow(["change_id","title","class","status","affected_parts","reason","owner","created"]); w.writerows(CHANGES)
print(len(DOCS), "docs,", len(PARTS), "parts,", len(CHANGES), "changes")
