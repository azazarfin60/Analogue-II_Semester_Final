# 📝 RUET 2024 Odd Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2105)

---

## SECTION - A

### Q.1
**(a) Why is a high output impedance desirable for some specific amplifier networks? [02 Marks]**
**Answer:**
A high output impedance is highly desirable in **Current Amplifiers** or **Transconductance Amplifiers**. According to Norton's theorem, an ideal current source has an infinite internal parallel resistance (output impedance). A high output impedance ensures that the amplifier acts as a stiff, constant current source, forcing the entirety of its amplified output current completely into the load, regardless of how the load resistance fluctuates.

**(b) Calculate $Z_i, Z_o, A_v$, and $v_o(t)$ for the cascaded JFET-BJT amplifier. [05 Marks]**
**Solution:**
**(Referencing identically biased circuit from 2023 Q.1(b)):**
*   **Stage 1 (JFET CS):** $V_{GSQ} = -1.89\text{ V}$, $g_m = 2.64\text{ mS}$. Input impedance $Z_{in1} = 3.3\text{ M}\Omega$.
*   **Stage 2 (BJT CE):** $I_{EQ} = 4.0\text{ mA}$, $r_e = 6.5\ \Omega$. Input impedance $Z_{in2} = 953\ \Omega$.
*   **Gains:**
    $$
    A_{v1} = -g_m (R_D \parallel Z_{in2}) = -2.64\text{ mS} \times (2.4\text{k} \parallel 0.953\text{k}) = -1.8
    $$
    $$
    A_{v2} = -\frac{R_C}{r_e} = -\frac{2200}{6.5} = -338.5
    $$
    $$
    A_v = A_{v1} \times A_{v2} = (-1.8) \times (-338.5) = 609.3
    $$
*   **Impedances:**
    $$
    Z_i = Z_{in1} = R_G = 3.3\text{ M}\Omega
    $$
    $$
    Z_o = R_C = 2.2\text{ k}\Omega
    $$
*   **Output Voltage Waveform:**
    $$
    v_o(t) = A_v \cdot v_i(t) = 609.3 \times 1\sin(\omega t)\text{ mV} = 609.3\sin(\omega t)\text{ mV} = 0.609\sin(\omega t)\text{ V}
    $$

**(c) Calculate DC bias for the NPN-PNP complementary push-pull emitter follower. [03 Marks]**
**Answer:**
In a standard Class B complementary symmetry push-pull amplifier, the quiescent DC current is exactly zero to maximize efficiency.
To set the DC output voltage to exactly half the supply ($V_o = V_{CC}/2 = 9\text{V}$), the inputs (bases) must be biased at exactly $0\text{V}$ relative to the output if no diodes are used, creating a deadband. Since there is no signal and both transistors are identical, the DC midpoint naturally settles at $9\text{V}$ when driving a coupled load.
*   **Quiescent Collector Currents:** $I_{CQ1} = 0\text{ A}$, $I_{CQ2} = 0\text{ A}$.
*   **Quiescent Base Currents:** $I_{BQ1} = 0\text{ A}$, $I_{BQ2} = 0\text{ A}$.
*   **Collector-Emitter Voltages:**
    $$
    V_{CEQ1} = V_{CC} - V_o = 18\text{V} - 9\text{V} = 9\text{V}
    $$
    $$
    V_{CEQ2} = 0\text{V} - V_o = 0\text{V} - 9\text{V} = -9\text{V}
    $$
*(Note: True Class AB biasing requires compensating diodes to overcome the $V_{BE}$ drops, which are absent here, making it a pure Class B configuration).*

---

