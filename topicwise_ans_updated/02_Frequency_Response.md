[Previous](01_Multistage_Amplifiers.md) | [Home](index.md) | [Next](03_Feedback_Amplifiers.md)

# 📚 Topic 02: Frequency Response
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Effect of Cascading on Bandwidth

**Question:**
*[Appeared in: 2024 Q2(c), 2023 Q2(b), 2021 Q2(a), 2020 Q3(b)]*
* **(c)** Discuss the physical effect of the number of stages on the lower-cutoff and upper-cutoff frequencies and the bandwidth of cascaded amplifiers. **[02/03 Marks]**

**Answer:**
When multiple amplifier stages are cascaded, the overall frequency response is significantly altered compared to a single stage:

1. **Lower Cutoff Frequency ($f_{L(overall)}$):** Shifts higher compared to a single stage. The multiple high-pass capacitor networks add together. This increases attenuation at lower frequencies.
2. **Upper Cutoff Frequency ($f_{H(overall)}$):** Shifts lower compared to a single stage. The multiple low-pass parasitic capacitances add together. This increases the shunting effect at high frequencies.
3. **Overall Usable Bandwidth ($BW$):** Shrinks a lot. We know $BW = f_{H(overall)} - f_{L(overall)}$. Moving the high cutoff down and the low cutoff up reduces total bandwidth.

**Mathematical Proof for Identical Stages:**
For $n$ identical, non-interacting cascaded stages, each with a single-stage upper cutoff frequency $f_H$:
The relative voltage gain of a single stage at high frequencies is $\frac{A_v(f)}{A_{mid}} = \frac{1}{1 + j(f/f_H)}$.
For $n$ identical stages, the overall relative magnitude is:
$$ \left| \frac{A_{v(overall)}}{A_{mid(overall)}} \right| = \left[ \frac{1}{\sqrt{1 + (f/f_H)^2}} \right]^n $$
At the overall $3\text{ dB}$ cutoff frequency $f = f_{H(overall)}$, the relative gain drops to $1/\sqrt{2}$:
$$ \frac{1}{\sqrt{2}} = \left[ \frac{1}{\sqrt{1 + (f_{H(overall)}/f_H)^2}} \right]^n \Rightarrow \frac{1}{2} = \left[ \frac{1}{1 + (f_{H(overall)}/f_H)^2} \right]^n $$
$$ 2^{1/n} = 1 + \left( \frac{f_{H(overall)}}{f_H} \right)^2 \Rightarrow f_{H(overall)} = f_H \sqrt{2^{1/n} - 1} $$
Since $\sqrt{2^{1/n}-1} < 1$ for $n > 1$, the upper cutoff is reduced.

Similarly, for the lower cutoff:
$$ f_{L(overall)} = \frac{f_L}{\sqrt{2^{1/n} - 1}} $$
Since the denominator is $< 1$, the lower cutoff is increased.

---

## 2. Dynamic Capacitances & Models

### 2.1 Miller Capacitance Derivation

**Question:**
*[Appeared in: 2024 Q4(a), 2022 Q2(a), 2020 Q2(b), 2019 Q3(a)]*
* **(a)** Define Miller effect capacitance. Derive the expression for the output Miller capacitance ($C_{Mo}$) of an inverting closed-loop amplifier with a voltage gain of $A_v$. **[03/04 Marks]**

**Answer:**
**Definition:**
Miller effect is the multiplication of a feedback capacitance. This happens when it connects the input and output of an inverting amplifier. This multiplied capacitance appears in parallel with the input and output. It severely limits high-frequency response.

**Derivation:**
**Miller's Theorem** helps split a feedback impedance $Z_f$. We assume $Z_f$ connects the input $V_i$ and output $V_o$ of an inverting amplifier. We can split it into two grounded shunt capacitances: $C_{Mi}$ (input) and $C_{Mo}$ (output).

