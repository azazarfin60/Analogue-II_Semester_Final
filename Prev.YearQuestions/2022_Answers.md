# 📝 RUET 2022 Odd Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2105)

---

## SECTION - A

### Q.1
**(a) Draw the detailed small-signal AC equivalent circuit of the cascode BJT amplifier. [03 Marks]**

**Answer:**
**Construction of AC Equivalent:**
1.  **Stage 1 (Common-Emitter $Q_1$):**
    *   The base is connected to the input signal $v_i$.
    *   The base bias resistors $R_{B1}$ and $R_{B2}$ are in parallel to AC ground.
    *   The emitter bypass capacitor $C_E$ shorts the emitter directly to AC ground.
    *   The collector features a dependent current source $g_{m1} v_{\pi 1}$ (or $\beta_1 i_{b1}$) in parallel with the output resistance $r_{o1}$, both connected between the collector and ground.
2.  **Stage 2 (Common-Base $Q_2$):**
    *   The emitter of $Q_2$ is driven directly by the collector of $Q_1$.
    *   The base of $Q_2$ is tied directly to Ground.
    *   The internal resistance of $Q_2$ is represented by $r_{e2}$ between emitter and base (ground).
    *   The collector features a dependent current source $\alpha i_{e2}$ (or $g_{m2} v_{\pi 2}$) pointing from collector to base (ground).
    *   The collector load resistor $R_C$ and the external load $R_L$ are connected between the collector and AC ground. The output $V_o$ is taken from this node.

---

**(b) Draw a current mirror circuit using BJTs and explain its operating logic. [03 Marks]**
*(Identical to 2020 Q.1(c). Two matched NPNs, $Q_1$ diode-connected. They share the same $V_{BE}$, forcing $Q_2$ to sink exactly the same collector current as the reference current flowing through $Q_1$).*

---

**(c) Design a 3-input CMOS NAND gate and explain its operation with truth table. [04 Marks]**
**Design:**
A 3-input CMOS NAND gate consists of 3 PMOS and 3 NMOS transistors.
*   **Pull-up Network:** The 3 PMOS transistors are connected in **parallel** between $+V_{DD}$ and the output node ($V_{out}$).
*   **Pull-down Network:** The 3 NMOS transistors are connected in **series** between the output node ($V_{out}$) and Ground.
*   Inputs A, B, and C each drive one pair of PMOS/NMOS gates.

**Operating Logic & Truth Table:**
1.  If **ALL** inputs are HIGH ($1, 1, 1$): All 3 series NMOS transistors turn ON, completing the path to ground. All 3 parallel PMOS transistors turn OFF. The output is firmly pulled LOW ($0$).
2.  If **ANY** input is LOW (e.g., $0, 1, 1$): The corresponding NMOS turns OFF, breaking the series chain to ground. Simultaneously, the corresponding PMOS turns ON, creating a direct short from $+V_{DD}$ to $V_{out}$. The output is pulled HIGH ($1$).

| A | B | C | $V_{out}$ (NAND) |
|---|---|---|---|
| 0 | 0 | 0 | 1 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

---

### Q.2
**(a) Derive the expression for the input Miller capacitance ($C_{Mi}$). [03 Marks]**
*(Identical to 2020 Q.2(b). Derivation via KCL at the input node showing that the current through the feedback capacitor $C$ is magnified by $(1 - A_v)$, making the equivalent input capacitance $C_{Mi} = C(1 - A_v)$).*

**(b) Draw a Darlington pair configuration and explain its mechanics. [03 Marks]**
*(Identical to 2020 Q.1(b). Two BJTs cascaded emitter-to-base, multiplying the current gains $\beta_D \approx \beta_1 \beta_2$ to provide ultra-high current amplification and high input impedance).*

**(c) Calculate the voltage gain ($A_v$) of the cascaded CE-CS amplifier. [04 Marks]**
**Solution:**
**Stage 1 (NPN CE):**
1.

    $$
    V_{th1} = 10\text{ V} \times \frac{8.2\text{ k}\Omega}{24\text{ k}\Omega + 8.2\text{ k}\Omega} = 2.546\text{ V}
    $$
2.

    $$
    R_{th1} = 24\text{ k}\Omega \parallel 8.2\text{ k}\Omega = 6.11\text{ k}\Omega
    $$
3.

    $$
    I_{E1} = \frac{V_{th1} - 0.7}{R_E + R_{th1}/150} = \frac{1.846\text{ V}}{2200 + 40.7} = 0.824\text{ mA}
    $$
