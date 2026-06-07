[Home](index.md) | [Next](02_Frequency_Response.md)

# 📚 Topic 01: Multistage Amplifiers
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Cascaded JFET-BJT Amplifier

**Question:**
*[Appeared in: 2024 Q1(b), 2023 Q1(b), 2018 Q1(b)]*
* **(b)** Calculate input impedance ($Z_i$), output impedance ($Z_o$), voltage gain ($A_v$), and the resulting output voltage ($v_o(t)$) for the cascaded JFET-BJT amplifier network shown below. The input signal is $v_i(t) = 1\sin(\omega t)\text{ mV}$. **[05 Marks, CO3]**

##### Circuit Diagram:
```text
           +20V (V_DD/V_CC)
             |
      +------+------+------------+
      |             |            |
     [ ] 2.4k      [ ] 15k      [ ] 2.2k
      |             |            |
      +---+         +-----+      +---+------||------+ Vo
      |   |               |      |   |     0.5uF
    D |   |  0.5uF     B  |    C |   |
     ---  +----||----+----+---|\ |   |
  G |   |             |       | \|   |
 ---+   |            [ ] 4.7k |  ----+
 |  | |---            |       | /|
 |    |   |           |    E  |/ |
 |    +---+           |   +--+
[ ]   |               |   |
3.3M  | S             |  [ ] 1k
 |    +-+             |   |
 |    | |             |  +-+
 |   [ ]|680  100uF   |  | | 100uF
 |    | ===           | [ ]| ===
 |    +-+ |           |  | |  |
 |      | |           |  +-+--+
 |      | |           |    |
-+------+-------------+----+--- GND
```
*(JFET parameters: $I_{DSS} = 10\text{ mA}$, $V_P = -4\text{ V}$. BJT parameters: $\beta = 200$, $V_{BE} = 0.7\text{ V}$.)*

**Answer:**

**Step 1: DC Bias Analysis of Stage 1 (JFET)**
The gate draws zero DC current ($I_G \approx 0$). Emitter/Source voltage:
$$V_{GS} = -I_D R_S = -680 I_D$$

Substitute this into Shockley's equation:
$$I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2 \Rightarrow I_D = 10\text{ m} \left( 1 - \frac{-680 I_D}{-4} \right)^2$$
$$I_D = 0.01 (1 - 170 I_D)^2 \Rightarrow I_D = 0.01 (1 - 340 I_D + 28900 I_D^2)$$
$$289 I_D^2 - 4.4 I_D + 0.01 = 0$$

Using the quadratic formula:
$$I_D = \frac{4.4 \pm \sqrt{(-4.4)^2 - 4(289)(0.01)}}{2(289)} = \frac{4.4 \pm 2.793}{578}$$

This yields two mathematical solutions:
*   $I_{D} \approx 12.4\text{ mA}$ (rejected, as it exceeds $I_{DSS} = 10\text{ mA}$)
*   $I_{D} \approx 2.78\text{ mA}$ (accepted)

Calculate the quiescent point:
$$V_{GSQ} = -680 \times 2.78\text{ mA} \approx -1.89\text{ V}$$
$$g_m = \frac{2 I_{DSS}}{|V_P|} \left( 1 - \frac{V_{GSQ}}{V_P} \right) = \frac{2 \times 10\text{ mA}}{4} \left( 1 - \frac{-1.89}{-4} \right) \approx 2.64\text{ mS}$$

**Step 2: DC Bias Analysis of Stage 2 (BJT)**
Using Thevenin's equivalent at the BJT base:
$$V_{th} = V_{DD} \left( \frac{R_{B2}}{R_{B1} + R_{B2}} \right) = 20\text{ V} \left( \frac{4.7\text{ k}\Omega}{15\text{ k}\Omega + 4.7\text{ k}\Omega} \right) \approx 4.77\text{ V}$$
$$R_{th} = R_{B1} \parallel R_{B2} = \frac{15\text{ k}\Omega \times 4.7\text{ k}\Omega}{15\text{ k}\Omega + 4.7\text{ k}\Omega} = 3.58\text{ k}\Omega$$

