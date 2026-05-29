# Class Note Digitization - Phase 11 (Part 2, Pages 44-53)

---

## Page 44: Analog_Class_Note_Part-2-044.png

### Content

#### Derivation of Closed-Loop Gain for Voltage Feedback Configurations:

#### 1. Voltage-Series Feedback Gain ($A_f$):
Feedback loop equations:
$$v_{id} = v_s - v_f \quad \text{and} \quad v_f = \beta v_o$$
$$v_o = A v_{id} = A(v_s - v_f) = A(v_s - \beta v_o)$$
$$v_o (1 + \beta A) = A v_s$$
$$\therefore \boxed{A_f = \frac{v_o}{v_s} = \frac{A}{1 + \beta A}}$$

---

#### 2. Voltage-Shunt Feedback Gain ($A_f$):
Feedback loop equations:
$$i_{id} = i_s - i_f \quad \text{and} \quad i_f = \beta v_o \quad (\text{where } \beta = -\frac{1}{R_f})$$
$$v_o = Z_t i_{id} = Z_t (i_s - \beta v_o)$$
$$v_o(1 + \beta Z_t) = Z_t i_s$$
$$\therefore \boxed{A_f = \frac{v_o}{i_s} = \frac{Z_t}{1 + \beta Z_t}}$$

---

## Page 45: Analog_Class_Note_Part-2-045.png

### Metadata
- **Date**: 20 April, 2026
- **Course**: ECE-2105 (Analog-2)
- **Instructor**: MJR Sir
- **Topic**: Input Impedance with Feedback

### Content

#### 1. Voltage-Series Feedback Input Impedance ($Z_{if}$):
```
           Source Loop                          Amplifier Model
    I_i    ---[ Z_i ]---*                   +---[ Z_o ]---*--- v_o
  v_s (~)               |                   |             |
           ---[ Z_f ]---*              (~) A * v_id      [R_L]
                                            |             |
                                           ===           ===
                                           GND           GND
```
* **KVL around input loop:**
  $$I_i = \frac{v_{id}}{Z_i} = \frac{v_s - v_f}{Z_i} = \frac{v_s - \beta v_o}{Z_i}$$
  $$I_i Z_i = v_s - \beta (A v_{id}) = v_s - \beta A (I_i Z_i)$$
  $$v_s = I_i Z_i + \beta A I_i Z_i = I_i Z_i (1 + \beta A)$$
  $$\therefore \boxed{Z_{if} = \frac{v_s}{I_i} = Z_i(1 + \beta A)}$$
  *(Note: Voltage-series feedback increases the input impedance by a factor of $(1+\beta A)$).*

---

#### 2. Voltage-Shunt Feedback Input Impedance ($Z_{if}$):
$$\therefore \boxed{Z_{if} = \frac{Z_i}{1 + \beta A}}$$
*(Note: Shunt mixing feedback decreases input impedance).*

---

## Page 46: Analog_Class_Note_Part-2-046.png

### Content

#### Output Impedance with Feedback ($Z_{of}$): Voltage-Series Case
To find output impedance, short the independent source ($v_s = 0$) and apply an external testing source $V$ at the output terminals, driving a current $I$:

```
               Input Loop                       Output Testing Model
            ---[ Z_i ]---*              I   +---[ Z_o ]---*--- (+)
                         |   <---------------+            |
                        ===                  |           (~) V (External source)
                        GND             (~) A * v_id      |
                                             |           (-)
                                            ===
                                            GND
```
* **Analysis:**
  Since $v_s = 0 \Rightarrow v_{id} = -v_f = -\beta V$.
  Applying KVL to the output loop:
  $$V = I Z_o + A v_{id} = I Z_o - A \beta V$$
  $$V (1 + \beta A) = I Z_o$$
  $$\therefore \boxed{Z_{of} = \frac{V}{I} = \frac{Z_o}{1 + \beta A}}$$
  *(Note: Voltage sampling feedback decreases the output impedance).*

