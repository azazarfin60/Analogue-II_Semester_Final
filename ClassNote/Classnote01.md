# Class Note Digitization - Phase 1 (Pages 1 to 10)

---

## Page 1: Analog_Class_Note_Part-1-001.png

### Metadata
- **Date**: 8 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir

### Content

#### Analog - I recap:
* **N-type** $\rightarrow$ free electron
* **P-type** $\rightarrow$ hole / positive charge

* **Diode**: [ n ] over [ p ]
* **Transistor**: [ n ] [ p ] [ n ]
* **Thyristor**: [ p ] [ n ] [ p ] [ n ]

---

#### Diode Bias Diagram
Below is the representation of the P-N junction under Forward Bias:

```
      P-type            N-type
   [   -  -   |   +  +   ]
   [  -    -  |  +    +  ]
   [          |          ]
        -  -  |  +  +
      Depletion Layer
             <- 
   (Electron Flow: circles with '-')
   
     |                       |
     |                       |
     +-------[ -  + ]--------+
               Battery
```

* **Forward Bias:**
  * $\rightarrow$ Flow of electron
  * $\leftarrow$ Flow of current

---

#### Questions & Core Concepts
* DC biasing কেন করা হয়? (Why is DC biasing done?)
* Reference Books: Boylestad, B.K. Mehta

---

#### Voltage Divider Bias Circuit
Below is the Voltage Divider Bias Configuration for an NPN BJT:

```
              V_CC
               |
         +-----+-----+
         |           |
        [R1]        [R_C]
         |           |       C2
   C1    |           +-------||---- v_o
  --||---+-- Base    |
         |  (NPN BJT) |
        [R2]         \  Q1
         |            \|
         |             +----+
         |             |    |
        ===           [R_E] === (C_E bypass optional)
        GND            |    GND
                      ===
                      GND
```

* We first find $I_B$:
  $$
  \beta = \frac{I_C}{I_B}
  $$
  $$
  R_{Th} = \frac{R_1 \cdot R_2}{R_1 + R_2}
  $$

---

#### Thevenin Equivalent Circuit at the Base
```
         R_Th       Base
      --[===]---------+
     |               |
   + |               | (V_BE)
   (E_Th)            v
   - |               |
     |              [R_E]
    ===              |
    GND             ===
                    GND
```

* **KVL around Base-Emitter Loop:**
  $$
  -E_{Th} + R_{Th} I_B + V_{BE} + R_E I_E = 0
  $$
  Since $I_E = (\beta + 1) I_B$:
  $$
  -E_{Th} + R_{Th} I_B + V_{BE} + (\beta + 1) R_E I_B = 0
  $$
  
  $$
  \Rightarrow I_B = \frac{E_{Th} - V_{BE}}{R_{Th} + (\beta + 1) R_E} \approx \frac{E_{Th} - V_{BE}}{R_{Th} + \beta R_E}
  $$

---

## Page 2: Analog_Class_Note_Part-1-002.png

### Metadata
- **Date**: 10 November, 2025
- **Course**: LAB-01 (Moley Sir)
- **Topic**: Exp 01: Experiment of multistage BJT Amplifier.

### Circuit Diagram: Two-stage BJT Common-Emitter (CE) Amplifier
```
                V_CC = 20V
                 |
   +-------+-----+---------------+-------+
   |       |     |               |       |
  [R1]    [R_C1] |              [R3]    [R_C2]
  100k    2.2k   |              100k    1k
   |       |     |               |       |       10uF
   | C1    |     |   C_coupling  | C_out |
  -||------+     +-------||------+       +-------||---- Output (v_o)
   |       |    / Q1             |      / Q2
  [R2]     +---|                [R4]    |
  4.7k     |    \                4.7k   |
   |      [R_E1] +               |     [R_E2]
   |      100    | Emitter       |     100    |
   |       |     | Bypass        |      |     | Emitter Bypass
  ===     ===   === (10uF)      ===    ===   === (10uF)
  GND     GND   GND             GND    GND   GND
```
* **Notes on values**:
  * Transistors: $Q_1, Q_2$ have $\beta = 200$.
  * Input signal: $25\text{ mV}$ AC signal source.
  * $A_{V_1}$: Voltage gain of Stage 1 (from base of $Q_1$ to base of $Q_2$).
  * $A_{V_2}$: Voltage gain of Stage 2 (from base of $Q_2$ to output).

