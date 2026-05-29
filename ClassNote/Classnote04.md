# Class Note Digitization - Phase 4 (Pages 31 to 40)

---

## Page 31: Analog_Class_Note_Part-1-031.png

### Metadata
- **Date**: 25 October, 2025
- **Course**: ECE-2105
- **Instructor**: MJP Sir (Note: MJP/MJR Sir depending on handwriting)
- **Topic**: Frequency Response

### Content

#### Frequency Response Definitions:
* **Mid Frequency** (Flat band gain region)
* **Low Frequency** $\rightarrow$ Cutoff / corner / break frequency / half-power frequency.
* **High Frequency** $\rightarrow$ Cutoff / corner / break frequency / half-power frequency.

#### Gain vs. Frequency Response Graph
```
   Voltage Gain (Av)
     ^
  Av_max +----------------.-----------------.
         |               /  \               \
0.707Av  +--------------+----+---------------+----+
         |             /|    |               |\   |
         |            / |    |   Midband     | \  |
         |           /  |    |  Frequency    |  \ |
         +----------+---+----+---------------+---+--------> Frequency (f)
                   /    |   f_L             f_H   \
       Lower Cutoff     |                         | Higher Cutoff
                        |                         |
                        | (100 MHz)               | (200 MHz)
```
* **Bengali Note:** $70.7\%$ (or $0.707 A_{vmax}$) পর্যন্ত consider করব (We will consider up to $70.7\%$).

#### Mathematical Relations:
$$
A_v = \frac{v_o}{v_i} \Rightarrow v_o = A_v v_i
$$
$$
P_o = \frac{v_o^2}{R} = \frac{A_v^2 v_i^2}{R} \qquad \text{--- (1)}
$$

---

## Page 32: Analog_Class_Note_Part-1-032.png

### Content