Apply KVL around the base-emitter loop:
$$V_{th} - I_B R_{th} - V_{BE} - I_E R_E = 0$$

Substitute $I_B = I_E / (\beta + 1) \approx I_E / 200$:
$$4.77 - I_E \left( \frac{3.58\text{ k}\Omega}{200} \right) - 0.7 - I_E (1\text{ k}\Omega) = 0 \Rightarrow 4.07 = I_E (1.0179\text{ k}\Omega)$$
$$I_{EQ} \approx 4.0\text{ mA}$$

Calculate the dynamic resistance:
$$r_e = \frac{26\text{ mV}}{I_{EQ}} = \frac{26\text{ mV}}{4.0\text{ mA}} = 6.5\ \Omega$$

**Step 3: AC Parameter Analysis and Loading**
*   **Input Impedance of Stage 2 ($Z_{i2}$):**
$$Z_{i2} = R_{th} \parallel \beta r_e = 3.58\text{ k}\Omega \parallel (200 \times 6.5\ \Omega) = 3.58\text{ k}\Omega \parallel 1.3\text{ k}\Omega \approx 953\ \Omega$$

*   **Stage 1 Gain ($A_{v1}$):**
$$A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.64\text{ mS} \times (2.4\text{ k}\Omega \parallel 953\ \Omega) \approx -1.8$$

*   **Stage 2 Gain ($A_{v2}$):**
$$A_{v2} = -\frac{R_C}{r_e} = -\frac{2.2\text{ k}\Omega}{6.5\ \Omega} \approx -338.5$$

*   **Overall Voltage Gain ($A_v$):**
$$A_v = A_{v1} \times A_{v2} = (-1.8) \times (-338.5) \approx 609.3$$

*   **Overall Input Impedance ($Z_i$):**
$$Z_i = R_G = 3.3\text{ M}\Omega$$

*   **Overall Output Impedance ($Z_o$):**
$$Z_o = R_C = 2.2\text{ k}\Omega$$

**Step 4: Output Wave Shape**
For $v_i(t) = 1\sin(\omega t)\text{ mV}$:
$$v_o(t) = A_v \times v_i(t) = 609.3 \times 1\sin(\omega t)\text{ mV} \approx 609.3\sin(\omega t)\text{ mV}$$

Since the total phase shift is $180^\circ \times 180^\circ = 360^\circ \equiv 0^\circ$, the output waveform is exactly **in-phase** with the input waveform.

---

## 2. Darlington Configurations

### 2.1 Darlington Current Gain Derivation

**Question:**
*[Appeared in: 2024 Q2(a), 2018 Q2(b)]*
* **(a)** What is the engineering benefit of the Darlington connection? For a Darlington pair circuit, prove that the overall current gain is given by $\beta_d \approx \beta_1 \beta_2$. **[04 Marks, CO2]**

**Answer:**
**Engineering Benefit:** The Darlington connection gives a very high current gain. This gain is the product of the individual gains. It also has a very high input impedance. This makes it ideal for buffers and motor drivers.

**Mathematical Proof of $\beta_D \approx \beta_1 \beta_2$:**
Let the input base current to $Q_1$ be $I_{B1}$.
1. The collector current of $Q_1$ is:
$$I_{C1} = \beta_1 I_{B1}$$
2. The emitter current of $Q_1$ is:
$$I_{E1} = I_{C1} + I_{B1} = (\beta_1 + 1) I_{B1}$$
3. Since $Q_1$'s emitter is tied directly to $Q_2$'s base, the base current of $Q_2$ is:
$$I_{B2} = I_{E1} = (\beta_1 + 1) I_{B1}$$
4. The collector current of $Q_2$ is:
$$I_{C2} = \beta_2 I_{B2} = \beta_2 (\beta_1 + 1) I_{B1}$$
5. The total composite collector current $I_C$ is the sum of both collector currents:
$$I_C = I_{C1} + I_{C2} = \beta_1 I_{B1} + \beta_2 (\beta_1 + 1) I_{B1}$$
$$I_C = (\beta_1 + \beta_1 \beta_2 + \beta_2) I_{B1}$$
6. The overall current gain $\beta_D$ is:
$$\beta_D = \frac{I_C}{I_{B1}} = \beta_1 \beta_2 + \beta_1 + \beta_2$$
7. Since $\beta_1, \beta_2 \gg 1$, their product $\beta_1\beta_2$ is vastly larger than their sum:
$$\beta_D \approx \beta_1 \beta_2$$

