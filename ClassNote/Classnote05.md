# Class Note Digitization - Phase 5 (Pages 41 to 50)

---

## Page 41: Analog_Class_Note_Part-1-041.png

### Metadata
- **Date**: 2 December, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MSR Sir (Note: MSR/MJR Sir depending on handwriting)
- **Topic**: BJT with Source Resistance ($R_s$)

### Content

#### 1. Circuit Diagram: BJT Common-Emitter Amplifier with Source Resistance
```
                            V_CC
                             |
               +-------+-----+---------------+-------+
               |       |                     |       |
              [R1]   [R_C]                  [R1]   [R_C]
               |       |                     |       |
        C_s    |       |               C_c   |       |
  v_s --||-----+       |         +------||---+       |
 (~)           |    Q1 |         |           |    Q2 |
[R_s]         [R2]     |----+    |          [R2]     +---||--- v_o
  |            |                ===          |           C_c
 ===          ===               GND         ===
 GND          GND                           GND
```
* **Parameters:**
  * $R_s$: Source internal resistance.
  * $C_s$: Source coupling capacitor.
  * $v_s$: AC source voltage.
  * $Z_i$: Input impedance looking into the base-biasing network (after $C_s$).

#### 2. Low-Frequency Analysis (Input Coupling Capacitor $C_s$)
* Lower cutoff frequency due to $C_s$ ($f_{L_s}$):
  $$
  \boxed{f_{L_s} = \frac{1}{2\pi (R_s + R_i) C_s}}
  $$
  where the input resistance $R_i$ is:
  $$
  R_i = R_1 \parallel R_2 \parallel \beta r_e
  $$

#### 3. Equivalent Input Loop & Voltage Divider
```
           C_s
    +------||------+-------+
    |              |       |
  v_s (~)         v_b     [R_i] (Equivalent Input Resistance)
  [R_s]            |       |
    |              +-------+
   ===
   GND
```
* Using voltage divider at the input:
  $$
  v_b = \frac{R_i}{R_i + R_s - j X_{Cs}} v_s
  $$
  $$
  \Rightarrow \frac{v_b}{v_s} = \frac{R_i}{R_i + R_s - j X_{Cs}} = \frac{R_i}{R_i \left( 1 + \frac{R_s}{R_i} - j \frac{X_{Cs}}{R_i} \right)}
  $$

---

## Page 42: Analog_Class_Note_Part-1-042.png

### Content

#### Derivation of BJT Source Cutoff (Continued)
$$
\Rightarrow \frac{v_b}{v_s} = \frac{1}{1 + \frac{R_s}{R_i} - j \frac{X_{Cs}}{R_i}}
$$
Factoring out the term $\left(1 + \frac{R_s}{R_i}\right)$ from the denominator:
$$
\frac{v_b}{v_s} = \frac{1}{\left(1 + \frac{R_s}{R_i}\right) \left[ 1 - j \frac{X_{Cs}}{R_i} \left( \frac{1}{1 + \frac{R_s}{R_i}} \right) \right]}
$$
$$
\therefore \frac{v_b}{v_s} = \frac{1}{\left( 1 + \frac{R_s}{R_i} \right) \left( 1 - j \frac{X_{Cs}}{R_i + R_s} \right)}
$$

#### Mathematical Side Note:
$$
\left( 1 + \frac{R_s}{R_i} \right) = \frac{R_s + R_i}{R_i} \Rightarrow \frac{1}{1 + \frac{R_s}{R_i}} = \frac{R_i}{R_s + R_i}
$$
$$
\text{Multiplying: } -j \frac{X_{Cs}}{R_i} \cdot \left( \frac{R_i}{R_s + R_i} \right) = -j \frac{X_{Cs}}{R_s + R_i}
$$

#### Substitution of Cutoff Frequency:
$$
\frac{X_{Cs}}{R_i + R_s} = \frac{\frac{1}{2\pi f C_s}}{R_i + R_s} = \frac{1}{2\pi f (R_i + R_s) C_s} = \frac{1}{f} \left( \frac{1}{2\pi (R_i + R_s) C_s} \right)
$$
Since $f_{L_s} = \frac{1}{2\pi (R_i + R_s) C_s}$:
$$
\Rightarrow \frac{X_{Cs}}{R_i + R_s} = \frac{f_{L_s}}{f}
$$

---

## Page 43: Analog_Class_Note_Part-1-043.png

### Content

