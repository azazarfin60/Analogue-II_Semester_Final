# 📚 Topic 02: Frequency Response
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Frequency Response Principles

### 1.1 Effect of Cascading on Cutoff Frequencies and Bandwidth
*[Appeared in: 2024 Q2(c), 2021 Q2(a), 2020 Q3(b), 2023 Q2(b)]*

When multiple stages of amplifiers are cascaded:
1.  **Lower Cutoff Frequency ($f_{L(overall)}$):** Shifts **higher** (increases) relative to the single-stage cutoff frequency. This is because the multiple high-pass coupling and bypass capacitor networks compound their attenuation at lower frequencies.
2.  **Upper Cutoff Frequency ($f_{H(overall)}$):** Shifts **lower** (decreases) relative to the single-stage upper cutoff frequency. This is because the multiple low-pass parasitic junction capacitance networks compound their shunting at higher frequencies.
3.  **Overall Usable Bandwidth ($BW$):** Severely **shrinks** because $BW = f_{H(overall)} - f_{L(overall)}$.

### 1.2 Mathematical Derivation of Multi-Stage Cutoffs
*[Appeared in: 2023 Q3(b)]*

Assuming $n$ identical, non-interacting cascaded stages, each with a single-stage lower cutoff frequency $f_L$ and upper cutoff frequency $f_H$:

#### Overall Upper Cutoff ($f_{H(overall)}$):
The voltage gain of a single stage in the high-frequency region is:
$$
\frac{A_v(f)}{A_{mid}} = \frac{1}{1 + j(f/f_H)}
$$
For $n$ identical stages, the overall relative gain is:
$$
\left| \frac{A_{v(overall)}}{A_{mid(overall)}} \right| = \left[ \frac{1}{\sqrt{1 + (f/f_H)^2}} \right]^n
$$
At the overall upper $3\text{ dB}$ cutoff frequency $f = f_{H(overall)}$, the relative gain drops to $1/\sqrt{2}$ (or $0.707$):
$$
\frac{1}{\sqrt{2}} = \left[ \frac{1}{\sqrt{1 + (f_{H(overall)}/f_H)^2}} \right]^n \Rightarrow \frac{1}{2} = \left[ \frac{1}{1 + (f_{H(overall)}/f_H)^2} \right]^n
$$
$$
2 = \left[ 1 + \left( \frac{f_{H(overall)}/f_H}{} \right)^2 \right]^n \Rightarrow 2^{1/n} = 1 + \left( \frac{f_{H(overall)}}{f_H} \right)^2
$$
$$
\left( \frac{f_{H(overall)}}{f_H} \right)^2 = 2^{1/n} - 1 \Rightarrow f_{H(overall)} = f_H \sqrt{2^{1/n} - 1}
$$
Since $\sqrt{2^{1/n}-1} < 1$ for $n > 1$, the overall high-frequency limit is severely reduced (e.g., for $n=2$, $f_{H(overall)} \approx 0.643 f_H$).

#### Overall Lower Cutoff ($f_{L(overall)}$):
By a similar process using the low-frequency single-stage gain relation $\frac{A_v(f)}{A_{mid}} = \frac{1}{1 - j(f_L/f)}$:
$$
f_{L(overall)} = \frac{f_L}{\sqrt{2^{1/n} - 1}}
$$
Since $\sqrt{2^{1/n}-1} < 1$ for $n > 1$, the overall low-frequency limit shifts higher (e.g., for $n=2$, $f_{L(overall)} \approx 1.55 f_L$).

---

## 2. Dynamic Capacitances & Models

### 2.1 Miller Capacitance Derivation
*[Appeared in: 2024 Q4(a), 2022 Q2(a)]*

**Miller's Theorem:** An impedance $Z_f$ connected between the input and output terminals of an inverting amplifier (possessing a voltage gain $A_v$) can be replaced by two equivalent shunt impedances connected to ground at the input ($Z_{in(M)}$) and output ($Z_{out(M)}$).

```
               +------ Zf ------+
               |                |
        Vi o---o-----[ Av ]-----o---o Vo
               |                |
              [ ] Zin(M)       [ ] Zout(M)
               |                |
        -------+----------------+------- Gnd
```

**Proof for Input Miller Capacitance ($C_{Mi}$):**
Let a feedback capacitor $C_f$ connect input node $V_i$ to output node $V_o$. The current $I_{in}$ drawn by $C_f$ from the input terminal is:
$$
I_{in} = \frac{V_i - V_o}{Z_f} = \frac{V_i - V_o}{1/j\omega C_f} = j\omega C_f (V_i - V_o)
$$
Since the voltage gain is $A_v = V_o / V_i \Rightarrow V_o = A_v V_i$. Substitute this into the equation:
$$
I_{in} = j\omega C_f (V_i - A_v V_i) = j\omega C_f (1 - A_v) V_i
$$
We want to define an equivalent input shunt capacitor $C_{Mi}$ connected from the input terminal to ground such that it draws the exact same current $I_{in}$:
$$
I_{in} = \frac{V_i}{Z_{in(M)}} = \frac{V_i}{1/j\omega C_{Mi}} = j\omega C_{Mi} V_i
$$
Equating both expressions for $I_{in}$:
$$
j\omega C_{Mi} V_i = j\omega C_f (1 - A_v) V_i \Rightarrow C_{Mi} = C_f (1 - A_v)
$$

