# Class Note Digitization - Phase 3 (Pages 21 to 30)

---

## Page 21: Analog_Class_Note_Part-1-021.png

### Content

$$\Rightarrow \frac{v_i}{v_s} = \frac{R_i}{R_i + R_s} \qquad \text{--- (I)}$$

$$v_o = \frac{R_L}{R_L + R_o} A_{v_{NL}} \cdot v_i$$

$$\Rightarrow \frac{v_o}{v_i} = \frac{R_L}{R_L + R_o} A_{v_{NL}} \qquad \text{--- (II)}$$

* **Total/Overall Voltage Gain:**
  $$\boxed{A_{v_T} = \frac{v_o}{v_s} = \frac{v_o}{v_i} \cdot \frac{v_i}{v_s}}$$

---

### Cascaded Systems
A multi-stage cascaded amplifier system containing $n$ stages in series:

```
        v_i1         v_o1       v_o2                 v_o(n-1)
  v_i  +----+       +----+     +----+                 +----+       v_o
 ----> | A1 | ----> | A2 | --> | A3 | ... ----------> | An | ----> across
 (Z_i) +----+ (Z_o1)+----+     +----+                 +----+ (Z_on)  R_L
```

* **Formulas:**
  $$v_{i_1} = v_i \quad ; \quad v_{i_2} = v_{o_1}$$
  $$\therefore v_{i_n} = v_{o_{n-1}}$$
  $$A_{v_1} = \frac{v_{o_1}}{v_{i_1}} \quad ; \quad A_{v_2} = \frac{v_{o_2}}{v_{i_2}}$$
  $$A'_{v_T} = \frac{v_{o_2}}{v_{i_1}} = \frac{v_{o_2}}{v_{i_2}} \cdot \frac{v_{o_1}}{v_{i_1}} = A_{v_2} \cdot A_{v_1}$$

---

## Page 22: Analog_Class_Note_Part-1-022.png

### Metadata
- **Date**: 22 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Cascaded Systems & Example 5.14

### Content
* Gain for first 2 stages:
  $$\therefore A'_{v_T} = A_{v_1} \times A_{v_2}$$
* Gain for $n$ stages:
  $$\therefore A_{v_T} = A_{v_1} \times A_{v_2} \times A_{v_3} \times \dots \times A_{v_n}$$

---

### Example 5.14
A two-stage amplifier circuit represented by blocks:

```
          R_s = 1k
         -[===]----+--------+                Z_o1 = 12k        Z_o2 = 5.1k
        |          |        |                 -[===]-------------[===]----+---+
    ( ~ ) v_s     [Ri]     === (A_vNL1 * v_i) (~)    (A_vNL2)    (~)      |   |
        |      10k| (v_i1)  |                 |      (v_o1=v_i2) |      [R_L] v_o
        |          |        |                 |                  |       8.2k |
        +----------+--------+                 +------------------+--------+---+
```
* **Stage 1 (Emitter Follower):**
  * $Z_i = 10\text{ k}\Omega$
  * $Z_o = 12\text{ k}\Omega$
  * $A_{v_{NL}} \approx 1$
* **Stage 2 (Common Base):**
  * $Z_i = 26\ \Omega$
  * $Z_o = 5.1\text{ k}\Omega$
  * $A_{v_{NL}} = 240$
  * Connected across load resistor $R_L = 8.2\text{ k}\Omega$.

* **Questions:**
  * (a) The loaded gain for each stage.
  * (b) The total gain, $A_v$ & $A_{v_s}$.
  * (c) The total current gain.
  * (d) The total gain if the emitter follower were removed.

---

## Page 23: Analog_Class_Note_Part-1-023.png

### Solution to Example 5.14

#### (a) Loaded Gain for Each Stage:
$$A_{v_L} = \frac{R_L}{R_L + R_o} A_{v_{NL}}$$
$$\Rightarrow v_o = \frac{R_L}{R_L + R_o} A_{v_{NL}} v_i$$

