# 📝 RUET 2017 Even Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2205)

---

## SECTION - A

### Q.1
**(a) What is the merit of a cascaded amplifier? [02 Marks]**

**Answer:**
A single-stage amplifier often cannot satisfy all the requirements of a practical electronic system (such as simultaneous high voltage gain, high current gain, very high input impedance, and very low output impedance). The primary merit of a cascaded (multi-stage) amplifier is its ability to combine the advantageous characteristics of different transistor configurations. By cascading stages, the overall voltage and current gain is the product of the individual stage gains. For example, a cascaded JFET-BJT amplifier uses the JFET for exceptionally high input impedance and the BJT for extremely high voltage gain, achieving a performance level impossible with a single device.

---

**(b) For the cascaded amplifier shown below, calculate the input impedance ($Z_i$), output impedance ($Z_o$), voltage gain ($A_v$), and the resulting output voltage ($v_o$). [04 Marks]**

**Solution:**
**Stage 1: n-channel JFET (Common-Source)**
1.  **DC Analysis:**
    $V_{GS} = -I_D R_S = -680 I_D$
    $I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2 = 10\text{ mA} \left(1 - \frac{V_{GS}}{-4}\right)^2$
    Solving the quadratic equation iteratively or exactly yields $V_{GS} \approx -1.9\text{ V}$ and $I_D \approx 2.8\text{ mA}$.
2.  **AC Parameters:**
    $g_{m0} = \frac{2 I_{DSS}}{|V_P|} = \frac{2(10\text{ mA})}{4\text{ V}} = 5\text{ mS}$
    $g_m = g_{m0} \left(1 - \frac{V_{GS}}{V_P}\right) = 5\text{ mS} \left(1 - \frac{-1.9}{-4}\right) \approx 2.625\text{ mS}$
    Input impedance of Stage 1: $Z_{i1} = R_G = 3.3\text{ M}\Omega$
    Output impedance of Stage 1 (without load): $Z_{o1} = R_D = 2.4\text{ k}\Omega$

**Stage 2: NPN BJT (Common-Emitter)**
1.  **DC Analysis:**
    $V_{th} = \frac{R_{B2}}{R_{B1} + R_{B2}} V_{CC} = \frac{4.7\text{ k}\Omega}{15\text{ k}\Omega + 4.7\text{ k}\Omega} \times 20\text{ V} = 4.77\text{ V}$
    $R_{th} = 15\text{ k}\Omega \parallel 4.7\text{ k}\Omega = 3.58\text{ k}\Omega$
    $I_E = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{4.77 - 0.7}{1\text{ k}\Omega + 3.58\text{ k}\Omega / 200} = \frac{4.07\text{ V}}{1.018\text{ k}\Omega} = 4.0\text{ mA}$
2.  **AC Parameters:**
    $r_e = \frac{26\text{ mV}}{I_E} = \frac{26\text{ mV}}{4.0\text{ mA}} = 6.5\ \Omega$
    Input impedance of Stage 2: $Z_{i2} = R_{B1} \parallel R_{B2} \parallel \beta r_e = 3.58\text{ k}\Omega \parallel 200(6.5\ \Omega) = 3.58\text{ k}\Omega \parallel 1.3\text{ k}\Omega = 0.953\text{ k}\Omega$
    Stage 2 Voltage Gain: $A_{v2} = -\frac{R_C}{r_e} = -\frac{2200}{6.5} = -338.46$

**Overall System Parameters:**
*   **Total Input Impedance ($Z_i$):** $Z_i = Z_{i1} = 3.3\text{ M}\Omega$
*   **Total Output Impedance ($Z_o$):** $Z_o = R_C = 2.2\text{ k}\Omega$ (Assuming $r_o \approx \infty$)
*   **Stage 1 Loaded Voltage Gain ($A_{v1}$):**
    $A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.625\text{ mS} \times (2.4\text{ k}\Omega \parallel 0.953\text{ k}\Omega) = -2.625\text{ mS} \times 0.682\text{ k}\Omega = -1.79$
*   **Total Voltage Gain ($A_v$):**
    $A_v = A_{v1} \times A_{v2} = (-1.79) \times (-338.46) \approx 605.8$