---

### 2.2 Darlington AC Analysis

**Question:**
*[Appeared in: 2024 Q2(b)]*
* **(b)** For the Darlington pair configuration shown below, calculate the AC input impedance ($Z_i$), AC current gain ($A_i$), and AC voltage gain ($A_v$). The individual transistors have current gains of $\beta_1 = \beta_2 = 110$. **[04 Marks, CO3]**

##### Circuit Diagram:
```text
           +27V
             |
      +------+------+
      |             |
     [ ] 470k      [ ] 1.2k
      |             |
      +---+         +-------||---+ Vo
      |   |         |
      |   |      C  |
      |   +-------\ |
      |            \|  Q1
      |        B1   +----+
      |             |    |
     [ ] 220k    E1 |  C |
      |             +--\ |
      |                 \|  Q2
      |             B2   +
      |                  | E2
      |                  |
      |                  +---+
      |                  |   |
      |                 [ ]  |
      |                 680  | === CE
      |                  |   |  |
     -+------------------+---+---+ GND
```

**Answer:**
**Step 1: DC Bias Analysis:**
$$\beta_D \approx \beta_1 \beta_2 = 110 \times 110 = 12100$$
Calculate Thevenin equivalents for the base bias network:
$$V_{th} = 27\text{ V} \times \frac{220\text{k}\Omega}{470\text{k}\Omega + 220\text{k}\Omega} = 27 \times 0.3188 \approx 8.61\text{ V}$$
$$R_{th} = 470\text{k}\Omega \parallel 220\text{k}\Omega \approx 149.86\text{ k}\Omega$$

Applying KVL around the base-emitter loop:
$$V_{th} - I_{B1} R_{th} - V_{BE1} - V_{BE2} - I_E R_E = 0$$
Substitute $I_E = (\beta_D + 1) I_{B1} \approx 12100 I_{B1}$:
$$8.61 - I_{B1}(149.86\text{ k}\Omega) - 0.7 - 0.7 - 12100 I_{B1} (680\ \Omega) = 0$$
$$7.21 = I_{B1}(149.86\text{ k}\Omega + 8228\text{ k}\Omega) \Rightarrow I_{B1} = \frac{7.21}{8377.86\text{ k}\Omega} \approx 0.86\ \mu\text{A}$$
$$I_{E2} \approx 12100 \times 0.86\ \mu\text{A} \approx 10.4\text{ mA}$$

Calculate dynamic resistances:
$$r_{e2} = \frac{26\text{ mV}}{10.4\text{ mA}} \approx 2.5\ \Omega$$
$$I_{E1} \approx I_{B2} = \frac{I_{E2}}{\beta_2} = \frac{10.4\text{ mA}}{110} \approx 94.5\ \mu\text{A}$$
$$r_{e1} = \frac{26\text{ mV}}{94.5\ \mu\text{A}} \approx 275.1\ \Omega$$

**Step 2: AC Parameters:**
The emitter is bypassed by $C_E$, so $R_E$ is shorted for AC analysis. 
Input impedance of the Darlington base:
$$Z_{base} = \beta_1 [r_{e1} + \beta_2(r_{e2})] \approx \beta_D r_{e2} = 12100 \times 2.5\ \Omega \approx 30.25\text{ k}\Omega$$
Total input impedance:
$$Z_i = R_{th} \parallel Z_{base} = 149.86\text{ k}\Omega \parallel 30.25\text{ k}\Omega \approx 25.17\text{ k}\Omega$$

