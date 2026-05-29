# 📝 RUET 2018 Even Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2205)

---

## SECTION - A

### Q.1
**(a) Derive an equation which describes the phase relationship between the input and output voltage for the direct-coupled cascaded configuration shown below. [04 Marks]**

**Answer:**
The circuit consists of a two-stage direct-coupled amplifier:
*   **Stage 1:** Common-Emitter (CE) amplifier using an NPN transistor ($Q_1$).
*   **Stage 2:** Common-Emitter (CE) amplifier using a PNP transistor ($Q_2$).

**Phase Derivation:**
1.  **Stage 1 ($Q_1$):** A signal $v_{in}$ applied to the base of a CE amplifier produces a collector voltage $v_{c1}$ that is amplified and inverted.
    $$
    v_{c1} = A_{v1} \cdot v_{in} \angle 180^\circ
    $$
    This $180^\circ$ phase shift occurs because an increase in base voltage increases collector current, which increases the voltage drop across $R_C$, thus lowering the collector voltage.
2.  **Stage 2 ($Q_2$):** The collector of $Q_1$ is directly coupled to the base of $Q_2$. Therefore, the input to Stage 2 is $v_{b2} = v_{c1}$.
    Stage 2 is also a CE amplifier (with a PNP transistor). It also introduces a phase inversion between its base and collector.
    $$
    v_{o} = A_{v2} \cdot v_{b2} \angle 180^\circ
    $$
3.  **Overall Phase Relationship:**
    Substituting $v_{b2}$ into the output equation:
    $$
    v_o = A_{v2} \cdot (A_{v1} \cdot v_{in} \angle 180^\circ) \angle 180^\circ
    $$
    $$
    v_o = |A_{v1} A_{v2}| \cdot v_{in} \angle (180^\circ + 180^\circ)
    $$
    $$
    v_o = A_v \cdot v_{in} \angle 360^\circ \equiv A_v \cdot v_{in} \angle 0^\circ
    $$

**Conclusion:** The total phase shift is $360^\circ$ (or $0^\circ$). The output voltage $V_o$ is exactly **in-phase** with the input voltage $V_i$.

---

**(b) For the cascaded JFET-BJT amplifier network, calculate (i) $A_v$, (ii) $Z_i$, (iii) $Z_o$, and (iv) Draw wave shapes for $v_i(t) = 10\sin(\omega t)\text{ mV}$. [08 Marks]**

**Solution:**
**1. DC and AC Parameters (Stage 1 - JFET):**
*   $V_{GS} = -I_D R_S = -680 I_D$
*   $I_D = I_{DSS}(1 - V_{GS}/V_P)^2 = 10\text{ mA} (1 - V_{GS}/-4)^2$
*   Solving gives $V_{GS} \approx -1.9\text{ V}$, $I_D \approx 2.8\text{ mA}$.
*   $g_m = \frac{2I_{DSS}}{|V_P|}\left(1 - \frac{V_{GS}}{V_P}\right) = \frac{20\text{ m}}{4} \left(1 - \frac{-1.9}{-4}\right) \approx 2.625\text{ mS}$
*   $Z_{i1} = R_G = 3.3\text{ M}\Omega$
*   $Z_{o1} = R_D = 2.4\text{ k}\Omega$

**2. DC and AC Parameters (Stage 2 - BJT):**
*   $V_{th} = \frac{4.7\text{k}}{15\text{k} + 4.7\text{k}} \times 20\text{ V} = 4.77\text{ V}$
*   $R_{th} = 15\text{k} \parallel 4.7\text{k} = 3.58\text{ k}\Omega$
*   $I_E = \frac{4.77 - 0.7}{1\text{k} + 3.58\text{k}/200} = 4.0\text{ mA}$
*   $r_e = 26\text{ mV} / 4.0\text{ mA} = 6.5\ \Omega$
*   $Z_{i2} = R_{B1} \parallel R_{B2} \parallel \beta r_e = 3.58\text{ k}\Omega \parallel 200(6.5\ \Omega) = 3.58\text{ k}\Omega \parallel 1.3\text{ k}\Omega = 0.953\text{ k}\Omega$