*   **Resulting Output Voltage ($v_o$):**
    $v_o = A_v \times v_s = 605.8 \times 1\text{ mV} = 0.606\text{ V}$ (or $606\text{ mV}$ in-phase)

---

**(c) Explain with a neat sketch the operation of a CMOS circuit. Why is it called an inverter? [04 Marks]**

**Answer:**
A CMOS (Complementary Metal-Oxide-Semiconductor) inverter consists of a p-channel MOSFET (PMOS) connected in series with an n-channel MOSFET (NMOS). The source of the PMOS is tied to $+V_{DD}$, and the source of the NMOS is tied to Ground. Their gates are tied together to form the input ($V_{in}$), and their drains are tied together to form the output ($V_{out}$).

**Operation:**
1.  **Input HIGH ($V_{in} = V_{DD}$):** The NMOS gate-to-source voltage is highly positive, turning the NMOS ON (acting as a closed switch). The PMOS gate-to-source voltage is $0\text{V}$, turning the PMOS OFF (acting as an open switch). The output node is pulled directly to Ground through the NMOS. Thus, $V_{out} = 0\text{V}$ (Logic LOW).
2.  **Input LOW ($V_{in} = 0\text{V}$):** The NMOS gate-to-source voltage is $0\text{V}$, turning it OFF. The PMOS gate-to-source voltage is highly negative ($-V_{DD}$), turning the PMOS ON. The output node is pulled directly to $V_{DD}$ through the PMOS. Thus, $V_{out} = V_{DD}$ (Logic HIGH).

**Why it is called an inverter:**
It is called an inverter because it performs the Boolean logic NOT operation. A Logic HIGH input results in a Logic LOW output, and a Logic LOW input results in a Logic HIGH output. It strictly inverts the digital state of the input signal.

---

### Q.2
**(a) Draw and explain the internal structure of a 3-input NAND gate using CMOS technology. [06 Marks]**

**Answer:**
**Structure:**
A 3-input CMOS NAND gate consists of 6 transistors in total: 3 PMOS transistors and 3 NMOS transistors.
*   **Pull-up Network (PMOS):** The 3 PMOS transistors are connected in **parallel** between the $V_{DD}$ supply rail and the output node ($V_{out}$).
*   **Pull-down Network (NMOS):** The 3 NMOS transistors are connected in **series** between the output node ($V_{out}$) and Ground.
*   **Inputs (A, B, C):** Each input is tied to the gate of one PMOS and one corresponding NMOS transistor.

**Explanation of Operation:**
For a NAND gate, the output is LOW ($0$) only when ALL inputs are HIGH ($1$). In all other cases, the output is HIGH ($1$).
*   **Case 1: All inputs A, B, and C are HIGH ($V_{DD}$):** All 3 parallel PMOS transistors turn OFF. All 3 series NMOS transistors turn ON. Because all NMOS are ON, they create a continuous conductive path from $V_{out}$ to Ground. The output is pulled LOW.
*   **Case 2: Any one (or more) inputs are LOW ($0\text{V}$):** The corresponding PMOS transistor(s) will turn ON, and the corresponding NMOS transistor(s) will turn OFF. The OFF NMOS breaks the series chain to Ground, preventing current sinking. The ON PMOS creates a direct conductive path from $V_{DD}$ to $V_{out}$. Therefore, the output is pulled HIGH.

---

**(b) For the following network, determine the change of gain with and without feedback. The JFET transconductance is $g_m = 5800\ \mu\text{S}$. [06 Marks]**

**Solution:**
The circuit is a JFET common-source amplifier employing **voltage-series negative feedback** via the $R_1$ and $R_2$ voltage divider.

**1. Gain without feedback ($A$):**
Without the feedback loop closed, the voltage gain is simply the open-loop gain of the JFET stage.
The equivalent load resistance at the drain is $R_L' = R_D \parallel R_L \parallel (R_1 + R_2)$. Assuming $(R_1 + R_2) = 120\text{ k}\Omega$ is much larger than $R_D = 10\text{ k}\Omega$ and $R_L = 10\text{ k}\Omega$, we approximate $R_L' \approx R_D \parallel R_L = 5\text{ k}\Omega$.
$$A = -g_m R_L' = -5800\times 10^{-6}\text{ S} \times 5000\ \Omega = -29$$

