# 📝 Class Test Answers
# Analog Electronic Circuits-II (ECE 2105)

---

## 📌 Class Test 1

### Q1. For the R-C coupled amplifier shown in Figure 1:
**(a) Determine the DC voltages $V_B, V_C$, and $V_E$ for each transistor ($Q_1$ and $Q_2$).**
**(b) Calculate the DC currents $I_B, I_C$, and $I_E$ for each transistor.**

**Solution:**
We perform DC analysis by treating all coupling and bypass capacitors ($C_c, C_E$) as open circuits. The two stages are DC isolated from each other by $C_{c1}$.

**For Transistor $Q_1$ (Stage 1):**
Using the approximate voltage-divider bias method (assuming $\beta_1 R_{E1} \gg 10 R_{12}$):
*   **Base Voltage ($V_{B1}$):**
    $$
    V_{B1} = \frac{R_{12}}{R_{11} + R_{12}} V_{CC} = \frac{4.7\text{ k}\Omega}{18\text{ k}\Omega + 4.7\text{ k}\Omega} \times 20\text{ V} = \frac{4.7}{22.7} \times 20 = 4.14\text{ V}
    $$
*   **Emitter Voltage ($V_{E1}$):**
    $$
    V_{E1} = V_{B1} - V_{BE} = 4.14\text{ V} - 0.7\text{ V} = 3.44\text{ V}
    $$
*   **Emitter Current ($I_{E1}$):**
    $$
    I_{E1} = \frac{V_{E1}}{R_{E1}} = \frac{3.44\text{ V}}{1\text{ k}\Omega} = 3.44\text{ mA}
    $$
*   **Collector Current ($I_{C1}$):**
    $$
    I_{C1} \approx I_{E1} = 3.44\text{ mA}
    $$
*   **Base Current ($I_{B1}$):**
    $$
    I_{B1} = \frac{I_{E1}}{\beta_1 + 1} = \frac{3.44\text{ mA}}{161} = 0.0213\text{ mA} = 21.3\ \mu\text{A}
    $$
*   **Collector Voltage ($V_{C1}$):**
    $$
    V_{C1} = V_{CC} - I_{C1}R_{C1} = 20\text{ V} - (3.44\text{ mA} \times 2.2\text{ k}\Omega) = 20\text{ V} - 7.57\text{ V} = 12.43\text{ V}
    $$

**For Transistor $Q_2$ (Stage 2):**
Similarly, for the second stage:
*   **Base Voltage ($V_{B2}$):**
    $$
    V_{B2} = \frac{R_{22}}{R_{21} + R_{22}} V_{CC} = \frac{3.3\text{ k}\Omega}{22\text{ k}\Omega + 3.3\text{ k}\Omega} \times 20\text{ V} = \frac{3.3}{25.3} \times 20 = 2.61\text{ V}
    $$
*   **Emitter Voltage ($V_{E2}$):**
    $$
    V_{E2} = V_{B2} - V_{BE} = 2.61\text{ V} - 0.7\text{ V} = 1.91\text{ V}
    $$
*   **Emitter Current ($I_{E2}$):**
    $$
    I_{E2} = \frac{V_{E2}}{R_{E2}} = \frac{1.91\text{ V}}{1.2\text{ k}\Omega} = 1.59\text{ mA}
    $$
*   **Collector Current ($I_{C2}$):**
    $$
    I_{C2} \approx I_{E2} = 1.59\text{ mA}
    $$
*   **Base Current ($I_{B2}$):**
    $$
    I_{B2} = \frac{I_{E2}}{\beta_2 + 1} = \frac{1.59\text{ mA}}{91} = 0.0175\text{ mA} = 17.5\ \mu\text{A}
    $$
*   **Collector Voltage ($V_{C2}$):**
    $$
    V_{C2} = V_{CC} - I_{C2}R_{C2} = 20\text{ V} - (1.59\text{ mA} \times 2.2\text{ k}\Omega) = 20\text{ V} - 3.50\text{ V} = 16.50\text{ V}
    $$