4.

    $$
    r_{e1} = \frac{26\text{ mV}}{0.824\text{ mA}} = 31.55\ \Omega
    $$
5.  Load on Stage 1 is $R_{C1} \parallel Z_{in2} = 2.7\text{ k}\Omega \parallel 10\text{ M}\Omega \approx 2.7\text{ k}\Omega$.
6.

    $$
    A_{v1} = -\frac{2700\ \Omega}{31.55\ \Omega} = -85.58
    $$

**Stage 2 (JFET CS):**
1.  Self-bias equation: $V_{GS} = -I_D R_S = -330 I_D$.
2.  Shockley's equation: $I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2 = 6\text{ mA} \left(1 + \frac{V_{GS}}{6}\right)^2$.
3.  Substituting $I_D$:
    $$
    \frac{-V_{GS}}{330} = 0.006 \left(1 + \frac{V_{GS}}{3} + \frac{V_{GS}^2}{36}\right)
    $$
    $$
    -V_{GS} = 1.98 \left(1 + 0.333 V_{GS} + 0.0278 V_{GS}^2\right) = 1.98 + 0.66 V_{GS} + 0.055 V_{GS}^2
    $$
    $$
    0.055 V_{GS}^2 + 1.66 V_{GS} + 1.98 = 0
    $$
    Using the quadratic formula yields $V_{GS} = -1.24\text{ V}$.
4.  Transconductance:
    $$
    g_m = \frac{2(6\text{ mA})}{6\text{ V}} \left(1 - \frac{-1.24}{-6}\right) = 2\text{ mS} \times (1 - 0.207) = 1.58\text{ mS}
    $$
5.

    $$
    A_{v2} = -g_m R_{D2} = -(1.58\text{ mS})(3.7\text{ k}\Omega) = -5.85
    $$

**Overall Voltage Gain ($A_v$):**
$$
A_v = A_{v1} \times A_{v2} = (-85.58) \times (-5.85) = 500.6
$$

---

### Q.3
**(a) Draw a differential amplifier using BJTs and explain its operating logic. [03 Marks]**
*(Identical to 2020 Q.2(a). Emitter-coupled pair utilizing a tail current source to amplify differential signals while rejecting common-mode noise via the constant total emitter current constraint).*

**(b) Define CMRR and slew rate. [02 Marks]**
*(Identical to 2019/2020/2021. CMRR = $20\log(A_d / A_{cm})$. Slew rate = Max rate of output voltage change $\text{V}/\mu\text{s}$).*

**(c) Calculate low-frequency cutoff parameters ($f_{LG}, f_{LC}, f_{LS}$) for the JFET CS amplifier. [05 Marks]**
**Solution:**
**(Referencing identically biased circuit from 2021 Q.3(b)):**
$I_{DSS} = 10\text{ mA}, V_P = -6\text{ V}, R_S = 2.2\text{ k}\Omega$.
Calculated DC Bias: $V_{GS} = -3.58\text{ V}$, $g_m = 1.34\text{ mS}$.
*   **Gate Input ($f_{LG}$):**
    Assuming the two $1\ \mu\text{F}$ capacitors shown at the input are in series, the equivalent input coupling capacitance is $C_{in} = 0.5\ \mu\text{F}$.
    $$
    R_i = 220\text{ k}\Omega \parallel 68\text{ k}\Omega = 51.9\text{ k}\Omega
    $$
    $$
    f_{LG} = \frac{1}{2\pi (R_s + R_i) C_{in}} = \frac{1}{2\pi (1.5\text{ k}\Omega + 51.9\text{ k}\Omega) 0.5\ \mu\text{F}} = 5.96\text{ Hz}
    $$
    *(Note: If interpreted as a single $1\ \mu\text{F}$ capacitor, $f_{LG} = 2.98\text{ Hz}$. Both are academically valid depending on visual interpretation).*
*   **Output Coupling ($f_{LC}$):**
    $$
    f_{LC} = \frac{1}{2\pi (R_D + R_L) C_{out}} = \frac{1}{2\pi (3.9\text{ k}\Omega + 5.6\text{ k}\Omega) 6.8\ \mu\text{F}} = 2.46\text{ Hz}
    $$
*   **Source Bypass ($f_{LS}$):**
    $$
    R_e = R_S \parallel \frac{1}{g_m} = 2200 \parallel 746 = 557\ \Omega
    $$
    $$
    f_{LS} = \frac{1}{2\pi (557\ \Omega) 10\ \mu\text{F}} = 28.5\text{ Hz}
    $$
