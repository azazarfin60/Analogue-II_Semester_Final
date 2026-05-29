# Digitized Class Tests - Analog Electronic Circuits-II (ECE 2105)

---

## Class Test 1
* **Institution:** Rajshahi University of Engineering & Technology (RUET)
* **Department:** Department of Electrical & Computer Engineering
* **Program:** B.Sc. in ECE
* **Course Code & Title:** ECE 2105: Analog Electronic Circuits-II
* **Series:** ECE 23
* **Class Test:** 01
* **Full Marks:** 20 | **Time:** 30 Minutes
* **CO Mapping:** CO1 (Analyze BJT, FET, and MOSFET multistage amplifiers, frequency response, and physical limitations)

---

### Questions

#### Q1. For the R-C coupled amplifier shown in Figure 1: [Marks: 10]
* **(a)** Determine the DC voltages $V_B$, $V_C$, and $V_E$ for each transistor ($Q_1$ and $Q_2$).
* **(b)** Calculate the DC currents $I_B$, $I_C$, and $I_E$ for each transistor.

##### Circuit Diagram (Figure 1):
```
                       +20 V (Vcc)
                         |
       +---------+-------+---------+--------+
       |         |                 |        |
      [ ] R11   [ ] RC1           [ ] R21  [ ] RC2
      [ ] 18k   [ ] 2.2k          [ ] 22k  [ ] 2.2k
       |         |                 |        |
       |         +-------||----+   |        +------||--- Output (Vo)
       |         |      Cc1    |   |        |     Cc3 (10uF)
       |       |/     (10uF)   |   |      |/
  Vi -||----+--| Q1            +---+------| Q2
     Cc (10uF)|  |>                 |      |>
             |   |                 |       |
            [ ] [ ] RE1           [ ]     [ ] RE2
        R12 [ ] [ ] 1k        R22 [ ]3.3k [ ] 1.2k
       4.7k  |   |   +--||--+ 3.3k  |       |   +--||--+
             |   |   | CE1  |       |       |   | CE2  |
             |   |   (20uF) |       |       |   (20uF) |
             |   +---+------+       |       +---+------+
             |   |                  |       |
       ------+---+------------------+-------+----------- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Power Supplies:**
   * $V_{CC} = +20\text{ V}$ connected to the top rail.
   * Reference Ground ($0\text{ V}$) connected to the bottom rail.
2. **Active Devices:**
   * **$Q_1$:** NPN BJT with common-emitter configuration. DC current gain $\beta_1 = 160$, base-emitter drop $V_{BE} = 0.7\text{ V}$.
   * **$Q_2$:** NPN BJT with common-emitter configuration. DC current gain $\beta_2 = 90$, base-emitter drop $V_{BE} = 0.7\text{ V}$.
3. **Stage 1 Configuration ($Q_1$):**
   * **Base Biasing:** Voltage divider network with $R_{11} = 18\text{ k}\Omega$ (top) and $R_{12} = 4.7\text{ k}\Omega$ (bottom).
   * **Input Coupling:** AC input signal $V_i$ coupled via capacitor $C_c = 10\ \mu\text{F}$.
   * **Collector Load:** Resistor $R_{C1} = 2.2\text{ k}\Omega$ connected to $+20\text{ V}$.
   * **Emitter Resistance & Bypass:** Resistor $R_{E1} = 1\text{ k}\Omega$ connected to ground, bypassed by $C_{E1} = 20\ \mu\text{F}$ capacitor.
4. **Interstage Coupling:**
   * The collector of $Q_1$ connects to the base of $Q_2$ viacoupling capacitor $C_{c1} = 10\ \mu\text{F}$.
5. **Stage 2 Configuration ($Q_2$):**
   * **Base Biasing:** Voltage divider network with $R_{21} = 22\text{ k}\Omega$ (top) and $R_{22} = 3.3\text{ k}\Omega$ (bottom).
   * **Collector Load:** Resistor $R_{C2} = 2.2\text{ k}\Omega$ connected to $+20\text{ V}$.
   * **Emitter Resistance & Bypass:** Resistor $R_{E2} = 1.2\text{ k}\Omega$ connected to ground, bypassed by $C_{E2} = 20\ \mu\text{F}$ capacitor.
   * **Output Coupling:** Output voltage $V_o$ is coupled via capacitor $C_{c3} = 10\ \mu\text{F}$.

---

#### Q2. Prove that although a feedback pair configuration operates with approximately unity voltage gain, it provides a very high current gain. [Marks: 10]

---

## Class Test 2
* **Institution:** Rajshahi University of Engineering & Technology (RUET)
* **Department:** Department of Electrical & Computer Engineering
* **Program:** B.Sc. in ECE
* **Course Code & Title:** ECE 2105: Analog Electronic Circuits-II
* **Series:** ECE 23
* **Class Test:** 02
* **Full Marks:** 20 | **Time:** 30 Minutes
* **CO Mapping:** CO1 (Analyze BJT, FET, and MOSFET multistage amplifiers, frequency response, and physical limitations)

---

### Questions

#### Q1. For the BJT amplifier shown in Figure 1: [Marks: 10]
* **(a)** Determine the low-cutoff frequencies ($f_{Ls}$, $f_{Lc}$, $f_{LE}$) for the network.
* **(b)** Sketch the resulting frequency response using a Bode plot.

##### Circuit Parameters:
* $V_{CC} = +20\text{ V}$
* $\beta = 100$ | $V_{BE} = 0.7\text{ V}$
* $R_1 = 40\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$, $R_C = 4\text{ k}\Omega$, $R_E = 2\text{ k}\Omega$
* $R_L = 2.2\text{ k}\Omega$
* Capacitors: $C_s = 10\ \mu\text{F}$ (source coupling), $C_E = 20\ \mu\text{F}$ (emitter bypass), $C_c = 1\ \mu\text{F}$ (drain coupling)

##### Circuit Diagram (Figure 1):
```
                       Vcc (+20V)
                        |
                +-------+-------+
                |               |
               [ ] R1 (40k)    [ ] Rc (4k)
               [ ]             [ ]
                |               |
    Vi --||-----+               +------||------ Vo
        Cs      |               |      Cc       |
      (10uF)    |             |/     (1uF)     [ ] RL (2.2k)
                +-------------|                [ ]
                              |>                |
                               |               |
                              [ ] RE (2k)      |
              [ ] R2 (10k)    [ ]              |
              [ ]              |   +--||--+    |
               |               +---+  CE  +----+
               |               |   |(20uF)|    |
               |               |   +------+    |
    ------------+---------------+---------------+---- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Biasing Scheme:** Voltage divider network with $R_1 = 40\text{ k}\Omega$ and $R_2 = 10\text{ k}\Omega$ provides DC base bias.
