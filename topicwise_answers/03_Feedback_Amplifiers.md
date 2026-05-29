# 📚 Topic 03: Feedback Amplifiers
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Feedback Topologies and Classification

### 1.1 The Four Feedback Topologies
*[Appeared in: 2024 Q3(a), 2022 Q2(c), 2017 Q4(a)]*

Negative feedback is classified based on the physical parameter sampled at the output (Voltage or Current) and how the feedback signal is mixed at the input (Series or Shunt):

| Feedback Topology | Output Sampling | Input Mixing | Gain Parameter | Ideal Input Impedance | Ideal Output Impedance |
|:---|:---|:---|:---|:---:|:---:|
| **Voltage-Series** | Voltage (Parallel) | Series (Voltage) | Voltage Gain ($A_v$) | $\infty$ (Increases) | $0$ (Decreases) |
| **Voltage-Shunt** | Voltage (Parallel) | Shunt (Current) | Transresistance ($R_m$) | $0$ (Decreases) | $0$ (Decreases) |
| **Current-Series** | Current (Series) | Series (Voltage) | Transconductance ($G_m$) | $\infty$ (Increases) | $\infty$ (Increases) |
| **Current-Shunt** | Current (Series) | Shunt (Current) | Current Gain ($A_i$) | $0$ (Decreases) | $\infty$ (Increases) |

---

### 1.2 Detailed View: Voltage-Shunt Feedback
*[Appeared in: 2017 Q4(a)]*

In a **Voltage-Shunt feedback** configuration:
*   **Output Sampling (Voltage):** The feedback network is connected in parallel (shunt) with the load. It samples the output voltage. Parallel sampling acts to stabilize the output voltage, which translates physically to a **decrease in output impedance** ($Z_{of} = Z_o / D$).
*   **Input Mixing (Shunt):** The feedback signal is mixed in parallel (shunt) with the input signal source. The feedback network injects a current ($I_f$) that opposes the input current ($I_i$). Mixing currents in parallel stabilizes the input voltage, requiring a higher current from the source to drive the same input voltage. This translates physically to a **decrease in input impedance** ($Z_{if} = Z_i / D$).
*   **Application:** Ideal for transresistance amplifiers (current-to-voltage converters), such as inverting operational amplifiers.

---

## 2. Voltage-Series Negative Feedback Derivations
*[Appeared in: 2024 Q3(b), 2021 Q2(b), 2018 Q6(a)]*

Assuming an open-loop amplifier with voltage gain $A$, input impedance $Z_i$, output impedance $Z_o$, and a feedback factor $\beta$:

```
               +----------------------------------------+
        Vi o---|---(+)------------------[ A ]--------+---|---> Vo
               |    |                                  |   |
               |   (-) <----[ Beta ]<------------------+   |
               +-------------------------------------------+
```

### 2.1 Bandwidth Improvement
Let $f_H$ and $f_L$ be the open-loop upper and lower cutoff frequencies.
*   **Upper Cutoff with Feedback ($f_{Hf}$):**
    $$
    A_f(f) = \frac{A(f)}{1 + A(f)\beta}
    $$
    Substituting the high-frequency open-loop response $A(f) \approx \frac{A_{mid}}{1 + j(f/f_H)}$:
    $$
    A_f(f) = \frac{\frac{A_{mid}}{1 + j(f/f_H)}}{1 + \beta \left( \frac{A_{mid}}{1 + j(f/f_H)} \right)} = \frac{A_{mid}}{1 + j(f/f_H) + A_{mid}\beta} = \frac{A_{mid}}{(1 + A_{mid}\beta) + j(f/f_H)}
    $$
    Divide both numerator and denominator by $(1 + A_{mid}\beta)$:
    $$
    A_f(f) = \frac{\frac{A_{mid}}{1 + A_{mid}\beta}}{1 + j \left( \frac{f}{f_H (1 + A_{mid}\beta)} \right)} = \frac{A_{mf}}{1 + j(f/f_{Hf})}
    $$
    $$
    \text{Thus,} \quad f_{Hf} = f_H (1 + A_{mid}\beta) = f_H D
    $$
