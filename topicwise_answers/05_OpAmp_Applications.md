# 📚 Topic 05: OpAmp Applications
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Linear Mathematical Circuits

### 1.1 Practical Integrators & Differentiators
*[Appeared in: 2024 Q5(b), 2023 Q5(b)]*

*   **Practical Integrator:**
    An ideal integrator ($V_o = -\frac{1}{RC}\int V_i dt$) has infinite DC gain because the feedback capacitor acts as an open circuit at $0\text{ Hz}$. Minute DC input offset voltages will integrate over time, causing the output to ramp up and saturate the rails.
    **Solution:** Connect a large feedback resistor $R_f$ in parallel with the capacitor. This caps the DC gain to $A_v = -R_f/R_{in}$ and stabilizes the circuit.
*   **Practical Differentiator:**
    An ideal differentiator ($V_o = -RC \frac{dVi}{dt}$) has a gain that increases linearly with frequency ($|A| = \omega RC$). This amplifies high-frequency input noise and causes instability.
    **Solution:** Add a small resistor $R_i$ in series with the input capacitor, and a small capacitor $C_f$ in parallel with the feedback resistor to roll off the high-frequency response.

---

### 1.2 Designing Complex Mathematical Schematics
*[Appeared in: 2020 Q8(b), 2019 Q4(a), 2018 Q4(b)]*

#### Example Design 1: $v_o = 0.5 v_1 - 0.7 v_2 + 0.2 \frac{d v_3}{d t}$
To implement this equation using an inverting summing configuration ($v_o = -[V_A + V_B + V_C]$):
1.  **Differentiator Channel ($v_3$):**
    Pass $v_3$ through an inverting differentiator stage:
    $$v_a = -R_d C_d \frac{dv_3}{dt}$$
    Choose $C_d = 1\ \mu\text{F}$ and $R_d = 200\text{ k}\Omega$ to yield:
    $$v_a = -0.2 \frac{dv_3}{dt}$$
2.  **Inverting Gain Channel ($v_1$):**
    Pass $v_1$ through an inverting amplifier:
    $$v_b = -\left( \frac{R_{f1}}{R_{i1}} \right) v_1$$
    Choose $R_{i1} = 100\text{ k}\Omega$ and $R_{f1} = 50\text{ k}\Omega$ to yield:
    $$v_b = -0.5 v_1$$
3.  **Inverting Summing Stage:**
    Sum $v_a$, $v_b$, and the direct input $v_2$ into a final inverting summer:
    $$v_o = -\left( \frac{R_f}{R_a} v_a + \frac{R_f}{R_b} v_b + \frac{R_f}{R_2} v_2 \right)$$
    Let $R_f = 100\text{ k}\Omega$.
    *   To yield $+0.2 \frac{dv_3}{dt}$, set $R_a = 100\text{ k}\Omega$ (gain of $-1$ on $v_a$).
    *   To yield $+0.5 v_1$, set $R_b = 100\text{ k}\Omega$ (gain of $-1$ on $v_b$).
    *   To yield $-0.7 v_2$, set $R_2 = 142.8\text{ k}\Omega$ (gain of $-0.7$ on $v_2$).

#### Example Design 2: $V_o = 3 V_1 - 2 V_2 - 3 \frac{d V_1}{d t}$
1.  **Gain Channel 1 ($V_1$):** Pass $V_1$ to an inverting stage with gain $-3$ ($R_i = 10\text{ k}\Omega, R_f = 30\text{ k}\Omega$), yielding $V_{1a} = -3V_1$.
2.  **Gain Channel 2 ($V_2$):** Pass $V_2$ to a non-inverting stage with gain $+2$ ($R_i = 10\text{ k}\Omega, R_f = 10\text{ k}\Omega$), yielding $V_{2a} = 2V_2$.
3.  **Differentiator Channel:** Pass $V_1$ through an inverting differentiator stage ($R_d = 300\text{ k}\Omega, C_d = 10\ \mu\text{F}$), yielding $V_d = -3 \frac{dV_1}{dt}$. Pass this to a unity inverter to yield $V_{da} = 3 \frac{dV_1}{dt}$.
4.  **Inverting Summer:** Sum $V_{1a}, V_{2a}, V_{da}$ with unity gain:
    $$V_o = -(V_{1a} + V_{2a} + V_{da}) = -(-3V_1 + 2V_2 + 3\frac{dV_1}{dt}) = 3V_1 - 2V_2 - 3\frac{dV_1}{dt}$$

---

## 2. Non-Linear Waveform Generators
*[Appeared in: 2017 Q6(c)]*

*   **Pulse Generator:** An astable multivibrator utilizing asymmetric charging/discharging feedback. By placing a diode in parallel with a portion of the feedback resistor network, the capacitor charges rapidly through a low-resistance path (diode forward-biased) and discharges slowly through a high-resistance path (diode reverse-biased), creating a narrow pulse train output.
*   **Triangular Wave Generator:** Created by cascading an astable Schmitt trigger stage (which outputs a square wave) into a practical integrator stage. The positive/negative levels of the square wave force the integrator to ramp down/up linearly, creating a highly symmetrical triangular waveform.

