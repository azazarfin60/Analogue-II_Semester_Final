# Class Note Digitization - Phase 10 (Part 2, Pages 34-43)

---

## Page 34: Analog_Class_Note_Part-2-034.png

### Metadata
- **Date**: 4 April, 2026
- **Course**: ECE-2105 (Analog)
- **Instructor**: M.R. Sir
- **Topic**: Introduction to 555 Timer

### Content
* The 555 timer is a highly versatile, monolithic integrated circuit designed to generate precise time delays or stable free-running oscillations (multivibrators).

#### Applications of the 555 Timer:
1. Precise Oscillators (Astable / Monostable)
2. Frequency Division
3. Alarm & Siren Generators
4. Linear Voltage Ramp Generators / Time Delays

#### Pin Configuration (8-Pin DIP Layout):
* **Pin 1 (GND):** Ground connection.
* **Pin 2 (Trigger):** Initiates timing transition.
* **Pin 3 (Output):** High/Low square pulse output.
* **Pin 4 (Reset):** Resets the timer operation (Active-low).
* **Pin 5 (Control Voltage):** Direct access to internal $\frac{2}{3}V_{CC}$ threshold node.
* **Pin 6 (Threshold):** Pin voltage compared against internal upper threshold.
* **Pin 7 (Discharge):** Connected to internal NPN discharge transistor collector.
* **Pin 8 ($+V_{CC}$):** Positive DC supply voltage.

---

## Page 35: Analog_Class_Note_Part-2-035.png

### Internal Block Diagram of the 555 Timer

```
                         Pin 8 (+V_CC)
                            |
                           [R] (5k)
                            |
           Node A ----------*-------- [ Pin 5 ] (Control Voltage)
         (2/3 V_CC)         |
                            | \ (Inverting)
                            |  \ Comparator 1
             [ Pin 6 ] ----+    \---------------+
            (Threshold)    | (+) /              |
                           |    /               |
                           |  /                 v (Reset)
                          [R] (5k)          +-------+
                           |                |       |------ [Pin 3] (Output)
           Node B ---------*                |  S-R  |
         (1/3 V_CC)         |               | Flip  |
                            | \ (Non-inv.)  | Flop  |
                            |  \ Comparator 2       |
             [ Pin 2 ] ----+    \---------------+------ [Discharge Transistor Q1]
             (Trigger)     | (-) /              |          (Base)
                           |    /            Q  |
                           |  /             === |
                          [R] (5k)          GND |
                           |                    |
                          ===                 =====
                          GND                  GND
```

#### Flip-Flop Logic & Operations:
* **SR Flip-Flop Truth Table:**

| S | R | $Q_n$ | $Q_{n+1}$ (Next State) |
| :-: | :-: | :-: | :-: |
| **0** | **0** | $0/1$ | No Change (Hold) |
| **0** | **1** | $0/1$ | **0** (Reset State) |
| **1** | **0** | $0/1$ | **1** (Set State) |
| **1** | **1** | $0/1$ | Forbidden State |

#### Threshold & Trigger Activation Rules:
1. **Comparator 1 (Pin 6 - Threshold):**
   * If Threshold Voltage $> \frac{2}{3} V_{CC} \Rightarrow$ Comparator 1 Output goes High $\Rightarrow$ Resets flip-flop ($R=1$) $\Rightarrow$ Output (Pin 3) goes Low.
2. **Comparator 2 (Pin 2 - Trigger):**
   * If Trigger Voltage $< \frac{1}{3} V_{CC} \Rightarrow$ Comparator 2 Output goes High $\Rightarrow$ Sets flip-flop ($S=1$) $\Rightarrow$ Output (Pin 3) goes High.

---

## Page 36: Analog_Class_Note_Part-2-036.png

### Monostable Multivibrator (One-Shot Generator)

```
                            +V_CC
                              |
                 +------------*----------+
                 |                       |
                [R1]                     |
                 |                       |
                 +-----------*-----------*----- [ Pin 4 ] (Reset)
                 |           |           |
                 |       +---+---+       |
                 |       | Pin 7 |-------|----- [ Pin 8 ] (+V_CC)
                 |       +-------+       |
                 |           |           |
                 +-----------*-----------*----- [ Pin 6 ] (Threshold)
                 |           |
               [C1]          | (Internal Q1 Collector Connection)
                 |          ===
                ===         GND
                GND
```
* **Bengali Explanatory Note:** $Q_1$ ON হলে capacitor charge হতে পারবে না (discharge হয়ে থাকবে)। (When internal discharge transistor $Q_1$ is ON, the capacitor $C_1$ is shorted to ground and cannot charge).

#### Comparator Threshold Summary:
* $+V_{\text{sat}} \Rightarrow \text{Logic } 1$
* $-V_{\text{sat}} \Rightarrow \text{Logic } 0$
* Inverting terminal voltage is higher $\Rightarrow \text{Output } 0$
* Non-inverting terminal voltage is higher $\Rightarrow \text{Output } 1$