Voltage Gain ($A_v$):
Output is taken from the collector.
$$A_v = -\frac{R_C}{r_{e1}/\beta_2 + r_{e2}} = -\frac{1.2\text{ k}\Omega}{2.5 + 275.1/110} = -\frac{1200}{2.5 + 2.5} = -\frac{1200}{5} = -240$$

Current Gain ($A_i$):
$$A_i = \frac{i_o}{i_{in}} = A_v \left( \frac{Z_i}{R_C} \right) = -240 \times \left( \frac{25.17\text{ k}\Omega}{1.2\text{ k}\Omega} \right) = -5034$$

---

## 3. Cascode Configurations

### 3.1 Principles and Cascode BJT Amplifier Numerical Analysis

**Question:**
*[Appeared in: 2019 Q2(a)]*
* **(a)** Calculate the voltage gain of each stage as well as the overall voltage gain for the cascode BJT amplifier circuit shown below. The input is $v_i(t) = 10\sin(\omega t)\text{ mV}$. **[05 Marks]**

##### Circuit Diagram:
```text
                        +20V
                          |
              +-----------+-------------------------+
              |                                     |
             [R_B1] (7.5 kOhm)                     [R_C] (1.5 kOhm)
              |                                     |
              +---(Node A)                          +----||----o v_o
              |       |                             |   C_out (1uF)
             ---     [R_B2] (6.2 kOhm)            |/ C
       (50uF) | |     |                     +-----|   Q2 (beta2=150)
       C_B   ---      +---(Node B)          |     |\ E
              |       |       |             |       |
             ===     [R_B3]   |             |       |
             GND    3.9 kOhm  +--||---------+       |
                      |         C_in (10uF) |       |
                     ===                    |     |/ C
                     GND          o---------+-----|   Q1 (beta1=150)
                                  v_i             |\ E
                                                    |
                                                    +----[R_E] (1 kOhm)
                                                    |     |
                                                   ===   ---  C_E
                                                   GND   --- (100nF)
                                                          |
                                                         ===
                                                         GND
```
*(Assume $V_{BE} = 0.7\text{ V}$.)*

**Answer:**
**Step 1: DC Analysis**
The base voltage of $Q_1$ (bottom CE stage) is biased by $R_{B3}$:
$$V_{B1} = V_{CC} \left( \frac{R_{B3}}{R_{B1} + R_{B2} + R_{B3}} \right) = 20\text{ V} \left( \frac{3.9\text{ k}\Omega}{7.5\text{ k} + 6.2\text{ k} + 3.9\text{ k}} \right) = 20 \times \frac{3.9}{17.6} \approx 4.43\text{ V}$$

Emitter voltage of $Q_1$:
$$V_{E1} = V_{B1} - V_{BE} = 4.43 - 0.7 = 3.73\text{ V}$$

Emitter current of $Q_1$:
$$I_{E1} = \frac{V_{E1}}{R_E} = \frac{3.73\text{ V}}{1\text{ k}\Omega} = 3.73\text{ mA}$$

Since $Q_1$ and $Q_2$ are connected in series, the emitter current of the CB stage ($Q_2$) is:
$$I_{E2} \approx I_{C1} \approx I_{E1} = 3.73\text{ mA}$$

Dynamic resistances:
$$r_{e1} = r_{e2} = \frac{26\text{ mV}}{3.73\text{ mA}} \approx 6.97\ \Omega$$

**Step 2: AC Voltage Gains**
*   **Stage 1 Gain ($A_{v1}$):** CE stage loaded by CB stage's input impedance $r_{e2}$:
$$A_{v1} = -\frac{r_{e2}}{r_{e1}} = -1$$

*   **Stage 2 Gain ($A_{v2}$):** CB stage loaded by $R_C$:
$$A_{v2} = +\frac{R_C}{r_{e2}} = +\frac{1.5\text{ k}\Omega}{6.97\ \Omega} \approx 215.2$$