### DC Bias Analysis & Voltage Gain Formulas

* **Base Voltage ($V_B$):**
  $$
  V_B = \frac{R_2 \cdot V_{CC}}{R_1 + R_2}
  $$
* **Emitter Voltage ($V_E$):**
  $$
  V_E = V_B - 0.7\text{ V}
  $$
* **Emitter Current ($I_E$):**
  $$
  I_E = \frac{V_E}{R_E}
  $$
* **Dynamic Emitter Resistance ($r_e$):**
  $$
  r_e = \frac{26\text{ mV}}{I_E}
  $$
* **Voltage Gain of Stage 1 ($A_{V_1}$):**
  $$
  A_{V_1} = \frac{- R_{C1} \parallel (R_3 \parallel R_4 \parallel \beta r_{e2})}{r_{e1}}
  $$

---

## Page 3: Analog_Class_Note_Part-1-003.png

### Metadata
- **Date**: 10 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Multi-stage Configuration
- **Sub-Topic**: Darlington Configuration
- **Reference**: Boylestad Chapter 9 (fig-9.67)

### Darlington Pair Configurations

#### 1. AC/DC Schematic of Darlington Pair
```
             V_CC
              |
         +----+---------+
         |              |
        [R_B]         Collector
         |              |
   C_i   |            +---+
  --||---+            |   |
         |         Q1 \   |
         |             |--+
         |            /   |
         +-----------+    |
                     | \  | Q2
                     |  |--+
                     | /
                     + Emitter
                     |
                    [R_E]
                     |      C_o
                     +------||---- Output (v_o)
                     |
                    [R_L]
                     |
                    ===
                    GND
```

#### 2. Detailed DC Current Path Diagram (fig-9.67)
```
                  V_CC
                   |
         +---------+-----+
         |               |
        I_B1            I_C
         |               |
     Base (Q1)         +---+
         |             |   |
         |         Q1  \   | I_C1
         |            \|---+
         |   V_BE1     +---+
         v   (+ / -)   |
     Emitter (Q1)      |
         |             |
         |   I_E1      |
         v   (=I_B2)   |
     Base (Q2)         | I_C2
         |             |
         |         Q2  \
         |            \|
         |   V_BE2     +
         v   (+ / -)   | Emitter (Q2)
                       |
                       v I_E2
                       |
                      [R_E]
                       |
                      ===
                      GND
```

### Derivations & Current Relationships
* **Emitter Current of $Q_1$:**
  $$
  I_{E_1} = (\beta_1 + 1) I_{B_1}
  $$
* **Emitter Current of $Q_2$:**
  $$
  I_{E_2} = (\beta_2 + 1) I_{B_2}
  $$
* Since the emitter of $Q_1$ is directly tied to the base of $Q_2$:
  $$
  I_{E_1} = I_{B_2}
  $$
* **Total Emitter Current $I_{E_2}$:**
  $$
  I_{E_2} = (\beta_2 + 1)(\beta_1 + 1) I_{B_1}
  $$
* Under the approximation that $\beta \gg 1$:
  $$
  I_{E_2} \approx \beta_1 \beta_2 I_{B_1}
  $$
  $$
  \therefore I_{E_2} \approx \beta_D I_{B_1}
  $$
  where $\beta_D = \beta_1 \beta_2$ is the total Darlington Beta.

---

## Page 4: Analog_Class_Note_Part-1-004.png

### Metadata
- **Topic**: Darlington Configuration DC Analysis (Continuation)

### DC Analysis Steps & Equations

* **Step 1: Find Base Current ($I_{B_1}$)**
  Using KVL around the Base-Emitter loop:
  $$
  I_{B_1} = \frac{V_{CC} - V_{BE_1} - V_{BE_2}}{R_B + (\beta_D + 1)R_E}
  $$

* **Step 2: Find Emitter Voltage of Second Transistor ($V_{E_2}$)**
  $$
  V_{E_2} = I_{E_2} \cdot R_E
  $$
  $$
  \therefore V_{E_2} = \beta_D \cdot I_{B_1} \cdot R_E
  $$
  *(Note: Since $\beta_D \gg 1$, we use $I_{E_2} \approx I_{C_2} = \beta_D I_{B_1}$)*

