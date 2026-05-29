# Class Note Digitization - Phase 6 (Part 1, Pages 51-57 & Part 2, Pages 1-3)

---

# Part 1: Pages 51 to 57

## Page 51: Analog_Class_Note_Part-1-051.png

### Circuit Diagram: BJT Common-Emitter Amplifier
```
                            V_CC = +20V
                             |
               +-------+-----+---------------+
               |       |                     |
             [R1]    [R_C]                 [R_L]
             40k      2.2k                  2.2k
               |       |                     |
     C_S       |       |       C_C           |
  v_i --||-----+-- B   |   +----||-----------*--- Output (V_o)
 (10uF)        |  \ Q1 |   |   (1uF)         |
              [R2]  \  /   |                ===
              10k   C_E \  /                GND
               |   =====   |
              ===  (20uF) [R_E]
              GND   |     2k
                   ===     |
                   GND    ===
                          GND
```
* **Given Parameters:**
  * $V_{CC} = 20\text{ V}$
  * $R_1 = 40\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$
  * $R_C = 2.2\text{ k}\Omega$, $R_E = 2\text{ k}\Omega$, $R_L = 2.2\text{ k}\Omega$
  * $C_S = 10\ \mu\text{F}$, $C_C = 1\ \mu\text{F}$, $C_E = 20\ \mu\text{F}$
  * Transistor: NPN BJT with $\beta = 100$, $r_o = \infty$

### Questions
* (i) Calculate $r_e$.
* (ii) Calculate $A_{v_{\text{mid}}}$.
* (iii) Calculate the cutoff frequencies.

### Solution

#### (i) DC Bias Analysis (Thevenin Equivalent at Base):
$$R_{th} = R_1 \parallel R_2 = 10\text{ k} \parallel 40\text{ k} = 8\text{ k}\Omega$$
$$V_{th} = \frac{R_2}{R_1 + R_2} V_{CC} = \frac{10\text{ k}}{40\text{ k} + 10\text{ k}} \times 20\text{ V} = 4\text{ V}$$
$$I_b = \frac{V_{th} - V_{BE}}{R_{th} + (\beta + 1) R_E} = \frac{4\text{ V} - 0.7\text{ V}}{8\text{ k}\Omega + (101 \times 2\text{ k}\Omega)} = \frac{3.3\text{ V}}{210\text{ k}\Omega} = 0.0157\text{ mA}$$
$$I_E = (\beta + 1) I_b = 101 \times 0.0157\text{ mA} = 1.59\text{ mA}$$
$$r_e = \frac{26\text{ mV}}{I_E} = \frac{26\text{ mV}}{1.59\text{ mA}} = 16.36\ \Omega$$

---

## Page 52: Analog_Class_Note_Part-1-052.png

### Solution (Continued)

* **Approximation Rule Check:**
  Since $\beta R_E = 100 \times 2\text{ k}\Omega = 200\text{ k}\Omega$ and $10 R_2 = 10 \times 10\text{ k}\Omega = 100\text{ k}\Omega$:
  $$\beta R_E \ge 10 R_2 \quad (200\text{ k}\Omega \ge 100\text{ k}\Omega)$$
  Since the inequality holds, the approximate method could also be used.

#### (ii) Midband Voltage Gain ($A_{v_{\text{mid}}}$):
$$A_{v_{\text{mid}}} = -\frac{R_C \parallel R_L}{r_e} = -\frac{2.2\text{ k}\Omega \parallel 2.2\text{ k}\Omega}{16.36\ \Omega} = -\frac{1100\ \Omega}{16.36\ \Omega} = -67.24$$

#### (iii) Cutoff Frequencies:
* BJT & FET configurations cutoff frequency formulas summary. *(Done)*

---

## Page 53: Analog_Class_Note_Part-1-053.png

### Metadata
- **Date**: 5 May, 2025
- **Course**: ECE-2105
- **Instructor**: M.D / S.H
- **Topic**: Operational Amplifiers (Op-Amps)

### Content
* Op-Amp $\rightarrow$ Operational Amplifier $\rightarrow$ এটার gain অনেক high (Its open-loop gain is extremely high).
* যেকোন ধরণের mathematical operation করা যায় (Used to perform various mathematical operations):
  1. Summation (Addition)
  2. Subtraction
  3. Differentiation
  4. Integration

### Applications
1. Amplifier
2. Filter (Active filter)
3. Oscillator
4. Voltage follower (Output follows the input exactly)
5. Comparator
6. Analog-to-Digital Converter (ADC) / Digital-to-Analog Converter (DAC)
7. Multivibrator

