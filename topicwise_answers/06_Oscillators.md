[Previous](05_OpAmp_Applications.md) | [Home](index.md) | [Next](07_555_Timer.md)

# 📚 Topic 06: Oscillators
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Oscillator Fundamentals

### 1.1 The Barkhausen Criterion Derivation
*[Appeared in: 2024 Q8(b), 2021 Q4(a), 2019 Q8(b), 2018 Q8(a)]*

**Question:**
* **(b)** Draw the circuit diagram of an op-amp based RC phase-shift oscillator and explain its operation. **[04 Marks, CO1]**

An oscillator is a regenerative feedback system that generates a continuous output waveform without requiring an external AC input signal.

```
                  +----------------------------------------+
           0 o----|---(+)------------------[ A ]--------+---|---> Vo
                  |    |                                  |   |
                  |   (+) <----[ Beta ]<------------------+   |
                  +-------------------------------------------+
```

Applying positive feedback, the closed-loop transfer function is:

$$
A_f = \frac{A}{1 - A\beta}
$$

For a self-sustained output to exist ($V_o \ne 0$) when the external input is zero ($V_i = 0$), the closed-loop gain $A_f$ must approach infinity:

$$
A_f \rightarrow \infty \Rightarrow 1 - A\beta = 0 \Rightarrow A\beta = 1\angle 0^\circ
$$

Since $A$ and $\beta$ are complex quantities:
1.  **Amplitude Condition:** The loop gain magnitude must be unity:

$$
|A\beta| = 1
$$

2.  **Phase Condition:** The total phase shift around the closed loop must be an integer multiple of $360^\circ$ (or $0^\circ$):

$$
\angle A + \angle \beta = 2n\pi, \quad n \in \{0, 1, 2, \dots\}
$$

---

### 1.2 Frequency & Amplitude Stability
*[Appeared in: 2022 Q8(a), 2017 Q4(c), 2023 Q4(c)]*

**Question:**
* **(a)** Explain the engineering necessity of both frequency and amplitude stability in practical oscillator circuits. **[02 Marks, CO1]**

*   **Gain Condition:** For oscillations to start, the loop gain $|A\beta|$ is designed to be slightly greater than $1$. As oscillations build, active device non-linearities reduce the amplifier gain $A$ until the system settles into a stable steady-state at $|A\beta| = 1$.
*   **Frequency Stability Condition:** The frequency-selective feedback network must have a steep phase-vs-frequency response curve ($d\phi/d\omega$). If internal components shift due to temperature or supply fluctuations, a steep phase curve ensures the system only shifts frequency minimally to maintain the $0^\circ$ phase criterion.

---

## 2. RC Phase-Shift Oscillators
*[Appeared in: 2021 Q4(b), 2019 Q8(c), 2018 Q5(c)]*

**Question:**
* **(b)** Formulate the equations to determine the charging and discharging time periods of the timing capacitor in a 555-timer astable multivibrator. **[04 Marks, CLO2]**

### 2.1 Complete Frequency & Gain Derivation
The RC phase-shift oscillator uses an inverting amplifier (gain $A$, contributing $180^\circ$ phase shift) and three identical high-pass RC sections in the feedback loop.

```
                    R1          R2          R3
              +---[  ]----+---[  ]----+---[  ]----+
              |           |           |           |
        Vo o--+----[C1]---+----[C2]---+----[C3]---+---o Vf (to inverting input)
```

Applying nodal analysis to the three RC sections:

$$
\beta(s) = \frac{V_f(s)}{V_o(s)} = \frac{1}{1 - \frac{5}{\omega^2 R^2 C^2} - j \left( \frac{6}{\omega R C} - \frac{1}{\omega^3 R^3 C^3} \right)}
$$

For the loop phase shift to be exactly $180^\circ$ (so the total loop phase is $180^\circ + 180^\circ = 360^\circ$), the imaginary term in the denominator must equal zero:

$$
\frac{6}{\omega RC} - \frac{1}{\omega^3 R^3 C^3} = 0 \Rightarrow 6 = \frac{1}{\omega^2 R^2 C^2}
$$

$$
\omega^2 = \frac{1}{6 R^2 C^2} \Rightarrow \omega = \frac{1}{\sqrt{6} RC}
$$

Since $\omega = 2\pi f_o$, the resonant frequency of oscillation is:

$$
f_o = \frac{1}{2\pi \sqrt{6} RC}
$$

Substitute $\omega^2 R^2 C^2 = 1/6$ back into the real part of the transfer function to find the feedback attenuation at resonance:

$$
\beta = \frac{1}{1 - 5(6)} = -\frac{1}{29}
$$

To satisfy $|A\beta| = 1$:

$$
|A| \ge 29
$$

The amplifier must provide an inverting gain of at least $29$ to sustain oscillations.

---

