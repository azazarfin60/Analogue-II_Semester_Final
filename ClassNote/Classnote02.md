# Class Note Digitization - Phase 2 (Pages 11 to 20)

---

## Page 11: Analog_Class_Note_Part-1-011.png

### Metadata
- **Date**: 15 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Common-Emitter Configuration (with Emitter Resistor $R_E$)

### Circuit Configurations

#### 1. Common-Emitter BJT Amplifier
```
             V_CC
              |
         +----+---------+
         |              |
        [R_B]         [R_C]
         |              |
   C1    |              +-------||---- Output (V_o)
  --||---+-- Base       |
  (V_i)  |  (NPN BJT)  / Q1
         |            |
         |             +----+
         |             |
        ===           [R_E]
        GND            |
                      ===
                      GND
```
* **Parameters**:
  * $I_i$: Input current entering before $C_1$.
  * $Z_i$: Input impedance looking into the base circuit after $C_1$.
  * $I_o$: Output current flowing down through collector resistor.
  * $Z_o$: Output impedance looking into the collector node.

---

#### 2. AC Equivalent Circuit (re model)
```
          Base (B)                       Collector (C)
  V_i      +---------+                      +------- V_o
  (AC)     |         |                      |
   |      [R_B]    [\beta r_e]    (\beta I_b) [R_C]
   |       |         |               |      |
   +-------+---------+               v      |
           |         | Emitter (E)   |      |
          ===        +---------------+------+
          GND        |
                    [R_E] (Current I_e)
                     |
                    ===
                    GND
```

### Derivations
* **Base Input Impedance ($Z_b$):**
  $$
  Z_b = \frac{V_i}{I_b}
  $$
  $$
  V_i = \beta r_e I_b + I_e R_E
  $$
  $$
  V_i = I_b \beta r_e + (\beta + 1) I_b R_E
  $$
  Since $\beta \gg 1$:
  $$
  V_i \approx I_b (\beta r_e + \beta R_E)
  $$
  $$
  \Rightarrow Z_b = \frac{V_i}{I_b} = \beta(r_e + R_E)
  $$

* **Total Input Impedance ($Z_i$):**
  $$
  Z_i = R_B \parallel Z_b = R_B \parallel \beta(r_e + R_E)
  $$

---

## Page 12: Analog_Class_Note_Part-1-012.png

### Metadata
- **Topic**: Darlington Configuration
- **Reference**: Boylestad Chapter 5 (fig 5.76)

### Circuit Configurations

#### 1. Darlington Pair Amplifier Circuit (Voltage Divider / Emitter Follower)
```
                  V_CC
                   |
         +---------+
         |         |
        [R_B]      | (Collectors connected)
         |         |
   C1    |       +---+
  --||---+-----> |   \ Q1
  (V_i)  |       |    |----+
         |        \   |    |
         |         +--+  Base (Q2)
         |         |     |
         |         |   +---+
         |         |   |   \ Q2
         |         |   |    |
         |         |    \   |
         |         |     +--+ Emitter (Q2)
         |         |     |
        ===       ===   [R_E]
        GND       GND    |
                        ===
                        GND
```

#### 2. AC Equivalent Circuit representation
```
          Input (B1)
           |
         [R_B]    (Z_i1)
           |        |
   V_i ----+--------+---- Base (Q1)
           |        |
          ===     [ Q1 ] (re model)
          GND       | (Emitter 1 / Base 2) (Z_i2)
                    +---- Base (Q2)
                    |
                  [ Q2 ] (re model)
                    | (Emitter 2)
                   [R_E]
                    |
                   ===
                   GND
```

### Derivations & Impedance Calculations
* **Input Impedance of Stage 2 ($Z_{i2}$):**
  $$
  Z_{i2} = \beta_2 (r_{e2} + R_E)
  $$
* **Input Impedance of Stage 1 ($Z_{i1}$):**
  $$
  Z_{i1} = \beta_1 (r_{e1} + Z_{i2})
  $$
  $$
  Z_{i1} = \beta_1 \{r_{e1} + \beta_2 (r_{e2} + R_E)\}
  $$
