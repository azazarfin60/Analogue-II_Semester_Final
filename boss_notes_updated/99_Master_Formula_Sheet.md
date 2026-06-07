[⬅ 09.1 CMOS Inverter and Logic](09.1_CMOS_Inverter_Logic.md) | [🏠 Index](00-index.md)

---

# Master Formula Sheet
> **Topic:** Course Summary | **Priority:** 🔴 CRITICAL | **Exam Frequency:** Required for all Numericals

## Basic Knowledge: The Math of Electronics

Analog electronics is deeply mathematical. However, you do not need to derive every equation from scratch during the exam. Memorizing the final, simplified formulas allows you to solve complex design problems quickly. 

This sheet compiles every mathematical formula necessary to solve numerical problems and complete standard derivations in ECE 2105: Analog Electronic Circuits II.

---

## 1. Multistage Amplifiers

**Cascaded Amplifiers**
* **Voltage Gain:** $A_v = A_{v1} \times A_{v2} \times A_{v3} \dots$
* **Decibel Gain:** $A_{v(dB)} = 20 \log_{10}|A_v|$
* **Cascaded dB Gain:** $A_{total(dB)} = A_{v1(dB)} + A_{v2(dB)} \dots$

**Darlington Pair**
* **Overall Current Gain:** $\beta_D = \beta_1 \beta_2 + \beta_1 + \beta_2 \approx \beta_1 \beta_2$
* **Input Impedance:** $Z_{in(base)} = \beta_D r_e$
* **Emitter Current:** $I_E = (\beta_D + 1) I_B \approx \beta_D I_B$

**Current Mirrors**
* **Standard Mirror:** $I_C \approx I_{ref} = \frac{V_{CC} - V_{BE}}{R}$
* **Wilson Mirror:** $I_{out} = I_{ref} \cdot \frac{1}{1 + \frac{2}{\beta^2 + \beta}}$

---

## 2. Frequency Response

**Bandwidth Shrinkage (Cascaded Stages)**
* **Low Cutoff ($f_{L}'$):** $f_{L}' = \frac{f_L}{\sqrt{2^{1/n} - 1}}$ (Increases as $n$ increases)
* **High Cutoff ($f_{H}'$):** $f_{H}' = f_H \sqrt{2^{1/n} - 1}$ (Decreases as $n$ increases)

**Miller's Theorem**
* **Input Capacitance:** $C_{in(Miller)} = C_F (1 - A_v)$
* **Output Capacitance:** $C_{out(Miller)} = C_F \left( 1 - \frac{1}{A_v} \right) \approx C_F$

**High-Frequency Cutoff ($f_H$)**
* **Total Input Capacitance:** $C_T = C_{gs} + C_{M_i} = C_{gs} + C_{gd}(1 - A_v)$
* **Upper Cutoff:** $f_H = \frac{1}{2\pi R_{Th} C_T}$ (where $R_{Th} = R_{sig} \parallel R_{in}$)

---

## 3. Feedback Amplifiers

**General Feedback Equation**
* **Closed-Loop Gain:** $A_f = \frac{A}{1 + A\beta}$
* **Loop Gain:** $A\beta$
* **Desensitivity Factor:** $D = 1 + A\beta$

**Voltage-Series Feedback (Non-Inverting)**
* **Gain:** $A_f = \frac{A}{1 + A\beta}$
* **Bandwidth:** $BW_f = BW(1 + A\beta)$ (Bandwidth increases)
* **Input Impedance:** $Z_{if} = Z_i(1 + A\beta)$ (Increases)
* **Output Impedance:** $Z_{of} = \frac{Z_o}{1 + A\beta}$ (Decreases)

**Voltage-Shunt Feedback (Inverting)**
* **Input Impedance:** $Z_{if} = \frac{Z_i}{1 + A\beta}$ (Decreases)
* **Output Impedance:** $Z_{of} = \frac{Z_o}{1 + A\beta}$ (Decreases)

---

## 4. Op-Amp Fundamentals

**Ideal Op-Amp Equations**
* **Virtual Short:** $V_+ = V_-$
* **CMRR:** $\text{CMRR (dB)} = 20\log_{10} \left( \frac{|A_d|}{|A_{cm}|} \right)$
* **Maximum Frequency (Slew Rate limited):** $f_{max} = \frac{SR}{2\pi V_p}$

---

## 5. Mathematical Op-Amp Circuits

**Basic Amplifiers**
* **Inverting Gain:** $A_v = -\frac{R_f}{R_1}$
* **Non-Inverting Gain:** $A_v = 1 + \frac{R_f}{R_1}$

**Analog Computing**
* **Inverting Summer:** $V_{out} = - \left( \frac{R_f}{R_1}V_1 + \frac{R_f}{R_2}V_2 \dots \right)$
* **Integrator:** $V_{out} = -\frac{1}{RC} \int V_{in} dt$
* **Differentiator:** $V_{out} = -RC \frac{d V_{in}}{dt}$

**Specialty Circuits**
* **Logarithmic Amplifier:** $V_{out} = -V_T \ln \left( \frac{V_{in}}{I_s R} \right)$
* **Negative Impedance Converter:** $Z_{in} = -R \left( \frac{R_1}{R_f} \right)$
* **Schmitt Trigger (Thresholds):**
  * $V_{UT} = V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) + V_{sat} \left( \frac{R_1}{R_1 + R_F} \right)$
  * $V_{LT} = V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) - V_{sat} \left( \frac{R_1}{R_1 + R_F} \right)$

---

## 6. Oscillators

**Barkhausen Criterion**
* **Magnitude:** $|A\beta| = 1$
* **Phase:** $\angle A + \angle \beta = 0^\circ \text{ or } 360^\circ$

**RC Phase-Shift Oscillator**
* **Frequency:** $f_o = \frac{1}{2\pi \sqrt{6} RC}$
* **Gain Requirement:** $|A| \ge 29$

**Wien Bridge Oscillator**
* **Frequency:** $f_o = \frac{1}{2\pi RC}$
* **Gain Requirement:** $A \ge 3 \implies R_F \ge 2 R_1$

**LC Oscillators**
* **Colpitts (Split-C):** $f_o = \frac{1}{2\pi \sqrt{L C_{eq}}} \quad \text{where } C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$
* **Hartley (Split-L):** $f_o = \frac{1}{2\pi \sqrt{C L_{eq}}} \quad \text{where } L_{eq} = L_1 + L_2$

---

## 7. 555 Timer

**Astable Mode**
* **Charge Time (HIGH):** $t_H = 0.693 (R_A + R_B) C$
* **Discharge Time (LOW):** $t_L = 0.693 (R_B) C$
* **Frequency:** $f_o = \frac{1.44}{(R_A + 2 R_B) C}$
* **Duty Cycle (No Diode):** $D = \frac{R_A + R_B}{R_A + 2 R_B} \times 100\%$
* **Duty Cycle (With Diode):** $D = \frac{R_A}{R_A + R_B} \times 100\%$

**Monostable Mode**
* **Pulse Width:** $W = 1.0986 RC \approx 1.1 RC$

---

## 8. Active Filters

**Standard Cutoff Frequency**
* $f_c = \frac{1}{2\pi RC}$

**Sallen-Key Equal-Component Topology**
* **Quality Factor:** $Q = \frac{1}{3 - K}$
* **Butterworth Requirement:** $Q = 0.707 \implies K = 1.586$
* **Stability Constraint:** $K < 3$ (If $K \ge 3$, circuit oscillates).

---

[⬅ 09.1 CMOS Inverter and Logic](09.1_CMOS_Inverter_Logic.md) | [🏠 Index](00-index.md)