#### Pulse Width Derivation ($T$):
The capacitor charges from $0\text{ V}$ towards $V_{CC}$ via $R_1$:
$$v_c(t) = V_{CC} \left( 1 - e^{-t / R_1 C_1} \right)$$
The output remains High until $v_c(t)$ reaches the upper threshold $\frac{2}{3} V_{CC}$:
$$\frac{2}{3} V_{CC} = V_{CC} \left( 1 - e^{-T / R_1 C_1} \right)$$
$$\frac{2}{3} = 1 - e^{-T / R_1 C_1} \Rightarrow e^{-T / R_1 C_1} = \frac{1}{3}$$
$$-T / R_1 C_1 = \ln(1/3) \Rightarrow T = R_1 C_1 \ln(3)$$
$$\therefore \boxed{T = 1.1 R_1 C_1}$$

---

## Page 37: Analog_Class_Note_Part-2-037.png

### Frequency Division using Monostable Multivibrator
* By applying a periodic trigger input with period $T$, and adjusting the monostable pulse width $t_p$ to span across multiple input periods, the circuit divides down the input frequency:
  * If $t_p > T \Rightarrow f_{\text{out}} = \frac{f_{\text{in}}}{2}$
  * If $t_p > 2T \Rightarrow f_{\text{out}} = \frac{f_{\text{in}}}{3}$
  * If $t_p > 3T \Rightarrow f_{\text{out}} = \frac{f_{\text{in}}}{4}$
* **General Condition:**
  $$\boxed{t_p > (n-1)T}$$

---

### Monostable Operating Principles (Summary)
* In the stable standby state, the timer output is Low (0).
* When an external negative-going trigger pulse ($< \frac{1}{3} V_{CC}$) is applied to Pin 2, the internal flip-flop is set, turning OFF the discharge transistor $Q_1$. This allows the external capacitor $C_1$ to begin charging towards $V_{CC}$ through resistor $R_1$.
* Once the capacitor voltage reaches $\frac{2}{3} V_{CC}$, Comparator 1 resets the flip-flop, which turns the discharge transistor $Q_1$ back ON, immediately discharging the capacitor to ground and pulling the output Low.

---

## Page 38: Analog_Class_Note_Part-2-038.png
*(Note: This page is an exact duplicate scan of Page 37 in the manuscript. All text, tables, and schematics are identical).*

---

## Page 39: Analog_Class_Note_Part-2-039.png

### Astable Multivibrator (Free-Running Square Wave Generator)

```
                            +V_CC
                              |
                 +------------*----------+
                 |                       |
                [R1]                     |
                 |                       |
                 +-----------*-----------*----- [ Pin 4 ] (Reset)
                 |           |           |
                 |       +---+---+       |
                 |       | Pin 7 |-------|----- [ Pin 8 ] (+V_CC)
                 |       +-------+       |
                 |           |           |
                [R2]         | (Internal Q1 Collector Connection)
                 |           |
                 +-----------*-----------*----- [ Pin 6 ] (Threshold)
                 |           |
                 *-----------|----------------- [ Pin 2 ] (Trigger)
                 |           |
               [ C ]        ===
                 |          GND
                ===
                GND
```

#### Detailed Operations & Waveforms:
1. Capacitor $C$ charges exponentially through $R_1 + R_2$ towards $+V_{CC}$ when the output is High.
2. The charging time ($t_1$) is the interval for the capacitor to charge from $\frac{1}{3}V_{CC}$ to $\frac{2}{3}V_{CC}$:
   $$t_1 = 0.693 (R_1 + R_2) C$$
3. Once $v_c$ reaches $\frac{2}{3}V_{CC}$, Comparator 1 resets the flip-flop, forcing Pin 3 Low and turning ON the discharge transistor $Q_1$.
4. The capacitor then discharges from $\frac{2}{3}V_{CC}$ down to $\frac{1}{3}V_{CC}$ through resistor $R_2$ into Pin 7.
5. The discharging time ($t_2$) is:
   $$t_2 = 0.693 R_2 C$$
6. Total Time Period ($T$):
   $$\boxed{T = t_1 + t_2 = 0.693 (R_1 + 2 R_2) C}$$

---

## Page 40: Analog_Class_Note_Part-2-040.png

### Content

#### Duty Cycle Analysis:
$$D = \frac{t_1}{T} = \frac{R_1 + R_2}{R_1 + 2 R_2}$$
* **Symmetric limitation:** Since $R_1$ cannot be zero (to prevent shorting Vcc to GND during discharge), the duty cycle of a standard astable circuit is always strictly greater than 50%:
  $$\boxed{D > 50\%}$$

---