---

### Q2. Prove that although a feedback pair configuration operates with approximately unity voltage gain, it provides a very high current gain.

**Proof:**
A feedback pair consists of a PNP transistor driving an NPN transistor, acting analogously to a Darlington pair but with complementary transistors. The collector of the PNP ($Q_1$) connects directly to the base of the NPN ($Q_2$), and the emitter of the PNP is tied to the collector of the NPN.

**1. Current Gain Analysis:**
Let the input current to the pair be $I_{B1}$ (base current of $Q_1$).
*   The collector current of $Q_1$ is $I_{C1} = \beta_1 I_{B1}$.
*   This entire collector current drives the base of $Q_2$, so $I_{B2} = I_{C1} = \beta_1 I_{B1}$.
*   The collector current of $Q_2$ is $I_{C2} = \beta_2 I_{B2} = \beta_1 \beta_2 I_{B1}$.
*   The total effective collector current of the composite pair is $I_{C(total)} \approx I_{C2} = \beta_1 \beta_2 I_{B1}$.
Thus, the composite current gain is $\beta_D = \frac{I_{C(total)}}{I_{B1}} \approx \beta_1 \beta_2$. Since both $\beta_1$ and $\beta_2$ are large, the overall current gain is very high.

**2. Voltage Gain Analysis:**
When used as an emitter-follower (or collector-follower in this complementary topology), the output is taken from the emitter of $Q_1$ (which is tied to the collector of $Q_2$ through a load resistor).
The voltage gain equation for an emitter-follower is:
$$
A_v = \frac{R_E}{r_e + R_E}
$$
Because the dynamic resistance $r_e$ of the composite device is extremely small (due to the massive current $I_{C2}$), $r_e \ll R_E$.
Therefore:
$$
A_v \approx \frac{R_E}{R_E} = 1
$$
Thus, the feedback pair provides unity voltage gain while supplying an extraordinarily high current gain.

---

## 📌 Class Test 2

### Q1. For the BJT amplifier shown in Figure 1:
**(a) Determine the low-cutoff frequencies ($f_{Ls}, f_{Lc}, f_{LE}$) for the network.**
**(b) Sketch the resulting frequency response using a Bode plot.**

**Solution:**
First, we must determine the dynamic emitter resistance, $r_e$.
*   $R_{th} = R_1 \parallel R_2 = 40\text{ k}\Omega \parallel 10\text{ k}\Omega = 8\text{ k}\Omega$
*   $V_{th} = \frac{10}{50} \times 20\text{ V} = 4\text{ V}$
*   $I_E = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{4\text{ V} - 0.7\text{ V}}{2\text{ k}\Omega + 8\text{ k}\Omega/100} = \frac{3.3\text{ V}}{2.08\text{ k}\Omega} = 1.586\text{ mA}$
*   $r_e = \frac{26\text{ mV}}{1.586\text{ mA}} = 16.39\ \Omega$

**1. Input Low-Cutoff Frequency ($f_{Ls}$):**
Input impedance of the amplifier stage with the emitter fully bypassed is $R_i = R_{th} \parallel \beta r_e$.
*   $\beta r_e = 100 \times 16.39\ \Omega = 1.639\text{ k}\Omega$
*   $R_i = 8\text{ k}\Omega \parallel 1.639\text{ k}\Omega = 1.36\text{ k}\Omega$
Assuming source resistance $R_{sig} = 0$:
$$
f_{Ls} = \frac{1}{2\pi (R_{sig} + R_i) C_s} = \frac{1}{2\pi \times 1.36\text{ k}\Omega \times 10\ \mu\text{F}} = 11.7\text{ Hz}
$$