**3. Cascaded Calculations:**
**(ii) Input Impedance ($Z_i$):**
$$
Z_i = Z_{i1} = 3.3\text{ M}\Omega
$$
**(iii) Output Impedance ($Z_o$):**
$$
Z_o = R_C = 2.2\text{ k}\Omega
$$
**(i) Voltage Gain ($A_v$):**
*   Stage 1 Gain: $A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.625\text{ mS} \times (2.4\text{ k}\Omega \parallel 0.953\text{ k}\Omega) = -2.625\text{ mS} \times 0.682\text{ k}\Omega = -1.79$
*   Stage 2 Gain: $A_{v2} = -R_C / r_e = -2200 / 6.5 = -338.46$
*   Total Gain: $A_v = A_{v1} \times A_{v2} = (-1.79)(-338.46) = 605.8$

**(iv) Wave Shapes:**
*   Input: $v_i(t) = 10\sin(\omega t)\text{ mV}$
*   Output: $v_o(t) = A_v \cdot v_i(t) = 605.8 \times 10\text{ mV} \cdot \sin(\omega t) = 6.06\sin(\omega t)\text{ V}$
*   *Sketch:* Draw a common vertical axis and horizontal time axis. The input is a very small sine wave peaking at $+10\text{ mV}$. The output is a large sine wave peaking at $+6.06\text{ V}$, exactly in-phase with the input (since the total phase shift of two cascaded inverting stages is $360^\circ$).

---

### Q.2
**(a) Calculate (i) $Z_i$, (ii) $Z_o$, (iii) $A_{v1}, A_{v2}$, and (iv) $A_v$ of the cascaded network. [08 Marks]**

**Solution:**
**Stage 1: JFET CS Amplifier**
1.  **DC Biasing:** $V_{GS} = -I_D R_S = -330 I_D$.
    $I_D = I_{DSS}(1 - V_{GS}/V_P)^2 = 6\text{ mA}(1 - V_{GS}/-3)^2$
    Substitute $I_D = -V_{GS}/330$:
    $\frac{-V_{GS}}{0.33\text{ k}\Omega} = 6(1 + \frac{V_{GS}}{3})^2 \Rightarrow -3.03 V_{GS} = 6 \left( 1 + \frac{2V_{GS}}{3} + \frac{V_{GS}^2}{9} \right)$
    $-3.03 V_{GS} = 6 + 4 V_{GS} + 0.667 V_{GS}^2 \Rightarrow 0.667 V_{GS}^2 + 7.03 V_{GS} + 6 = 0$
    Solving the quadratic yields $V_{GS} = -0.94\text{ V}$ (the other root $-9.6\text{V}$ is ignored as it is beyond $V_P$).
2.  **AC Parameters:**
    $g_m = \frac{2I_{DSS}}{|V_P|}\left(1 - \frac{V_{GS}}{V_P}\right) = \frac{12\text{ m}}{3} \left(1 - \frac{-0.94}{-3}\right) = 4\text{ mS} (1 - 0.313) = 2.75\text{ mS}$
    $Z_{i1} = R_G = 10\text{ M}\Omega$
    $Z_{o1} = R_D = 1.8\text{ k}\Omega$

**Stage 2: BJT CE Amplifier**
1.  **DC Biasing:** Base bias resistor $R_{B1} = 24\text{ k}\Omega$ is connected to $V_{DD} = 10\text{ V}$.
    $I_B = \frac{V_{DD} - V_{BE}}{R_{B1} + (\beta+1)R_E} = \frac{10\text{ V} - 0.7\text{ V}}{24\text{ k}\Omega + (151)2.2\text{ k}\Omega} = \frac{9.3\text{ V}}{356.2\text{ k}\Omega} = 26.1\ \mu\text{A}$
    $I_E = (\beta+1)I_B = 151 \times 26.1\ \mu\text{A} = 3.94\text{ mA}$
2.  **AC Parameters:**
    $r_e = \frac{26\text{ mV}}{3.94\text{ mA}} = 6.6\ \Omega$
    $Z_{i2} = R_{B1} \parallel \beta r_e = 24\text{ k}\Omega \parallel 150(6.6\ \Omega) = 24\text{ k}\Omega \parallel 0.99\text{ k}\Omega = 0.95\text{ k}\Omega$

**Final Calculations:**
*   **(i) Input Impedance ($Z_i$):** $Z_i = Z_{i1} = 10\text{ M}\Omega$
*   **(ii) Output Impedance ($Z_o$):** $Z_o = R_C = 2.7\text{ k}\Omega$
*   **(iii) Individual Voltage Gains:**
    $A_{v2} = -\frac{R_C}{r_e} = -\frac{2700}{6.6} = -409$
    $A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.75\text{ mS} \times (1.8\text{ k}\Omega \parallel 0.95\text{ k}\Omega) = -2.75\text{ mS} \times 0.622\text{ k}\Omega = -1.71$