*   **Lower Cutoff with Feedback ($f_{Lf}$):**
    Substituting the low-frequency open-loop response $A(f) \approx \frac{A_{mid}}{1 - j(f_L/f)}$:
    $$
    f_{Lf} = \frac{f_L}{1 + A_{mid}\beta} = \frac{f_L}{D}
    $$
*   **Bandwidth with Feedback ($BW_f$):**
    $$
    BW_f = f_{Hf} - f_{Lf} \approx f_H D - \frac{f_L}{D} \approx f_H D \approx BW \times (1 + A\beta)
    $$
This mathematically proves negative feedback expands the operating bandwidth by a factor of $(1+A\beta)$.

---

### 2.2 Input Impedance ($Z_{if}$)
For a series input connection, the feedback voltage $V_f = \beta V_o$ opposes the input voltage $V_i$:
$$
V_i = V_s - V_f = V_s - \beta V_o
$$
Since $V_o = A V_i$:
$$
V_s = V_i + \beta(A V_i) = V_i (1 + A\beta)
$$
The input impedance looking into the source terminals is:
$$
Z_{if} = \frac{V_s}{I_i}
$$
Since $I_i = V_i / Z_i$ (where $Z_i$ is the open-loop input impedance):
$$
Z_{if} = \frac{V_i (1 + A\beta)}{V_i / Z_i} = Z_i (1 + A\beta)
$$
This mathematically proves the input impedance increases by the factor $(1+A\beta)$.

---

### 2.3 Output Impedance ($Z_{of}$)
To find the output impedance $Z_{of}$, we short the input signal source ($V_s = 0$) and apply an external test voltage $V_t$ at the output terminal, measuring the resulting current $I_t$.
$$
I_t = \frac{V_t - A V_i}{Z_o}
$$
Since $V_s = 0$, the voltage at the amplifier input is strictly the negative of the feedback voltage:
$$
V_i = -V_f = -\beta V_o = -\beta V_t
$$
Substitute $V_i = -\beta V_t$ into the current equation:
$$
I_t = \frac{V_t - A (-\beta V_t)}{Z_o} = \frac{V_t (1 + A\beta)}{Z_o}
$$
$$
Z_{of} = \frac{V_t}{I_t} = \frac{Z_o}{1 + A\beta}
$$
This mathematically proves the output impedance decreases by the factor $(1+A\beta)$.

---

## 3. Worked Feedback Numericals

### 3.1 Voltage-Series BJT Feedback Amplifier Parameter Extraction
*[Appeared in: 2018 Q6(b)]*

**Problem Details:**
A voltage-series feedback amplifier has open-loop parameters: voltage gain $A = -100$, input impedance $R_i = 10\text{ k}\Omega$, and output impedance $R_o = 20\text{ k}\Omega$. The feedback factor is $\beta = -0.1$.

#### Step-by-Step Solution:

##### Step 1: Calculate the desensitivity factor ($D$)
$$
D = 1 + A\beta = 1 + (-100)(-0.1) = 1 + 10 = 11
$$

##### Step 2: Calculate closed-loop voltage gain ($A_f$)
$$
A_f = \frac{A}{1+A\beta} = \frac{-100}{11} \approx -9.09
$$

##### Step 3: Calculate closed-loop input impedance ($R_{if}$)
For a series input connection, input impedance increases:
$$
R_{if} = R_i (1+A\beta) = 10\text{ k}\Omega \times 11 = 110\text{ k}\Omega
$$

##### Step 4: Calculate closed-loop output impedance ($R_{of}$)
For a parallel output connection (voltage sampling), output impedance decreases:
$$
R_{of} = \frac{R_o}{1+A\beta} = \frac{20\text{ k}\Omega}{11} \approx 1.818\text{ k}\Omega
$$

---

### 3.2 JFET CS Feedback Loop Analysis
*[Appeared in: 2017 Q2(b)]*