### Q.2
**(a) Engineering benefit of Darlington connection and proof of $\beta_d \approx \beta_1 \beta_2$. [04 Marks]**
**Answer:**
*   **Benefit:** It provides a monumental overall current gain and an extraordinarily high input impedance, allowing extremely weak signals to drive heavy power loads (e.g., motors or speakers).
*   **Proof:** The emitter current of $Q_1$ is $I_{E1} = (\beta_1 + 1) I_{B1}$. This current is fed directly into the base of $Q_2$, so $I_{B2} = I_{E1}$. The total output emitter current is $I_{E2} = (\beta_2 + 1) I_{B2}$.
    Substituting $I_{B2}$:
    $$
    I_o = I_{E2} = (\beta_2 + 1)(\beta_1 + 1) I_{B1}
    $$
    Since $\beta_1, \beta_2 \gg 1$:
    $$
    I_o \approx (\beta_1 \beta_2) I_{B1} \Rightarrow \beta_D = \frac{I_o}{I_{B1}} \approx \beta_1 \beta_2
    $$

**(b) Calculate $Z_i, A_i, A_v$ for the Darlington Common-Emitter configuration. [04 Marks]**
**Solution:**
**1. DC Biasing:**
$V_{CC} = 27\text{V}$. $\beta_1 = \beta_2 = 110$. Composite $\beta_D \approx 12100$.
$$
V_{B1} = 27\text{ V} \times \frac{220\text{ k}\Omega}{470\text{ k}\Omega + 220\text{ k}\Omega} = 8.6\text{ V}
$$
$$
R_{th} = 470\text{k} \parallel 220\text{k} = 149.8\text{ k}\Omega
$$
$$
I_{E2} = \frac{V_{B1} - 1.4\text{ V}}{R_E + R_{th}/\beta_D} = \frac{8.6 - 1.4}{680 + 149800/12100} = \frac{7.2\text{ V}}{680 + 12.4} = 10.4\text{ mA}
$$
$$
r_{e2} = \frac{26\text{ mV}}{10.4\text{ mA}} = 2.5\ \Omega
$$
$$
I_{E1} = \frac{I_{E2}}{\beta_2} = \frac{10.4\text{ mA}}{110} = 94.5\ \mu\text{A} \Rightarrow r_{e1} = \frac{26\text{ mV}}{94.5\ \mu\text{A}} = 275\ \Omega
$$

**2. AC Parameters:**
The emitter is fully bypassed by $C_E$ ($R_E$ is shorted to AC ground). The output is taken from the collector ($R_C = 1.2\text{ k}\Omega$).
*   **Input Impedance ($Z_i$):**
    $$
    Z_{base} = \beta_1 r_{e1} + \beta_1 \beta_2 r_{e2} \approx \beta_D r_{e2} = 12100 \times 2.5\ \Omega = 30.25\text{ k}\Omega
    $$
    $$
    Z_i = R_{th} \parallel Z_{base} = 149.8\text{ k}\Omega \parallel 30.25\text{ k}\Omega = 25.1\text{ k}\Omega
    $$
*   **Voltage Gain ($A_v$):**
    $$
    A_v = -\frac{R_C}{r_{e2} + r_{e1}/\beta_2} = -\frac{1200\ \Omega}{2.5\ \Omega + 2.5\ \Omega} = -\frac{1200}{5} = -240
    $$
*   **Current Gain ($A_i$):**
    $$
    A_i = \frac{i_o}{i_{in}} = A_v \left( \frac{Z_i}{R_C} \right) = -240 \times \left( \frac{25100\ \Omega}{1200\ \Omega} \right) = -5020
    $$

**(c) Physical effect of the number of stages on cutoff frequencies and bandwidth. [02 Marks]**
*(Identical to 2021 Q.2(a). Lower cutoff shifts higher, upper cutoff shifts lower, resulting in significant bandwidth shrinkage).*

---