2. **Active Device:** NPN BJT in common-emitter configuration. DC parameters: $\beta = 100$, $r_e = \frac{26\text{ mV}}{I_E}$.
3. **Input Loop:** The source signal $V_i$ drives the base through $C_s = 10\ \mu\text{F}$. Input impedance is $Z_i = R_1 \parallel R_2 \parallel \beta(r_e + R_E)$ without bypass, or $Z_i = R_1 \parallel R_2 \parallel \beta r_e$ when fully bypassed.
4. **Emitter Branch:** $R_E = 2\text{ k}\Omega$ bypassed by $C_E = 20\ \mu\text{F}$ introduces a low-frequency pole/zero.
5. **Output Loop:** Collector load $R_C = 4\text{ k}\Omega$ coupled to load $R_L = 2.2\text{ k}\Omega$ via output capacitor $C_c = 1\ \mu\text{F}$.

---

#### Q2. For the FET amplifier shown in Figure 2: [Marks: 10]
* **(a)** Determine the low-cutoff frequencies ($f_{LG}$, $f_{LC}$, $f_{LS}$) for the network.
* **(b)** Determine the high-cutoff frequencies ($f_{Hi}$, $f_{Ho}$) for the network.

##### Circuit Parameters:
* $V_{DD} = +20\text{ V}$
* $I_{DSS} = 8\text{ mA}$ | $V_P = -4\text{ V}$
* $R_{sig} = 10\text{ k}\Omega$, $R_G = 1\text{ M}\Omega$, $R_D = 4.7\text{ k}\Omega$, $R_S = 1\text{ k}\Omega$, $R_L = 2.2\text{ k}\Omega$
* Capacitors: $C_G = 0.01\ \mu\text{F}$, $C_S = 2\ \mu\text{F}$, $C_C = 0.5\ \mu\text{F}$
* Parasitic Capacitances: $C_{gd} = 2\text{ pF}$, $C_{gs} = 4\text{ pF}$, $C_{ds} = 0.5\text{ pF}$
* Wiring Capacitances: $C_{Wi} = 5\text{ pF}$ (input), $C_{Wo} = 6\text{ pF}$ (output)