---

### Passive Filter Node (Side Concept)
```
          R
     ---[===]---+------ Output
    |           |
  Input        [C]
    |           |
   ===         ===
   GND         GND
```
* Basic filter circuit with only passive elements ($R$, $C$) is called a **Passive Filter**.

---

### Op-Amp Schematic Symbol
```
             +V (Biasing Voltage)
              |
     v_2 ---+ | \
  (Inverting)|  \
     (-)     |   \
             |    \------- Output (v_o)
     v_1 ---|    /
(Non-Inverting) /
     (+)     | /
              |
             -V (Biasing Voltage)
```
* **Gain Relationship:**
  $$A = \frac{v_o}{v_d}$$
  where $v_d$ is the differential input voltage:
  $$v_d = v_1 - v_2$$

---

## Page 54: Analog_Class_Note_Part-1-054.png

### Op-Amp Configurations

#### 1. Non-Inverting Op-Amp Configuration (if $v_2 = 0$)
```
     v_2 --- === (GND)
             | \
             |  \
             |   \------- v_o
     v_1 ----|   /
             |  /
             | /
```
* Inverting terminal is grounded ($v_2 = 0$). Input signal is applied to non-inverting terminal.
* Output voltage:
  $$v_o = A v_1 \quad (\text{in phase, } 0^\circ \text{ phase shift})$$

#### 2. Inverting Op-Amp Configuration (if $v_1 = 0$)
```
     v_2 ----| \
             |  \
             |   \------- v_o
             |   /
     v_1 ---+  /
             | /
            ===
            GND
```
* Non-inverting terminal is grounded ($v_1 = 0$). Input signal is applied to inverting terminal.
* Output voltage:
  $$v_o = A(0 - v_2) \Rightarrow \boxed{v_o = -A v_2}$$
* **Important Note (Bengali):** Inverting amplifier-এ output, input-এর চেয়ে $180^\circ$ phase difference-এ থাকে (phase shift). same ভাবে non-inverting-এর ক্ষেত্রে $0^\circ$ বা in phase-এ থাকে। (In the inverting amplifier, the output is $180^\circ$ out-of-phase with the input. Similarly, in the non-inverting amplifier, it is in-phase or at $0^\circ$).

---

## Page 55: Analog_Class_Note_Part-1-055.png

### Differential Op-Amp (if neither $v_1$ nor $v_2$ is grounded)
* Gain is extremely high:
  $$\boxed{A = 10^5 \text{ to } 10^6}$$

---

### Voltage Transfer Curve
```
   Vo (Output Voltage)
     ^
+Vsat+            .------------------
     |           /
     |          / (Linear Region)
     |         /
   0 +--------+-----------> Vd (Differential Input Voltage)
     |       /
     |      /
-Vsat+-----'
```
* **Analysis (Bengali Notes):**
  * আমরা চাই $\rightarrow$ Saturation-এ না যাক। (We want to avoid operating in saturation).
  * আমরা চাই $\rightarrow$ linear region-এ operate করাতে যাতে করে নিজে control করতে পারি। (We want to operate in the linear region so that we can control the gain ourselves).
  * কিন্তু linear region অনেক ছোট জায়গা (But the linear region is extremely narrow, e.g. $\pm 15\ \mu\text{V}$ for $A=10^6$).
  * তাই আমরা feedback-এর মাধ্যমে gain কমিয়ে আনি (Therefore, we use negative feedback to reduce the gain and stabilize operation).

---

## Page 56: Analog_Class_Note_Part-1-056.png

### Op-Amp Equivalent Circuit (Ideal Case)
```
          Input Terminals                   Output Terminals
        v_1 o------+                         +----o Output (v_o)
                   |                         |
                  [Ri] (Ri = \infty)     (~) | A * v_d (Dependent Source)
                   |                         |
        v_2 o------+                         +----o Ground
```
* **Ideal Op-Amp Parameters:**
  1. Input resistance: $R_i \rightarrow \infty$
  2. Output resistance: $R_o \rightarrow 0$
  3. Bandwidth: $BW \rightarrow \infty$
  4. Open-loop gain: $A \rightarrow \infty$
  5. Slew rate: $SR \rightarrow \infty$
  6. Common-Mode Rejection Ratio: $\text{CMRR} \rightarrow \infty$