* **Approximations:**
  * Since $R_E \gg r_{e2}$:
    $$
    Z_{i1} \approx \beta_1 (r_{e1} + \beta_2 R_E)
    $$
  * Since $\beta_2 R_E \gg r_{e1}$:
    $$
    Z_{i1} \approx \beta_1 \beta_2 R_E
    $$
    $$
    \therefore Z_{i1} \approx \beta_D R_E \quad (\text{where } \beta_D = \beta_1 \beta_2)
    $$
* **Total Input Impedance ($Z_i$):**
  $$
  Z_i = R_B \parallel Z_{i1} \approx R_B \parallel \beta_D R_E
  $$

---

## Page 13: Analog_Class_Note_Part-1-013.png

### Metadata
- **Topic**: Darlington Configuration (Continued)
- **Sections**: AC Equivalent Circuit, Current Gain ($A_i$), and Voltage Gain ($A_v$)

### Detailed AC Equivalent Circuit (re model)
```
          B1                                Collectors
   I_i     +---------+-----------+----------------+ AC GND
  ----->   |         |           |                |
  (V_i)   [R_B]   [\beta_1 r_e1] |                |
           |         |           v (\beta_1 I_b1) |
   +-------+---------+-----------+                |
   |       |         | E1 / B2   |                |
  ===     ===        +-----------+                |
  GND     GND        |                            |
                     |                            |
                  [\beta_2 r_e2]                  |
                     |                            v (\beta_2 I_b2)
                     +----------------------------+
                     | E2
                    [R_E]  (Current I_o flows down)
                     |
                    ===
                    GND
```

### Derivations

#### 1. Current Gain ($A_i$)
* **Node Currents:**
  $$
  I_{b2} = I_{b1} + \beta_1 I_{b1} = (\beta_1 + 1) I_{b1}
  $$
  $$
  I_o = I_{b2} + \beta_2 I_{b2} = (\beta_2 + 1) I_{b2}
  $$
  $$
  \therefore I_o = (\beta_1 + 1)(\beta_2 + 1) I_{b1} \approx \beta_1 \beta_2 I_{b1} = \beta_D I_{b1}
  $$