##### Circuit Diagram (Figure 2):
```
                                VDD (+20V)
                                    |
                                   [ ] RD (4.7k)
                                   [ ]
                                    |
                    +---------------+------||---------- Vo
                    |   Cgd (2pF)   |     Cc (0.5uF)    |
                    +-----||----+   |                  [ ] RL (2.2k)
                    |           |   |                  [ ]
       CG           |          (D)  |                   |
Vi --||-------------+---------(G)   |                   |
    (0.01uF)        |    JFET   \   |                   |
                    |            (S)+-------+           |
                   [ ] RG (1M)    | |       |           |
                   [ ]            | | Cds   |           |
                    |   Cgs (4pF) | |(0.5pF)|           |
                    +-----||------+ |       |           |
                    |               |      --- CWo      |
                   --- CWi         [ ] RS  --- (6pF)    |
                   --- (5pF)       [ ] (1k) |           |
                    |               |       |           |
                    |               +--||---+           |
                    |               |  CS (2uF)         |
                    |               |       |           |
  ------------------+---------------+-------+-----------+---- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Transistor Type:** n-channel JFET operated in self-bias configuration.
2. **DC Biasing:** $R_S = 1\text{ k}\Omega$ sets $V_{GS} = -I_D R_S$, and $R_G = 1\text{ M}\Omega$ ties the gate to ground reference ($0\text{ V}$). Transconductance is $g_{m0} = \frac{2 I_{DSS}}{|V_P|} = 4\text{ mS}$.
3. **High-Frequency Miller Model:**
   * **Input Miller Capacitance:** $C_{Mi} = (1 - A_v) C_{gd}$
   * **Output Miller Capacitance:** $C_{Mo} = (1 - 1/A_v) C_{gd}$
   * **Total Input High-Frequency Capacitance:** $C_i = C_{Wi} + C_{gs} + C_{Mi}$
   * **Total Output High-Frequency Capacitance:** $C_o = C_{Wo} + C_{ds} + C_{Mo}$

---

## Class Test 3
* **Institution:** Rajshahi University of Engineering & Technology (RUET)
* **Department:** Department of Electrical & Computer Engineering
* **Program:** B.Sc. in ECE
* **Course Code & Title:** ECE 2105: Analog Electronic Circuits-II
* **Series:** ECE 23
* **Class Test:** 03
* **Full Marks:** 20 | **Time:** 30 Minutes
* **CO Mapping:** CO2 (Design practical circuits using feedback amplifiers, op-amp circuits, oscillators, 555 timers, and active filters)

---

### Questions

#### Q1. Two operational amplifiers have common-mode rejection ratios (CMRR) of 90 dB and 120 dB, respectively. Analyze which op-amp provides better common-mode noise suppression and justify your conclusion with appropriate reasoning based on CMRR characteristics and practical circuit performance. Which one is better? [Marks: 5, CO2]

---

#### Q2. An ideal operational amplifier integrator has circuit parameters such as that: $R_1 C_f = 1$ and the input frequency range of proper operation is $10\text{ Hz} - 1\text{ kHz}$, as shown in Fig. 01. [Marks: 5, CO2]

A sinusoidal input is applied in two separate cases:
* **Case I:** $V_i(t) = 5\sin(2\pi f_s t)$, with signal frequency $f_s = 1\text{ kHz}$.
* **Case II:** $V_i(t) = 5\sin(2\pi f_s t)$, with signal frequency $f_s = 5\text{ Hz}$.

Derive the output voltage expression $V_o(t)$ mathematically for both cases and analyze the output waveforms based on the shape and amplitude in each case.

##### Circuit Diagram (Fig. 01):
```
                    Cf
                  +--||---+
                  |       |
             R1   |  |\   |
    Vi o-----[ ]---+--|-\  |
            (1)      |  \-+----o Vo
                     |   >|    |
             ROM  +--|+/  |   [ ] RL
    GND o----[ ]---+  |/   |   [ ]
                          |    |
    -----------------------+----+---- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Ideal Op-Amp Integrator:** Standard inverting configuration. The inverting terminal ($-$) acts as a virtual ground ($V_n \approx 0\text{ V}$).
2. **Transfer Function:**
   $$V_o(t) = -\frac{1}{R_1 C_f} \int V_i(t) dt + V_o(0)$$