**2. Feedback Factor ($\beta$):**
The feedback network samples the output voltage and returns a fraction to the source terminal.
$$\beta = -\frac{R_2}{R_1 + R_2} = -\frac{20\text{ k}\Omega}{100\text{ k}\Omega + 20\text{ k}\Omega} = -\frac{20}{120} = -0.1667$$

**3. Gain with feedback ($A_f$):**
$$A_f = \frac{A}{1 + \beta A} = \frac{-29}{1 + (-0.1667)(-29)} = \frac{-29}{1 + 4.834} = \frac{-29}{5.834} = -4.97$$

**Change in Gain:**
*   Gain without feedback: $-29$
*   Gain with feedback: $-4.97$
*   Absolute change in gain magnitude: $|-29| - |-4.97| = 29 - 4.97 = 24.03$

The negative feedback has significantly reduced the voltage gain (desensitizing it), which in turn will improve bandwidth and decrease distortion.

---

### Q.3
**(a) Define a current mirror circuit. Why is it called a current mirror? Explain. [04 Marks]**

**Answer:**
A **current mirror** is a circuit designed to copy a current flowing through one active device and control the current in another active device, keeping the output current constant regardless of loading.

**Why it is called a "mirror":**
It is called a mirror because the current in the output branch is an exact reflection (or scaled mirror image) of a highly stable reference current generated in the input branch. The input and output transistors are perfectly matched (same $V_{BE}$ and same physical characteristics) and their bases and emitters are tied together. Because they share the exact same $V_{BE}$, the base-emitter junction equations force them to draw the exact same collector current. Thus, the output "mirrors" the input.

---

**(b) Calculate the current $I$ through each of the transistors $Q_2$ and $Q_3$ in the Wilson current mirror circuit. Assume identical transistors with $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. [04 Marks]**

**Solution:**
This is a standard Wilson Current Mirror configuration.
First, we calculate the reference current ($I_{ref}$) set by resistor $R = 1.3\text{ k}\Omega$. The voltage drop across $R$ is $V_{CC}$ minus the two base-emitter drops of $Q_1$ and $Q_3$ (or $Q_2$ and $Q_3$).
$$I_{ref} = \frac{V_{CC} - V_{BE1} - V_{BE3}}{R} = \frac{6\text{ V} - 0.7\text{ V} - 0.7\text{ V}}{1.3\text{ k}\Omega} = \frac{4.6\text{ V}}{1.3\text{ k}\Omega} = 3.538\text{ mA}$$

The exact output current $I$ (which is the collector current of $Q_3$ and ultimately equal to the collector current of $Q_2$) for a Wilson current mirror with finite $\beta$ is given by:
$$I = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right)$$
For $\beta = 100$:
$$\frac{2}{100^2 + 100} = \frac{2}{10100} \approx 0.000198$$
$$I = 3.538\text{ mA} \times \left( \frac{1}{1.000198} \right) \approx 3.537\text{ mA}$$

Because the Wilson mirror is highly accurate, the current $I$ through $Q_3$ (the output transistor) and $Q_2$ are essentially identical.
*   Current through $Q_3 \approx 3.537\text{ mA}$
*   Current through $Q_2 \approx 3.537\text{ mA}$

---

**(c) Calculate the DC voltages $V_{o1}$ and $V_{o2}$ for the symmetrical differential BJT amplifier circuit. [04 Marks]**

**Solution:**
1.  **Tail Current Calculation:**
    The emitters of both $Q_1$ and $Q_2$ are tied together and connected to the $-9\text{V}$ rail through $R_{EE} = 3.3\text{ k}\Omega$.
    Assuming ideal matched transistors and $0\text{V}$ DC at the bases, the voltage at the common emitter node is $V_E = -0.7\text{ V}$.
    The total tail current $I_{EE}$ is:
    $$I_{EE} = \frac{V_E - (-V_{EE})}{R_{EE}} = \frac{-0.7\text{ V} - (-9\text{ V})}{3.3\text{ k}\Omega} = \frac{8.3\text{ V}}{3.3\text{ k}\Omega} = 2.515\text{ mA}$$