### 2.2 Worked RC Phase-Shift Design
*[Appeared in: 2019 Q8(c)]*

**Question:**
* **(c)** Design the op-amp based 3-stage RC phase-shift oscillator shown in Figure 8(c) to operate at a frequency of $f_o = 400\text{ Hz}$. Find the values of $R$, $C$, $R_1$, and $R_F$. **[04 Marks]**

##### Figure 8(c) Circuit Diagram:
```
                     R_1             R_F
                 +---[ ]---+----+---[ ]---+
                 |         |    |         |
                ---       -|    |         |
            R_OM| |      |  \   |         |
                ---      | A >--+---------+
                 |       |  /             |
                ===      |+/              |
                GND                       |
                 |                        |
                 +----||----+----||---+---||---+
                 |    C     |    C    |   C    |
                 |         [ ]        [ ]      [ ]
                 |          R          R        R
                 |          |          |        |
                 +----------+----------+--------+
                                       |
                                      ===
                                      GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Feedback Phase-Shift Loop:** Three identical high-pass $R-C$ stages connected in series. Each stage introduces a $60^\circ$ phase shift at the oscillation frequency $f_o = 400\text{ Hz}$.
2. **Frequency Formula:**

$$
f_o = \frac{1}{2\pi \sqrt{6} R C}
$$

3. **Amplifier Stage:**
   * Inverting amplifier with gain:

$$
A_{CL} = -\frac{R_F}{R_1} = -29
$$

   * For matching phase-shift loading: $R_1 = R$.

[Previous](2018.md) | [Home](index.md) | [Next](2020.md)

**Problem Details:**
Design an op-amp based 3-stage RC phase-shift oscillator to operate at a resonant frequency of $f_o = 400\text{ Hz}$.

#### Step-by-Step Solution:

##### Step 1: Select a practical capacitor value
Let $C = 0.1\ \mu\text{F} = 10^{-7}\text{ F}$.

##### Step 2: Calculate the required resistor value ($R$)

$$
f_o = \frac{1}{2\pi \sqrt{6} RC} \Rightarrow R = \frac{1}{2\pi \sqrt{6} f_o C}
$$

$$
R = \frac{1}{2\pi \sqrt{6} (400\text{ Hz}) (10^{-7}\text{ F})} = \frac{1}{2\pi \times 2.449 \times 4 \times 10^{-5}} \approx 1624.7\ \Omega
$$

Use standard resistor value: $R = 1.62\text{ k}\Omega$.

##### Step 3: Determine the amplifier feedback resistors
The input resistor of the inverting amplifier must match $R$ to maintain the network loading:

$$
R_1 = R = 1.62\text{ k}\Omega
$$

To satisfy the gain condition $A \ge 29$:

$$
R_F \ge 29 \times R_1 = 29 \times 1.62\text{ k}\Omega \approx 47\text{ k}\Omega
$$

---

## 3. Wien Bridge Oscillators

### 3.1 Wien selective bridge analysis
*[Appeared in: 2020 Q5(a), 2020 Q5(c)]*

**Question:**
* **(a)** Define regenerative (positive) and degenerative (negative) feedback configurations. **[02 Marks]**

The non-inverting input path of the Wien Bridge oscillator contains a series RC branch and a parallel RC branch:

$$
\beta(s) = \frac{Z_p}{Z_s + Z_p} = \frac{\frac{R}{1 + sRC}}{R + \frac{1}{sC} + \frac{R}{1 + sRC}} = \frac{R}{R(1+sRC) + \frac{1+sRC}{sC} + R}
$$

Substituting $s = j\omega$ and using identical $R$ and $C$ values:

$$
\beta = \frac{1}{3 + j \left( \omega RC - \frac{1}{\omega RC} \right)}
$$

For a phase shift of exactly $0^\circ$, the imaginary term must equal zero:

$$
\omega RC - \frac{1}{\omega RC} = 0 \Rightarrow \omega = \frac{1}{RC} \Rightarrow f_o = \frac{1}{2\pi RC}
$$

At resonance, the feedback fraction is:

$$
\beta = \frac{1}{3}
$$

Therefore, the non-inverting amplifier must provide a closed-loop gain of:

$$
A_{CL} = 1 + \frac{R_F}{R_1} \ge 3 \Rightarrow R_F \ge 2 R_1
$$

---

### 3.2 Worked Wien Bridge Design
*[Appeared in: 2018 Q8(c), 2020 Q5(c)]*

**Question:**
* **(c)** Design an op-amp based Wien bridge oscillator to operate at a frequency of $f_o = 10\text{ kHz}$. **[04 Marks]**

[Previous](2017.md) | [Home](index.md) | [Next](2019.md)

**Problem Details:**
Design an op-amp based Wien bridge oscillator to operate at a frequency of $f_o = 10\text{ kHz}$.

#### Step-by-Step Solution:

##### Step 1: Select a practical capacitor value
Let $C = 10\text{ nF} = 0.01\ \mu\text{F}$.

##### Step 2: Calculate the required resistor value ($R$)

$$
R = \frac{1}{2\pi f_o C} = \frac{1}{2\pi (10,000\text{ Hz}) (10 \times 10^{-9}\text{ F})} = \frac{1}{2\pi \times 10^{-4}} \approx 1591.5\ \Omega
$$

Use standard resistor value: $R = 1.6\text{ k}\Omega$.

##### Step 3: Determine the amplifier feedback resistors
For sustained oscillation, we need $R_F \ge 2 R_1$.
Let $R_1 = 10\text{ k}\Omega$:

$$
R_F = 2 \times 10\text{ k}\Omega = 20\text{ k}\Omega
$$

To guarantee oscillations start, we can select a slightly larger standard value: $R_F = 22\text{ k}\Omega$.

---

## 4. Colpitts Oscillator Derivation
*[Appeared in: 2021 Q4(a), 2019 Q6(a), 2018 Q5(b), CT4 Q2]*

**Question:**
* **(a)** Differentiate between active and passive filters. Mention the electrical characteristics of a Sallen-Key active Butterworth low-pass filter. **[04 Marks, CLO1]**

The Colpitts oscillator employs an inductive/capacitive parallel LC tank in its feedback path:

```
                         L
               +-------[   ]-------+
               |                   |
        Vo o---+----[ C1 ]----+----+---o Vf
                              |
                             Gnd