**2. Output Low-Cutoff Frequency ($f_{Lc}$):**
Assuming transistor output resistance $r_o \approx \infty$, output resistance $R_o = R_C = 4\text{ k}\Omega$.
$$
f_{Lc} = \frac{1}{2\pi (R_o + R_L) C_c} = \frac{1}{2\pi (4\text{ k}\Omega + 2.2\text{ k}\Omega) 1\ \mu\text{F}} = \frac{1}{2\pi \times 6.2\text{ k}\Omega \times 1\ \mu\text{F}} = 25.68\text{ Hz}
$$

**3. Emitter Low-Cutoff Frequency ($f_{LE}$):**
Equivalent resistance seen by the emitter bypass capacitor $C_E$ is $R_e = R_E \parallel \left( r_e + \frac{R_{sig} \parallel R_{th}}{\beta} \right)$.
Since $R_{sig} = 0$, $R_e = R_E \parallel r_e = 2000\ \Omega \parallel 16.39\ \Omega \approx 16.26\ \Omega$.
$$
f_{LE} = \frac{1}{2\pi R_e C_E} = \frac{1}{2\pi \times 16.26\ \Omega \times 20\ \mu\text{F}} = 489.5\text{ Hz}
$$

**Overall Dominant Lower Cut-off:**
The highest of these three frequencies dictates the overall low-frequency response limit. Therefore, $f_L \approx f_{LE} = 489.5\text{ Hz}$.

*(For part b, a standard Bode plot would show a +20 dB/decade rising slope hitting a $-3\text{ dB}$ corner at roughly $489.5\text{ Hz}$, then plateauing at the midband gain).*

---

### Q2. For the FET amplifier shown in Figure 2:
**(a) Determine the low-cutoff frequencies ($f_{LG}, f_{LC}, f_{LS}$) for the network.**
**(b) Determine the high-cutoff frequencies ($f_{Hi}, f_{Ho}$) for the network.**

**Solution:**
First, we find the midband parameters. Given $V_{GS} = -I_D R_S$, and solving the Shockley equation, assume we find the operating point. However, the transconductance is provided directly by the self-bias operating point equation: $g_{m0} = \frac{2 I_{DSS}}{|V_P|} = \frac{2 \times 8\text{ mA}}{4\text{ V}} = 4\text{ mS}$. Let's assume operation near $I_{DSS}/4$, so $g_m \approx 2\text{ mS}$ (or we can use the maximum $g_{m0}=4\text{ mS}$ for worst-case). Using $g_m = 2\text{ mS}$ for typical analysis:

**Part A: Low-Cutoff Frequencies**
*   **Gate ($f_{LG}$):**
    $$
    f_{LG} = \frac{1}{2\pi (R_{sig} + R_G) C_G} = \frac{1}{2\pi (10\text{ k}\Omega + 1\text{ M}\Omega) 0.01\ \mu\text{F}} \approx 15.76\text{ Hz}
    $$
*   **Drain/Coupling ($f_{LC}$):**
    $$
    f_{LC} = \frac{1}{2\pi (R_D + R_L) C_C} = \frac{1}{2\pi (4.7\text{ k}\Omega + 2.2\text{ k}\Omega) 0.5\ \mu\text{F}} = 46.13\text{ Hz}
    $$
*   **Source/Bypass ($f_{LS}$):**
    $$
    R_{eq} = R_S \parallel \frac{1}{g_m} = 1\text{ k}\Omega \parallel \frac{1}{2\text{ mS}} = 1000 \parallel 500 = 333.3\ \Omega
    $$
    $$
    f_{LS} = \frac{1}{2\pi R_{eq} C_S} = \frac{1}{2\pi \times 333.3\ \Omega \times 2\ \mu\text{F}} = 238.7\text{ Hz}
    $$

