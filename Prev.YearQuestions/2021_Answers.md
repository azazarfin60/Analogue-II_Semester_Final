# 📝 RUET 2021 Even Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2205)

---

## SECTION - A

### Q.1
**(a) Why are a low input impedance and a high output impedance desirable for some specific amplifier networks? [02 Marks]**

**Answer:**
This specific impedance profile (low $Z_i$ and high $Z_o$) characterizes an ideal **Current Amplifier**.
1.  **Low Input Impedance:** Allows the amplifier to draw the maximum possible current from the preceding signal source without creating a voltage bottleneck.
2.  **High Output Impedance:** Ensures that the amplifier acts as a stiff, ideal constant current source. It forces the amplified current completely into the load, unaffected by changes in the load resistance.

---

**(b) Determine $A_v, Z_i$, and $Z_o$ for the two-stage BJT amplifier circuit. [06 Marks]**

**Solution:**
Both transistors are identical NPNs with $\beta = 100, V_{BE} = 0.7\text{ V}, r_o = \infty$.

**Stage 1: Common-Emitter (Bypassed Emitter)**
1.  **DC Analysis:**
    $$V_{th1} = V_{CC} \frac{R_2}{R_1 + R_2} = 15\text{ V} \times \frac{25\text{ k}\Omega}{65\text{ k}\Omega + 25\text{ k}\Omega} = 15 \times \frac{25}{90} = 4.167\text{ V}$$
    $$R_{th1} = 65\text{ k}\Omega \parallel 25\text{ k}\Omega = 18.06\text{ k}\Omega$$
    $$I_{E1} = \frac{V_{th1} - V_{BE}}{R_{E1} + R_{th1}/\beta} = \frac{4.167 - 0.7}{400 + 18060/100} = \frac{3.467\text{ V}}{400 + 180.6} = \frac{3.467}{580.6} = 5.97\text{ mA}$$
2.  **AC Parameters:**
    $$r_{e1} = \frac{26\text{ mV}}{5.97\text{ mA}} = 4.35\ \Omega$$
    $$Z_{i1} = R_{th1} \parallel \beta r_{e1} = 18.06\text{ k}\Omega \parallel 100(4.35) = 18.06\text{ k}\Omega \parallel 435\ \Omega = 425\ \Omega$$

