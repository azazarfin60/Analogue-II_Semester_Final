# 📝 RUET 2019 Even Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2205)

---

## SECTION - A

### Q.1
**(a) For the cascaded CE-CS multistage amplifier, draw the AC equivalent circuit and derive the equations for $A_v, Z_i$, and $Z_o$. [08 Marks]**

**Answer:**
**AC Equivalent Circuit Construction:**
1.  Short all DC voltage sources to ground ($+V_{DD}$ and $+V_{CC}$ become AC grounds).
2.  Short all coupling capacitors ($C_1, C_2, C_3$) and bypass capacitors ($C_S, C_E$) to ground.
3.  Replace the JFET with its small-signal model: an open circuit at the gate, and a dependent current source $g_m v_{gs}$ from drain to source in parallel with internal output resistance $r_d$.
4.  Replace the BJT with its hybrid-$\pi$ / $r_e$ small-signal model: an input resistance $\beta r_e$ between base and emitter, and a dependent current source $\beta i_b$ from collector to emitter in parallel with internal output resistance $r_o$.

*AC Equivalent Schematic Description:*
*   **Input:** $v_i$ connects to $R_G$ (to ground). This is the JFET gate.
*   **JFET Output:** The drain has a current source $g_m v_{gs}$, parallel to $r_d$ and $R_D$ (both to ground). This node is coupled directly to the BJT base.
*   **BJT Input:** The base node connects to $R_1 \parallel R_2$ (to ground) and $\beta r_e$ (to ground, since emitter is bypassed).
*   **BJT Output:** The collector has a current source $\beta i_b$, parallel to $r_o, R_C$, and $R_L$ (all to ground). This node provides $v_o$.

**Derivations:**
**(ii) Input Impedance ($Z_i$):**
Looking into the input terminals (JFET gate), the only component is $R_G$ since the JFET gate draws zero current.
$$
Z_i = R_G
$$

**(iii) Output Impedance ($Z_o$):**
Looking back into the output terminals (BJT collector) with $v_i = 0$ and removing $R_L$:
$$
Z_o = r_o \parallel R_C \approx R_C \quad (\text{since usually } r_o \gg R_C)
$$

**(i) Overall Voltage Gain ($A_v$):**
Let $Z_{i2}$ be the input impedance of the second stage (BJT).
$$
Z_{i2} = R_1 \parallel R_2 \parallel \beta r_e
$$
The AC load on the JFET drain is $R_{L1} = r_d \parallel R_D \parallel Z_{i2}$.
The voltage gain of the first stage (CS) is:
$$
A_{v1} = \frac{v_{b2}}{v_i} = -g_m (r_d \parallel R_D \parallel Z_{i2})
$$
The AC load on the BJT collector is $R_{L2} = r_o \parallel R_C \parallel R_L \approx R_C \parallel R_L$.
The voltage gain of the second stage (CE) is:
$$
A_{v2} = \frac{v_o}{v_{b2}} = -\frac{r_o \parallel R_C \parallel R_L}{r_e} \approx -\frac{R_C \parallel R_L}{r_e}
$$
The overall voltage gain is the product of the two stage gains:
$$
A_v = A_{v1} \times A_{v2} = \left[ -g_m (r_d \parallel R_D \parallel Z_{i2}) \right] \times \left[ -\frac{R_C \parallel R_L}{r_e} \right]
$$
$$
A_v = g_m (r_d \parallel R_D \parallel Z_{i2}) \times \frac{R_C \parallel R_L}{r_e}
$$

---

**(b) Draw a current mirror circuit using BJTs and explain its operating principles. [04 Marks]**

**Answer:**
*(Schematic Description: A reference resistor $R$ connects $+V_{CC}$ to the collector of an NPN transistor $Q_1$. The base of $Q_1$ is shorted to its collector (diode-connected). The base of $Q_1$ is tied to the base of a matched NPN transistor $Q_2$. Both emitters are grounded. The collector of $Q_2$ provides the constant output current $I_{out}$.)*

**Operating Principle:**
1.  The reference current flows through $R$ and $Q_1$. Because $Q_1$ is diode-connected, it creates a specific base-emitter voltage drop ($V_{BE}$) based on this current.
    $$
    I_{ref} = \frac{V_{CC} - V_{BE}}{R}
    $$