* **Step 3: Find Collector Voltage of Second Transistor ($V_{C_2}$)**
  $$
  V_{C_2} = V_{CC}
  $$

* **Step 4: Find Collector-Emitter Voltage of Second Transistor ($V_{CE_2}$)**
  $$
  V_{CE_2} = V_{C_2} - V_{E_2}
  $$

---

## Page 5: Analog_Class_Note_Part-1-005.png

### Metadata
- **Topic**: Feedback Pair Configuration
- **Reference**: Boylestad Chapter 9 (fig-4.71)

### Feedback Pair Circuit Descriptions

#### 1. AC/DC Schematic of Feedback Pair
A complementary transistor configuration containing a PNP first stage ($Q_1$) and an NPN second stage ($Q_2$).
```
             V_CC
              |
         +----+-------+
         |            |
        [R_B]        [R_C]
         |            |
   C_s   |            +-----+----- v_o (via C_c to R_L)
  --||---+            |     |
         |         Q1 \     |
         |             |--  |
         |            /     |
         +-----------+    +---+
                     |    |   |
                     | Q2 \   |
                     |    \|--+
                     |     +
                     |     |
                    ===   ===
                    GND   GND
```

#### 2. Detailed DC Current Path Diagram (fig-4.71)
```
                     V_CC
                      |
            +---------+
            |         |
           [R_B]     [R_C] (Current I_C flows down)
            |         |
        Base (Q1)     +------- Collector (Q2)
            |        / (PNP)  (Current I_C2 enters)
            +-------| Q1
            |        \ (Emitter) [Current I_E1 flows out to R_C node]
            |         |
            |         +------- Base (Q2) [Current I_B2 = I_C1]
           [R_B]      |
            |        / Q2 (NPN)
           ===      |
           GND     === (Emitter of Q2 to Ground, current I_E2)
```
* **KVL Loop Path:** Starts from Ground, up through $R_B$, up through Base-Emitter of PNP $Q_1$, up through $R_C$ to $V_{CC}$.

### DC Analysis: Step 1 (Convert all currents to $I_{B_1}$)
* **KVL around Base-Emitter Loop:**
  $$
  V_{CC} - R_C I_C - V_{BE_1} - I_{B_1} R_B = 0
  $$

* **Current relationships:**
  1. $I_C = I_{E_1} + I_{C_2}$
  2. $I_{E_1} = (\beta_1 + 1) I_{B_1}$
  3. $I_{C_2} = \beta_2 I_{B_2}$
  4. Since $Q_1$ collector current feed $Q_2$ base: $I_{B_2} = I_{C_1} = \beta_1 I_{B_1}$
  5. Thus, $I_{C_2} = \beta_2 (\beta_1 I_{B_1}) = \beta_1 \beta_2 I_{B_1}$

* **Substituting back to find total current $I_C$:**
  $$
  I_C = I_{E_1} + I_{C_2}
  $$
  $$
  I_C = (\beta_1 + 1) I_{B_1} + \beta_1 \beta_2 I_{B_1}
  $$
  $$
  I_C = I_{B_1} (\beta_1 + 1 + \beta_1 \beta_2)
  $$
  Since $\beta \gg 1$:
  $$
  I_C \approx \beta_1 \beta_2 I_{B_1}
  $$

* **Final KVL Equation in terms of $I_{B_1}$:**
  $$
  V_{CC} - R_C (\beta_1 \beta_2 I_{B_1}) - V_{BE_1} - I_{B_1} R_B = 0
  $$
  $$
  \Rightarrow I_{B_1} = \frac{V_{CC} - V_{BE_1}}{R_B + \beta_1 \beta_2 R_C}
  $$

---

## Page 6: Analog_Class_Note_Part-1-006.png

### Metadata
- **Topic**: Feedback Pair Configuration DC Analysis (Continuation)

### DC Voltages Calculation Steps

* **Step 2: Base Voltages ($V_{B_1}$ & $V_{B_2}$)**
  $$
  V_{B_1} = I_{B_1} \cdot R_B
  $$
  $$
  V_{B_2} = V_{BE_2} = 0.7\text{ V}
  $$

* **Step 3: Collector Voltages ($V_{C_1}$ & $V_{C_2}$)**
  $$
  V_{C_1} = V_{BE_2} = 0.7\text{ V}
  $$
  $$
  V_{C_2} = V_{CC} - I_C R_C \quad (\text{where } I_C \approx I_{C_2})
  $$

