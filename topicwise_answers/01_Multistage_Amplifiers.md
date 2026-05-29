# 📚 Topic 01: Multistage Amplifiers
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. JFET-BJT Cascaded Amplifiers

### 1.1 The Golden JFET-BJT Cascaded Amplifier
*[Appeared in: 2024 Q1(b), 2023 Q1(b), 2018 Q1(b), 2017 Q1(b), CT1 Q1]*

**Problem Schematic Description:**
A two-stage cascaded amplifier.
*   **Stage 1:** Common-Source JFET amplifier. Input $v_i$ is coupled via $C_G$ to the gate. Biasing resistors are $R_G = 3.3\text{ M}\Omega$, $R_D = 2.4\text{ k}\Omega$, and $R_S = 680\ \Omega$ bypassed by $C_S$. JFET parameters: $I_{DSS} = 10\text{ mA}$, $V_P = -4\text{ V}$.
*   **Stage 2:** Common-Emitter BJT amplifier. Input is coupled via $C_C$ from Stage 1's drain to Stage 2's base. Biasing resistors are $R_{B1} = 15\text{ k}\Omega$, $R_{B2} = 4.7\text{ k}\Omega$, $R_C = 2.2\text{ k}\Omega$, and $R_E = 1\text{ k}\Omega$ bypassed by $C_E$. BJT parameters: $\beta = 200$, $V_{BE} = 0.7\text{ V}$.
*   **Supply:** $+V_{DD} = +20\text{ V}$ (common supply for both).

**Objective:**
Calculate (i) Input Impedance $Z_i$, (ii) Output Impedance $Z_o$, (iii) Stage 1 gain $A_{v1}$, Stage 2 gain $A_{v2}$, and overall gain $A_v$, and (iv) Sketch output wave shapes for $v_i(t) = 10\sin(\omega t)\text{ mV}$.

#### Complete Step-by-Step Solution:

##### Step 1: DC Bias Analysis of Stage 1 (JFET)
The gate draws zero DC current ($I_G \approx 0$). Emitter/Source voltage:
$$V_{GS} = -I_D R_S = -680 I_D$$
Substitute this into Shockley's equation:
$$I_D = I_{DSS} \left( 1 - \frac{V_{GS}}{V_P} \right)^2 \Rightarrow I_D = 10\text{ m} \left( 1 - \frac{-680 I_D}{-4} \right)^2$$
$$I_D = 0.01 (1 - 170 I_D)^2 \Rightarrow I_D = 0.01 (1 - 340 I_D + 28900 I_D^2)$$
$$I_D = 0.01 - 3.4 I_D + 289 I_D^2 \Rightarrow 289 I_D^2 - 4.4 I_D + 0.01 = 0$$
Using the quadratic formula:
$$I_D = \frac{4.4 \pm \sqrt{(-4.4)^2 - 4(289)(0.01)}}{2(289)} = \frac{4.4 \pm \sqrt{19.36 - 11.56}}{578} = \frac{4.4 \pm 2.793}{578}$$
This yields two mathematical solutions:
*   $I_{D} \approx 12.4\text{ mA}$ (rejected, as it exceeds $I_{DSS} = 10\text{ mA}$)
*   $I_{D} \approx 2.78\text{ mA}$ (accepted)

Calculate the quiescent point:
$$V_{GSQ} = -680 \times 2.78\text{ mA} \approx -1.89\text{ V}$$
$$g_m = \frac{2 I_{DSS}}{|V_P|} \left( 1 - \frac{V_{GSQ}}{V_P} \right) = \frac{2 \times 10\text{ mA}}{4} \left( 1 - \frac{-1.89}{-4} \right) = 5\text{ mS} \times (1 - 0.4725) \approx 2.64\text{ mS}$$