3. **Offset Cancellation:** Resistor $R_{OM} = R_1 \parallel R_L$ is connected between non-inverting terminal ($+$) and ground to minimize input bias current offsets.
4. **Behavior Analysis:** For $5\text{ Hz}$ input, the signal falls outside the high-pass integration limit ($10\text{ Hz} - 1\text{ kHz}$), leading to op-amp open-loop saturation behavior.

---

#### Q3. Fig. 02 shows an operational amplifier differentiator designed to operate effectively over an input frequency range of $10\text{ Hz}$ to $1\text{ kHz}$. [Marks: 10, CO2]

Assume that the circuit satisfies $R_f C_1 = 1$. Consider two separate cases of excitation at $1\text{ kHz}$:
* **Case I:** A $5\text{ V}$ peak sine wave is applied at the input ($V_i(t) = 5\sin(2\pi f t)$).
* **Case II:** A $10\text{ V}$ peak cosine wave is applied at the input ($V_i(t) = 10\cos(2\pi f t)$).

Analyze the corresponding output waveforms for both cases, clearly indicating the amplitude relationship and the phase difference between the input and output signals.

##### Circuit Diagram (Fig. 02):
```
                    RF
                  +-[ ]---+
                  |       |
             C1   |  |\   |
    Vi o-----||----+--|-\  |
                     |  \-+----o Vo
                     |   >|    |
             ROM  +--|+/  |   [ ] RL
    GND o----[ ]---+  |/   |   [ ]
                          |    |
    -----------------------+----+---- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Ideal Op-Amp Differentiator:** Standard inverting configuration. Output equation:
   $$V_o(t) = -R_f C_1 \frac{d V_i(t)}{d t}$$
2. **Inverting Virtual Ground:** $V_n \approx 0\text{ V}$. Input current is $i_i(t) = C_1 \frac{d V_i}{d t}$.
3. **Feedback:** Feedback resistor $R_f$ is connected between inverting input and output node.

---

## Class Test 4
* **Institution:** Rajshahi University of Engineering & Technology (RUET)
* **Department:** Department of Electrical & Computer Engineering
* **Program:** B.Sc. in ECE
* **Course Code & Title:** ECE 2105: Analog Electronic Circuits-II
* **Series:** ECE 23
* **Class Test:** 04
* **Full Marks:** 20 | **Time:** 30 Minutes
* **CO Mapping:** CO2 (Design practical circuits using feedback amplifiers, op-amp circuits, oscillators, 555 timers, and active filters)

---

### Questions

#### Q1. An Op-Amp circuit is constructed with a feedback network formed by cascading three identical RC sections. During testing, it is observed that the circuit generates a sinusoidal output without any external input signal. Further investigation shows that each RC section introduces a phase shift that depends on frequency and at a certain frequency, the total phase shift of the feedback network becomes $180^\circ$. The amplifier configuration provides the additional phase shift required for sustained oscillation. [Marks: 10, CO2]
* **(a)** Based on the given observations, determine the type of oscillator and explain the mechanism of oscillation by applying the Barkhausen Criterion.
* **(b)** Analyze the effect on circuit operation if one of the RC sections is removed from the feedback network. Justify your answer based on phase shift and oscillation conditions.

---

#### Q2. An Op-Amp based Colpitts oscillator is designed using an inverting amplifier configuration with a gain defined by $R_f$ and $R_i$. The feedback network consists of an inductor L and two capacitors $C_1$ and $C_2$. During the commissioning of the circuit, it is found that the circuit fails to oscillate despite the LC components being correctly calculated for the desired frequency. [Marks: 10, CO2]
* **(a)** From the given description, construct the equivalent oscillator model and derive the expression for the frequency of oscillation ($f_o$).
* **(b)** Analyze the relationship between the capacitor ratio ($C_2 / C_1$) and the closed-loop gain ($A_v = R_f / R_i$). For $C_2 / C_1 = 0.5$, determine whether the circuit can sustain oscillation with a gain $A_v = 2$. Justify your conclusion based on oscillation conditions.

##### Reference Circuit Diagram (Standard Op-Amp Colpitts Oscillator):
```
                    Rf
                 +--[ ]---+
                 |        |
            Ri   |  |\    |
   V_f o---[ ]---+--|-\   |
                    |  \--+----o Vo
                 +--|+/
                 |  |/
                GND
                
   Feedback network (Colpitts tank):
         Vo
         |
         +-------+-------+
         |       |       |
        --- C2   |      ( ) L
        ---      |      ( )
         |       |       |
        GND      +-------+
         |       |
        --- C1   |
        ---      |
         |       |
         +-------+
         |
         V_f
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Op-Amp Inverting Amplifier:** The Gain is $A_v = -\frac{R_f}{R_i}$, providing a $180^\circ$ phase shift.
2. **Tank Feedback Network:**
   * Capacitor $C_2$ is connected in parallel with the output node $V_o$ and ground.
   * Inductor $L$ is in series with the feedback loop, connected between output $V_o$ and feedback node $V_f$.
   * Capacitor $C_1$ is connected between feedback node $V_f$ and ground.