2.  **Individual Emitter/Collector Currents:**
    Because the circuit is symmetrical and $0\text{V}$ is applied to both bases, the tail current splits exactly in half.
    $$I_{E1} = I_{E2} = \frac{I_{EE}}{2} = \frac{2.515\text{ mA}}{2} = 1.2575\text{ mA}$$
    Assuming $I_C \approx I_E$:
    $$I_{C1} = I_{C2} \approx 1.2575\text{ mA}$$

3.  **Output DC Voltages:**
    The DC output voltages are measured at the collectors.
    $$V_{o1} = V_{CC} - I_{C1}R_{C1} = 9\text{ V} - (1.2575\text{ mA} \times 3.9\text{ k}\Omega) = 9\text{ V} - 4.904\text{ V} = 4.096\text{ V}$$
    $$V_{o2} = V_{CC} - I_{C2}R_{C2} = 9\text{ V} - (1.2575\text{ mA} \times 3.9\text{ k}\Omega) = 4.096\text{ V}$$

Therefore, $V_{o1} = V_{o2} = 4.096\text{ V}$.

---

### Q.4
**(a) What are the types of feedback connections? Explain voltage-shunt feedback configuration. [04 Marks]**

**Answer:**
There are four basic types of negative feedback connections, categorized by how the signal is sampled at the output and mixed at the input:
1.  Voltage-Series Feedback
2.  Voltage-Shunt Feedback
3.  Current-Series Feedback
4.  Current-Shunt Feedback

**Voltage-Shunt Feedback Configuration:**
In this topology, the output **voltage** is sampled (connected in parallel with the load) and a **current** proportional to this output voltage is fed back to the input in parallel (shunt) with the signal source.
*   Because the output is sampled in parallel, it tends to keep the output voltage constant, thereby drastically **decreasing the output impedance**.
*   Because the feedback is mixed in parallel at the input, the feedback current subtracts from the source current, demanding more current from the source for a given voltage, thereby drastically **decreasing the input impedance**.
*   This configuration is essentially a transresistance amplifier (converts input current to output voltage). The classic example is an inverting operational amplifier configuration.

---

**(b) Calculate (i) Oscillation frequency ($f_o$), (ii) Feedback factor ($\beta$), and (iii) Voltage gain ($A_v$) for the Clapp JFET oscillator network. [05 Marks]**

**Solution:**
Based on the schematic provided, the tank circuit contains two inductors ($L_1 = 30\ \mu\text{H}, L_2 = 10\ \mu\text{H}$) in series, and two identical capacitors ($C_1 = 0.01\ \mu\text{F}, C_2 = 0.01\ \mu\text{F}$) in series.
Wait, standard Clapp utilizes three capacitors. Let's analyze the provided schematic's equivalent tank.
The inductors are in series: $L_{eq} = L_1 + L_2 = 30\ \mu\text{H} + 10\ \mu\text{H} = 40\ \mu\text{H}$.
The capacitors are in series: $C_{eq} = \frac{C_1 C_2}{C_1 + C_2} = \frac{0.01\ \mu\text{F}}{2} = 0.005\ \mu\text{F} = 5\text{ nF}$.

**(i) Oscillation Frequency ($f_o$):**
$$f_o = \frac{1}{2\pi \sqrt{L_{eq} C_{eq}}} = \frac{1}{2\pi \sqrt{40 \times 10^{-6} \times 5 \times 10^{-9}}}$$
$$f_o = \frac{1}{2\pi \sqrt{200 \times 10^{-15}}} = \frac{1}{2\pi \sqrt{2 \times 10^{-13}}} = \frac{1}{2\pi (4.47 \times 10^{-7})} = 355.88\text{ kHz}$$

**(ii) Feedback Factor ($\beta$):**
In this type of parallel LC oscillator (similar to Colpitts), the feedback fraction determined by the capacitive voltage divider is:
$$\beta = \frac{C_1}{C_2} = \frac{0.01\ \mu\text{F}}{0.01\ \mu\text{F}} = 1$$

