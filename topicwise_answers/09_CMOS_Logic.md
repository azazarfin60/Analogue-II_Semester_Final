# 📚 Topic 09: CMOS Logic
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. CMOS Technology Principles

### 1.1 Structural Advantages
*[Appeared in: 2023 Q3(c), 2021 Q8(b)]*

CMOS (Complementary Metal-Oxide-Semiconductor) technology pairs complementary p-channel (PMOS) and n-channel (NMOS) enhancement-mode MOSFETs. Its dominant structural advantages include:
1.  **Ultra-Low Static Power Dissipation:** Under steady-state conditions, either the pull-up network (PMOS) or the pull-down network (NMOS) is entirely OFF. Consequently, no direct DC path exists between the power supply ($V_{DD}$) and Ground, keeping static power dissipation in the nanowatt range. Current is only drawn during active logic state transitions when charging internal gate capacitances.
2.  **Symmetrical Rail-to-Rail Swings:** The high logic state is pulled directly to $+V_{DD}$ (via ON PMOS) and the low logic state is pulled directly to Ground (via ON NMOS), maximizing the logic signal range.
3.  **High Input Impedance:** Because the MOS gate is insulated by a thin layer of silicon dioxide ($SiO_2$), CMOS inputs draw virtually zero DC gate leakage current ($R_{in} > 10^{12}\ \Omega$).
4.  **Wide Noise Margins:** The symmetrical switching threshold (typically at $V_{DD}/2$) results in exceptionally wide noise margins, rendering CMOS circuits highly immune to external voltage spikes.
5.  **High Packing Density:** MOSFETs are physically smaller than BJTs and require no internal isolation resistors, allowing millions of gates to be fabricated on a single silicon die.

---

### 1.2 CMOS Inverter Operation
*[Appeared in: 2017 Q1(c)]*

A CMOS inverter represents the fundamental building block of CMOS logic:

```
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

*   **Construction:**
    *   **PMOS:** Source connected to $+V_{DD}$, Drain connected to the output node ($V_{out}$).
    *   **NMOS:** Source connected to Ground ($0\text{V}$), Drain connected to the output node ($V_{out}$).
    *   **Gates:** Tied together to form the input node ($V_{in}$).
*   **Operating States:**
    1.  **Input Logic HIGH ($V_{in} = V_{DD}$):**
        *   **NMOS:** Gate-to-source voltage $V_{GS(N)} = V_{DD} > V_{th(N)}$, turning the NMOS **ON** (acting as a low-resistance closed switch to Ground).
        *   **PMOS:** Gate-to-source voltage $V_{GS(P)} = 0\text{V} > V_{th(P)}$, keeping the PMOS **OFF** (acting as an open switch).
        *   The output node is pulled directly to Ground: $V_{out} = 0\text{V}$ (Logic LOW).
    2.  **Input Logic LOW ($V_{in} = 0\text{V}$):**
        *   **NMOS:** Gate-to-source voltage $V_{GS(N)} = 0\text{V} < V_{th(N)}$, turning the NMOS **OFF** (open switch).
        *   **PMOS:** Gate-to-source voltage $V_{GS(P)} = -V_{DD} < V_{th(P)}$, turning the PMOS **ON** (low-resistance closed switch to $V_{DD}$).
        *   The output node is pulled directly to $+V_{DD}$: $V_{out} = V_{DD}$ (Logic HIGH).
Because a Logic HIGH input yields a Logic LOW output, and vice versa, the circuit acts as a digital **NOT** gate (inverter).

---

## 2. 2-Input CMOS Logic Gates

### 2.1 2-Input CMOS NAND Gate
*[Appeared in: 2022 Q4(a), 2021 Q8(c)]*

*   **Topology:**
    *   **Pull-up Network (PMOS):** Two PMOS transistors ($Q_{P1}, Q_{P2}$) connected in **parallel** between $+V_{DD}$ and the output node.
    *   **Pull-down Network (NMOS):** Two NMOS transistors ($Q_{N1}, Q_{N2}$) connected in **series** between the output node and Ground.

```
                         +VDD
                     +-----+-----+
                     |     |     |
                    Qp1   Qp2    |  (Parallel PMOS)
                     |     |     |
                     +-----+-----+---> Vout
                           |
                          Qn1
                           |        (Series NMOS)
                          Qn2
                           |
                          Gnd
```

*   **Operating States:**
    *   If **both** inputs A and B are HIGH: Both series NMOS transistors turn ON, completing the pull-down path to Ground. Both parallel PMOS transistors turn OFF. The output is pulled **LOW** ($0\text{V}$).
    *   If **any** input (A or B) is LOW: The corresponding NMOS transistor turns OFF, breaking the series path to Ground. Simultaneously, the corresponding PMOS transistor turns ON, pulling the output **HIGH** ($V_{DD}$).

#### Truth Table:
| Input A | Input B | $Q_{P1}$ State | $Q_{P2}$ State | $Q_{N1}$ State | $Q_{N2}$ State | Output $V_{out}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **LOW** | **LOW** | ON | ON | OFF | OFF | **HIGH** ($1$) |
| **LOW** | **HIGH** | ON | OFF | OFF | ON | **HIGH** ($1$) |
| **HIGH** | **LOW** | OFF | ON | ON | OFF | **HIGH** ($1$) |
| **HIGH** | **HIGH** | OFF | OFF | ON | ON | **LOW** ($0$) |

---

### 2.2 2-Input CMOS NOR Gate
*[Appeared in: 2021 Q8(c)]*

*   **Topology:**
    *   **Pull-up Network (PMOS):** Two PMOS transistors connected in **series** between $+V_{DD}$ and the output node.
    *   **Pull-down Network (NMOS):** Two NMOS transistors connected in **parallel** between the output node and Ground.

```
                         +VDD
                           |
                          Qp1
                           |        (Series PMOS)
                          Qp2
                           |
                     +-----+-----+---> Vout
                     |     |     |
                    Qn1   Qn2    |  (Parallel NMOS)
                     |     |     |
                     +-----+-----+
                           |
                          Gnd