*(Note: Faint drawings and text on this page represent backside bleed-through from the physical notebook.)*

---

## Page 7: Analog_Class_Note_Part-1-007.png

### Metadata
- **Topic**: Direct Coupled Amplifier

### Circuit Diagram: Two-stage Direct-Coupled BJT Amplifier
```
             V_CC
              |
         +----+---------+
         |    |         |
        [R1] [R_C1]    [R_C2]
         |    |         |
   Input |    +---------+----- Base (Q2)
  ------>+   / Q1       |
         |--|        Q2 \
        [R2] \           |
         |    +          +---- Output (v_o)
         |   [R_E1]     [R_E2]
         |    |          |
        ===  ===        ===
        GND  GND        GND
```

### Analysis Steps & Equations

* **Step 1: Perform Thevenin Equivalent at the Base of $Q_1$**
  $$
  R_{Th} = R_1 \parallel R_2
  $$
  $$
  E_{Th} = \frac{R_2}{R_1 + R_2} \cdot V_{CC}
  $$
  $$
  I_{B_1} = \frac{E_{Th} - V_{BE_1}}{R_{Th} + (\beta_1 + 1)R_{E_1}}
  $$

* **Step 2: Find Base Voltage of Stage 2 ($V_{B_2}$)**
  $$
  V_{B_2} = V_{CC} - I_{C_1} R_{C_1}
  $$
  Assuming base current $I_{B_2}$ is small enough that $I_{C_1} \approx \beta_1 I_{B_1}$:
  $$
  V_{B_2} = V_{CC} - \beta_1 I_{B_1} R_{C_1}
  $$

* **Step 3: Find Emitter Voltage of Stage 2 ($V_{E_2}$)**
  $$
  V_{E_2} = I_{E_2} R_{E_2}
  $$
  Since $V_{BE_2} = V_{B_2} - V_{E_2}$:
  $$
  \therefore V_{E_2} = V_{B_2} - V_{BE_2}
  $$

* **Step 4: Find Collector Voltages & Output Limits**
  $$
  V_{C_2} = V_{CC}
  $$
  $$
  V_{CE_2} = V_{C_2} - V_{E_2}
  $$

---

## Page 8: Analog_Class_Note_Part-1-008.png

### Metadata
- **Date**: 11 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Cascode Configuration

### Circuit Diagram: BJT Cascode Configuration
A configuration stacking a common-emitter stage ($Q_1$) underneath a common-base stage ($Q_2$).
```
                  V_CC
                   |
         +----+----+---------------+
         |    |                    |
        [R1]  |                  [R_C]
         |    |                    |
         +----+------- Base (Q2)   |
         |    |                    |
        [R2]  |                Q2  \ (CB Stage)
         |  C_B                    |--+
         +--||-+                   |  |
         |     |                   |  v_o (via C_out)
        [R3]  ===      +-----------+
         |    GND     / Q1         (Node V_C1 = V_E2)
         |           |-- Base (Q1) via C_in
         |            \ (CE Stage)
         |             +
         |            [R_E]
         |             |
        ===           ===
        GND           GND
```

### DC Bias Analysis

* **Step 1: Base Biasing Voltages ($V_{B_1}$, $V_{B_2}$)**
  Using the voltage divider across $R_1, R_2, R_3$:
  $$
  V_{B_1} = \frac{R_3}{R_1 + R_2 + R_3} \cdot V_{CC}
  $$
  $$
  V_{B_2} = \frac{R_2 + R_3}{R_1 + R_2 + R_3} \cdot V_{CC}
  $$

* **Step 2: Emitter Voltages ($V_{E_1}$, $V_{E_2}$)**
  $$
  V_{E_1} = V_{B_1} - V_{BE_1}
  $$
  $$
  V_{E_2} = V_{B_2} - V_{BE_2}
  $$

* **Step 3: Emitter Current ($I_{E_1}$)**
  From the Base-Emitter loop of $Q_1$:
  $$
  -V_{B_1} + V_{BE_1} + I_{E_1} R_E = 0 \Rightarrow I_{E_1} = \frac{V_{B_1} - V_{BE_1}}{R_E}
  $$
  
  *Note: Due to series stacking, the currents are approximately equal:*
  $$
  I_{C_2} \approx I_{E_2} \approx I_{C_1} \approx I_{E_1}
  $$