##### Step 2: DC Bias Analysis of Stage 2 (BJT)
Using Thevenin's equivalent at the BJT base:
$$V_{th} = V_{DD} \left( \frac{R_{B2}}{R_{B1} + R_{B2}} \right) = 20\text{ V} \left( \frac{4.7\text{ k}\Omega}{15\text{ k}\Omega + 4.7\text{ k}\Omega} \right) = 20 \times \frac{4.7}{19.7} \approx 4.77\text{ V}$$
$$R_{th} = R_{B1} \parallel R_{B2} = \frac{15\text{ k}\Omega \times 4.7\text{ k}\Omega}{15\text{ k}\Omega + 4.7\text{ k}\Omega} = 3.58\text{ k}\Omega$$
Apply KVL around the base-emitter loop:
$$V_{th} - I_B R_{th} - V_{BE} - I_E R_E = 0$$
Substitute $I_B = I_E / (\beta + 1) \approx I_E / 200$:
$$4.77 - I_E \left( \frac{3.58\text{ k}\Omega}{200} \right) - 0.7 - I_E (1\text{ k}\Omega) = 0 \Rightarrow 4.07 = I_E (1.0179\text{ k}\Omega)$$
$$I_{EQ} \approx 4.0\text{ mA}$$
Calculate the dynamic resistance:
$$r_e = \frac{26\text{ mV}}{I_{EQ}} = \frac{26\text{ mV}}{4.0\text{ mA}} = 6.5\ \Omega$$

##### Step 3: AC Parameter Analysis and Loading
*   **Input Impedance of Stage 2 ($Z_{i2}$):**
    $$Z_{i2} = R_{th} \parallel \beta r_e = 3.58\text{ k}\Omega \parallel (200 \times 6.5\ \Omega) = 3.58\text{ k}\Omega \parallel 1.3\text{ k}\Omega \approx 953\ \Omega$$
*   **Stage 1 Gain ($A_{v1}$):**
    $$A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.64\text{ mS} \times (2.4\text{ k}\Omega \parallel 953\ \Omega) = -2.64\text{ mS} \times 682.3\ \Omega \approx -1.8$$
*   **Stage 2 Gain ($A_{v2}$):**
    $$A_{v2} = -\frac{R_C}{r_e} = -\frac{2.2\text{ k}\Omega}{6.5\ \Omega} \approx -338.5$$
*   **Overall Voltage Gain ($A_v$):**
    $$A_v = A_{v1} \times A_{v2} = (-1.8) \times (-338.5) \approx 609.3$$
*   **Overall Input Impedance ($Z_i$):**
    $$Z_i = R_G = 3.3\text{ M}\Omega$$
*   **Overall Output Impedance ($Z_o$):**
    $$Z_o = R_C = 2.2\text{ k}\Omega$$

##### Step 4: Output Wave Shape Sketch
For $v_i(t) = 10\sin(\omega t)\text{ mV}$:
$$v_o(t) = A_v \times v_i(t) = 609.3 \times 10\sin(\omega t)\text{ mV} \approx 6.09\sin(\omega t)\text{ V}$$
*   **Phase:** Since the total phase shift is $180^\circ \times 180^\circ = 360^\circ \equiv 0^\circ$, the output waveform is exactly **in-phase** with the input waveform.
*   **Sketch:** Sketch a $10\text{ mV}$ peak sine wave as $v_i(t)$ and a matching, in-phase $6.09\text{ V}$ peak sine wave as $v_o(t)$.

---

### 1.2 Cascaded JFET-BJT (Alternative Component Values)
*[Appeared in: 2021 Q1(b), 2022 Q1(a)]*

**Problem Details:**
*   **Stage 1:** JFET CS ($I_{DSS}=6\text{ mA}, V_P=-3\text{ V}, R_G=10\text{ M}\Omega, R_D=1.8\text{ k}\Omega, R_S=330\ \Omega$).
*   **Stage 2:** BJT CE ($\beta=150, V_{BE}=0.7\text{ V}, R_{B1}=24\text{ k}\Omega$ to $+10\text{ V}$, $R_C=2.7\text{ k}\Omega$, $R_E=2.2\text{ k}\Omega$ bypassed).

**Solution Summary:**
1.  **JFET DC Bias:** $V_{GS} = -0.33 I_D$. Substituting into Shockley's equation yields:
    $$0.667 V_{GS}^2 + 7.03 V_{GS} + 6 = 0 \Rightarrow V_{GSQ} \approx -0.94\text{ V}$$
    $$g_m = \frac{12\text{ m}}{3} \left( 1 - \frac{-0.94}{-3} \right) \approx 2.75\text{ mS}$$