---

#### Output Impedance for Current-Series Feedback:
$$\therefore \boxed{Z_{of} = Z_o(1 + \beta A)}$$
*(Note: Current sampling feedback increases the output impedance).*
* **Self-Study:** Look at Boylestad Table 14.1 & 14.2 for comprehensive feedback parameter comparisons.

---

## Page 47: Analog_Class_Note_Part-2-047.png

### Practical Voltage-Series Feedback JFET Circuit

```
                          +V_DD
                            |
                           [RD]
                            |
                 C_c        |
        v_s ----||----*-----*--------- Output (v_o)
                      |     |
                    [R1]   [Ro]
                      |     |
                      *-----+
                      |
                    [R2]
                      |
                     ===
                     GND
```

#### 1. AC Gain Without Feedback ($A$):
$$A = -g_m R_L$$
where:
$$R_L = R_o \parallel R_D \parallel (R_1 + R_2) \approx R_o \parallel R_D$$

#### 2. Feedback Factor ($\beta$):
$$v_f = \left( \frac{-R_2}{R_1 + R_2} \right) v_o \Rightarrow \boxed{\beta = \frac{v_f}{v_o} = -\frac{R_2}{R_1 + R_2}}$$

#### 3. Closed-Loop Gain ($A_f$):
$$A_f = \frac{A}{1 + \beta A} = \frac{-g_m R_L}{1 + g_m R_L \left( \frac{R_2}{R_1 + R_2} \right)}$$

---

## Page 48: Analog_Class_Note_Part-2-048.png

### Content

#### Closed-loop Gain Simplification:
If loop gain is very large ($\beta A \gg 1$):
$$A_f \approx \frac{1}{\beta} = -\left( \frac{R_1 + R_2}{R_2} \right)$$

---

#### JFET Voltage-Series Design Problem (Ex 14.3):
* **Given Parameters:**
  * $R_1 = 80\ \Omega$, $R_2 = 20\text{ k}\Omega$, $R_o = 10\text{ k}\Omega$, $R_D = 10\text{ k}\Omega$, $g_m = 4000\ \mu\text{S}$.
* **Calculate:** $R_L$, gain without feedback $A$, feedback factor $\beta$, and closed-loop gain $A_f$.
* **Solution:**
  $$R_L = R_o \parallel R_D = 10\text{ k}\Omega \parallel 10\text{ k}\Omega = 5\text{ k}\Omega$$
  $$A = -g_m R_L = -4000\ \mu\text{S} \times 5\text{ k}\Omega = -20$$
  $$\beta = -\frac{R_1}{R_1 + R_2} = -\frac{80\ \Omega}{80\ \Omega + 20\text{ k}\Omega} = -0.00398$$
  $$A_f = \frac{A}{1 + \beta A} = \frac{-20}{1 + (-0.00398 \times -20)} = \frac{-20}{1 + 0.0796} = -18.52$$
* **Self-Study Assignments:** Boylestad Example 14.4 & 14.5.

---

### Practical Voltage-Shunt Feedback JFET Circuit
* **Feedback Configuration:** Resistor $R_f$ connected from Drain (output) directly back to the Gate (input).
* **Gain Without Feedback ($A$):**
  $$A = -g_m R_D R_s$$

---

## Page 49: Analog_Class_Note_Part-2-049.png

### Content

#### Voltage-Shunt Feedback Analysis (Ex 14.6):
* **Feedback Current ($I_f$):**
  $$I_f = -\frac{V_o}{R_f}$$
* **Feedback Factor ($\beta$):**
  $$\beta = \frac{I_f}{V_o} = -\frac{1}{R_f}$$
* **Closed-loop Gain (Transresistance):**
  $$A_f = \frac{V_o}{I_s} = \frac{A}{1 + \beta A}$$
