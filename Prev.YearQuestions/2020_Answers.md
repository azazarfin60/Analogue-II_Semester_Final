# 📝 RUET 2020 Even Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2205)

---

## SECTION - A

### Q.1
**(a) Calculate $A_v, Z_i$, and $Z_o$ of the cascaded BJT-JFET amplifier circuit. [06 Marks]**

**Solution:**
**Stage 1: NPN BJT (Common-Emitter)**
1.  **DC Analysis:**
    The base is biased by $R_{B1} = 24\text{ k}\Omega$ and $R_{B2} = 8.2\text{ k}\Omega$.
    $$
    V_{th} = V_{CC} \frac{R_{B2}}{R_{B1} + R_{B2}} = 10\text{ V} \times \frac{8.2}{24 + 8.2} = 10 \times \frac{8.2}{32.2} = 2.546\text{ V}
    $$
    $$
    R_{th} = 24\text{ k}\Omega \parallel 8.2\text{ k}\Omega = 6.11\text{ k}\Omega
    $$
    $$
    I_{E1} = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{2.546 - 0.7}{2.2\text{ k}\Omega + 6.11\text{ k}\Omega / 150} = \frac{1.846\text{ V}}{2.24\text{ k}\Omega} = 0.824\text{ mA}
    $$
2.  **AC Parameters:**
    $$
    r_{e1} = \frac{26\text{ mV}}{I_{E1}} = \frac{26\text{ mV}}{0.824\text{ mA}} = 31.55\ \Omega
    $$
    Input impedance of Stage 1:
    $$
    Z_{i1} = R_{B1} \parallel R_{B2} \parallel \beta r_{e1} = 6.11\text{ k}\Omega \parallel 150(31.55\ \Omega) = 6.11\text{ k}\Omega \parallel 4.73\text{ k}\Omega = 2.66\text{ k}\Omega
    $$

**Stage 2: n-channel JFET (Common-Source)**
1.  **DC Analysis:**
    $V_{GS} = -I_D R_S = -330 I_D$.
    $I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2 = 6\text{ mA} \left(1 - \frac{V_{GS}}{-3}\right)^2$.
    Solving this yields $V_{GS} = -0.94\text{ V}$ and $I_D = 2.85\text{ mA}$.
2.  **AC Parameters:**
    $$
    g_m = \frac{2 I_{DSS}}{|V_P|} \left(1 - \frac{V_{GS}}{V_P}\right) = \frac{12\text{ mA}}{3\text{ V}} \left(1 - \frac{-0.94}{-3}\right) = 4\text{ mS} (1 - 0.313) = 2.75\text{ mS}
    $$
    Input impedance of Stage 2:
    $$
    Z_{i2} = R_G = 10\text{ M}\Omega
    $$

**Cascaded Parameters:**
*   **(i) Overall Voltage Gain ($A_v$):**
    Stage 1 Voltage Gain ($A_{v1}$): The load on the BJT collector is $R_{C1} \parallel Z_{i2}$.
    $$
    A_{v1} = -\frac{R_{C1} \parallel Z_{i2}}{r_{e1}} = -\frac{2.7\text{ k}\Omega \parallel 10\text{ M}\Omega}{31.55\ \Omega} \approx -\frac{2700}{31.55} = -85.58
    $$
    Stage 2 Voltage Gain ($A_{v2}$):
    $$
    A_{v2} = -g_m R_D = -2.75\text{ mS} \times 1.8\text{ k}\Omega = -4.95
    $$
    Total Voltage Gain:
    $$
    A_v = A_{v1} \times A_{v2} = (-85.58) \times (-4.95) = 423.6
    $$
*   **(ii) Input Impedance ($Z_i$):**
    $$
    Z_i = Z_{i1} = 2.66\text{ k}\Omega
    $$
*   **(iii) Output Impedance ($Z_o$):**
    $$
    Z_o = R_D = 1.8\text{ k}\Omega
    $$

---

**(b) What is the significance of using Darlington pair circuits? Explain its operation. [03 Marks]**