**(iii) Required Voltage Gain ($A_v$):**
To satisfy the Barkhausen criterion for sustained oscillation, the magnitude of the loop gain must be at least 1:
$$|A_v \beta| \ge 1 \Rightarrow A_v \ge \frac{1}{\beta}$$
Since $\beta = 1$, the minimum required voltage gain of the amplifier is $A_v = 1$.

---

**(c) What is the gain and frequency stability condition for an oscillator? [03 Marks]**

**Answer:**
*   **Gain Condition:** The oscillator must satisfy the Barkhausen amplitude criterion, $|A \beta| \ge 1$. For oscillations to start, $|A \beta|$ must be slightly greater than $1$. Once oscillations reach the desired amplitude, non-linearities in the active device reduce the gain until $|A \beta|$ stabilizes at exactly $1$.
*   **Frequency Stability Condition:** The circuit must satisfy the Barkhausen phase criterion: the total phase shift around the closed loop must be $0^\circ$ (or $360^\circ$). The oscillator will lock onto the specific frequency ($f_o$) where the reactive feedback network provides exactly the phase shift required to bring the total loop phase to zero. A highly stable oscillator (like a crystal) has a very steep phase-vs-frequency curve ($d\phi/d\omega$), meaning small phase perturbations cause virtually zero frequency drift.

---

## SECTION - B

### Q.5
**(a) What is an operational amplifier (op-amp)? Write down the electrical properties of an Ideal op-amp. [04 Marks]**

**Answer:**
An **operational amplifier (op-amp)** is a high-gain, DC-coupled, differential electronic voltage amplifier with two inputs (inverting and non-inverting) and a single-ended output. It is widely used in linear applications (amplification, filtering, mathematical operations) and non-linear applications (comparators, oscillators).

**Properties of an Ideal Op-Amp:**
1.  Infinite open-loop voltage gain ($A \rightarrow \infty$).
2.  Infinite input impedance ($Z_{in} \rightarrow \infty$) — it draws zero input current.
3.  Zero output impedance ($Z_{out} \rightarrow 0$) — it can drive any load.
4.  Infinite bandwidth ($BW \rightarrow \infty$) — it amplifies all frequencies equally.
5.  Infinite Common-Mode Rejection Ratio (CMRR $\rightarrow \infty$).
6.  Infinite Slew Rate ($SR \rightarrow \infty$) — output voltage can change instantaneously.
7.  Zero input offset voltage (output is $0\text{V}$ when inputs are shorted together).

---

**(b) Draw a voltage follower circuit. Mention its key practical applications. [04 Marks]**

**Answer:**
A voltage follower (or unity-gain buffer) is created by tying the output of an op-amp directly back to its inverting ($-$) input, while the signal is applied to the non-inverting ($+$) input.

*(Schematic Description: Op-amp symbol. Inverting input tied directly to Output with a wire. Input signal $V_{in}$ connected to Non-inverting input. $V_{out} = V_{in}$.)*

**Key Practical Applications:**
1.  **Impedance Matching / Buffering:** Because it has extremely high input impedance and extremely low output impedance, it isolates a high-impedance source from a low-impedance load, preventing signal loading (voltage drop).
2.  **Sensor Isolation:** Used between delicate sensors (like piezoelectric crystals or pH probes) and ADCs to prevent current draw from the sensor.
3.  **Active Filters:** Used to isolate cascading stages so that the reactive components of one filter stage do not load and alter the cutoff frequency of the previous stage.

---

**(c) Show that the output voltage of an op-amp differentiator is proportional to the rate of change of the input voltage. [04 Marks]**

**Answer:**
*(Schematic: An op-amp in an inverting configuration. A capacitor $C_1$ is connected between the input signal $V_i$ and the inverting terminal. A feedback resistor $R_f$ is connected between the output $V_o$ and the inverting terminal. The non-inverting terminal is grounded.)*