* **Using Input Current Divider for $I_{b1}$:**
  $$
  I_{b1} = \frac{R_B}{R_B + Z_{i1}} I_i
  $$
  Since $Z_{i1} \approx \beta_D R_E$:
  $$
  I_o \approx \beta_D \left( \frac{R_B}{R_B + \beta_D R_E} \right) I_i
  $$
  $$
  \therefore A_i = \frac{I_o}{I_i} = \frac{\beta_D R_B}{R_B + \beta_D R_E}
  $$
  *(Note: There is a typo in the student's notebook where this current gain formula is labeled as $A_v$.)*

#### 2. Voltage Gain ($A_v$)
* **Equations:**
  $$
  V_o = I_o R_E
  $$
  $$
  V_i = I_i (R_B \parallel Z_{i1})
  $$
  $$
  A_v = \frac{V_o}{V_i} = \frac{I_o R_E}{I_i (R_B \parallel Z_{i1})} = A_i \frac{R_E}{R_B \parallel Z_{i1}}
  $$

---

## Page 14: Analog_Class_Note_Part-1-014.png

### Metadata
- **Topic**: Darlington Configuration Output Impedance ($Z_o$)
- **Reference**: Boylestad Chapter 5 (fig 5.82)

### AC Equivalent Circuit for $Z_o$ (Input Grounded, Test Voltage $V_o$ Applied at Emitter)
```
          B1 (AC GND)                        Collectors
           |                                  |
           +---------+-----------+------------+ (AC GND)
           |         |           |
        (\beta_1 I_b1|           |
           ^         |           |
           |      [\beta_1 r_e1] |
           +---------+-----------+
                     | E1 / B2
                     +-----------+
                     |           |
                  [\beta_2 r_e2] |
                     |           v (\beta_2 I_b2)
                     +-----------+
                     | E2 (Output Node)
                    [R_E]  <------- Current I_o enters
                     |      V_o
                    ===
                    GND
```

### Derivations

* **KCL at Output Node (Emitter 2):**
  $$
  I_o = \frac{V_o}{R_E} - I_{e2}
  $$
  Since currents flow in reverse:
  $$
  I_{e2} = - (I_{b2} + \beta_2 I_{b2}) = - (\beta_2 + 1) I_{b2}
  $$
  $$
  I_{b2} = - (\beta_1 + 1) I_{b1}
  $$

* **KVL from Output to Ground:**
  $$
  V_o = \beta_1 r_{e1} I_{b1} + \beta_2 r_{e2} I_{b2}
  $$
  $$
  V_o = \beta_1 r_{e1} I_{b1} + \beta_2 (\beta_1 + 1) r_{e2} I_{b1}
  $$
  $$
  \Rightarrow I_{b1} = \frac{V_o}{\beta_1 r_{e1} + \beta_2(\beta_1 + 1)r_{e2}}
  $$

* **Combining KCL and KVL:**
  $$
  I_o = \frac{V_o}{R_E} + \frac{(\beta_2 + 1)(\beta_1 + 1) V_o}{\beta_1 r_{e1} + (\beta_1 + 1)\beta_2 r_{e2}}
  $$

* **Solving for Output Impedance ($Z_o = \frac{V_o}{I_o}$):**
  $$
  Z_o = R_E \parallel \frac{\beta_1 r_{e1} + (\beta_1 + 1)\beta_2 r_{e2}}{(\beta_2 + 1)(\beta_1 + 1)}
  $$
  Approximating $\beta_1 + 1 \approx \beta_1$ and $\beta_2 + 1 \approx \beta_2$:
  $$
  Z_o \approx R_E \parallel \frac{\beta_1 r_{e1} + \beta_1 \beta_2 r_{e2}}{\beta_1 \beta_2}
  $$
  $$
  Z_o \approx R_E \parallel \left[ r_{e2} + \frac{r_{e1}}{\beta_2} \right]
  $$

---

## Page 15: Analog_Class_Note_Part-1-015.png

### Metadata
- **Date**: 17 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Feedback Pair BJT Configuration
- **Reference**: Boylestad Chapter 5 (fig 5.89)

### Circuit Diagrams

#### 1. Feedback Pair Amplifier Circuit
```
                  V_CC
                   |
         +---------+
         |         |
        [R_B]     [R_C]
         |         |          C_c
   C_s   |         +----------||---- Output (V_o)
  --||---+         | (Emitter Q2 - PNP)
  (V_i)  |      +--+
         |   Q1 |  \ Q2 (PNP)
         +---->|    |
                \   |
                 +--+ (Collector Q2 - NPN Emitter junction)
                 |
                ===
                GND
```

#### 2. AC Equivalent Circuit (re model)
```
          B1                                   Output (Vo)
   I_i     +---------+--------------------+---------+
  ----->   |         |                    |         |
  (V_i)   [R_B]   [\beta_1 r_e1]       [\beta_2 r_e2] [R_C]
           |         | (I_b1)             | (I_b2)  |
   +-------+---------+                    +---------+
   |       |         | E1 (GND)           | B2      |
  ===     ===       ===                   v         v (\beta_2 I_b2)
  GND     GND       GND              (\beta_1 I_b1) |
                                          |         |
                                         ===       ===
                                         GND       GND
```

### Derivations

* **Input Impedance looking into the base ($Z'_i$):**
  $$
  Z'_i = \frac{V_i}{I'_i}
  $$
* **KCL at the Output Node (Emitter of $Q_2$):**
  $$
  I_{b1} + \beta_1 I_{b1} - \beta_2 I_{b2} + I_o = 0
  $$
* **KCL at Node $B_2$ / Collector $Q_1$:**
  $$
  I_{b2} = -\beta_1 I_{b1}
  $$
* **Substituting $I_{b2}$:**
  $$
  I_{b1} + \beta_1 I_{b1} + \beta_1 \beta_2 I_{b1} + I_o = 0
  $$
  $$
  \therefore I_o = - I_{b1} (1 + \beta_1 + \beta_1 \beta_2)
  $$
  Since $\beta_1 \beta_2 \gg \beta_1 \gg 1$:
  $$
  I_o \approx -I_{b1} \beta_1 \beta_2
  $$

---

## Page 16: Analog_Class_Note_Part-1-016.png

### Metadata
- **Topic**: Feedback Pair Configuration DC Analysis (Continuation)

### Mathematical Derivations

* **Expressing Base Current $I_{b1}$:**
  $$
  I_{b1} = \frac{V'_i - V_o}{\beta_1 r_{e1}} \quad \text{and} \quad V_o = -I_o R_C
  $$
  $$
  \Rightarrow V_o = \beta_1 \beta_2 R_C I_{b1}
  $$

* **Substituting $V_o$ back:**
  $$
  I_{b1} = \frac{V'_i - \beta_1 \beta_2 R_C I_{b1}}{\beta_1 r_{e1}}
  $$
  $$
  \Rightarrow \beta_1 r_{e1} I_{b1} + \beta_1 \beta_2 R_C I_{b1} = V'_i
  $$
  $$
  \Rightarrow I_{b1} = \frac{V'_i}{\beta_1 r_{e1} + \beta_1 \beta_2 R_C}
  $$

* **Stage Input Impedance ($Z'_i$):**
  Since $I'_i \approx I_{b1}$:
  $$
  Z'_i = \frac{V'_i}{I'_i} \approx \beta_1 r_{e1} + \beta_1 \beta_2 R_C
  $$
  $$
  Z_i = R_B \parallel Z'_i
  $$

* **Current Gain ($A_i$):**
  $$
  A'_i = \frac{I_o}{I'_i} = \frac{-\beta_1 \beta_2 I_{b1}}{I_{b1}} = -\beta_1 \beta_2
  $$
  $$
  A_i = \frac{I_o}{I_i} = \frac{I_o}{I'_i} \cdot \frac{I'_i}{I_i} = -\beta_1 \beta_2 \frac{R_B}{R_B + Z'_i}
  $$

---

## Page 17: Analog_Class_Note_Part-1-017.png

### Metadata
- **Topic**: Feedback Pair Voltage and Output Impedance Derivations

### Voltage Gain ($A_v$)
$$
I'_i = \frac{R_B}{R_B + Z'_i} I_i = \frac{R_B}{R_B + \beta_1 r_{e1} + \beta_1 \beta_2 R_C} I_i
$$
$$
A_v = \frac{V_o}{V'_i} = \frac{-I_o R_C}{I'_i Z'_i} = \frac{\beta_1 \beta_2 I'_i R_C}{I'_i (\beta_1 r_{e1} + \beta_1 \beta_2 R_C)}
$$
$$
A_v = \frac{\beta_2 R_C}{r_{e1} + \beta_2 R_C} \approx 1 \quad (\text{since } \beta_2 R_C \gg r_{e1})
$$

---

### Output Impedance ($Z_o$)
$$
Z_o = \frac{V_o}{I_o} = \frac{V_o}{-\beta_2 I_{b2}} \quad \text{where } I_{b1} = \frac{-V_o}{\beta_1 r_{e1}}
$$
Looking into the emitter of the second transistor (excluding $R_C$):
$$
Z'_o = \frac{r_{e1}}{\beta_2}
$$
Overall Output Impedance:
$$
Z_o = R_C \parallel Z'_o = R_C \parallel \frac{r_{e1}}{\beta_2}
$$

---

## Page 18: Analog_Class_Note_Part-1-018.png

### Metadata
- **Date**: 18 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Note**: CT-1 Announcement (Syllabus: All previous classes + today)
- **Topic**: Two-Port Systems

### Block Diagram of a Two-Port System
```
     Input Port                              Output Port
       I_i --->                              <--- I_o
      +------------------------------------------+
      |                                          |
  Vi  |            2-Port System                 |  Vo
      |  (Z_i)                            (Z_o)  |
      +------------------------------------------+
```
* **Bengali Note**: $Z_i$, $Z_o$, and $A_{v_{NL}}$ will be given. Main target is finding the loaded voltage gain.

### Thevenin Equivalent Model of the Output Port
```
           Z_o (Z_th)
         ----[===]-------------+ Output Terminal
        |                      |
     +  |                      |
   (A_vNL * V_i)               v V_o
     -  |                      |
        |                      |
       ===                    ===
       GND                    GND
```
* **No-Load Voltage Gain ($A_{v_{NL}}$):**
  $$
  A_{v_{NL}} = \frac{V_o}{V_i} \Rightarrow V_{th} = V_o = A_{v_{NL}} V_i
  $$

---

## Page 19: Analog_Class_Note_Part-1-019.png

### Metadata
- **Topic**: Loaded Two-Port Systems & Gain Derivation

### AC Equivalent Circuit Model with Load ($R_L$)
```
         Input Port                                Output Port
          I_i --->                    R_o            I_o --->
          +-------+                  -[===]----+--------+
          |       |                 |          |        |
      Vi [R_i]   ===  (A_vNL * V_i) (~)        |       [R_L]  Vo
          |       |                 |          |        |
          +-------+                  ----------+--------+
```

### Derivations

* **Current Gain ($A_i$) Relationship to Voltage Gain ($A_v$):**
  $$
  A_i = -A_v \left( \frac{Z_i}{R_L} \right)
  $$

* **Loaded Voltage Gain ($A_v$):**
  * From Loop 1 (output node):
    $$
    V_o = -I_o R_L
    $$
  * From Loop 2 (internal output loop):
    $$
    -A_{v_{NL}} V_i - I_o R_o - I_o R_L = 0 \Rightarrow I_o = -\frac{A_{v_{NL}} V_i}{R_o + R_L}
    $$
  * Substituting $I_o$ into the output voltage equation:
    $$
    V_o = A_{v_{NL}} V_i \left( \frac{R_L}{R_o + R_L} \right)
    $$
    $$
    A_v = \frac{V_o}{V_i} = A_{v_{NL}} \left( \frac{R_L}{R_o + R_L} \right)
    $$

* **Important conclusion (Bengali Note: "Proof will be asked in exam"):**
  Since $R_o + R_L > R_L$, the loaded gain is always less than no-load gain:
  $$
  A_{v_{NL}} > A_v
  $$

---

## Page 20: Analog_Class_Note_Part-1-020.png

### Metadata
- **Topic**: Two-Port Systems with Source Resistance ($R_s$) and Load Resistance ($R_L$)

### 1. Two-Port System with Source Resistance (No Load)
```
          R_s
         -[===]----+-------+                  R_o
        |          |       |                 -[===]------------+
      ( ~ ) V_s   [R_i]   ===  (A_vNL * V_i) (~)               | Vo
        |          |  (V_i)|                 |                 |
        +----------+-------+                  -----------------+
```
* **Source-to-Output Voltage Gain ($A_{v_s}$):**
  $$
  V_i = \frac{R_i}{R_i + R_s} V_s \quad (\text{Voltage divider at input})
  $$
  $$
  V_o = A_{v_{NL}} V_i
  $$
  $$
  A_{v_s} = \frac{V_o}{V_s} = \frac{R_i}{R_i + R_s} A_{v_{NL}}
  $$

---

### 2. Two-Port System with Source ($R_s$) and Load ($R_L$)
```
          R_s                                 R_o
         -[===]----+-------+                 -[===]----+-------+
        |          |       |                |          |       |
      ( ~ ) V_s   [R_i]   === (A_vNL * V_i) (~)       [R_L]   [RL] Vo
        |          |  (V_i)|                |          |       |
        +----------+-------+                 ----------+-------+
```
* **Voltages:**
  $$
  V_i = \frac{R_i}{R_i + R_s} V_s
  $$
  $$
  V_o = A_{v_{NL}} V_i \left( \frac{R_L}{R_o + R_L} \right)
  $$
* **Total loaded source voltage gain ($A_{v_s}$):**
  $$
  A_{v_s} = \frac{V_o}{V_s} = \left( \frac{R_i}{R_i + R_s} \right) \left( \frac{R_L}{R_o + R_L} \right) A_{v_{NL}}
  $$
