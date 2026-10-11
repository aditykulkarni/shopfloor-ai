# SOP-ECM-001: Engineering change management procedure

Type: procedure | Revision: E | Status: released | Date: 2026-02-12

Purpose: control every change to released parts, drawings, BOMs and documents of the E3 platform.

Flow: anyone may raise an engineering change request (ECR). Design engineering assesses technical feasibility. Manufacturing engineering completes the impact analysis within 5 working days, covering affected parts and assemblies (where-used), plants, open orders and stock, tooling, work instructions and suppliers. The change control board (CCB) meets every Thursday and decides. An approved change is released as an engineering change notice (ECN) with an effectivity date or vehicle serial number.

Change classes:
Class A: affects safety, homologation, regulatory compliance, or form, fit or function seen by the customer. Requires CCB approval and sign-off by the CTO, and homologation review.
Class B: affects form, fit or function internally, cost, or a supplier. Requires CCB approval.
Class C: documentation only, no effect on the physical part. Approved by the design lead.

Interchangeability rule: if the new part is not interchangeable with the old one in every use, it must get a new part number. If it is fully interchangeable, the revision letter is incremented.

Stock disposition must be stated on every ECN: use as is, rework, or scrap. Suppliers must receive released ECNs within 2 working days.