*   **(iv) Overall Voltage Gain ($A_v$):**
    $A_v = A_{v1} \times A_{v2} = (-1.71)(-409) = 699.4$

---

**(b) Draw a Darlington connection and show $\beta_D \approx \beta_1 \beta_2$. [04 Marks]**

**Answer:**
*(Schematic: Two NPN transistors. The collectors of $Q_1$ and $Q_2$ are tied together. The emitter of $Q_1$ connects directly to the base of $Q_2$. The base of $Q_1$ is the input, and the emitter of $Q_2$ is the output.)*

**Proof:**
Let the input base current be $I_{B1}$.
1.  The collector current of $Q_1$ is $I_{C1} = \beta_1 I_{B1}$.
2.  The emitter current of $Q_1$ is $I_{E1} = I_{C1} + I_{B1} = (\beta_1 + 1)I_{B1}$.
3.  Since the emitter of $Q_1$ drives the base of $Q_2$, we have $I_{B2} = I_{E1} = (\beta_1 + 1)I_{B1}$.
4.  The collector current of $Q_2$ is $I_{C2} = \beta_2 I_{B2} = \beta_2(\beta_1 + 1)I_{B1}$.
5.  The total composite collector current is:
    $I_{C(total)} = I_{C1} + I_{C2} = \beta_1 I_{B1} + \beta_2(\beta_1 + 1)I_{B1} = (\beta_1 + \beta_1\beta_2 + \beta_2) I_{B1}$
6.  The overall current gain is:
    $\beta_D = \frac{I_{C(total)}}{I_{B1}} = \beta_1\beta_2 + \beta_1 + \beta_2$
7.  Because $\beta_1$ and $\beta_2$ are typically large (e.g., $>100$), their product $\beta_1\beta_2$ is vastly larger than their sum.
    Therefore, $\beta_D \approx \beta_1 \beta_2$.

---

### Q.3
**(a) Determine the output voltage ($V_o$) of the op-amp circuit. [04 Marks]**

**Solution:**
The circuit is a combined inverting and non-inverting amplifier. We solve it using the Superposition Theorem.

**Step 1: Find the voltage at the non-inverting terminal ($V_p$) due to $V_2$:**
The non-inverting terminal is connected to a voltage divider consisting of the $150\text{ k}\Omega$ and $10\text{ k}\Omega$ resistors.
$$
V_p = V_2 \left( \frac{10\text{ k}\Omega}{150\text{ k}\Omega + 10\text{ k}\Omega} \right) = V_2 \left( \frac{10}{160} \right) = \frac{V_2}{16}
$$

**Step 2: Apply Superposition for $V_o$:**
The output is the sum of the inverting response (due to $V_1$) and the non-inverting response (due to $V_p$).
$$
V_o = V_{o(inverting)} + V_{o(non-inverting)}
$$
$$
V_o = -\left( \frac{R_f}{R_1} \right) V_1 + \left( 1 + \frac{R_f}{R_1} \right) V_p
$$
$$
V_o = -\left( \frac{330\text{ k}\Omega}{10\text{ k}\Omega} \right) V_1 + \left( 1 + \frac{330\text{ k}\Omega}{10\text{ k}\Omega} \right) \left( \frac{V_2}{16} \right)
$$
$$
V_o = -33 V_1 + (34) \left( \frac{V_2}{16} \right) = -33 V_1 + 2.125 V_2
$$

---

## SECTION - B

### Q.3 (continued)
**(b) Prove mathematically that the active op-amp network operates as an integrating circuit. [04 Marks]**

**Proof:**
1.  Assume an ideal op-amp. The non-inverting terminal is grounded ($0\text{V}$). By the virtual ground principle, the inverting terminal voltage is $V_n \approx 0\text{V}$.
2.  The op-amp has infinite input impedance, so no current flows into the inverting terminal. Therefore, the current flowing through input resistor $R$ ($i_R$) must equal the current flowing through feedback capacitor $C$ ($i_C$).
3.  $i_R = \frac{V_i - V_n}{R} = \frac{V_i}{R}$
4.  $i_C = C \frac{d(V_n - V_o)}{dt} = -C \frac{dV_o}{dt}$
5.  Equating the currents:
    $\frac{V_i}{R} = -C \frac{dV_o}{dt} \Rightarrow dV_o = -\frac{1}{RC} V_i dt$
