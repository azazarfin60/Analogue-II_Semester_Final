# 📚 Topic 04: OpAmp Fundamentals
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Ideal vs. Practical Op-Amps

### 1.1 Properties Comparison
*[Appeared in: 2024 Q5(a), 2022 Q5(a), 2017 Q5(a)]*

| Parameter | Ideal Op-Amp | Practical Op-Amp (e.g., $\mu\text{A}741$) | Physical Significance |
|:---|:---:|:---:|:---|
| **Open-Loop Gain ($A_{OL}$)** | $\infty$ | $\sim 2 \times 10^5$ ($106\text{ dB}$) | Amplifies differential inputs to massive outputs. |
| **Input Impedance ($Z_i$)** | $\infty$ | $\sim 2\text{ M}\Omega$ (BJT) / $>10^{12}\ \Omega$ (FET) | Draws zero current from input signal sources. |
| **Output Impedance ($Z_o$)** | $0$ | $\sim 75\ \Omega$ | Can drive any load impedance without signal sag. |
| **Bandwidth ($BW$)** | $\infty$ | $\sim 1\text{ MHz}$ (Unity Gain) | Amplifies all signals from DC to high frequency. |
| **Common-Mode Rejection ($CMRR$)**| $\infty$ | $\sim 90\text{ dB}$ | Rejects common-mode noise and interference. |
| **Slew Rate ($SR$)** | $\infty$ | $\sim 0.5\text{ V}/\mu\text{s}$ | Output can track instantaneous input transitions. |
| **Input Offset Voltage ($V_{OS}$)** | $0$ | $\sim 1\text{ mV}$ to $5\text{ mV}$ | Output is $0\text{V}$ when input differential is $0\text{V}$. |

---

### 1.2 The Virtual Ground Concept
*[Appeared in: 2022 Q5(b)]*

For an operational amplifier operating with negative feedback:
1.  The open-loop gain $A_{OL}$ is extremely high ($>10^5$).
2.  The output voltage is limited by the power supply rails ($V_{sat} \approx \pm 14\text{ V}$).
3.  The differential input voltage $V_d = V_+ - V_-$ is related to the output by:
    $$V_o = A_{OL} (V_+ - V_-) \Rightarrow V_+ - V_- = \frac{V_o}{A_{OL}}$$
4.  Since $A_{OL} \rightarrow \infty$, the differential input voltage must approach zero:
    $$V_+ - V_- \approx 0 \Rightarrow V_- \approx V_+$$
This is the **Virtual Short** principle. If the non-inverting terminal ($V_+$) is connected physically to Ground ($0\text{V}$), the inverting terminal ($V_-$) is held at a potential of exactly $0\text{V}$, functioning as a **Virtual Ground**. It can sink or source current but cannot maintain any voltage relative to ground.

---

### 1.3 Closed-Loop Gain Derivation (Non-Inverting)
*[Appeared in: 2023 Q6(a)]*

```
                         Rf
                   +---[ R2 ]---+
                   |            |
        Vin o---(+)----[ Av ]---+---o Vout
                   |
        Gnd o---[ R1 ]---o (-)
```

1.  Assume an ideal op-amp. The input current into the inverting terminal is $I_- \approx 0$.
2.  By the virtual short principle, the voltage at the inverting terminal tracks the input voltage:
    $$V_- = V_+ = V_{in}$$
3.  Apply KCL at the inverting terminal node:
    $$\frac{0 - V_-}{R_1} + \frac{V_{out} - V_-}{R_f} = 0 \Rightarrow -\frac{V_{in}}{R_1} + \frac{V_{out} - V_{in}}{R_f} = 0$$
    $$\frac{V_{out}}{R_f} = V_{in} \left( \frac{1}{R_1} + \frac{1}{R_f} \right) \Rightarrow V_{out} = V_{in} \left( \frac{R_f}{R_1} + 1 \right)$$
    $$A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_1}$$

---

## 2. Op-Amp Non-Idealities & Parameters

### 2.1 Standard Parameter Definitions
*[Appeared in: 2024 Q5(a), 2022 Q5(a), 2017 Q6(a)]*

*   **Input Bias Current ($I_B$):** The average of the DC currents flowing into the inverting ($I_{B-}$) and non-inverting ($I_{B+}$) input terminals required to bias the internal input transistors:
    $$I_B = \frac{I_{B+} + I_{B-}}{2}$$
*   **Input Offset Current ($I_{OS}$):** The algebraic difference between the individual input bias currents, resulting from slight mismatches in the input transistors:
    $$I_{OS} = |I_{B+} - I_{B-}|$$
*   **Input Offset Voltage ($V_{OS}$):** The DC differential voltage that must be applied across the input terminals to force the output voltage to exactly $0\text{V}$.
*   **PSRR (Power Supply Rejection Ratio):** The ratio of the change in input offset voltage to the corresponding change in one of the power supply voltages, expressed in decibels:
    $$PSRR = 20\log_{10} \left( \frac{\Delta V_{OS}}{\Delta V_{CC}} \right)$$

---

### 2.2 Slew Rate and Frequency Limitations
*[Appeared in: 2019 Q4(b), 2017 Q4(a), 2017 Q6(b)]*

**Slew Rate (SR)** is the maximum physical rate of change of the output voltage of an op-amp:
$$SR = \left. \frac{dv_o}{dt} \right|_{max}$$
It is typically expressed in $\text{V}/\mu\text{s}$. If the input signal demands a faster change than the slew rate can provide, the output will distort into a triangular shape.