---

## Page 9: Analog_Class_Note_Part-1-009.png

### Metadata
- **Topic**: Cascode Configuration (Continuation) & Current Mirror

### Cascode Configuration (Continuation)
* **Step 4: Collector Voltages ($V_{C_1}$, $V_{C_2}$)**
  $$
  V_{C_1} = V_{E_2}
  $$
  $$
  V_{C_2} = V_{CC} - I_{C_2} R_C \quad (\text{where } I_{C_2} \approx I_{E_1})
  $$

---

### Current Mirror Circuit
```
                   V_CC
                    |
              +-----+---------+
              |               |
             [R]            Load
              |               |
         I_control            | I_L = I_C2
              |               |
     +--------+---- Base      |
     |        |    (Shared)   |
     |     Collector        Collector
     |      Node (Q1)       Node (Q2)
     |        |               |
     |     Q1 \            Q2 \
     +-------|                |
              \                \
               +                +
               |                |
              ===              ===
              GND              GND
```

#### Matching Conditions for Current Mirror:
1. Identical transistors: $\beta_1 = \beta_2$
2. Equal base currents: $I_{B_1} = I_{B_2}$
3. Equal base-emitter voltages: $V_{BE_1} = V_{BE_2}$

#### Derivation of Current Relationships:
* Feedback base current node:
  $$
  I_B = I_{B_1} + I_{B_2} = 2 I_{B_1}
  $$
* Control current branch:
  $$
  I_{control} = I_{C_1} + I_B
  $$
  $$
  I_{control} = \beta_1 I_{B_1} + 2 I_{B_1} = (\beta_1 + 2) I_{B_1}
  $$
* Assuming high beta ($\beta_1 \gg 2$):
  $$
  I_{control} \approx \beta_1 I_{B_1}
  $$
  $$
  \Rightarrow I_{B_1} \approx \frac{I_{control}}{\beta_1}
  $$
* Since the transistors are matched:
  $$
  I_{L} = I_{C_2} = \beta_2 I_{B_2} = \beta_1 I_{B_1} \approx I_{control}
  $$

---

## Page 10: Analog_Class_Note_Part-1-010.png

### Metadata
- **Topic**: Current Mirror Stabilization & Current Source Circuits

### Current Mirror Stabilization (Negative Feedback Mechanism)
If the load current $I_L$ fluctuates, negative feedback naturally stabilizes the circuit:
$$
\text{same হয়ে যাবে (It will become the same).}
$$
$$
I_L \uparrow \;\rightarrow\; I_{C_2} \uparrow \;\rightarrow\; I_{B_2} \uparrow \;\rightarrow\; V_{BE_2} \uparrow \;\rightarrow\; V_{BE_1} \uparrow \;\rightarrow\; V_{CE_1} \uparrow \;\rightarrow\; I_{control} \downarrow \;\rightarrow\; I_B \downarrow \;\rightarrow\; I_{B_2} \downarrow \;\rightarrow\; I_{E_2} \downarrow \;\rightarrow\; I_L \downarrow
$$

From the control loop:
$$
-V_{CC} + I_{control} \cdot R + V_{CE_1} = 0 \Rightarrow V_{CE_1} = V_{CC} - I_{control} \cdot R
$$

---

### BJT Current Source Circuit
Using dual power supplies (Ground and $-V_{EE}$):
```
             GND (0V)
              |
         +----+--------+
         |             |
        [R1]         Load
         |             |
         +------- Base |
         |             |
        [R2]        Q1 \
         |             + Emitter
         |             |
         |            [R_E]
         |             |
         +----+--------+
              |
            -V_EE
```

* **Base Voltage ($V_B$):**
  $$
  V_B = \frac{R_1}{R_1 + R_2} (-V_{EE})
  $$
* **Emitter Voltage ($V_E$):**
  $$
  V_{BE} = V_B - V_E \Rightarrow V_E = V_B - V_{BE}
  $$
* **Emitter Current ($I_E$):**
  $$
  I_E = \frac{V_E - (-V_{EE})}{R_E}
  $$
  Since $I_C \approx I_E$:
  $$
  I_C \approx \frac{V_E + V_{EE}}{R_E}
  $$