2.  **BJT DC Bias:** Base current is calculated directly:
    $$I_B = \frac{V_{DD} - V_{BE}}{R_{B1} + (\beta+1)R_E} = \frac{10 - 0.7}{24\text{ k} + (151 \times 2.2\text{ k})} \approx 26.1\ \mu\text{A}$$
    $$I_E = (\beta+1)I_B \approx 3.94\text{ mA} \Rightarrow r_e = \frac{26\text{ mV}}{3.94\text{ mA}} \approx 6.6\ \Omega$$
3.  **AC Impedances and Gain:**
    $$Z_i = R_G = 10\text{ M}\Omega \quad \text{and} \quad Z_o = R_C = 2.7\text{ k}\Omega$$
    $$Z_{i2} = R_{B1} \parallel \beta r_e = 24\text{ k}\Omega \parallel 990\ \Omega \approx 950\ \Omega$$
    $$A_{v1} = -g_m (R_D \parallel Z_{i2}) = -2.75\text{ mS} \times (1.8\text{ k} \parallel 0.95\text{ k}) \approx -1.71$$
    $$A_{v2} = -\frac{R_C}{r_e} = -\frac{2.7\text{ k}}{6.6} \approx -409.1$$
    $$A_v = A_{v1} \times A_{v2} = (-1.71) \times (-409.1) \approx 699.6$$

---

## 2. Darlington Configurations

### 2.1 Darlington Current Gain Analytical Derivation
*[Appeared in: 2024 Q2(a), 2023 Q1(a), 2018 Q2(b)]*

**Darlington Configuration Schematic:**
```
            Collector (C)
            o-----------+
                        |
                        |
                  C1  |/ Q1
        Base (B) o----|
                      |> E1
                        |
                        +----+
                             |
                       C2  |/ Q2
                           |-----> Output Emitter (E)
                           |> E2
```

**Mathematical Proof of $\beta_D \approx \beta_1 \beta_2$:**
Let the input base current to $Q_1$ be $I_{B1}$.
1.  The collector current of $Q_1$ is:
    $$I_{C1} = \beta_1 I_{B1}$$
2.  The emitter current of $Q_1$ is:
    $$I_{E1} = I_{C1} + I_{B1} = (\beta_1 + 1) I_{B1}$$
3.  Since $Q_1$'s emitter is tied directly to $Q_2$'s base, the base current of $Q_2$ is:
    $$I_{B2} = I_{E1} = (\beta_1 + 1) I_{B1}$$
4.  The collector current of $Q_2$ is:
    $$I_{C2} = \beta_2 I_{B2} = \beta_2 (\beta_1 + 1) I_{B1}$$
5.  The total composite collector current $I_C$ is the sum of both collector currents:
    $$I_C = I_{C1} + I_{C2} = \beta_1 I_{B1} + \beta_2 (\beta_1 + 1) I_{B1}$$
    $$I_C = (\beta_1 + \beta_1 \beta_2 + \beta_2) I_{B1}$$
6.  The overall current gain $\beta_D$ is:
    $$\beta_D = \frac{I_C}{I_{B1}} = \beta_1 \beta_2 + \beta_1 + \beta_2$$
7.  Since $\beta_1, \beta_2 \gg 1$, their product $\beta_1\beta_2$ is vastly larger than their sum ($\beta_1 + \beta_2$):
    $$\beta_D \approx \beta_1 \beta_2$$

---

### 2.2 Darlington Emitter Follower AC Analysis
*[Appeared in: 2019 Q2(b)]*

**Problem Details:**
*   **Circuit:** Darlington Emitter Follower. $R_B = 2.4\text{ M}\Omega$, $R_E = 510\ \Omega$, $\beta_1 = 50$, $\beta_2 = 120$, $V_{CC} = +16\text{ V}$.
*   **Objective:** Find voltage gain $A_v$ and current gain $A_i$.

