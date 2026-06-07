[Previous](04_OpAmp_Fundamentals.md) | [Home](index.md) | [Next](06_Oscillators.md)

# 📚 Topic 05: OpAmp Applications
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Mathematical Implementation Circuits

### 1.1 Designing Complex Mathematical Schematics
*[Appeared in: 2024 Q7(b), 2022 Q5(b), 2021 Q6(d)]*

**Question:**
* **(b)** Design an op-amp circuit whose output voltage satisfies the mathematical equation:
$$ V_o = 0.5 V_1 + 3 V_2 + 2 \int V_3 d t - 5 \frac{d V_4}{d t} $$
  **[04 Marks]**

**Answer:**
We can use an inverting summing configuration ($v_o = -[v_a + v_b + v_c + v_d]$). First we condition each input signal. Then we pass them through a final unity-gain inverting summer to fix the sign.

**Step 1: Signal Conditioning Channels**
1.  **Differentiator Channel ($V_4$):**
    Pass $V_4$ through an inverting differentiator stage:
    $$ v_d = -R_d C_d \frac{dV_4}{dt} $$
    To yield $-5 \frac{dV_4}{dt}$ directly at the output, we need the summer to receive $+5 \frac{dV_4}{dt}$. So set $R_d C_d = 5$. Let $C_d = 10\ \mu\text{F}$ and $R_d = 500\text{ k}\Omega$.
    $$ v_d = -5 \frac{dV_4}{dt} $$
    *(Wait, if $v_d = -5 dV_4/dt$, passing it through the inverting summer makes it $+5 dV_4/dt$. The equation requires $-5 dV_4/dt$. So we need an extra unity inverter for this channel, or we set $R_d C_d = -5$ which is impossible. So $v_d \rightarrow \text{Unity Inverter} \rightarrow \text{Summer}$.)*
    Actually, let's process them all directly into an inverting summer with feedback resistor $R_f$:
    $$ V_{sum} = -\left( \text{sum} \right) $$
    Let the final output $V_o$ come from an inverting unity-gain amplifier ($R_{in} = R_f = 10\text{ k}\Omega$) connected to the main summer. So the main summer output $V_{sum} = -(0.5 V_1 + 3 V_2 + 2 \int V_3 dt - 5 \frac{dV_4}{dt})$.

2.  **Inverting Gain Channel 1 ($V_1$):**
    We need $-0.5 V_1$ into the summer. Pass $V_1$ into an inverting amplifier: $v_1' = -\frac{R_f}{R_i} V_1$. Let $R_i = 20\text{ k}\Omega, R_f = 10\text{ k}\Omega$. So $v_1' = -0.5 V_1$.
3.  **Inverting Gain Channel 2 ($V_2$):**
    We need $-3 V_2$ into the summer. Pass $V_2$ into an inverting amplifier: $v_2' = -\frac{R_f}{R_i} V_2$. Let $R_i = 10\text{ k}\Omega, R_f = 30\text{ k}\Omega$. So $v_2' = -3 V_2$.
4.  **Integrator Channel ($V_3$):**
    We need $-2 \int V_3 dt$ into the summer. Pass $V_3$ into an inverting integrator: $v_3' = -\frac{1}{R_c C_c} \int V_3 dt$. To get a coefficient of $2$, set $R_c C_c = 0.5\text{ s}$. Let $C_c = 10\ \mu\text{F}$ and $R_c = 50\text{ k}\Omega$. So $v_3' = -2 \int V_3 dt$.
5.  **Differentiator Channel ($V_4$):**
    We need $+5 \frac{dV_4}{dt}$ into the summer. Pass $V_4$ into an inverting differentiator: $v_4' = -R_d C_d \frac{dV_4}{dt}$. Set $R_d C_d = 5\text{ s}$. Let $C_d = 10\ \mu\text{F}$ and $R_d = 500\text{ k}\Omega$. So $v_4' = -5 \frac{dV_4}{dt}$. Then pass $v_4'$ through a unity-gain inverting amplifier to get $v_4'' = +5 \frac{dV_4}{dt}$.

