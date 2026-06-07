[Previous](05_OpAmp_Applications.md) | [Home](index.md) | [Next](07_555_Timer.md)

# 📚 Topic 06: Oscillators
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Oscillator Fundamentals

### 1.1 The Barkhausen Criterion Derivation
*[Appeared in: 2019 Q8(b), 2018 Q8(a)]*

**Question:**
* **(a)** For any oscillator circuit, prove that the Barkhausen Criterion is given by $A\beta = 1\angle 0^\circ$. **[03 Marks]**

**Answer:**
An oscillator is a regenerative feedback system. It generates a continuous output waveform. It needs no external AC input signal.
```text
                  +----------------------------------------+
           0 o----|---(+)------------------[ A ]--------+---|---> Vo
                  |    |                                  |   |
                  |   (+) <----[ Beta ]<------------------+   |
                  +-------------------------------------------+
```

Applying positive feedback, the closed-loop transfer function is:
$$ A_f = \frac{A}{1 - A\beta} $$

For a self-sustained output ($V_o \ne 0$) with no external input ($V_i = 0$), the closed-loop gain $A_f$ must approach infinity:
$$ A_f \rightarrow \infty \Rightarrow 1 - A\beta = 0 \Rightarrow A\beta = 1 $$

$A$ (amplifier gain) and $\beta$ (feedback network gain) depend on frequency. This leads to the two conditions of the **Barkhausen Criterion**:
1.  **Amplitude Condition:** The loop gain magnitude must be exactly 1 to sustain constant-amplitude oscillations:
$$ |A\beta| = 1 $$
2.  **Phase Condition:** The total phase shift around the closed loop must be an integer multiple of $360^\circ$ ($0^\circ$). This ensures the feedback perfectly reinforces the output:
$$ \angle A + \angle \beta = 2n\pi, \quad n \in \{0, 1, 2, \dots\} $$

---

### 1.2 Frequency & Amplitude Stability
*[Appeared in: 2022 Q8(a), 2017 Q4(c)]*

**Question:**
* **(a)** Explain the engineering necessity of both frequency and amplitude stability in practical oscillator circuits. **[02 Marks, CO1]**

**Answer:**
*   **Amplitude Stability:** The initial loop gain $|A\beta|$ is slightly greater than $1$ to start oscillations. Without control, the amplitude grows until saturation. Stability mechanisms (like diodes or FETs) automatically reduce the gain $A$ as the signal grows. They settle the system at $|A\beta| = 1$ to prevent distortion.
*   **Frequency Stability:** The feedback network must have a steep phase curve. If components drift due to temperature, a steep curve ensures the frequency shifts very little to keep the total phase at $0^\circ$.

---

## 2. RC Phase-Shift Oscillators

### 2.1 Complete Frequency & Gain Derivation
*[Appeared in: 2024 Q8(b), 2023 Q4(a), 2020 Q5(b), 2018 Q8(b), 2018 Q5(c)]*

**Question:**
* **(a)** Show mathematically that for sustained oscillations in a 3-stage op-amp RC phase-shift oscillator, the gain of the inverting amplifier stage must satisfy $A_{CL} \ge 29$. **[04 Marks, CLO2]**

**Answer:**
The RC phase-shift oscillator uses an inverting amplifier (giving a $180^\circ$ phase shift). It also uses three high-pass RC sections in the feedback loop.
```text
                    R1          R2          R3
              +---[  ]----+---[  ]----+---[  ]----+
              |           |           |           |
        Vo o--+----[C1]---+----[C2]---+----[C3]---+---o Vf (to inverting input)
```

Applying nodal analysis to the three cascaded RC sections, the feedback transfer function is:
$$ \beta(s) = \frac{V_f(s)}{V_o(s)} = \frac{1}{1 - \frac{5}{\omega^2 R^2 C^2} - j \left( \frac{6}{\omega R C} - \frac{1}{\omega^3 R^3 C^3} \right)} $$

**Frequency of Oscillation ($f_o$):**
The feedback loop must provide the other $180^\circ$ phase shift. So the total loop phase is $360^\circ$. This means the imaginary term in the denominator must be zero:
$$ \frac{6}{\omega RC} - \frac{1}{\omega^3 R^3 C^3} = 0 \Rightarrow 6 = \frac{1}{\omega^2 R^2 C^2} $$
$$ \omega^2 = \frac{1}{6 R^2 C^2} \Rightarrow \omega = \frac{1}{\sqrt{6} RC} $$
Since $\omega = 2\pi f_o$:
$$ f_o = \frac{1}{2\pi \sqrt{6} RC} $$

