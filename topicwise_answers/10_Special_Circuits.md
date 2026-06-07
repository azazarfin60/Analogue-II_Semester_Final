[Previous](09_CMOS_Logic.md) | [Home](index.md)

# 📚 Topic 10: Special Circuits
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Integrated Circuit Current Sources

### 1.1 Basic Current Mirror matching logic
*[Appeared in: 2024 Q1(c), 2022 Q1(b), 2020 Q1(c)]*

**Question:**
* **(c)** Calculate the DC bias currents and voltages for the NPN-PNP complementary push-pull emitter follower stage shown below, such that the DC output voltage is exactly half of the supply voltage ($V_o = 9\text{ V}$). Transistor parameters are: NPN $Q_1$ ($\beta_1 = 140$) and PNP $Q_2$ ($\beta_2 = 180$). **[03 Marks, CO2]**

##### Circuit Diagram (Q.1(c)):
```
             Vcc = +18V
              |
             [ ] Rc = 750
              |
              +----+
              |    |
            C |    |
            --+    |
          B |  ----+ Q1 (NPN, b1 = 140)
       +----+  |  /|
       |    |  |/ |
       |    |  +--+
       | Ii |  |
  Vi >-||---+--+ (Vo midpoint)
       |       |
       |       |
       |       |  C
       |       +--\
      [ ]      |   \
      2M       |    ----+ Q2 (PNP, b2 = 180)
       |     B |   /|
       |       |  / |
       |       +--+
       |       | E
      -+-------+---------- GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Complementary Push-Pull Config:** Collectors of NPN $Q_1$ (via $R_C = 750\ \Omega$) and PNP $Q_2$ (direct to Ground) are configured to drive a common emitter output node $V_o$.
2. **Input Coupling:** Input $V_i$ coupled via coupling capacitor to base junction. High-value base resistor $R_S = 2\text{ M}\Omega$ connected from base junction to Ground.
3. **Midpoint Potential:** Quiescent output potential is $V_o = 9\text{ V}$.

In integrated circuits (ICs), resistors are highly space-inefficient. Instead, transistors are configured to act as active current sources. The **Current Mirror** represents the core bias block:

```
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

*   **Logic:** $Q_1$ is diode-connected (its collector is shorted directly to its base), forcing it to operate in the active region. The current $I_{ref}$ flowing down through resistor $R$ establishes a base-emitter voltage $V_{BE}$ across $Q_1$:

$$
V_{BE} = V_T \ln \left( \frac{I_{ref}}{I_{s1}} \right)
$$

*   Since the base and emitter terminals of $Q_1$ and $Q_2$ are tied directly in parallel, $Q_2$ is subjected to the exact same $V_{BE}$.
*   Assuming perfectly matched, identical transistors ($I_{s1} = I_{s2}$):

$$
I_{out} = I_{s2} e^{V_{BE} / V_T} = I_{ref}
$$

The output current $I_{out}$ in the collector of $Q_2$ mirrors the reference current $I_{ref}$, behaving as a constant current sink regardless of the load voltage connected at $Q_2$'s collector.

---

### 1.2 Finite $\beta$ Effect Analysis
In practical BJTs, base currents are non-zero:

$$
I_{ref} = I_{C1} + I_{B1} + I_{B2} = I_C + \frac{I_C}{\beta} + \frac{I_C}{\beta} = I_C \left( 1 + \frac{2}{\beta} \right)
$$

$$
I_{out} = I_C = I_{ref} \left( \frac{1}{1 + 2/\beta} \right)
$$

If $\beta = 100$, the output current is $2\%$ lower than the reference current due to base current robbing.

---

## 2. The Wilson Current Mirror
*[Appeared in: 2017 Q3(b)]*

**Question:**
* **(b)** Calculate the current $I$ through each of the transistors $Q_2$ and $Q_3$ in the Wilson current mirror circuit shown below. Assume identical transistors with $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. **[04 Marks]**