1. **Proof for Input Miller Capacitance ($C_{Mi}$):**
The current $I_{in}$ drawn by $C_f$ from the input terminal is:
$$ I_{in} = \frac{V_i - V_o}{Z_f} = \frac{V_i - V_o}{1/j\omega C_f} = j\omega C_f (V_i - V_o) $$
Since $V_o = A_v V_i$, we substitute to get:
$$ I_{in} = j\omega C_f (V_i - A_v V_i) = j\omega C_f (1 - A_v) V_i $$
For an equivalent input shunt capacitor $C_{Mi}$ to draw the exact same current:
$$ I_{in} = j\omega C_{Mi} V_i $$
Equating the two expressions:
$$ j\omega C_{Mi} V_i = j\omega C_f (1 - A_v) V_i \Rightarrow C_{Mi} = C_f (1 - A_v) $$

2. **Proof for Output Miller Capacitance ($C_{Mo}$):**
The current $I_{out}$ flowing from the output terminal back into $C_f$ is:
$$ I_{out} = \frac{V_o - V_i}{Z_f} = j\omega C_f (V_o - V_i) = j\omega C_f \left( V_o - \frac{V_o}{A_v} \right) = j\omega C_f \left( 1 - \frac{1}{A_v} \right) V_o $$
For an equivalent output shunt capacitor $C_{Mo}$ to draw the exact same current:
$$ I_{out} = j\omega C_{Mo} V_o $$
Equating the two expressions:
$$ j\omega C_{Mo} V_o = j\omega C_f \left( 1 - \frac{1}{A_v} \right) V_o \Rightarrow C_{Mo} = C_f \left( 1 - \frac{1}{A_v} \right) $$

*(For a high-gain inverting amplifier where $A_v \ll -1$, $C_{Mo} \approx C_f$.)*

---

### 2.2 High-Frequency BJT Hybrid-$\pi$ Model

**Question:**
*[Appeared in: 2019 Q3(c)]*
* **(c)** Explain the high-frequency BJT model and discuss how to derive the upper-cutoff frequencies for an amplifier. **[03 Marks]**

**Answer:**
The standard low-frequency BJT model fails at high frequencies. This is due to charge-storage effects in the junctions. The **High-Frequency Hybrid-$\pi$ model** fixes this. It adds two small parasitic capacitances:
1. **Base-Emitter Capacitance ($C_{\pi}$ or $C_{be}$):** Formed across the forward-biased base-emitter junction (contains both depletion and diffusion capacitances).
2. **Base-Collector Capacitance ($C_{\mu}$ or $C_{bc}$):** Formed across the reverse-biased base-collector junction (depletion capacitance).

**Deriving Upper-Cutoff Frequencies:**
To isolate the input and output high-frequency cutoff points:
1. **Miller Split:** The bridging capacitor $C_{\mu}$ is split into $C_{Mi} = C_{\mu} (1 - A_v)$ and $C_{Mo} = C_{\mu} (1 - 1/A_v)$.
2. **Input Upper Cutoff ($f_{Hi}$):**
   The total input shunt capacitance is $C_{in(total)} = C_{\pi} + C_{Mi}$.
   The Thevenin resistance seen by this capacitance is $R_{Thi} = R_s \parallel R_B \parallel \beta r_e$.
   $$ f_{Hi} = \frac{1}{2\pi R_{Thi} C_{in(total)}} $$
3. **Output Upper Cutoff ($f_{Ho}$):**
   The total output shunt capacitance is $C_{out(total)} = C_{Mo} + C_{wiring}$.
   The Thevenin resistance seen by this capacitance is $R_{Tho} = R_C \parallel R_L$.
   $$ f_{Ho} = \frac{1}{2\pi R_{Tho} C_{out(total)}} $$
4. **Overall Upper Cutoff:**
   The overall system upper cutoff is defined by the dominant (lowest) pole:
   $$ f_H \approx \min(f_{Hi}, f_{Ho}) $$

---

## 3. Worked Lower Cutoff Frequency Numericals

### 3.1 JFET Common-Source Lower Cutoff

**Question:**
*[Appeared in: 2024 Q4(b), 2022 Q3(c), 2021 Q3(b)]*
* **(b)** Determine the lower-cutoff frequency ($f_L$) for the JFET Common-Source amplifier shown below. **[04 Marks, CO3]**

