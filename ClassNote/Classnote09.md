# Class Note Digitization - Phase 9 (Part 2, Pages 24-33)

---

## Page 24: Analog_Class_Note_Part-2-024.png

### Content

#### Wien Bridge Oscillator Analysis (Continued):
* **Feedback Network Components:**
  * RC network $\rightarrow$ used to generate low frequencies (AF range).
  * LC network $\rightarrow$ used to generate high frequencies (RF range).
* **Gain Condition Comparison:**
  For a non-inverting op-amp configuration:
  $$A_v = 1 + \frac{R_f}{R_1}$$
  Using the loop gain criteria:
  $$\frac{R_1}{R_2} + \frac{C_2}{C_1} + 1 = 1 + \frac{R_f}{R_1} \Rightarrow \boxed{\frac{R_f}{R_1} = \frac{R_1}{R_2} + \frac{C_2}{C_1}}$$
* **Symmetric Case ($R_1 = R_2$, $C_1 = C_2$):**
  $$A_v = 3 \Rightarrow \boxed{R_f = 2 R_1}$$

#### Design Problem 7.13:
* **Question:** Design the Wien bridge oscillator of fig (7.19) so that $f_o = 965\text{ Hz}$.

---

#### LC Oscillator Categories:
```
                         LC Oscillators
                        /              \
                       /                \
          2 Capacitors, 1 Inductor     2 Inductors, 1 Capacitor
             (Colpitts)                    (Hartley)
```

---

## Page 25: Analog_Class_Note_Part-2-025.png

### Colpitts Oscillator
* **Amplifier Section:** Inverting configuration ($180^\circ$ phase shift).
* **Feedback Section:** LC network ($180^\circ$ phase shift).

#### Colpitts active feedback circuit diagram
```
                  Feedback Resistor (R_f)
               +-----------[===]-----------+
               |                           |
               |      Inverting Op-Amp     |
     V_f ------*------- |-\                |
               |        |  \---------------+--- Output (V_o)
              [R_1]     |+/                |
               |        |/                 |
              ===                          *---- [ Z_2 ] (C_2) --- === (GND)
              GND                          |
               |                           *---- [ Z_3 ] (L)   --- V_f
             [ Z_1 ]                       |
             (C_1)                         |
               |                           |
              ===                         ===
              GND                         GND
```

#### Feedback Factor Analysis:
* **Parallel Equivalent Impedance ($Z_p$):**
  $$Z_p = Z_2 \parallel (Z_1 + Z_3)$$
* **Feedback Factor ($\beta$):**
  $$V_f = \left( \frac{Z_1}{Z_1 + Z_3} \right) V_o \Rightarrow \boxed{\beta = \frac{V_f}{V_o} = \frac{Z_1}{Z_1 + Z_3}}$$

---

## Page 26: Analog_Class_Note_Part-2-026.png

### Content

#### Equivalent Output Loading Model
```
           Ro
  -Av * Vi -[==]---*--- v_o
                   |
                 [Z_p]
                   |
                  ===
                  GND
```
* **Output Voltage:**
  $$V_o = \left( \frac{Z_p}{Z_p + R_o} \right) (-A_v V_i)$$
  $$\Rightarrow A = \frac{V_o}{V_i} = -A_v \frac{Z_p}{Z_p + R_o}$$
  If output resistance $R_o \rightarrow 0 \Rightarrow A \approx -A_v$.
* **Loop Gain Equation:**
  Substitute $Z_p = \frac{Z_2(Z_1 + Z_3)}{Z_1 + Z_2 + Z_3}$:
  $$A = -A_v \frac{Z_2 (Z_1 + Z_3)}{Z_2 (Z_1 + Z_3) + R_o (Z_1 + Z_2 + Z_3)}$$
  $$\therefore A\beta = A \times \left( \frac{Z_1}{Z_1 + Z_3} \right) = \frac{-A_v Z_1 Z_2}{Z_2(Z_1 + Z_3) + R_o (Z_1 + Z_2 + Z_3)}$$

* **LC Substitutions:**
  $$Z_1 = \frac{1}{j\omega C_1} \quad ; \quad Z_2 = \frac{1}{j\omega C_2} \quad ; \quad Z_3 = j\omega L$$
  $$A\beta = \frac{-A_v \left( \frac{1}{j\omega C_1} \right) \left( \frac{1}{j\omega C_2} \right)}{R_o \left[ \frac{1}{j\omega C_1} + \frac{1}{j\omega C_2} + j\omega L \right] + \left( \frac{1}{j\omega C_2} \right) \left( j\omega L + \frac{1}{j\omega C_1} \right)}$$
  Multiply numerator and denominator by $-\omega^2 C_1 C_2$:
  $$\therefore A\beta = \frac{A_v}{j\omega R_o ( -C_1 - C_2 + \omega^2 L C_1 C_2 ) + ( -1 + \omega^2 L C_1 )}$$

---

## Page 27: Analog_Class_Note_Part-2-027.png

### Content

