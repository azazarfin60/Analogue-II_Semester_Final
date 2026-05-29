# Class Note Digitization - Phase 8 (Part 2, Pages 14-23)

---

## Page 14: Analog_Class_Note_Part-2-014.png

### Metadata
- **Date**: 2 February, 2026
- **Course**: ECE-2105 (Analog Lab-5)
- **Topic**: Astable and Monostable Multivibrators using 555 Timer IC

### Content

#### 1. Astable Multivibrator Circuit (Free-Running Oscillator)
```
                          +V_CC
                            |
                 +----------*----------+
                 |                     |
                [R_A]                  |
                 |                     |
                 +--------- [ Pin 7 ]  |
                 |         (Discharge) |
                [R_B]                  |
                 |                     |
                 *--------- [ Pin 6 ]  |
                 |         (Threshold) |   +---------------+
                 +--------- [ Pin 2 ]  |   |               |
                 |          (Trigger)  +---| Pin 8 (V_CC)  |
               [ C ]                       |               |
                 |                         |    555        |---> Output (Pin 3)
                ===                        |   Timer       |
                GND                        |    IC         |
                                           |               |
                                       +---| Pin 1 (GND)   |
                                       |   |               |
                                      ===  +---------------+
                                      GND
```
* **Pins Description:**
  * Pin 1: Connected to ground.
  * Pins 2 & 6: Shorted together and connected to ground through capacitor $C$.
  * Pin 3: Output pin ($V_{out}$).
  * Pins 4 (Reset) & 8 ($V_{CC}$): Connected to $+V_{CC}$.
  * Pin 5 (Control Voltage): Connected to ground through a $0.01\ \mu\text{F}$ bypass capacitor.
  * Pin 7: Connected to $+V_{CC}$ via $R_A$, and to Pin 6/2 via $R_B$.

---

#### 2. Monostable Multivibrator Circuit (One-Shot Generator)
```
                          +V_CC
                            |
                 +----------*----------+
                 |                     |
                [ R ]                  |
                 |                     |
                 *--------- [ Pin 7 ]  |
                 |         (Discharge) |   +---------------+
                 +--------- [ Pin 6 ]  |   |               |
                 |         (Threshold) +---| Pin 8 (V_CC)  |
               [ C ]                       |               |
                 |                         |    555        |---> Output (Pin 3)
                ===                        |   Timer       |
                GND                        |    IC         |
                                           |               |
                                       +---| Pin 1 (GND)   |
                                       |   |               |
                                      ===  +---------------+
                                      GND
```
* **Pins Description:**
  * Pin 1: Connected to ground.
  * Pin 2 (Trigger): Connected to $+V_{CC}$ through a pull-up resistor, and triggered by a negative-going pulse (push-button switch to ground).
  * Pin 3: Output pin ($V_{out}$).
  * Pins 4 & 8: Connected to $+V_{CC}$.
  * Pin 5: Connected to ground through a bypass capacitor.
  * Pins 6 & 7: Shorted together and connected to ground through timing capacitor $C$, and to $+V_{CC}$ via timing resistor $R$.

---

## Page 15: Analog_Class_Note_Part-2-015.png
*(Note: This page is a duplicate scan of Page 14 in the manuscript. All text, symbols, and circuits are identical to Page 14).*

---

## Page 16: Analog_Class_Note_Part-2-016.png

### Metadata
- **Date**: 28 March, 2026
- **Course**: ECE-2105 (Analog)
- **Instructor**: MIR Sir
- **Announcements**: Saturday Class Test on Oscillators (Math is mandatory for all topics, even if not explicitly solved in class).

### Content

#### Applications of Oscillators:
1. Used as a clock pulse generator.
2. Local oscillators are used to generate high-frequency carrier signals in communication systems.

---

#### Feedback Oscillator Block Diagram
```
  Thermal Noise (Input)
        v_in (1 mV)
             |
             v
            (+)
     v_in --> O --(v_A)--> [ Amplifier ] --------*----> Output (v_o)
              ^                 (A)              |
              |                                  |
              +---------- [ Feedback ] <---------+
                               (B)
                    (Freq. Selective Network)
```
* **Signals Relationship:**
  * $V_A = V_{in} + V_f$ (where $V_f = B V_o$)
  * $V_o = A V_A$

#### Waveform Generation Conditions:
1. **if $A\beta > 1$:** Output amplitude grows exponentially (used at startup).
2. **if $A\beta < 1$:** Output amplitude decays and dies out.
3. **if $A\beta = 1$:** Steady-state sustained oscillations (pure sine wave).