*   **Overall Voltage Gain ($A_v$):**
$$A_v = A_{v1} \times A_{v2} = (-1) \times 215.2 = -215.2$$

---

## 4. Direct-Coupled Amplifiers

### 4.1 NPN-PNP Phase Relationship Derivation

**Question:**
*[Appeared in: 2018 Q1(a)]*
* **(a)** Derive an equation which describes the phase relationship between the input and output voltage for the direct-coupled cascaded configuration shown below. **[04 Marks]**

##### Circuit Diagram:
```text
                     +----------------------------+------ Vcc
                     |                            |
                    [ ] RC                       [ ] R3
                    [ ]                          [ ]
                     |      PNP (Q2)       C2    |
                     |      / \  E        +--||--+
                     |    c/   \----------+
                     +----|                 
                    /|    b\               
                   / |      \ c
                  |  |       +------------+------ Vo
                 /   |       |            |
             Q1 /    |      [ ] R4       (~) Output
          (NPN) |    |      [ ]          
                \    |       |            |
                 \   |      GND          GND
                  |  |
                  +--+
                  |  |
                 [ ] [ ] R1
                 R2  R_E
                 |   |
                GND GND
```

**Answer:**
**Derivation:**
1.  **Stage 1 ($Q_1$ - NPN CE):**
    The input AC signal $v_{in}$ is applied to the base of the NPN transistor. The stage operates as a common-emitter amplifier, introducing a $180^\circ$ phase inversion:
$$v_{c1} = A_{v1} v_{in} \angle 180^\circ$$

2.  **Stage 2 ($Q_2$ - PNP CE):**
    The collector of $Q_1$ is directly connected to the base of the PNP transistor ($v_{b2} = v_{c1}$). Since a PNP CE stage also operates in common-emitter configuration, it introduces another $180^\circ$ phase inversion:
$$v_o = A_{v2} v_{b2} \angle 180^\circ$$

3.  **Overall Response:**
    Substitute the first stage's output into the second stage:
$$v_o = A_{v2} (A_{v1} v_{in} \angle 180^\circ) \angle 180^\circ = |A_{v1} A_{v2}| v_{in} \angle (180^\circ + 180^\circ)$$
$$v_o = A_v v_{in} \angle 360^\circ \equiv A_v v_{in} \angle 0^\circ$$

**Conclusion:**
The overall phase shift is $360^\circ$ (or $0^\circ$). The output voltage $v_o(t)$ is perfectly **in-phase** with the input voltage $v_{in}(t)$.

---

## 5. Cascaded CE-CS Multistage Amplifier

### 5.1 AC Equivalent Circuit and Parameters Derivation

**Question:**
*[Appeared in: 2019 Q1(a)]*
* **(a)** For the cascaded CE-CS multistage amplifier shown in Figure 1(a), draw the AC equivalent circuit and derive the equations to determine the (i) overall voltage gain ($A_v$), (ii) input impedance ($Z_i$), and (iii) output impedance ($Z_o$). **[08 Marks]**

*(Note: Assumes a JFET CS input stage and BJT CE output stage based on standard naming convention).*

**Answer:**
**Step 1: AC Equivalent Circuit Layout**
1. Replace the JFET (CS) stage with its small-signal model ($g_m v_{gs}$ in parallel with $r_d$, input is open at gate).
2. Replace the BJT (CE) stage with its hybrid-$\pi$ model ($\beta r_e$, dependent current source $\beta i_b$, internal collector resistance $r_o$).
3. Ground all DC power rails ($V_{DD}, V_{CC}$) and short-circuit all coupling and bypass capacitors.

```text
          JFET Stage (CS)                         BJT Stage (CE)
    Gate                                 Base
    o-----+                        +------o-------------------------+
          |                        |                                |
         [ ] RG                   [ ] RD                           [ ] R_th (R1||R2)
          |                        |                                |
    o-----+------o                 +------o                         +------o
    Gnd          |                 |      |                         |      |
                ( ) gm*vgs        [ ] rd ( ) beta*ib               [ ] beta*re
                 |                 |      |                         |      |
    o------------+-----------------+------+-------------------------+------+
    Gnd
```