##### Circuit Diagram (Q.3(b)):
```
      +6 V
       |
      [ ] R = 1.3k
       |
       +---------+
       |         |
       |       B | C
     C |      +--+
    +--+   +--| Q3
    |  |   |  +--+
    | Q1   |     | E
    +--+   |     +----------> Output (Current I)
       |   |     |
       +---+-----+ (Node connecting Q1_base, Q2_base, and Q3_emitter/Q2_collector)
       |         |
     B |       C |
    +--+      +--+
    |         | Q2
    |         +--+
       |         | E
      GND       GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Circuit Architecture:** Wilson current mirror consisting of three matched NPN BJTs ($Q_1, Q_2, Q_3$).
2. **Current Equations:**
   * Reference input current:

$$
I_{ref} = \frac{6\text{ V} - V_{BE1} - V_{BE3}}{R} = \frac{6\text{ V} - 0.7\text{ V} - 0.7\text{ V}}{1.3\text{ k}\Omega} = 3.538\text{ mA}
$$

   * Output collector current $I$ taking finite $\beta$ into account:

$$
I = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right)
$$

### 2.1 Circuit Layout and Mechanics
The Wilson current mirror uses three transistors to drastically increase output resistance and reduce base current errors:

```
                       Iout (to load)
                         |
                        Q3
                         |
           +-------------+-------+
           |                     |
          [R]                    |
           |                     |
        Iref ---> Q1 ----------- Q2
           |      |              |
           +------+              |
           |                     |
          Gnd                   Gnd
```

1.  **Operation:** $Q_3$ is in series with the output branch. Its emitter current drives the diode-connected $Q_2$ and the base of $Q_1$.
2.  **Error Correction:** If output current $I_{out}$ rises, the current in $Q_2$ increases. This increases the base-emitter voltage of $Q_2$ and $Q_1$. $Q_1$ conducts more heavily, pulling down on the base voltage of $Q_3$. This negative feedback counteracts the initial rise, stabilizing $I_{out}$.

---

### 2.2 Mathematical Output Current Derivation
Assume identical, matched transistors with finite $\beta$:
1.  Collector current of $Q_1$ is:

$$
I_{C1} = I_{ref} - I_{B3}
$$

2.  Since $Q_1$ and $Q_2$ form a basic mirror, their base-emitter terminals are in parallel:

$$
I_{C1} = I_{C2} = I_C
$$

3.  The emitter current of $Q_3$ feeds the bases of $Q_1, Q_2$ and the collector of $Q_2$:

$$
I_{E3} = I_{C2} + I_{B1} + I_{B2} = I_C + \frac{2 I_C}{\beta} = I_C \left( 1 + \frac{2}{\beta} \right)
$$

4.  The output current is the collector current of $Q_3$:

$$
I_{out} = I_{C3} = \frac{\beta}{\beta + 1} I_{E3} = \frac{\beta}{\beta + 1} I_C \left( 1 + \frac{2}{\beta} \right) = I_C \left( \frac{\beta + 2}{\beta + 1} \right)
$$

5.  Substitute $I_C = I_{ref} - I_{B3} = I_{ref} - \frac{I_{out}}{\beta}$:

$$
I_{out} = \left( I_{ref} - \frac{I_{out}}{\beta} \right) \left( \frac{\beta + 2}{\beta + 1} \right) \Rightarrow I_{out} \left( 1 + \frac{\beta + 2}{\beta^2 + \beta} \right) = I_{ref} \left( \frac{\beta + 2}{\beta + 1} \right)
$$

$$
I_{out} \left( \frac{\beta^2 + 2\beta + 2}{\beta(\beta + 1)} \right) = I_{ref} \left( \frac{\beta(\beta + 2)}{\beta(\beta + 1)} \right) \Rightarrow I_{out} = I_{ref} \left( \frac{\beta^2 + 2\beta}{\beta^2 + 2\beta + 2} \right)
$$

6.  Divide numerator and denominator by $\beta^2 + 2\beta$:

$$
I_{out} = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + 2\beta}} \right) \approx I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right)
$$

For $\beta = 100$, the transfer error is reduced to a minuscule $0.02\%$.

---

### 2.3 Worked Wilson Current Mirror Numerical
*[Appeared in: 2017 Q3(b)]*

**Question:**
* **(b)** Calculate the current $I$ through each of the transistors $Q_2$ and $Q_3$ in the Wilson current mirror circuit shown below. Assume identical transistors with $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. **[04 Marks]**

##### Circuit Diagram (Q.3(b)):
```
      +6 V
       |
      [ ] R = 1.3k
       |
       +---------+
       |         |
       |       B | C
     C |      +--+
    +--+   +--| Q3
    |  |   |  +--+
    | Q1   |     | E
    +--+   |     +----------> Output (Current I)
       |   |     |
       +---+-----+ (Node connecting Q1_base, Q2_base, and Q3_emitter/Q2_collector)
       |         |
     B |       C |
    +--+      +--+
    |         | Q2
    |         +--+
       |         | E
      GND       GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Circuit Architecture:** Wilson current mirror consisting of three matched NPN BJTs ($Q_1, Q_2, Q_3$).
