# 📝 RUET 2023 Odd Semester Examination — Answers
# Analog Electronic Circuits II (ECE 2105)

---

## SECTION - A

### Q.1
**(a) Draw the BJT current mirror circuit and describe how it operates. [04 Marks]**
*(Answer identical to 2020 Q.1(c) and 2022 Q.1(b). Two matched NPNs, $Q_1$ diode-connected, forcing an identical $V_{BE}$ across $Q_2$ so it perfectly mirrors $I_{ref}$ from the programming resistor).*

**(b) Calculate $A_v, Z_i$, and $Z_o$ of the cascaded JFET-BJT amplifier. [06 Marks]**
**Solution:**
**Stage 1 (n-channel JFET CS):**
1.  **DC Biasing:** $V_{DD} = 20\text{V}$, $I_{DSS} = 10\text{mA}$, $V_P = -4\text{V}$, $R_S = 680\ \Omega$.
    $V_{GS} = -I_D R_S = -0.68 I_D$ (with $I_D$ in mA).
    $$
    I_D = I_{DSS}\left(1 - \frac{V_{GS}}{V_P}\right)^2 = 10\left(1 + \frac{V_{GS}}{4}\right)^2 = 10\left(1 + 0.5 V_{GS} + 0.0625 V_{GS}^2\right)
    $$
    $$
    -\frac{V_{GS}}{0.68} = 10 + 5 V_{GS} + 0.625 V_{GS}^2 \Rightarrow -1.47 V_{GS} = 10 + 5 V_{GS} + 0.625 V_{GS}^2
    $$
    $$
    0.625 V_{GS}^2 + 6.47 V_{GS} + 10 = 0
    $$
    Applying the quadratic formula yields $V_{GS} = -1.89\text{ V}$.
2.  **AC Parameters:**
    $$
    g_m = \frac{2 I_{DSS}}{|V_P|} \left(1 - \frac{V_{GS}}{V_P}\right) = \frac{20\text{ mA}}{4\text{ V}} \left(1 - \frac{-1.89}{-4}\right) = 5\text{ mS} (1 - 0.4725) = 2.64\text{ mS}
    $$
    Input Impedance: $Z_{in1} = R_G = 3.3\text{ M}\Omega$.

**Stage 2 (NPN BJT CE):**
1.  **DC Biasing:** $V_{CC} = 20\text{V}$, $\beta = 200$. $R_{B1} = 15\text{ k}\Omega$, $R_{B2} = 4.7\text{ k}\Omega$.
    $$
    V_{th} = 20\text{ V} \times \frac{4.7}{15 + 4.7} = 4.77\text{ V}
    $$
    $$
    R_{th} = 15\text{ k}\Omega \parallel 4.7\text{ k}\Omega = 3.58\text{ k}\Omega
    $$
    $$
    I_E = \frac{V_{th} - V_{BE}}{R_E + R_{th}/\beta} = \frac{4.77 - 0.7}{1000 + 3580/200} = \frac{4.07\text{ V}}{1017.9\ \Omega} = 4.0\text{ mA}
    $$
2.  **AC Parameters:**
    $$
    r_e = \frac{26\text{ mV}}{4.0\text{ mA}} = 6.5\ \Omega
    $$
    Input Impedance of Stage 2:
    $$
    Z_{in2} = R_{th} \parallel \beta r_e = 3.58\text{ k}\Omega \parallel 200(6.5\ \Omega) = 3580 \parallel 1300 = 953\ \Omega \approx 0.95\text{ k}\Omega
    $$

**Overall Parameters:**
*   **(i) Overall Voltage Gain ($A_v$):**
    $$
    A_{v1} = -g_m (R_D \parallel Z_{in2}) = -2.64\text{ mS} \times (2.4\text{ k}\Omega \parallel 0.95\text{ k}\Omega) = -2.64 \times 0.68 = -1.8
    $$
    $$
    A_{v2} = -\frac{R_C}{r_e} = -\frac{2200}{6.5} = -338.5
    $$
    $$
    A_v = A_{v1} \times A_{v2} = (-1.8) \times (-338.5) = 609.3
    $$
*   **(ii) Input Impedance ($Z_i$):**
    $$
    Z_i = Z_{in1} = R_G = 3.3\text{ M}\Omega
    $$
*   **(iii) Output Impedance ($Z_o$):**
    $$
    Z_o = R_C = 2.2\text{ k}\Omega
    $$

