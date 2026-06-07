[Previous](08_Active_Filters.md) | [Home](index.md)

# 📚 Topic 09: CMOS Logic and Special Circuits
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. CMOS Logic Principles

### 1.1 Structural Advantages
*[Appeared in: 2023 Q3(c)]*

**Question:**
* **(c)** Briefly explain the key electrical characteristics and structural advantages of CMOS logic gates. **[03 Marks, CLO1]**

**Answer:**
CMOS technology pairs p-channel (PMOS) and n-channel (NMOS) enhancement-mode MOSFETs. Its structural advantages include:
1.  **Ultra-Low Static Power Dissipation:** Under steady-state, either the PMOS or the NMOS network is OFF. No direct DC path exists between $V_{DD}$ and Ground. This keeps static power dissipation extremely low. Current is drawn mostly during logic transitions.
2.  **Symmetrical Rail-to-Rail Swings:** The high logic state is pulled directly to $+V_{DD}$ (via PMOS). The low logic state is pulled directly to Ground (via NMOS). This maximizes the logic signal swing.
3.  **High Input Impedance:** A thin layer of silicon dioxide insulates the MOS gate. So CMOS inputs draw virtually zero DC gate leakage current.
4.  **Wide Noise Margins:** The symmetrical switching threshold (at $V_{DD}/2$) creates exceptionally wide noise margins. This makes CMOS circuits highly immune to external voltage spikes.

---

### 1.2 CMOS Inverter Operation
*[Appeared in: 2024 Q3(c), 2017 Q1(c)]*

**Question:**
* **(c)** Briefly explain how a CMOS circuit operates as a digital logic inverter. Draw its schematic diagram. **[03 Marks, CO1]**

**Answer:**
A CMOS inverter represents the fundamental building block of all CMOS digital logic:
```text
                      +VDD
                       |
                     [ PMOS ]  (Source to Drain)
                       |
        Vin o----------+---> Vout
                       |
                     [ NMOS ]  (Drain to Source)
                       |
                      Gnd
```
*   **Operating States:**
    1.  **Input Logic HIGH ($V_{in} = V_{DD}$):**
        *   **NMOS:** Gate-to-source voltage $V_{GS(N)} = V_{DD} > V_{th(N)}$, turning the NMOS **ON** (acting as a closed switch to Ground).
        *   **PMOS:** Gate-to-source voltage $V_{GS(P)} = 0\text{V} > V_{th(P)}$, keeping the PMOS **OFF** (acting as an open switch).
        *   The output node is pulled directly to Ground: $V_{out} = 0\text{V}$ (Logic LOW).
    2.  **Input Logic LOW ($V_{in} = 0\text{V}$):**
        *   **NMOS:** Gate-to-source voltage $V_{GS(N)} = 0\text{V} < V_{th(N)}$, turning the NMOS **OFF**.
        *   **PMOS:** Gate-to-source voltage $V_{GS(P)} = -V_{DD} < V_{th(P)}$, turning the PMOS **ON** (closed switch to $V_{DD}$).
        *   The output node is pulled directly to $+V_{DD}$: $V_{out} = V_{DD}$ (Logic HIGH).
*   A Logic HIGH input yields a Logic LOW output, and vice versa. So the circuit acts as a digital **NOT** gate (inverter).

---

## 2. CMOS Logic Gate Design

### 2.1 3-Input CMOS NAND Gate
*[Appeared in: 2022 Q1(c), 2017 Q2(a)]*

**Question:**
* **(c)** Design a 3-input CMOS NAND gate and explain its operation with its truth table. **[04 Marks, CO3]**

**Answer:**
To implement a 3-input CMOS NAND gate (implementing $V_{out} = \overline{A \cdot B \cdot C}$):
*   **Pull-up Network:** Three PMOS transistors ($Q_{P1}, Q_{P2}, Q_{P3}$) connected in **parallel** between $+V_{DD}$ and the output node.
*   **Pull-down Network:** Three NMOS transistors ($Q_{N1}, Q_{N2}, Q_{N3}$) connected in **series** between the output node and Ground.
```text
                           +VDD
                 +-----+-----+-----+
                 |     |     |     |
                Qp1   Qp2   Qp3    |   (Parallel PMOS Pull-up)
                 |     |     |     |
                 +-----+-----+-----+---> Vout
                       |
                      Qn1
                       |
                      Qn2              (Series NMOS Pull-down)
                       |
                      Qn3
                       |
                      Gnd
```
**Operating Logic:**
1.  **All Inputs HIGH ($A = B = C = 1$):** All PMOS transistors are OFF. All NMOS transistors are ON. This creates a series path to Ground. The output is pulled to **0** (LOW).
2.  **Any Input LOW:** The corresponding NMOS transistor turns OFF. This breaks the series path to Ground. The corresponding PMOS transistor turns ON, connecting the output to $+V_{DD}$. The output is pulled to **1** (HIGH).