```

**Proof of Colpitts Resonant Frequency:**
For oscillations to exist, the loop reactances around the closed LC tank loop must sum to zero at the resonant frequency:

$$
X_L + X_{C1} + X_{C2} = 0
$$

Substitute the dynamic reactive impedances:

$$
j\omega L + \frac{1}{j\omega C_1} + \frac{1}{j\omega C_2} = 0
$$

Multiply by $-j$ (recall that $1/j = -j$):

$$
\omega L - \frac{1}{\omega C_1} - \frac{1}{\omega C_2} = 0 \Rightarrow \omega L = \frac{1}{\omega} \left( \frac{1}{C_1} + \frac{1}{C_2} \right)
$$

Multiply by $\omega$:

$$
\omega^2 L = \frac{C_1 + C_2}{C_1 C_2} \Rightarrow \omega^2 = \frac{1}{L} \left( \frac{C_1 + C_2}{C_1 C_2} \right) = \frac{1}{L C_{eq}}
$$

where the equivalent series capacitance is $C_{eq} = \frac{C_1 C_2}{C_1 + C_2}$.

$$
\omega = \frac{1}{\sqrt{L C_{eq}}} \Rightarrow f_o = \frac{1}{2\pi \sqrt{L \left( \frac{C_1 C_2}{C_1 + C_2} \right)}}
$$

---

## 5. Hartley & Clapp Oscillators

### 5.1 Clapp JFET Oscillator Numerical Analysis
*[Appeared in: 2017 Q4(b)]*

**Question:**
* **(b)** Calculate (i) Oscillation frequency ($f_o$), (ii) Feedback factor ($\beta$), and (iii) Voltage gain ($A_v$) for the Clapp JFET oscillator network shown below. **[05 Marks]**

##### Circuit Diagram (Q.4(b)):
```
                        +15 V_DC
                           |
                          [ ] RFC (Radio Frequency Choke)
                           |
                  +---------+----------+--||----+--> Vout
                  |         |          |  Co   |
                  |       D |          |0.001u[ ] RL = 1k
                  |       +-+-+        |       |
         +--||----+--||---| J1|        |      GND
         |  C1    |  C3   +-+-+        |
         | 0.01u  | 0.01u   | S        |
         |        |        GND         |
       +-+--------+--------------------+
       |  |                            |
       | [ ] Rg = 10M                  |
       |  |                            |
       | GND                           |
       |                               |
       +-----+-------------------+-----+
       |     |                   |     |
      ---   ---                 ( )   ( )
     C| |  C| |                L1| | L2| |
  0.01u   0.01u               30u |   10u |
       |     |                   |     |
       +--+--+                   +--+--+
          |                         |
         GND                       GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Resonant Network Topology:** The resonant circuit uses two parallel branches connected between JFET gate and drain loops:
   * Branch 1: Two capacitors ($C = 0.01\ \mu\text{F}$ and $C = 0.01\ \mu\text{F}$) connected in series to Ground.
   * Branch 2: Two inductors ($L_1 = 30\ \mu\text{H}$ and $L_2 = 10\ \mu\text{H}$) connected in series to Ground.
2. **Frequency of Resonant Tank:**

$$
L_{eq} = L_1 + L_2 = 30\ \mu\text{H} + 10\ \mu\text{H} = 40\ \mu\text{H}
$$