**Proof:**
1.  Assume an ideal op-amp. The non-inverting terminal is at ground ($0\text{V}$). Due to the virtual ground concept, the inverting terminal voltage is also $V_n \approx 0\text{V}$.
2.  Since the op-amp has infinite input impedance, no current flows into its inputs.
3.  Therefore, the current flowing through the input capacitor $C_1$ must exactly equal the current flowing through the feedback resistor $R_f$.
    $$i_C = i_R$$
4.  The current through a capacitor is proportional to the rate of change of the voltage across it:
    $$i_C = C_1 \frac{d}{dt} (V_i - V_n) = C_1 \frac{dV_i}{dt} \quad (\text{since } V_n = 0)$$
5.  The current through the feedback resistor is:
    $$i_R = \frac{V_n - V_o}{R_f} = -\frac{V_o}{R_f}$$
6.  Equating the two currents:
    $$C_1 \frac{dV_i}{dt} = -\frac{V_o}{R_f}$$
    $$V_o(t) = -R_f C_1 \frac{dV_i(t)}{dt}$$

This proves that the output voltage is directly proportional to the time derivative (rate of change) of the input voltage, scaled by the constant $-R_f C_1$.

---

### Q.6
**(a) Define the following op-amp non-idealities: (i) Input bias current, (ii) Input offset voltage, (iii) CMRR, and (iv) PSRR. [04 Marks]**

**Answer:**
*   **(i) Input bias current ($I_B$):** The extremely small, but non-zero, average DC current required by the base/gate of the internal input stage transistors of the op-amp to operate properly.
*   **(ii) Input offset voltage ($V_{OS}$):** The small DC differential voltage that must be applied between the two input terminals to force the output to exactly zero volts. It arises due to microscopic mismatches in the internal differential pair transistors.
*   **(iii) CMRR (Common-Mode Rejection Ratio):** The ratio of the differential gain to the common-mode gain ($CMRR = 20\log(A_d / A_{cm})$). It defines the op-amp's ability to reject noise signals that appear simultaneously and in-phase at both input terminals.
*   **(iv) PSRR (Power Supply Rejection Ratio):** A measure of the op-amp's ability to reject fluctuations or noise present on its power supply rails. It indicates how much the output voltage will change for a $1\text{V}$ change in the DC power supply.

---

**(b) Determine the maximum allowable peak input voltage and maximum frequency ($f_{max}$) for the inverting op-amp if $SR = 0.5\text{ V}/\mu\text{s}$. Input is $v_i(t) = 10\sin(2\pi f t)\text{ mV}$ peak. [05 Marks]**

**Solution:**
First, determine the closed-loop voltage gain ($A_{CL}$) of the inverting amplifier:
$$A_{CL} = -\frac{R_f}{R_1} = -\frac{100\text{ k}\Omega}{10\text{ k}\Omega} = -10$$

The output voltage $v_o(t)$ is:
$$v_o(t) = A_{CL} \times v_i(t) = -10 \times 10\sin(2\pi f t)\text{ mV} = -100\sin(2\pi f t)\text{ mV} = -0.1\sin(2\pi f t)\text{ V}$$
The peak output voltage is $V_{p(out)} = 0.1\text{ V}$.

The slew rate equation for a sinusoidal signal is:
$$SR \ge 2\pi f_{max} V_{p(out)}$$
Given $SR = 0.5\text{ V}/\mu\text{s} = 0.5 \times 10^6\text{ V/s}$:
$$0.5 \times 10^6 = 2\pi f_{max} (0.1)$$
$$f_{max} = \frac{0.5 \times 10^6}{2\pi \times 0.1} = \frac{5 \times 10^6}{2\pi} \approx 795,774\text{ Hz} \approx 795.8\text{ kHz}$$

For the maximum allowable peak input voltage across the entire operational bandwidth, without slew-rate distortion, the output peak voltage cannot exceed the saturation rails (typically $\pm 15\text{V}$ for standard op-amps). If limited by the rails, $V_{in(max)} = V_{sat} / |A_{CL}| \approx 15\text{V} / 10 = 1.5\text{V}$. However, for the specific $10\text{mV}$ signal, it can operate linearly up to $795.8\text{ kHz}$.

---

**(c) Draw neat schematics of pulse and triangular wave generator circuits using operational amplifiers. [03 Marks]**

