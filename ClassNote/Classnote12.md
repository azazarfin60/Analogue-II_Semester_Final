# Class Note Digitization - Phase 12 (Part 2, Page 54)

---

## Page 54: Analog_Class_Note_Part-2-054.png

### Content

#### 1. Inverting Summing Amplifier Design Problem
* **Question:** Design an op-amp circuit to implement the logic:
  $$v_o = -2 V_1 - 3 V_2$$
  Determine the feedback resistor $R_f$ and input resistors $R_1, R_2$.

#### Circuit Schematic:
```
           R1
  V1 -----[===]-----*---- (-) \
           R2       |          \
  V2 -----[===]-----*     [Rf]  \------- Output (v_o)
                    |  +--[===]-/
                   === |  |    /
                   GND | ===
                       | GND
                       +--+
```

#### Calculations:
We know the closed-loop output voltage of an inverting summing amplifier is:
$$v_o = -\left( \frac{R_f}{R_1} V_1 + \frac{R_f}{R_2} V_2 \right)$$
By comparing this with the required equation $v_o = -2 V_1 - 3 V_2$:
$$\frac{R_f}{R_1} = 2 \Rightarrow R_1 = \frac{R_f}{2}$$
$$\frac{R_f}{R_2} = 3 \Rightarrow R_2 = \frac{R_f}{3}$$
* **Component Design Choice:** Let $R_f = 6\text{ k}\Omega$:
  * $R_1 = \frac{6\text{ k}\Omega}{2} = 3\text{ k}\Omega$
  * $R_2 = \frac{6\text{ k}\Omega}{3} = 2\text{ k}\Omega$

---

#### 2. Important Advanced Op-Amp Application Topics (Self-Study):
* **Precision Rectifier Circuits**
* **Negative Impedance Converters (NIC)**
* *(Note in manuscript: These topics are mandatory reading for the final exam).*

---

#### 3. Semester Final Exam Structure & Syllabus Breakdown:
* **Active Filters & Frequency Response:** 1 full question set.
* **CT (Coupling/Tuned Amplifiers):** 2 full question sets.
* **Feedback Amplifiers:** 1 full question set.
* **Basic Op-Amp Principles:** 1 full question set.
* **555 Timer Circuits:** 1 full question set.
* **Oscillator Circuits:** 1 full question set.
* **Op-Amp Practical Applications:** 1 full question set.