* **Bengali Explanatory Notes:**
  * $R_i = \infty$ হলে current pass করবে না। (Since $R_i = \infty$, no current passes into the inputs).
  * $\therefore$ voltage drop কম হবে $\therefore$ gain বেশি। (Therefore, voltage loading is minimized, resulting in high gain).
  * Linear region-এ operate করানোর জন্য gain কমাতে হবে $\rightarrow$ feedback add করতে হবে (output থেকে input-এ)। (To operate in the linear region, we must reduce the gain by adding feedback from the output to the input).

---

### Feedback Classifications

#### 1. Positive Feedback (not preferred for linear operation)
```
      v_1 ---> (+) \
                    \
                     \------- Output (v_o)
      v_2 ---> (-)  /
         |         /
         +---[R]---+
```
* Feedback resistor $R$ connected to the non-inverting terminal.
* **Explanatory Note:** positive feedback $\rightarrow$ দিব না (We do not use this for amplification due to instability / latch-up).

#### 2. Negative Feedback (preferred configuration)
```
      v_1 ---> (+) \
         |          \
         |           \------- Output (v_o)
      v_2|---> (-)  /
         |         /
         +---[R]---+
```
* Feedback resistor $R$ connected to the inverting terminal.
* **Explanatory Note:** neg. feedback $\rightarrow$ দিব (We will use this). Reason $\rightarrow$ stability purpose.

---

## Page 57: Analog_Class_Note_Part-1-057.png

### Concept: Virtual Ground / Virtual Short
```
                       R_f (Feedback)
                +-------[===]-------+
                |                   |
        R_i     |   I_2             |
  V_1 --[===]---*--- (-) \          |
        I_1     V_A       \         |
                          \--------*----- Output (V_o)
                    (+)   /
                     |   /
                    ===
                    GND
```

#### Derivation of Virtual Short:
$$A = \frac{V_o}{V_d} \Rightarrow V_d = \frac{V_o}{A}$$
For $V_o = 10\text{ V}$ and open loop gain $A = 10^6$:
$$V_d = \frac{10}{10^6} = 10\ \mu\text{V} \approx 0$$
$$\because V_d = V_1 - V_2 \approx 0 \Rightarrow \boxed{V_1 \approx V_2}$$
If non-inverting terminal $V_2$ is grounded:
$$\therefore V_1 \approx V_A \approx 0 \quad (\text{Virtual Ground})$$

---

#### Derivation of Closed-Loop Gain for Inverting Op-Amp:
Applying KCL at node $V_A$:
$$I_1 = I_2 + I_i$$
Since input impedance $R_i \rightarrow \infty$, the input current $I_i \rightarrow 0$:
$$\therefore I_1 \approx I_2$$
$$\frac{V_1 - V_A}{R_i} = \frac{V_A - V_o}{R_f}$$
Since $V_A \rightarrow 0$ (virtual ground):
$$\frac{V_1}{R_i} = \frac{-V_o}{R_f} \Rightarrow \boxed{A_v = \frac{V_o}{V_1} = -\frac{R_f}{R_i}}$$
$$\Rightarrow \boxed{V_o = -\left( \frac{R_f}{R_i} \right) V_1}$$

---
---

# Part 2: Pages 1 to 3

## Page 1: Analog_Class_Note_Part-2-001.png

### Metadata
- **Instructor**: MIR Sir

### Topic: Slew Rate ($SR$)
* **Definition (Bengali):** Time-এর সাপেক্ষে output max. যতটুকু change হতে পারে। (The maximum rate of change of the output voltage with respect to time).
* **Mathematical Definition:**
  $$\boxed{\text{Slew Rate} = \left. \frac{dV_{out}}{dt} \right|_{\max}}$$

---

### Waveforms & Distortion

#### 1. Sinusoidal Input (Slew Rate Limitation Distortion)
* An input sine wave of $5\text{ V}$ peak is amplified. If the required output slope exceeds the slew rate limit, the zero-crossings are flattened into linear ramps, distorting the output sine wave.
* **Worst-case slope** occurs at the zero-crossings where $\cos(\omega t)$ is maximum.

#### 2. Square Wave Input response (Transient Transition)
```
  Input Voltage (Square Wave)
    +5V +      .-----------.
        |      |           |
     0  +------+-----------+-------> Time
        |      |           |
    -5V +------'           '

  Output Voltage (Slew-Rate-Limited Actual Response)
    +5V +                  .-------
        |                 /|
     0  +                / |  (Actual Triangular Ramp)
        |               /  |
    -5V +--------------'   |
        |<-- 10 us --->|
```
* **Example:**
  * For input square wave transitions between $\pm 5\text{ V}$ ($\Delta V = 10\text{ V}$):
    If $\text{Slew Rate} = 1\text{ V}/\mu\text{s}$:
    * It takes $\Delta t = \frac{10\text{ V}}{1\text{ V}/\mu\text{s}} = 10\ \mu\text{s}$ to transition.
    * The output wave is distorted into a triangular ramp.