---

## 3. Self-Study Circuit 1: Precision Rectifiers
*[Appeared in: 2020 Q7(c), 2019 Q5(b), 2023 Q8(a)]*

### 3.1 Precision Half-Wave Rectifier
A standard diode requires a forward voltage drop of $\sim 0.7\text{ V}$ to turn on, which clips small input signals. Placing the diode inside the op-amp's feedback loop overcomes this:

```
                  D1 (Cathode)
              +----|<-----+
              |           |
        Vin o-(+)--[ Av ]-o----> Vout
              |           |
              +-----------+
```

*   **Positive Half-Cycle ($V_{in} > 0$):** The op-amp output swings positive, forward-biasing the diode. The feedback loop closes, and the output at the cathode tracks the input: $V_{out} = V_{in}$. The open-loop gain divides the $0.7\text{ V}$ drop to virtually zero.
*   **Negative Half-Cycle ($V_{in} < 0$):** The op-amp output swings to negative saturation, reverse-biasing the diode. The feedback loop opens, and the output is pulled to $0\text{V}$ by the load resistor: $V_{out} = 0\text{V}$.

---

### 3.2 Precision Full-Wave Rectifier
Constructed by cascading a precision half-wave rectifier and an inverting summing stage:
*   The input $V_{in}$ is fed to the summer with a gain of $-1$ (via resistor $R$).
*   The input $V_{in}$ is also fed to the precision half-wave rectifier, which outputs $-V_{in}$ during positive cycles and $0\text{V}$ during negative cycles. This output is fed to the summer with a gain of $-2$ (via resistor $R/2$).
*   **Positive cycles:** Summer output $V_o = -[ 1(V_{in}) + 2(-V_{in}) ] = +V_{in}$.
*   **Negative cycles:** Summer output $V_o = -[ 1(-V_{in}) + 2(0) ] = +V_{in}$.
The output is the absolute value: $V_o = |V_{in}|$.

---

## 4. Self-Study Circuit 2: Log & Antilog Amplifiers
*[Appeared in: 2022 Q7(c), 2020 Q7(b)]*

### 4.1 Logarithmic Amplifier Derivation
An inverting op-amp configuration with a matched BJT placed in the feedback loop:

```
                     Q1 (BJT)
                   +--|<|---+ (Collector to Emitter)
                   |  C   E |
        Vin o-[ R ]+--o (-) |
                      |     |
        Gnd o--------(+)----+---o Vout
```

1.  By virtual ground, the inverting terminal voltage is $V_n \approx 0\text{V}$.
2.  Input current flowing through resistor $R$:
    $$I_{in} = \frac{V_{in} - 0}{R} = \frac{V_{in}}{R}$$
3.  Since the op-amp has infinite input impedance, all of $I_{in}$ must flow into the BJT's collector:
    $$I_C = I_{in} = \frac{V_{in}}{R}$$
4.  The BJT collector current is exponentially related to its base-emitter voltage:
    $$I_C = I_s e^{V_{BE} / V_T}$$
    where $I_s$ is the reverse saturation current and $V_T \approx 26\text{ mV}$ at room temperature.
5.  Since the base is grounded ($V_B = 0\text{V}$) and the emitter is tied to the output ($V_E = V_{out}$):
    $$V_{BE} = V_B - V_E = -V_{out}$$
6.  Substitute this expression into the BJT current equation:
    $$I_C = I_s e^{-V_{out} / V_T} \Rightarrow \frac{V_{in}}{R} = I_s e^{-V_{out} / V_T} \Rightarrow \frac{V_{in}}{I_s R} = e^{-V_{out} / V_T}$$
7.  Take the natural logarithm of both sides:
    $$\ln \left( \frac{V_{in}}{I_s R} \right) = -\frac{V_{out}}{V_T} \Rightarrow V_{out} = -V_T \ln \left( \frac{V_{in}}{I_s R} \right)$$
The output voltage is proportional to the natural logarithm of the input voltage.

---

### 4.2 Antilogarithmic Amplifier
Placing the BJT at the input and the resistor $R$ in the feedback loop reverses the mathematical operation:
$$I_C = I_s e^{V_{in} / V_T} \quad \text{and} \quad V_{out} = -I_C R = -R I_s e^{V_{in} / V_T}$$
The output is exponentially proportional to the input voltage.

---

## 5. Self-Study Circuit 3: Negative Impedance Converter (NIC)
*[Appeared in: 2023 Q6(b), 2019 Q5(a)]*

An NIC is an active op-amp configuration that simulates a negative resistance:

```
                    R2
               +---[  ]---+
               |          |
        Vi o--(+)--[ Av ]-+---o Vo
               |          |
               +---[  ]---+
                    R1
```

**Mathematical Proof of Negative Input Impedance ($Z_{in}$):**
1.  Assume $R_1 = R_2$. The feedback network to the inverting input is a voltage divider:
    $$V_- = V_{out} \left( \frac{R_1}{R_1 + R_2} \right) = \frac{V_{out}}{2}$$