**Answer:**
1.  **Triangular Wave Generator:** Constructed by cascading an astable Schmitt trigger (which generates a square wave) into an Op-Amp Integrator. The integrator ramps up when the square wave is positive and ramps down when it is negative, producing a perfect triangular wave.
2.  **Pulse Generator:** Created using an astable multivibrator op-amp circuit, but incorporating a diode in parallel with a variable resistor in the RC feedback loop. The diode allows the capacitor to charge quickly through a low resistance, but forces it to discharge slowly through a high resistance, creating an asymmetrical square wave (a narrow pulse).

---

### Q.7
**(a) Draw the functional block diagram of a 555 timer IC, and explain how it operates. [06 Marks]**

**Answer:**
*(Block Diagram Components: Three $5\text{k}\Omega$ resistors in series acting as a voltage divider from $V_{CC}$ to Ground. Two voltage comparators. An RS Flip-Flop. A discharge BJT transistor. An inverting output buffer.)*

**Operation:**
The internal voltage divider establishes reference voltages at $1/3 V_{CC}$ and $2/3 V_{CC}$.
1.  **Lower Comparator:** Compares the external Trigger (Pin 2) to $1/3 V_{CC}$. If Trigger falls below $1/3 V_{CC}$, it outputs HIGH, setting the RS Flip-Flop. This makes the main Output (Pin 3) go HIGH and turns OFF the discharge transistor.
2.  **Upper Comparator:** Compares the external Threshold (Pin 6) to $2/3 V_{CC}$. When the external capacitor voltage rises above $2/3 V_{CC}$, it outputs HIGH, resetting the RS Flip-Flop. This makes the main Output go LOW and turns ON the internal discharge transistor (Pin 7), which quickly drains the external capacitor to ground.
This simple, elegant interplay between charging/discharging and threshold comparisons allows the 555 to function as an oscillator (astable) or a one-shot timer (monostable).

---

**(b) Find the timing values ($t_H, t_L$) and design the resistor values ($R_A, R_B$) of the 555-timer astable multivibrator. $C = 0.01\ \mu\text{F}$, $t_H = 20\ \mu\text{s}$, $t_L = 10\ \mu\text{s}$. [06 Marks]**

**Solution:**
In a 555 astable multivibrator:
*   Time high ($t_H$) = $0.693 (R_A + R_B) C$
*   Time low ($t_L$) = $0.693 R_B C$

Given $t_L = 10\ \mu\text{s}$ and $C = 0.01\ \mu\text{F} = 10\text{ nF}$:
$$10 \times 10^{-6} = 0.693 \times R_B \times 0.01 \times 10^{-6}$$
$$R_B = \frac{10}{0.693 \times 0.01} = \frac{1000}{0.693} = 1443\ \Omega \approx 1.44\text{ k}\Omega$$

Given $t_H = 20\ \mu\text{s}$:
$$20 \times 10^{-6} = 0.693 (R_A + 1443) \times 0.01 \times 10^{-6}$$
$$\frac{20}{0.693 \times 0.01} = R_A + 1443$$
$$2886 = R_A + 1443$$
$$R_A = 2886 - 1443 = 1443\ \Omega \approx 1.44\text{ k}\Omega$$

**Design Values:**
$R_A = 1.44\text{ k}\Omega$, $R_B = 1.44\text{ k}\Omega$.

---

**(c) Draw the pin configuration diagram and internal block diagram of a 555 timer IC. [02 Marks]**

**Answer:**
**8-Pin DIP Configuration:**
*   Pin 1: Ground (GND)
*   Pin 2: Trigger (TRIG)
*   Pin 3: Output (OUT)
*   Pin 4: Reset (RST)
*   Pin 5: Control Voltage (CV)
*   Pin 6: Threshold (THR)
*   Pin 7: Discharge (DIS)
*   Pin 8: Power Supply ($V_{CC}$)

---

### Q.8
**(a) Why is op-amp frequency compensation required? Explain how internal phase compensation is achieved. [02 Marks]**