2.  Because $Q_1$ and $Q_2$ are precisely matched and their bases and emitters are wired in parallel, $Q_2$ is forced to have the exact same $V_{BE}$ as $Q_1$.
3.  According to the Ebers-Moll equation, identical transistors with identical $V_{BE}$ will draw identical collector currents. Thus, $I_{out} = I_{ref}$ (ignoring small base current errors). The circuit "mirrors" the reference current into the load attached to $Q_2$.

---

### Q.2
**(a) Calculate $A_{v1}, A_{v2}, A_v$ for the cascode BJT amplifier. Draw wave shapes for $v_i(t) = 10\sin(\omega t)\text{ mV}$. [05 Marks]**

**Solution:**
**1. DC Analysis:**
The base of $Q_2$ is biased by a voltage divider. The total resistance is $R_{total} = 7.5\text{k} + 6.2\text{k} + 3.9\text{k} = 17.6\text{ k}\Omega$.
Voltage at Node A (Base of $Q_2$):
$$
V_{B2} = 20\text{V} \times \frac{6.2\text{k} + 3.9\text{k}}{17.6\text{k}} = 20 \times \frac{10.1}{17.6} = 11.47\text{ V}
$$
Voltage at Node B (Base of $Q_1$):
$$
V_{B1} = 20\text{V} \times \frac{3.9\text{k}}{17.6\text{k}} = 4.43\text{ V}
$$
Emitter voltage of $Q_1$: $V_{E1} = V_{B1} - 0.7\text{V} = 4.43 - 0.7 = 3.73\text{ V}$.
Emitter current of $Q_1$: $I_{E1} = V_{E1} / R_E = 3.73\text{V} / 1\text{ k}\Omega = 3.73\text{ mA}$.
Since $Q_1$ and $Q_2$ are in series, $I_{E2} \approx I_{C1} \approx I_{E1} = 3.73\text{ mA}$.
Dynamic resistances: $r_{e1} = r_{e2} = \frac{26\text{ mV}}{3.73\text{ mA}} = 6.97\ \Omega$.

**2. AC Voltage Gains:**
*   **Stage 1 ($Q_1$ - Common Emitter):** Its load is the input impedance of $Q_2$ (which is a Common Base stage). The input impedance of a CB stage is $r_{e2}$.
    $$
    A_{v1} = -\frac{\text{Load}}{r_{e1}} = -\frac{r_{e2}}{r_{e1}} = -\frac{6.97}{6.97} = -1
    $$
*   **Stage 2 ($Q_2$ - Common Base):** Its load is $R_C = 1.5\text{ k}\Omega$. A CB stage is non-inverting.
    $$
    A_{v2} = +\frac{R_C}{r_{e2}} = \frac{1500}{6.97} = 215.2
    $$
*   **Overall Gain ($A_v$):**
    $$
    A_v = A_{v1} \times A_{v2} = (-1) \times 215.2 = -215.2
    $$

**3. Output Wave Shape:**
$v_o(t) = A_v \cdot v_i(t) = -215.2 \times 10\sin(\omega t)\text{ mV} = -2.15\sin(\omega t)\text{ V}$.
*Sketch:* The input is a $10\text{mV}$ sine wave. The output is a $2.15\text{V}$ sine wave that is phase-inverted (shifted $180^\circ$) relative to the input.

---

**(b) Find the voltage gain ($A_v$) and current gain ($A_i$) for the Darlington emitter follower. [05/06 Marks]**