#### Resonant Frequency Analysis:
For the loop phase shift to be $0^\circ$ (since $A\beta = 1$), the imaginary part of the denominator must equal zero:
$$\text{Im} = 0 \Rightarrow \omega_o^2 L C_1 C_2 - (C_1 + C_2) = 0$$
$$\Rightarrow \omega_o^2 = \frac{C_1 + C_2}{L C_1 C_2} = \frac{1}{L \left( \frac{C_1 C_2}{C_1 + C_2} \right)}$$
Let the equivalent series capacitance $C_{eq}$ be:
$$C_{eq} = C_1 \parallel C_2 = \frac{C_1 C_2}{C_1 + C_2}$$
$$\therefore \boxed{f = \frac{1}{2\pi \sqrt{L C_{eq}}}} \quad (\text{Colpitts Resonant Frequency})}$$

#### Loop Gain Condition:
Under resonant condition, the imaginary term disappears:
$$A\beta = \frac{A_v}{-1 + \omega_o^2 L C_1}$$
Substitute $\omega_o^2 = \frac{C_1 + C_2}{L C_1 C_2}$:
$$A\beta = \frac{A_v}{-1 + \left( \frac{C_1 + C_2}{C_2} \right)} = \frac{A_v}{\frac{C_1}{C_2}} \Rightarrow \boxed{A\beta = A_v \left( \frac{C_2}{C_1} \right)}$$
Using $A\beta = 1$:
$$\Rightarrow \boxed{\beta = \frac{C_2}{C_1} \quad \text{and} \quad A_v = \frac{C_1}{C_2}}$$

---

## Page 28: Analog_Class_Note_Part-2-028.png

### Content

#### Design Example:
* **Given Parameters:**
  * $C_1 = 8\text{ nF}$, $C_2 = 1\text{ nF}$, $L = 10\text{ mH}$.
* **Calculate:** Oscillation frequency $f$, and resistors $R_1, R_f$.
* **Solution:**
  $$C_{eq} = \frac{C_1 C_2}{C_1 + C_2} = \frac{8 \times 1}{8 + 1} = 0.89\text{ nF}$$
  $$f = \frac{1}{2\pi \sqrt{L C_{eq}}} = \frac{1}{2\pi \sqrt{10\text{ mH} \times 0.89\text{ nF}}} = 1687\text{ Hz} \approx 1.69\text{ kHz}$$
  $$\beta = \frac{C_2}{C_1} = \frac{1\text{ nF}}{8\text{ nF}} = 0.125$$
  $$A_v \ge \frac{C_1}{C_2} = 8 \Rightarrow R_f \ge 8 R_1$$
  $$\text{If we select } R_1 = 1\text{ k}\Omega \Rightarrow R_f \ge 8\text{ k}\Omega \quad (\text{use } 10\text{ k}\Omega\text{ to ensure startup})$$

---

## Page 29: Analog_Class_Note_Part-2-029.png

### Metadata
- **Course**: Analog Lab-6
- **Instructor**: Moloy Sir
- **Topic**: Exp 06: Experiment of Phase-Shift Oscillator using Op-Amp

### Content

#### Phase Shift Oscillator Experimental Connection Diagram
```
                     Feedback Resistor (R_f)
                  +-----------[===]-----------+
                  |                           |
                  |     Inverting Op-Amp      |
        R_1       |        |\                 |
  V_f --[===]-----*------- |-\                |
                           |  \---------------+--- Output (V_o)
                  +------- |+/                |
                  |        |/                 |
                 ===                          |
                 GND                          |
                  |                           |
         +--------+---------------------------+
         |                                    |
         |         3-Stage RC Network         |
         |     C          C          C        |
         +----||----*----||----*----||---- V_o|
                    |          |          |   |
                  [ R ]      [ R ]      [ R ] |
                    |          |          |   |
                   ===        ===        ===  |
                   GND        GND        GND  |
```
* **Phase Alignment (Bengali Notes):**
  * Op-Amp stage $\rightarrow$ introduces a phase shift of $180^\circ$.
  * RC network $\rightarrow$ introduces an additional phase shift of $180^\circ$ at the resonant frequency.
  * Total loop phase shift is $360^\circ$ ($0^\circ$), completing the positive feedback loop.

---

## Page 30: Analog_Class_Note_Part-2-030.png

### Metadata
- **Date**: 31 March, 2026
- **Course**: ECE-2105 (Analog-2)
- **Instructor**: MIR Sir
- **Topic**: Square Wave Generator (Astable Multivibrator)

### Content
* Quadrature Oscillator $\rightarrow$ Study it yourself (নিজে পড়ে নিবে).

#### Active Square Wave Generator (Op-Amp Astable Multivibrator)
```
                          R (Feedback)
                  +-------[===]-------+
                  |                   |
        C         |        |\         |
  +----||----*----+------- |-\        |
  |          |  v_2        |  \-------*--- Output (V_o)
 ===        ===   +------- |+/        |
 GND        GND   |  v_1   |/         |
                  |                   |
                  +---[ R_1 ]----*----+
                  |              |
                 ===            [R_2]
                 GND             |
                                ===
                                GND
```
* **Transition Analysis:**
  $$v_{id} = v_1 - v_2$$
  * If $v_{id} > 0 \Rightarrow V_o = +V_{\text{sat}}$
  * If $v_{id} < 0 \Rightarrow V_o = -V_{\text{sat}}$
  * Feedback voltage at non-inverting terminal:
    $$v_1 = \left( \frac{R_1}{R_1 + R_2} \right) V_o$$
  * Initial State: Capacitor voltage $v_c = 0$, $v_2 = 0$, $V_o = +V_{\text{sat}} \Rightarrow v_1 > v_2$, which triggers output saturation.