**Step 2: Derivations of AC Parameters**
**1. Input Impedance ($Z_i$)**
Since JFET gate current is zero, the input impedance looking into the first stage is strictly defined by the gate bias resistor:
$$Z_i = R_G$$

**2. Output Impedance ($Z_o$)**
Looking back into the BJT collector output terminal (with input $v_{in} = 0$), the output impedance (excluding load $R_L$) is:
$$Z_o = R_C \parallel r_o \approx R_C \quad (\text{since } r_o \gg R_C)$$

**3. Voltage Gain ($A_v$)**
*   **Stage 1 Load:** The AC load on the JFET drain is:
$$R_{L1} = r_d \parallel R_D \parallel Z_{i2} \quad \text{where} \quad Z_{i2} = R_1 \parallel R_2 \parallel \beta r_e$$

*   **Stage 1 Gain ($A_{v1}$):**
$$A_{v1} = -g_m (r_d \parallel R_D \parallel Z_{i2})$$

*   **Stage 2 Load:** The AC load on the BJT collector is:
$$R_{L2} = R_C \parallel r_o \approx R_C$$

*   **Stage 2 Gain ($A_{v2}$):**
$$A_{v2} = -\frac{R_C}{r_e}$$

*   **Overall Gain ($A_v$):**
$$A_v = A_{v1} \times A_{v2} = g_m (r_d \parallel R_D \parallel Z_{i2}) \times \frac{R_C}{r_e}$$

[Home](index.md) | [Next](02_Frequency_Response.md)

---

## 6. Constant Current Source Design

**Question:**
*[Appeared in: 2021 Q2(c)]*
* **(c)** Design an NPN BJT constant current source circuit to sink a constant current of $I = 4.65\text{ mA}$ from the collector. The negative DC supply is $-V_{EE} = -20\text{ V}$. Assume a silicon transistor with $V_{BE} = 0.7\text{ V}$ and emitter node voltage $V_E = -10.7\text{ V}$. Find the values of $R_1, R_2$ and $R_E$. **[04 Marks, CLO3]**

**Answer:**
**Step 1: Calculate Emitter Resistor ($R_E$)**
The emitter current is roughly equal to the collector current ($I_E \approx I_C = 4.65\text{ mA}$).
$$R_E = \frac{V_E - (-V_{EE})}{I_E} = \frac{-10.7\text{ V} - (-20\text{ V})}{4.65\text{ mA}} = \frac{9.3\text{ V}}{4.65\text{ mA}} = 2\text{ k}\Omega$$

**Step 2: Calculate Base Voltage ($V_B$)**
$$V_B = V_E + V_{BE} = -10.7\text{ V} + 0.7\text{ V} = -10\text{ V}$$

**Step 3: Design Voltage Divider ($R_1, R_2$)**
The voltage divider sets $V_B$ to $-10\text{ V}$. The divider connects between Ground ($0\text{ V}$) and $-20\text{ V}$.
$$V_B = -V_{EE} \left( \frac{R_1}{R_1 + R_2} \right)$$
Using $V_B = -10\text{ V}$ and $-V_{EE} = -20\text{ V}$, we see $V_B$ is exactly half the supply voltage.
$$\frac{R_1}{R_1 + R_2} = 0.5 \implies R_1 = R_2$$
Choose standard resistor values, for example:
$$R_1 = 10\text{ k}\Omega$$
$$R_2 = 10\text{ k}\Omega$$

---

## 7. Collector-Feedback Configuration

**Question:**
*[Appeared in: 2023 Q2(c)]*
* **(c)** For the collector-feedback BJT amplifier network, calculate the input impedance ($Z_i$), output impedance ($Z_o$), voltage gain ($A_v$), and current gain ($A_i$). The BJT parameter values are $h_{fe} = 120$, $h_{ie} = 1.175\text{ k}\Omega$, and $h_{oe} = 20\ \mu\text{A/V}$. The circuit has $R_C = 2.7\text{ k}\Omega$ and $R_F = 330\text{ k}\Omega$. **[03 Marks, CLO2]**