6.  Integrating both sides:
    $$
    V_o(t) = -\frac{1}{RC} \int V_i(t) dt + V_o(0)
    $$
Because the output voltage is proportional to the time integral of the input voltage, the circuit perfectly functions as an integrating circuit.

---

**(c) Sketch the output voltage waveform ($v_o(t)$) for the switched op-amp integrator. [04 Marks]**

**Solution:**
1.  The switch closes at $t=0$, applying a constant $V_i = 12\text{V}$ DC to the integrator.
2.  The integration rate (slope) is:
    $$
    \frac{dV_o}{dt} = -\frac{V_i}{RC} = -\frac{12\text{ V}}{200\text{ k}\Omega \times 1\ \mu\text{F}} = -\frac{12}{0.2} = -60\text{ V/s}
    $$
3.  **Waveform Sketch:** The output $v_o(t)$ starts at $0\text{V}$ at $t=0$. It ramps down linearly in a straight line with a constant slope of $-60\text{ V/s}$.
4.  Since real op-amps have finite power supply limits, the ramp will not continue indefinitely. Assuming typical $\pm 15\text{V}$ supplies, the op-amp will saturate at approx $-14\text{V}$ or $-15\text{V}$. The time it takes to saturate is $t_{sat} = \frac{-14\text{ V}}{-60\text{ V/s}} = 0.233\text{ s}$ (or $233\text{ ms}$). After this time, the output is a flat horizontal line at $-14\text{V}$.

---

### Q.4
**(a) What is the slew rate of an operational amplifier? How does it limit the maximum operating frequency? [04 Marks]**

**Answer:**
**Slew Rate (SR)** is the maximum rate at which an operational amplifier can change its output voltage. It is expressed in Volts per microsecond ($\text{V}/\mu\text{s}$). It is caused by the internal compensation capacitor of the op-amp charging and discharging through a finite internal constant-current source.

**Frequency Limitation:**
For a sinusoidal output signal $v_o(t) = V_p \sin(2\pi f t)$, the maximum rate of change occurs at the zero-crossing, mathematically given by the derivative evaluated at $t=0$:
$$
\left| \frac{dv_o}{dt} \right|_{max} = 2\pi f V_p
$$
For the op-amp to output this signal without distortion, its Slew Rate must be greater than or equal to this required rate of change:
$$
SR \ge 2\pi f V_p \Rightarrow f_{max} = \frac{SR}{2\pi V_p}
$$
This equation shows that for a given output amplitude $V_p$, there is an absolute maximum frequency limit ($f_{max}$). If the frequency exceeds this limit, the op-amp cannot "keep up" with the sine wave, and the output will distort into a triangular shape with attenuated amplitude.

---

**(b) Design an op-amp circuit that computes: $v_o = 0.5 v_1 - 0.7 v_2 + 0.2 \frac{d v_3}{d t}$. [04 Marks]**

**Design Strategy:**
We can achieve this using three op-amp stages.
*   **Stage 1: Differentiator for $v_3$.**
    $$
    v_{a} = -R_d C_d \frac{d v_3}{dt}
    $$
    Let $C_d = 1\ \mu\text{F}$ and $R_d = 200\text{ k}\Omega$. Then $R_d C_d = 0.2\text{ s}$.
    Result: $v_a = -0.2 \frac{d v_3}{dt}$.
*   **Stage 2: Inverting Amplifier for $v_1$.**
    $$
    v_b = -\left(\frac{R_{f1}}{R_{i1}}\right) v_1
    $$
    Let $R_{i1} = 100\text{ k}\Omega$ and $R_{f1} = 50\text{ k}\Omega$. Then $R_{f1}/R_{i1} = 0.5$.
    Result: $v_b = -0.5 v_1$.
*   **Stage 3: Inverting Summing Amplifier.**
    We sum $v_a$, $v_b$, and the $v_2$ input into a final inverting stage.
    $$
    v_o = -\left( \frac{R_f}{R_a} v_a + \frac{R_f}{R_b} v_b + \frac{R_f}{R_2} v_2 \right)
    $$
    Let the feedback resistor $R_f = 100\text{ k}\Omega$.
    *   To process $v_a$: We want $+0.2 \frac{dv_3}{dt}$, so we need a gain of $-1$ for $v_a$. Thus, $R_a = 100\text{ k}\Omega$.
    *   To process $v_b$: We want $+0.5 v_1$, so we need a gain of $-1$ for $v_b$. Thus, $R_b = 100\text{ k}\Omega$.
    *   To process $v_2$: We want $-0.7 v_2$, so we need a gain of $+0.7$ overall. Since the summer is inverting, the summing gain must be $0.7$. Thus, $\frac{100\text{k}}{R_2} = 0.7 \Rightarrow R_2 = 142.8\text{ k}\Omega$.