**Gain Condition ($A_{CL} \ge 29$):**
Substitute $\frac{1}{\omega^2 R^2 C^2} = 6$ back into the real part of the transfer function to find the feedback attenuation factor at resonance:
$$ \beta = \frac{1}{1 - 5(6)} = -\frac{1}{29} $$
To satisfy the Barkhausen amplitude criterion $|A\beta| \ge 1$:
$$ |A| \left( \frac{1}{29} \right) \ge 1 \Rightarrow |A| \ge 29 $$
The inverting amplifier must provide a voltage gain of at least $29$ to sustain oscillations.

---

### 2.2 Worked RC Phase-Shift Design
*[Appeared in: 2019 Q8(c)]*

**Question:**
* **(c)** Design the op-amp based 3-stage RC phase-shift oscillator shown in Figure 8(c) to operate at a frequency of $f_o = 400\text{ Hz}$. Find the values of $R$, $C$, $R_1$, and $R_F$. **[04 Marks]**

**Answer:**
**Step 1: Select a practical capacitor value**
Let $C = 0.1\ \mu\text{F} = 10^{-7}\text{ F}$.

**Step 2: Calculate the required phase-shift resistor ($R$)**
$$ f_o = \frac{1}{2\pi \sqrt{6} RC} \Rightarrow R = \frac{1}{2\pi \sqrt{6} f_o C} $$
$$ R = \frac{1}{2\pi \sqrt{6} (400) (10^{-7})} = \frac{1}{2\pi \times 2.449 \times 400 \times 10^{-7}} \approx 1624.7\ \Omega $$
Use a standard resistor value: $R \approx 1.62\text{ k}\Omega$.

**Step 3: Determine the amplifier feedback resistors ($R_1$ and $R_F$)**
To prevent loading effects and match the phase-shift network, the input resistor of the inverting amplifier should be:
$$ R_1 = R = 1.62\text{ k}\Omega $$
To satisfy the gain condition $|A| \ge 29$:
$$ \frac{R_F}{R_1} \ge 29 \Rightarrow R_F \ge 29 \times 1.62\text{ k}\Omega = 46.98\text{ k}\Omega $$
Select $R_F = 47\text{ k}\Omega$ (standard value) to ensure oscillations start.

---

## 3. Wien Bridge Oscillators

### 3.1 Wien Selective Bridge Analysis
*[Appeared in: 2018 Q5(a)]*

**Question:**
* **(a)** Calculate the resonant oscillation frequency ($f_o$) of the active Wien-bridge bandpass/oscillator network shown below. **[04 Marks]**

**Answer:**
The non-inverting input path of a Wien Bridge oscillator contains a series RC branch and a parallel RC branch, forming a lead-lag bandpass network. The feedback factor is:
$$ \beta(s) = \frac{Z_p}{Z_s + Z_p} = \frac{\frac{R}{1 + sRC}}{R + \frac{1}{sC} + \frac{R}{1 + sRC}} $$
Substituting $s = j\omega$ and simplifying yields:
$$ \beta = \frac{1}{3 + j \left( \omega RC - \frac{1}{\omega RC} \right)} $$

**Phase Condition ($0^\circ$):**
The non-inverting amplifier provides $0^\circ$ phase shift. Therefore, the feedback network must also provide exactly $0^\circ$ phase shift. This occurs when the imaginary term is zero:
$$ \omega RC - \frac{1}{\omega RC} = 0 \Rightarrow \omega = \frac{1}{RC} \Rightarrow f_o = \frac{1}{2\pi RC} $$

**Amplitude Condition:**
At resonance, the imaginary term disappears, and the feedback fraction is exactly:
$$ \beta = \frac{1}{3} $$
Therefore, the non-inverting amplifier must provide a closed-loop gain of:
$$ A_{CL} = 1 + \frac{R_F}{R_1} \ge 3 \Rightarrow \frac{R_F}{R_1} \ge 2 \Rightarrow R_F \ge 2 R_1 $$

---