#### Modified Astable Multivibrator for Variable Duty Cycle ($D \le 50\%$)
```
                            +V_CC
                              |
                 +------------*
                 |            |
                [R1]          |
                 |            |
                 *-----+      |
                 |     |      |
                 |    [D]     |
                 |   (Diode)  |
                 |     |      |
                 *-----+------*----- [ Pin 7 ] (Discharge)
                 |            |
                [R2]          |
                 |            |
                 *------------*----- [ Pin 6 ] (Threshold)
                 |            |
                 *------------|----- [ Pin 2 ] (Trigger)
                 |            |
               [ C ]         ===
                 |           GND
                ===
                GND
```
* **Charging path:** Through $R_1$ and forward-biased diode $D$ directly to capacitor $C$ (bypassing $R_2$).
  $$t_1 = 0.693 R_1 C$$
* **Discharging path:** Through $R_2$ and the internal discharge transistor to Ground.
  $$t_2 = 0.693 R_2 C$$
* **Duty Cycle control:**
  $$D = \frac{R_1}{R_1 + R_2}$$
  By setting $R_1 = R_2$, a perfect $50\%$ duty cycle is obtained.

---

## Page 41: Analog_Class_Note_Part-2-041.png

### Feedback Amplifiers

#### Classifications of Feedback:
1. **Positive Feedback (Regenerative):** Input signal and feedback signal are in-phase ($0^\circ$). Used in oscillators.
2. **Negative Feedback (Degenerative):** Input signal and feedback signal are out-of-phase ($180^\circ$). Used in stabilized amplifiers.

#### Block Diagram: Closed-Loop Feedback System
```
            + (Sum/Diff) Node
  Input ---> O ----(v_id)---> [ Amplifier ] --------*----> Output (v_o)
   (v_i)     ^                  (Gain A)            |
             |                                      |
             +----------- [ Feedback ] <------------+
                              (Beta)
```

#### Derivation of Closed-Loop Gain ($A_f$):
Let $v_{id}$ be the differential input:
$$v_{id} = v_i - v_f \quad \text{(Negative Feedback Case)}$$
$$v_o = A v_{id} = A (v_i - \beta v_o)$$
$$v_o (1 + A \beta) = A v_i$$
$$\therefore \boxed{A_f = \frac{v_o}{v_i} = \frac{A}{1 + A \beta}}$$
For the general case (Positive and Negative Feedback):
$$\boxed{A_f = \frac{A}{1 \pm A \beta}}$$

---

## Page 42: Analog_Class_Note_Part-2-042.png

### Content

#### Effects of Negative Feedback on Amplifier Performance:
1. **Gain Reduction:** Reduces gain by factor of $(1 + A\beta)$.
2. **Gain Stabilization:** The gain becomes less dependent on internal parameters:
   $$A_f \approx \frac{1}{\beta} \quad (\text{if } A\beta \gg 1)$$
3. **Bandwidth Extension:**
   $$\boxed{BW_f = BW(1 + A\beta)}$$
   * Cutoff frequencies shift:
     $$f_{1f} = \frac{f_1}{1 + A\beta} \quad ; \quad f_{2f} = f_2(1 + A\beta)$$

```
   Voltage Gain
     ^
  A  +--------.               (Without Feedback: High Gain, Narrow BW)
     |         \
  Af +-----------.            (With Negative Feedback: Low Gain, Wide BW)
     |           | \
     +---+---+---+--+--------> Frequency
        f1f f1  f2 f2f
```

---

#### Feedback Mixing Configurations (Input Side):
* **Series Mixing:** Voltage addition at input ($v_{in} = v_s - v_f$).
* **Shunt Mixing:** Current addition at input ($i_{in} = i_s - i_f$).

---

## Page 43: Analog_Class_Note_Part-2-043.png

### Feedback Sampling Configurations (Output Side)
1. **Voltage Sampling (Parallel Connection):** Feedback network connected in parallel with output terminals. Samples voltage $v_o$.
2. **Current Sampling (Series Connection):** Feedback network connected in series with load. Samples output current $i_o$.

---

### Four Fundamental Feedback Topologies:

#### 1. Voltage-Series Feedback:
```
           Source Voltage (v_s)                     Voltage Sampling (Vo)
            v_s --- (+) Node ---> [ Amplifier ] --------*--- v_o
                     ^               (A_v)              |
                     |                                 [R_L]
                     +--------- [ Feedback ] <----------*
                                   (Beta)
```
* **Closed-loop Gain:**
  $$A_{vf} = \frac{v_o}{v_s} = \frac{A_v}{1 + A_v \beta}$$

#### 2. Voltage-Shunt Feedback:
```
           Source Current (I_s)                     Voltage Sampling (Vo)
            I_s --- (+) Node ---> [ Amplifier ] --------*--- v_o
                     ^               (Z_t)              |
                     |                                 [R_L]
                     +--------- [ Feedback ] <----------*
                                   (Beta)
```
* **Closed-loop Gain (Transresistance):**
  $$A_{zf} = \frac{v_o}{I_s} = \frac{Z_t}{1 + Z_t \beta}$$