**Overall Lower Cutoff Frequency:**
$$
f_L \approx f_{LS} = 28.5\text{ Hz}
$$

---

### Q.4
**(a) Draw the internal block configuration of a 555 timer. [03 Marks]**
*(Standard diagram: Voltage divider with three $5\text{k}\Omega$ resistors, two comparators, an SR flip-flop, a discharge NPN transistor, and an inverting output buffer).*

**(b) Design a 555 astable frequency driver and explain. [03 Marks]**
**Design & Operation:**
Connect $R_A$ between $V_{CC}$ and Pin 7 (Discharge). Connect $R_B$ between Pin 7 and Pin 6 (Threshold). Tie Pin 6 to Pin 2 (Trigger), and connect timing capacitor $C$ from Pin 6 to ground.
**Operation:** The capacitor $C$ charges through $(R_A + R_B)$ until it hits $\frac{2}{3} V_{CC}$. The upper comparator triggers the flip-flop, driving the output LOW and turning ON the discharge transistor. $C$ then discharges strictly through $R_B$ until it drops to $\frac{1}{3} V_{CC}$. The lower comparator triggers the flip-flop, turning OFF the discharge transistor and driving the output HIGH. The cycle repeats infinitely.

**(c) Design an active triangular wave generator using a 555 and an op-amp ($f_o = 10\text{ kHz}$). [04 Marks]**
**Design Strategy:**
A triangular wave generator is created by feeding a $50\%$ duty cycle square wave into an active op-amp integrator.
1.  **Stage 1: 555 Square Wave Generator ($10\text{ kHz}$)**
    To get a $50\%$ duty cycle, use the astable configuration with a bypass diode across $R_B$.
    $t_{charge} = 0.693 R_A C$. $t_{discharge} = 0.693 R_B C$.
    For $50\%$, $R_A = R_B$. Let $C = 10\text{ nF}$.
    $$
    f_o = \frac{1.44}{2 R_A C} = 10,000\text{ Hz} \Rightarrow R_A = \frac{1.44}{20000 \times 10^{-8}} = 7.2\text{ k}\Omega
    $$
    Set $R_A = 7.2\text{ k}\Omega$ and $R_B = 7.2\text{ k}\Omega$.
2.  **Stage 2: Op-Amp Integrator**
    Feed the $10\text{ kHz}$ square wave from the 555 output to an op-amp integrator.
    For good integration, the integrator's RC time constant should be roughly equivalent to the wave period ($T = 100\ \mu\text{s}$). Let $R_{int} = 10\text{ k}\Omega$ and $C_{int} = 10\text{ nF}$ ($\tau = 100\ \mu\text{s}$).
    The integrator ramps linearly up and down in response to the constant HIGH/LOW square wave inputs, yielding a perfect triangular wave.

---

## SECTION - B

### Q.5
**(a) Explain how an op-amp can be configured to act as an instrumentation amplifier. [03 Marks]**
**Answer:**
A standard instrumentation amplifier uses three op-amps. The first two op-amps act as high-input-impedance non-inverting buffers (the input stage), which do not load the delicate signal source. They amplify the differential signal while passing the common-mode signal with a gain of strictly 1. Their outputs are fed into a third op-amp configured as a standard differential amplifier (subtractor). This third stage strips away the common-mode noise and amplifies strictly the desired differential signal. The total differential gain can be easily tuned using a single resistor ($R_G$) placed between the two input buffers.

**(b) Design an op-amp circuit: $V_o = 0.5 V_1 + V_2 + 2 \int V_3 d t - 5 \frac{d V_4}{d t}$. [04 Marks]**
**Design Strategy:**
Rewrite as an inverting summation: $V_o = - \left( -0.5 V_1 - V_2 - 2 \int V_3 d t + 5 \frac{d V_4}{d t} \right)$.
1.  **Stage 1 ($V_1$):** Inverting amplifier. Gain = $-0.5$ ($R_i = 20\text{k}, R_f = 10\text{k}$). Output is $-0.5 V_1$.
2.  **Stage 2 ($V_2$):** Inverting amplifier. Gain = $-1$ ($R_i = 10\text{k}, R_f = 10\text{k}$). Output is $-V_2$.
3.  **Stage 3 ($V_3$):** Inverting Integrator. Transfer = $-\frac{1}{RC}\int$. We need $-2\int$, so $RC = 0.5\text{ s}$ ($R = 500\text{k}, C = 1\mu\text{F}$). Output is $-2 \int V_3 dt$.
4.  **Stage 4 ($V_4$):** Differentiator. Transfer = $-RC\frac{d}{dt}$. We need a final term of $+5\frac{d}{dt}$. So the input to the final summer must be $+5\frac{d}{dt}$. The differentiator gives $-5\frac{d}{dt}$ if $RC = 5$ ($R=5\text{M}, C=1\mu\text{F}$). Pass this through a unity-gain inverting amplifier to get $+5 \frac{d V_4}{d t}$.
Feed the outputs of all 4 stages into a final 4-input unity-gain inverting summing amplifier.