**Answer:**
Convert $h$-parameters to $r_e$ model parameters:
$$\beta = h_{fe} = 120$$
$$r_e = \frac{h_{ie}}{\beta} = \frac{1175\ \Omega}{120} \approx 9.79\ \Omega$$
$$r_o = \frac{1}{h_{oe}} = \frac{1}{20\ \mu\text{A/V}} = 50\text{ k}\Omega$$

**1. Input Impedance ($Z_i$):**
$$Z_i = \beta r_e \parallel \frac{R_F}{|A_v|}$$
Assuming $|A_v| \approx R_C / r_e = 2700 / 9.79 = 275.8$:
$$Z_i \approx 1175 \parallel \frac{330\text{ k}\Omega}{275.8} = 1175 \parallel 1196 \approx 593\ \Omega$$

**2. Output Impedance ($Z_o$):**
$$Z_o = R_C \parallel R_F \parallel r_o = 2.7\text{ k}\Omega \parallel 330\text{ k}\Omega \parallel 50\text{ k}\Omega \approx 2.55\text{ k}\Omega$$

**3. Voltage Gain ($A_v$):**
$$A_v = -\frac{R_C \parallel R_F \parallel r_o}{r_e} = -\frac{2550}{9.79} \approx -260.5$$

**4. Current Gain ($A_i$):**
$$A_i = \frac{I_o}{I_i} = A_v \left( \frac{Z_i}{R_C} \right) = -260.5 \left( \frac{593}{2700} \right) \approx -57.2$$

---

## 8. Push-Pull Configuration Biasing

**Question:**
*[Appeared in: 2024 Q1(c)]*
* **(c)** Calculate the DC bias currents and voltages for the NPN-PNP complementary push-pull emitter follower stage, such that the DC output voltage is exactly half of the supply voltage ($V_o = 9\text{ V}$). Transistor parameters are: NPN $Q_1$ ($\beta_1 = 140$) and PNP $Q_2$ ($\beta_2 = 180$). The circuit has $V_{CC} = +18\text{ V}$, $R_C = 750\ \Omega$, and a base resistor $R_B = 2\text{ M}\Omega$. **[03 Marks, CO2]**

**Answer:**
**Step 1: Output Node Voltage**
The problem specifies the quiescent output voltage is exactly half the supply voltage:
$$V_o = \frac{18\text{ V}}{2} = 9\text{ V}$$

**Step 2: Base Voltages**
Assuming standard emitter follower configuration:
For the NPN transistor ($Q_1$), the base voltage must be $0.7\text{ V}$ higher than the emitter.
$$V_{B1} = V_o + 0.7\text{ V} = 9.7\text{ V}$$
For the PNP transistor ($Q_2$), the base voltage must be $0.7\text{ V}$ lower than the emitter.
$$V_{B2} = V_o - 0.7\text{ V} = 8.3\text{ V}$$

**Step 3: Quiescent Currents**
In a true Class B push-pull amplifier without base biasing diodes, both transistors are completely OFF under zero-signal DC conditions. Therefore, the quiescent bias currents are zero:
$$I_{CQ1} = I_{CQ2} = 0\text{ mA}$$
*(Note: If this is an active feedback pair, the $2\text{ M}\Omega$ resistor sets the base current $I_B = 9.7\text{ V} / 2\text{ M}\Omega = 4.85\ \mu\text{A}$, yielding $I_{C1} = 140 \times 4.85\ \mu\text{A} = 0.68\text{ mA}$.)*

---

## 9. JFET Biasing Configurations

### 9.1 Self-Bias JFET Q-Point