### Q.3
**(a) Explain current-mirror functions and prove $I_{B1} = I_{control}/(\beta_1 + 2)$. [04/05 Marks]**
**Proof:**
Applying KCL at the collector node of the reference transistor $Q_1$:
$$
I_{control} = I_{C1} + I_{B(total)}
$$
Since $Q_1$ and $Q_2$ are matched, $I_{B1} = I_{B2}$, so $I_{B(total)} = 2 I_{B1}$.
Using the fundamental relation $I_{C1} = \beta_1 I_{B1}$:
$$
I_{control} = \beta_1 I_{B1} + 2 I_{B1} = I_{B1} (\beta_1 + 2)
$$
$$
I_{B1} = \frac{I_{control}}{\beta_1 + 2}
$$

**(b) Choose $R_D$ and $R_S$ for JFET self-bias to achieve $|A_v| = 8$. [03 Marks]**
**Solution:**
$I_{DSS} = 10\text{ mA}, V_P = -4\text{ V}, g_{m0} = 5\text{ mS}, r_d = 20\text{ k}\Omega$. $V_{GSQ} = \frac{1}{4} V_P = -1\text{ V}$.
1.  **Calculate $R_S$:**
    $$
    I_D = I_{DSS} \left(1 - \frac{V_{GSQ}}{V_P}\right)^2 = 10\text{ mA} \left(1 - \frac{-1}{-4}\right)^2 = 10 (0.75)^2 = 5.625\text{ mA}
    $$
    $$
    R_S = \frac{-V_{GSQ}}{I_D} = \frac{1\text{ V}}{5.625\text{ mA}} = 177.8\ \Omega
    $$
2.  **Calculate $g_m$:**
    $$
    g_m = g_{m0} \left(1 - \frac{V_{GSQ}}{V_P}\right) = 5\text{ mS} (0.75) = 3.75\text{ mS}
    $$
3.  **Calculate $R_D$ for $|A_v| = 8$:**
    $$
    |A_v| = g_m (R_D \parallel r_d \parallel R_L) = 8
    $$
    $$
    R_{eq} = R_D \parallel r_d \parallel R_L = \frac{8}{3.75\text{ mS}} = 2.133\text{ k}\Omega
    $$
    $$
    \frac{1}{R_{eq}} = \frac{1}{R_D} + \frac{1}{r_d} + \frac{1}{R_L} \Rightarrow \frac{1}{2.133\text{k}} = \frac{1}{R_D} + \frac{1}{20\text{k}} + \frac{1}{10\text{M}}
    $$
    $$
    \frac{1}{R_D} = 0.4688\text{ mS} - 0.05\text{ mS} - 0.0001\text{ mS} = 0.4187\text{ mS}
    $$
    $$
    R_D = \frac{1}{0.4187\text{ mS}} = 2.388\text{ k}\Omega \approx 2.4\text{ k}\Omega
    $$

**(c) Explain CMOS digital logic inverter with schematic. [03 Marks]**
*(Identical to 2023 Q.3(c), but explicitly 1-input. PMOS pull-up, NMOS pull-down. Input $0$ -> NMOS OFF, PMOS ON -> Output $1$. Input $1$ -> NMOS ON, PMOS OFF -> Output $0$).*

---

### Q.4
**(a) Define Miller effect capacitance. Derive expression for Output Miller capacitance ($C_{Mo}$). [04 Marks]**
**Definition:** The apparent increase in equivalent capacitance caused by a physical capacitor bridging the input and output of an inverting amplifier.
**Derivation for Output ($C_{Mo}$):**
1.  A feedback capacitor $C_f$ bridges input $V_i$ and output $V_o$. The voltage gain is $A_v = V_o / V_i$, so $V_i = V_o / A_v$.
2.  The current flowing from the output node into the capacitor is:
    $$
    I_o = \frac{V_o - V_i}{1/j\omega C_f} = j\omega C_f \left( V_o - \frac{V_o}{A_v} \right) = j\omega C_f \left( 1 - \frac{1}{A_v} \right) V_o
    $$
3.  The equivalent output impedance is:
    $$
    Z_{out} = \frac{V_o}{I_o} = \frac{1}{j\omega C_f (1 - 1/A_v)}
    $$