**Part B: High-Cutoff Frequencies**
First, determine the midband voltage gain:
$$
A_v = -g_m (R_D \parallel R_L) = -2\text{ mS} \times (4.7\text{ k}\Omega \parallel 2.2\text{ k}\Omega) = -2\text{ mS} \times 1.5\text{ k}\Omega = -3
$$
*   **Input Miller Capacitance:** $C_{Mi} = C_{gd} (1 - A_v) = 2\text{ pF} \times (1 - (-3)) = 8\text{ pF}$
*   **Output Miller Capacitance:** $C_{Mo} = C_{gd} (1 - 1/A_v) = 2\text{ pF} \times (1 - (-1/3)) = 2.67\text{ pF}$

*   **Total Input High-Frequency Capacitance ($C_i$):**
    $$
    C_i = C_{Wi} + C_{gs} + C_{Mi} = 5\text{ pF} + 4\text{ pF} + 8\text{ pF} = 17\text{ pF}
    $$
*   **Input High Cutoff ($f_{Hi}$):**
    $$
    R_{Thi} = R_{sig} \parallel R_G = 10\text{ k}\Omega \parallel 1\text{ M}\Omega \approx 9.9\text{ k}\Omega
    $$
    $$
    f_{Hi} = \frac{1}{2\pi R_{Thi} C_i} = \frac{1}{2\pi \times 9.9\text{ k}\Omega \times 17\text{ pF}} = 945.7\text{ kHz}
    $$

*   **Total Output High-Frequency Capacitance ($C_o$):**
    $$
    C_o = C_{Wo} + C_{ds} + C_{Mo} = 6\text{ pF} + 0.5\text{ pF} + 2.67\text{ pF} = 9.17\text{ pF}
    $$
*   **Output High Cutoff ($f_{Ho}$):**
    $$
    R_{Tho} = R_D \parallel R_L = 1.5\text{ k}\Omega
    $$
    $$
    f_{Ho} = \frac{1}{2\pi R_{Tho} C_o} = \frac{1}{2\pi \times 1.5\text{ k}\Omega \times 9.17\text{ pF}} = 11.57\text{ MHz}
    $$

---

## 📌 Class Test 3

### Q1. Two operational amplifiers have common-mode rejection ratios (CMRR) of 90 dB and 120 dB. Analyze which op-amp provides better common-mode noise suppression.

**Solution:**
The **120 dB** op-amp provides significantly better common-mode noise suppression.

**Justification:**
CMRR (Common-Mode Rejection Ratio) is a measure of an operational amplifier's ability to reject signals that are present simultaneously and in-phase at both input terminals (such as electromagnetic interference or 50/60 Hz mains hum). Mathematically, it is defined as:
$$
\text{CMRR} = 20 \log_{10} \left( \frac{A_d}{A_{cm}} \right)
$$
where $A_d$ is the differential gain and $A_{cm}$ is the common-mode gain.

A higher CMRR (120 dB compared to 90 dB) implies that the ratio of differential gain to common-mode gain is 1,000 times larger ($120\text{ dB} - 90\text{ dB} = 30\text{ dB}$, and $10^{30/20} = 31.6$ linear difference in ratio). Practically, this means the 120 dB op-amp will amplify the desired differential signal while shrinking background noise and voltage offsets much more aggressively than the 90 dB op-amp, leading to a much cleaner output signal.

---

### Q2. Op-amp integrator with $R_1 C_f = 1$ and valid range $10\text{ Hz} - 1\text{ kHz}$. Input is $5\sin(2\pi f_s t)$.
**Case I: $f_s = 1\text{ kHz}$.**
**Case II: $f_s = 5\text{ Hz}$.**

**Solution:**
The output voltage for an ideal inverting integrator is given by:
$$
V_o(t) = -\frac{1}{R_1 C_f} \int V_i(t) dt
$$
Given $R_1 C_f = 1$, the expression simplifies to $V_o(t) = -\int V_i(t) dt$.