**Solution:**
1.  **DC Bias Analysis:**
    $$\beta_D \approx \beta_1 \beta_2 = 50 \times 120 = 6000$$
    Applying KVL around the base-emitter loop:
    $$V_{CC} - I_{B1} R_B - V_{BE1} - V_{BE2} - I_E R_E = 0$$
    Substitute $I_E = (\beta_D + 1) I_{B1} \approx 6000 I_{B1}$:
    $$16 - I_{B1} (2.4\text{ M}\Omega) - 0.7 - 0.7 - 6000 I_{B1} (510) = 0$$
    $$14.6 = I_{B1} (2.4\text{ M}\Omega + 3.06\text{ M}\Omega) = I_{B1} (5.46\text{ M}\Omega)$$
    $$I_{B1} = \frac{14.6}{5.46\text{ M}\Omega} \approx 2.67\ \mu\text{A}$$
    $$I_E = 6000 \times 2.67\ \mu\text{A} \approx 16.02\text{ mA}$$
    Calculate dynamic resistances:
    $$r_{e2} = \frac{26\text{ mV}}{16.02\text{ mA}} \approx 1.62\ \Omega$$
    $$I_{E1} \approx I_{B2} = \frac{I_E}{\beta_2} = \frac{16.02\text{ mA}}{120} \approx 133.5\ \mu\text{A}$$
    $$r_{e1} = \frac{26\text{ mV}}{133.5\ \mu\text{A}} \approx 194.7\ \Omega$$
2.  **AC Parameters:**
    Input impedance of the Darlington base:
    $$Z_{base} \approx \beta_1 [r_{e1} + \beta_2(r_{e2} + R_E)] \approx \beta_1 \beta_2 R_E = 6000 \times 510\ \Omega \approx 3.06\text{ M}\Omega$$
    Total input impedance:
    $$Z_i = R_B \parallel Z_{base} = 2.4\text{ M}\Omega \parallel 3.06\text{ M}\Omega \approx 1.34\text{ M}\Omega$$
3.  **Voltage Gain ($A_v$):**
    $$A_v = \frac{R_E}{R_E + r_{e2} + r_{e1}/\beta_2} = \frac{510}{510 + 1.62 + 194.7/120} = \frac{510}{513.24} \approx 0.994$$
4.  **Current Gain ($A_i$):**
    $$A_i = \frac{i_o}{i_{in}} = A_v \left( \frac{Z_i}{R_E} \right) = 0.994 \times \left( \frac{1.34\text{ M}\Omega}{510\ \Omega} \right) \approx 2612$$

---

## 3. Cascode Configurations

### 3.1 Principles and Benefits
*[Appeared in: 2023 Q2(a), 2022 Q1(a)]*

A Cascode configuration consists of a **Common-Emitter (CE)** stage driving a **Common-Base (CB)** stage.
*   **Neutralization of Miller Effect:** The input CE stage has a load impedance equal to the input impedance of the CB stage ($Z_{in(CB)} = r_e$). The voltage gain of the first stage is therefore $A_{v1} \approx -r_e/r_e = -1$. Because the gain is extremely low, the Miller feedback capacitance at the input is minimal ($C_{Mi} = C_{\mu}(1 - A_{v1}) = 2 C_{\mu}$), preventing bandwidth degradation.
*   **High Gain and Output Impedance:** The second stage (CB) provides the actual voltage gain of the system ($A_{v2} \approx R_C / r_e$), resulting in a massive overall voltage gain with an extremely wide high-frequency bandwidth.

---

### 3.2 Cascode BJT Amplifier Numerical Analysis
*[Appeared in: 2019 Q2(a)]*

**Problem Details:**
*   **Circuit:** Cascode configuration biased by $V_{CC} = +20\text{ V}$. Divider resistors: $R_{B1} = 7.5\text{ k}\Omega$, $R_{B2} = 6.2\text{ k}\Omega$, $R_{B3} = 3.9\text{ k}\Omega$ (top to bottom). Collector resistor $R_C = 1.5\text{ k}\Omega$, Emitter resistor $R_E = 1\text{ k}\Omega$. $\beta_1 = \beta_2 = 150$, $V_{BE} = 0.7\text{ V}$.

**Solution:**
1.  **DC Analysis:**
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
2.  **AC Voltage Gains:**
    *   **Stage 1 Gain ($A_{v1}$):** CE stage loaded by CB stage's input impedance $r_{e2}$:
        $$A_{v1} = -\frac{r_{e2}}{r_{e1}} = -1$$
    *   **Stage 2 Gain ($A_{v2}$):** CB stage loaded by $R_C$:
        $$A_{v2} = +\frac{R_C}{r_{e2}} = +\frac{1.5\text{ k}\Omega}{6.97\ \Omega} \approx 215.2$$
    *   **Overall Voltage Gain ($A_v$):**
        $$A_v = A_{v1} \times A_{v2} = (-1) \times 215.2 = -215.2$$