**Answer:**
**Significance:** The Darlington pair is highly significant in power electronics and audio amplification because it provides an astronomically high current gain (typically $\beta_D \approx \beta_1 \beta_2$, reaching $1000$ to $10,000+$). This allows a microscopic input base current from a sensitive controller to switch or drive a massive load current. Furthermore, it provides extremely high input impedance and low output impedance, making it an ideal buffer.
**Operation:** Two BJTs are connected such that the emitter current of the first transistor ($Q_1$) directly feeds the base of the second transistor ($Q_2$). The input signal is applied to the base of $Q_1$. $Q_1$ amplifies this base current by a factor of $\beta_1$ and passes it to $Q_2$. $Q_2$ then takes this already-amplified current and amplifies it again by a factor of $\beta_2$, dumping the colossal resulting current out of its emitter to the load.

---

**(c) Draw a current mirror circuit using transistors and explain its operation. [03 Marks]**

**Answer:**
*(Schematic: A reference resistor $R$ connects $+V_{CC}$ to the collector of a diode-connected NPN transistor $Q_1$. The base of $Q_1$ is tied to the base of an identical NPN transistor $Q_2$. Both emitters are grounded. The collector of $Q_2$ provides the constant output current $I_{out}$.)*
**Operation:** The current $I_{ref}$ flowing down through $R$ and $Q_1$ establishes a specific $V_{BE}$ across $Q_1$. Because $Q_1$ and $Q_2$ are matched transistors sharing the exact same base-emitter terminals, $Q_2$ is subjected to the exact same $V_{BE}$. Due to the fundamental semiconductor property that $V_{BE}$ defines $I_C$, $Q_2$ will draw a collector current ($I_{out}$) identical to $I_{ref}$, regardless of the load voltage attached to $Q_2$'s collector. It perfectly "mirrors" the reference current.

---

### Q.2
**(a) Draw a differential amplifier using BJTs and explain its operating principles. [04 Marks]**

**Answer:**
*(Schematic: Two perfectly matched NPN BJTs, $Q_1$ and $Q_2$. Their emitters are tied together and connected to a common tail resistor $R_{EE}$ (or a constant current source) going to $-V_{EE}$. Symmetrical collector resistors $R_C$ connect each collector to $+V_{CC}$. Inputs $V_{in1}$ and $V_{in2}$ are at the bases. Output is taken differentially across the two collectors.)*
**Operating Principles:**
A differential amplifier amplifies the *difference* between the two input signals while rejecting any signal common to both.
1.  **Differential Mode:** If $V_{in1}$ increases and $V_{in2}$ decreases by the same amount, $Q_1$ conducts more current and $Q_2$ conducts less. The total current through $R_{EE}$ remains constant, keeping the emitter node voltage fixed. The collector of $Q_1$ drops while the collector of $Q_2$ rises, yielding a large differential output.
2.  **Common Mode:** If $V_{in1}$ and $V_{in2}$ both increase together (e.g., noise), both transistors try to conduct more. This raises the voltage at the common emitter node, which in turn reduces the base-emitter voltage, cancelling out the current increase. Thus, the collector voltages remain unchanged, completely rejecting the common noise.

---

**(b) Define Miller effect capacitance. Derive the expression of input Miller capacitance ($C_{Mi}$). [04 Marks]**

**Answer:**
**Definition:** The Miller effect is an equivalent increase in the effective input capacitance of an inverting amplifier due to amplification of the capacitance bridging the input and output nodes (e.g., $C_{gd}$ or $C_{\mu}$).
**Derivation:**
Consider an inverting amplifier with voltage gain $A_v$ ($A_v$ is negative). A physical feedback capacitor $C_f$ is connected between the input node (voltage $V_i$) and output node (voltage $V_o$).
1.  The current flowing through the capacitor from the input node is:
    $$
    I_i = \frac{V_i - V_o}{X_{Cf}} = \frac{V_i - A_v V_i}{1 / j\omega C_f}
    $$
2.  Factor out $V_i$:
    $$
    I_i = j\omega C_f (1 - A_v) V_i
    $$
3.  The equivalent input impedance caused by this capacitor is:
    $$
    Z_{in} = \frac{V_i}{I_i} = \frac{1}{j\omega C_f (1 - A_v)}
    $$
4.  This is the reactance of an equivalent capacitor $C_{Mi}$ located strictly at the input to ground, where:
    $$
    Z_{in} = \frac{1}{j\omega C_{Mi}}
    $$
5.  Equating the two yields the Input Miller Capacitance:
    $$
    C_{Mi} = C_f (1 - A_v)
    $$

---