* **Effect:** Signal damage (slew-rate induced distortion).

---

### Digital Logic Concept: Mod-4 Synchronous Counter
```
          FF1 (D-type)            FF2 (J-K type)            FF3 (J-K type)
         +------------+          +------------+          +------------+
  CLK -> | >CLK       |   CLK -> | >CLK       |   CLK -> | >CLK       |
         |  D1     Q1 |----------| J2      Q2 |----------| J3      Q3 |-> Y
         |  Q1'       |          | K2(=1)     |          | K3(=1)     |
         +------------+          +------------+          +------------+
           |                       ^
           |    AND Gate           |
           +-----\__  -------------+
                  ) \
           +-----/__/
           |
         FF3' (Q3')
```
* **State Sequence:** $000 \rightarrow 001 \rightarrow 010 \rightarrow 101 \rightarrow 000 \dots$

---

## Page 2: Analog_Class_Note_Part-2-002.png

### Slew Rate Mathematical Derivation
Let the input voltage be:
$$v_{in}(t) = V_p \sin(\omega t)$$
$$\frac{dv_{in}}{dt} = \omega V_p \cos(\omega t)$$
The maximum value of the derivative is the slew rate ($SR$):
$$\text{SR} = \left. \frac{dv_{in}}{dt} \right|_{\max} = \omega V_p$$
$$\boxed{\text{SR} = 2\pi f V_p}$$
where $f$ is the signal frequency and $V_p$ is the peak output voltage.

---

### Active Filters
* **Definition (Bengali):** যে Filter-এ active element (e.g. Op-Amp) থাকে। (Filters that contain active components).

#### 1. Passive Filters Limitations: Loading Problem
```
           Stage 1             Stage 2
        ---[ R ]---+--------[ R ]---+---- Output
                   |                |
                  [C]              [C]
                   |                |
                  ===              ===
                  GND              GND
```
* When cascading multiple passive stages, Stage 2 acts as a load on Stage 1, pulling down the output voltage and shifting the cutoff frequency. This is known as the **loading problem**.

#### 2. Active vs. Passive Filter Frequency Response
```
   Gain (dB)
     ^
     |      ._________________ (Ideal brickwall)
     |     / \                \
     |    /   \________________\_____ (Active: sharp roll-off)
     |   /                      \
     |  /                        \____ (Passive: soft/slow roll-off)
     +--+----+------------------------> Frequency (f)
```

---

### Filter Classifications
1. **Analog Filters:** Works directly on continuous analog signals.
2. **Digital Filters:** Digitizes continuous analog signals first, then processes them using digital mathematical algorithms.

---

## Page 3: Analog_Class_Note_Part-2-003.png

### Metadata
- **Audio Filter:** RC based (Low frequency).
- **Radio Filter:** LC based (High frequency).

### Active Filter Categories
* **Butterworth:** Provides flat passband response at the cost of roll-off steepness.
* **Chebyshev:** Provides steeper roll-off at the cost of ripple in the passband.

---

### 1st-Order Butterworth Low-Pass Filter
* **Key Properties:**
  * Flat passband response.
  * The higher the filter order (number of poles), the steeper the transition from passband to stopband.
```
  Gain (dB)
    ^
  0 +-------------------.
    |                   |\  -20 dB/decade (1st Order - 1 Pole)
    |                   | \
    |                   |  \ -40 dB/decade (2nd Order - 2 Poles)
    |                   |   \
    |                   |    \ -60 dB/decade (3rd Order - 3 Poles)
    +-------------------+-----+-------------------> Frequency
                       f_c
```

---

### Active Low-Pass Filter Circuit Diagram
```
                     R
         v_in -----[-==-]---*-------- (+) \
                            |              \
                           [C]              \-------- Output (V_o)
                            |       +---|   /
                           ===      |   |  /
                           GND      |    |/
                                    |
                                    +--- (-)
                                    |
                                   [Rf]
                                    |
                                    +---*---- [R1] --- === (GND)
                                    |
                                   ===
                                   GND
```
* **Mathematical Node Analysis:**
  Voltage at the non-inverting input terminal ($V_1$):
  $$V_1 = \left( \frac{-j X_C}{R - j X_C} \right) v_{in} = \left( \frac{1}{1 + j \omega R C} \right) v_{in}$$