4.  This perfectly matches the reactance formula $\frac{1}{j\omega C_{Mo}}$, yielding:
    $$
    C_{Mo} = C_f \left( 1 - \frac{1}{A_v} \right)
    $$

**(b) Determine the lower-cutoff frequency ($f_L$) for the JFET CS amplifier. [04 Marks]**
**Solution:**
$V_{DD} = +20\text{V}, I_{DSS} = 8\text{mA}, V_P = -4\text{V}, R_S = 1\text{ k}\Omega$.
1.  **DC Biasing:**
    $V_{GS} = -I_D R_S = -1 I_D$ (in mA).
    $$
    I_D = 8 \left(1 + \frac{V_{GS}}{4}\right)^2 \Rightarrow -V_{GS} = 8 \left(1 + 0.5 V_{GS} + 0.0625 V_{GS}^2\right) = 8 + 4 V_{GS} + 0.5 V_{GS}^2
    $$
    $$
    0.5 V_{GS}^2 + 5 V_{GS} + 8 = 0
    $$
    Using the quadratic formula: $V_{GSQ} = -2\text{ V}$.
    $$
    g_m = \frac{16}{4} \left(1 - \frac{-2}{-4}\right) = 4(0.5) = 2\text{ mS}
    $$
2.  **Cutoff Frequencies:**
    *   **Input ($f_{LG}$):**
        $$
        f_{LG} = \frac{1}{2\pi (R_{sig} + R_G) C_G} = \frac{1}{2\pi (10\text{k} + 1000\text{k}) 0.01\ \mu\text{F}} = \frac{1}{2\pi (1.01\times 10^6) (10^{-8})} = 15.7\text{ Hz}
        $$
    *   **Output ($f_{LC}$):**
        $$
        f_{LC} = \frac{1}{2\pi (R_D + R_L) C_C} = \frac{1}{2\pi (4.7\text{k} + 2.2\text{k}) 0.5\ \mu\text{F}} = \frac{1}{2\pi (6900) (5\times 10^{-7})} = 46.1\text{ Hz}
        $$
    *   **Source Bypass ($f_{LS}$):**
        $$
        R_{eq} = R_S \parallel \frac{1}{g_m} = 1000 \parallel 500 = 333.3\ \Omega
        $$
        $$
        f_{LS} = \frac{1}{2\pi (333.3) 2\ \mu\text{F}} = 238.7\text{ Hz}
        $$
**Overall Lower Cutoff Frequency:**
$$
f_L \approx \max(f_{LG}, f_{LC}, f_{LS}) = 238.7\text{ Hz}
$$

**(c) Define GBW product. What capacitances limit BJT/FET high-frequency response? [02 Marks]**
**Answer:**
*   **Gain-Bandwidth Product (GBW):** A constant figure of merit for a specific op-amp, dictating that any increase in closed-loop gain will cause a mathematically proportional decrease in available bandwidth ($GBW = A_v \times f_c$).
*   **Limiting Capacitances:** The primary physical limitations are the microscopic **inter-electrode parasitic capacitances** spanning the semiconductor junctions ($C_\pi$ and $C_\mu$ in BJTs; $C_{gs}$ and $C_{gd}$ in FETs). These act as high-frequency short circuits, degrading the signal.

---

## SECTION - B

### Q.5
**(a) Virtual ground concept and non-inverting gain derivation. [04 Marks]**
*(Identical to 2021 Q.5(a)).*