**Solution:**
**1. DC Analysis:**
Composite $\beta_D \approx \beta_1 \beta_2 = 50 \times 120 = 6000$.
Base voltage $V_B = 16 - I_{B1} R_B$.
Emitter voltage $V_E = I_E R_E = (\beta_D I_{B1}) R_E = 6000 I_{B1} (510) = 3.06\times 10^6 I_{B1}$.
KVL around Base-Emitter loop:
$$
V_{CC} - I_{B1}R_B - V_{BE1} - V_{BE2} - I_E R_E = 0
$$
$$
16 - I_{B1}(2.4\text{ M}\Omega) - 0.7 - 0.7 - I_{B1}(3.06\text{ M}\Omega) = 0
$$
$$
14.6 = I_{B1}(5.46\text{ M}\Omega) \Rightarrow I_{B1} = \frac{14.6}{5.46\times 10^6} = 2.67\ \mu\text{A}
$$
$$
I_E = 6000 \times 2.67\ \mu\text{A} = 16.02\text{ mA}
$$
$$
r_{e2} = \frac{26\text{ mV}}{16.02\text{ mA}} = 1.62\ \Omega
$$
$$
I_{E1} \approx I_{B2} = I_E / \beta_2 = 16.02\text{ mA} / 120 = 133.5\ \mu\text{A} \Rightarrow r_{e1} = \frac{26\text{ mV}}{133.5\ \mu\text{A}} = 194.7\ \Omega
$$

**2. AC Parameters:**
The input impedance looking into the base of $Q_1$:
$$
Z_{base} = \beta_1 [r_{e1} + \beta_2(r_{e2} + R_E)] \approx \beta_1 \beta_2 R_E = 6000 \times 510 = 3.06\text{ M}\Omega
$$
Total input impedance: $Z_i = R_B \parallel Z_{base} = 2.4\text{ M}\Omega \parallel 3.06\text{ M}\Omega = 1.34\text{ M}\Omega$.

**Voltage Gain ($A_v$):**
$$
A_v = \frac{R_E}{R_E + r_{e2} + r_{e1}/\beta_2} = \frac{510}{510 + 1.62 + 194.7/120} = \frac{510}{513.24} = 0.993
$$
$A_v \approx 1$.

**Current Gain ($A_i$):**
$$
A_i = \frac{i_o}{i_{in}} = \frac{v_o / R_E}{v_i / Z_i} = A_v \left( \frac{Z_i}{R_E} \right) = 0.993 \times \frac{1.34\text{ M}\Omega}{510\ \Omega} \approx 2609
$$

---

**(c) Write short notes on: (i) CMRR of an operational amplifier, (ii) Slew rate. [02 Marks]**

**Answer:**
*   **(i) CMRR (Common-Mode Rejection Ratio):** It is the ability of an op-amp to reject signals (like noise or interference) that appear equally and in-phase at both input terminals. It is defined as the ratio of the differential-mode gain to the common-mode gain, expressed in decibels ($CMRR = 20\log(A_d/A_{cm})$). Higher CMRR indicates a higher-quality op-amp.
*   **(ii) Slew Rate:** It is the maximum physical rate at which the op-amp's output voltage can change, measured in Volts per microsecond ($\text{V}/\mu\text{s}$). It dictates the absolute upper frequency limit for large-signal operation without introducing severe triangle-wave distortion.

---

### Q.3
**(a) Define Miller effect capacitance and inter-electrode capacitance. [04 Marks]**

**Answer:**
*   **Inter-electrode Capacitance:** These are the inevitable, microscopic parasitic capacitances formed across the semiconductor PN junctions of active devices (e.g., $C_{\pi}$ and $C_{\mu}$ in BJTs, or $C_{gs}$ and $C_{gd}$ in JFETs). They are physically caused by the separation of charge across the dielectric-like depletion regions of reverse/forward-biased junctions.
*   **Miller Effect Capacitance:** This is a phenomenon where an inter-electrode capacitance situated between the input and an inverting output (like $C_{gd}$ or $C_{cb}$) is mathematically multiplied by the voltage gain of the amplifier when viewed from the input terminal. Because of the phase inversion, a small voltage change at the input causes a huge voltage change across the capacitor, demanding much more charging current, making the capacitor appear $A_v$ times larger at the input ($C_{Mi} = C(1+A_v)$).

---

**(b) Determine the low-cutoff frequencies ($f_{Ls}, f_{Lc}, f_{LE}$) for the BJT common-emitter amplifier. [05 Marks]**

**Solution:**
**(Same circuit and values as 2018 CT-2 Q1)**
1.  **Dynamic Resistance:**
    $R_{th} = 40\text{k} \parallel 10\text{k} = 8\text{ k}\Omega$, $V_{th} = 4\text{ V}$.
    $I_E = \frac{4 - 0.7}{2\text{k} + 8\text{k}/100} = 1.586\text{ mA} \Rightarrow r_e = 16.39\ \Omega$.