---

## Page 17: Analog_Class_Note_Part-2-017.png

### Content
* An oscillator is a circuit capable of generating a repetitive waveform of fixed amplitude and frequency without requiring any external input signal.
* **Frequency & Shape:** The oscillation frequency and shape depend on the values and types of components in the feedback circuit.
* **Oscillator Condition:**
  $$
  \boxed{|A\beta| = 1 \quad \text{and} \quad \angle A\beta = 0^\circ \text{ or } 360^\circ}
  $$

---

### RC Phase Shift Oscillator (Low-Frequency / AF Range)

#### 1. Basic High-Pass RC Filter Section
```
             C
     v_i ---||---+--- v_o
                 |
                [R]
                 |
                ===
                GND
```
* **Phase Shift Derivation:**
  $$
  X_C = \frac{1}{\omega C}
  $$
  $$
  v_o = \left( \frac{R}{R - j X_C} \right) v_i = \left( \frac{1}{1 - j \left( \frac{X_C}{R} \right)} \right) v_i
  $$
  $$
  \phi = \tan^{-1} \left( \frac{X_C}{R} \right) = \tan^{-1} \left( \frac{1}{\omega R C} \right)
  $$
* If $X_C = 0 \Rightarrow \phi = 0^\circ$ (high frequency limit).
* If $R = 0 \Rightarrow \phi = 90^\circ$ (maximum theoretical shift of single stage, but practically impossible since output would be shorted).

* **Bengali Explanatory Note:** $180^\circ$-এর জন্য ২টি RC Filter লাগবে। একটি থেকে $90^\circ$ পাব কিন্তু $R=0$ করা possible না। তাই ৩টি use করতে হবে। মিলিয়ে মিশিয়ে set করতে হবে যেন $\phi = 60^\circ$ (To get $180^\circ$ total phase shift, we theoretically need at least two RC filters since one stage can shift up to $90^\circ$. However, since $R=0$ is impossible, one stage cannot achieve exactly $90^\circ$. Therefore, we use 3 stages and design each to shift by $\phi = 60^\circ$, giving a total of $180^\circ$).

---

## Page 18: Analog_Class_Note_Part-2-018.png

### Content
* **Bengali Explanatory Note:** যেহেতু practically $R=0$ করা possible না তাই ৩টি নিই এবং প্রতিটিতে যেন $60^\circ$ করে পাই। (Since $R=0$ is practically impossible, we use 3 stages and target $60^\circ$ phase shift per stage).

#### Phase Shift Oscillator Circuit Diagram
```
                     Feedback Resistor (R_f)
                  +-----------[===]-----------+
                  |                           |
                  |     Inverting Op-Amp      |
        R_1       |        |\                 |
  V_f --[===]-----*------- |-\                |
                           |  \---------------+--- Output (V_o)
                  +------- |+/
                  |        |/
                 ===
                 GND
                  |
         +--------+----------------------------+
         |                                     |
         |         3-Stage RC Network          |
         |     C          C          C         |
         +----||----*----||----*----||---- V_o |
                    |          |          |    |
                  [ R ]      [ R ]      [ R ]  |
                    |          |          |    |
                   ===        ===        ===   |
                   GND        GND        GND   |
```

#### Node Analysis of the Feedback Network:
Let us analyze the 3-stage high-pass RC network from output to input:
```
           I_1          I_2          I_3
  V_in ----||----*-----||----*-----||---- V_o
                 |  V_2      |  V_1
               [ R ]       [ R ]       [ R ]
                 |           |           |
                ===         ===         ===
                GND         GND         GND
```
At the output node $V_o$:
$$
V_2 = I_3 (-j X_C) + V_o
$$
$$
I_3 = \frac{V_o}{R}
$$
$$
\Rightarrow V_2 = V_o \left( -j \frac{X_C}{R} \right) + V_o
$$
Since $-j X_C = \frac{1}{j\omega C}$:
$$
\Rightarrow V_2 = V_o \left[ 1 + \frac{1}{j\omega R C} \right]
$$

---

## Page 19: Analog_Class_Note_Part-2-019.png

### Content

#### Node Analysis (Continued)

#### 1. Calculating $I_2$:
$$
I_2 = \frac{V_2}{R} + I_3 = \frac{V_o}{R} \left[ 1 + \frac{1}{j\omega R C} \right] + \frac{V_o}{R}
$$
$$
\therefore I_2 = \frac{V_o}{R} \left[ 2 + \frac{1}{j\omega R C} \right]
$$