* **Closed-loop Voltage Gain ($A_{vf}$):**
  $$A_{vf} = \frac{V_o}{V_s} = \frac{V_o}{I_s \cdot R_s} = \frac{A_f}{R_s}$$

---

#### Active Arithmetic Circuits Design:
* **Question:** Design an active circuit to compute:
  $$v_o = 2 V_1 - 3 V_2$$
  *(Note: Must implement using inverting summing and cascading inverting topologies).*

```
           V_1 ----- [ R_1 ] -----+
                                  |
   V_2 ---> [ Inverter ] - [ R_2 ]--*---> [ Inverting Summing Amp ] ---> [ Inverter ] ---> Output (v_o)
```
* **Mathematical Proof:**
  * Inverter Stage for $V_2$: Output $= -V_2$.
  * Summing Stage: Output $V_o' = -\left( \frac{R_f}{R_1} V_1 + \frac{R_f}{R_2} (-V_2) \right) = -\left( 2 V_1 - 3 V_2 \right)$
    *(where we select $R_f = 6\text{ k}\Omega$, $R_1 = 3\text{ k}\Omega$, $R_2 = 2\text{ k}\Omega$)*.
  * Final Inverter Stage: Output $v_o = -V_o' = 2 V_1 - 3 V_2$.

---

## Page 50: Analog_Class_Note_Part-2-050.png

### Metadata
- **Date**: 21 April, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: Mohsin Sir
- **Topic**: MOS Field-Effect Transistors (MOSFETs)

### Content
* MOSFET configurations:
  * **n-MOS:** Positive voltage at the Gate turns the transistor ON.
  * **p-MOS:** Negative voltage at the Gate turns the transistor ON.

#### Physical Cross-Section of n-MOS Transistor
```
                       Gate (G)
                          |
                   +------+------+
                   |    Metal    |
                   +-------------+
                   |    Oxide    |
       Drain (D) --+-------------+-- Source (S)
       (n+ region) |   Channel   |  (n+ region)
                   +-------------+
                   | p-substrate |
                   +-------------+
                          |
                      Substrate
```
* **CMOS (Complementary MOS):** Created by combining matching pairs of p-MOS and n-MOS transistors on a single silicon substrate.

---

## Page 51: Analog_Class_Note_Part-2-051.png

### CMOS Logic Implementation

#### CMOS Design Rules:
1. One logic input variable requires exactly **1 p-MOS** and **1 n-MOS** transistor.
2. Two logic input variables require **2 p-MOS** and **2 n-MOS** transistors.

---

#### 1. CMOS Inverter Circuit
```
                         +V_DD
                           |
                     +-----*-----+
                     |           |
               A ----*--- [ p-MOS ]
                     |   (Pull-up)
                     |     |
                     |     +----------- Output (Y)
                     |     |
               A ----*--- [ n-MOS ]
                         (Pull-down)
                           |
                          ===
                          GND
```
* **Truth Table:**

| Input (A) | p-MOS | n-MOS | Output (Y) |
| :-: | :-: | :-: | :-: |
| **0** | **ON** | **OFF** | **1** ($V_{DD}$) |
| **1** | **OFF** | **ON** | **0** (Ground) |

---

#### 2. CMOS NOR Gate Circuit
```
                         +V_DD
                           |
                         [p-MOS A]
                           |
                         [p-MOS B]
                           |
               +-----------*----------- Output (Y)
               |                       |
           [n-MOS A]               [n-MOS B]
           (Parallel)              (Parallel)
               |                       |
              ===                     ===
              GND                     GND
```
* **Logic Function:** $Y = \overline{A + B}$
  * Series pull-up path (p-MOS) conducts only when both $A = 0$ and $B = 0 \Rightarrow Y = 1$.
  * Parallel pull-down path (n-MOS) conducts when either $A = 1$ or $B = 1 \Rightarrow Y = 0$.

---

## Page 52: Analog_Class_Note_Part-2-052.png