2.  **Input ($f_{Ls}$):**
    $R_i = R_1 \parallel R_2 \parallel \beta r_e = 8\text{ k}\Omega \parallel 1.639\text{ k}\Omega = 1.36\text{ k}\Omega$.
    $f_{Ls} = \frac{1}{2\pi (R_s + R_i) C_{in}} = \frac{1}{2\pi(0 + 1.36\text{k})(10\mu)} = 11.7\text{ Hz}$.
3.  **Output ($f_{Lc}$):**
    $f_{Lc} = \frac{1}{2\pi (R_C + R_L) C_{out}} = \frac{1}{2\pi(4\text{k} + 2.2\text{k})(1\mu)} = 25.68\text{ Hz}$.
4.  **Emitter Bypass ($f_{LE}$):**
    $R_e = R_E \parallel r_e = 2000 \parallel 16.39 = 16.26\ \Omega$.
    $f_{LE} = \frac{1}{2\pi R_e C_E} = \frac{1}{2\pi(16.26)(20\mu)} = 489.5\text{ Hz}$.

---

**(c) Explain the high-frequency BJT model and derive upper-cutoff frequencies. [03 Marks]**

**Answer:**
At high frequencies, the standard BJT model fails because internal parasitic capacitances start shorting out the signals. The **Hybrid-$\pi$ high-frequency model** introduces two crucial capacitors: $C_\pi$ (base-emitter capacitance) and $C_\mu$ (base-collector capacitance).
To find the upper-cutoff frequencies:
1.  Apply the **Miller Theorem** to split the bridging capacitance $C_\mu$ into an equivalent input shunt capacitance $C_{Mi} = C_\mu (1 - A_v)$ and an output shunt capacitance $C_{Mo} = C_\mu (1 - 1/A_v)$.
2.  Sum the input capacitances: $C_{in(total)} = C_\pi + C_{Mi}$. Find the Thevenin resistance seen by this capacitor ($R_{Thi} = R_s \parallel R_1 \parallel R_2 \parallel \beta r_e$). The input high-cutoff is $f_{Hi} = \frac{1}{2\pi R_{Thi} C_{in(total)}}$.
3.  Sum the output capacitances: $C_{out(total)} = C_{Mo} + C_{wiring}$. Find the Thevenin resistance seen by this capacitor ($R_{Tho} = R_C \parallel R_L$). The output high-cutoff is $f_{Ho} = \frac{1}{2\pi R_{Tho} C_{out(total)}}$.

---

### Q.4
**(a) Design an op-amp circuit for: $v_o = -5 v_1 + 7 \frac{d v_2}{d t} + 10 \int v_3 d t$. [04 Marks]**

**Design Strategy:**
We will use three parallel stages feeding into a final inverting summer.
*   **Stage 1: Differentiator for $v_2$.**
    $$
    v_{o2} = -R_d C_d \frac{dv_2}{dt}
    $$
    We need a factor of $-7$ (so the final inverter makes it $+7$). Let $C_d = 10\ \mu\text{F}$ and $R_d = 700\text{ k}\Omega$, so $R_d C_d = 7$.
*   **Stage 2: Integrator for $v_3$.**
    $$
    v_{o3} = -\frac{1}{R_{int} C_{int}} \int v_3 dt
    $$
    We need a factor of $-10$ (so the final inverter makes it $+10$). Let $C_{int} = 1\ \mu\text{F}$ and $R_{int} = 100\text{ k}\Omega$, so $1/(R_{int}C_{int}) = 10$.
*   **Stage 3: Inverting Summer.**
    The inputs to the summer are $v_1, v_{o2},$ and $v_{o3}$. The output is:
    $$
    v_o = -\left( \frac{R_f}{R_1} v_1 + \frac{R_f}{R_x} v_{o2} + \frac{R_f}{R_y} v_{o3} \right)
    $$
    Let feedback resistor $R_f = 50\text{ k}\Omega$.
    *   For $v_1$: We want a total coefficient of $-5$. Thus $\frac{R_f}{R_1} = 5 \Rightarrow R_1 = 10\text{ k}\Omega$.
    *   For $v_{o2}$: We want a coefficient of $1$ (to pass the $-7$ cleanly to the inverter). Thus $R_x = R_f = 50\text{ k}\Omega$.
    *   For $v_{o3}$: We want a coefficient of $1$ (to pass the $-10$ cleanly to the inverter). Thus $R_y = R_f = 50\text{ k}\Omega$.