**Stage 2: Common-Emitter (Unbypassed Emitter)**
1.  **DC Analysis:**
    The schematic shows two $400\ \Omega$ resistors in series on the emitter ($R_{E2}$ and $R_{E2'}$). Total DC emitter resistance is $800\ \Omega$.
    $$V_{th2} = 15\text{ V} \times \frac{25}{90} = 4.167\text{ V}$$
    $$R_{th2} = 18.06\text{ k}\Omega$$
    $$I_{E2} = \frac{4.167 - 0.7}{800 + 180.6} = \frac{3.467\text{ V}}{980.6\ \Omega} = 3.535\text{ mA}$$
2.  **AC Parameters:**
    $$r_{e2} = \frac{26\text{ mV}}{3.535\text{ mA}} = 7.35\ \Omega$$
    Total unbypassed AC emitter resistance $R_E = 800\ \Omega$.
    $$Z_{i2} = R_{th2} \parallel \beta (r_{e2} + R_E) = 18.06\text{ k}\Omega \parallel 100(7.35 + 800) = 18.06\text{ k}\Omega \parallel 80.7\text{ k}\Omega \approx 14.76\text{ k}\Omega$$

**Cascaded Parameters:**
*   **(i) Overall Voltage Gain ($A_v$):**
    Stage 1 Voltage Gain ($A_{v1}$):
    $$A_{v1} = -\frac{R_{C1} \parallel Z_{i2}}{r_{e1}} = -\frac{1000 \parallel 14760}{4.35} = -\frac{936.5}{4.35} = -215.3$$
    Stage 2 Voltage Gain ($A_{v2}$):
    $$A_{v2} = -\frac{R_{C2} \parallel R_L}{r_{e2} + R_E} = -\frac{1000 \parallel 20000}{807.35} = -\frac{952.4}{807.35} = -1.18$$
    Total Voltage Gain ($A_v$):
    $$A_v = A_{v1} \times A_{v2} = (-215.3) \times (-1.18) = 254.0$$
*   **(ii) Input Impedance ($Z_i$):**
    $$Z_i = Z_{i1} = 425\ \Omega$$
*   **(iii) Output Impedance ($Z_o$):**
    Assuming $r_o = \infty$, the output impedance is strictly the collector resistor of Stage 2.
    $$Z_o = R_{C2} = 1\text{ k}\Omega$$

---

**(c) Design a 3-input NOR gate using CMOS technology and explain. [04 Marks]**

**Answer:**
**Design:**
A 3-input CMOS NOR gate consists of 6 transistors: 3 PMOS and 3 NMOS.
*   **Pull-up Network:** The 3 PMOS transistors are connected in **series** between the $+V_{DD}$ rail and the output node ($V_{out}$).
*   **Pull-down Network:** The 3 NMOS transistors are connected in **parallel** between the output node ($V_{out}$) and Ground.
*   The three inputs (A, B, C) are tied to corresponding PMOS/NMOS pairs.

**Operating Logic:**
For a NOR gate, the output is HIGH ($1$) *only* when ALL inputs are LOW ($0$).
1.  If A=0, B=0, and C=0: All 3 NMOS are OFF (breaking the path to ground). All 3 PMOS are ON. Since they are in series, they form a solid path from $+V_{DD}$ to $V_{out}$. The output is HIGH.
2.  If ANY input is HIGH (e.g., A=1): The corresponding NMOS turns ON, creating a direct short to Ground and pulling the output LOW. Simultaneously, the corresponding PMOS turns OFF, breaking the series chain and disconnecting the $+V_{DD}$ rail.

---

### Q.2
**(a) Discuss the effect of the number of cascaded stages on cutoff frequencies and bandwidth. [03 Marks]**

**Answer:**
*(Identical to 2020 Q.3(b). Cascading stages compounds both low-frequency and high-frequency attenuation. The lower cutoff frequency ($f_L$) shifts **higher** because of cascaded coupling capacitors. The upper cutoff frequency ($f_H$) shifts **lower** because of cascaded parasitic capacitances. Consequently, the overall bandwidth severely **shrinks**).*

---

**(b) Derive equations of $A_i$ and $A_v$ for the Darlington emitter-follower. [05 Marks]**

**Answer:**
*(Derivation is standard for Common-Collector Darlington).*
**Voltage Gain ($A_v$):**
The input voltage $V_i$ drops across the base-emitter junctions of $Q_1$ and $Q_2$, and the emitter resistor $R_E$. The output $V_o$ is taken across $R_E$.
$$V_i = i_{b1} \beta_1 r_{e1} + i_{b2} \beta_2 r_{e2} + i_e R_E$$
Since $i_{b2} = \beta_1 i_{b1}$ and $i_e = \beta_1 \beta_2 i_{b1}$:
$$V_i = i_{b1} [ \beta_1 r_{e1} + \beta_1 \beta_2 r_{e2} + \beta_1 \beta_2 R_E ]$$
$$V_o = i_e R_E = \beta_1 \beta_2 i_{b1} R_E$$
$$A_v = \frac{V_o}{V_i} = \frac{\beta_1 \beta_2 R_E}{\beta_1 r_{e1} + \beta_1 \beta_2 r_{e2} + \beta_1 \beta_2 R_E} \approx \frac{\beta_D R_E}{\beta_D R_E} \approx 1$$

**Current Gain ($A_i$):**
The input current splits between $R_B$ and the base of $Q_1$.
$$i_{b1} = i_{in} \frac{R_B}{R_B + Z_{base}}$$
The output current is $i_o = i_e = \beta_1 \beta_2 i_{b1} = \beta_D i_{b1}$.
$$A_i = \frac{i_o}{i_{in}} = \beta_D \frac{R_B}{R_B + Z_{base}}$$
Because $\beta_D$ is massive, the current gain is extremely high.

---

**(c) Design an NPN constant current source: $I = 4.65\text{ mA}, -V_{EE} = -20\text{ V}, V_E = -10.7\text{ V}$. Find $R_1, R_2, R_E$. [04 Marks]**

**Solution:**
1.  **Calculate $R_E$:**
    The voltage at the emitter is $-10.7\text{V}$, and the bottom of the resistor is at $-20\text{V}$.
    The current through the resistor is the emitter current $I_E \approx I_C = 4.65\text{ mA}$.
    $$R_E = \frac{V_E - (-V_{EE})}{I_E} = \frac{-10.7\text{ V} - (-20\text{ V})}{4.65\text{ mA}} = \frac{9.3\text{ V}}{4.65\text{ mA}} = 2000\ \Omega = 2\text{ k}\Omega$$
2.  **Calculate Base Voltage ($V_B$):**
    $$V_B = V_E + V_{BE} = -10.7\text{ V} + 0.7\text{ V} = -10.0\text{ V}$$
3.  **Design the Voltage Divider ($R_1, R_2$):**
    Resistor $R_1$ connects Ground ($0\text{V}$) to the Base ($-10\text{V}$). Resistor $R_2$ connects the Base ($-10\text{V}$) to $-V_{EE}$ ($-20\text{V}$).
    For a stiff voltage divider, we assume the base current is negligible compared to the divider current.
    The voltage drop across $R_1$ is $0 - (-10) = 10\text{V}$.
    The voltage drop across $R_2$ is $-10 - (-20) = 10\text{V}$.
    Since the voltage drops are equal, the resistors must be equal: $R_1 = R_2$.
    To ensure a "stiff" divider, the current through the divider should be roughly 10x the base current ($I_B \approx 4.65\text{mA}/100 = 46.5\ \mu\text{A}$). Let $I_{div} = 500\ \mu\text{A}$.
    $$R_1 + R_2 = \frac{20\text{ V}}{500\ \mu\text{A}} = 40\text{ k}\Omega$$
    Therefore, $R_1 = 20\text{ k}\Omega$ and $R_2 = 20\text{ k}\Omega$. (Any equal pair between $5\text{k}$ and $20\text{k}$ is acceptable).

---

### Q.3
**(a) What are the physical functions of coupling and bypass capacitors? [03 Marks]**

**Answer:**
*   **Coupling Capacitors:** They are placed in series between amplifier stages. Their function is to block the DC bias voltages of one stage from bleeding into and upsetting the delicate DC bias of the next stage, while simultaneously allowing the AC signal to pass through unimpeded.
*   **Bypass Capacitors:** They are placed in parallel with emitter or source resistors. Their function is to provide a low-impedance (short-circuit) path to ground for the AC signal, effectively bypassing the resistor at signal frequencies. This prevents AC degenerative negative feedback, thereby restoring the amplifier to its maximum theoretical voltage gain.

---

**(b) Calculate the lower-cutoff frequency for the JFET CS amplifier. [05 Marks]**

**Solution:**
**1. DC Biasing (Self-Bias):**
The gate is at $0\text{V}$ DC (isolated by capacitor). $V_{GS} = -I_D R_S = -2200 I_D$.
Given $I_{DSS} = 10\text{ mA}, V_P = -6\text{ V}$:
$$I_D = 10\text{ mA} \left(1 - \frac{V_{GS}}{-6}\right)^2 = 10\text{ mA} \left(1 + \frac{V_{GS}}{6}\right)^2$$
Substitute $I_D = -V_{GS}/2200$:
$$\frac{-V_{GS}}{2200} = 0.01 \left(1 + \frac{V_{GS}}{3} + \frac{V_{GS}^2}{36}\right) \Rightarrow -0.0454 V_{GS} = 1 + 0.333 V_{GS} + 0.0278 V_{GS}^2$$
$$0.0278 V_{GS}^2 + 0.378 V_{GS} + 1 = 0$$
Using the quadratic formula, $V_{GS} = -3.58\text{ V}$.
$$g_m = \frac{2(10\text{ mA})}{6\text{ V}} \left(1 - \frac{-3.58}{-6}\right) = 3.33\text{ mS} \times (1 - 0.597) = 1.34\text{ mS}$$

**2. Cutoff Frequencies:**
*   **Input ($f_{LS}$):**
    $R_i = R_{G1} \parallel R_{G2} = 220\text{ k}\Omega \parallel 68\text{ k}\Omega = 51.9\text{ k}\Omega$.
    $$f_{LS} = \frac{1}{2\pi (R_s + R_i) C_{s1}} = \frac{1}{2\pi (1.5\text{ k}\Omega + 51.9\text{ k}\Omega) 1\ \mu\text{F}} = \frac{1}{2\pi (53400) (10^{-6})} = 2.98\text{ Hz}$$
*   **Output ($f_{LC}$):**
    $$f_{LC} = \frac{1}{2\pi (R_D + R_L) C_c} = \frac{1}{2\pi (3.9\text{ k}\Omega + 5.6\text{ k}\Omega) 6.8\ \mu\text{F}} = \frac{1}{2\pi (9500) (6.8 \times 10^{-6})} = 2.46\text{ Hz}$$
*   **Source Bypass ($f_{LE}$):**
    $$f_{LE} = \frac{1}{2\pi (R_S \parallel \frac{1}{g_m}) C_{s2}} = \frac{1}{2\pi \left( 2200 \parallel \frac{1}{1.34\text{ mS}} \right) 10\ \mu\text{F}} = \frac{1}{2\pi (2200 \parallel 746) 10\ \mu\text{F}}$$
    $$f_{LE} = \frac{1}{2\pi (557\ \Omega) 10\ \mu\text{F}} = 28.5\text{ Hz}$$

**Overall Lower-Cutoff Frequency:**
Dominated by the highest individual cutoff:
$$f_L \approx f_{LE} = 28.5\text{ Hz}$$

---

## SECTION - B

### Q.3 (continued)
**(c) Design an op-amp based voltage subtractor circuit: $V_o = V_1 - V_2$. [04 Marks]**

**Design Strategy:**
A voltage subtractor is a differential amplifier.
*(Schematic: Connect $V_1$ to the non-inverting terminal through resistor $R_1$. Connect the non-inverting terminal to ground through resistor $R_2$. Connect $V_2$ to the inverting terminal through resistor $R_3$. Connect a feedback resistor $R_4$ from the output $V_o$ to the inverting terminal).*
To achieve exactly $V_o = V_1 - V_2$, we set all four resistors to the exact same value. Let $R_1 = R_2 = R_3 = R_4 = 10\text{ k}\Omega$.
The transfer function is:
$$V_o = V_1 \left( \frac{R_2}{R_1 + R_2} \right) \left( 1 + \frac{R_4}{R_3} \right) - V_2 \left( \frac{R_4}{R_3} \right)$$
Substituting $R = 10\text{ k}\Omega$:
$$V_o = V_1 \left( \frac{1}{2} \right) (2) - V_2 (1) = V_1 - V_2$$

---

### Q.4
**(a) Active vs Passive filters. Characteristics of Sallen-Key Butterworth LPF. [04 Marks]**
*(Answer identical to 2020 Q.4(a). Active uses op-amps for gain, passive uses strictly RLC).*
**Sallen-Key Butterworth LPF Characteristics:**
1.  Provides a maximally flat passband response ($0\text{ dB}$ ripple).
2.  Quality factor is mathematically fixed at $Q = 0.707$.
3.  Rolls off sharply at $-40\text{ dB/decade}$ in the stopband (being a 2nd-order topology).

**(b) Formulate equations for charging/discharging time of 555-timer astable. [04 Marks]**
*(Answer identical to 2020 Q.6(a), extended to astable configuration where $t_{charge} = 0.693(R_A + R_B)C$ and $t_{discharge} = 0.693 R_B C$).*

**(c) Design Sallen-Key Butterworth LPF: Unity Gain ($K=1$), $f_c = 10\text{ kHz}, Q = 0.707$. [04 Marks]**
**Solution:**
For a unity-gain ($K=1$) Sallen-Key filter, the op-amp is configured as a voltage follower (output tied directly to inverting input). To set $Q = 0.707$, we must use unequal capacitors. Let $R_1 = R_2 = R$.
The quality factor is given by: $Q = 0.5 \sqrt{\frac{C_1}{C_2}}$.
$$0.707 = 0.5 \sqrt{\frac{C_1}{C_2}} \Rightarrow 1.414 = \sqrt{\frac{C_1}{C_2}} \Rightarrow \frac{C_1}{C_2} = 2 \Rightarrow C_1 = 2 C_2$$
Let $C_2 = 10\text{ nF}$. Then $C_1 = 20\text{ nF}$.
The cutoff frequency is:
$$f_c = \frac{1}{2\pi R \sqrt{C_1 C_2}} = 10,000\text{ Hz}$$
$$10000 = \frac{1}{2\pi R \sqrt{200 \times 10^{-18}}} = \frac{1}{2\pi R (14.14\text{ nF})}$$
$$R = \frac{1}{2\pi \times 10000 \times 14.14\times 10^{-9}} = 1125\ \Omega \approx 1.1\text{ k}\Omega$$
**Design Values:** $K=1$, $R_1 = R_2 = 1.1\text{ k}\Omega$, $C_1 = 20\text{ nF}$, $C_2 = 10\text{ nF}$.

---

### Q.5
**(a) Explain "virtual ground" and derive non-inverting gain. [04 Marks]**
**Answer:**
**Virtual Ground:** In a closed-loop negative feedback op-amp circuit, the massive open-loop gain forces the differential voltage between the two inputs to zero. Since $V_{out} = A_d (V_+ - V_-)$ and $A_d \rightarrow \infty$, the voltage difference $(V_+ - V_-)$ must be infinitely small (effectively $0\text{V}$). Therefore, the inverting terminal is "virtually" at the same voltage as the non-inverting terminal without any physical connection between them.
**Derivation:**
For a non-inverting amplifier, $V_i$ is applied to $V_+$. By virtual ground, $V_- = V_i$.
A resistor $R_i$ connects $V_-$ to ground. A feedback resistor $R_f$ connects $V_o$ to $V_-$.
Since the op-amp draws no current, the current through $R_i$ equals the current through $R_f$:
$$\frac{0 - V_-}{R_i} = \frac{V_- - V_o}{R_f}$$
Substitute $V_- = V_i$:
$$-\frac{V_i}{R_i} = \frac{V_i - V_o}{R_f}$$
$$-V_i \frac{R_f}{R_i} = V_i - V_o \Rightarrow V_o = V_i + V_i \frac{R_f}{R_i} = V_i \left( 1 + \frac{R_f}{R_i} \right)$$

**(b) Justify: Integrator is LPF, Differentiator is HPF. [04 Marks]**
**Answer:**
*   **Integrator:** Transfer function $H_{int}(f) \propto \frac{1}{f}$. As frequency increases, the gain strictly decreases. Thus, it passes low frequencies and heavily attenuates high frequencies, mathematically acting as an ideal Low-Pass Filter.
*   **Differentiator:** Transfer function $H_{diff}(f) \propto f$. As frequency increases, the gain strictly increases. Thus, it blocks DC and low frequencies while amplifying high frequencies, mathematically acting as a High-Pass Filter.

**(c) Design Wien bridge oscillator for $f_o = 20\text{ kHz}$. [04 Marks]**
**Solution:**
$$f_o = \frac{1}{2\pi R C} = 20,000\text{ Hz}$$
Let $C = 1\text{ nF}$.
$$R = \frac{1}{2\pi (20000)(10^{-9})} = 7957\ \Omega \approx 8\text{ k}\Omega$$
Gain network: $R_F = 2 R_1$. Let $R_1 = 10\text{ k}\Omega$, then $R_F = 20\text{ k}\Omega$.

---

### Q.6
**(a) Differentiate between comparator and oscillator. [02 Marks]**
*   **Comparator:** Uses an open-loop or positive feedback configuration (Schmitt) designed to be highly non-linear. Its transfer characteristic is a harsh step function that outputs DC saturation voltages ($+V_{sat}$ or $-V_{sat}$) based on the input crossing a threshold.
*   **Oscillator:** Uses positive feedback designed specifically to meet the Barkhausen criterion ($A\beta = 1$). Its transfer characteristic is a continuous, self-sustaining sine wave generator at a singular frequency without any external input.

**(b) Effect of input noise on comparator? Practical solution? [02 Marks]**
*(Same as previous years: False triggering. Solved by Schmitt Trigger hysteresis).*

**(c) Draw $v_o(t)$ for the clamping network. [04 Marks]**
**Solution:**
The inverting amplifier has a gain $A_{CL} = -20\text{k} / 2\text{k} = -10$.
The input is $v_{in}(t) = 1\sin(\omega t)\text{ V}$.
The theoretical output is $v_o(t) = -10\sin(\omega t)\text{ V}$, which oscillates between $+10\text{ V}$ and $-10\text{ V}$.
Diode $D_1$ limits the output to a maximum of $+15\text{V}$ (tied to $+15\text{V}$ rail). Diode $D_2$ limits the output to a minimum of $-15\text{V}$ (tied to $-15\text{V}$ rail).
Because the theoretical peak of $\pm 10\text{V}$ never exceeds the $\pm 15\text{V}$ limits, the diodes remain reverse-biased and never conduct.
The output $v_o(t)$ is a clean, perfectly unclipped inverted sine wave with an amplitude of $10\text{ V}$.

**(d) Design: $v_o = 5 v_1 + 6 v_2 - 0.5 \frac{d v_3}{d t} + 0.5 \int v_4 d t$. [04 Marks]**
**Design Strategy:**
Using an inverting summing configuration $v_o = -(V_A + V_B + V_C + V_D)$, we require the inputs to the summer to be: $-5v_1$, $-6v_2$, $+0.5 \frac{dv_3}{dt}$, and $-0.5 \int v_4 dt$.
*   **For $v_1$:** Inverting amp ($A_v = -5$).
*   **For $v_2$:** Inverting amp ($A_v = -6$).
*   **For $v_3$:** Inverting differentiator ($V_C = -RC \frac{dv_3}{dt}$). Set $RC = 0.5$. (To get positive sign, pass it through an inverter, yielding $+0.5 \frac{dv_3}{dt}$). Wait, summer will invert it back to $-0.5$. So feed the differentiator output directly into the summer! The differentiator outputs $-0.5 \frac{dv_3}{dt}$. The summer inverts it to $+0.5 \frac{dv_3}{dt}$.
*   **For $v_4$:** Inverting integrator ($V_D = -\frac{1}{RC} \int v_4 dt$). Set $1/RC = 0.5 \Rightarrow RC = 2$. Output is $-0.5 \int v_4 dt$. The summer inverts it to $+0.5 \int v_4 dt$.
Feed all these intermediate signals into a unity-gain inverting summer to produce the final $v_o$.

---

### Q.7
**(a) Define Slew Rate and CMRR. [02 Marks]** *(Already answered).*
**(b) Voltage Follower. Where and why employed? [02 Marks]**
*(Answered in 2017 Q.5(b). Used for impedance matching/buffering).*
**(c) Series-shunt feedback $R_{if}$ and $R_{of}$. [04 Marks]**
*(Answered in 2018 Q.6(a). $R_{if} = R_i(1+A\beta)$, $R_{of} = R_o/(1+A\beta)$).*
**(d) Design 555-timer sawtooth generator: $f_0 = 10\text{ kHz}$, duty cycle $= 0.25$. [04 Marks]**
**Solution:**
A standard 555 astable cannot produce a duty cycle less than 50%. To achieve $25\%$, an ideal diode must be placed across $R_B$ to bypass it during the charging phase.
Duty Cycle $D = \frac{R_A}{R_A + R_B} = 0.25$.
$$R_A = 0.25 R_A + 0.25 R_B \Rightarrow 0.75 R_A = 0.25 R_B \Rightarrow R_B = 3 R_A$$
Frequency $f_o = \frac{1.44}{(R_A + R_B)C} = \frac{1.44}{4 R_A C} = 10,000\text{ Hz}$.
$$4 R_A C = 1.44 \times 10^{-4}$$
Let $C = 10\text{ nF}$.
$$R_A = \frac{1.44 \times 10^{-4}}{4 \times 10^{-8}} = 3600\ \Omega = 3.6\text{ k}\Omega$$
$$R_B = 3 \times 3.6\text{ k}\Omega = 10.8\text{ k}\Omega$$

---

### Q.8
**(a) 555 internal blocks. [04 Marks]** *(Already answered).*
**(b) Calculate output $V_o$ for the instrumentation amplifier. $V_{in} = 50\text{ mV}$ peak. [04 Marks]**
**Solution:**
**Stage 1 (Buffers):**
Op-Amp 2 (Op2) is configured as a simple voltage follower.
$$V_{o2} = 50\text{ mV}$$
Op-Amp 1 (Op1) is configured as an inverting amplifier taking $V_{o2}$ as input.
$$V_{o1} = -\frac{R_{f1}}{R_g} V_{o2} = -\frac{100\text{ k}\Omega}{10\text{ k}\Omega} (50\text{ mV}) = -500\text{ mV}$$
**Stage 2 (Differential Amplifier):**
The output op-amp processes $V_{o1}$ and $V_{o2}$.
The voltage at the non-inverting terminal ($V_p$) is derived from $V_{o2}$ via a voltage divider ($15\text{k}\Omega$ and $15\text{k}\Omega$):
$$V_p = V_{o2} \left( \frac{15\text{k}}{15\text{k} + 15\text{k}} \right) = \frac{50\text{ mV}}{2} = 25\text{ mV}$$
The output voltage $V_o$ is calculated using superposition:
$$V_o = -V_{o1} \left(\frac{30\text{k}}{10\text{k}}\right) + V_p \left(1 + \frac{30\text{k}}{10\text{k}}\right)$$
$$V_o = -(-500\text{ mV})(3) + (25\text{ mV})(4) = 1500\text{ mV} + 100\text{ mV} = 1600\text{ mV}$$
$$V_o = 1.6\text{ V (peak)}$$

**(c) Missing pulse detector circuit. [04 Marks]** *(Already answered in 2020 Q.6(c)).*