### 3.2 Worked Wien Bridge Design
*[Appeared in: 2024 Q8(a), 2021 Q5(c)]*

**Question:**
* **(a)** Design an active op-amp based Wien bridge oscillator circuit to generate sustained sinusoidal oscillations at a frequency of $f_o = 20\text{ kHz}$. **[03 Marks, CO1]**

**Answer:**
**Step 1: Select a practical capacitor value**
Let $C = 1\text{ nF} = 10^{-9}\text{ F}$.

**Step 2: Calculate the required frequency-determining resistor ($R$)**
$$ R = \frac{1}{2\pi f_o C} = \frac{1}{2\pi (20,000\text{ Hz}) (10^{-9}\text{ F})} = \frac{1}{2\pi \times 2 \times 10^{-5}} \approx 7957.7\ \Omega $$
Use a standard resistor value: $R = 8.2\text{ k}\Omega$ (or a $10\text{k}\Omega$ potentiometer tuned to $7.96\text{ k}\Omega$).

**Step 3: Determine the amplifier gain resistors ($R_1$ and $R_F$)**
For sustained oscillation, the non-inverting gain must satisfy $A_v \ge 3$, so $R_F \ge 2 R_1$.
Let $R_1 = 10\text{ k}\Omega$.
$$ R_F \ge 2 \times 10\text{ k}\Omega = 20\text{ k}\Omega $$
Select $R_F = 22\text{ k}\Omega$ to guarantee oscillations begin.

---

## 4. Quadrature Oscillator
*[Appeared in: 2022 Q8(b)]*

**Question:**
* **(b)** Draw the circuit diagram and explain the operating principles of an active Quadrature Oscillator. **[04 Marks, CO2]**

**Answer:**
**Circuit Diagram:**
A quadrature oscillator consists of an active inverting integrator cascaded with a non-inverting integrator, placed in a positive feedback loop.
```text
           C                     C
       +--||--+              +--||--+
       |      |              |      |
       |    |\      Sine     |    |\      Cosine
  +----|----| \      Out     |    | \      Out
  |    |    |  >------o------|----|+ \
  |  +-|----|+/              |    |   >-----o
  |  | |    |/               +----|- /      |
  |  | |      Inverting      |    |/        |
  |  | [ ]R   Integrator    [ ]R Non-Inv.   |
  |  |  |                    |   Integrator |
  |  +--+--------------------+              |
  |                                         |
  +-----------------------------------------+
```

**Operating Principles:**
1.  **Dual Outputs:** The circuit generates two sinusoidal outputs at the same time. They are $90^\circ$ out of phase with each other (in quadrature). These are a Sine wave and a Cosine wave.
2.  **Phase Shift:** 
    *   The inverting integrator stage provides a $-90^\circ$ phase shift (integration) plus a $180^\circ$ phase shift (inversion), totaling $90^\circ$.
    *   The non-inverting integrator stage provides exactly $-90^\circ$ phase shift (integration).
    *   Total loop phase shift = $90^\circ - 90^\circ = 0^\circ$, satisfying the Barkhausen phase criterion.
3.  **Frequency of Oscillation:** Set by the identical RC time constants of both integrators:
$$ f_o = \frac{1}{2\pi RC} $$

---

## 5. LC Oscillators (Colpitts & Clapp)

### 5.1 Colpitts Oscillator Derivation
*[Appeared in: 2019 Q6(a), 2018 Q5(b)]*

**Question:**
* **(a)** For a Colpitts oscillator, prove that the frequency of oscillation is given by:
$$ f_o = \frac{1}{2\pi} \sqrt{\frac{C_1+C_2}{L C_1 C_2}} $$