**Case I: $f_s = 1\text{ kHz}$**
Since $1\text{ kHz}$ is within the proper operating range:
$$
V_i(t) = 5\sin(2000\pi t)
$$
$$
V_o(t) = -\int 5\sin(2000\pi t) dt = -5 \left( \frac{-1}{2000\pi} \cos(2000\pi t) \right) = \frac{5}{2000\pi} \cos(2000\pi t)
$$
$$
V_o(t) = 0.00079 \cos(2000\pi t)\text{ V} \approx 0.79\text{ mV} \cos(2000\pi t)
$$
*Analysis:* The output is a cosine wave (shifted by $90^\circ$ relative to the input sine wave) with a heavily attenuated amplitude of $0.79\text{ mV}$. It operates perfectly linearly.

**Case II: $f_s = 5\text{ Hz}$**
*Analysis:* The $5\text{ Hz}$ frequency falls *below* the minimum operating frequency of $10\text{ Hz}$. At very low frequencies, the capacitive reactance of the feedback capacitor ($X_C = \frac{1}{2\pi f C}$) becomes extremely large. The op-amp effectively behaves as an open-loop amplifier with near-infinite gain. Consequently, the output will immediately clip and saturate to the power supply rails ($\pm V_{sat}$). The waveform will lose its sinusoidal shape and appear as a square wave distorted by rail saturation.

---

### Q3. Op-amp differentiator with $R_f C_1 = 1$. Range $10\text{ Hz} - 1\text{ kHz}$.
**Case I: $V_i(t) = 5\sin(2\pi f t)$ at $1\text{ kHz}$.**
**Case II: $V_i(t) = 10\cos(2\pi f t)$ at $1\text{ kHz}$.**

**Solution:**
The output voltage for an ideal differentiator is given by:
$$
V_o(t) = -R_f C_1 \frac{d V_i(t)}{dt}
$$
Given $R_f C_1 = 1$, the expression simplifies to $V_o(t) = -\frac{d V_i(t)}{dt}$. The frequency is $1\text{ kHz}$, so $\omega = 2000\pi$.

**Case I:** $V_i(t) = 5\sin(2000\pi t)$
$$
V_o(t) = -\frac{d}{dt} [5\sin(2000\pi t)] = -5 \times 2000\pi \cos(2000\pi t) = -10000\pi \cos(2000\pi t) \approx -31415\cos(2000\pi t)\text{ V}
$$
*Analysis:* The mathematical derivative produces a theoretical amplitude of $31,415\text{ V}$. Since this vastly exceeds any practical op-amp power supply (usually $\pm 15\text{ V}$), the output will be completely saturated into a square wave at the rail limits ($\pm V_{sat}$).

**Case II:** $V_i(t) = 10\cos(2000\pi t)$
$$
V_o(t) = -\frac{d}{dt} [10\cos(2000\pi t)] = -10 \times 2000\pi (-\sin(2000\pi t)) = 20000\pi \sin(2000\pi t) \approx 62831\sin(2000\pi t)\text{ V}
$$
*Analysis:* Similar to Case I, the enormous scaling factor introduced by differentiating a high-frequency signal pushes the theoretical amplitude to $62,831\text{ V}$. The op-amp will heavily saturate to its maximum supply rails ($\pm V_{sat}$), outputting a clipped square wave.

---

## 📌 Class Test 4

### Q1. RC Phase-Shift Oscillator
**(a) Type of oscillator and mechanism of oscillation via Barkhausen.**
**(b) Effect of removing one RC section.**

**Solution:**
**(a)** The circuit is an **RC Phase-Shift Oscillator**.
*Mechanism:* According to the **Barkhausen Criterion**, for a circuit to sustain continuous oscillations, two conditions must be met:
1.  The magnitude of the loop gain must be equal to unity: $|A\beta| = 1$.
2.  The total phase shift around the closed loop must be $0^\circ$ or $360^\circ$.
In this circuit, the inverting operational amplifier inherently provides a phase shift of $180^\circ$. To achieve the required total $360^\circ$ phase shift, the feedback network must provide exactly $180^\circ$ of phase shift. A single RC high-pass network can provide a maximum theoretical phase shift of $90^\circ$ (practically $\approx 60^\circ$). By cascading three identical RC sections, each contributes $60^\circ$ at a specific frequency $f_o$, resulting in a total feedback phase shift of $180^\circ$. At this specific frequency, the overall loop phase shift becomes $360^\circ$ (or $0^\circ$), fulfilling the Barkhausen criterion and sustaining oscillations.