**Truth Table Overview:**
| A | B | C | Output |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **1** |
| X | X | 0 | **1** |
| 1 | 1 | 1 | **0** |
*(Output is 0 only when all inputs are 1).*

---

### 2.2 3-Input CMOS NOR Gate
*[Appeared in: 2021 Q1(c)]*

**Question:**
* **(c)** Design a 3-input NOR gate using CMOS technology and explain its operating logic. **[04 Marks, CLO3]**

**Answer:**
To implement a 3-input CMOS NOR gate (implementing $V_{out} = \overline{A + B + C}$):
*   **Pull-up Network:** Three PMOS transistors connected in **series** between $+V_{DD}$ and the output node.
*   **Pull-down Network:** Three NMOS transistors connected in **parallel** between the output node and Ground.
```text
                         +VDD
                           |
                          Qp1
                           |        (Series PMOS Pull-up)
                          Qp2
                           |
                          Qp3
                           |
                     +-----+-----+-----+---> Vout
                     |     |     |     |
                    Qn1   Qn2   Qn3    |  (Parallel NMOS Pull-down)
                     |     |     |     |
                     +-----+-----+-----+
                           |
                          Gnd
```
**Operating Logic:**
1.  **All Inputs LOW ($A = B = C = 0$):** All PMOS transistors are ON. This creates a continuous series path to $+V_{DD}$. All NMOS transistors are OFF. The output is pulled to **1** (HIGH).
2.  **Any Input HIGH:** The corresponding PMOS transistor turns OFF. This breaks the series path to $+V_{DD}$. The corresponding NMOS transistor turns ON, connecting the output to Ground. The output is pulled to **0** (LOW).

---

## 3. Current Mirrors

### 3.1 Basic BJT Current Mirror
*[Appeared in: 2022 Q1(b)]*

**Question:**
* **(b)** Draw a current mirror circuit using BJTs and explain its operating logic. **[03 Marks, CO2]**

**Answer:**
In integrated circuits, resistors take up too much space. Instead, transistors act as active current sources.
```text
                  +Vcc
                   |
                  [R]
                   |
        Iref ----->+------------+
                   |            |
                  Q1 (Diode)   Q2 (Sink)
                   |            |
                  Gnd          Gnd
```
**Operating Logic:**
*   $Q_1$ is diode-connected (collector shorted to base). This forces it to operate in the active region. The current $I_{ref}$ flows through resistor $R$. This establishes a base-emitter voltage $V_{BE}$ across $Q_1$.
*   Since the base and emitter terminals of $Q_1$ and $Q_2$ are tied directly in parallel, $Q_2$ is subjected to the exact same $V_{BE}$.
*   Assume matched transistors with high $\beta$. The output collector current of $Q_2$ accurately mirrors the reference current ($I_{out} \approx I_{ref}$). $Q_2$ behaves as a constant current sink.

---

### 3.2 The Wilson Current Mirror
*[Appeared in: 2017 Q3(b)]*

**Question:**
* **(b)** Calculate the current $I$ through each of the transistors $Q_2$ and $Q_3$ in the Wilson current mirror circuit shown below. Assume identical transistors with $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. **[04 Marks]**

*(Circuit Given: Wilson mirror biased with $V_{CC} = 6\text{ V}$ and a reference resistor $R = 1.3\text{ k}\Omega$.)*

**Answer:**
The Wilson current mirror uses a third transistor ($Q_3$) for negative feedback. This increases output resistance and reduces base current transfer errors. The output current equation for finite $\beta$ is:
$$ I_{out} = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right) $$

**Step 1: Calculate reference current ($I_{ref}$)**
The reference path contains the resistor $R$ in series with two forward-biased base-emitter junctions ($Q_1$ and $Q_3$):
$$ I_{ref} = \frac{V_{CC} - V_{BE1} - V_{BE3}}{R} = \frac{6\text{ V} - 0.7\text{ V} - 0.7\text{ V}}{1.3\text{ k}\Omega} = \frac{4.6\text{ V}}{1300\ \Omega} \approx 3.538\text{ mA} $$

**Step 2: Calculate output current ($I_{C3}$)**
For $\beta = 100$, the error term is $\frac{2}{10000 + 100} = \frac{2}{10100} \approx 0.000198$.
$$ I_{C3} = 3.538\text{ mA} \times \left( \frac{1}{1.000198} \right) \approx 3.537\text{ mA} $$
The current through $Q_3$ and $Q_2$ is approximately $3.537\text{ mA}$.