##### Circuit Diagram:
```text
                       VDD = +20V
                        |
                       [ ] RD = 4.7k
                        |
         CG = 0.01u     +---------||---------> Vo
   Vs                    |         CC = 0.5u   |
  ~-+- [ ] -+----||----+ |                     |
    |  Rsig |          | |                   [ ] RL = 2.2k
    |  =10k |        G | | D                  |
    |      [ ] RG     ---                     +--- GND
    |      =1M       |   |---
    |       |        |   |
    |       |        |   | S
    |       |        +---+---+
    |       |        |       |
    |       |       [ ] RS  === CS = 2u
    |       |       =1k      |
  --+-------+--------+-------+--- GND
```
*(Assume JFET parameters: $I_{DSS} = 8\text{ mA}$, $V_P = -4\text{ V}$, $r_d = \infty\ \Omega$, yielding a transconductance $g_m = 2\text{ mS}$).*

**Answer:**
**Step 1: Input Gate Coupling Capacitor ($C_G$)**
The resistance seen by the input coupling capacitor $C_G$ is:
$$ R_{in(G)} = R_{sig} + R_G = 10\text{ k}\Omega + 1\text{ M}\Omega = 1.01\text{ M}\Omega $$
$$ f_{LG} = \frac{1}{2\pi R_{in(G)} C_G} = \frac{1}{2\pi (1.01 \times 10^6\ \Omega) (0.01 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.0101} \approx 15.76\text{ Hz} $$

**Step 2: Output Coupling Capacitor ($C_C$)**
The resistance seen by the output coupling capacitor $C_C$ is:
$$ R_{out(C)} = R_D + R_L = 4.7\text{ k}\Omega + 2.2\text{ k}\Omega = 6.9\text{ k}\Omega $$
$$ f_{LC} = \frac{1}{2\pi R_{out(C)} C_C} = \frac{1}{2\pi (6.9 \times 10^3\ \Omega) (0.5 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.00345} \approx 46.13\text{ Hz} $$

**Step 3: Source Bypass Capacitor ($C_S$)**
The resistance seen by the source bypass capacitor $C_S$ is:
$$ R_{out(S)} = R_S \parallel \left( \frac{1}{g_m} \right) = 1\text{ k}\Omega \parallel \left( \frac{1}{2\text{ mS}} \right) = 1000\ \Omega \parallel 500\ \Omega \approx 333.33\ \Omega $$
$$ f_{LS} = \frac{1}{2\pi R_{out(S)} C_S} = \frac{1}{2\pi (333.33\ \Omega) (2 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.0006667} \approx 238.73\text{ Hz} $$

**Step 4: Overall Lower Cutoff Frequency ($f_L$)**
The overall lower cutoff frequency is dominated by the highest of these three individual cutoff frequencies:
$$ f_L \approx \max(f_{LG}, f_{LC}, f_{LS}) = 238.73\text{ Hz} $$

---

### 3.2 BJT Common-Emitter Lower Cutoff

**Question:**
*[Appeared in: 2020 Q3(c), 2019 Q3(b)]*
* **(c)** For the Common-Emitter BJT amplifier shown in Figure 3(c), determine the lower-cutoff frequencies ($f_{LS}, f_{LC}, f_{LE}$). Find the overall lower-cutoff frequency of the network. **[05 Marks]**

##### Circuit Diagram:
```text
                        +20V
                          |
              +-----------+-----------------------+
              |                                   |
             [R1] (40 kOhm)                      [RC] (4 kOhm)
              |                                   |
              +---------------+                   +----||----o v_o
              |               |                   |   C_out (1uF)
             ---            |/ C                  |
     (10uF)  | |            |                     |
      C_in   ---            |                     [RL] (2.2 kOhm)
              |             |                     |
             v_i   +--------+                     ===
                   |        |\ E                  GND
                   |          |
                  [R2]        +----+
                10 kOhm       |    |
                   |         [RE] --- CE
                  ===       2 kOhm---(20uF)
                  GND         |    |
                             ===  ===
                             GND  GND
```
*(Assume BJT parameters: $\beta = 100$, $V_{BE} = 0.7\text{ V}$, $r_o = \infty$, $R_s = 0\ \Omega$).*

**Answer:**
**Step 1: DC Bias & Parameter Extraction:**
Using Thevenin's equivalent at the BJT base:
$$ V_{th} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right) = 20\text{ V} \left( \frac{10\text{ k}}{40\text{ k} + 10\text{ k}} \right) = 4\text{ V} $$
$$ R_{th} = R_1 \parallel R_2 = 40\text{ k}\Omega \parallel 10\text{ k}\Omega = 8\text{ k}\Omega $$
$$ I_E = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{4 - 0.7}{2000 + 8000/100} = \frac{3.3\text{ V}}{2080\ \Omega} \approx 1.587\text{ mA} $$
$$ r_e = \frac{26\text{ mV}}{I_E} = \frac{26\text{ mV}}{1.587\text{ mA}} \approx 16.39\ \Omega $$

**Step 2: Input Base Coupling Capacitor ($C_{in}$):**
Calculate the input impedance of the base:
$$ Z_i = R_1 \parallel R_2 \parallel \beta r_e = 8000\ \Omega \parallel (100 \times 16.39\ \Omega) = 8000 \parallel 1639 \approx 1.36\text{ k}\Omega $$
The resistance seen by $C_{in}$ is:
$$ R_{in(in)} = R_s + Z_i = 0 + 1360\ \Omega = 1360\ \Omega $$
$$ f_{Ls} = \frac{1}{2\pi R_{in(in)} C_{in}} = \frac{1}{2\pi (1360\ \Omega) (10 \times 10^{-6}\text{ F})} \approx 11.70\text{ Hz} $$

**Step 3: Output Coupling Capacitor ($C_{out}$):**
The resistance seen by $C_{out}$ is:
$$ R_{out(out)} = R_C + R_L = 4\text{ k}\Omega + 2.2\text{ k}\Omega = 6.2\text{ k}\Omega $$
$$ f_{Lc} = \frac{1}{2\pi R_{out(out)} C_{out}} = \frac{1}{2\pi (6200\ \Omega) (1 \times 10^{-6}\text{ F})} \approx 25.67\text{ Hz} $$

**Step 4: Emitter Bypass Capacitor ($C_E$):**
The resistance seen looking back into the emitter terminal of the BJT is:
$$ R_e = R_E \parallel \left( r_e + \frac{R_s \parallel R_{th}}{\beta} \right) $$
Since $R_s = 0\ \Omega$, $R_s \parallel R_{th} = 0$:
$$ R_e = R_E \parallel r_e = 2000\ \Omega \parallel 16.39\ \Omega \approx 16.26\ \Omega $$
$$ f_{LE} = \frac{1}{2\pi R_e C_E} = \frac{1}{2\pi (16.26\ \Omega) (20 \times 10^{-6}\text{ F})} \approx 489.41\text{ Hz} $$

**Step 5: Overall Lower Cutoff Frequency ($f_L$):**
The overall lower cutoff frequency is dominated by the highest of these three individual cutoff frequencies:
$$ f_L \approx \max(f_{Ls}, f_{Lc}, f_{LE}) \approx f_{LE} \approx 489.41\text{ Hz} $$

---

## 4. Coupling Type Comparisons

**Question:**
*[Appeared in: 2020 Q3(a)]*
* **(a)** Compare and explain the frequency response curves of: (i) RC coupled amplifier, (ii) Transformer coupled amplifier, and (iii) Direct coupled amplifier. **[03 Marks]**

**Answer:**
1.  **RC Coupled Amplifier:**
    *   **Response:** Gain drops sharply at low frequencies. This happens because capacitors block low-frequency signals. Gain also drops sharply at high frequencies due to parasitic capacitances. It has a flat midband region.
    *   **Application:** Audio frequency (AF) amplifiers.
2.  **Transformer Coupled Amplifier:**
    *   **Response:** Low-frequency response is worse than RC coupling. The transformer acts as a short at DC. High-frequency response is also poor. Leakage inductance and capacitance cause resonance peaks. The midband is narrow and not flat.
    *   **Application:** Power amplifiers for impedance matching (e.g., driving a speaker).
3.  **Direct Coupled Amplifier:**
    *   **Response:** Response goes perfectly down to $0\text{ Hz}$ (DC). There are no series coupling capacitors. Gain is flat from DC until the high-frequency limit. Internal transistor capacitances cause the high-frequency drop.
    *   **Application:** Amplifying very low-frequency signals and DC voltages (e.g., Op-Amps, sensor interfaces).

[Previous](01_Multistage_Amplifiers.md) | [Home](index.md) | [Next](03_Feedback_Amplifiers.md)