*   **Verification:**
    $$
    v_o = -\left[ 1(-0.2 d v_3/dt) + 1(-0.5 v_1) + 0.7 v_2 \right] = 0.2 \frac{d v_3}{dt} + 0.5 v_1 - 0.7 v_2
    $$

---

**(c) Explain how a Schmitt trigger circuit eliminates false triggering and chattering in comparators. [04 Marks]**

**Answer:**
A standard basic comparator has a single reference threshold. If the input signal is noisy and hovers near this threshold, the noise spikes will cause the input to cross back and forth across the threshold rapidly. This causes the output to uncontrollably toggle HIGH and LOW (chattering/false triggering).

A **Schmitt trigger** eliminates this by employing **positive feedback**. This creates **hysteresis**, meaning the circuit has *two different threshold voltages* depending on the current output state:
1.  Upper Trigger Point ($V_{UT}$): The threshold to cross when the input is rising.
2.  Lower Trigger Point ($V_{LT}$): The threshold to cross when the input is falling.

When a noisy rising signal crosses $V_{UT}$, the output snaps to the opposite state. Crucially, the positive feedback instantaneously shifts the threshold down to $V_{LT}$. Now, the noise spikes (which are small) are far above the new threshold $V_{LT}$, so they cannot cause the output to flip back. The signal must deliberately drop all the way down to $V_{LT}$ before the output changes state again. This hysteresis band ($V_{UT} - V_{LT}$) acts as an immunity zone that completely absorbs and ignores input noise, eliminating chattering.

---

### Q.5
**(a) Calculate the resonant oscillation frequency ($f_o$) of the active Wien-bridge. [04 Marks]**

**Solution:**
The non-inverting input path forms a classic Wien Bridge frequency-selective network.
The series branch has $R_s = 51\text{ k}\Omega, C_s = 0.001\ \mu\text{F}$.
The parallel branch has $R_p = 51\text{ k}\Omega, C_p = 0.001\ \mu\text{F}$.
Since the components are identical ($R = 51\text{ k}\Omega, C = 0.001\ \mu\text{F}$), the resonant frequency is simply:
$$
f_o = \frac{1}{2\pi RC} = \frac{1}{2\pi \times 51\text{ k}\Omega \times 0.001\ \mu\text{F}} = \frac{1}{2\pi \times 51 \times 10^{-6}}
$$
$$
f_o \approx 3120.7\text{ Hz} = 3.12\text{ kHz}
$$

---

**(b) For a Colpitts oscillator, prove that $f_o = \frac{1}{2\pi \sqrt{L \frac{C_1 C_2}{C_1 + C_2}}}$. [04 Marks]**

**Proof:**
In a Colpitts oscillator, the feedback network is a parallel resonant LC tank circuit consisting of an inductor $L$ in parallel with two series capacitors, $C_1$ and $C_2$.
For oscillation to occur, the total reactive impedance of the tank loop must sum to zero at the resonant frequency (Barkhausen phase condition).
The sum of the reactances around the closed tank loop is:
$$
X_L + X_{C1} + X_{C2} = 0
$$
Substituting the complex impedances:
$$
j\omega L + \frac{1}{j\omega C_1} + \frac{1}{j\omega C_2} = 0
$$
Dividing by $j$ (where $1/j = -j$):
$$
\omega L - \frac{1}{\omega C_1} - \frac{1}{\omega C_2} = 0
$$
$$
\omega L = \frac{1}{\omega} \left( \frac{1}{C_1} + \frac{1}{C_2} \right)
$$
Multiply both sides by $\omega$:
$$
\omega^2 L = \frac{C_1 + C_2}{C_1 C_2}
$$
$$
\omega^2 = \frac{1}{L} \left( \frac{C_1 + C_2}{C_1 C_2} \right) = \frac{1}{L \cdot C_{eq}} \quad \text{where} \quad C_{eq} = \frac{C_1 C_2}{C_1 + C_2}
$$
$$
\omega = 2\pi f_o = \frac{1}{\sqrt{L \cdot C_{eq}}}
$$
$$
f_o = \frac{1}{2\pi \sqrt{L \left(\frac{C_1 C_2}{C_1 + C_2}\right)}}
$$

---

