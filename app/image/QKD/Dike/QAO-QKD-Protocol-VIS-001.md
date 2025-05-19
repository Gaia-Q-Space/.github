

## QKD Protocol (BB84): DIKE-Class Visual Flowchart

Here is a **fully self-contained, render-safe SVG** for your QKD (BB84) protocol as a DIKE-class diagram—**with no external image references, pure SVG only**. You can copy-paste this into your repo, and it should render correctly in GitHub and Markdown previews.

<div align="center">

```svg
<svg width="680" height="370" viewBox="0 0 680 370" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title { font: bold 22px sans-serif; fill: #34495e }
    .subtitle { font: 15px sans-serif; fill: #2980b9 }
    .box { fill: #eaf6fb; stroke: #2980b9; stroke-width:2 }
    .box2 { fill: #f8f8fa; stroke: #5d6d7e; stroke-width:2 }
    .arrow { stroke: #34495e; stroke-width:2; marker-end:url(#arrowhead) }
    .label { font: 13px sans-serif; fill: #273746 }
    .note { font: italic 11px sans-serif; fill: #7d8a96 }
    .dike { font: bold 11px sans-serif; fill: #17a589 }
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" 
      refX="10" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#34495e"/>
    </marker>
  </defs>
  <!-- Title -->
  <text x="180" y="35" class="title">QKD Protocol (BB84): DIKE-Class Visual Flowchart</text>
  <text x="200" y="60" class="subtitle">GAIA-Q-SPACE · DIKE ID: DIKE-QSPACE-QKD-0001</text>
  <!-- Alice -->
  <rect x="40" y="110" width="110" height="60" rx="8" class="box"/>
  <text x="55" y="135" class="label">Alice (Sender)</text>
  <text x="48" y="155" class="note">Generates random bits & bases</text>
  <!-- Quantum Channel Arrow -->
  <line x1="150" y1="140" x2="240" y2="140" class="arrow"/>
  <text x="160" y="132" class="label">Quantum Channel</text>
  <!-- Bob -->
  <rect x="240" y="110" width="110" height="60" rx="8" class="box"/>
  <text x="265" y="135" class="label">Bob (Receiver)</text>
  <text x="250" y="155" class="note">Measures incoming photons</text>
  <!-- Sifting Process -->
  <rect x="390" y="110" width="110" height="60" rx="8" class="box2"/>
  <text x="410" y="135" class="label">Basis Sifting</text>
  <text x="395" y="155" class="note">Compare bases over public channel</text>
  <!-- Error Correction -->
  <rect x="540" y="110" width="110" height="60" rx="8" class="box2"/>
  <text x="555" y="135" class="label">Error Correction</text>
  <text x="545" y="155" class="note">Classical communication, correct errors</text>
  <!-- Arrows between steps -->
  <line x1="350" y1="140" x2="390" y2="140" class="arrow"/>
  <line x1="500" y1="140" x2="540" y2="140" class="arrow"/>
  <!-- Final Key Generation -->
  <rect x="240" y="240" width="410" height="60" rx="8" class="box"/>
  <text x="260" y="265" class="label">Final Secret Key Generation</text>
  <text x="250" y="285" class="note">Shared bits after error correction, privacy amplification</text>
  <!-- Arrow down from Error Correction -->
  <line x1="595" y1="170" x2="595" y2="240" class="arrow"/>
  <!-- DIKE Traceability Field -->
  <rect x="40" y="240" width="170" height="60" rx="8" class="box2"/>
  <text x="50" y="265" class="dike">DIKE Traceability</text>
  <text x="50" y="285" class="note">Epistemic, operational, ethical log</text>
  <!-- Arrows from Sifting to DIKE and to Key Gen -->
  <line x1="445" y1="170" x2="445" y2="240" class="arrow"/>
  <line x1="110" y1="170" x2="110" y2="240" class="arrow"/>
  <!-- Legend -->
  <rect x="40" y="330" width="610" height="30" rx="8" fill="#f9f9fa" stroke="#bfc9d1" stroke-width="1"/>
  <text x="50" y="350" class="note">
    Legend: | Blue = Quantum Steps | Gray = Classical Steps | Green = DIKE Metadata | All transitions are traceable.
  </text>
</svg>
```

</div>

---

### Diagram Overview

This SVG visualization illustrates a DIKE-Class visual flowchart for the BB84 Quantum Key Distribution (QKD) protocol, tailored for GAIA-Q-SPACE, and highlights:

- **Title and Subtitle**
  - **Title:** QKD Protocol (BB84): DIKE-Class Visual Flowchart
  - **Subtitle:** GAIA-Q-SPACE · DIKE ID: DIKE-QSPACE-QKD-0001

- **Actors**
  - **Alice (Sender):** Generates random bits and bases (quantum step, blue box).
  - **Bob (Receiver):** Measures incoming photons (quantum step, blue box).

- **Processes**
  - **Quantum Channel:** Key transfer medium (quantum).
  - **Basis Sifting:** Compare bases over public channel (classical, gray box).
  - **Error Correction:** Correct errors via classical communication (gray box).
  - **Final Secret Key Generation:** After error correction and privacy amplification.

- **DIKE Traceability**
  - Dedicated for epistemic, operational, and ethical logs, supporting DIKE principles.

- **Transitions**
  - Arrowed lines show the sequence and auditability of all steps.

- **Legend**
  - **Blue:** Quantum Steps
  - **Gray:** Classical Steps
  - **Green:** DIKE Metadata
  - **All transitions are traceable**

---

**This flowchart provides a comprehensive, ethical, and operational visualization of QKD, emphasizing traceability and DIKE compliance for advanced quantum communication systems.**

---

> _Tip: You can embed this SVG block directly in your Markdown for full GitHub and Markdown preview compatibility._