#### 2. Calculating $V_1$:
$$
V_1 = V_2 + \frac{I_2}{j\omega C}
$$
$$
V_1 = V_o \left[ 1 + \frac{1}{j\omega R C} \right] + \frac{V_o}{R} \left[ 2 + \frac{1}{j\omega R C} \right] \times \frac{1}{j\omega C}
$$
$$
\therefore V_1 = V_o \left[ 1 + \frac{3}{j\omega R C} - \frac{1}{\omega^2 R^2 C^2} \right]
$$

#### 3. Calculating $I_1$:
$$
I_1 = \frac{V_1}{R} + I_2
$$
$$
I_1 = \frac{V_o}{R} \left[ 1 + \frac{3}{j\omega R C} - \frac{1}{\omega^2 R^2 C^2} \right] + \frac{V_o}{R} \left[ 2 + \frac{1}{j\omega R C} \right]
$$
$$
\therefore I_1 = \frac{V_o}{R} \left[ 3 + \frac{4}{j\omega R C} - \frac{1}{\omega^2 R^2 C^2} \right]
$$

---

## Page 20: Analog_Class_Note_Part-2-020.png

### Content

#### 4. Calculating $V_{in}$ (Feedback Input):
$$
V_{in} = V_1 + \frac{I_1}{j\omega C}
$$
$$
V_{in} = V_o \left[ 1 + \frac{3}{j\omega R C} - \frac{1}{\omega^2 R^2 C^2} \right] + \frac{V_o}{R} \left( \frac{1}{j\omega C} \right) \left[ 3 + \frac{4}{j\omega R C} - \frac{1}{\omega^2 R^2 C^2} \right]
$$
$$
V_{in} = V_o \left[ 1 + \frac{6}{j\omega R C} - \frac{5}{\omega^2 R^2 C^2} - \frac{1}{j\omega^3 R^3 C^3} \right]
$$

#### Finding the Frequency of Oscillation:
For the phase shift through the RC network to be exactly $180^\circ$, the feedback factor $\beta = \frac{V_o}{V_{in}}$ must be purely real. Thus, the imaginary part of the denominator must equal zero:
$$
\text{Im} = 0 \Rightarrow \frac{6}{j\omega R C} - \frac{1}{j\omega^3 R^3 C^3} = 0
$$
$$
\Rightarrow \frac{6}{\omega R C} = \frac{1}{\omega^3 R^3 C^3} \Rightarrow \omega^2 R^2 C^2 = \frac{1}{6}
$$
$$
\Rightarrow \omega = \frac{1}{\sqrt{6} R C}
$$
$$
\therefore \boxed{f = \frac{1}{2\pi R C \sqrt{6}}} \quad (\text{For 3-stage RC Phase-Shift Oscillator})
$$
* General Formula for $n$-stages:
  $$
  f = \frac{1}{2\pi R C \sqrt{2n}}
  $$

---

## Page 21: Analog_Class_Note_Part-2-021.png

### Content

#### Frequency Stability
* **Definition:** The ability of an oscillator circuit to oscillate at one exact design frequency is called **Frequency Stability**.
* Frequency stability is impacted by:
  * Temperature variations.
  * DC power supply fluctuations.
* **Figure of Merit:** Labeled as $Q$ (Quality Factor).

---

#### Calculating the Feedback Factor ($\beta$):
Substitute $\omega = \frac{1}{\sqrt{6} R C}$ back into the real part of $V_{in}$:
$$
V_{in} = V_o \left[ 1 - \frac{5}{\omega^2 R^2 C^2} \right]
$$
$$
V_{in} = V_o \left[ 1 - \frac{5}{\left( \frac{1}{6 R^2 C^2} \right) R^2 C^2} \right] = V_o [1 - 30] = -29 V_o
$$
$$
\therefore \boxed{\beta = \frac{V_o}{V_{in}} = -\frac{1}{29}}
$$

---

#### Loop Gain Condition for Oscillation:
$$
|A\beta| = 1 \Rightarrow A \left( -\frac{1}{29} \right) = 1 \Rightarrow \boxed{A = -29}
$$
Since it's an inverting amplifier:
$$
A = -\frac{R_f}{R_1} = -29 \Rightarrow \boxed{R_f = 29 R_1}
$$

---

### Oscillator Comparison Summary