**(c) Show that for sustained oscillation in an op-amp RC phase-shift oscillator, the open-loop gain must be $A_v \ge 29$. [04 Marks]**

**Proof:**
In an RC phase-shift oscillator, the feedback network consists of three identical cascaded RC high-pass sections.
By performing nodal analysis on the three RC sections, the transfer function (feedback fraction $\beta$) relating the network output to its input is derived as:
$$
\beta = \frac{v_f}{v_o} = \frac{1}{1 - 5\alpha^2 - j(6\alpha - \alpha^3)}
$$
where $\alpha = \frac{1}{\omega RC}$.
For the phase shift to be exactly $180^\circ$, the imaginary part of the denominator must be zero:
$$
6\alpha - \alpha^3 = 0 \Rightarrow \alpha^2 = 6
$$
Substitute $\alpha^2 = 6$ back into the real part of the transfer function:
$$
\beta = \frac{1}{1 - 5(6)} = \frac{1}{1 - 30} = -\frac{1}{29}
$$
The negative sign indicates the expected $180^\circ$ phase shift. The magnitude of the feedback attenuation is exactly $1/29$.
According to the Barkhausen criterion, for sustained oscillations, the magnitude of the loop gain must be at least 1:
$$
|A_v \beta| \ge 1 \Rightarrow A_v \ge \left| \frac{1}{\beta} \right| \Rightarrow A_v \ge 29
$$
Thus, the amplifier must provide a voltage gain of at least 29 to compensate for the attenuation of the 3-stage RC network.

---

### Q.6
**(a) Prove that voltage-series feedback is the most effective connection topology in improving bandwidth, input impedance, and output impedance. [04 Marks]**

**Proof:**
1.  **Bandwidth:** All negative feedback topologies reduce the closed-loop gain ($A_f = \frac{A}{1+A\beta}$). Because the Gain-Bandwidth Product (GBP) of an amplifier is constant, a reduction in gain by a factor of $(1+A\beta)$ results in an exact proportional increase in bandwidth:
    $$
    BW_f = BW \times (1+A\beta)
    $$
2.  **Input Impedance ($Z_{if}$):** The "Series" connection at the input means the feedback voltage opposes the input voltage (a subtraction in a series loop). This requires the signal source to provide a higher voltage to drive the same input current into the amplifier. By Ohm's law, a higher required voltage for the same current implies a higher impedance.
    $$
    Z_{if} = Z_i \times (1+A\beta)
    $$
3.  **Output Impedance ($Z_{of}$):** The "Voltage" (or Shunt) connection at the output means the feedback network samples the output voltage in parallel. If the load changes causing the output voltage to dip, the feedback network immediately detects this and drives the amplifier harder to restore the voltage. This ability to maintain a constant voltage regardless of load is the definition of a low output impedance source (an ideal voltage source).
    $$
    Z_{of} = \frac{Z_o}{1+A\beta}
    $$
Combining series input mixing and parallel voltage sampling provides the best of all worlds: vastly increased bandwidth, vastly increased input impedance (preventing source loading), and vastly decreased output impedance (improving load driving capability).

---

**(b) Voltage-series feedback amplifier: $A = -100, R_i = 10\text{ k}\Omega, R_o = 20\text{ k}\Omega, \beta = -0.1$. Determine $A_f, R_{if}, R_{of}$. [04 Marks]**

**Solution:**
First, calculate the desensitivity factor: $D = 1 + A\beta = 1 + (-100)(-0.1) = 1 + 10 = 11$.
**(i) Closed-loop voltage gain ($A_f$):**
$$
A_f = \frac{A}{1+A\beta} = \frac{-100}{11} = -9.09
$$
**(ii) Closed-loop input impedance ($R_{if}$):**
Because it is a series input connection, input impedance increases:
$$
R_{if} = R_i (1+A\beta) = 10\text{ k}\Omega \times 11 = 110\text{ k}\Omega
$$
**(iii) Closed-loop output impedance ($R_{of}$):**
Because it is a voltage sampling (parallel) connection, output impedance decreases:
$$
R_{of} = \frac{R_o}{1+A\beta} = \frac{20\text{ k}\Omega}{11} = 1.818\text{ k}\Omega
$$

---

**(c) Discuss the key performance improvements of an amplifier due to negative feedback. [04 Marks]**