$$
C_{eq} = \frac{C \cdot C}{C + C} = 0.005\ \mu\text{F}
$$

$$
f_o = \frac{1}{2\pi \sqrt{L_{eq} C_{eq}}}
$$

**Problem Details:**
A Clapp JFET oscillator has series tank inductors $L_1 = 30\ \mu\text{H}$ and $L_2 = 10\ \mu\text{H}$ in series, and series capacitors $C_1 = 0.01\ \mu\text{F}$ and $C_2 = 0.01\ \mu\text{F}$ in series. Calculate (i) resonant frequency $f_o$, (ii) feedback factor $\beta$, and (iii) minimum required voltage gain $A_v$.

#### Step-by-Step Solution:

##### Step 1: Calculate equivalent tank inductance ($L_{eq}$)

$$
L_{eq} = L_1 + L_2 = 30\ \mu\text{H} + 10\ \mu\text{H} = 40\ \mu\text{H}
$$

##### Step 2: Calculate equivalent series capacitance ($C_{eq}$)

$$
C_{eq} = \frac{C_1 C_2}{C_1 + C_2} = \frac{0.01\ \mu\text{F} \times 0.01\ \mu\text{F}}{0.01\ \mu\text{F} + 0.01\ \mu\text{F}} = 0.005\ \mu\text{F} = 5\text{ nF}
$$

##### Step 3: Calculate the resonant frequency ($f_o$)

$$
f_o = \frac{1}{2\pi \sqrt{L_{eq} C_{eq}}} = \frac{1}{2\pi \sqrt{(40 \times 10^{-6}\text{ H}) (5 \times 10^{-9}\text{ F})}} = \frac{1}{2\pi \sqrt{2 \times 10^{-13}}}
$$

$$
f_o = \frac{1}{2\pi \times (4.472 \times 10^{-7})} \approx 355.88\text{ kHz}
$$

##### Step 4: Calculate the feedback factor ($\beta$)

$$
\beta = \frac{C_1}{C_2} = \frac{0.01\ \mu\text{F}}{0.01\ \mu\text{F}} = 1
$$

##### Step 5: Determine required voltage gain ($A_v$)
To satisfy the Barkhausen criterion $|A_v \beta| \ge 1$:

$$
A_v \ge \frac{1}{\beta} = 1
$$

---

## 6. Crystal Oscillators
*[Appeared in: 2020 Q5(d)]*

**Question:**
* **(d)** Write a short note on the operation and frequency stability of crystal oscillators. **[02 Marks]**

### 6.1 Equivalent Circuit and Piezoelectric Effect
Crystal oscillators exploit the **piezoelectric effect** of a quartz crystal: when mechanical pressure is applied, it generates a voltage across its faces; conversely, when an AC voltage is applied, it vibrates mechanically at a highly stable natural resonant frequency.

```
                L       C       R
        o-----[   ]---[   ]---[   ]-----o (Series Branch)
          |                           |
          +----------[ Cp ]-----------+ (Parallel Branch)
```

The electrical equivalent circuit consists of:
1.  **Series Resonant Branch ($L, C, R$):** Represents the physical crystal's mass ($L$), compliance ($C$), and internal mechanical friction ($R$).
2.  **Parallel Branch ($C_p$):** Represents the electrostatic capacitance between the physical metal mounting plates.

### 6.2 Series vs. Parallel Resonance
The crystal has two distinct resonant frequencies:
1.  **Series Resonant Frequency ($f_s$):** The series LC branch impedance falls to its minimum ($R$):

$$
f_s = \frac{1}{2\pi \sqrt{L C}}
$$

2.  **Parallel (Antiresonant) Frequency ($f_p$):** The series branch becomes inductive and resonates with the parallel plate capacitance $C_p$, creating a maximum impedance point:

$$
f_p = \frac{1}{2\pi \sqrt{L C_{eq}}} \quad \text{where} \quad C_{eq} = \frac{C \cdot C_p}{C + C_p}
$$

Since $C_p \gg C$, $f_p$ is situated extremely close to $f_s$ (typically within $1\text{ kHz}$).

### 6.3 Supreme Stability & Q-Factor
Quartz crystal oscillators possess an exceptionally high **Q-Factor** (Quality Factor), typically in the range of $10,000$ to $100,000+$, compared to $\sim 100$ for standard LC tank circuits. This massive Q-factor is mathematically given by:

$$
Q = \frac{\omega_0 L}{R}
$$

Because the equivalent inductance $L$ of the crystal is extremely large (often in Henries) and $R$ is tiny, the crystal only oscillates over a highly narrow phase-locked frequency range, making it practically immune to temperature changes, aging, or supply voltage drifts.

[Previous](05_OpAmp_Applications.md) | [Home](index.md) | [Next](07_555_Timer.md)
