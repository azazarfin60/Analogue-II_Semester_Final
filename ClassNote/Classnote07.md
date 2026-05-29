# Class Note Digitization - Phase 7 (Part 2, Pages 4-13)

---

## Page 4: Analog_Class_Note_Part-2-004.png

### Content

#### Derivation of Closed-Loop Gain for 1st-Order Low-Pass Filter (Continued):
$$X_C = \frac{1}{2\pi f C}$$
$$\Rightarrow V_1 = \frac{-j X_C}{R - j X_C} V_{in} = \frac{V_{in}}{1 + j 2\pi f R C}$$
$$\therefore V_o = \left( 1 + \frac{R_f}{R_1} \right) V_1$$
$$\Rightarrow V_o = \left( 1 + \frac{R_f}{R_1} \right) \times \frac{V_{in}}{1 + j 2\pi f R C}$$
Using $A_F = 1 + \frac{R_f}{R_1}$:
$$\Rightarrow V_o = A_F \times \frac{V_{in}}{1 + j 2\pi f R C} \Rightarrow \frac{V_o}{V_{in}} = \frac{A_F}{1 + j 2\pi f R C}$$
$$\Rightarrow A_v = \frac{V_o}{V_{in}} = \frac{A_F}{1 + j \left( \frac{f}{f_H} \right)}$$
where:
* $f$: input frequency.
* $f_H = \frac{1}{2\pi R C}$: upper cutoff frequency.
* $A_F = 1 + \frac{R_f}{R_1}$: passband gain.

#### Magnitude & Phase:
$$\boxed{|A_v| = \frac{A_F}{\sqrt{1 + \left( \frac{f}{f_H} \right)^2}} \quad ; \quad \phi = -\tan^{-1} \left( \frac{f}{f_H} \right)}$$

#### Bode Asymptotes:
* If $f < f_H \Rightarrow |A_v| \approx A_F$ (flat passband)
* If $f = f_H \Rightarrow |A_v| = 0.707 A_F$ (cutoff point)
* If $f > f_H \Rightarrow |A_v| < A_F$ (decaying at $-20\text{ dB/decade}$)

---

## Page 5: Analog_Class_Note_Part-2-005.png

### Metadata
- **Date**: 27 January, 2026
- **Course**: ECE-2105 (Analog-2)
- **Instructor**: MIR Sir
- **Topic**: Second-Order Low-Pass Butterworth Filter

### Content
* Passband roll-off rate comparison:
  * 1st Order $\rightarrow -20\text{ dB/decade}$
  * 2nd Order $\rightarrow -40\text{ dB/decade}$
  * 3rd Order $\rightarrow -60\text{ dB/decade}$

#### Second-Order Low-Pass Active Filter Circuit
```
                      R_2       R_3
         v_in -----[-==-]---*---[-==-]---*-------- (+) \
                            |            |              \
                          [C_2]        [C_3]             \-------- Output (v_o)
                            |            |       +---|   /
                           ===          ===      |   |  /
                           GND          GND      |    |/
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
* **Cutoff Frequency ($f_H$):**
  $$f_H = \frac{1}{2\pi \sqrt{R_2 R_3 C_2 C_3}}$$
* **Closed-loop Gain Magnitude:**
  $$\boxed{\left| \frac{V_o}{V_{in}} \right| = \frac{A_F}{\sqrt{1 + \left( \frac{f}{f_H} \right)^4}}}$$
  where:
  * $A_F = 1 + \frac{R_f}{R_1}$: passband gain.
  * $f$: frequency of input signal.

---

## Page 6: Analog_Class_Note_Part-2-006.png

### Content

#### Second-Order Filter Design Steps:
1. Cutoff frequency $f_H$ is given.
2. Assume equal components to simplify matching:
   $$R_2 = R_3 = R \quad ; \quad C_2 = C_3 = C \quad (\text{choose } C \le 1\ \mu\text{F})$$
   $$f_H = \frac{1}{2\pi R C}$$
3. Calculate the required resistor value:
   $$R = \frac{1}{2\pi f_H C}$$
4. Calculate $R_f$ and $R_1$ for passband gain $A_F$ (specifically, Butterworth response requires $A_F = 1.586 \Rightarrow R_f = 0.586 R_1$).

---

### First-Order High-Pass Butterworth Filter
```
                      C
         v_in ------||------*-------- (+) \
                            |              \
                           [R]              \-------- Output (V_o)
                            |       +---|   /
                           ===      |   |  /
                           GND      |    |/
                                    |
                                    +--- (-)
                                    |
                                   [R_F]
                                    |
                                    +---*---- [R1] --- === (GND)
                                    |
                                   ===
                                   GND