**Answer:**
The Colpitts oscillator uses a parallel resonant tank circuit for feedback. It has one inductor $L$ in parallel with two series capacitors $C_1$ and $C_2$. The feedback connects between the two capacitors.
For oscillations to exist, the total loop reactance around the closed LC tank loop must sum to zero at the resonant frequency:
$$ X_L + X_{C1} + X_{C2} = 0 $$
Substitute the dynamic reactive impedances:
$$ j\omega L + \frac{1}{j\omega C_1} + \frac{1}{j\omega C_2} = 0 $$
Multiply the equation by $-j$ (recall that $1/j = -j$):
$$ \omega L - \frac{1}{\omega C_1} - \frac{1}{\omega C_2} = 0 $$
$$ \omega L = \frac{1}{\omega} \left( \frac{1}{C_1} + \frac{1}{C_2} \right) $$
Multiply by $\omega$:
$$ \omega^2 L = \frac{C_1 + C_2}{C_1 C_2} $$
$$ \omega^2 = \frac{1}{L} \left( \frac{C_1 + C_2}{C_1 C_2} \right) $$
Taking the square root and substituting $\omega = 2\pi f_o$:
$$ 2\pi f_o = \frac{1}{\sqrt{L \left( \frac{C_1 C_2}{C_1 + C_2} \right)}} \Rightarrow f_o = \frac{1}{2\pi} \sqrt{\frac{C_1+C_2}{L C_1 C_2}} $$

---

### 5.2 Clapp JFET Oscillator Numerical Analysis
*[Appeared in: 2017 Q4(b)]*

**Question:**
* **(b)** Calculate (i) Oscillation frequency ($f_o$), (ii) Feedback factor ($\beta$), and (iii) Voltage gain ($A_v$) for the Clapp JFET oscillator network shown below. **[05 Marks]**

**Circuit Parameters Provided:**
*   Series tank inductors: $L_1 = 30\ \mu\text{H}$ and $L_2 = 10\ \mu\text{H}$
*   Series tank capacitors: $C_1 = 0.01\ \mu\text{F}$ and $C_2 = 0.01\ \mu\text{F}$
*   *(Note: The Clapp adds an extra series capacitor to the tank to improve stability, but based on the provided parameter groupings, we treat the equivalent branch reactances.)*

**Answer:**
**Step 1: Calculate equivalent tank inductance ($L_{eq}$)**
$$ L_{eq} = L_1 + L_2 = 30\ \mu\text{H} + 10\ \mu\text{H} = 40\ \mu\text{H} $$

**Step 2: Calculate equivalent series capacitance ($C_{eq}$)**
$$ C_{eq} = \frac{C_1 C_2}{C_1 + C_2} = \frac{0.01\ \mu\text{F} \times 0.01\ \mu\text{F}}{0.01\ \mu\text{F} + 0.01\ \mu\text{F}} = 0.005\ \mu\text{F} = 5\text{ nF} $$

**Step 3: Calculate the resonant frequency ($f_o$)**
$$ f_o = \frac{1}{2\pi \sqrt{L_{eq} C_{eq}}} = \frac{1}{2\pi \sqrt{(40 \times 10^{-6}\text{ H}) (5 \times 10^{-9}\text{ F})}} = \frac{1}{2\pi \sqrt{2 \times 10^{-13}}} $$
$$ f_o = \frac{1}{2\pi \times (4.472 \times 10^{-7})} \approx 355.88\text{ kHz} $$

**Step 4: Calculate the feedback factor ($\beta$)**
In a Colpitts/Clapp configuration, the feedback fraction is set by the ratio of the two tapping capacitors:
$$ \beta = \frac{C_1}{C_2} = \frac{0.01\ \mu\text{F}}{0.01\ \mu\text{F}} = 1 $$

**Step 5: Determine required voltage gain ($A_v$)**
To satisfy the Barkhausen criterion $|A_v \beta| \ge 1$:
$$ A_v \ge \frac{1}{\beta} = 1 $$

---

## 6. Crystal Oscillators
*[Appeared in: 2020 Q5(d)]*

**Question:**
* **(d)** Write a short note on the operation and frequency stability of crystal oscillators. **[02 Marks]**

**Answer:**
**Operation:**
**Operation:**
Crystal oscillators use the **piezoelectric effect** of a quartz crystal. Mechanical pressure generates a voltage. And an AC voltage makes it vibrate at a stable resonant frequency. The electrical circuit is a series resonant LC branch in parallel with a parasitic capacitance ($C_p$).

**Frequency Stability:**
Quartz crystals have a very high **Q-Factor** ($10,000$ to $100,000+$). Standard LC tanks only have about $100$. The equivalent inductance $L$ is huge and resistance $R$ is tiny. So the crystal only oscillates over a very narrow frequency range. This makes them immune to temperature changes, aging, or supply drifts. It guarantees great frequency stability.

[Previous](05_OpAmp_Applications.md) | [Home](index.md) | [Next](07_555_Timer.md)