### CMOS OR Gate Implementation
To implement a CMOS OR gate, cascade a CMOS NOR gate stage with a CMOS Inverter stage:
```
  Inputs A, B ---> [ CMOS NOR Gate Stage ] ---> [ CMOS Inverter Stage ] ---> Output Y
```

---

### Midterm Exam Study Guide & Syllabus:
1. **Multistage Amplifiers:** Boylestad Chapter 9 (Part A).
2. **Operational Amplifiers (Op-Amps):** Sadiku Chapter 5 / Boylestad Chapter 10 (Part B).
3. **Feedback & 555 Timers:** Mixed textbooks (Part C).

---

### Inverting Summing Amplifier
```
        R1
  V1 --[===]--*
        R2    |
  V2 --[===]--*----------- (-) \
        R3    |                 \
  V3 --[===]--*           [Rf]   \-------- Output (V_o)
              |      +----[===]--/
             ===     |    |     /
             GND     |   ===
                     |   GND
                     +----+
```
* **Closed-loop Output Voltage:**
  $$\boxed{v_o = -\left( \frac{R_f}{R_1} V_1 + \frac{R_f}{R_2} V_2 + \frac{R_f}{R_3} V_3 \right)}$$
* Derived using the virtual ground principle and Superposition Theorem.

---

## Page 53: Analog_Class_Note_Part-2-053.png

### Content

#### 1. Non-Inverting Summing Amplifier
```
        R1
  V1 --[===]--*
        R2    |
  V2 --[===]--*----------- (+) \
              |                 \
             ===           [Rf]  \-------- Output (V_o)
             GND     +----[===]--/
                     |    |     /
                     |   [R1']
                     |    |
                     |   ===
                     |   GND
                     +----+
```
* **Derivation using Superposition at $(+)$ node ($V_p$):**
  * If $V_2 = 0 \Rightarrow V_{p1} = \left( \frac{R_2}{R_1 + R_2} \right) V_1$
  * If $V_1 = 0 \Rightarrow V_{p2} = \left( \frac{R_1}{R_1 + R_2} \right) V_2$
  * Total $V_p = V_{p1} + V_{p2} = \frac{R_2 V_1 + R_1 V_2}{R_1 + R_2}$.
  * Overall Output Voltage:
    $$\boxed{v_o = \left( 1 + \frac{R_f}{R_1'} \right) V_p}$$

---

#### 2. Dual-Input Differential Amplifier Topology:
* Apply Superposition: analyze the inverting gain path (input $V_1$) and non-inverting gain path (input $V_2$) independently, then sum the output voltages.

---

#### 3. Parameter Design Practice Problem:
```
           R1 = 5k
  V_1 ----[===]-----*---- (-) \
                    |          \
                  [ R_f ]       \------- Output (v_o = 5V max)
                    |     (+)  /
                    +----- |  /
                           | /
```
* **Given Parameters:**
  * Feedback current $I_f = 5\text{ mA}$ (flowing from output to inverting node).
  * Input resistor $R_1 = 5\text{ k}\Omega$.
  * Max output voltage $v_o = 5\text{ V}$.
* **Calculate:** $R_f$, $I_1$, and $R_1$ loop parameters.
* **Solution:**
  * Virtual Ground at $(-)$ node: $V_n = V_p = 0\text{ V}$.
  * Current entering op-amp terminal is $I_n = 0\text{ A}$.
  * By KCL: $I_1 = I_f = 5\text{ mA}$.
  * Voltage across $R_1$: $V_{R1} = I_1 R_1 = 5\text{ mA} \times 5\text{ k}\Omega = 25\text{ V}$.
  * Feedback Resistor: $R_f = \frac{V_n - v_o}{I_f} = \frac{0\text{ V} - 5\text{ V}}{5\text{ mA}} = -1\text{ k}\Omega$ (absolute value $1\text{ k}\Omega$ for magnitude analysis).