---

### Q.2
**(a) Calculate the no-load voltage gain ($A_v$) for the cascode BJT configuration. [04 Marks]**
**Solution:**
**1. DC Biasing (Voltage Divider string):**
Total series resistance $R_{total} = 6.8\text{k} + 5.6\text{k} + 4.7\text{k} = 17.1\text{ k}\Omega$.
Voltage at Base of $Q_1$ (Stage 1):
$$
V_{B1} = 18\text{ V} \times \frac{4.7\text{ k}\Omega}{17.1\text{ k}\Omega} = 4.95\text{ V}
$$
$$
V_{E1} = V_{B1} - 0.7 = 4.95 - 0.7 = 4.25\text{ V}
$$
$$
I_{E1} = \frac{V_{E1}}{R_{E1}} = \frac{4.25\text{ V}}{1.1\text{ k}\Omega} = 3.86\text{ mA} \Rightarrow r_{e1} = \frac{26\text{ mV}}{3.86\text{ mA}} = 6.74\ \Omega
$$
Since $Q_1$ and $Q_2$ are in series, $I_{E2} \approx I_{C1} \approx I_{E1} = 3.86\text{ mA}$.
$$
r_{e2} = \frac{26\text{ mV}}{3.86\text{ mA}} = 6.74\ \Omega
$$
**2. AC Voltage Gain:**
Stage 1 (CE) is loaded by Stage 2's input impedance ($r_{e2}$).
$$
A_{v1} = -\frac{r_{e2}}{r_{e1}} = -\frac{6.74}{6.74} = -1
$$
Stage 2 (CB) is loaded by $R_C = 1.8\text{ k}\Omega$.
$$
A_{v2} = \frac{R_C}{r_{e2}} = \frac{1800}{6.74} = 267
$$
Overall Voltage Gain:
$$
A_v = A_{v1} \times A_{v2} = (-1) \times 267 = -267
$$

**(b) Effect of number of cascaded stages on cutoff frequencies and bandwidth. [03 Marks]**
*(Identical to 2020 Q.3(b) and 2021 Q.2(a). Lower cutoff shifts higher, upper cutoff shifts lower, resulting in significant bandwidth shrinkage).*