**(c) Determine the closed-loop output voltage $V_o$ of the multi-input summing circuit. [03 Marks]**
**Solution:**
Using Millman's Theorem, the voltage at the non-inverting node ($V_+$) is:
$$
V_+ = \frac{ \frac{V_a}{R_a} + \frac{V_b}{R_b} + \frac{V_c}{R_c} }{ \frac{1}{R_a} + \frac{1}{R_b} + \frac{1}{R_c} }
$$
The op-amp is configured as a non-inverting amplifier. The gain is:
$$
A_v = 1 + \frac{R_f}{R_1}
$$
Therefore, the total closed-loop output voltage is:
$$
V_o = V_+ \left( 1 + \frac{R_f}{R_1} \right) = \left( 1 + \frac{R_f}{R_1} \right) \left[ \frac{ \frac{V_a}{R_a} + \frac{V_b}{R_b} + \frac{V_c}{R_c} }{ \frac{1}{R_a} + \frac{1}{R_b} + \frac{1}{R_c} } \right]
$$

---

### Q.6
**(a) What is an active filter? Why are they superior? [03 Marks]**
*(Answer identical to 2020 Q.4(a). Uses op-amps. Superior because they provide voltage gain, have no loading effect between stages due to op-amp isolation, and eliminate heavy, expensive inductors).*

**(b) Differentiate between Bessel, Butterworth, and Chebyshev filters. [03 Marks]**
1.  **Butterworth:** Optimized for a "maximally flat" passband with $0\text{ dB}$ ripple. It has a moderate transition slope (roll-off rate).
2.  **Chebyshev:** Optimized for the steepest possible transition slope between the passband and stopband. However, this comes at the cost of deliberate, unavoidable ripples in the passband gain.
3.  **Bessel:** Optimized for a perfectly linear phase response (constant group delay). It ensures that all frequencies are delayed by the exact same amount of time, preserving the physical shape of complex square/pulse waves. It has the poorest transition slope of the three.

**(c) Design an active Sallen-Key bandpass filter ($100\text{ kHz}$ to $300\text{ kHz}$). [04 Marks]**
**Design Strategy:** Cascade a High-Pass Filter ($f_L = 100\text{ kHz}$) and a Low-Pass Filter ($f_H = 300\text{ kHz}$).
1.  **Stage 1: High-Pass Filter ($100\text{ kHz}$):**
    Let $C = 1\text{ nF} = 10^{-9}\text{ F}$.
    $$
    R = \frac{1}{2\pi f_L C} = \frac{1}{2\pi (100,000) (10^{-9})} = 1591\ \Omega \approx 1.6\text{ k}\Omega
    $$
2.  **Stage 2: Low-Pass Filter ($300\text{ kHz}$):**
    Let $C = 1\text{ nF} = 10^{-9}\text{ F}$.
    $$
    R = \frac{1}{2\pi f_H C} = \frac{1}{2\pi (300,000) (10^{-9})} = 530.5\ \Omega \approx 530\ \Omega
    $$
*(Note: At these frequencies, a high GBWP, high-slew-rate operational amplifier must be specified to prevent intrinsic op-amp roll-off from ruining the $300\text{ kHz}$ response).*

---

### Q.7
**(a) Explain operating states of monostable and astable multivibrators. [02 Marks]**
*(Identical to 2020 Q.8(a). Monostable: one stable state, requires trigger to enter transient state. Astable: zero stable states, continuously toggles automatically).*

**(b) Calculate the closed-loop gain $V_o/V_i$ of the two-stage cascaded op-amp feedback amplifier. [05 Marks]**
**Solution:**
Let the output of Stage 1 be $V_{o1}$. Let the output of Stage 2 be $V_o$.
1.  **Stage 2:** This is a non-inverting amplifier. The input is $V_{o1}$.
    The feedback network is $R_{f2} = 2\text{ k}\Omega$ and $R_{g2} = 10\text{ k}\Omega$.
    $$
    V_o = V_{o1} \left( 1 + \frac{2\text{k}}{10\text{k}} \right) = V_{o1} (1.2)
    $$
    $$
    V_{o1} = \frac{V_o}{1.2} = \frac{5}{6} V_o
    $$