**Answer:**
1.  **Desensitization of Gain:** The closed-loop gain ($A_f \approx 1/\beta$) becomes highly stable and independent of variations in internal transistor parameters, temperature changes, or supply voltage drifts.
2.  **Extended Bandwidth:** The high and low cutoff frequencies are pushed outward, significantly widening the flat operational bandwidth.
3.  **Reduction of Non-Linear Distortion:** Negative feedback drastically reduces harmonic distortion and noise generated internally within the amplifier stages by forcing the output to strictly follow the input geometry.
4.  **Impedance Control:** It allows the designer to precisely tailor input and output impedances to match sources and loads (e.g., maximizing input impedance and minimizing output impedance).

---

### Q.7
**(a) Draw the detailed internal block diagram of a 555 timer IC. [03 Marks]**

**Answer:**
*(Diagram features to include: Three $5\text{k}\Omega$ resistors forming a voltage divider defining $2/3 V_{CC}$ and $1/3 V_{CC}$. A Threshold comparator connected to $2/3 V_{CC}$. A Trigger comparator connected to $1/3 V_{CC}$. An SR Flip-Flop driven by the comparators. An output inverting buffer. An NPN discharge transistor connected to Pin 7, driven by the inverted flip-flop output.)*

---

**(b) Define duty cycle. Calculate the duty cycle of the 555-timer astable network with an ideal diode across $R_B$. $R_A = 1\text{ k}\Omega, R_B = 10\text{ k}\Omega$. [05 Marks]**

**Solution:**
**Definition:** Duty cycle is the ratio of the time a signal is in its active (HIGH) state ($t_c$) to the total period of the signal ($T$). It is usually expressed as a percentage: $D = (t_c / T) \times 100\%$.

**Calculation with Ideal Diode:**
1.  **Charging phase ($t_c$):** Output is HIGH. The current flows from $V_{CC}$ through $R_A$. Instead of passing through $R_B$, the current takes the path of least resistance through the forward-biased ideal diode. Therefore, the capacitor charges *only* through $R_A$.
    $$
    t_c = 0.693 R_A C
    $$
2.  **Discharging phase ($t_d$):** Output is LOW. The internal discharge transistor turns ON. The diode is now reverse-biased (blocking). The capacitor must discharge through $R_B$ to reach Pin 7.
    $$
    t_d = 0.693 R_B C
    $$
3.  **Duty Cycle:**
    $$
    D = \frac{t_c}{t_c + t_d} = \frac{0.693 R_A C}{0.693 R_A C + 0.693 R_B C} = \frac{R_A}{R_A + R_B}
    $$
    $$
    D = \frac{1\text{ k}\Omega}{1\text{ k}\Omega + 10\text{ k}\Omega} \times 100\% = \frac{1}{11} \times 100\% = 9.09\%
    $$

---

**(c) Sketch the output voltage waveform ($V_o$) of the 555-timer monostable multivibrator triggered at $t = 1\text{ ms}$ and $t = 5\text{ ms}$. [04 Marks]**

**Solution:**
1.  **Pulse Width Calculation:**
    $$
    W = 1.1 R C = 1.1 \times 4.7\text{ k}\Omega \times 0.1\ \mu\text{F} = 1.1 \times 4700 \times 10^{-7} = 0.000517\text{ s} = 0.517\text{ ms}
    $$
2.  **Waveform Description:**
    *   **$t = 0$ to $1\text{ ms}$:** The output is LOW ($0\text{V}$).
    *   **$t = 1\text{ ms}$:** The first trigger pulse arrives. The output instantly goes HIGH ($V_{CC} \approx 10\text{V}$). It stays HIGH for the duration of the pulse width $W = 0.517\text{ ms}$.
    *   **$t = 1.517\text{ ms}$:** The pulse ends. The output returns to LOW ($0\text{V}$).
    *   **$t = 1.517\text{ ms}$ to $5\text{ ms}$:** The output remains LOW.
    *   **$t = 5\text{ ms}$:** The second trigger pulse arrives. The output instantly goes HIGH again.
    *   **$t = 5.517\text{ ms}$:** The pulse ends. The output returns to LOW.
*(Sketch: A horizontal axis (time in ms). A steady $0\text{V}$ line, interrupted by two rectangular pulses. The first pulse starts exactly at $1.0\text{ms}$ and drops at $1.517\text{ms}$. The second pulse starts exactly at $5.0\text{ms}$ and drops at $5.517\text{ms}$. Both pulses reach a height of approx $+10\text{V}$.)*

---

### Q.8
**(a) Prove that the Barkhausen Criterion is given by $A\beta = 1\angle 0^\circ$. [03 Marks]**