2. **Current Equations:**
   * Reference input current:

$$
I_{ref} = \frac{6\text{ V} - V_{BE1} - V_{BE3}}{R} = \frac{6\text{ V} - 0.7\text{ V} - 0.7\text{ V}}{1.3\text{ k}\Omega} = 3.538\text{ mA}
$$

   * Output collector current $I$ taking finite $\beta$ into account:

$$
I = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right)
$$

**Problem Details:**
A Wilson current mirror is biased with $V_{CC} = 6\text{ V}$ and a reference resistor $R = 1.3\text{ k}\Omega$. Assume identical transistors with $\beta = 100$ and $V_{BE} = 0.7\text{ V}$. Calculate the current through transistors $Q_2$ and $Q_3$.

#### Step-by-Step Solution:

##### Step 1: Calculate reference current ($I_{ref}$)
The reference path contains the resistor $R$ in series with two forward-biased base-emitter junctions ($Q_1$ and $Q_3$):

$$
I_{ref} = \frac{V_{CC} - V_{BE1} - V_{BE3}}{R} = \frac{6\text{ V} - 0.7\text{ V} - 0.7\text{ V}}{1.3\text{ k}\Omega} = \frac{4.6\text{ V}}{1300\ \Omega} \approx 3.538\text{ mA}
$$

##### Step 2: Calculate output current ($I_{out}$ or $I_{C3}$)
Using the derived Wilson current equation:

$$
I_{C3} = I_{ref} \left( \frac{1}{1 + \frac{2}{\beta^2 + \beta}} \right)
$$

For $\beta = 100$:

$$
\text{Error Term} = \frac{2}{100^2 + 100} = \frac{2}{10100} \approx 0.000198
$$

$$
I_{C3} = 3.538\text{ mA} \times \left( \frac{1}{1.000198} \right) \approx 3.537\text{ mA}
$$

##### Step 3: Determine collector currents
Since the Wilson mirror is highly accurate:
*   Current through $Q_3 = 3.537\text{ mA}$
*   Current through $Q_2 = I_{C2} = I_{C1} \approx 3.537\text{ mA}$

---

## 3. Differential Amplifiers

### 3.1 Symmetrical BJT Differential Pair DC Analysis
*[Appeared in: 2017 Q3(c)]*

**Question:**
* **(c)** Calculate the DC voltages $V_{o1}$ and $V_{o2}$ for the symmetrical differential BJT amplifier circuit shown below. **[04 Marks]**