#### Maximum Frequency without Slew Distortion ($f_{max}$):
For a sinusoidal output $v_o(t) = V_p \sin(2\pi f t)$:
$$\frac{dv_o}{dt} = 2\pi f V_p \cos(2\pi f t) \Rightarrow \left. \frac{dv_o}{dt} \right|_{max} = 2\pi f V_p$$
To prevent slew rate distortion, we must satisfy:
$$SR \ge 2\pi f V_p \Rightarrow f_{max} = \frac{SR}{2\pi V_p}$$

---

## 3. Op-Amp Frequency Compensation
*[Appeared in: 2024 Q8(a), 2017 Q8(a)]*

### 3.1 Why Frequency Compensation is Needed
An operational amplifier consists of multiple cascaded internal transistor stages (differential input, level shifter, output buffer). Each stage introduces an RC pole, contributing to a high-frequency phase shift.
If the op-amp is configured with negative feedback, the closed-loop transfer function is:
$$A_f = \frac{A}{1 + A\beta}$$
If the cumulative phase shift of the open-loop gain $A$ reaches $-180^\circ$ at a frequency where the magnitude $|A\beta| \ge 1$:
1.  The negative feedback term ($1+A\beta$) transforms into subtraction ($1 - |A\beta| \rightarrow 0$).
2.  The closed-loop gain approaches infinity ($A_f \rightarrow \infty$).
3.  The amplifier becomes unstable and oscillates uncontrollably.
To prevent this, we must perform **frequency compensation** to ensure the open-loop gain drops below $0\text{ dB}$ ($|A| < 1$) before the phase shift reaches $-180^\circ$ (ensuring a stable phase margin).

---

### 3.2 Internal Phase Compensation Method
The most common technique is **Miller dominant-pole compensation**:
1.  A small capacitor $C_c$ (typically $\sim 30\text{ pF}$) is placed in parallel across the feedback path of an internal high-gain stage (the intermediate CE stage).
2.  Due to the Miller effect, this capacitance is multiplied by the stage gain, appearing as a massive virtual capacitor at the stage input.
3.  This creates a dominant low-frequency pole (typically at $10\text{ Hz}$).
4.  This dominant pole rolls off the open-loop gain at a steady rate of $-20\text{ dB/decade}$ over a massive frequency range, forcing the gain to cross $0\text{ dB}$ (unity gain) at a frequency well below the high-frequency poles, keeping the total phase shift safe at $\sim -90^\circ$ at the crossover point.

---

## 4. Worked Op-Amp Fundamentals Numericals

### 4.1 Maximum Frequency Calculation under Slew Rate Constraint
*[Appeared in: 2017 Q6(b)]*

**Problem Details:**
An inverting op-amp has feedback resistor $R_f = 100\text{ k}\Omega$ and input resistor $R_1 = 10\text{ k}\Omega$. The slew rate is $SR = 0.5\text{ V}/\mu\text{s}$. The input signal is $v_i(t) = 10\sin(2\pi f t)\text{ mV}$ peak. Calculate the maximum operating frequency ($f_{max}$) without distortion.

#### Step-by-Step Solution:

##### Step 1: Calculate the closed-loop voltage gain ($A_{CL}$)
$$A_{CL} = -\frac{R_f}{R_1} = -\frac{100\text{ k}\Omega}{10\text{ k}\Omega} = -10$$

##### Step 2: Determine output peak voltage ($V_{p(out)}$)
$$V_{p(out)} = |A_{CL}| \times V_{p(in)} = 10 \times 10\text{ mV} = 100\text{ mV} = 0.1\text{ V}$$

##### Step 3: Calculate $f_{max}$
Convert the slew rate to standard SI units ($\text{V/s}$):
$$SR = 0.5\text{ V}/\mu\text{s} = 0.5 \times 10^6\text{ V/s}$$
Apply the slew rate frequency equation:
$$f_{max} = \frac{SR}{2\pi V_{p(out)}} = \frac{0.5 \times 10^6\text{ V/s}}{2\pi \times 0.1\text{ V}} = \frac{5 \times 10^6}{2\pi}\text{ Hz} \approx 795.8\text{ kHz}$$

---

### 4.2 Peak-to-Peak Input Voltage under Slew Constraint
*[Appeared in: 2019 Q4(b)]*

**Problem Details:**
An op-amp circuit with a closed-loop gain of $10$ operates at $f = 40\text{ kHz}$. If the slew rate is $SR = 0.5\text{ V}/\mu\text{s}$, determine the maximum peak-to-peak input voltage ($V_{p-p(in)}$) that can be applied without causing output distortion.

#### Step-by-Step Solution:

##### Step 1: Calculate the maximum output peak voltage ($V_{p(out)}$)
$$SR \ge 2\pi f V_{p(out)} \Rightarrow V_{p(out)} = \frac{SR}{2\pi f}$$
$$V_{p(out)} = \frac{0.5 \times 10^6\text{ V/s}}{2\pi \times 40,000\text{ Hz}} = \frac{500,000}{80,000\pi} = \frac{50}{8\pi} \approx 1.989\text{ V (peak)}$$

##### Step 2: Calculate the peak-to-peak output voltage ($V_{p-p(out)}$)
$$V_{p-p(out)} = 2 \times V_{p(out)} = 2 \times 1.989\text{ V} \approx 3.978\text{ V}_{p-p}$$

##### Step 3: Calculate the maximum peak-to-peak input voltage ($V_{p-p(in)}$)
Since the closed-loop gain is $10$:
$$V_{p-p(in)} = \frac{V_{p-p(out)}}{\text{Gain}} = \frac{3.978\text{ V}_{p-p}}{10} \approx 0.398\text{ V}_{p-p} \quad (\text{or } 398\text{ mV}_{p-p})$$