**Proof for Output Miller Capacitance ($C_{Mo}$):**
The current $I_{out}$ flowing from the output terminal back into $C_f$ is:
$$
I_{out} = \frac{V_o - V_i}{Z_f} = j\omega C_f (V_o - V_i) = j\omega C_f \left( V_o - \frac{V_o}{A_v} \right) = j\omega C_f \left( 1 - \frac{1}{A_v} \right) V_o
$$
Equating this to the current drawn by an equivalent output shunt capacitor $C_{Mo}$ connected from the output node to ground ($I_{out} = j\omega C_{Mo} V_o$):
$$
j\omega C_{Mo} V_o = j\omega C_f \left( 1 - \frac{1}{A_v} \right) V_o \Rightarrow C_{Mo} = C_f \left( 1 - \frac{1}{A_v} \right)
$$
For high-gain inverting amplifiers ($A_v \ll -1$), $C_{Mi} \approx C_f |A_v|$ and $C_{Mo} \approx C_f$.

---

### 2.2 High-Frequency BJT Hybrid-$\pi$ Model
*[Appeared in: 2019 Q3(c)]*

At high frequencies, the standard low-frequency BJT model is inadequate due to the physical charge-storage effects within the junction depletion regions. The **High-Frequency Hybrid-$\pi$ model** resolves this by adding two microscopic parasitic capacitances:
1.  **Base-Emitter Capacitance ($C_{\pi}$ or $C_{be}$):** Formed across the forward-biased base-emitter junction (contains both depletion and diffusion capacitances).
2.  **Base-Collector Capacitance ($C_{\mu}$ or $C_{bc}$):** Formed across the reverse-biased base-collector junction (depletion capacitance).

#### Upper-Cutoff Frequency Derivation:
To isolate the input and output high-frequency cutoff points:
1.  **Miller Split:** The bridging capacitor $C_{\mu}$ is split into:
    $$
    C_{Mi} = C_{\mu} (1 - A_v) \quad \text{and} \quad C_{Mo} = C_{\mu} \left( 1 - \frac{1}{A_v} \right)
    $$
2.  **Input Upper Cutoff ($f_{Hi}$):**
    The total input shunt capacitance is:
    $$
    C_{in(total)} = C_{\pi} + C_{Mi}
    $$
    The Thevenin resistance seen by this capacitance is:
    $$
    R_{Thi} = R_s \parallel R_B \parallel Z_{base} \quad \text{where} \quad Z_{base} \approx \beta r_e
    $$
    $$
    f_{Hi} = \frac{1}{2\pi R_{Thi} C_{in(total)}}
    $$
3.  **Output Upper Cutoff ($f_{Ho}$):**
    The total output shunt capacitance is:
    $$
    C_{out(total)} = C_{Mo} + C_{wiring}
    $$
    The Thevenin resistance seen by this capacitance is:
    $$
    R_{Tho} = R_C \parallel R_L
    $$
    $$
    f_{Ho} = \frac{1}{2\pi R_{Tho} C_{out(total)}}
    $$
The overall system upper cutoff is defined by the lower of these two frequencies:
$$
f_H \approx \min(f_{Hi}, f_{Ho})
$$

---

## 3. Worked Cutoff Frequency Numericals

### 3.1 JFET Common-Source Lower Cutoff Frequency Calculation
*[Appeared in: 2024 Q4(b), 2022 Q3(c), 2021 Q3(b)]*

**Problem Details:**
A JFET common-source amplifier has the following parameters: $I_D$ yields $g_m = 2\text{ mS}$. Biasing resistors: $R_{sig} = 10\text{ k}\Omega$, $R_G = 1\text{ M}\Omega$, $R_D = 4.7\text{ k}\Omega$, $R_S = 1\text{ k}\Omega$, and load resistor $R_L = 2.2\text{ k}\Omega$. Coupling capacitors: $C_G = 0.01\ \mu\text{F}$, $C_C = 0.5\ \mu\text{F}$, and bypass capacitor $C_S = 2\ \mu\text{F}$.

#### Step-by-Step Solution:

##### 1. Input Gate Coupling Capacitor ($C_G$):
The resistance seen by the input coupling capacitor $C_G$ is:
$$
R_{in(G)} = R_{sig} + R_G = 10\text{ k}\Omega + 1\text{ M}\Omega = 1.01\text{ M}\Omega
$$
$$
f_{LG} = \frac{1}{2\pi R_{in(G)} C_G} = \frac{1}{2\pi (1.01 \times 10^6\ \Omega) (0.01 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.0101} \approx 15.76\text{ Hz}
$$

##### 2. Output Coupling Capacitor ($C_C$):
The resistance seen by the output coupling capacitor $C_C$ is:
$$
R_{out(C)} = R_D + R_L = 4.7\text{ k}\Omega + 2.2\text{ k}\Omega = 6.9\text{ k}\Omega
$$
$$
f_{LC} = \frac{1}{2\pi R_{out(C)} C_C} = \frac{1}{2\pi (6.9 \times 10^3\ \Omega) (0.5 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.00345} \approx 46.13\text{ Hz}
$$

##### 3. Source Bypass Capacitor ($C_S$):
The resistance seen by the source bypass capacitor $C_S$ is:
$$
R_{out(S)} = R_S \parallel \left( \frac{1}{g_m} \right) = 1\text{ k}\Omega \parallel \left( \frac{1}{2\text{ mS}} \right) = 1000\ \Omega \parallel 500\ \Omega \approx 333.33\ \Omega
$$
$$
f_{LS} = \frac{1}{2\pi R_{out(S)} C_S} = \frac{1}{2\pi (333.33\ \Omega) (2 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 0.0006667} \approx 238.73\text{ Hz}
$$

##### 4. Overall Lower Cutoff Frequency ($f_L$):
The overall lower cutoff frequency is dominated by the highest of these three individual cutoff frequencies:
$$
f_L \approx \max(f_{LG}, f_{LC}, f_{LS}) = 238.73\text{ Hz}
$$

---

### 3.2 BJT Common-Emitter Lower Cutoff Frequency Calculation
*[Appeared in: 2019 Q3(b), 2020 Q3(c), CT2 Q1]*

**Problem Details:**
A BJT common-emitter amplifier has parameters: $\beta = 100, V_{BE} = 0.7\text{ V}$. Resistors: $R_1 = 40\text{ k}\Omega$, $R_2 = 10\text{ k}\Omega$, $R_C = 4\text{ k}\Omega$, $R_E = 2\text{ k}\Omega$, source resistance $R_s = 0\ \Omega$, and load resistor $R_L = 2.2\text{ k}\Omega$. Capacitors: $C_{in} = 10\ \mu\text{F}$, $C_{out} = 1\ \mu\text{F}$, and bypass capacitor $C_E = 20\ \mu\text{F}$.

#### Step-by-Step Solution:

##### 1. DC Bias & Parameter Extraction:
Using Thevenin's equivalent at the BJT base:
$$
V_{th} = V_{CC} \left( \frac{R_2}{R_1 + R_2} \right) = 20\text{ V} \left( \frac{10\text{ k}}{40\text{ k} + 10\text{ k}} \right) = 4\text{ V}
$$
$$
R_{th} = R_1 \parallel R_2 = 40\text{ k}\Omega \parallel 10\text{ k}\Omega = 8\text{ k}\Omega
$$
$$
I_E = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{4 - 0.7}{2000 + 8000/100} = \frac{3.3\text{ V}}{2080\ \Omega} \approx 1.587\text{ mA}
$$
$$
r_e = \frac{26\text{ mV}}{I_E} = \frac{26\text{ mV}}{1.587\text{ mA}} \approx 16.39\ \Omega
$$

##### 2. Input Base Coupling Capacitor ($C_{in}$):
Calculate the input impedance of the base:
$$
Z_i = R_1 \parallel R_2 \parallel \beta r_e = 8000\ \Omega \parallel (100 \times 16.39\ \Omega) = 8000 \parallel 1639 \approx 1.36\text{ k}\Omega
$$
The resistance seen by $C_{in}$ is:
$$
R_{in(in)} = R_s + Z_i = 0 + 1360\ \Omega = 1360\ \Omega
$$
$$
f_{Ls} = \frac{1}{2\pi R_{in(in)} C_{in}} = \frac{1}{2\pi (1360\ \Omega) (10 \times 10^{-6}\text{ F})} \approx 11.70\text{ Hz}
$$

##### 3. Output Coupling Capacitor ($C_{out}$):
The resistance seen by $C_{out}$ is:
$$
R_{out(out)} = R_C + R_L = 4\text{ k}\Omega + 2.2\text{ k}\Omega = 6.2\text{ k}\Omega
$$
$$
f_{Lc} = \frac{1}{2\pi R_{out(out)} C_{out}} = \frac{1}{2\pi (6200\ \Omega) (1 \times 10^{-6}\text{ F})} \approx 25.67\text{ Hz}
$$

##### 4. Emitter Bypass Capacitor ($C_E$):
The resistance seen looking back into the emitter terminal of the BJT is:
$$
R_e = R_E \parallel \left( r_e + \frac{R_s \parallel R_{th}}{\beta} \right)
$$
Since $R_s = 0\ \Omega \Rightarrow R_s \parallel R_{th} = 0$:
$$
R_e = R_E \parallel r_e = 2000\ \Omega \parallel 16.39\ \Omega \approx 16.26\ \Omega
$$
$$
f_{LE} = \frac{1}{2\pi R_e C_E} = \frac{1}{2\pi (16.26\ \Omega) (20 \times 10^{-6}\text{ F})} \approx 489.41\text{ Hz}
$$

##### 5. Overall Lower Cutoff Frequency ($f_L$):
The overall lower cutoff frequency is dominated by the highest of these three individual cutoff frequencies:
$$
f_L \approx f_{LE} \approx 489.41\text{ Hz}
$$