---

## 4. Feedback Pair (Feedback Multistage Connection)

### 4.1 Proof of Unity Voltage Gain & High Current Gain
*[Appeared in: CT1 Q2]*

A **Feedback Pair** (or Complementary Darlington) consists of a matched NPN-PNP pair.

```
                  Collector (C)
                      o---------+
                                |
                                |/ Q2 (PNP)
                        +-------|
                        |       |>
                        |         |
                  C1  |/ Q1 (NPN) |
        Base (B) o----|           |
                      |> E1       |
                        |         |
                        +---------+-----> Output Emitter (E)
```

**Proof of Voltage Gain ($A_v \approx 1$):**
The input is applied to the base of $Q_1$, and the output is taken from the emitter of $Q_1$ which is connected back to the collector of $Q_2$. 
Because the emitter of $Q_1$ is directly connected to the output node, the configuration acts as an emitter follower (common-collector) for the input stage. By virtual base-emitter tracking, any voltage change at the base of $Q_1$ is mirrored at its emitter, meaning:
$$V_{out} = V_{in} - V_{BE1} \Rightarrow A_v = \frac{\Delta V_{out}}{\Delta V_{in}} \approx 1$$

**Proof of High Current Gain ($A_i \approx \beta_1 \beta_2$):**
1.  The input base current to $Q_1$ is $I_{B1}$.
2.  The collector current of $Q_1$ is $I_{C1} = \beta_1 I_{B1}$.
3.  This collector current drives the base of the PNP transistor $Q_2$. Hence, $I_{B2} = I_{C1} = \beta_1 I_{B1}$.
4.  The collector current of $Q_2$ is:
    $$I_{C2} = \beta_2 I_{B2} = \beta_1 \beta_2 I_{B1}$$
5.  This collector current is returned back to the output node (emitter of $Q_1$), summing with $Q_1$'s emitter current.
6.  The overall output current is:
    $$I_{out} = I_{E1} + I_{C2} \approx I_{C1} + I_{C2} = \beta_1 I_{B1} + \beta_1 \beta_2 I_{B1} \approx (\beta_1 \beta_2) I_{B1}$$
    $$A_i = \frac{I_{out}}{I_{B1}} \approx \beta_1 \beta_2$$

---

## 5. Direct-Coupled Amplifiers

### 5.1 NPN-PNP Phase Relationship Derivation
*[Appeared in: 2018 Q1(a)]*

**Problem Setup:**
Derive the phase relationship between the input and output voltage for a direct-coupled cascaded configuration consisting of an NPN CE stage followed by a PNP CE stage.

**Mathematical Derivation:**
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

## 6. Cascaded BJT CE-CS AC Analysis and Derivations
*[Appeared in: 2019 Q1(a)]*

**Problem Setup:**
For a cascaded CE-CS multistage amplifier, draw the AC equivalent circuit and derive the equations for $A_v, Z_i$, and $Z_o$.

### 6.1 AC Equivalent Circuit Layout
1.  Replace the JFET (CS) stage with its small-signal model ($g_m v_{gs}$ in parallel with $r_d$, input is open at gate).
2.  Replace the BJT (CE) stage with its hybrid-$\pi$ model ($\beta r_e$, dependent current source $\beta i_b$, internal collector resistance $r_o$).
3.  Ground all DC power rails ($V_{DD}, V_{CC}$) and short-circuit all coupling and bypass capacitors.

```
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

### 6.2 Derivations of AC Parameters

#### 1. Input Impedance ($Z_i$)
Since JFET gate current is zero, the input impedance looking into the first stage is strictly defined by the gate bias resistor:
$$Z_i = R_G$$

#### 2. Output Impedance ($Z_o$)
Looking back into the BJT collector output terminal (with input $v_{in} = 0$), the output impedance (excluding load $R_L$) is:
$$Z_o = R_C \parallel r_o \approx R_C \quad (\text{since } r_o \gg R_C)$$

#### 3. Voltage Gain ($A_v$)
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