```

*   **Operating States:**
    *   If **both** inputs A and B are LOW: Both series PMOS transistors turn ON, creating a low-resistance path to $+V_{DD}$. Both parallel NMOS transistors are OFF. The output is pulled **HIGH** ($V_{DD}$).
    *   If **any** input (A or B) is HIGH: The corresponding parallel NMOS transistor turns ON, creating a low-resistance path to Ground. Simultaneously, the corresponding series PMOS turns OFF, isolating the output from $+V_{DD}$. The output is pulled **LOW** ($0\text{V}$).

#### Truth Table:
| Input A | Input B | PMOS Series | NMOS Parallel | Output $V_{out}$ |
|:---:|:---:|:---:|:---:|:---:|
| **LOW** | **LOW** | Both ON (Closed to $V_{DD}$) | Both OFF (Open to Ground) | **HIGH** ($1$) |
| **LOW** | **HIGH** | $Q_{P2}$ OFF (Open to $V_{DD}$) | $Q_{N2}$ ON (Closed to Ground) | **LOW** ($0$) |
| **HIGH** | **LOW** | $Q_{P1}$ OFF (Open to $V_{DD}$) | $Q_{N1}$ ON (Closed to Ground) | **LOW** ($0$) |
| **HIGH** | **HIGH** | Both OFF (Open to $V_{DD}$) | Both ON (Closed to Ground) | **LOW** ($0$) |

---

## 3. 3-Input CMOS NAND Gate Design
*[Appeared in: 2022 Q1(c), 2017 Q2(a)]*

### 3.1 Circuit Layout
To implement a 3-input CMOS NAND gate (implementing $V_{out} = \overline{A \cdot B \cdot C}$):
*   **Pull-up Network:** Three PMOS transistors ($Q_{P1}, Q_{P2}, Q_{P3}$) connected in **parallel** between $+V_{DD}$ and the output node.
*   **Pull-down Network:** Three NMOS transistors ($Q_{N1}, Q_{N2}, Q_{N3}$) connected in **series** between the output node and Ground.
*   **Inputs:** Inputs A, B, and C each drive the gate terminals of one complementary pair of PMOS and NMOS transistors.

```
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

---

### 3.2 Detailed Operating Logic & Truth Table
1.  **Case 1: All Inputs HIGH ($A = B = C = V_{DD}$):**
    *   The PMOS transistors $Q_{P1}, Q_{P2}, Q_{P3}$ have $V_{GS} = 0\text{V}$, turning all of them **OFF** (open circuits).
    *   The NMOS transistors $Q_{N1}, Q_{N2}, Q_{N3}$ have $V_{GS} = V_{DD} > V_{th}$, turning all of them **ON** (closed circuits).
    *   A continuous low-resistance path is created from the output node to Ground through the series NMOS chain.
    *   The output voltage is pulled directly to $0\text{V}$ (Logic LOW).
2.  **Case 2: Any Input LOW (e.g., $A = 0\text{V}$):**
    *   The PMOS transistor $Q_{P1}$ has $V_{GS} = -V_{DD} < V_{th}$, turning it **ON** (closed circuit).
    *   The NMOS transistor $Q_{N1}$ has $V_{GS} = 0\text{V}$, turning it **OFF** (open circuit).
    *   The series path to Ground is broken by the OFF transistor $Q_{N1}$, preventing the output from discharging.
    *   The ON PMOS transistor $Q_{P1}$ connects the output directly to $+V_{DD}$.
    *   The output voltage is pulled directly to $+V_{DD}$ (Logic HIGH).

#### Complete Truth Table:
| Input A | Input B | Input C | $Q_{P1}$ | $Q_{P2}$ | $Q_{P3}$ | $Q_{N1}$ | $Q_{N2}$ | $Q_{N3}$ | Output $V_{out}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | **0** | **0** | ON | ON | ON | OFF | OFF | OFF | **1** |
| **0** | **0** | **1** | ON | ON | OFF | OFF | OFF | ON | **1** |
| **0** | **1** | **0** | ON | OFF | ON | OFF | ON | OFF | **1** |
| **0** | **1** | **1** | ON | OFF | OFF | OFF | ON | ON | **1** |
| **1** | **0** | **0** | OFF | ON | ON | ON | OFF | OFF | **1** |
| **1** | **0** | **1** | OFF | ON | OFF | ON | OFF | ON | **1** |
| **1** | **1** | **0** | OFF | OFF | ON | ON | ON | OFF | **1** |
| **1** | **1** | **1** | OFF | OFF | OFF | ON | ON | ON | **0** |