##### Circuit Diagram (Q.3(c)):
```
                 +9V
                  |
         +--------+--------+
         |                 |
        [ ] RC1           [ ] RC2
        [ ] 3.9k          [ ] 3.9k
         |                 |
  Vo1 o--+                 +--o Vo2
         |                 |
       C |               C |
      +--+              +--+
    B |  | Q1         B |  | Q2
  ----+  |            --+  |
      +--+              +--+
       | E               | E
       +--------+--------+
                |
               [ ] REE
               [ ] 3.3k
                |
               -9V
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Symmetrical Structure:** Matched transistors $Q_1, Q_2$ with identical collector resistors $R_{C1} = R_{C2} = 3.9\text{ k}\Omega$.
2. **Biasing Resistor:** Emitter resistor $R_{EE} = 3.3\text{ k}\Omega$ connected to negative DC rail $-9\text{ V}$.
3. **Collector DC Voltages:**
   * Total emitter bias current:

$$
I_{EE} = \frac{0\text{ V} - V_{BE} - (-9\text{ V})}{R_{EE}} = \frac{9\text{ V} - 0.7\text{ V}}{3.3\text{ k}\Omega} = 2.515\text{ mA}
$$

   * Emitter current of each half-circuit:

$$
I_{E1} = I_{E2} = \frac{I_{EE}}{2} = 1.258\text{ mA}
$$

   * Output DC collector voltages:

$$
V_{o1} = V_{o2} = V_{CC} - I_{C} R_C \approx 9\text{ V} - (1.258\text{ mA} \times 3.9\text{ k}\Omega) = 4.095\text{ V}
$$

**Problem Details:**
A symmetrical BJT differential amplifier is connected to $+9\text{ V}$ and $-9\text{ V}$ power supplies. Emitters are tied together and connected to the negative rail through tail resistor $R_{EE} = 3.3\text{ k}\Omega$. Symmetrical collector resistors are $R_C = 3.9\text{ k}\Omega$. Calculate the individual DC collector voltages ($V_{o1}, V_{o2}$) under zero input conditions ($0\text{V}$ at both bases). Assume matched transistors with $V_{BE} = 0.7\text{ V}$.

#### Step-by-Step Solution:

##### Step 1: Calculate the common emitter voltage ($V_E$)
With both bases grounded ($0\text{V}$):

$$
V_E = V_B - V_{BE} = 0 - 0.7\text{ V} = -0.7\text{ V}
$$

##### Step 2: Calculate the total tail current ($I_{EE}$) flowing through $R_{EE}$

$$
I_{EE} = \frac{V_E - (-V_{EE})}{R_{EE}} = \frac{-0.7\text{ V} - (-9\text{ V})}{3.3\text{ k}\Omega} = \frac{8.3\text{ V}}{3300\ \Omega} \approx 2.515\text{ mA}
$$

##### Step 3: Split the tail current between the matched transistors
Due to perfect circuit symmetry, the tail current splits exactly in half:

$$
I_{E1} = I_{E2} = \frac{I_{EE}}{2} = \frac{2.515\text{ mA}}{2} = 1.2575\text{ mA}
$$

Assuming $I_C \approx I_E$:

$$
I_{C1} = I_{C2} \approx 1.2575\text{ mA}
$$

##### Step 4: Calculate the DC output voltages at the collectors

$$
V_{o1} = V_{CC} - I_{C1} R_C = 9\text{ V} - (1.2575\text{ mA} \times 3.9\text{ k}\Omega) = 9\text{ V} - 4.904\text{ V} = 4.096\text{ V}
$$

$$
V_{o2} = V_{CC} - I_{C2} R_C = 9\text{ V} - 4.904\text{ V} = 4.096\text{ V}
$$

Under zero input conditions, the DC voltages at both collector terminals are identical: $V_{o1} = V_{o2} = 4.096\text{ V}$.

---

## 4. Multi-Stage Op-Amp Feedback Networks
*[Appeared in: 2022 Q7(b)]*

**Question:**
* **(b)** Calculate the closed-loop gain $V_o/V_i$ of the two-stage cascaded op-amp feedback amplifier network shown below. **[04/05 Marks, CO2]**

##### Circuit Diagram (Q.7(b)):
```
                      4k
             +-------[  ]-----------------+
             |                            |
             |   10k                      |
             +--[  ]------+               |
             |            |               |
       5k    |    |\      |      |\       |
   Vi -[  ]---+----|-\     |   +--|+\      |
                   |  \    |   |  |  \     |
     +             |   >---+---+  |   \    |
     -  -----------|+ /           |    >---+-----+---> Vo
                   | /            |   /          |    +
                  -+-           +-|- /          [2k]  -
                  GND           | |/             |
                                +----------------+
                                |
                              [10k]
                                |
                               -+-
                               GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Op-Amp Stage 1 (Summing Inverting Configuration):**
   * Non-inverting (+) terminal is grounded.
   * Inverting (-) terminal receives input $V_i$ via $R_{in1} = 5\text{ k}\Omega$.
   * Feedback paths:
     * $R_{f1} = 10\text{ k}\Omega$ connected from Stage 1 output ($V_{o1}$).
     * $R_{f12} = 4\text{ k}\Omega$ connected from Stage 2 output ($V_o$).
2. **Op-Amp Stage 2 (Non-Inverting Gain Configuration):**
   * Non-inverting (+) terminal receives Stage 1 output $V_{o1}$.
   * Inverting (-) terminal is connected to feedback resistor $R_{f2} = 2\text{ k}\Omega$ (connected to $V_o$) and resistor $R_{g2} = 10\text{ k}\Omega$ (connected to Ground).
3. **Gain Formulation:** Solve using nodal equations at the inverting node of Stage 1.

### 4.1 Closed-loop gain analysis of multi-stage loops
In high-performance integrated designs, feedback loops are frequently wrapped around multiple cascaded op-amp stages to stabilize overall gain.

### 4.2 Worked Closed-Loop Gain Derivation
*[Appeared in: 2022 Q7(b)]*

**Question:**
* **(b)** Calculate the closed-loop gain $V_o/V_i$ of the two-stage cascaded op-amp feedback amplifier network shown below. **[04/05 Marks, CO2]**