**(b)** If one RC section is removed, the feedback network will consist of only two RC stages. Since a single practical RC stage can only provide a phase shift strictly less than $90^\circ$, two stages can provide a maximum theoretical phase shift approaching $180^\circ$ only at a frequency of zero (DC) or infinity, which requires infinite attenuation. Practically, two stages can never provide the exact $180^\circ$ required to satisfy the $360^\circ$ closed-loop Barkhausen phase condition. Consequently, the circuit will fail to oscillate.

---

### Q2. Colpitts Oscillator
**(a) Derive the expression for the frequency of oscillation ($f_o$).**
**(b) If $C_2/C_1 = 0.5$ and $A_v = 2$, can it sustain oscillation?**

**Solution:**
**(a)** In a Colpitts oscillator, the feedback network is an LC tank circuit comprising two capacitors ($C_1, C_2$) in series, placed in parallel with an inductor ($L$). The resonant frequency of this LC tank dictates the frequency of oscillation.
The equivalent capacitance of the two series capacitors is:
$$
C_{eq} = \frac{C_1 C_2}{C_1 + C_2}
$$
The resonant frequency of an LC tank is $f_o = \frac{1}{2\pi \sqrt{L C_{eq}}}$.
Substituting $C_{eq}$:
$$
f_o = \frac{1}{2\pi} \sqrt{\frac{C_1 + C_2}{L C_1 C_2}}
$$

**(b)** To sustain oscillation, the Barkhausen criterion requires $|A_v \beta| \ge 1$.
In a Colpitts oscillator utilizing an inverting amplifier, the feedback fraction is determined by the capacitive voltage divider in the tank circuit:
$$
\beta = \frac{C_1}{C_2}
$$
The required minimum closed-loop gain $A_v$ to sustain oscillation must compensate for this feedback fraction:
$$
A_v \ge \frac{1}{\beta} \Rightarrow A_v \ge \frac{C_2}{C_1}
$$
We are given that $\frac{C_2}{C_1} = 0.5$. Therefore, the required minimum gain is $A_v \ge 0.5$.
The provided closed-loop gain is $A_v = 2$.
Since $2 \ge 0.5$, the amplifier provides more than enough gain to overcome the feedback network's attenuation. **Yes**, the circuit will easily sustain continuous oscillation.

---

## 📌 Class Test 5

### Q1. 555-timer frequency divider.
**(a) Circuit diagram in monostable mode + frequency division justification.**
**(b) Sketch output waveform and time period relationship.**

**Solution:**
**(a)** **Monostable Frequency Divider Circuit:**
*(Circuit Description: Pin 2 (Trigger) receives the input pulse train. Pin 6 & 7 are tied together between an external Resistor $R$ (connected to $V_{CC}$) and Capacitor $C$ (connected to Ground). Pin 3 is the output).*

**Analytic Justification:**
In monostable mode, the 555 timer generates a single output pulse of fixed duration $W$ for every negative-going trigger pulse it receives. The pulse width is determined by:
$$
W = 1.1 R C
$$
To achieve frequency division by 2, we deliberately choose $R$ and $C$ such that the monostable pulse width $W$ is slightly longer than the time period $T$ of the incoming trigger pulse train, but shorter than $2T$ (i.e., $T < W < 2T$).
When the first trigger pulse arrives, the output goes HIGH for duration $W$. Because $W > T$, when the second trigger pulse arrives at time $T$, the 555 timer is already active (output HIGH) and charging its capacitor. The 555 timer completely ignores trigger pulses while it is in its active state. Therefore, the second pulse is ignored.
The output goes LOW after time $W$. The timer is now reset and waits for the next pulse. It will trigger on the third pulse (at time $2T$). Because the timer only triggers on every *alternating* input pulse, the output frequency is exactly half of the input frequency ($f_{out} = f_{in} / 2$).