**(c) For the collector-feedback BJT amplifier, calculate $Z_i, Z_o, A_v, A_i$. [03 Marks]**
**Solution:**
$R_C = 2.7\text{ k}\Omega$, $R_F = 330\text{ k}\Omega$, $h_{fe} = 120$, $h_{ie} = 1.175\text{ k}\Omega$, $h_{oe} = 20\ \mu\text{S} \Rightarrow r_o = 1/20\mu\text{S} = 50\text{ k}\Omega$.
Effective collector load $R_C' = R_C \parallel r_o = 2.7\text{k} \parallel 50\text{k} = 2.56\text{ k}\Omega$.
1.  **Voltage Gain ($A_v$):**
    $$
    A_v = -h_{fe} \frac{R_C' \parallel R_F}{h_{ie}} = -120 \frac{2.56\text{k} \parallel 330\text{k}}{1.175\text{k}} = -120 \frac{2.54\text{k}}{1.175\text{k}} = -259.4
    $$
2.  **Input Impedance ($Z_i$):**
    Using Miller's theorem, the feedback resistor appears at the input as $R_{Mi} = \frac{R_F}{1 - A_v} = \frac{330\text{k}}{1 + 259.4} = 1.26\text{ k}\Omega$.
    $$
    Z_i = h_{ie} \parallel R_{Mi} = 1.175\text{ k}\Omega \parallel 1.26\text{ k}\Omega = 607\ \Omega
    $$
3.  **Output Impedance ($Z_o$):**
    $$
    Z_o = R_C \parallel r_o \parallel R_F \approx R_C' \parallel R_F = 2.54\text{ k}\Omega
    $$
4.  **Current Gain ($A_i$):**
    $$
    A_i = \frac{i_o}{i_i} = \frac{v_o / R_C}{v_i / Z_i} = A_v \left( \frac{Z_i}{R_C} \right) = -259.4 \left( \frac{607\ \Omega}{2700\ \Omega} \right) = -58.3
    $$

---

### Q.3
**(a) Calculate $I_{DQ}, V_{GSQ}$, and $V_D$ for the JFET self-bias network. [04 Marks]**
**Solution:**
$V_{DD} = 20\text{V}$, $I_{DSS} = 8\text{mA}$, $V_P = -8\text{V}$, $R_D = 6.2\text{ k}\Omega$, $R_S = 2.4\text{ k}\Omega$.
1.  **Self-Bias Equation:** $V_{GS} = -I_D R_S = -2.4 I_D$ (with $I_D$ in mA).
2.  **Shockley's Equation:**
    $$
    I_D = I_{DSS} \left(1 - \frac{V_{GS}}{V_P}\right)^2 = 8 \left(1 + \frac{V_{GS}}{8}\right)^2 = 8 \left(1 + 0.25 V_{GS} + 0.0156 V_{GS}^2\right) = 8 + 2 V_{GS} + 0.125 V_{GS}^2
    $$
3.  **Equating:**
    $$
    -\frac{V_{GS}}{2.4} = 8 + 2 V_{GS} + 0.125 V_{GS}^2 \Rightarrow -0.417 V_{GS} = 8 + 2 V_{GS} + 0.125 V_{GS}^2
    $$
    $$
    0.125 V_{GS}^2 + 2.417 V_{GS} + 8 = 0
    $$
    Using the quadratic formula: $V_{GSQ} = -4.24\text{ V}$.
4.  **Q-Point Drain Current:**
    $$
    I_{DQ} = \frac{-V_{GSQ}}{R_S} = \frac{4.24\text{ V}}{2.4\text{ k}\Omega} = 1.76\text{ mA}
    $$
5.  **Drain Voltage ($V_D$):**
    $$
    V_D = V_{DD} - I_{DQ} R_D = 20\text{ V} - (1.76\text{ mA})(6.2\text{ k}\Omega) = 20 - 10.91 = 9.09\text{ V}
    $$

**(b) Determine $R_S$ for JFET voltage-divider bias: $V_D = 12\text{V}, V_{GSQ} = -2\text{V}$. [03 Marks]**
**Solution:**
1.  **Calculate Drain Current ($I_D$):**
    $$
    I_D = \frac{V_{DD} - V_D}{R_D} = \frac{16\text{ V} - 12\text{ V}}{1.8\text{ k}\Omega} = \frac{4\text{ V}}{1.8\text{ k}\Omega} = 2.22\text{ mA}
    $$
2.  **Calculate Gate Voltage ($V_G$):**
    $$
    V_G = V_{DD} \frac{R_{G2}}{R_{G1} + R_{G2}} = 16\text{ V} \times \frac{47\text{ k}\Omega}{91\text{ k}\Omega + 47\text{ k}\Omega} = 16 \times \frac{47}{138} = 5.45\text{ V}
    $$
3.  **Calculate Source Voltage ($V_S$) and $R_S$:**
    $$
    V_{GS} = V_G - V_S \Rightarrow -2\text{ V} = 5.45\text{ V} - V_S \Rightarrow V_S = 7.45\text{ V}
    $$
    $$
    R_S = \frac{V_S}{I_D} = \frac{7.45\text{ V}}{2.22\text{ mA}} = 3.35\text{ k}\Omega
    $$

**(c) Explain electrical characteristics and structural advantages of CMOS logic gates. [03 Marks]**
**Answer:**
*   **Characteristics:** CMOS uses complementary pairs of symmetric p-type and n-type MOSFETs for logic functions. It features astronomically high input impedance (draws almost zero gate current) and offers rail-to-rail voltage swings, providing exceptionally wide noise margins.
*   **Structural Advantages:** The primary advantage is **near-zero static power dissipation**. Because the PMOS pull-up and NMOS pull-down networks are never fully ON simultaneously during a steady state, no direct path exists from power to ground. They only consume power dynamically during switching. Additionally, their simple structural design allows for extremely high packing densities in VLSI chips.

---

### Q.4
**(a) Show mathematically that for sustained oscillations in a 3-stage RC phase-shift oscillator, $A_{CL} \ge 29$. [04 Marks]**
*(Identical to the standard Barkhausen criteria derivation for a high-pass RC ladder. By setting the imaginary part of the loop transfer function to zero, the resonant frequency is found. Plugging this frequency back into the real part of the transfer function reveals that the RC network inherently attenuates the signal by a factor of exactly $\frac{1}{29}$. Therefore, to satisfy $A\beta = 1$, the inverting amplifier must provide a compensating voltage gain of exactly 29).*

**(b) Design Wien bridge oscillator for $f_o = 15\text{ kHz}$. [03/04 Marks]**
*(Identical to 2020 Q.5(c). $R = 10.6\text{ k}\Omega, C = 1\text{ nF}, R_1 = 10\text{ k}\Omega, R_f = 20\text{ k}\Omega$).*

**(c) Define frequency stability and its physical significance. [03 Marks]**
*(Identical to 2022 Q.8(a). Defined as the ability to maintain the exact target oscillation frequency despite changes in temperature, aging, or supply voltage. Physically significant to prevent transmitter drift, data corruption, and out-of-band interference in communications).*

---

## SECTION - B

### Q.5
**(a) Why is an op-amp referred to as an "operational" amplifier? [02 Marks]**
**Answer:**
The term originated in the 1940s during the era of analog vacuum-tube computers. These high-gain DC-coupled amplifiers were historically designed explicitly to perform mathematical **"operations"** (such as addition, subtraction, integration, and differentiation) to model and solve complex differential equations in real-time.

**(b) Describe how practical integrator/differentiator circuits overcome limitations. [03 Marks]**
**Answer:**
*   **Integrator:** An ideal integrator behaves as an open circuit at DC, meaning the op-amp's infinite open-loop gain will amplify minute DC offset voltages and instantly saturate the output. Practically, a large feedback resistor ($R_f$) is placed in parallel with the capacitor to cap the DC gain and stabilize the circuit.
*   **Differentiator:** An ideal differentiator has a gain that increases linearly to infinity at high frequencies, amplifying high-frequency electronic noise and making the circuit highly unstable. Practically, a small resistor ($R_i$) is added in series with the input capacitor, and a small capacitor ($C_f$) is placed in parallel with the feedback resistor to roll off the gain at very high frequencies, capping the bandwidth.

**(c) Design op-amp based circuit schematics for: [05 Marks]**
**1. $V_o = 3 V_1 - 2 V_2 + 5 V_3 - 4 V_4$**
Rearrange for an inverting summer configuration: $V_o = -(-3 V_1 + 2 V_2 - 5 V_3 + 4 V_4)$.
*   Pass $V_1$ through an inverting amplifier (Gain $=-3$). Output is $-3 V_1$.
*   Pass $V_3$ through an inverting amplifier (Gain $=-5$). Output is $-5 V_3$.
*   Connect the outputs of these two inverting amplifiers, along with input $V_2$ and input $V_4$, directly to a 4-input inverting summer.
*   Set the summer weighting resistors such that the $-3 V_1$ line has a weight of $1$, the $-5 V_3$ line has a weight of $1$, the $V_2$ line has a weight of $2$, and the $V_4$ line has a weight of $4$.
The summer output yields exactly the requested equation.

**2. $V_o = -3 \frac{d V_1}{d t} + 4 \int V_2 d t$**
Rearrange for an inverting summer: $V_o = - \left( 3 \frac{d V_1}{d t} - 4 \int V_2 d t \right)$.
*   Pass $V_1$ through a Differentiator ($RC = 3$). Output is $-3 \frac{d V_1}{d t}$. Pass this output through a unity-gain Inverter (Gain $=-1$) to yield $+3 \frac{d V_1}{d t}$.
*   Pass $V_2$ through an Integrator ($RC = 0.25$, so $1/RC = 4$). Output is $-4 \int V_2 d t$.
*   Feed the outputs of both the inverted-differentiator and the integrator into a 2-input unity-gain inverting summer.
The summer output yields exactly the requested equation.

---

### Q.6
**(a) Derive transfer characteristics of inverting and non-inverting amplifiers. [04 Marks]**
*(Standard derivations applying KCL at the inverting terminal using the virtual ground assumption. Inverting yields $A_v = -R_f/R_i$. Non-inverting yields $A_v = 1 + R_f/R_i$).*

**(b) Explain Negative Impedance Converter (NIC). [03 Marks]**
*(Identical to 2019 Q.5(a). Injects current back into the source, generating apparent negative resistance $-R$).*

**(c) Calculate CMRR in dB. [03 Marks]**
**Solution:**
1.  **Differential Gain ($A_d$):**
    $$
    A_d = \frac{V_{o(diff)}}{V_d} = \frac{120\text{ mV}}{1\text{ mV}} = 120
    $$
2.  **Common-Mode Gain ($A_{cm}$):**
    $$
    A_{cm} = \frac{V_{o(cm)}}{V_c} = \frac{20\ \mu\text{V}}{1\text{ mV}} = \frac{0.02\text{ mV}}{1\text{ mV}} = 0.02
    $$
3.  **CMRR Calculation:**
    $$
    \text{CMRR}_{dB} = 20 \log_{10} \left( \frac{A_d}{A_{cm}} \right) = 20 \log_{10} \left( \frac{120}{0.02} \right) = 20 \log_{10} (6000)
    $$
    $$
    \text{CMRR}_{dB} = 20 \times 3.778 = 75.56\text{ dB}
    $$

---

### Q.7
**(a) Internal working principles and timing cycle of 555 astable. [03 Marks]**
*(Identical to 2022 Q.4(b). Cycle of charging through $R_A+R_B$ to $2/3 V_{CC}$ and discharging through $R_B$ to $1/3 V_{CC}$).*

**(b) Determine frequency and draw waveforms for the 555 astable. [04 Marks]**
**Solution:**
$R_A = 7.5\text{ k}\Omega, R_B = 7.5\text{ k}\Omega, C = 0.1\ \mu\text{F}$.
$$
f_o = \frac{1.44}{(R_A + 2 R_B) C} = \frac{1.44}{(7.5\text{k} + 15\text{k}) \times 10^{-7}} = \frac{1.44}{22.5\text{k} \times 0.1\mu} = 640\text{ Hz}
$$
**Waveforms:**
*   $v_c(t)$: Exponentially ramps up from $1.67\text{ V}$ ($1/3 V_{CC}$) to $3.33\text{ V}$ ($2/3 V_{CC}$) taking $1.04\text{ ms}$, then ramps down back to $1.67\text{ V}$ taking $0.52\text{ ms}$.
*   $V_o(t)$: A square wave that is $5\text{ V}$ (HIGH) during the $1.04\text{ ms}$ charge phase, and $0\text{ V}$ (LOW) during the $0.52\text{ ms}$ discharge phase (Duty cycle $= 66.7\%$).

**(c) Determine $R_A, R_B, C$ for a $2\text{ kHz}$ square wave with $80\%$ duty cycle. [03 Marks]**
**Solution:**
Duty Cycle $D = \frac{R_A + R_B}{R_A + 2 R_B} = 0.80$.
$$
R_A + R_B = 0.8 R_A + 1.6 R_B \Rightarrow 0.2 R_A = 0.6 R_B \Rightarrow R_A = 3 R_B
$$
Frequency $f_o = \frac{1.44}{(R_A + 2R_B)C} = 2000\text{ Hz}$.
$$
2000 = \frac{1.44}{(3R_B + 2R_B)C} = \frac{1.44}{5 R_B C} \Rightarrow 5 R_B C = 7.2 \times 10^{-4}
$$
Let $C = 10\text{ nF} = 10^{-8}\text{ F}$.
$$
R_B = \frac{7.2 \times 10^{-4}}{5 \times 10^{-8}} = 14400\ \Omega = 14.4\text{ k}\Omega
$$
$$
R_A = 3 \times 14.4\text{ k}\Omega = 43.2\text{ k}\Omega
$$

---

### Q.8
**(a) Differentiate between active and passive filters (loading, tuning, power). [03 Marks]**
*   **Loading:** Passive filters suffer severely from impedance loading between stages, altering their designated cutoff frequencies. Active filters isolate stages completely via the high input/low output impedance of op-amps.
*   **Tuning:** Passive filters are difficult to tune because variable inductors are rare and bulky. Active filters are exceptionally easy to tune using simple variable resistors (potentiometers).
*   **Power:** Passive filters require zero external power to operate. Active filters mandate an external DC power supply ($V_{CC}/V_{EE}$) to bias the operational amplifiers.

**(b) Draw active 1st-order HPF and sketch frequency response. [03 Marks]**
*(Identical to 2019 Q.6(b). Non-inverting op-amp with series capacitor and shunt resistor at the input. Response starts at $0$ gain, rises at $+20\text{dB/dec}$, and flats out at unity or set gain after $f_H$).*

**(c) Design active Sallen-Key bandpass filter ($100\text{ kHz}$ to $300\text{ kHz}$). [04 Marks]**
*(Identical to 2022 Q.6(c). Cascade a $100\text{ kHz}$ HPF ($C=1\text{nF}, R=1.6\text{k}\Omega$) and a $300\text{ kHz}$ LPF ($C=1\text{nF}, R=530\ \Omega$)).*