---

**(b) Slew rate $SR = 0.5\text{ V}/\mu\text{s}$, Gain $= 10$, $f = 40\text{ kHz}$. Find max peak-to-peak input signal without distortion. [04 Marks]**

**Solution:**
The absolute maximum slew rate equation is:
$$
SR \ge 2\pi f V_{p(out)}
$$
$$
0.5 \times 10^6\text{ V/s} = 2\pi (40,000) V_{p(out)}
$$
$$
V_{p(out)} = \frac{500,000}{80,000 \pi} = \frac{50}{8\pi} = 1.989\text{ V (peak)}
$$
The peak-to-peak output voltage is:
$$
V_{p-p(out)} = 2 \times 1.989\text{ V} = 3.979\text{ V}_{p-p}
$$
Since the closed-loop gain is 10, the maximum allowable peak-to-peak input voltage is:
$$
V_{p-p(in)} = \frac{V_{p-p(out)}}{\text{Gain}} = \frac{3.979\text{ V}}{10} = 0.398\text{ V}_{p-p} \quad (\text{or } 398\text{ mV}_{p-p})
$$

---

**(c) What is false triggering in a comparator? How is it solved? [04 Marks]**

**Answer:**
**False Triggering:** In a standard comparator, if the input signal has electrical noise riding on it and passes slowly through the reference threshold voltage, the noise will cross the threshold multiple times in rapid succession. This causes the op-amp output to chatter (rapidly switch back and forth between HIGH and LOW) instead of making a single, clean transition.
**Solution:** This is solved by using a **Schmitt Trigger** configuration. A Schmitt trigger employs positive feedback to create *hysteresis*—two separate thresholds (Upper Trigger Point and Lower Trigger Point). Once the noisy signal crosses the upper threshold, the output changes state and the threshold instantly snaps down to the lower point. The noise is not large enough to reach all the way down to the new lower threshold, effectively locking the output and preventing any false triggering or chattering.

---

## SECTION - B

### Q.5
**(a) Show how an op-amp can act as a Negative Impedance Converter (NIC). [04 Marks]**

**Answer:**
*(Schematic: Op-amp with a resistor $R$ connecting the output to the non-inverting (+) input. The input signal $V_i$ is applied to the (+) input. The output is also connected back to the inverting (-) input via a voltage divider consisting of $R_1$ and $R_2$).*
**Operation:**
By applying positive feedback through a specific resistor, the circuit injects current *back* into the signal source rather than drawing current from it.
Calculations show that the input impedance looking into the non-inverting terminal is negative. For a standard configuration where $R_1 = R_2$, the voltage gain to the output is 2. The voltage across the positive feedback resistor $R$ is $V_{out} - V_{in} = 2V_{in} - V_{in} = V_{in}$. The current flowing *out* of the input terminal toward the source is $i = V_{in} / R$. Therefore, the apparent impedance seen by the source is $Z_{in} = \frac{V_{in}}{-i} = -R$. It perfectly simulates a negative resistor.

---

**(b) Draw a precision half-wave rectifier and explain it. [04 Marks]**