**(b)** **Waveform Relationship:**
If input trigger train has period $T_{in}$:
*   Pulse 1 (t=0): Triggers timer. Output goes HIGH.
*   Pulse 2 (t=$T_{in}$): Ignored because output is still HIGH ($W > T_{in}$).
*   Timer turns off at $t = W$.
*   Pulse 3 (t=$2T_{in}$): Triggers timer again. Output goes HIGH.
The output cycle repeats every $2T_{in}$.
Therefore, $T_{out} = 2 T_{in}$, which implies $f_{out} = \frac{1}{2} f_{in}$.

---

### Q2. 555 Timer Astable Multivibrator
**(a) Determine $t_c, t_d, f_o$, and duty cycle. Explain $R_A, R_B, C$ effects.**
**(b) Effect if $R_B$ is increased.**

**Solution:**
**(a)** Given values: $R_A = 2.2\text{ k}\Omega$, $R_B = 3.9\text{ k}\Omega$, $C = 0.1\ \mu\text{F}$.

*   **Charging time / Positive pulse width ($t_c$):**
    During $t_c$, capacitor $C$ charges through both $R_A$ and $R_B$.
    $$
    t_c = 0.693(R_A + R_B)C = 0.693 (2.2\text{ k}\Omega + 3.9\text{ k}\Omega) \times 0.1\ \mu\text{F} = 0.693 \times 6.1\text{ k}\Omega \times 0.1\ \mu\text{F} = 0.4227\text{ ms}
    $$
*   **Discharging time / Negative pulse width ($t_d$):**
    During $t_d$, capacitor $C$ discharges only through $R_B$.
    $$
    t_d = 0.693(R_B)C = 0.693(3.9\text{ k}\Omega) \times 0.1\ \mu\text{F} = 0.2702\text{ ms}
    $$
*   **Total Period ($T$):**
    $$
    T = t_c + t_d = 0.4227 + 0.2702 = 0.6929\text{ ms}
    $$
*   **Free-running frequency ($f_o$):**
    $$
    f_o = \frac{1}{T} = \frac{1.44}{(R_A + 2R_B)C} = \frac{1}{0.6929\text{ ms}} = 1443.2\text{ Hz} \approx 1.44\text{ kHz}
    $$
*   **Duty Cycle ($D$):**
    $$
    D = \frac{t_c}{T} \times 100\% = \frac{R_A + R_B}{R_A + 2R_B} \times 100\% = \frac{6.1\text{ k}\Omega}{10.0\text{ k}\Omega} \times 100\% = 61\%
    $$

*Explanation:* $R_A, R_B,$ and $C$ explicitly define the RC time constants that govern the charging and discharging rates of the internal capacitor, thereby directly controlling the high-time, low-time, frequency, and duty cycle of the output square wave.

**(b)** **If $R_B$ is increased:**
*   $t_c = 0.693(R_A + R_B)C \Rightarrow$ Since $R_B$ is in the equation, $t_c$ will **increase**.
*   $t_d = 0.693 R_B C \Rightarrow$ Since it depends entirely on $R_B$, $t_d$ will **increase** significantly.
*   Total Period $T = t_c + t_d \Rightarrow$ Will **increase**.
*   Frequency $f_o = 1/T \Rightarrow$ Will **decrease**.
*   **Duty Cycle:** $D = \frac{R_A + R_B}{R_A + 2R_B}$. As $R_B$ becomes much larger than $R_A$ ($R_B \gg R_A$), the $R_A$ term becomes negligible. The equation approaches $D \approx \frac{R_B}{2R_B} = 0.5$. Therefore, as $R_B$ increases, the duty cycle **decreases toward 50%**.