**Step 2: Main Inverting Summer**
Feed $v_1', v_2', v_3'$, and $v_4''$ into a summing amplifier with $R_{in1} = R_{in2} = R_{in3} = R_{in4} = R_{f(sum)} = 10\text{ k}\Omega$.
$$ V_{sum} = -(v_1' + v_2' + v_3' + v_4'') = -(-0.5 V_1 - 3 V_2 - 2 \int V_3 dt + 5 \frac{dV_4}{dt}) $$
$$ V_{sum} = 0.5 V_1 + 3 V_2 + 2 \int V_3 dt - 5 \frac{dV_4}{dt} $$
*(Note: Because the signs perfectly cancelled, we don't need the final unity inverter we planned! The output of the main summer is our target $V_o$.)*

---

### 1.2 Integrator & Differentiator Practical Limitations
*[Appeared in: 2023 Q5(b)]*

**Question:**
* **(b)** Describe how practical op-amp integrator and differentiator circuits overcome the frequency stability and noise limitations of basic models. **[03 Marks, CLO2]**

**Answer:**
*   **Practical Integrator:**
    An ideal integrator ($V_o = -\frac{1}{RC}\int V_i dt$) has infinite DC gain. The feedback capacitor acts as an open circuit at $0\text{ Hz}$. Tiny DC input offsets will integrate over time. This makes the output ramp up and saturate the rails.
    **Solution:** Connect a large feedback resistor $R_f$ (e.g., $10\text{ M}\Omega$) in parallel with the capacitor. This caps the maximum DC gain to $A_v = -R_f/R_{in}$, preventing saturation while maintaining integration at higher frequencies.
*   **Practical Differentiator:**
    An ideal differentiator ($V_o = -RC \frac{dVi}{dt}$) has a gain that increases with frequency ($|A| = \omega RC$). This amplifies high-frequency noise. It also causes instability due to phase shift approaching $-180^\circ$.
    **Solution:** Add a small resistor $R_i$ in series with the input capacitor. Add a small capacitor $C_f$ in parallel with the feedback resistor. This rolls off the high-frequency response and stabilizes the circuit.

---

### 1.3 Multi-Stage Op-Amp Circuit Calculation
*[Appeared in: 2024 Q7(c), 2021 Q8(b)]*

**Question:**
* **(c)** Calculate the closed-loop output voltage $V_o$ of the multi-stage operational amplifier circuit shown below. The input voltage is $V_1 = 0.1\text{ V}$ DC. **[03 Marks, CO3]**

*(Assuming standard 3-stage instrumentation or cascaded amplifier schematic)*

**Answer:**
*(For a generic cascade where Stage 1 is non-inverting gain, Stage 2 is inverting, etc. Below is the methodology.)*
1.  **Stage 1 Analysis:** Identify the topology. If it's a non-inverting amplifier, $V_{o1} = V_{in} \left( 1 + \frac{R_f}{R_1} \right)$.
2.  **Stage 2 Analysis:** If $V_{o1}$ feeds into an inverting amplifier, $V_{o2} = -\left(\frac{R_f}{R_1}\right) V_{o1}$.
3.  **Final Output:** Cascade the equations. $V_o = V_{o(final)} = A_1 \times A_2 \times V_{in}$.
*If this is an Instrumentation Amplifier:* The output is $V_o = \left( 1 + \frac{2 R_{feedback}}{R_{gain}} \right) \left( \frac{R_3}{R_2} \right) (V_{in2} - V_{in1})$. Substitute the given resistor values and differential input to solve for $V_o$.

---

## 2. Comparators & Schmitt Triggers

### 2.1 Comparator vs. Oscillator
*[Appeared in: 2021 Q6(a)]*

**Question:**
* **(a)** Differentiate between comparator and oscillator circuits in terms of feedback loop configuration and transfer characteristics. **[02 Marks, CLO1]**

**Answer:**
*   **Feedback Loop Configuration:** A comparator operates strictly **open-loop** (or with positive feedback for hysteresis). An oscillator *must* have a closed **positive feedback loop** to sustain its output.
*   **Transfer Characteristics:** A comparator compares two input voltages. It abruptly switches its output between extreme saturation states ($+V_{sat}$ or $-V_{sat}$). It does not generate a signal, it just thresholds one. An oscillator generates a continuous periodic AC waveform on its own. It needs no external AC input.

---

### 2.2 Noise in Comparators and Schmitt Trigger Solution
*[Appeared in: 2021 Q6(b)]*

**Question:**
* **(b)** Discuss the effect of high-frequency input noise on basic comparator circuits. How can this problem be solved practically? **[02 Marks, CLO1]**

**Answer:**
**The Problem (Chattering):** A noisy analog input slowly passes through a single threshold. The high-frequency noise spikes cross the threshold multiple times. This makes the comparator output chatter rapidly between its positive and negative states. It causes false triggering in digital logic.

**The Solution (Schmitt Trigger):** A **Schmitt Trigger** solves this problem. It uses positive feedback to establish **hysteresis**.
Instead of a single threshold, the Schmitt Trigger creates two separate thresholds: an Upper Trigger Point ($V_{UT}$) and a Lower Trigger Point ($V_{LT}$). 
When the rising noisy input crosses $V_{UT}$, the output switches states. The threshold instantly drops to $V_{LT}$. The noise spikes cannot cross this new, lower threshold. The output stays stable. The input must fall below $V_{LT}$ to switch back.

---

## 3. Non-Linear Log/Antilog Amplifiers

### 3.1 Logarithmic Amplifier Derivation
*[Appeared in: 2020 Q7(b)]*

**Question:**
* **(b)** Derive the expression of output voltage $V_o$ for the logarithmic amplifier circuit shown in Figure 7(b). **[04 Marks]**

**Answer:**
An inverting op-amp configuration with a matched BJT placed in the feedback loop:
```text
                     Q1 (BJT)
                   +--|<|---+ (Collector to Emitter)
                   |  C   E |
        Vin o-[ R ]+--o (-) |
                      |     |
        Gnd o--------(+)----+---o Vout
```
1.  By virtual ground, the inverting terminal voltage is $V_- \approx 0\text{V}$.
2.  Input current flowing through resistor $R$:
$$ I_{in} = \frac{V_{in} - 0}{R} = \frac{V_{in}}{R} $$
3.  Since the op-amp has infinite input impedance, all of $I_{in}$ must flow through the BJT's collector:
$$ I_C = I_{in} = \frac{V_{in}}{R} $$
4.  The BJT collector current is exponentially related to its base-emitter voltage:
$$ I_C = I_s e^{V_{BE} / \eta V_T} $$
    where $I_s$ is the reverse saturation current and $V_T \approx 26\text{ mV}$ is the thermal voltage.
5.  Since the base is grounded ($V_B = 0\text{V}$) and the emitter is tied to the output ($V_E = V_{out}$):
$$ V_{BE} = V_B - V_E = -V_{out} $$
6.  Substitute this expression into the BJT current equation:
$$ I_C = I_s e^{-V_{out} / \eta V_T} \Rightarrow \frac{V_{in}}{R} = I_s e^{-V_{out} / \eta V_T} \Rightarrow \frac{V_{in}}{I_s R} = e^{-V_{out} / \eta V_T} $$
7.  Take the natural logarithm of both sides:
$$ \ln \left( \frac{V_{in}}{I_s R} \right) = -\frac{V_{out}}{\eta V_T} \Rightarrow V_{out} = -\eta V_T \ln \left( \frac{V_{in}}{I_s R} \right) $$
The output voltage is proportional to the natural logarithm of the input voltage.

---

### 3.2 Antilogarithmic Amplifier Design
*[Appeared in: 2022 Q7(c)]*

**Question:**
* **(c)** Design an antilogarithmic amplifier circuit using an op-amp and a matched diode/BJT feedback device. **[04/05 Marks, CO3]**

**Answer:**
Placing the BJT at the input and the resistor $R$ in the feedback loop reverses the mathematical operation of the logarithmic amplifier.
```text
                     Rf
                   +-[ ]----+ 
                   |        |
        Vin o--|>|-+--o (-) |
               B E    |     |
        Gnd o--------(+)----+---o Vout
```
1.  By virtual ground, the inverting terminal voltage is $V_- \approx 0\text{V}$. The base is at $V_{in}$ and emitter at $0\text{V}$, so $V_{BE} = V_{in}$.
2.  The collector current injected into the inverting node is:
$$ I_C = I_s e^{V_{in} / \eta V_T} $$
3.  All of this current must flow through the feedback resistor $R_f$:
$$ V_{out} = -I_C R_f = -R_f I_s e^{V_{in} / \eta V_T} $$
The output is exponentially (antilogarithmically) proportional to the input voltage.

---

## 4. Specialized Configurations

### 4.1 Instrumentation Amplifier
*[Appeared in: 2022 Q5(a)]*

**Question:**
* **(a)** Explain how an operational amplifier can be configured to act as an instrumentation amplifier. **[03 Marks, CO1]**

**Answer:**
An instrumentation amplifier is constructed using three operational amplifiers:
1.  **Input Buffer Stage (Two Op-Amps):** Two non-inverting amplifiers are cross-coupled. They share a single gain resistor ($R_G$). This provides almost infinite input impedance. It draws zero current from delicate sensors. It amplifies the differential signal but passes the common-mode signal with a gain of 1.
2.  **Differential Stage (One Op-Amp):** A four-resistor differential amplifier subtracts the outputs of the two buffers. The common-mode signal was not amplified earlier, but the differential signal was. So this stage easily rejects the common-mode noise. This gives a very high CMRR.
**Application:** Used for amplifying very small differential signals (e.g., from strain gauges or biomedical sensors) in highly noisy environments.

---

### 4.2 Negative Impedance Converter (NIC)
*[Appeared in: 2023 Q6(b)]*

**Question:**
* **(b)** Explain the operational configuration of an op-amp as a Negative Impedance Converter (NIC). **[03 Marks, CLO1]**

**Answer:**
An NIC is an active op-amp configuration that simulates a negative resistance:
```text
                    R2
               +---[  ]---+
               |          |
        Vi o--(+)--[ Av ]-+---o Vo
               |          |
               +---[  ]---+
                    R1
```
**Operational Explanation:**
1.  Assume $R_1 = R_2$. The feedback network to the inverting input is a voltage divider:
$$ V_- = V_{out} \left( \frac{R_1}{R_1 + R_2} \right) = \frac{V_{out}}{2} $$
2.  By the virtual short principle, $V_- = V_+ \Rightarrow V_{in} = \frac{V_{out}}{2} \Rightarrow V_{out} = 2 V_{in}$.
3.  A positive feedback resistor $R$ is connected between the non-inverting input ($V_{in}$) and the output ($V_{out}$). The current $I_{in}$ flowing from the signal source into the input terminal is:
$$ I_{in} = \frac{V_{in} - V_{out}}{R} $$
4.  Substitute $V_{out} = 2 V_{in}$:
$$ I_{in} = \frac{V_{in} - 2 V_{in}}{R} = -\frac{V_{in}}{R} $$
5.  The apparent input impedance seen by the source is:
$$ Z_{in} = \frac{V_{in}}{I_{in}} = -R $$
The circuit acts as a negative resistor. It pushes current *back* into the signal source instead of drawing it.

[Previous](04_OpAmp_Fundamentals.md) | [Home](index.md) | [Next](06_Oscillators.md)