**(b) Design an op-amp summing circuit: $V_o = -2 V_1 + 4 V_2 - 3 V_3$. [03 Marks]**
**Design Strategy:**
Rearrange the equation into a pure negative sum: $V_o = -( 2 V_1 - 4 V_2 + 3 V_3 )$.
1.  Pass input $V_2$ through a unity-gain inverting amplifier ($R_i = 10\text{k}, R_f = 10\text{k}$). The output is $-V_2$.
2.  Feed $V_1$, the inverted $-V_2$, and $V_3$ into a 3-input inverting summing amplifier with a feedback resistor $R_f = 12\text{ k}\Omega$ (chosen for easy mathematical common multiples).
3.  Set the input resistors for the summer:
    *   For $V_1$ (weight 2): $R_1 = R_f / 2 = 12\text{k} / 2 = 6\text{ k}\Omega$.
    *   For $-V_2$ (weight 4): $R_2 = R_f / 4 = 12\text{k} / 4 = 3\text{ k}\Omega$.
    *   For $V_3$ (weight 3): $R_3 = R_f / 3 = 12\text{k} / 3 = 4\text{ k}\Omega$.
The summer output yields: $V_o = - ( 2 V_1 + 4(-V_2) + 3 V_3 ) = -2 V_1 + 4 V_2 - 3 V_3$.

**(c) Define and explain physical significance of CMRR, $A_{OL}$, and $V_{OS}$. [03 Marks]**
*   **(i) CMRR:** Ability to cancel identical noise on both inputs. Crucial for rejecting electromagnetic interference in instrumentation cables.
*   **(ii) Open-Loop Gain ($A_{OL}$):** The massive, un-feedbacked raw amplification power of the op-amp. Crucial because a near-infinite $A_{OL}$ is what mathematically forces the "virtual ground" condition necessary for stable feedback equations to function.
*   **(iii) Input Offset Voltage ($V_{OS}$):** The differential DC voltage that must be manually applied across the input terminals to force the quiescent output exactly to $0\text{V}$. Crucial for precision DC instrumentation, as uncorrected $V_{OS}$ will be massively amplified and saturate the output.

---

### Q.6
**(a) 555-timer astable working principles. [04/05 Marks]**
*(Identical to 2022/2023 astable descriptions).*

**(b) Design a 555 astable frequency driver. [03 Marks]**
*(Provide standard schematic: $R_A$ between $V_{CC}$ and Discharge, $R_B$ between Discharge and Threshold/Trigger, $C$ to Ground. The frequency is dictated by $f = 1.44 / [(R_A + 2R_B)C]$).*

**(c) Functional role of each of the 8 pins in a standard 555 timer. [03 Marks]**
*   **Pin 1 (GND):** Main system ground reference.
*   **Pin 2 (Trigger):** Drops below $1/3 V_{CC}$ to set the flip-flop and initiate a HIGH output cycle.
*   **Pin 3 (Output):** The robust push-pull buffer output capable of sourcing/sinking current.
*   **Pin 4 (Reset):** Active-low override that instantly forces the output LOW.
*   **Pin 5 (Control):** Access to the internal $2/3 V_{CC}$ voltage divider node; can be used to modulate the frequency (FSK).
*   **Pin 6 (Threshold):** Rises above $2/3 V_{CC}$ to reset the flip-flop and end the HIGH output cycle.
*   **Pin 7 (Discharge):** Open-collector NPN transistor that shorts the timing capacitor to ground during the LOW cycle.
*   **Pin 8 ($V_{CC}$):** Positive DC power supply rail.

---

### Q.7
**(a) Determine output voltage with CMRR constraints. [03 Marks]**
**Solution:**
$V_{i1} = 150\ \mu\text{V}$, $V_{i2} = 140\ \mu\text{V}$, $A_d = 4000$.
Differential voltage $V_d = V_{i1} - V_{i2} = 10\ \mu\text{V}$.
Common-mode voltage $V_c = \frac{V_{i1} + V_{i2}}{2} = 145\ \mu\text{V}$.
The output voltage formula accounting for CMRR is: $V_o = A_d \left( V_d + \frac{V_c}{\text{CMRR}} \right)$.
1.  **(i) CMRR = 100:**
    $$
    V_o = 4000 \left( 10\ \mu\text{V} + \frac{145\ \mu\text{V}}{100} \right) = 4000 (10\ \mu\text{V} + 1.45\ \mu\text{V}) = 4000 (11.45\ \mu\text{V}) = 45.8\text{ mV}
    $$