##### Circuit Diagram (Q.7(b)):
```
                      4k
             +-------[  ]-----------------+
             |                            |
             |   10k                      |
             +--[  ]------+               |
             |            |               |
       5k    |    |\      |      |\       |
   Vi -[  ]---+----|-\     |   +--|+\      |
                   |  \    |   |  |  \     |
     +             |   >---+---+  |   \    |
     -  -----------|+ /           |    >---+-----+---> Vo
                   | /            |   /          |    +
                  -+-           +-|- /          [2k]  -
                  GND           | |/             |
                                +----------------+
                                |
                              [10k]
                                |
                               -+-
                               GND
```

##### AI-Ready Structural Walkthrough & Parameter Definitions:
1. **Op-Amp Stage 1 (Summing Inverting Configuration):**
   * Non-inverting (+) terminal is grounded.
   * Inverting (-) terminal receives input $V_i$ via $R_{in1} = 5\text{ k}\Omega$.
   * Feedback paths:
     * $R_{f1} = 10\text{ k}\Omega$ connected from Stage 1 output ($V_{o1}$).
     * $R_{f12} = 4\text{ k}\Omega$ connected from Stage 2 output ($V_o$).
2. **Op-Amp Stage 2 (Non-Inverting Gain Configuration):**
   * Non-inverting (+) terminal receives Stage 1 output $V_{o1}$.
   * Inverting (-) terminal is connected to feedback resistor $R_{f2} = 2\text{ k}\Omega$ (connected to $V_o$) and resistor $R_{g2} = 10\text{ k}\Omega$ (connected to Ground).
3. **Gain Formulation:** Solve using nodal equations at the inverting node of Stage 1.

**Problem Details:**
Calculate the closed-loop gain $V_o/V_i$ of the two-stage cascaded op-amp feedback amplifier shown below.
*   **Stage 1:** Inverting summing amplifier. Inputs are: $V_i$ through a $5\text{ k}\Omega$ resistor, output $V_{o1}$ of Stage 1 through a $10\text{ k}\Omega$ resistor, and overall output $V_o$ through a $4\text{ k}\Omega$ resistor.
*   **Stage 2:** Non-inverting amplifier driven by $V_{o1}$. Feedback resistors: $R_{f2} = 2\text{ k}\Omega, R_{g2} = 10\text{ k}\Omega$.

#### Step-by-Step Solution:

##### Step 1: Analyze Stage 2 (Non-Inverting Stage)
The input to Stage 2 is $V_{o1}$, and the output is $V_o$:

$$
V_o = V_{o1} \left( 1 + \frac{R_{f2}}{R_{g2}} \right) = V_{o1} \left( 1 + \frac{2\text{ k}\Omega}{10\text{ k}\Omega} \right) = 1.2 V_{o1}
$$

Express the intermediate voltage $V_{o1}$ in terms of the final output $V_o$:

$$
V_{o1} = \frac{V_o}{1.2} = \frac{5}{6} V_o
$$

##### Step 2: Apply KCL at the inverting node of Stage 1
By the virtual ground principle, the inverting input of Stage 1 is held at $0\text{V}$. The sum of currents entering this node must equal zero:

$$
\frac{V_i - 0}{5\text{ k}\Omega} + \frac{V_{o1} - 0}{10\text{ k}\Omega} + \frac{V_o - 0}{4\text{ k}\Omega} = 0 \Rightarrow \frac{V_i}{5} + \frac{V_{o1}}{10} + \frac{V_o}{4} = 0
$$

##### Step 3: Substitute $V_{o1} = \frac{5}{6} V_o$ into the KCL equation

$$
\frac{V_i}{5} + \frac{\frac{5}{6} V_o}{10} + \frac{V_o}{4} = 0 \Rightarrow \frac{V_i}{5} + \frac{V_o}{12} + \frac{V_o}{4} = 0
$$

$$
\frac{V_i}{5} + V_o \left( \frac{1}{12} + \frac{3}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + V_o \left( \frac{4}{12} \right) = 0 \Rightarrow \frac{V_i}{5} + \frac{V_o}{3} = 0
$$

##### Step 4: Solve for the closed-loop voltage gain ($A_v$)

$$
\frac{V_o}{3} = -\frac{V_i}{5} \Rightarrow A_v = \frac{V_o}{V_i} = -\frac{3}{5} = -0.6
$$

The overall closed-loop gain of the multi-stage feedback system is exactly $-0.6$.

[Previous](09_CMOS_Logic.md) | [Home](index.md)