**(c) Define CMRR and slew rate. Draw an op-amp based circuit that solves a practical engineering problem. [04 Marks]**

**Answer:**
*   **CMRR (Common-Mode Rejection Ratio):** A measure of an op-amp's ability to reject identical noise/interference present on both input terminals ($CMRR = 20\log(A_d / A_{cm})$).
*   **Slew Rate:** The maximum rate of change of the op-amp's output voltage ($\text{V}/\mu\text{s}$), dictating its high-frequency, large-signal bandwidth limit.
*   **Practical Engineering Circuit (Instrumentation Amplifier):**
    *(Schematic: A classic 3-op-amp instrumentation amplifier. Two non-inverting buffers feeding into a differential amplifier. Used to amplify tiny differential signals from Wheatstone bridge sensors (like strain gauges or load cells) while rejecting massive common-mode industrial noise).*

---

### Q.3
**(a) Compare and explain the frequency response curves of: (i) RC coupled, (ii) Transformer coupled, (iii) Direct coupled amplifiers. [03 Marks]**

**Answer:**
1.  **(i) RC Coupled:** The gain is zero at DC ($0\text{ Hz}$) because the coupling capacitors block it. Gain rises to a flat midband, then drops at high frequencies due to parasitic transistor capacitances. It provides a wide, flat midband.
2.  **(ii) Transformer Coupled:** Similar to RC, it cannot pass DC. The low-frequency response drops due to the primary inductance of the transformer. The high-frequency response drops rapidly due to inter-winding capacitance and leakage inductance. It has the narrowest bandwidth and a "peaky" response curve.
3.  **(iii) Direct Coupled:** The gain is completely flat all the way down to DC ($0\text{ Hz}$) because there are no coupling capacitors. It only rolls off at high frequencies due to internal parasitic capacitances.

---

**(b) Discuss the effect of the number of stages on the lower and upper cutoff frequencies and bandwidth. [04 Marks]**

