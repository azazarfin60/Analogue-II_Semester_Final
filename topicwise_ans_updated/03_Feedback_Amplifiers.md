[Previous](02_Frequency_Response.md) | [Home](index.md) | [Next](04_OpAmp_Fundamentals.md)

# 📚 Topic 03: Feedback Amplifiers
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Feedback Topologies and Classification

### 1.1 The Four Feedback Topologies & Voltage-Shunt Configuration

**Question:**
*[Appeared in: 2017 Q4(a)]*
* **(a)** What are the types of feedback connections? Explain voltage-shunt feedback configuration. **[04 Marks]**

**Answer:**
Negative feedback has four types. They depend on the parameter sampled at the output (Voltage or Current) and how the feedback mixes at the input (Series or Shunt):

| Feedback Topology | Output Sampling | Input Mixing | Gain Parameter | Ideal Input Impedance | Ideal Output Impedance |
|:---|:---|:---|:---|:---:|:---:|
| **Voltage-Series** | Voltage (Parallel) | Series (Voltage) | Voltage Gain ($A_v$) | $\infty$ (Increases) | $0$ (Decreases) |
| **Voltage-Shunt** | Voltage (Parallel) | Shunt (Current) | Transresistance ($R_m$) | $0$ (Decreases) | $0$ (Decreases) |
| **Current-Series** | Current (Series) | Series (Voltage) | Transconductance ($G_m$) | $\infty$ (Increases) | $\infty$ (Increases) |
| **Current-Shunt** | Current (Series) | Shunt (Current) | Current Gain ($A_i$) | $0$ (Decreases) | $\infty$ (Increases) |

**Voltage-Shunt Feedback Configuration:**
*   **Output Sampling (Voltage):** The feedback connects in parallel (shunt) with the load. It samples the output voltage. Parallel sampling stabilizes the output voltage. This physically decreases output impedance ($Z_{of} = Z_o / (1+A\beta)$).
*   **Input Mixing (Shunt):** The feedback mixes in parallel (shunt) with the input source. It injects a current ($I_f$) that opposes the input current ($I_i$). This stabilizes the input voltage. The source must provide more current to drive the same voltage. This physically decreases input impedance ($Z_{if} = Z_i / (1+A\beta)$).
*   **Application:** Ideal for transresistance amplifiers (current-to-voltage converters), such as inverting operational amplifiers.

---

### 1.2 Voltage-Series Configuration Derivations (Bandwidth & Impedance)

**Question:**
*[Appeared in: 2021 Q7(c), 2018 Q6(a), 2018 Q6(c)]*
* **(a)** Prove that a voltage-series feedback configuration is the most effective connection topology among negative feedback amplifiers in improving bandwidth, input impedance, and output impedance. **[04 Marks]**

**Answer:**
A voltage-series feedback amplifier is the best type for an ideal voltage amplifier. It increases input impedance, decreases output impedance, and expands bandwidth all at once.

**1. Bandwidth Expansion:**
Let $f_H$ and $f_L$ be the open-loop upper and lower cutoff frequencies, and $A_{mid}$ be the midband gain. 
The high-frequency open-loop response is $A(f) \approx \frac{A_{mid}}{1 + j(f/f_H)}$.
With feedback, the closed-loop gain $A_f$ is:
$$ A_f(f) = \frac{A(f)}{1 + A(f)\beta} = \frac{\frac{A_{mid}}{1 + j(f/f_H)}}{1 + \beta \left( \frac{A_{mid}}{1 + j(f/f_H)} \right)} = \frac{A_{mid}}{1 + A_{mid}\beta + j(f/f_H)} $$
Divide numerator and denominator by $(1 + A_{mid}\beta)$:
$$ A_f(f) = \frac{\frac{A_{mid}}{1 + A_{mid}\beta}}{1 + j \left( \frac{f}{f_H (1 + A_{mid}\beta)} \right)} = \frac{A_{mf}}{1 + j(f/f_{Hf})} $$
Thus, the new upper cutoff frequency is:
$$ f_{Hf} = f_H (1 + A_{mid}\beta) $$
Similarly, the lower cutoff frequency shifts to:
$$ f_{Lf} = \frac{f_L}{1 + A_{mid}\beta} $$
The overall bandwidth expands by the desensitivity factor $D = (1 + A_{mid}\beta)$.

**2. Input Impedance ($Z_{if}$) Increase:**
For a series input connection, the feedback voltage $V_f = \beta V_o$ opposes the input source voltage $V_s$:
$$ V_s = V_i + V_f = V_i + \beta V_o = V_i + \beta(A V_i) = V_i (1 + A\beta) $$
The input impedance looking into the source terminals is:
$$ Z_{if} = \frac{V_s}{I_i} $$
Since $I_i = V_i / Z_i$ (where $Z_i$ is the open-loop input impedance):
$$ Z_{if} = \frac{V_i (1 + A\beta)}{V_i / Z_i} = Z_i (1 + A\beta) $$
This proves the input impedance increases by the factor $(1+A\beta)$.