**Answer:**
*(Schematic: An op-amp with the input signal connected to the non-inverting terminal. A diode is placed within the feedback loop, with its anode connected to the op-amp output and its cathode connected to the inverting terminal. The output of the circuit is taken from the diode's cathode, which is also tied to a load resistor to ground).*
**Operation:**
A standard diode requires $\sim 0.7\text{V}$ to turn on, clipping small signals. By placing the diode inside the op-amp's feedback loop, the op-amp uses its massive open-loop gain to compensate for the diode's voltage drop. If $V_{in} > 0$, the op-amp output swings to $+0.7\text{V}$ to forward-bias the diode, maintaining exactly $V_{in}$ at the cathode (output). If $V_{in} < 0$, the op-amp output swings to negative saturation, reverse-biasing the diode and completely disconnecting the output (resulting in $0\text{V}$ across the load). It acts as a mathematically perfect ideal diode.

---

**(c) Determine the closed-loop voltage gain $A_v = V_o/V_i$ of the two-stage circuit. [04 Marks]**

**Solution:**
**Stage 1 (Op-Amp A1):**
This is a non-inverting amplifier. The non-inverting terminal is connected to $V_i$ through a $180\text{ k}\Omega$ resistor. Since ideal op-amps draw zero current, there is no voltage drop across $R_{in}$. Thus, $V_{in(+)} = V_i$.
The feedback network consists of $R_2 = 200\text{ k}\Omega$ and $R_1 = 20\text{ k}\Omega$.
$$
V_{o1} = V_i \left( 1 + \frac{R_2}{R_1} \right) = V_i \left( 1 + \frac{200}{20} \right) = 11 V_i
$$

**Stage 2 (Op-Amp A2):**
This is a differential amplifier.
*   The inverting input receives $V_{o1}$ via $R_4 = 50\text{ k}\Omega$, with feedback $R_5 = 500\text{ k}\Omega$.
*   The non-inverting input is connected to the original $V_i$ node via $R_3 = 45\text{ k}\Omega$. Note there is no resistor from the non-inverting terminal to ground. Therefore, no current flows through $R_3$, and the voltage at the non-inverting terminal of A2 is exactly $V_i$.
Using superposition for a differential amplifier:
$$
V_o = V_{in(+)} \left( 1 + \frac{R_5}{R_4} \right) - V_{in(-)} \left( \frac{R_5}{R_4} \right)
$$
$$
V_o = V_i \left( 1 + \frac{500}{50} \right) - V_{o1} \left( \frac{500}{50} \right)
$$
$$
V_o = V_i (11) - V_{o1} (10)
$$
Substitute $V_{o1} = 11 V_i$:
$$
V_o = 11 V_i - 10(11 V_i) = 11 V_i - 110 V_i = -99 V_i
$$
**Voltage Gain:** $A_v = \frac{V_o}{V_i} = -99$.

---

### Q.6
**(a) Prove Colpitts frequency formula. [04 Marks]**
*(Identical proof to 2018 Q.5(b). By summing the reactive impedances in the tank loop $j\omega L + \frac{1}{j\omega C_1} + \frac{1}{j\omega C_2} = 0$, leading to $f_o = \frac{1}{2\pi} \sqrt{\frac{C_1+C_2}{L C_1 C_2}}$).*

**(b) Design an active 1st-order high-pass filter. What is the drawback? [04 Marks]**
**Design:** Place a capacitor $C$ in series and a resistor $R$ to ground at the non-inverting input of an op-amp. Configure the op-amp as a non-inverting amplifier with resistors $R_f$ and $R_1$. The cutoff frequency is $f_c = \frac{1}{2\pi R C}$.
**Drawback & Mitigation:** The main drawback of an active HPF is that an operational amplifier does not have infinite bandwidth; its open-loop gain drops at high frequencies (Gain-Bandwidth limit). Thus, an active HPF eventually turns into a low-pass filter at very high frequencies, making it a bandpass filter in reality. This is mitigated by selecting high-speed, high-bandwidth op-amps.

**(c) Design an active bandpass filter (50 kHz to 100 kHz). [04 Marks]**
**Design Strategy:** Cascade a High-Pass Filter (HPF) set to $f_L = 50\text{ kHz}$ and a Low-Pass Filter (LPF) set to $f_H = 100\text{ kHz}$.
1.  **HPF Stage ($50\text{ kHz}$):**
    Let $C_H = 1\text{ nF}$.
    $$
    R_H = \frac{1}{2\pi f_L C_H} = \frac{1}{2\pi \times 50\times 10^3 \times 1\times 10^{-9}} = 3.18\text{ k}\Omega
    $$
2.  **LPF Stage ($100\text{ kHz}$):**
    Let $C_L = 1\text{ nF}$.
    $$
    R_L = \frac{1}{2\pi f_H C_L} = \frac{1}{2\pi \times 100\times 10^3 \times 1\times 10^{-9}} = 1.59\text{ k}\Omega
    $$

---

### Q.7
**(a) 555 internal block diagram. [03 Marks]**
*(Standard diagram with 3 resistors, 2 comparators, SR flip-flop, discharge transistor).*

**(b) Monostable as frequency divider. [04 Marks]**
*(Detailed explanation and timing diagram identical to Class Test 5 Q1, showing how setting the pulse width $W$ such that $T_{in} < W < 2T_{in}$ causes the timer to ignore every alternating trigger pulse, effectively halving the output frequency).*

**(c) Design 555 astable: $f_o = 3.5\text{ kHz}$, Duty cycle $60\%$. [05 Marks]**
**Solution:**
Duty Cycle $D = \frac{R_A + R_B}{R_A + 2R_B} = 0.60$.
$$
R_A + R_B = 0.6 R_A + 1.2 R_B \Rightarrow 0.4 R_A = 0.2 R_B \Rightarrow R_B = 2 R_A
$$
Frequency $f_o = \frac{1.44}{(R_A + 2R_B)C} = 3500\text{ Hz}$.
Substitute $R_B = 2R_A$:
$$
3500 = \frac{1.44}{(R_A + 4R_A)C} = \frac{1.44}{5 R_A C}
$$
$$
5 R_A C = \frac{1.44}{3500} = 4.114 \times 10^{-4}
$$
Choose a practical capacitor value, e.g., $C = 0.01\ \mu\text{F} = 10^{-8}\text{ F}$.
$$
5 R_A (10^{-8}) = 4.114 \times 10^{-4} \Rightarrow R_A = \frac{41140}{5} = 8228\ \Omega \approx 8.2\text{ k}\Omega
$$
$$
R_B = 2 R_A = 2 \times 8228 = 16456\ \Omega \approx 16.5\text{ k}\Omega
$$
**Design Values:** $C = 0.01\ \mu\text{F}$, $R_A = 8.2\text{ k}\Omega$, $R_B = 16.5\text{ k}\Omega$.

---

### Q.8
**(a) Explain how a 555 timer can be an FSK modulator. [04 Marks]**
**Answer:**
Frequency Shift Keying (FSK) involves shifting the output frequency between two distinct values based on a digital input signal (0 or 1).
To configure a 555 timer as an FSK modulator, it is wired in its standard Astable mode. The digital input signal is applied directly to **Pin 5 (Control Voltage)**.
*   When the digital input is HIGH, it alters the internal $2/3 V_{CC}$ threshold of the upper comparator to a new, higher voltage. This forces the capacitor to take longer to charge, resulting in a **lower** output frequency.
*   When the digital input is LOW, the internal threshold drops, the capacitor charges faster, resulting in a **higher** output frequency.
Thus, the digital binary stream modulates the analog output frequency.

**(b) Prove the Barkhausen criteria. [04 Marks]**
*(Proof identical to 2018 Q.8(a), showing that for infinite closed-loop gain $A_f = A / (1 - A\beta)$, the denominator $1 - A\beta$ must equal $0$, hence $A\beta = 1\angle 0^\circ$).*

**(c) Design 3-stage RC phase-shift oscillator for $f_o = 400\text{ Hz}$. [04 Marks]**
**Solution:**
The oscillation frequency is $f_o = \frac{1}{2\pi \sqrt{6} RC}$.
Let $C = 0.1\ \mu\text{F} = 10^{-7}\text{ F}$.
$$
R = \frac{1}{2\pi \sqrt{6} f_o C} = \frac{1}{2\pi \sqrt{6} (400) (10^{-7})} = \frac{1}{0.0006155} = 1624.7\ \Omega \approx 1.62\text{ k}\Omega
$$
To prevent loading the phase-shift network, the input resistor to the inverting amplifier should match $R$.
$$
R_1 = R = 1.62\text{ k}\Omega
$$
For sustained oscillation, the gain must be 29 ($R_F / R_1 \ge 29$).
$$
R_F = 29 \times R_1 = 29 \times 1624.7 = 47116\ \Omega \approx 47\text{ k}\Omega
$$
**Design Values:** $C = 0.1\ \mu\text{F}, R = 1.62\text{ k}\Omega, R_1 = 1.62\text{ k}\Omega, R_F = 47\text{ k}\Omega$.