2.  **Stage 1:** This is a summing inverting amplifier. By virtual ground, the inverting node voltage is $0\text{V}$.
    Applying KCL at the inverting node:
    $$
    \frac{V_i - 0}{5\text{ k}\Omega} + \frac{V_{o1} - 0}{10\text{ k}\Omega} + \frac{V_o - 0}{4\text{ k}\Omega} = 0
    $$
3.  **Substitute $V_{o1}$ into KCL:**
    $$
    \frac{V_i}{5} + \frac{\frac{5}{6} V_o}{10} + \frac{V_o}{4} = 0
    $$
    $$
    \frac{V_i}{5} + \frac{V_o}{12} + \frac{V_o}{4} = 0
    $$
    $$
    \frac{V_i}{5} + V_o \left( \frac{1}{12} + \frac{3}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + V_o \left( \frac{4}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + \frac{V_o}{3} = 0
    $$
4.  **Solve for Gain:**
    $$
    \frac{V_o}{3} = -\frac{V_i}{5}
    $$
    $$
    A_v = \frac{V_o}{V_i} = -\frac{3}{5} = -0.6
    $$

**(c) Design an antilogarithmic amplifier circuit. [04/05 Marks]**
**Design:**
*(Schematic: Connect a matched PN junction diode or a diode-connected NPN BJT in the input path (from $V_i$ to the inverting terminal). Connect a resistor $R_f$ in the feedback loop from $V_o$ to the inverting terminal. Non-inverting terminal is grounded).*
**Operation:**
The current through the input diode is exponentially related to the input voltage:
$$
I_{in} = I_s e^{V_i / V_T}
$$
By virtual ground, all of $I_{in}$ flows through the feedback resistor $R_f$. The output voltage is the drop across $R_f$:
$$
V_o = - I_{in} R_f = - I_s R_f e^{V_i / V_T}
$$
The output is proportional to the antilog (exponential) of the input voltage.

---

### Q.8
**(a) Explain engineering necessity of frequency and amplitude stability. [02 Marks]**
*   **Frequency Stability:** It is critically necessary to prevent the oscillator from drifting off its assigned frequency due to temperature fluctuations, component aging, or power supply variations. In RF communications, a drifting frequency causes the transmitter to bleed into adjacent channels and lose lock with the receiver.
*   **Amplitude Stability:** Without amplitude control, an oscillator with positive feedback will grow exponentially until the op-amp violently clips against the power rails, creating severe harmonic distortion. Stabilizing it ensures a pure, clean sine wave.

**(b) Draw circuit diagram and explain active Quadrature Oscillator. [04 Marks]**
**Answer:**
*(Schematic: Two cascaded op-amps. Op-Amp 1 is an inverting integrator. Op-Amp 2 is a non-inverting integrator. The output of Op-Amp 2 is fed all the way back to the input of Op-Amp 1 to complete the positive feedback loop).*
**Operating Principles:**
A quadrature oscillator generates two perfect sinusoidal signals that are exactly $90^\circ$ out of phase (a sine wave and a cosine wave).
1.  The first stage is an inverting integrator. It provides a $-90^\circ$ phase shift (integration) plus a $-180^\circ$ phase shift (inversion), totaling $-270^\circ$ (or $+90^\circ$).
2.  The second stage is a non-inverting integrator, which provides exactly a $-90^\circ$ phase shift.
3.  The total loop phase shift is $+90^\circ - 90^\circ = 0^\circ$ (or $360^\circ$), which strictly satisfies the Barkhausen criterion for sustained oscillation. The output of Stage 1 is the Cosine wave, and the output of Stage 2 is the Sine wave.

**(c) Design a Wien bridge oscillator for $f_o = 10\text{ kHz}$. [04 Marks]**
**Solution:**
$$
f_o = \frac{1}{2\pi R C} = 10,000\text{ Hz}
$$
Let $C = 1\text{ nF} = 10^{-9}\text{ F}$.
$$
R = \frac{1}{2\pi (10000)(10^{-9})} = 15915\ \Omega \approx 15.9\text{ k}\Omega
$$
To satisfy the Barkhausen gain criterion ($A_v \ge 3$):
$$
1 + \frac{R_f}{R_1} \ge 3 \Rightarrow R_f = 2 R_1
$$
Let $R_1 = 10\text{ k}\Omega$, then set $R_f = 20\text{ k}\Omega$ (use a $22\text{k}\Omega$ trim pot to fine-tune the amplitude and prevent clipping).