**3. Output Impedance ($Z_{of}$) Decrease:**
To find $Z_{of}$, we short the input source ($V_s = 0$) and apply a test voltage $V_t$ at the output. 
The current drawn is $I_t = \frac{V_t - A V_i}{Z_o}$.
Since $V_s = 0$, $V_i = -V_f = -\beta V_t$.
Substituting this into the current equation:
$$ I_t = \frac{V_t - A (-\beta V_t)}{Z_o} = \frac{V_t (1 + A\beta)}{Z_o} $$
$$ Z_{of} = \frac{V_t}{I_t} = \frac{Z_o}{1 + A\beta} $$
This proves the output impedance decreases by the factor $(1+A\beta)$.

---

## 2. Worked Feedback Numericals

### 2.1 Voltage-Series BJT Feedback Amplifier

**Question:**
*[Appeared in: 2018 Q6(b)]*
* **(b)** A voltage-series feedback amplifier has an open-loop voltage gain $A = -100$, open-loop input impedance $R_i = 10\text{ k}\Omega$, open-loop output impedance $R_o = 20\text{ k}\Omega$, and feedback factor $\beta = -0.1$. Determine (i) closed-loop voltage gain ($A_f$), (ii) closed-loop input impedance ($R_{if}$), and (iii) closed-loop output impedance ($R_{of}$). **[04 Marks]**

**Answer:**
**Step 1: Calculate the desensitivity factor ($D$)**
$$ D = 1 + A\beta = 1 + (-100)(-0.1) = 1 + 10 = 11 $$

**Step 2: Calculate closed-loop voltage gain ($A_f$)**
$$ A_f = \frac{A}{1+A\beta} = \frac{-100}{11} \approx -9.09 $$

**Step 3: Calculate closed-loop input impedance ($R_{if}$)**
For a voltage-series feedback (series input), input impedance increases:
$$ R_{if} = R_i (1+A\beta) = 10\text{ k}\Omega \times 11 = 110\text{ k}\Omega $$

**Step 4: Calculate closed-loop output impedance ($R_{of}$)**
For a voltage-series feedback (parallel output), output impedance decreases:
$$ R_{of} = \frac{R_o}{1+A\beta} = \frac{20\text{ k}\Omega}{11} \approx 1.818\text{ k}\Omega $$

---

### 2.2 Gain Sensitivity Numerical

**Question:**
*[Appeared in: 2024 Q8(c)]*
* **(c)** Discuss the engineering necessity of negative feedback in practical amplifiers. An amplifier stage with an open-loop gain $A = -1000$ and feedback factor $\beta = -0.1$ undergoes a gain change of $20\%$ due to temperature fluctuations. Calculate the percentage change in the closed-loop feedback gain ($A_f$). **[03 Marks, CO2]**

**Answer:**
**Engineering Need:** Negative feedback reduces sensitivity to temperature, component tolerances, and aging. It lowers the overall gain. But it greatly improves bandwidth and reduces distortion. It also allows precise control of impedances.

**Calculation:**
The change in closed-loop gain ($\frac{dA_f}{A_f}$) relates to the change in open-loop gain ($\frac{dA}{A}$) through the desensitivity factor:
$$ \frac{dA_f}{A_f} = \frac{1}{1 + A\beta} \left( \frac{dA}{A} \right) $$

Given:
*   $\frac{dA}{A} = 20\% = 0.20$
*   $A = -1000$
*   $\beta = -0.1$

Calculate the desensitivity factor:
$$ D = 1 + A\beta = 1 + (-1000)(-0.1) = 1 + 100 = 101 $$

Calculate the percentage change in closed-loop gain:
$$ \frac{dA_f}{A_f} = \frac{1}{101} \times 20\% \approx 0.198\% $$
The closed-loop gain only changes by **$0.2\%$**. This shows the stabilizing power of negative feedback.

---

### 2.3 JFET CS Feedback Loop Analysis

**Question:**
*[Appeared in: 2017 Q2(b)]*
* **(b)** For the following network, determine the change of gain with and without feedback. The JFET transconductance is $g_m = 5800\ \mu\text{S}$. **[06 Marks]**