**Proof:**
The closed-loop gain $A_f$ of a system with an open-loop gain $A$ and a positive feedback loop $\beta$ is:
$$
A_f = \frac{A}{1 - A\beta}
$$
An oscillator is a circuit that generates an output signal without any external input signal. For a finite output to exist when the input is strictly zero, the closed-loop gain $A_f$ must be theoretically infinite.
For $A_f \rightarrow \infty$, the denominator of the equation must be equal to zero:
$$
1 - A\beta = 0 \Rightarrow A\beta = 1
$$
Since $A$ and $\beta$ are complex quantities possessing magnitude and phase, this translates to two conditions:
1.  Magnitude: $|A\beta| = 1$
2.  Phase: The total phase shift around the loop must be an integer multiple of $360^\circ$ (which is $0^\circ$).
Combining these gives the Barkhausen Criterion: $A\beta = 1\angle 0^\circ$.

---

**(b) Describe with a neat schematic the operation of an op-amp based RC phase-shift oscillator and derive the frequency of oscillation ($f_o$). [05 Marks]**

**Answer:**
*(Schematic: An op-amp in an inverting amplifier configuration (resistors $R_f$ and $R_1$). The output is fed back to the inverting input through a cascade of three identical High-Pass RC networks.)*

**Operation:**
The inverting op-amp naturally provides a $180^\circ$ phase shift. To achieve the required $360^\circ$ loop phase shift for oscillation, the feedback network must provide an additional $180^\circ$ of phase shift. A single RC high-pass network provides between $0^\circ$ and $90^\circ$ of phase lead. By cascading three identical RC networks, each section contributes exactly $60^\circ$ of phase shift at one specific resonant frequency ($f_o$), summing to $180^\circ$. The system will oscillate solely at this frequency where Barkhausen criteria are met.

**Derivation:**
The transfer function of the 3-stage RC feedback network is:
$$
\beta = \frac{1}{1 - 5/(\omega RC)^2 - j[6/(\omega RC) - 1/(\omega RC)^3]}
$$
For the phase shift to be $180^\circ$, the imaginary component of the denominator must be zero:
$$
\frac{6}{\omega RC} - \frac{1}{(\omega RC)^3} = 0
$$
$$
\frac{6}{\omega RC} = \frac{1}{(\omega RC)^3} \Rightarrow 6 = \frac{1}{(\omega RC)^2}
$$
$$
\omega^2 = \frac{1}{6 (RC)^2} \Rightarrow \omega = \frac{1}{\sqrt{6} RC}
$$
Since $\omega = 2\pi f_o$, we get the frequency of oscillation:
$$
f_o = \frac{1}{2\pi \sqrt{6} RC}
$$

---

**(c) Design an op-amp based Wien bridge oscillator to operate at a frequency of $f_o = 10\text{ kHz}$. [04 Marks]**

**Design Strategy:**
The resonant frequency of a Wien bridge oscillator is $f_o = \frac{1}{2\pi RC}$.
We are given $f_o = 10,000\text{ Hz}$.
1.  **Select a practical capacitor value:** Let $C = 10\text{ nF} = 0.01\ \mu\text{F}$.
2.  **Calculate the resistor value ($R$):**
    $$
    R = \frac{1}{2\pi f_o C} = \frac{1}{2\pi \times 10000 \times 10 \times 10^{-9}} = \frac{1}{2\pi \times 10^{-4}} = \frac{10000}{2\pi} \approx 1591.5\ \Omega
    $$
    Use a standard resistor value, $R = 1.6\text{ k}\Omega$.
3.  **Determine Amplifier Gain Resistors:**
    For sustained oscillation, the non-inverting amplifier must have a gain $A_v \ge 3$.
    $$
    A_v = 1 + \frac{R_f}{R_1} \ge 3 \Rightarrow \frac{R_f}{R_1} \ge 2 \Rightarrow R_f \ge 2 R_1
    $$
    Let $R_1 = 10\text{ k}\Omega$. Then $R_f$ must be exactly $20\text{ k}\Omega$. To ensure oscillations start, we choose $R_f$ slightly larger, e.g., $R_f = 22\text{ k}\Omega$ (or a $20\text{k}\Omega$ fixed resistor with a small potentiometer).

**Final Component Values:**
*   Feedback Network: $R = 1.6\text{ k}\Omega$, $C = 10\text{ nF}$.
*   Amplifier Network: $R_1 = 10\text{ k}\Omega$, $R_f = 20\text{ k}\Omega$ (minimum).