**Answer:**
When multiple identical amplifier stages are cascaded, the overall bandwidth of the system **shrinks significantly**.
1.  **Lower Cutoff Frequency ($f_L'$):** Each stage's RC coupling networks attenuate low frequencies. Cascading them compounds this attenuation. The overall lower cutoff frequency shifts **upward** (higher):
    $$
    f_L' = \frac{f_L}{\sqrt{2^{1/n} - 1}}
    $$
2.  **Upper Cutoff Frequency ($f_H'$):** Each stage's parasitic capacitances attenuate high frequencies. Cascading them compounds the attenuation. The overall upper cutoff frequency shifts **downward** (lower):
    $$
    f_H' = f_H \sqrt{2^{1/n} - 1}
    $$
3.  **Bandwidth ($BW'$):** Because the low cutoff moves up and the high cutoff moves down, the overall bandwidth ($BW' \approx f_H' - f_L'$) becomes significantly narrower than a single stage.

---

**(c) Determine $f_{LS}, f_{LC}, f_{LE}$ and overall lower-cutoff frequency for the BJT CE amplifier. [05 Marks]**

**Solution:**
**1. DC Dynamic Resistance:**
$R_{th} = 30\text{ k}\Omega \parallel 20\text{ k}\Omega = 12\text{ k}\Omega$.
$V_{th} = 10\text{ V} \times \frac{20}{50} = 4\text{ V}$.
$I_E = \frac{4 - 0.7}{3.7\text{ k}\Omega + 12\text{ k}\Omega / 80} = \frac{3.3\text{ V}}{3.7\text{k} + 0.15\text{k}} = \frac{3.3}{3.85} = 0.857\text{ mA}$.
$r_e = \frac{26\text{ mV}}{0.857\text{ mA}} = 30.3\ \Omega$.
Input Resistance: $R_{in} = R_{th} \parallel \beta r_e = 12\text{ k}\Omega \parallel 80(30.3\ \Omega) = 12\text{ k}\Omega \parallel 2.42\text{ k}\Omega = 2.01\text{ k}\Omega$.

**2. Low Cutoff Frequencies:**
*   **Input Coupling ($f_{LS}$):**
    $$
    f_{LS} = \frac{1}{2\pi (R_{sig} + R_{in}) C_s} = \frac{1}{2\pi (1\text{ k}\Omega + 2.01\text{ k}\Omega) 1\ \mu\text{F}} = \frac{1}{2\pi \times 3010 \times 10^{-6}} = 52.8\text{ Hz}
    $$
*   **Output Coupling ($f_{LC}$):**
    $$
    f_{LC} = \frac{1}{2\pi (R_C + R_L) C_c} = \frac{1}{2\pi (4.9\text{ k}\Omega + 5\text{ k}\Omega) 1\ \mu\text{F}} = \frac{1}{2\pi \times 9900 \times 10^{-6}} = 16.08\text{ Hz}
    $$
*   **Emitter Bypass ($f_{LE}$):**
    Equivalent resistance seen by $C_E$:
    $$
    R_e = R_E \parallel \left( r_e + \frac{R_{sig} \parallel R_{th}}{\beta} \right) = 3700 \parallel \left( 30.3 + \frac{1000 \parallel 12000}{80} \right) = 3700 \parallel \left( 30.3 + \frac{923}{80} \right) = 3700 \parallel 41.8 = 41.3\ \Omega
    $$
    $$
    f_{LE} = \frac{1}{2\pi R_e C_E} = \frac{1}{2\pi (41.3) (5\ \mu\text{F})} = 770.8\text{ Hz}
    $$

**Overall Lower-Cutoff Frequency:**
The overall low cutoff frequency is dominated by the highest of the individual cutoff frequencies.
$$
f_L \approx f_{LE} = 770.8\text{ Hz}
$$

---

### Q.4
**(a) What are the basic differences between active and passive filters? Merits and drawbacks? [03 Marks]**

**Answer:**
*   **Differences:** Passive filters are built exclusively using resistors, capacitors, and inductors; they cannot amplify the signal (gain $< 1$). Active filters incorporate active devices (Op-Amps) alongside resistors and capacitors (eliminating inductors); they can provide voltage gain.
*   **Merits of Active Filters:** Can provide voltage amplification. No signal loading issues (due to high input / low output impedance of op-amps). Avoids the use of bulky, heavy, and expensive inductors. Easy to tune.
*   **Drawbacks:** Requires an external DC power supply. Highly limited by the high-frequency Gain-Bandwidth Product (GBWP) of the op-amp, making them unsuitable for very high-frequency (RF) applications.

---

**(b) Prove that an integrator using an op-amp can act as a first-order active low-pass filter. [04 Marks]**

**Proof:**
An op-amp integrator consists of an input resistor $R$ and a feedback capacitor $C$.
The transfer function in the Laplace domain is:
$$
H(s) = \frac{V_o(s)}{V_i(s)} = -\frac{1}{sRC}
$$
Substituting $s = j\omega = j 2\pi f$:
$$
|H(f)| = \frac{1}{2\pi f RC}
$$
1.  **At very low frequencies ($f \rightarrow 0$):** The capacitor acts as an open circuit. The gain approaches the massive open-loop gain of the op-amp (in practice, a large feedback resistor $R_f$ is added to cap this DC gain and prevent saturation). It easily passes low-frequency signals.
2.  **At very high frequencies ($f \rightarrow \infty$):** The capacitor acts as a short circuit. The gain approaches zero. It completely blocks high-frequency signals.
Because the gain decreases at a constant rate of $-20\text{ dB/decade}$ as frequency increases, it perfectly matches the Bode plot characteristics of a first-order Low-Pass Filter.

---

**(c) Design a second-order active Sallen-Key low-pass filter: $f_H = 1.5\text{ kHz}, K = 5, Q = 0.707$. [05 Marks]**

**Design Strategy:**
A standard equal-component Sallen-Key LPF ($R_1 = R_2 = R, C_1 = C_2 = C$) mathematically forces the quality factor to be $Q = \frac{1}{3 - K}$. If we need $K=5$, the $Q$ becomes negative, making the filter an unstable oscillator.
To achieve both a specific $K=5$ and $Q=0.707$ (Butterworth) without mathematically violating the topology, the most robust engineering approach is to design an equal-component Sallen-Key filter optimized strictly for $Q=0.707$, and cascade it with an independent non-inverting amplifier stage to make up the remaining gain.

**Stage 1: Sallen-Key Filter ($Q = 0.707$)**
1.  For $Q = 0.707$, the required internal gain is $K_1 = 3 - \frac{1}{0.707} = 3 - 1.414 = 1.586$.
2.  Choose $C = 10\text{ nF}$.
3.  Calculate $R$ for $f_H = 1.5\text{ kHz}$:
    $$
    R = \frac{1}{2\pi f_H C} = \frac{1}{2\pi (1500)(10^{-8})} = 10.61\text{ k}\Omega
    $$
4.  Set internal feedback resistors ($R_A, R_B$) for $K_1 = 1.586$:
    $$
    K_1 = 1 + \frac{R_F}{R_1} = 1.586 \Rightarrow \frac{R_F}{R_1} = 0.586
    $$
    Let $R_1 = 10\text{ k}\Omega$, then $R_F = 5.86\text{ k}\Omega$.

**Stage 2: Gain Amplifier Stage**
We need a total system gain of $K_{total} = 5$.
The required gain for Stage 2 is $K_2 = \frac{5}{1.586} = 3.15$.
Using a non-inverting amplifier:
$$
K_2 = 1 + \frac{R_{F2}}{R_{12}} = 3.15 \Rightarrow \frac{R_{F2}}{R_{12}} = 2.15
$$
Let $R_{12} = 10\text{ k}\Omega$, then $R_{F2} = 21.5\text{ k}\Omega$.
*(Note: Cascading these two stages perfectly yields the requested $f_H = 1.5\text{ kHz}$, $Q = 0.707$, and total passband gain $K = 5$).*

---

## SECTION - B

### Q.5
**(a) Define regenerative and degenerative feedback. [02 Marks]**
*   **Regenerative (Positive) Feedback:** A portion of the output signal is returned to the input *in-phase* with the input signal, adding to it. Used primarily to create oscillators and Schmitt triggers.
*   **Degenerative (Negative) Feedback:** A portion of the output signal is returned to the input *out-of-phase* ($180^\circ$ shifted) with the input signal, subtracting from it. Used primarily to stabilize amplifier gain and increase bandwidth.

**(b) Draw an op-amp RC phase-shift oscillator and explain. [04 Marks]**
*(Answer identical to 2018 Q.8(b). The inverting op-amp provides $180^\circ$ phase shift. Three cascaded RC high-pass sections provide the remaining $180^\circ$ phase shift ($60^\circ$ each at resonant frequency) to satisfy Barkhausen criteria $360^\circ$ / $0^\circ$).*

**(c) Design a Wien bridge oscillator for $f_o = 15\text{ kHz}$. [04 Marks]**
**Solution:**
$$
f_o = \frac{1}{2\pi R C} = 15,000\text{ Hz}
$$
Let $C = 1\text{ nF} = 10^{-9}\text{ F}$.
$$
R = \frac{1}{2\pi (15000) (10^{-9})} = 10.61\text{ k}\Omega
$$
For sustained oscillation, $A_v \ge 3$. $1 + R_f / R_1 \ge 3 \Rightarrow R_f \ge 2 R_1$.
Let $R_1 = 10\text{ k}\Omega$, then $R_f = 20\text{ k}\Omega$ (use a $22\text{k}\Omega$ potentiometer).

**(d) Write a short note on crystal oscillators. [02 Marks]**
**Answer:** Crystal oscillators utilize the piezoelectric effect of quartz crystals. When an AC voltage is applied, the crystal mechanically vibrates at its highly stable natural resonant frequency. They possess an extraordinarily high Q-factor (often $>10,000$, compared to $\sim 10$ for LC tanks). This ensures that the oscillation frequency is practically immune to temperature changes, voltage fluctuations, and aging, making them the standard for highly precise clocks and radio transmitters.

---

### Q.6
**(a) Show that monostable output pulse width is $W \approx 1.1 R C$. [04 Marks]**
**Proof:**
In a 555 monostable, the timing capacitor charges through $R$ from $0\text{V}$ toward $V_{CC}$.
The voltage across a charging capacitor is:
$$
v_c(t) = V_{CC} (1 - e^{-t / RC})
$$
The pulse ends (output goes LOW) when the capacitor voltage reaches the upper comparator threshold, which is exactly $\frac{2}{3} V_{CC}$. Let the time this takes be $W$.
$$
\frac{2}{3} V_{CC} = V_{CC} (1 - e^{-W / RC})
$$
$$
\frac{2}{3} = 1 - e^{-W / RC}
$$
$$
e^{-W / RC} = 1 - \frac{2}{3} = \frac{1}{3}
$$
Take the natural logarithm of both sides:
$$
-\frac{W}{RC} = \ln\left(\frac{1}{3}\right) = -1.0986
$$
$$
W = 1.0986 RC \approx 1.1 RC
$$

**(b) Design a square wave generator (astable) using a 555 timer. $V_{CC} = 12\text{ V}, f_o = 3.5\text{ kHz}$. [04 Marks]**
**Solution:**
Assuming a standard 555 configuration where $D \approx 50\%$ requires $R_A \ll R_B$.
$$
f_o = \frac{1.44}{(R_A + 2R_B)C} = 3500\text{ Hz}
$$
Let $R_A = 1\text{ k}\Omega$ and $R_B = 10\text{ k}\Omega$ (this gives a duty cycle of $11/21 \approx 52\%$, which is very close to a square wave).
$$
3500 = \frac{1.44}{(1000 + 20000)C} = \frac{1.44}{21000 C}
$$
$$
C = \frac{1.44}{3500 \times 21000} = 1.959 \times 10^{-8}\text{ F} \approx 20\text{ nF}
$$
**Design Values:** $C = 20\text{ nF}$, $R_A = 1\text{ k}\Omega$, $R_B = 10\text{ k}\Omega$.

**(c) Missing pulse detector circuit. [04 Marks]**
*(Schematic: A 555 timer in monostable mode. A PNP transistor is connected completely across the timing capacitor $C$. The base of the PNP and Pin 2 (Trigger) are both driven by the continuous input pulse train).*
**Operation:** The monostable pulse width $W$ is deliberately set to be slightly longer than the time period $T$ of the incoming pulse train. Under normal conditions, every incoming negative pulse triggers the timer AND turns on the PNP transistor, discharging the capacitor to $0\text{V}$. Because the pulses arrive faster than the capacitor can reach $2/3 V_{CC}$, the output stays constantly HIGH. If a pulse goes missing, the capacitor is not discharged. It continues charging, hits $2/3 V_{CC}$, and forces the timer output LOW, triggering an alarm that a pulse was missed.

---

### Q.7
**(a) Effect of input noise on comparator? Solution? [04 Marks]**
*(Answer identical to 2019 Q.4(c). Noise causes false triggering/chattering. Solved by implementing a Schmitt Trigger to introduce hysteresis).*

**(b) Derive $V_o$ for the logarithmic amplifier. [04 Marks]**
**Derivation:**
1.  By virtual ground, the inverting terminal is at $0\text{V}$. Therefore, the input current through $R$ is exactly:
    $$
    I_{in} = \frac{V_i}{R}
    $$
2.  Because the op-amp inputs draw no current, all of $I_{in}$ must flow into the collector of the feedback transistor.
    $$
    I_C = I_{in} = \frac{V_i}{R}
    $$
3.  The collector current of a BJT is exponentially related to its base-emitter voltage:
    $$
    I_C = I_s e^{V_{BE} / V_T}
    $$
    where $I_s$ is reverse saturation current and $V_T \approx 26\text{mV}$.
4.  The base of the NPN is grounded ($V_B = 0$). The emitter is tied to the output ($V_E = V_o$). Therefore, $V_{BE} = V_B - V_E = -V_o$.
5.  Substitute $V_{BE}$:
    $$
    I_C = I_s e^{-V_o / V_T}
    $$
6.  Equate the currents:
    $$
    \frac{V_i}{R} = I_s e^{-V_o / V_T} \Rightarrow \frac{V_i}{I_s R} = e^{-V_o / V_T}
    $$
7.  Take the natural logarithm of both sides:
    $$
    \ln\left(\frac{V_i}{I_s R}\right) = -\frac{V_o}{V_T}
    $$
    $$
    V_o = -V_T \ln\left( \frac{V_i}{I_s R} \right)
    $$
The output is proportional to the natural logarithm of the input voltage.

**(c) Precision full-wave rectifier. [04 Marks]**
*(Schematic: A cascading of a precision half-wave rectifier and an inverting summing amplifier. The input is fed directly to the summing amplifier through resistor $R$, and also fed to the half-wave rectifier. The output of the half-wave rectifier (which produces $-V_{in}$ for positive cycles) is fed to the summing amplifier through a resistor $R/2$).*
**Operation:** For positive half-cycles, the half-wave stage outputs $-V_{in}$. The summer adds $-2(-V_{in})$ and $-1(V_{in})$ yielding $+V_{in}$. For negative half-cycles, the half-wave stage outputs $0$. The summer adds $-1(-V_{in})$ yielding $+V_{in}$. The result is absolute value (full-wave rectification) without diode drops.

---

### Q.8
**(a) What are monostable and astable multivibrators? [04 Marks]**
*   **Monostable (One-Shot):** Has exactly *one* stable state. It rests in this state until forced into an unstable state by an external trigger. It stays in the unstable state for a specific time (determined by an RC constant) and then automatically returns to the stable state. (Schematic: standard 555 timer with one RC network).
*   **Astable (Free-Running):** Has *zero* stable states. It continuously oscillates back and forth between two unstable states without requiring any external trigger, producing a continuous square wave. (Schematic: standard 555 timer with $R_A, R_B, C$).

**(b) Design a circuit for $V_o = 3 V_1 - 2 V_2 - 3 \frac{d V_1}{d t}$. [04 Marks]**
**Design Strategy:**
Rearrange the equation to match the format of an inverting summer ($V_o = -(V_A + V_B + V_C)$):
$$
V_o = - \left( -3 V_1 + 2 V_2 + 3 \frac{d V_1}{d t} \right)
$$
We will process the inputs separately and feed them into a final inverting summing amplifier where all summer input resistors ($R$) equal the feedback resistor ($R_f = 10\text{ k}\Omega$, gain of $-1$).
*   **Channel A (Requires $-3 V_1$):** Pass $V_1$ through an inverting amplifier with a gain of $-3$. ($R_{fA} = 30\text{ k}\Omega, R_{iA} = 10\text{ k}\Omega$).
*   **Channel B (Requires $+2 V_2$):** Pass $V_2$ through a non-inverting amplifier with a gain of $+2$. ($R_{fB} = 10\text{ k}\Omega, R_{iB} = 10\text{ k}\Omega$).
*   **Channel C (Requires $+3 \frac{d V_1}{d t}$):** Pass $V_1$ through an inverting differentiator ($v = -RC \frac{dV_1}{dt}$). Let $RC = 3$ (e.g., $R_d = 300\text{ k}\Omega, C_d = 10\ \mu\text{F}$). This outputs $-3 \frac{d V_1}{d t}$. To get $+3 \frac{d V_1}{d t}$, pass this output through a unity-gain inverting amplifier ($R_{in} = 10\text{k}, R_f = 10\text{k}$).
Summing Channel A, B, and C into the final inverter yields exactly the required mathematical equation.

**(c) Design the inverting Schmitt trigger: $V_{UT} = 7\text{ V}, V_{LT} = 3\text{ V}, V_{sat} = 14\text{ V}$. [04 Marks]**
**Solution:**
The trigger threshold equations for the provided topology are:
1.

    $$
    V_{UT} = V_{ref} \frac{R_F}{R_1 + R_F} + V_{sat} \frac{R_1}{R_1 + R_F} = 7
    $$
2.

    $$
    V_{LT} = V_{ref} \frac{R_F}{R_1 + R_F} - V_{sat} \frac{R_1}{R_1 + R_F} = 3
    $$

Subtracting (2) from (1):
$$
2 V_{sat} \frac{R_1}{R_1 + R_F} = 4 \Rightarrow 2(14) \frac{R_1}{R_1 + R_F} = 4 \Rightarrow \frac{R_1}{R_1 + R_F} = \frac{4}{28} = \frac{1}{7}
$$
$$
7 R_1 = R_1 + R_F \Rightarrow R_F = 6 R_1
$$
Let $R_1 = 10\text{ k}\Omega$, then $R_F = 60\text{ k}\Omega$.

Adding (1) and (2):
$$
2 V_{ref} \frac{R_F}{R_1 + R_F} = 10 \Rightarrow V_{ref} \frac{R_F}{R_1 + R_F} = 5
$$
Substitute $R_F = 6 R_1$:
$$
V_{ref} \frac{6 R_1}{7 R_1} = 5 \Rightarrow V_{ref} \frac{6}{7} = 5
$$
$$
V_{ref} = \frac{35}{6} = 5.833\text{ V}
$$

**Design Values:**
$R_1 = 10\text{ k}\Omega$
$R_F = 60\text{ k}\Omega$
$V_{ref} = 5.833\text{ V}$