##### Circuit Diagram:
```text
                    +15 V (Vdd)
                      |
                     [ ] RD = 10k
                      |
             +--------+
             |        |
          G  |     D  |
        +----+      +-+-+
   Vi (~| J1        |   | J1 (JFET)
        +-+--+      +-+-+
          |  |        | S
          |  |        +-----+
          |  |              |
          |  +--||----------+
          |     Cc (0.01uF) |
          |                 +-----+
          |                 |     |
          |                [ ]   [ ] RL = 10k
          |            R1  [ ]   [ ]
          |            100k |     |
          +-----------------+     |
          |                 |     |
         [ ] R2 = 20k      [ ]   ---
         [ ]               [ ]   GND
          |                 |
         GND               GND
```

**Answer:**
**Step 1: Gain without feedback ($A$)**
With the feedback loop open, the AC load resistance at the drain is:
$$ R_L' \approx R_D \parallel R_L = 10\text{ k}\Omega \parallel 10\text{ k}\Omega = 5\text{ k}\Omega $$
$$ A = -g_m R_L' = -5800 \times 10^{-6}\text{ S} \times 5000\ \Omega = -29 $$

**Step 2: Feedback factor ($\beta$)**
The voltage divider $R_1$ and $R_2$ defines the feedback fraction:
$$ \beta = -\frac{R_2}{R_1 + R_2} = -\frac{20\text{ k}\Omega}{100\text{ k}\Omega + 20\text{ k}\Omega} = -\frac{20}{120} \approx -0.1667 $$

**Step 3: Gain with feedback ($A_f$)**
$$ A_f = \frac{A}{1 + A\beta} = \frac{-29}{1 + (-29)(-0.1667)} = \frac{-29}{1 + 4.834} = \frac{-29}{5.834} \approx -4.97 $$

**Step 4: Calculate the gain change**
*   Gain without feedback: $-29$
*   Gain with feedback: $-4.97$
*   Absolute change in gain magnitude: $|A| - |A_f| = 29 - 4.97 = 24.03$ (an $82.8\%$ reduction).

---

### 2.4 Collector-Feedback BJT Amplifier Calculations

**Question:**
*[Appeared in: 2023 Q2(c)]*
* **(c)** For the collector-feedback BJT amplifier network shown below, calculate the input impedance ($Z_i$), output impedance ($Z_o$), voltage gain ($A_v$), and current gain ($A_i$). The BJT parameter values are $h_{fe} = 120$, $h_{ie} = 1.175\text{ k}\Omega$, and $h_{oe} = 20\ \mu\text{A/V}$. **[03 Marks, CLO2]**

##### Circuit Diagram:
```text
             +8V
              |
             [ ] 2.7k
              |
              +---+------+---||---> Io (Vo)
              |   |      |
             [ ]  |    C |
             330k |    --+
              |   |  B |  ----+
              +---+----+  |  /|
                       |  |/ |
                    Ii |  +---+
              Vi >-||--+      | E
                              |
                            ----- GND
```

**Answer:**
**Step 1: Effective load resistance ($R_C'$)**
From $h_{oe}$, the internal output resistance is $r_o = 1/h_{oe} = 1 / (20\ \mu\text{S}) = 50\text{ k}\Omega$.
$$ R_C' = R_C \parallel r_o = 2.7\text{ k}\Omega \parallel 50\text{ k}\Omega \approx 2.56\text{ k}\Omega $$

**Step 2: Voltage Gain ($A_v$)**
The open-loop voltage gain including the parallel feedback branch is:
$$ A_v = -h_{fe} \frac{R_C' \parallel R_F}{h_{ie}} = -120 \frac{2.56\text{ k}\Omega \parallel 330\text{ k}\Omega}{1.175\text{ k}\Omega} \approx -120 \times \frac{2.54\text{ k}\Omega}{1.175\text{ k}\Omega} \approx -259.4 $$

**Step 3: Input Impedance ($Z_i$)**
Using Miller's theorem, the feedback resistor $R_F$ is reflected at the input as:
$$ R_{Mi} = \frac{R_F}{1 - A_v} = \frac{330\text{ k}\Omega}{1 - (-259.4)} = \frac{330\text{ k}\Omega}{260.4} \approx 1.267\text{ k}\Omega $$
$$ Z_i = h_{ie} \parallel R_{Mi} = 1.175\text{ k}\Omega \parallel 1.267\text{ k}\Omega \approx 607\ \Omega $$

**Step 4: Output Impedance ($Z_o$)**
$$ Z_o = R_C \parallel r_o \parallel R_F \approx R_C' \parallel R_F \approx 2.54\text{ k}\Omega $$

**Step 5: Current Gain ($A_i$)**
$$ A_i = \frac{i_o}{i_i} = A_v \left( \frac{Z_i}{R_C} \right) = -259.4 \times \left( \frac{607\ \Omega}{2700\ \Omega} \right) \approx -58.3 $$

[Previous](02_Frequency_Response.md) | [Home](index.md) | [Next](04_OpAmp_Fundamentals.md)