3. **Resonant Frequency:**
   $$f_o = \frac{1}{2\pi \sqrt{L C_{eq}}} \quad \text{where} \quad C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$$
4. **Sustained Oscillation Condition:**
   $$A_v \ge \frac{C_2}{C_1} \Rightarrow \frac{R_f}{R_i} \ge \frac{C_2}{C_1}$$

---

## Class Test 5
* **Institution:** Rajshahi University of Engineering & Technology (RUET)
* **Department:** Department of Electrical & Computer Engineering
* **Program:** B.Sc. in ECE
* **Course Code & Title:** ECE 2105: Analog Electronic Circuits-II
* **Series:** ECE 23
* **Class Test:** 05
* **Full Marks:** 20 | **Time:** 30 Minutes
* **CO Mapping:** CO2 (Design practical circuits using feedback amplifiers, op-amp circuits, oscillators, 555 timers, and active filters)

---

### Questions

#### Q1. A 555-timer circuit is configured such that its output frequency becomes half of a given reference signal. [Marks: 10, CO2]
* **(a)** Draw the circuit diagram of the 555 timer in a monostable mode and also explain analytically how the selection of resistor and capacitor values influences the output frequency. Justify how the circuit can achieve a frequency division operation. [Marks: 6]
* **(b)** Sketch the output waveform and explain the relationship between time period and frequency. [Marks: 4]

---

#### Q2. The following 555 Timer circuit is configured as an astable multivibrator, as shown in Fig. 1. [Marks: 10, CO2]
* **(a)** Determine the positive pulse width $t_c$, negative pulse width $t_d$, free-running frequency $f_o$, and duty cycle of the circuit. Also explain how the values of $R_A$, $R_B$ and $C$ affect these quantities. [Marks: 5]
* **(b)** If $R_B$ is increased while keeping other parameters unchanged, explain how $t_c$, $t_d$, frequency, and duty cycle will change. Analyze your results with the original case and comment on the change in duty cycle. [Marks: 5]

##### Circuit Diagram (Fig. 1):
```
                  +Vcc (+5V)
                     |
            +--------+--------+
            |                 |
           [ ] RA (2.2k)      |
           [ ]                |
            |                 |
            +------------(7)  |
            |            | |  |
           [ ] RB (3.9k) | |  |
           [ ]           | |  |
            |            | |  |
            +------------(6)  |
            |            |    |
            +------------(2)  |
            |                 |
           --- C (0.1uF)     (8) (4)
           ---               +--+--+
            |                | 555 |------(3)--> Output
            |                +--+--+
            |                (1) (5)
            |                 |   |
            |                 |  --- C1 (0.01uF)
            |                 |  ---
            |                 |   |
      ------+-----------------+---+---- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Astable Multivibrator Parameters:**
   * $t_c = 0.693 (R_A + R_B) C$ (Charging time / output High)
   * $t_d = 0.693 R_B C$ (Discharging time / output Low)
   * $T = t_c + t_d = 0.693 (R_A + 2 R_B) C$ (Total Period)
   * $f_o = \frac{1.44}{(R_A + 2 R_B) C}$ (Free-running oscillation frequency)
   * $D = \frac{t_c}{T} = \frac{R_A + R_B}{R_A + 2 R_B}$ (Duty Cycle)
2. **External Pin Wire Map:**
   * **Pin 8 (VCC) & Pin 4 (RESET)** connected directly to $+5\text{ V}$ to prevent spurious resets.
   * **Pin 1 (GND)** connected to ground.
   * **Pin 7 (DISCHARGE)** connected between resistors $R_A$ and $R_B$.
   * **Pin 6 (THRESHOLD) & Pin 2 (TRIGGER)** are tied together and connected to the junction of $R_B$ and the timing capacitor $C = 0.1\ \mu\text{F}$.
   * **Pin 5 (CONTROL VOLTAGE)** connected to ground through noise-bypass capacitor $C_1 = 0.01\ \mu\text{F}$.
   * **Pin 3 (OUTPUT)** provides the square wave pulse output.