2.  By the virtual short principle:
    $$V_- = V_+ \Rightarrow V_{in} = \frac{V_{out}}{2} \Rightarrow V_{out} = 2 V_{in}$$
3.  A positive feedback resistor $R$ is connected between the non-inverting input ($V_{in}$) and the output ($V_{out}$). The current $I_{in}$ flowing into the input terminal is:
    $$I_{in} = \frac{V_{in} - V_{out}}{R}$$
4.  Substitute $V_{out} = 2 V_{in}$:
    $$I_{in} = \frac{V_{in} - 2 V_{in}}{R} = -\frac{V_{in}}{R}$$
5.  The apparent input impedance is:
    $$Z_{in} = \frac{V_{in}}{I_{in}} = -R$$
The circuit acts as a negative resistor, pushing current back into the signal source.

---

## 6. Self-Study Circuit 4: Schmitt Trigger Threshold Design

### 6.1 Comparator Chattering and Hysteresis Solution
*[Appeared in: 2019 Q4(c), 2018 Q4(c)]*

*   **Chattering:** When a noisy input signal slowly passes through a single comparator threshold voltage, noise spikes will cause the signal to cross the threshold multiple times. The output chatters rapidly between states, introducing false triggering.
*   **Schmitt Trigger Solution:** Employs positive feedback to establish two separate thresholds: Upper Trigger Point ($V_{UT}$) and Lower Trigger Point ($V_{LT}$). When the rising input crosses $V_{UT}$, the output switches states and the threshold instantly drops to $V_{LT}$. Noise spikes cannot cross this new, lower threshold, keeping the output stable. The input must fall below $V_{LT}$ to switch back.

---

### 6.2 Worked Schmitt Trigger Design
*[Appeared in: 2020 Q8(c)]*

**Problem Details:**
Design an inverting Schmitt trigger with $V_{UT} = 7\text{ V}$, $V_{LT} = 3\text{ V}$. Assume saturation voltage $V_{sat} = 14\text{ V}$.

#### Step-by-Step Solution:

##### Step 1: Write the threshold equations
For an inverting Schmitt trigger biased with a reference voltage $V_{ref}$:
$$V_{UT} = V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) + V_{sat} \left( \frac{R_1}{R_1 + R_F} \right) = 7\text{ V} \quad \text{--- (Eq. 1)}$$
$$V_{LT} = V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) - V_{sat} \left( \frac{R_1}{R_1 + R_F} \right) = 3\text{ V} \quad \text{--- (Eq. 2)}$$

##### Step 2: Solve for resistor ratio ($R_F / R_1$)
Subtract Equation 2 from Equation 1:
$$2 V_{sat} \left( \frac{R_1}{R_1 + R_F} \right) = 4\text{ V} \Rightarrow 2(14) \left( \frac{R_1}{R_1 + R_F} \right) = 4 \Rightarrow \frac{R_1}{R_1 + R_F} = \frac{4}{28} = \frac{1}{7}$$
$$7 R_1 = R_1 + R_F \Rightarrow R_F = 6 R_1$$
Choose $R_1 = 10\text{ k}\Omega$ as a standard design value:
$$R_F = 6 \times 10\text{ k}\Omega = 60\text{ k}\Omega$$

##### Step 3: Solve for reference voltage ($V_{ref}$)
Add Equation 1 and Equation 2:
$$2 V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) = 10\text{ V} \Rightarrow V_{ref} \left( \frac{R_F}{R_1 + R_F} \right) = 5\text{ V}$$
Substitute $R_F = 6 R_1$:
$$V_{ref} \left( \frac{6 R_1}{7 R_1} \right) = 5\text{ V} \Rightarrow V_{ref} \left( \frac{6}{7} \right) = 5 \Rightarrow V_{ref} = \frac{35}{6} \approx 5.83\text{ V}$$

---

## 7. Sensor Systems: 3-Op-Amp Instrumentation Amplifier
*[Appeared in: 2020 Q2(c)]*

Used to amplify small differential sensor signals in high-noise industrial environments:

```
        V1 o----(+)---\           R
                      [ Av1 ]-o--[ ]---\
        Gnd o---[Rg]--/                |
                 |                     |----(+)---\
                 +-----------------\   |          [ Av3 ]---o Vout
                 |                 |   |----(-)--/
        Gnd o---[Rg]--\                |
                      [ Av2 ]-o--[ ]---/
        V2 o----(+)---/           R
```

*   **Input Stage (Buffers):** Op-Amps $A_1$ and $A_2$ act as high input impedance buffers with a differential gain determined by a single gain resistor $R_g$:
    $$V_{o2} - V_{o1} = \left( 1 + \frac{2 R}{R_g} \right) (V_2 - V_1)$$
*   **Differential Stage:** Op-Amp $A_3$ is a standard differential stage with gain $R_f / R$. It rejects common-mode noise and provides single-ended output:
    $$V_{out} = \left( \frac{R_f}{R} \right) (V_{o2} - V_{o1}) = \left( \frac{R_f}{R} \right) \left( 1 + \frac{2 R}{R_g} \right) (V_2 - V_1)$$
*   **Benefit:** The extremely high CMRR isolates small sensor readings from large common-mode electrical noise.