---

## 4. Differential Amplifiers
*[Appeared in: 2022 Q3(a), 2017 Q3(c)]*

**Question:**
* **(c)** Calculate the DC voltages $V_{o1}$ and $V_{o2}$ for the symmetrical differential BJT amplifier circuit shown below. **[04 Marks]**

*(Circuit Given: Symmetrical BJT diff-amp connected to $+9\text{ V}$ and $-9\text{ V}$ supplies. Emitters tied together to tail resistor $R_{EE} = 3.3\text{ k}\Omega$. Collector resistors $R_C = 3.9\text{ k}\Omega$.)*

**Answer:**
**Operating Logic:** A differential amplifier amplifies the difference between two signals. It rejects any signals common to both inputs (Common-Mode Rejection). The long-tail pair design keeps the total bias current constant. The current splits between the two branches based on the differential input.

**Step-by-Step DC Solution (for zero input conditions):**
**Step 1: Calculate the common emitter voltage ($V_E$)**
With both bases grounded ($0\text{V}$), $V_E = 0 - 0.7\text{ V} = -0.7\text{ V}$.

**Step 2: Calculate the total tail current ($I_{EE}$)**
$$ I_{EE} = \frac{V_E - (-V_{EE})}{R_{EE}} = \frac{-0.7\text{ V} - (-9\text{ V})}{3.3\text{ k}\Omega} = \frac{8.3\text{ V}}{3300\ \Omega} \approx 2.515\text{ mA} $$

**Step 3: Split the tail current**
Due to perfect symmetry, the tail current splits exactly in half:
$$ I_{E1} = I_{E2} = \frac{2.515\text{ mA}}{2} = 1.2575\text{ mA} \approx I_C $$

**Step 4: Calculate the DC output voltages**
$$ V_{o1} = V_{o2} = V_{CC} - I_C R_C = 9\text{ V} - (1.2575\text{ mA} \times 3.9\text{ k}\Omega) = 9\text{ V} - 4.904\text{ V} = 4.096\text{ V} $$

---

## 5. Special Op-Amp Networks

### 5.1 Multi-Stage Cascaded Feedback
*[Appeared in: 2022 Q7(b)]*

**Question:**
* **(b)** Calculate the closed-loop gain $V_o/V_i$ of the two-stage cascaded op-amp feedback amplifier network shown below. **[04/05 Marks, CO2]**

*(Circuit Given: Stage 1 is an inverting summing amplifier with inputs $V_i$ through $5\text{k}\Omega$, $V_{o1}$ through $10\text{k}\Omega$, and overall output $V_o$ through $4\text{k}\Omega$. Stage 2 is a non-inverting amplifier driven by $V_{o1}$ with feedback resistors $R_{f2} = 2\text{k}\Omega, R_{g2} = 10\text{k}\Omega$.)*

**Answer:**
**Step 1: Analyze Stage 2 (Non-Inverting Stage)**
The input to Stage 2 is $V_{o1}$, and the output is $V_o$:
$$ V_o = V_{o1} \left( 1 + \frac{R_{f2}}{R_{g2}} \right) = V_{o1} \left( 1 + \frac{2\text{ k}\Omega}{10\text{ k}\Omega} \right) = 1.2 V_{o1} $$
Express the intermediate voltage $V_{o1}$ in terms of the final output $V_o$:
$$ V_{o1} = \frac{V_o}{1.2} = \frac{5}{6} V_o $$

**Step 2: Apply KCL at the inverting node of Stage 1**
By the virtual ground principle, the inverting input of Stage 1 is held at $0\text{V}$. The sum of currents entering this node must equal zero:
$$ \frac{V_i}{5} + \frac{V_{o1}}{10} + \frac{V_o}{4} = 0 $$

**Step 3: Substitute $V_{o1} = \frac{5}{6} V_o$ into the KCL equation**
$$ \frac{V_i}{5} + \frac{\frac{5}{6} V_o}{10} + \frac{V_o}{4} = 0 \Rightarrow \frac{V_i}{5} + \frac{V_o}{12} + \frac{V_o}{4} = 0 $$
$$ \frac{V_i}{5} + V_o \left( \frac{1}{12} + \frac{3}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + V_o \left( \frac{4}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + \frac{V_o}{3} = 0 $$

**Step 4: Solve for the overall closed-loop voltage gain ($A_v$)**
$$ \frac{V_o}{3} = -\frac{V_i}{5} \Rightarrow A_v = \frac{V_o}{V_i} = -\frac{3}{5} = -0.6 $$

[Previous](08_Active_Filters.md) | [Home](index.md)