```
* **Transfer Function:**
  $$\frac{V_o}{V_{in}} = A_F \left[ \frac{j \left( \frac{f}{f_L} \right)}{1 + j \left( \frac{f}{f_L} \right)} \right]$$
  where:
  * $A_F = 1 + \frac{R_F}{R_1}$: passband gain.
  * $f_L = \frac{1}{2\pi R C}$: lower cutoff frequency.
* **Gain Magnitude:**
  $$\boxed{\left| \frac{V_o}{V_{in}} \right| = \frac{A_F \left( \frac{f}{f_L} \right)}{\sqrt{1 + \left( \frac{f}{f_L} \right)^2}}}$$

---

## Page 7: Analog_Class_Note_Part-2-007.png

### Content

#### Design Practice Problem:
* **Question:** Design an op-amp circuit such that:
  $$v_o = 5 \frac{dv_{in}}{dt} + 10 \int v_{in} dt$$
  *(Note: This is a combined differentiator and integrator circuit).*

---

#### Second-Order High-Pass Butterworth Filter:
```
                      C_2       C_3
         v_in ------||------*----||------*-------- (+) \
                            |            |              \
                           [R_2]        [R_3]            \-------- Output (V_o)
                            |            |       +---|   /
                           ===          ===      |   |  /
                           GND          GND      |    |/
                                                 |
                                                 +--- (-)
                                                 |
                                                [R_F]
                                                 |
                                                 +---*---- [R1] --- === (GND)
                                                 |
                                                ===
                                                GND