#### Proof: At cutoff frequency, power is halved
If $A_v = 0.707 A_{vmax}$:
$$
P'_o = \frac{(0.707 A_v v_i)^2}{R} = (0.707)^2 \frac{(A_v v_i)^2}{R}
$$
Substituting $P_o$ from Equation (1):
$$
P'_o = (0.707)^2 P_o = 0.5 P_o
$$
$$
\boxed{P'_o = 0.5 P_o}
$$
* **Definitions:**
  * $P'_o$: Power at cutoff frequency (Half-power frequency).
  * $P_o$: Power at midband frequency.
* **Bengali Question:** Prove that cutoff frequency-এ power half হয়! (Prove that power is halved at the cutoff frequency!)

#### Bandwidth Formula:
$$
\boxed{B = f_H - f_L}
$$

---

### Low Frequency Response (High-Pass RC Filter)
```
            C
         ---||---+------ +
        |        |
   v_i (~)      [R]     v_o
        |        |
         --------+------ -
```
* **Limiting Behaviors:**
  * **At $f = 0$ (DC):**
    $$
    X_C = \frac{1}{2\pi f C} = \infty \quad \text{(Capacitor acts as an open circuit)} \Rightarrow A_v = 0
    $$
  * **At $f = \infty$:**
    $$
    X_C = 0 \quad \text{(Capacitor acts as a short circuit)}
    $$

#### High-Pass Transfer Function
$$
v_o = \frac{R}{R - j X_C} v_i \Rightarrow v_o = \frac{R}{\sqrt{R^2 + X_C^2}} v_i
$$
* **Bengali Note:** যেহেতু $X_C$ phasor ঐ জন্য সরাসরি যোগ হবে না, তাই $R+X_C$ হবে না। (Since $X_C$ is a phasor, they cannot be added directly, hence the denominator is not $R+X_C$).

---

## Page 33: Analog_Class_Note_Part-1-033.png

### Content

#### Reactance & Resistance Equivalence
Let $X_C = R$:
$$
v_o = \frac{R}{\sqrt{R^2 + R^2}} v_i = \frac{R}{\sqrt{2} R} v_i = \frac{1}{\sqrt{2}} v_i
$$
$$
\Rightarrow \frac{v_o}{v_i} = \frac{1}{\sqrt{2}} = 0.707
$$
* **Bengali Note:** যখন আমাদের Reactance এবং Resistance সমান হবে তখন cutoff frequency-তে operation করতে পারি। (When our reactance and resistance are equal, we can operate at the cutoff frequency).

#### Lower Cutoff Frequency ($f_L$):
$$
X_C = R \Rightarrow \frac{1}{2\pi f_L C} = R \Rightarrow \boxed{f_L = \frac{1}{2\pi R C}}
$$

#### Logarithmic Scales (Bode representation)
* **Definition:** Output/input power-এর Ratio-কে log scale-এ দেখালে তাকে Bel বলে। (Representing the ratio of output to input power on a log scale is called Bel).
  $$
  \text{Gain in Bels} = \log_{10} \left( \frac{P_2}{P_1} \right) \text{ Bel}
  $$
  $$
  \text{Gain in decibels (dB)} = 10 \log_{10} \left( \frac{P_2}{P_1} \right) \text{ dB}
  $$
* **Expressing in terms of Voltage Ratio:**
  $$
  \text{Gain (dB)} = 10 \log_{10} \left( \frac{V_2^2}{V_1^2} \right) = 20 \log_{10} \left( \frac{V_2}{V_1} \right) = \boxed{20 \log_{10} A_v}
  $$

---

## Page 34: Analog_Class_Note_Part-1-034.png

### Content

#### Gain in terms of Cutoff Frequency ($f_L$)
$$
A_v = \frac{v_o}{v_i} = \frac{R}{R - j X_C} = \frac{1}{1 - j \left(\frac{X_C}{R}\right)}
$$
Since $X_C = \frac{1}{2\pi f C}$ and $f_L = \frac{1}{2\pi R C}$:
$$
\frac{X_C}{R} = \frac{1}{2\pi f C R} = \frac{f_L}{f}
$$
$$
\therefore \boxed{A_v = \frac{1}{1 - j \left(\frac{f_L}{f}\right)} = \frac{1}{\sqrt{1 + \left(\frac{f_L}{f}\right)^2}} \angle \tan^{-1} \left( \frac{f_L}{f} \right)}
$$

#### Decibel Gain Drop at Cutoff:
$$
G = 20 \log_{10} (0.707) \approx -3\text{ dB}
$$
* **Bengali Note:** Cutoff frequency-তে gain maximum frequency (midband) থেকে $3\text{ dB}$ কম হবে। ওই ক্ষেত্রে maximum frequency-তে $0\text{ dB}$ পাব। (At the cutoff frequency, the gain will be $3\text{ dB}$ lower than the maximum gain. In that case, we get $0\text{ dB}$ at the maximum frequency).

#### Gain in dB (Bode Magnitude):
$$
A_{v_{dB}} = 20 \log_{10} \left( \frac{1}{\sqrt{1 + \left(\frac{f_L}{f}\right)^2}} \right) = -10 \log_{10} \left[ 1 + \left(\frac{f_L}{f}\right)^2 \right]
$$

---

## Page 35: Analog_Class_Note_Part-1-035.png

### Content

#### Gain Expression at Very Low Frequencies ($f \ll f_L$):
$$
1 + \left(\frac{f_L}{f}\right)^2 \approx \left(\frac{f_L}{f}\right)^2
$$
$$
A_{v_{dB}} \approx -10 \log_{10} \left[ \left(\frac{f_L}{f}\right)^2 \right] \Rightarrow \boxed{A_{v_{dB}} \approx -20 \log_{10} \left(\frac{f_L}{f}\right)}
$$

#### Plot Ticks / Values Calculation:
* **At $f = f_L$:**
  $$
  A_{v_{dB}} = -20 \log_{10}(1) = 0\text{ dB} \quad (\text{ideal linear asymptote})
  $$
* **At $f = \frac{1}{2} f_L$:**
  $$
  A_{v_{dB}} = -20 \log_{10}(2) \approx -6\text{ dB}
  $$
* **At $f = \frac{1}{4} f_L$:**
  $$
  A_{v_{dB}} = -20 \log_{10}(4) \approx -12\text{ dB}
  $$
* **At $f = \frac{1}{10} f_L$:**
  $$
  A_{v_{dB}} = -20 \log_{10}(10) = -20\text{ dB}
  $$

* **Bengali Note:** যখনই $f$ অর্ধেক করব তখনই $6\text{ dB}$ করে কমবে (Or: যখনই $f$ দ্বিগুণ করব তখন $6\text{ dB}$ করে কমবে - written as octave rolloff of $-6\text{ dB/octave}$ or $-20\text{ dB/decade}$).

---

## Page 36: Analog_Class_Note_Part-1-036.png

### Metadata
- **Date**: 1 December, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Syllabus**: Boylestad Chapter 9 (for Class Test 2 - CT-2)
- **Topic**: Frequency Response & Bode Plot

### Content

* **Bode Plot:** Logarithmic scale plot of gain vs frequency.
```
  Linear Scale:       |----|----|----|
                     10   20   30   40
                     (Equally spaced ticks)

  Logarithmic Scale:  |--|---|-----|-------|
                     10  100  1000  10000
                     (Decades equally spaced, representing log base 10)
```

#### Transfer Function Magnitude Recap:
$$
|A_v| = \frac{1}{\sqrt{1 + \left(\frac{f_L}{f}\right)^2}}
$$
* For $f \ll f_L$:
  $$
  20\log_{10} |A_v| = -20\log_{10} \left( \frac{f_L}{f} \right)
  $$
  * $f = f_L \Rightarrow 0\text{ dB}$
  * $f = 0.5 f_L \Rightarrow -6\text{ dB}$
  * $f = 0.25 f_L \Rightarrow -12\text{ dB}$
  * $f = 0.1 f_L \Rightarrow -20\text{ dB}$

---

## Page 37: Analog_Class_Note_Part-1-037.png

### Content

#### Bode Plot vs. Actual Frequency Response Curve
```
   Av (dB)
     ^
  0 +------------------+-----------------------------
    |                / |
 -3 + - - - - - - - *  | (Actual Response)
    |              /|  |
 -6 + - - - - - - + |  | (Ideal Bode Asymptotes)
    |            /| |  |
-12 + - - - - - + | |  |
    |          /| | |  |
-20 + - - - - + | | |  |
    +--------+--+-+-+--+-------------------------> Frequency (f)
          f_L/10 | f_L/2
              f_L/4   f_L
```

#### Phase Angle ($\theta$) Derivation:
$$
A_v = \frac{1}{1 - j \left(\frac{f_L}{f}\right)}
$$
$$
\theta = \tan^{-1} \left(\frac{f_L}{f}\right)
$$

* **Case 1: Very Low Frequency ($f \ll f_L$):**
  If $f_L = 100 f$:
  $$
  \theta = \tan^{-1}(100) \approx 89.42^\circ \Rightarrow \theta \rightarrow 90^\circ
  $$
* **Case 2: Very High Frequency ($f \gg f_L$):**
  If $f = 100 f_L$:
  $$
  \theta = \tan^{-1}(0.01) \approx 0.57^\circ \Rightarrow \theta \rightarrow 0^\circ
  $$

---

## Page 38: Analog_Class_Note_Part-1-038.png

### Content

#### Phase Angle Response Curve
```
  Phase (Deg)
    ^
 90 +-------------.
    |              \
 45 + - - - - - - - *
    |                \
  0 +-----------------+-------------> Frequency (f)
   0.1f_L            f_L   10f_L
```
* **Phase relationships:**
  * $f \le 0.1 f_L \Rightarrow \theta \approx 90^\circ$
  * $f = f_L \Rightarrow \theta = 45^\circ$
  * $f \ge 10 f_L \Rightarrow \theta \approx 0^\circ$

---

### Low Frequency Response of BJT Amplifier
Common Emitter configuration capacitors:

```
                +V_CC
                  |
         +--------+-----+
         |              |
        [R1]           [R_C]
         |              |
   C_s   |              +-------||----- Output (v_o)
  --||---+-- Base       |       C_c    |
  (v_i)  |  (NPN BJT)  / Q1           [R_L]
         |            |                |
        [R2]           +----+         ===
         |             |    |         GND
        ===           [R_E] === C_E (bypass)
        GND            |    GND
                      ===
                      GND
```
* **Bengali & English Notes:**
  * Low frequency-তে capacitor-কে open circuit ধরা যাবে না (At low frequencies, capacitors cannot be assumed to be open circuits).
  * ৩টি capacitor-এর জন্য ৩টি cutoff frequency effect থাকবে (Thus, there will be 3 cutoff frequencies corresponding to the 3 capacitors: $C_s$, $C_c$, and $C_E$).

---

## Page 39: Analog_Class_Note_Part-1-039.png

### Content

### 1. Effect of Source Coupling Capacitor ($C_s$)
To analyze $C_s$, we form the equivalent circuit looking into the base:
```
           C_s
    +------||------+-------+
    |              |       |
  v_i (~)         v_b     [R_i] (Equivalent Input Resistance)
    |              |       |
    +--------------+-------+
```
where the equivalent input resistance $R_i$ is:
$$
R_i = R_1 \parallel R_2 \parallel \beta r_e
$$

#### Derivation of Cutoff:
$$
v_b = \frac{R_i}{R_i - j X_{Cs}} v_i \Rightarrow \frac{v_b}{v_i} = \frac{1}{1 - j \left( \frac{X_{Cs}}{R_i} \right)}
$$
Since $X_{Cs} = \frac{1}{2\pi f C_s}$:
$$
\frac{X_{Cs}}{R_i} = \frac{1}{2\pi f R_i C_s} = \frac{f_{Ls}}{f}
$$
where the lower cutoff frequency due to $C_s$ ($f_{Ls}$) is:
$$
\boxed{f_{Ls} = \frac{1}{2\pi R_i C_s}}
$$
$$
\therefore \frac{v_b}{v_i} = \frac{1}{1 - j \left( \frac{f_{Ls}}{f} \right)} \Rightarrow \left| \frac{v_b}{v_i} \right| = \frac{1}{\sqrt{1 + \left( \frac{f_{Ls}}{f} \right)^2}}
$$

---

## Page 40: Analog_Class_Note_Part-1-040.png

### Content

### 2. Effect of Output Coupling Capacitor ($C_c$)
The output stage equivalent circuit seen by $C_c$:
```
                    C_c
       +------------||----+----+
       |                  |    |
    ( ~ ) A_mid * v_i    v_o  [R_L]
    [R_o]                 |    |
       |                  +----+
      ===                 |
      GND                ===
                         GND
```
* The equivalent output impedance $R_o$ of the BJT collector is:
  $$
  R_o = R_C \parallel r_o \approx R_C \quad (\text{since } r_o \approx \infty)
  $$
* The total series resistance seen by $C_c$ is:
  $$
  R_{eq} = R_o + R_L
  $$
* Lower cutoff frequency due to $C_c$ ($f_{Lc}$):
  $$
  \boxed{f_{Lc} = \frac{1}{2\pi (R_o + R_L) C_c}}
  $$
* Resulting transfer function:
  $$
  A_v(f) = \frac{A_{mid}}{\sqrt{1 + \left(\frac{f_{Lc}}{f}\right)^2}}
  $$

---

### 3. Effect of Emitter Bypass Capacitor ($C_E$)
The equivalent circuit looking into the BJT emitter node:
```
           Emitter (E)
       +--------+--------+
       |        |        |
     [R_E]    [R_e']   [C_E]
       |        |        |
      ===      ===      ===
      GND      GND      GND
```
* The resistance looking into the BJT emitter node ($R_e'$) is:
  $$
  R_e' = r_e + \frac{R_1 \parallel R_2 \parallel R_s}{\beta}
  $$
* The total equivalent resistance seen across the terminals of $C_E$ ($R_e$) is:
  $$
  \boxed{R_e = R_E \parallel R_e' = R_E \parallel \left( r_e + \frac{R_1 \parallel R_2 \parallel R_s}{\beta} \right)}
  $$
* Lower cutoff frequency due to $C_E$ ($f_{LE}$):
  $$
  \boxed{f_{LE} = \frac{1}{2\pi R_e C_E}}
  $$

---

#### Important takeaways:
* **Red Margin Note:** সবগুলা Capacitor এর across-এ cutoff frequency নির্ণয় করতে হবে। (The cutoff frequencies for all three capacitors must be calculated, and the largest of these three determines the overall lower cutoff frequency $f_L$ of the amplifier).
* **Summary:** BJT low-frequency frequency response using Bode plots of individual cutoff frequencies.