**Problem Details:**
A JFET CS amplifier with $g_m = 5800\ \mu\text{S}$ is configured with feedback division using resistors $R_1 = 100\text{ k}\Omega$ and $R_2 = 20\text{ k}\Omega$. Load components: $R_D = 10\text{ k}\Omega$, $R_L = 10\text{ k}\Omega$. Calculate the gain change with and without feedback.

#### Step-by-Step Solution:

##### Step 1: Gain without feedback ($A$)
With the feedback loop open, the AC load resistance at the drain is:
$$
R_L' \approx R_D \parallel R_L = 10\text{ k}\Omega \parallel 10\text{ k}\Omega = 5\text{ k}\Omega
$$
$$
A = -g_m R_L' = -5800 \times 10^{-6}\text{ S} \times 5000\ \Omega = -29
$$

##### Step 2: Feedback factor ($\beta$)
The feedback fraction returned to the source terminal is:
$$
\beta = -\frac{R_2}{R_1 + R_2} = -\frac{20\text{ k}\Omega}{100\text{ k}\Omega + 20\text{ k}\Omega} = -\frac{20}{120} \approx -0.1667
$$

##### Step 3: Gain with feedback ($A_f$)
$$
A_f = \frac{A}{1 + A\beta} = \frac{-29}{1 + (-29)(-0.1667)} = \frac{-29}{1 + 4.834} = \frac{-29}{5.834} \approx -4.97
$$

##### Step 4: Calculate the gain change
*   Gain without feedback: $-29$
*   Gain with feedback: $-4.97$
*   Absolute change in gain magnitude: $|A| - |A_f| = 29 - 4.97 = 24.03$ (an $82.8\%$ reduction).

---

### 3.3 Collector-Feedback BJT Amplifier Calculations
*[Appeared in: 2023 Q2(c)]*

**Problem Details:**
A collector-feedback BJT amplifier has components: $R_C = 2.7\text{ k}\Omega$, feedback resistor $R_F = 330\text{ k}\Omega$, and h-parameters: $h_{fe} = 120$, $h_{ie} = 1.175\text{ k}\Omega$, $h_{oe} = 20\ \mu\text{S} \Rightarrow r_o = 1/h_{oe} = 50\text{ k}\Omega$. Calculate $Z_i, Z_o, A_v, A_i$.

#### Step-by-Step Solution:

##### Step 1: Effective load resistance ($R_C'$)
$$
R_C' = R_C \parallel r_o = 2.7\text{ k}\Omega \parallel 50\text{ k}\Omega \approx 2.56\text{ k}\Omega
$$

##### Step 2: Voltage Gain ($A_v$)
The open-loop voltage gain including the parallel feedback branch is:
$$
A_v = -h_{fe} \frac{R_C' \parallel R_F}{h_{ie}} = -120 \frac{2.56\text{ k}\Omega \parallel 330\text{ k}\Omega}{1.175\text{ k}\Omega} \approx -120 \times \frac{2.54\text{ k}\Omega}{1.175\text{ k}\Omega} \approx -259.4
$$

##### Step 3: Input Impedance ($Z_i$)
Using Miller's theorem, the feedback resistor $R_F$ is reflected at the input as:
$$
R_{Mi} = \frac{R_F}{1 - A_v} = \frac{330\text{ k}\Omega}{1 - (-259.4)} = \frac{330\text{ k}\Omega}{260.4} \approx 1.267\text{ k}\Omega
$$
$$
Z_i = h_{ie} \parallel R_{Mi} = 1.175\text{ k}\Omega \parallel 1.267\text{ k}\Omega \approx 607\ \Omega
$$

##### Step 4: Output Impedance ($Z_o$)
$$
Z_o = R_C \parallel r_o \parallel R_F \approx R_C' \parallel R_F \approx 2.54\text{ k}\Omega
$$

##### Step 5: Current Gain ($A_i$)
$$
A_i = \frac{i_o}{i_i} = A_v \left( \frac{Z_i}{R_C} \right) = -259.4 \times \left( \frac{607\ \Omega}{2700\ \Omega} \right) \approx -58.3
$$