**Question:**
*[Appeared in: 2023 Q3(a)]*
* **(a)** Calculate the Q-point parameters ($I_{DQ}$ and $V_{GSQ}$) and the quiescent drain-to-ground voltage ($V_D$) for the JFET self-bias network. The JFET parameters are $I_{DSS} = 8\text{ mA}$ and $V_P = -8\text{ V}$. The circuit has $V_{DD} = 20\text{ V}$, $R_D = 6.2\text{ k}\Omega$, and $R_S = 2.4\text{ k}\Omega$. **[04 Marks, CLO2]**

**Answer:**
**Step 1: Find $V_{GSQ}$ and $I_{DQ}$**
In a self-bias circuit, the gate draws no DC current, so $V_G = 0\text{ V}$.
The source voltage is $V_S = I_D R_S$.
$$V_{GS} = V_G - V_S = -I_D R_S = -2400 I_D$$

Substitute into Shockley's equation:
$$I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2 = 8\text{ mA} \left( 1 - \frac{-2400 I_D}{-8} \right)^2$$
$$I_D = 0.008 (1 - 300 I_D)^2 = 0.008 (1 - 600 I_D + 90000 I_D^2)$$
$$720 I_D^2 - 5.8 I_D + 0.008 = 0$$

Using the quadratic formula:
$$I_D = \frac{5.8 \pm \sqrt{(-5.8)^2 - 4(720)(0.008)}}{2(720)} = \frac{5.8 \pm 3.256}{1440}$$
This gives $I_D \approx 6.28\text{ mA}$ (rejected, $V_{GS}$ exceeds $V_P$) and $I_D \approx 1.76\text{ mA}$ (accepted).
$$I_{DQ} = 1.76\text{ mA}$$

Calculate $V_{GSQ}$:
$$V_{GSQ} = -2400 \times 1.76\text{ mA} \approx -4.22\text{ V}$$

**Step 2: Calculate Drain Voltage ($V_D$)**
$$V_D = V_{DD} - I_D R_D = 20\text{ V} - (1.76\text{ mA} \times 6.2\text{ k}\Omega)$$
$$V_D = 20\text{ V} - 10.91\text{ V} = 9.09\text{ V}$$

---

### 9.2 Voltage-Divider Bias JFET Design

**Question:**
*[Appeared in: 2023 Q3(b)]*
* **(b)** For the JFET voltage-divider bias configuration, determine the value of the source resistor $R_S$ required to yield a drain voltage $V_D = 12\text{ V}$ and a quiescent gate-to-source voltage $V_{GSQ} = -2\text{ V}$. The circuit has $V_{DD} = 16\text{ V}$, $R_{G1} = 91\text{ k}\Omega$, $R_{G2} = 47\text{ k}\Omega$, and $R_D = 1.8\text{ k}\Omega$. **[03 Marks, CLO2]**

**Answer:**
**Step 1: Calculate Drain Current ($I_D$)**
We know the drain voltage $V_D$ and the supply $V_{DD}$.
$$I_D = \frac{V_{DD} - V_D}{R_D} = \frac{16\text{ V} - 12\text{ V}}{1.8\text{ k}\Omega} = \frac{4\text{ V}}{1.8\text{ k}\Omega} \approx 2.22\text{ mA}$$

**Step 2: Calculate Gate Voltage ($V_G$)**
Using the voltage divider formula:
$$V_G = V_{DD} \left( \frac{R_{G2}}{R_{G1} + R_{G2}} \right) = 16\text{ V} \left( \frac{47\text{ k}\Omega}{91\text{ k}\Omega + 47\text{ k}\Omega} \right) = 16 \times \frac{47}{138} \approx 5.45\text{ V}$$

**Step 3: Calculate Source Resistor ($R_S$)**
We know that $V_{GS} = V_G - V_S$, and $V_S = I_D R_S$.
$$V_{GS} = V_G - I_D R_S$$
$$-2\text{ V} = 5.45\text{ V} - (2.22\text{ mA} \times R_S)$$
$$2.22\text{ mA} \times R_S = 7.45\text{ V}$$
$$R_S = \frac{7.45\text{ V}}{2.22\text{ mA}} \approx 3.35\text{ k}\Omega$$

[Home](index.md) | [Next](02_Frequency_Response.md)