2.  **(ii) CMRR = $10^5$:**
    $$
    V_o = 4000 \left( 10\ \mu\text{V} + \frac{145\ \mu\text{V}}{100,000} \right) = 4000 (10\ \mu\text{V} + 0.00145\ \mu\text{V}) \approx 4000 (10\ \mu\text{V}) = 40.0\text{ mV}
    $$

**(b) Design circuit: $V_o = 0.5 V_1 + 3 V_2 + 2 \int V_3 d t - 5 \frac{d V_4}{d t}$. [04 Marks]**
*(Design strategy matches 2023 Q.5(c). Convert to negative sum, apply pre-inverters, pre-differentiators, and pre-integrators, and feed into a multi-input inverting summer).*

**(c) Calculate closed-loop $V_o$ for multi-stage network. [03 Marks]**
**Solution:**
**Left Op-Amp Stage (Non-Inverting):**
Input is $V_1 = 0.1\text{V}$. $R_{f1} = 400\text{ k}\Omega, R_1 = 20\text{ k}\Omega$.
$$
V_{o1} = V_1 \left( 1 + \frac{R_{f1}}{R_1} \right) = 0.1\text{ V} \left( 1 + \frac{400\text{k}}{20\text{k}} \right) = 0.1(21) = 2.1\text{ V}
$$

**Right Op-Amp Stage (Inverting Summer):**
Inputs to this stage are $V_1$ (via $20\text{ k}\Omega$) and $V_{o1}$ (via $10\text{ k}\Omega$). $R_{f2} = 100\text{ k}\Omega$.
$$
V_o = -\left( V_1 \frac{R_{f2}}{R_{in1}} + V_{o1} \frac{R_{f2}}{R_{in2}} \right) = -\left( 0.1\text{ V} \frac{100\text{k}}{20\text{k}} + 2.1\text{ V} \frac{100\text{k}}{10\text{k}} \right)
$$
$$
V_o = -[ 0.1(5) + 2.1(10) ] = -[ 0.5\text{ V} + 21.0\text{ V} ] = -21.5\text{ V}
$$

---

### Q.8
**(a) Design active Wien bridge oscillator for $f_o = 20\text{ kHz}$. [03 Marks]**
*(Identical to 2021 Q.5(c). $C=1\text{nF}, R=7.95\text{k}\Omega, R_f=20\text{k}\Omega, R_1=10\text{k}\Omega$).*

**(b) Draw RC phase-shift oscillator and explain. [04 Marks]**
*(Identical to 2018 Q.8(b). Inverting op-amp for $-180^\circ$ and 3 RC ladders for the remaining $-180^\circ$ shift).*

**(c) Necessity of negative feedback. Calculate percentage change in $A_f$. [03 Marks]**
**Answer:**
*   **Necessity:** Negative feedback sacrifices excessive raw gain to drastically improve stability, widen the bandwidth, increase input impedance, and practically eliminate distortion and noise.
*   **Calculation:**
    Open-loop gain $A = -1000$. Feedback factor $\beta = -0.1$. Open-loop change $\Delta A / A = 20\%$.
    The equation for the fractional change in closed-loop gain is:
    $$
    \frac{\Delta A_f}{A_f} = \frac{1}{1 + A\beta} \left( \frac{\Delta A}{A} \right)
    $$
    Calculate the desensitivity factor $(1 + A\beta)$:
    $$
    1 + A\beta = 1 + (-1000)(-0.1) = 1 + 100 = 101
    $$
    Calculate the percentage change:
    $$
    \%\text{ Change in } A_f = \frac{1}{101} \times 20\% = 0.198\%
    $$
    *(Conclusion: The feedback network reduced a massive $20\%$ physical gain fluctuation down to an imperceptible $0.198\%$ change).*