---

## Page 31: Analog_Class_Note_Part-2-031.png

### Content

#### Timing Analysis of Astable Multivibrator:
Total period $T$ of square wave:
$$\boxed{T = 2 R C \ln\left( \frac{2 R_1 + R_2}{R_2} \right)}$$
$$f_o = \frac{1}{2 R C \ln\left( \frac{2 R_1 + R_2}{R_2} \right)}$$
* **Symmetric / Simplified Case:** If we choose $R_2 \approx 1.16 R_1$:
  $$\ln\left( \frac{2 R_1 + R_2}{R_2} \right) = \ln(2.718) \approx 1$$
  $$\therefore \boxed{f_o = \frac{1}{2 R C}}$$
* **Practice Question (Bengali):** দেখাও যে $f_o$-এর সাথে Resistance inversely proportional. (Show that oscillation frequency $f_o$ is inversely proportional to resistance).

#### Design Problem 7.15:
* **Question:** Design the square wave oscillator of fig (7.21) so that $f_o = 1\text{ kHz}$. The op-amp is a 741 with supply voltages of $\pm 15\text{ V}$.
* **Solution:**
  Using the simplified case $R_2 = 1.16 R_1$:
  Let $R_1 = 10\text{ k}\Omega \Rightarrow R_2 = 11.6\text{ k}\Omega$.
  Choose $C = 0.05\ \mu\text{F}$:
  $$f_o = \frac{1}{2 R C} \Rightarrow R = \frac{1}{2 f_o C} = \frac{1}{2 \times 1\text{ kHz} \times 0.05\ \mu\text{F}} = 10\text{ k}\Omega$$

---

## Page 32: Analog_Class_Note_Part-2-032.png

### Triangular Wave Generator

#### Circuit Diagram: Improved Active Integrator-Schmitt Trigger Design
```
       Comparator Stage (Schmitt Trigger)             Integrator Stage
                     R_3                                    C
             +-------[===]-------+                  +------||------+
             |                   |                  |              |
        R_2  |        |\         |       R_1        |    |\        |
  V_o --[==]-*------- |+\        |   +---[==]---*---+--- |-\       |
             |        |  \-------*---| v_o1     |        |  \------*--- Output (V_o)
            ===  +--- |-/            |         ===  +--- |+/
            GND  |    |/             |         GND  |    |/
                ===                  |             ===
                GND                  |             GND
                                     |
                                     +---------------------------------+
```

#### Mathematical Formulations:
* **Integrator Output Relation:**
  $$v_o(t) = -\frac{1}{R_1 C} \int_{0}^{t} v_{o1}(\tau) d\tau$$
* **Schmitt Trigger Node Equation (KCL at $v_A$):**
  $$\frac{v_o - v_A}{R_3} = \frac{v_A - v_{o1}}{R_2}$$
  At the threshold of switching, the comparator input $v_A \approx 0$.
  For $v_{o1} = +V_{\text{sat}}$:
  $$\frac{v_o}{R_3} = -\frac{V_{\text{sat}}}{R_2} \Rightarrow v_o = -\left( \frac{R_3}{R_2} \right) V_{\text{sat}}$$

---

## Page 33: Analog_Class_Note_Part-2-033.png

### Content

#### 1. Peak-to-Peak Output Voltage:
When $v_{o1} = -V_{\text{sat}}$, the switching occurs at:
$$v_o = \left( \frac{R_3}{R_2} \right) V_{\text{sat}}$$
Thus, the total peak-to-peak output amplitude is:
$$\boxed{V_{o(p-p)} = 2 \left( \frac{R_3}{R_2} \right) V_{\text{sat}} \qquad \text{--- (i)}}$$

---

#### 2. Amplitude derivation from integration:
During the half-period $T/2$, the integrator input $v_{o1}$ is at $-V_{\text{sat}}$:
$$V_{o(p-p)} = -\frac{1}{R_1 C} \int_{0}^{T/2} (-V_{\text{sat}}) dt = \frac{V_{\text{sat}} \cdot T}{2 R_1 C} \qquad \text{--- (ii)}$$

---

#### 3. Output Frequency Derivation:
Equating (i) and (ii):
$$2 \left( \frac{R_3}{R_2} \right) V_{\text{sat}} = \frac{V_{\text{sat}} \cdot T}{2 R_1 C}$$
$$T = \frac{4 R_1 R_3 C}{R_2}$$
$$\therefore \boxed{f = \frac{R_2}{4 R_1 R_3 C}}$$
* **Frequency Dependencies:**
  * $f \propto R_2$ (frequency increases linearly with comparator feedback resistor).
  * $f \propto \frac{1}{R_1 R_3}$ (frequency is inversely proportional to integrator components).