1. **For Emitter-Follower (Stage 1):**
   * Input impedance of Stage 2 acts as load: $R_L = Z_{i_2} = 26\ \Omega$
   * Output impedance of Stage 1: $R_o = Z_{o_1} = 12\text{ k}\Omega$
   * No-load voltage gain: $A_{v_{NL}} \approx 1$
   $$A_{v_1} = \frac{26}{26 + 12} \cdot 1 = 0.68$$
   *(Note: There is a unit mismatch in the student's notebook: $Z_{i_2} = 26\ \Omega$ and $Z_{o_1} = 12\text{ k}\Omega$. The calculation in the notes treats them both as unitless values ($26$ and $12$), yielding $\frac{26}{38} = 0.68$. The mathematically correct calculation with matching units is $\frac{26}{26 + 12000} \approx 0.002$.)*

2. **For Common-Base (Stage 2):**
   * Load resistor: $R_L = 8.2\text{ k}\Omega$
   * Output impedance of Stage 2: $R_o = 5.1\text{ k}\Omega$
   * No-load voltage gain: $A_{v_{NL}} = 240$
   $$A_{v_2} = \frac{8.2}{8.2 + 5.1} \times 240 = 147.96$$

---

## Page 24: Analog_Class_Note_Part-1-024.png

### Solution to Example 5.14 (Continued)

#### (b) Total Gain $A_v$ & $A_{v_s}$:
* **Total loaded voltage gain ($A_v$):**
  $$A_v = A_{v_1} A_{v_2} = 0.68 \times 147.96 = 100.61$$
* **Input Voltage Divider:**
  $$\frac{v_i}{v_s} = \frac{R_i}{R_i + R_s} = \frac{10\text{ k}}{10\text{ k} + 1\text{ k}} = 0.9$$
  where $R_i = 10\text{ k}\Omega$ and $R_s = 1\text{ k}\Omega$.
* **Overall loaded gain ($A_{v_s}$):**
  $$A_{v_s} = \frac{v_i}{v_s} A_v = 0.9 \times 100.61 = 91.46$$

#### (c) Total Current Gain ($A_i$):
$$A_i = -A_v \frac{Z_i}{R_L}$$
where $Z_i = Z_{i_1} = 10\text{ k}\Omega$ and $R_L = 8.2\text{ k}\Omega$.
$$A_i = -100.61 \times \frac{10\text{ k}}{8.2\text{ k}} = -122.69$$

---

## Page 25: Analog_Class_Note_Part-1-025.png

### Example 5.15
A two-stage Common-Emitter (CE) BJT amplifier circuit:

```
                         +20V
                          |
             +------+-----+---------------+------+
             |      |     |               |      |
            [15k]  [2.2k]|               [15k]  [2.2k]
             |      |     |               |      |
      0.05u  |      |     | 0.05u         |      |
  v_i --||---+      |     +---||----------+      |
  (25uV)     |   Q1 |    /                |   Q2 |
            [4.7k]  |---+                [4.7k]  |---+---||--- v_o
             |      |                    |       |
            ===    [1k] === (bypass)    ===     [1k] === (bypass)
            GND     |   GND             GND      |   GND
                   ===                          ===
                   GND                          GND
```
* **Parameters:** Both NPN BJTs $Q_1, Q_2$ have $\beta = 200$.

* **Questions:**
  * (a) Calculate the no-load voltage gain, input voltage, and output voltage.
  * (b) Calculate the overall gain and output voltage if a $4.7\text{ k}\Omega$ load is applied to the second stage.
  * (c) Calculate input impedance & output impedance (for 1st and 2nd stages).

#### (a) Solution Method:
* Voltage gain of a single stage:
  $$A_v = -\frac{R_C}{r_e}$$
  *(Note: The writer uses $R_e$ to refer to the collector resistor $R_C$ in formulas.)*
* Emitter impedance loading:
  $$A_{v_1} = -\frac{R_{C1} \parallel R_{1(stage2)} \parallel R_{2(stage2)} \parallel \beta r_{e2}}{r_{e1}}$$
  $$A_{v_2} = -\frac{R_{C2}}{r_{e2}}$$
  $$\text{Total gain } A_{v_T} = A_{v_1} \cdot A_{v_2}$$

---

## Page 26: Analog_Class_Note_Part-1-026.png

### Content

* Syllabus note: Class Test 1 (CT-1) will cover Chapters 4-5 up to today's topic.

#### (b) Output Voltage with Load $R_L = 4.7\text{ k}\Omega$:
$$A_{v_T} = \frac{R_L}{R_L + Z_o} A_{v_{NL}}$$
where:
* $R_L = 4.7\text{ k}\Omega$
* $Z_o = R_{C2} = 2.2\text{ k}\Omega$ (Output impedance of 2nd stage)

#### (c) Impedances:
* **Input Impedance ($Z_i$):**
  $$Z_i = R_1 \parallel R_2 \parallel \beta r_{e1} \quad \text{(for 1st stage)}$$
* **Output Impedance ($Z_o$):**
  $$Z_o = R_{C2} = 2.2\text{ k}\Omega \quad \text{(for 2nd stage)}$$

---

### Example 5.16: Cascode Connection
A stacked Cascode BJT connection:

```
                  V_o2
                   |
                +--+ (Collector Q2)
             Q2 |
      Base2 --->|
      (AC GND)   \ (Emitter Q2)
                  + (Node V_C1 = V_E2)
             Q1  / (Collector Q1)
      v_in ---->|
                 \ Emitter1 (GND)
                  |
                 ===
                 GND
```

* Stage 1 Voltage Gain:
  $$A_{v_1} = -\frac{R_C}{r_e}$$
  * *Student's hand-written notes:*
    * "Re পাব না" (We won't get $R_E$ - since the emitter of $Q_1$ is grounded).
    * "Rc হবে second stage এর?" (Will it be $R_C$ of the second stage? No, the load for $Q_1$ is the input impedance of $Q_2$, which is $\approx r_{e2}$).

---

## Page 27: Analog_Class_Note_Part-1-027.png

### Metadata
- **Course**: ANALOG - LAB 2
- **Date**: 24 November, 2025
- **Instructor**: Moloy Sir
- **Topic**: Experiment 02 (JFET Common Source Amplifier)

### Content
* AC Input signal: $V_{in} = 10\text{ mV}$ or $20\text{ mV}$

#### Circuit Diagram: N-Channel JFET (2N5458) Common-Source Amplifier
```
                          V_dd = +15V
                             |
                           [4.7k]
                             |
               0.1uF         +---||--- Output (V_out)
        V_in ---||---+-- D    |
                     | (Gate)/ Q1 (2N5458)
                    [1M]    | (Source)
                     |      +----+
                    ===     |    |
                    GND   [1k]  === (10uF bypass)
                            |   GND
                           ===
                           GND
```

#### Pin Configuration (TO-92 Package)
```
          +-------+
          |       |  Flat Side Facing Front
          | 2N5458|
          +-------+
           |  |  |
           D  S  G   (Drain, Source, Gate - Left to Right)
```

---

## Page 28: Analog_Class_Note_Part-1-028.png

### Metadata
- **Date**: 24 November, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Topic**: Two-stage JFET Amplifier (Example 8.16)

### Example 8.16
Determine the DC bias, voltage gain, input impedance, and output impedance of the following two-stage JFET amplifier:

```
                            V_DD = +20V
                              |
               +-------+------+---------------+-------+
               |       |                      |       |
             [2.4k]  [3.3M]                 [2.4k]  [3.3M]
               |       |                      |       |
        0.05u  |       |               0.05u  |       |
  v_in ---||---+       |         +------||----+       |
               |     G |         |            |     G |
               |   +---+         |            |   +---+
               | Q1|             |            | Q2|
               |   +---+         |            |   +---+
               |       | S       |            |       | S
               |     [680] ===   |            |     [680] === (bypass)
               |       |   GND   |            |       |   GND
              ===     ===       ===          ===     ===
              GND     GND       GND          GND     GND
```
* **JFET Parameters (Matched):** $I_{DSS} = 10\text{ mA}$, $V_P = -4\text{ V}$.

#### Solution & AC Analysis:
1. **Transconductance ($g_m$):**
   $$g_m = 2.6\text{ mS} \quad (\text{calculated from DC Q-point})$$
2. **Voltage Gain of Stage 2 ($A_{v_2}$):**
   $$A_{v_2} = -g_m \cdot R_{D_2} = -2.6\text{ mS} \cdot 2.4\text{ k}\Omega = -6.24$$
3. **Voltage Gain of Stage 1 ($A_{v_1}$):**
   Since the input impedance of Stage 2 ($R_{G2} = 3.3\text{ M}\Omega$) is much larger than the collector load of Stage 1 ($R_{D1} = 2.4\text{ k}\Omega$):
   $$A_{v_1} = -g_m \cdot (R_{D_1} \parallel R_{G_2}) \approx -g_m \cdot R_{D_1} = -6.24$$
4. **Total Voltage Gain ($A_v$):**
   $$A_v = A_{v_1} A_{v_2} = (-6.24) \times (-6.24) = 38.94$$
5. **Impedances:**
   * **Input Impedance ($Z_i$):** $Z_i = R_{G_1} = 3.3\text{ M}\Omega$
   * **Output Impedance ($Z_o$):** $Z_o = R_{D_2} = 2.4\text{ k}\Omega$

---

## Page 29: Analog_Class_Note_Part-1-029.png

### Example 8.17: JFET-BJT Cascade Amplifier
A JFET first stage cascaded into a BJT second stage:

```
                            V_CC = +20V
                              |
               +-------+------+---------------+-------+-------+
               |       |                      |       |       |
             [2.4k]  [3.3M]                 [15k]   [2.2k]    |
               |       |                      |       |       |
        0.05u  |       |                0.5u  |       |  0.5u |
  v_i ----||---+       |         +------||----+       +---||--- v_o
               |     G |         |            |    Q2 |
               |   +---+         |          [4.7k]    |----+
               | Q1|             |            |       |
               |   +---+         |            |     [1k] === (bypass)
               |       | S       |            |       |   GND
              ===     [680] === ===          ===     ===
              GND      |    GND GND          GND     GND
                      ===
                      GND
```
* **Stage 1 (JFET):** $I_{DSS} = 10\text{ mA}$, $V_P = -4\text{ V}$.
* **Stage 2 (BJT):** Voltage divider bias with $R_1=15\text{ k}\Omega$, $R_2=4.7\text{ k}\Omega$, $R_C=2.2\text{ k}\Omega$, $R_E=1\text{ k}\Omega$.

* **Questions:**
  * Determine Input Impedance ($Z_i$), Output Impedance ($Z_o$), Voltage Gain ($A_v$), and Output Voltage ($v_o$).

#### Solution Method:
* **Total Gain:**
  $$A_v = A_{v_1} \cdot A_{v_2}$$
* **Stage 2 Loaded Gain ($A_{v_2}$):**
  $$A_{v_2} = -\frac{R_C}{r_{e2}}$$
* **Stage 1 Loaded Gain ($A_{v_1}$):**
  $$A_{v_1} = -g_m \cdot (R_D \parallel R'_i)$$
  where $R'_i$ is the AC input impedance of the second (BJT) stage:
  $$R'_i = R_1 \parallel R_2 \parallel \beta r_{e2}$$

---

## Page 30: Analog_Class_Note_Part-1-030.png

### Topic: Frequency Response

#### Gain vs Frequency Response Curve
```
   Voltage Gain (Av)
     ^
  Av_max +             .-------------.
         |            /               \
 0.707Av +           +                 +
         |          / |               | \
         |         /  |               |  \
         +--------+---+---------------+---+--------> Frequency (f)
                  |   f_L             f_H |
                  |<---- Midband Freq --->|
```
* **Cutoff Frequencies:**
  * $f_L$: Lower cutoff frequency.
  * $f_H$: Higher cutoff frequency.
  * At cutoff frequencies, gain drops to $70.7\%$ (or $-3\text{ dB}$) of maximum gain.

#### Core Concepts (Bengali & English Notes):
* **DC Analysis** $\rightarrow Q$-point বের করা (Calculates/finds the $Q$-point).
* **AC Analysis** $\rightarrow$ Input/Output Impedances and Gain calculations. This yields the maximum gain.
* **Maximum Gain** is obtained in the **Midband Frequency** range.
* **Frequency Examples:**
  * What is the gain at $20\text{ Hz}$?
  * If gain at $1000\text{ Hz}$ is $1$ ($10\text{ dB}$), what will be the gain at $10\text{ Hz}$?
* **Cutoff Frequency definition:** The frequencies beyond which gain drops significantly (1 for lower, 1 for higher cutoff).

---

#### Circuit Diagram: Cascode stacked BJT amplifier
```
                       V_CC
                        |
             +----+-----+-----+
             |    |           |
            [R1]  |         [R_C]
             |    |           |
             +----+--- B2     +--- Output
             |    |           |
            [R2]  |       Q2 /  (CB Stage)
             |    |         |
             +----+---------+   (Node V_C1 = V_E2)
             |    |        / Q1 (CE Stage)
            [R3]  |       |-- Input
             |    |        \
            ===  ===       === (bypassed Emitter)
            GND  GND       GND
```
* Note: A cascode features stacked transistors to achieve wide bandwidth and high input impedance.