| Oscillator Type | Frequency Range | Output Waveform |
| :--- | :--- | :--- |
| **RC (Phase Shift, Wien Bridge)** | Audio Frequency (AF) | Sinusoidal |
| **LC (Hartley, Colpitts)** | Radio Frequency (RF) | Sinusoidal |
| **Crystal** | High Frequency RF (Most Stable) | Sinusoidal |
| **Relaxation (555 Timer)** | Low to Medium Frequency | Square / Triangular / Sawtooth |

---

## Page 22: Analog_Class_Note_Part-2-022.png

### Wien Bridge Oscillator

```
                                  R_f
                          +------[===]------+
                          |                 |
                          |      |\         |
                     +----*----- |-\        |
                     |           |  \-------*--- Output (V_o)
                     +---------- |+/
                     |           |/
                     |
         +-----------+----------------------+
         |                                  |
         |         Feedback Network         |
         |   C_1       R_1                  |
         +---||-------[===]-------*------ V_o |
                                  |           |
                                 [R_2] === C_2|
                                  |    ===    |
                                 ===   GND    |
                                 GND          |
```

#### Transfer Function of the Feedback Loop:
$$
V_o = \left( \frac{Z_2}{Z_1 + Z_2} \right) V_{in}
$$
$$
\beta = \frac{V_o}{V_{in}} = \frac{Z_2}{Z_1 + Z_2}
$$
where:
* **Series branch ($Z_1$):** $Z_1 = R_1 + \frac{1}{j\omega C_1}$ (High-pass characteristic)
* **Parallel branch ($Z_2$):** $Z_2 = R_2 \parallel \frac{1}{j\omega C_2} = \frac{R_2}{1 + j\omega R_2 C_2}$ (Low-pass characteristic)

$$
\therefore \frac{V_o}{V_{in}} = \frac{\frac{R_2}{1 + j\omega R_2 C_2}}{\left( R_1 + \frac{1}{j\omega C_1} \right) + \frac{R_2}{1 + j\omega R_2 C_2}}
$$

---

## Page 23: Analog_Class_Note_Part-2-023.png

### Content

#### Wien Bridge Analysis (Continued):
To achieve oscillation, the loop phase shift must be $0^\circ$ (non-inverting configuration). Thus, the imaginary part must be zero:
$$
\beta = \frac{j\omega R_2 C_1}{1 - \omega^2 R_1 R_2 C_1 C_2 + j\omega(R_1 C_1 + R_2 C_2 + R_2 C_1)}
$$
Multiply numerator and denominator by $1 - \omega^2 R_1 R_2 C_1 C_2 - j\omega(R_1 C_1 + R_2 C_2 + R_2 C_1)$ to separate real and imaginary parts.
For the phase shift to be $0^\circ$, the real part of the denominator must be zero:
$$
1 - \omega^2 R_1 R_2 C_1 C_2 = 0 \Rightarrow \omega^2 R_1 R_2 C_1 C_2 = 1
$$
$$
\Rightarrow \omega = \frac{1}{\sqrt{R_1 R_2 C_1 C_2}}
$$
$$
\therefore \boxed{f = \frac{1}{2\pi \sqrt{R_1 R_2 C_1 C_2}}} \quad (\text{Resonant Frequency})
$$
* **Symmetric Component Case:** If $R_1 = R_2 = R$ and $C_1 = C_2 = C$:
  $$
  \therefore \boxed{f = \frac{1}{2\pi R C}}
  $$

---

#### Calculating the Loop Feedback Factor ($\beta$):
Under resonant condition, the imaginary part cancels, leaving:
$$
\beta = \frac{R_2 C_1}{R_1 C_1 + R_2 C_2 + R_2 C_1}
$$
* **Symmetric Case ($R_1 = R_2$, $C_1 = C_2$):**
  $$
  \therefore \beta = \frac{R C}{3 R C} = \boxed{\frac{1}{3}}
  $$

---

#### Amplifier Gain Requirement:
$$
A \beta = 1 \Rightarrow A = \frac{1}{\beta}
$$
$$
A = \frac{R_1 C_1 + R_2 C_2 + R_2 C_1}{R_2 C_1} = \boxed{\frac{R_1}{R_2} + \frac{C_2}{C_1} + 1}
$$
* For the symmetric case:
  $$
  A = 1 + 1 + 1 = 3
  $$
  Since $A = 1 + \frac{R_f}{R_1} = 3 \Rightarrow \boxed{R_f = 2 R_1}$ (gain of the non-inverting op-amp must be at least 3 to start oscillations).