**Answer:**
Op-amp frequency compensation is required to prevent instability and unwanted high-frequency oscillations. Because an op-amp has multiple internal transistor stages, each stage introduces an RC pole, causing the phase shift to accumulate and potentially reach $-180^\circ$ at a frequency where the open-loop gain is still greater than 1. If negative feedback is applied under these conditions, the total loop phase becomes $360^\circ$ (positive feedback), satisfying Barkhausen criteria and turning the amplifier into an oscillator.
**Internal Phase Compensation** is achieved by placing a small internal capacitor (typically $\sim 30\text{ pF}$, like in the 741) across a high-gain internal stage (Miller compensation). This deliberately creates a dominant, low-frequency pole (e.g., at $10\text{ Hz}$) that rolls off the gain at $-20\text{ dB/decade}$ so that the gain crosses $0\text{ dB}$ (unity) long before the phase shift reaches $-180^\circ$, ensuring a stable phase margin.

---

**(b) Draw the frequency response curve for the active filter. Assume identical component values of $R = 10\text{ k}\Omega$ and $C = 0.1\ \mu\text{F}$. [06 Marks]**

**Solution:**
The provided schematic consists of a 2nd-order active Low-Pass Filter cascaded with a 1st-order active Low-Pass Filter, making it a **3rd-order active Low-Pass Filter**.
The cutoff frequency is identical for all RC sections:
$$f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi (10\text{ k}\Omega)(0.1\ \mu\text{F})} = 159.15\text{ Hz}$$
**Frequency Response Curve Description:**
*   **Passband:** The gain remains relatively flat (at $0\text{ dB}$, assuming unity gain configurations) from $0\text{ Hz}$ (DC) up to the cutoff frequency of $159\text{ Hz}$.
*   **Cutoff Point:** At $159.15\text{ Hz}$, the gain is down by $-3\text{ dB}$.
*   **Stopband:** Beyond $159\text{ Hz}$, the gain rolls off extremely steeply. Because it is a 3rd-order filter, the asymptotic roll-off slope is $-60\text{ dB/decade}$ (or $-18\text{ dB/octave}$).

---

**(c) Sketch the output voltage wave shape for the cascaded op-amp analog circuit. The inputs are $v_{s1} = 10\sin(\omega t - 30^\circ)\text{ V}$ and $v_{s2} = 10\sin(\omega t + 30^\circ)\text{ V}$. [04 Marks]**

**Solution:**
**Stage 1 Analysis:**
The first op-amp is an inverting amplifier with $R_{f1} = 100\text{ k}\Omega$ and $R_1 = 10\text{ k}\Omega$.
$$v_{o1} = -\left( \frac{R_{f1}}{R_1} \right) v_{s1} = -10 \times [10\sin(\omega t - 30^\circ)] = -100\sin(\omega t - 30^\circ)\text{ V}$$

**Stage 2 Analysis:**
The second op-amp is an inverting summing amplifier with inputs $v_{o1}$ and $v_{s2}$. $R_{f2} = 10\text{ k}\Omega$ and the input resistors $R$ are both $10\text{ k}\Omega$.
$$V_o = -\left[ \frac{R_{f2}}{R} v_{o1} + \frac{R_{f2}}{R} v_{s2} \right] = -\left[ 1 \times v_{o1} + 1 \times v_{s2} \right] = -(v_{o1} + v_{s2})$$

Substitute $v_{o1}$:
$$V_o = -(-100\sin(\omega t - 30^\circ) + 10\sin(\omega t + 30^\circ))$$
$$V_o = 100\sin(\omega t - 30^\circ) - 10\sin(\omega t + 30^\circ)\text{ V}$$

**Wave Shape Description:**
The output waveform is a summation of two sine waves of the same frequency but different phases and drastically different amplitudes. Because the $100\text{V}$ component dominates, the output wave shape will closely resemble a very large sine wave of $100\text{V}$ peak amplitude (shifted $-30^\circ$ in phase), with slight morphological distortion and a small phase shift introduced by subtracting the smaller $10\text{V}$ signal. (Note: In reality, an op-amp outputting $100\text{V}$ is impossible with standard $\pm 15\text{V}$ supplies, so a real circuit would heavily saturate into a square wave. Mathematically, it is the composite sine wave described above).