```
* **Transfer Function Magnitude:**
  $$\boxed{\left| \frac{V_o}{V_{in}} \right| = \frac{A_F \left( \frac{f}{f_L} \right)^2}{\sqrt{1 + \left( \frac{f}{f_L} \right)^4}}}$$
  where:
  * $A_F = 1 + \frac{R_F}{R_1}$: passband gain (Butterworth response requires $A_F = 1.586$).
  * $f_L = \frac{1}{2\pi \sqrt{R_2 R_3 C_2 C_3}}$: lower cutoff frequency.

---

## Page 8: Analog_Class_Note_Part-2-008.png

### Topic: Band-Pass Filters
* Bandwidth of the filter:
  $$BW = f_H - f_L$$
* Filters are categorized based on Quality Factor ($Q$):
  1. **Wide Band-Pass Filter:** $Q < 10$
  2. **Narrow Band-Pass Filter:** $Q \ge 10$

* **Quality Factor ($Q$) Formula:**
  $$\boxed{Q = \frac{f_c}{BW}}$$
  where $f_c$ is the center frequency:
  $$f_c = \sqrt{f_L f_H}$$
* Reference Problems: Sadiku Example 7.1 to 7.7.

---

### Wide Band-Pass Filter Circuit (Cascaded HPF and LPF stages)
```
          First Stage (High-Pass Filter)          Second Stage (Low-Pass Filter)
              C_1                                     R_2
  v_in ------||------*-------- (+) \     +---------[-==-]---*-------- (+) \
                     |              \    |                  |              \
                   [R_1]             \---| v_o1            [C_2]            \--- v_o
                     |       +---|   /   |                  |       +---|   /
                    ===      |   |  /    |                 ===      |   |  /
                    GND      |    |/     |                 GND      |    |/
                             |           |                          |
                             +--- (-)    |                          +--- (-)
                             |           |                          |
                            [RF1]        |                         [RF2]
                             |           |                          |
                             +---*--[R1] |                          +---*--[R1']
                                 |       |                              |
                                ===      |                             ===
                                GND      |                             GND
```
* **Bode Magnitude Response:**
```
  Gain (dB)
    ^
  AF+         .------------.
    |        /              \  -20 dB/decade
    |       /                \
  0 +------+---+----------+---+---------> Frequency (f)
          f_L             f_H
           |<--Bandwidth-->|
```

---

## Page 9: Analog_Class_Note_Part-2-009.png

### Content

#### Band-Pass Filter Design:
1. Low cutoff frequency $f_L$ and high cutoff frequency $f_H$ are given.
2. Select capacitances $C_1, C_2 \le 1\ \mu\text{F}$.
3. Calculate resistances:
   $$R_1 = \frac{1}{2\pi f_L C_1} \quad ; \quad R_2 = \frac{1}{2\pi f_H C_2}$$
4. Calculate gain-setting resistors $R_f$ and $R_1$:
   $$A_{F1} = 1 + \frac{R_{F1}}{R_{1}} \quad ; \quad A_{F2} = 1 + \frac{R_{F2}}{R_{1}'}$$
   Total Passband Gain:
   $$A_F = A_{F1} \times A_{F2}$$

#### Frequency Scaling Method:
If the cutoff frequency of a designed filter needs to be changed from $f_{\text{old}}$ to $f_{\text{new}}$:
$$\boxed{R_{\text{new}} = \text{ratio} \times R_{\text{old}}}$$
where:
$$\text{ratio} = \frac{f_{\text{old}}}{f_{\text{new}}}$$

---

## Page 10: Analog_Class_Note_Part-2-010.png

### Metadata
- **Date**: 2 February, 2026
- **Course**: ECE-2105 (Analog-2)
- **Instructor**: MIR Sir
- **Announcements**: Class Test 4 (Oscillators) & Class Test 5 (555 Timer)
- **Topic**: Band-Reject Filter (Band-Stop / Notch Filter)

### Content

* Categories based on Quality Factor ($Q$):
  1. Wide Band-Reject Filter ($Q < 10$)
  2. Narrow Band-Reject / Notch Filter ($Q \ge 10$)

```
  Gain (dB)
    ^
  AF+--------.                  .---------
    |         \                /
    |          \              /
  0 +-----------+------------+-------------> Frequency (f)
               f_L    fo    f_H
```
* **Center Frequency ($f_o$):**
  $$f_o = \sqrt{f_L f_H}$$

---

### Wide Band-Reject Filter Circuit Diagram
Consists of a Low-Pass Filter and a High-Pass Filter connected in parallel, with their outputs combined by a Summing Amplifier:

```
                  +---> Low-Pass Filter Stage ----> [R_3] ---+
                  |                                          |
  v_in -----------+                                          +--- (-) \
                  |                                                    \------- Output (v_o)
                  +---> High-Pass Filter Stage ---> [R_4] ---*-------- (+) /
                                                             |
                                                           [R_om]
                                                             |
                                                            ===
                                                            GND
```
* **Summing Stage:** Inverting summer with feedback resistor $R_f$ and input resistors $R_3, R_4$.
* **Analysis:** High frequencies pass through the HPF path; low frequencies pass through the LPF path. The band of frequencies between $f_L$ and $f_H$ is attenuated by both paths, creating the band-reject response.

---

## Page 11: Analog_Class_Note_Part-2-011.png

### Metadata
- **Topic**: Oscillators
- **Reading Assignment**: Narrow Band-Pass & All-Pass Filters (All math from text).

### Content
* **Oscillator Principle:** An oscillator generates a periodic AC signal from a DC voltage source without needing an external AC input signal.

#### Feedback Oscillator Block Diagram
```
     Thermal Noise (1 mV)
           |
           v
  v_in --> O --(v_d)--> [ Amplifier ] --------*----> Output (v_o)
           ^                 (A_v)            |
           |                                  |
           +------------ [ Feedback ] <-------+
                            (B)
```

#### Startup Mechanism (Handwritten Iterative Example):
* Closed-loop relation: $V_o = A_v(V_{in} + V_f)$
* Start with $V_{in} = 0\text{ V}$. Thermal noise provides a tiny initial signal $V_d = 1\text{ mV}$.
* If $A_v = 2$, output is:
  $$V_o = A_v V_d = 2 \times 1\text{ mV} = 2\text{ mV}$$
* Feedback factor $B = 1 \Rightarrow V_f = B V_o = 1 \times 2\text{ mV} = 2\text{ mV}$.
* In the next loop iteration, the feedback voltage adds:
  $$V_d = V_{in} + V_f = 0 + 2\text{ mV} = 2\text{ mV}$$
  $$V_o = A_v V_d = 2 \times 2\text{ mV} = 4\text{ mV}$$
* This loop repeats, and the output amplitude grows exponentially until it reaches the saturation limits of the amplifier, establishing stable steady-state oscillations.

#### Barkhausen Criteria (Conditions for Oscillation):
1. **Loop Gain Magnitude:**
   $$\boxed{|A_v B| = 1}$$
2. **Loop Phase Shift:**
   $$\boxed{\theta = 0^\circ \text{ or } 360^\circ}$$
   (The feedback signal must return in-phase to sustain oscillation).

---

## Page 12: Analog_Class_Note_Part-2-012.png

### Derivation of Barkhausen Criterion
Let:
$$V_d = V_{in} + V_f \qquad \text{--- (1)}$$
$$V_o = A_v V_d \qquad \text{--- (2)}$$
$$V_f = B V_o \qquad \text{--- (3)}$$
where $B$ is the gain/feedback factor of the feedback network.

Substituting (1) and (3) into (2):
$$V_o = A_v (V_{in} + B V_o) = A_v V_{in} + A_v B V_o$$
$$V_o - A_v B V_o = A_v V_{in}$$
$$V_o (1 - A_v B) = A_v V_{in}$$
$$\Rightarrow \frac{V_o}{V_{in}} = \frac{A_v}{1 - A_v B}$$

For an oscillator, we have a sustained output voltage $V_o \neq 0$ even when the external input voltage $V_{in} = 0$:
$$\Rightarrow 1 - A_v B = 0$$
$$\therefore \boxed{A_v B = 1} \quad \text{(Barkhausen Criterion proved)}$$

---

## Page 13: Analog_Class_Note_Part-2-013.png

### Content

#### Classifications of Oscillators

#### 1. By Feedback Network Component:
* **RC Oscillators:** Used for low-frequency range (Audio Frequency - AF range).
* **LC Oscillators:** Used for high-frequency range (Radio Frequency - RF range).
* **Crystal Oscillators:** Used for highly stable frequency applications.

#### 2. By Frequency Range:
* **Audio Frequency (AF):** Low frequency oscillators.
* **Radio Frequency (RF):** High frequency oscillators.

#### 3. By Output Waveform Shape:
* **Sinusoidal Oscillators:** Generates pure sine waves.
* **Non-Sinusoidal (Relaxation) Oscillators:**
  * Square waves
  * Triangular waves
  * Sawtooth waves