#### Final Expression for Normalized Voltage Gain
$$
\frac{v_b}{v_s} = \left( \frac{R_i}{R_i + R_s} \right) \cdot \frac{1}{1 - j \left( \frac{f_{L_s}}{f} \right)}
$$
Since $A_{v,mid} = A_{v,max}$ at midband is $\frac{R_i}{R_i + R_s}$:
$$
A_v = A_{v,mid} \left( \frac{1}{1 - j \left( \frac{f_{L_s}}{f} \right)} \right)
$$
* **Normalized Form:**
  $$
  \boxed{\frac{A_v}{A_{v,mid}} = \frac{1}{1 - j \left( \frac{f_{L_s}}{f} \right)}}
  $$

---

### Cutoff Frequencies for $C_c$ and $C_E$ (Common-Emitter Stage)

* **Output Coupling Capacitor ($C_c$):**
  $$
  \boxed{f_{L_c} = \frac{1}{2\pi (R_o + R_L) C_c}}
  $$
  where:
  $$
  R_o = R_C \parallel r_o \approx R_C \quad (\text{normally } r_o = \infty)
  $$

* **Emitter Bypass Capacitor ($C_E$):**
  $$
  \boxed{f_{L_E} = \frac{1}{2\pi R_e C_E}}
  $$
  where:
  $$
  R_s' = R_1 \parallel R_2 \parallel R_s
  $$
  $$
  R_e = R_E \parallel \left( r_e + \frac{R_s'}{\beta} \right)
  $$

#### Bengali Notes:
* সব math করতে হবে (All math exercises must be solved).
* Definition $\rightarrow$ করতে হবে (Definitions must be prepared).

---

## Page 44: Analog_Class_Note_Part-1-044.png

### Topic: FET Low Frequency Response (Common-Source JFET)

```
                            V_DD
                             |
                      +------+-----+
                      |            |
                     [R_D]         |
                      |            |
        C_G    Gate   |            |   C_C
  v_s --||-----+-- G  +------------+----||--- Output (v_o)
 (~)           |   \ Q1            |         |
[R_sig]       [R_G] +--- S (Source)        [R_L]
  |            |    |                        |
 ===          ===  [R_S] === C_S            ===
 GND          GND   |    GND                GND
                   ===
                   GND
```
* **Impedance Definitions:**
  * Input impedance looking into gate: $R_i = R_G$
  * Output impedance looking into drain: $R_o = R_D \parallel r_d$

#### Cutoff Frequency Equations:

* **Input Coupling Capacitor ($C_G$):**
  $$
  \boxed{f_{L_G} = \frac{1}{2\pi (R_{sig} + R_i) C_G}}
  $$

* **Output Coupling Capacitor ($C_C$):**
  $$
  \boxed{f_{L_C} = \frac{1}{2\pi (R_o + R_L) C_C}}
  $$

* **Source Bypass Capacitor ($C_S$):**
  $$
  \boxed{f_{L_S} = \frac{1}{2\pi R_{eq} C_S}}
  $$
  where:
  $$
  R_{eq} = \frac{R_S}{1 + \frac{R_S (1 + g_m r_d)}{r_d + R_D \parallel R_L}}
  $$
  If $r_d = \infty$:
  $$
  \boxed{R_{eq} = R_S \parallel \frac{1}{g_m}}
  $$

---

## Page 45: Analog_Class_Note_Part-1-045.png

### Metadata
- **Date**: 5 December, 2025
- **Course**: ECE-2105 (Analog)
- **Instructor**: MSR Sir
- **Topic**: Miller's Theorem

### Content

* **Bengali introductory note:** Output থেকে ১টি portion feedback হিসেবে Input-এ যায় (A portion of output goes to the input as feedback).

#### Two-Port Network Block with Feedback
```
        I_s          I_1        Feedback Impedance (Z)
   v_s ----*-----------[===]------------*------> v_o (Output)
           |                            |
          [R_in]   +-------------+      |
           |       |             |      |
           +-----> |   2-Port    |------+
          v_i      |   Network   |     v_o
                   +-------------+
```
* **Parameters:**
  * $R_{in}^o = \frac{v_i}{I_s}$: Input impedance including feedback.
  * $R_i^o = \frac{v_i}{I_i}$: Intrinsic input impedance of the network.
  * $Z = \frac{v_i - v_o}{I_1}$: Feedback branch impedance.

#### Derivation of Miller's Input Impedance:
Applying KCL at the input node:
$$
I_s = I_1 + I_i
$$
$$
\Rightarrow \frac{v_i}{R_{in}^o} = \frac{v_i - v_o}{Z} + \frac{v_i}{R_i^o}
$$
Dividing both sides by $v_i$:
$$
\Rightarrow \frac{1}{R_{in}^o} = \frac{1 - \frac{v_o}{v_i}}{Z} + \frac{1}{R_i^o}
$$
Since voltage gain $A_v = \frac{v_o}{v_i}$:
$$
\Rightarrow \frac{1}{Z_{in}^o} = \frac{1}{Z_i^o} + \frac{1 - A_v}{Z} = \frac{1}{Z_i^o} + \frac{1}{\left( \frac{Z}{1 - A_v} \right)}
$$

Let Miller input impedance $Z_{mi}$ be:
$$
\boxed{Z_{mi} = \frac{Z}{1 - A_v}}
$$
$$
\therefore \frac{1}{Z_{in}^o} = \frac{1}{Z_i^o} + \frac{1}{Z_{mi}} \Rightarrow \boxed{Z_{in} = Z_i \parallel Z_{mi}}
$$

---

## Page 46: Analog_Class_Note_Part-1-046.png

### Content

#### Redrawing the Feedback Circuit (Miller Input Equivalent)
```
          +-------+      +-----------+
  Input --+  Z_mi +------+  2-Port   +-- Output
          +-------+      |  Network  |
                         +-----------+
```
* **Bengali Note:** কোন circuit এ কোনো Impedance input বা output থেকে output বা input-এ feedback হিসাবে কাজ করলে আমরা তাকে $Z_{in}$ এর সাথে parallel এ $Z_{mi}$ দিতে পারি। (If an impedance acts as feedback between input and output, we can represent it as $Z_{mi}$ in parallel with $Z_{in}$).

---

#### Derivation of Miller Output Impedance ($Z_{mo}$):
Looking at the output node:
```
                       Feedback Impedance (Z)
           +--------------------[===]--------------------+
           |                                             |
           |             +-----------+            I_2    |
          v_i            |  2-Port   |            <--   v_o
   v_i ----*-------------|  Network  |-------------*-----*---- v_o
                         +-----------+             |     |
                                                   |    [R_L]
                                                  [R_o]  |
                                                   |    ===
                                                  ===   GND
                                                  GND
```
* **Equations:**
  $$
  Z = \frac{V_o - V_i}{I_2}
  $$
  $$
  I_L = I_o + I_2
  $$
  $$
  \frac{V_o}{R_L} = \frac{V_o}{R_o} + \frac{V_o - V_i}{Z}
  $$
  $$
  \Rightarrow \frac{1}{R_L} = \frac{1}{R_o} + \frac{1 - \frac{V_i}{V_o}}{Z}
  $$

---

## Page 47: Analog_Class_Note_Part-1-047.png

### Content

#### Derivation of Miller Output Impedance (Continued)
$$
\Rightarrow \frac{1}{R_L} = \frac{1}{R_o} + \frac{1}{\left( \frac{Z}{1 - A_v^{-1}} \right)}
$$
$$
\Rightarrow Z = Z_o \parallel Z_{mo}
$$
where the Miller output impedance $Z_{mo}$ is:
$$
\boxed{Z_{mo} = \frac{Z}{1 - A_v^{-1}} = \frac{Z}{1 - \frac{1}{A_v}}}
$$

---

### Miller Effect with Capacitive Feedback ($Z = X_C$)
If feedback branch is a capacitor $C$:
$$
X_C = \frac{1}{2\pi f C}
$$

1. **Miller Output Impedance/Capacitance:**
   $$
   X_{mo} = \frac{X_C}{1 - A_v^{-1}} \Rightarrow \frac{1}{2\pi f C_{mo}} = \frac{1}{2\pi f C (1 - A_v^{-1})}
   $$
   $$
   \therefore \boxed{C_{mo} = C \left( 1 - \frac{1}{A_v} \right)}
   $$

2. **Miller Input Impedance/Capacitance:**
   $$
   Z_{mi} = \frac{Z}{1 - A_v} \Rightarrow X_{mi} = \frac{X_C}{1 - A_v}
   $$
   $$
   \Rightarrow \frac{1}{2\pi f C_{mi}} = \frac{1}{2\pi f C (1 - A_v)}
   $$
   $$
   \therefore \boxed{C_{mi} = C (1 - A_v)}
   $$

---

## Page 48: Analog_Class_Note_Part-1-048.png

### Content
* **Bengali Note:** High frequency-তে Miller effect ঘটে। (Miller effect occurs at high frequencies).

#### Proof of Low-Pass RC Network Response
```
                 R
        +------[===]------+
        |                 |
  v_i  (~)              ===== C    v_o
        |                 |
        +-----------------+
```
* High-frequency response:
  $$
  \boxed{A_v = \frac{1}{1 + j \left( \frac{f}{f_H} \right)}}
  $$
* Low-frequency response comparison:
  $$
  A_v = \frac{1}{1 - j \left( \frac{f_L}{f} \right)}
  $$

---

### High Frequency Response of BJT CE Amplifier
Includes internal parasitic BJT capacitances and external wire capacitances:

```
                            V_CC
                             |
               +-------+-----+---------------+-------+
               |       |                     |       |
              [R1]   [R_C]                  [R1]   [R_C]
               |       |                     |       |
   v_s  C_s    |       |      C_bc     C_c   |       |
  --||--||-----+----- B \    ---||---  -||---+       +--- v_o
 (~)           |  C_wi   \ Q1 / C_ce  |      |       |
[R_s]         [R2]  ===== \  / ===== =====  [R2]    [R_L] C_wo
  |            |    C_be   \/   |     C_wo   |       |    =====
 ===          ===          |   ===    ===   ===     ===    ===
 GND          GND         [R_E]GND    GND   GND     GND    GND
                           |
                          ===
                          GND
```
* **Parasitic Capacitances:**
  * $C_{be}, C_{bc}, C_{ce}$: Transistor junctions parasitic capacitances.
  * $C_{wi}, C_{wo}$: Input and output wire capacitances.
* **Bengali Note:** High frequency-এ wire-এর capacitance count করতে হবে। (At high frequencies, wire capacitance must be counted).

#### Input Side Cutoff Frequency ($f_{H_i}$):
$$
\boxed{f_{H_i} = \frac{1}{2\pi R_{Th} C_i}}
$$
where:
$$
R_{Th} = R_s \parallel R_1 \parallel R_2 \parallel \beta r_e
$$
$$
C_i = C_{wi} + C_{be} + C_{mi} = C_{wi} + C_{be} + (1 - A_v) C_{bc}
$$

---

## Page 49: Analog_Class_Note_Part-1-049.png

### Content

#### Output Side Cutoff Frequency ($f_{H_o}$):
$$
\boxed{f_{H_o} = \frac{1}{2\pi R_{Th_o} C_o}}
$$
where:
$$
R_{Th_o} = R_C \parallel R_L \parallel r_o
$$
$$
C_o = C_{wo} + C_{ce} + C_{mo} = C_{wo} + C_{ce} + \left( 1 - \frac{1}{A_v} \right) C_{bc}
$$

#### High-Frequency Transistor Formulas:
$$
\boxed{f_{\beta} = \frac{1}{h_{fe_{mid}}} \cdot \frac{1}{2\pi r_e (C_{\pi} + C_{\mu})}}
$$
$$
\boxed{f_{\beta} = f_{\alpha} (1 - \alpha)}
$$

---

## Page 50: Analog_Class_Note_Part-1-050.png

### Metadata
- **Date**: 7 December, 2025
- **Course**: ECE-2105
- **Instructor**: MIP Sir (MIR Sir)
- **Topic**: FET High Frequency Response

### Content

#### Circuit Diagram: JFET Common-Source High-Frequency AC Model
```
                             +V_DD
                               |
                      +--------+-----+
                      |              |
                     [R_D]           |
                      |    C_gd      |
        C1     Gate   |    -||-      |   C_c
  v_s --||-----+-- G  +----+----+----+----||--- Output (v_o)
 (~)    C_wi   |   \ Q1   /     | C_wo    |
[R_sig] ===== [R_G] +--- S      =====    [R_L]
  |    =====   |    |  C_gs     ===       |
 ===    ===   ===  [R_S]                  ===
 GND    GND   GND   |                     GND
                   ===
                   GND
```

* **Transconductance & Gain Equations:**
  $$
  g_{m_0} = \frac{2 I_{DSS}}{|V_p|}
  $$
  $$
  g_m = g_{m_0} \left( 1 - \frac{V_{GS}}{V_p} \right)
  $$
  $$
  \boxed{A_v = -g_m (r_d \parallel R_D \parallel R_L)}
  $$
  * **Bengali Note:** $r_d$ না দেওয়া থাকলে $A_v = -g_m (R_D \parallel R_L)$ (If $r_d$ is not given, use $A_v = -g_m (R_D \parallel R_L)$).

#### 1. Input Side Cutoff Frequency ($f_{H_i}$):
$$
\boxed{f_{H_i} = \frac{1}{2\pi R_{Th_i} C_i}}
$$
where:
$$
R_{Th_i} = R_G \parallel R_{sig}
$$
$$
C_i = C_{wi} + C_{gs} + C_{mi} \quad \text{with} \quad \boxed{C_{mi} = (1 - A_v) C_{gd}}
$$

#### 2. Output Side Cutoff Frequency ($f_{H_o}$):
$$
\boxed{f_{H_o} = \frac{1}{2\pi R_{Th_o} C_o}}
$$
where:
$$
R_{Th_o} = R_L \parallel R_D \parallel r_d
$$
$$
C_o = C_{wo} + C_{ds} + C_{mo} \quad \text{with} \quad \boxed{C_{mo} = \left( 1 - \frac{1}{A_v} \right) C_{gd}}
$$
