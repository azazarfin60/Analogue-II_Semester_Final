[Previous](03_Feedback_Amplifiers.md) | [Home](index.md) | [Next](05_OpAmp_Applications.md)

# 📚 Topic 04: OpAmp Fundamentals
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Ideal Characteristics & Virtual Ground

### 1.1 Physical Parameters & The Virtual Ground Concept
*[Appeared in: 2024 Q5(a), 2024 Q5(c), 2023 Q5(a)]*

**Question:**
* **(a)** Explain the concept of "virtual ground" in operational amplifiers. Derive the closed-loop voltage gain of a non-inverting op-amp using this concept. **[04 Marks, CO2]**
* **(c)** Define and explain the physical significance of the following op-amp parameters: (i) Common-Mode Rejection Ratio (CMRR), (ii) Open-loop voltage gain ($A_{OL}$), and (iii) Input offset voltage ($V_{OS}$). **[03 Marks, CO1]**

**Answer:**
**Op-Amp Parameters:**
1.  **Open-Loop Voltage Gain ($A_{OL}$):** The raw differential gain of the op-amp without feedback. It is ideally infinite ($\infty$), but practically very large ($\sim 10^5$ to $10^6$). Its massive size creates the virtual short concept.
2.  **Common-Mode Rejection Ratio (CMRR):** The ratio of the differential gain ($A_d$) to the common-mode gain ($A_c$). It is ideally infinite. It measures the op-amp's ability to reject noise on both input terminals.
3.  **Input Offset Voltage ($V_{OS}$):** The small DC voltage needed across the inputs to force the output to exactly $0\text{V}$. It is ideally zero. It comes from tiny manufacturing mismatches in the input transistors.

**The Virtual Ground Concept:**
In a closed-loop negative feedback circuit, the power supply rails (e.g., $\pm 15\text{V}$) constrain the output voltage ($V_o$). Since $A_{OL}$ is huge, the required differential input voltage is tiny:
$$ V_d = V_+ - V_- = \frac{V_o}{A_{OL}} \approx 0 \Rightarrow V_+ \approx V_- $$
This is the **Virtual Short** principle. If the non-inverting terminal ($V_+$) connects to ground ($0\text{V}$), the inverting terminal ($V_-$) also goes to exactly $0\text{V}$. It acts as a **Virtual Ground**. It is a node at $0\text{V}$. But unlike a true ground, no current flows into the op-amp. This is due to infinite input impedance.

**Derivation of Non-Inverting Amplifier Gain:**
```text
                         Rf
                   +---[ R2 ]---+
                   |            |
        Vin o---(+)----[ Av ]---+---o Vout
                   |
        Gnd o---[ R1 ]---o (-)
```
1.  Input is applied to the non-inverting terminal ($V_+ = V_{in}$).
2.  By the virtual short principle, the inverting terminal tracks the input: $V_- = V_+ = V_{in}$.
3.  Apply KCL at the inverting node (assuming zero current enters the op-amp):
$$ \frac{0 - V_-}{R_1} + \frac{V_{out} - V_-}{R_f} = 0 $$
Substitute $V_- = V_{in}$:
$$ -\frac{V_{in}}{R_1} + \frac{V_{out} - V_{in}}{R_f} = 0 \Rightarrow \frac{V_{out}}{R_f} = V_{in} \left( \frac{1}{R_1} + \frac{1}{R_f} \right) $$
$$ V_{out} = V_{in} \left( \frac{R_f}{R_1} + 1 \right) \Rightarrow A_v = \frac{V_{out}}{V_{in}} = 1 + \frac{R_f}{R_1} $$

---

### 1.2 Voltage Follower
*[Appeared in: 2021 Q7(b)]*

**Question:**
* **(b)** Draw an op-amp voltage follower circuit. Where and why is this circuit employed? **[02 Marks, CLO1]**

**Answer:**
**Circuit Diagram:**
```text
               +---------------+
               |               |
        Vin o-(+)----[ Av ]----+---o Vout
                     (-)-------+
```

**Where and Why it is Employed:**
The voltage follower (unity-gain buffer) is used when a high-impedance source drives a low-impedance load. It prevents signal loss (loading effect). 
The output feeds directly back to the inverting input ($R_f = 0$, $R_1 = \infty$). So the gain is $A_v = 1 + 0/\infty = 1$. It provides great impedance isolation. It maintains the exact voltage of the signal.

---

## 2. Dynamic Parameters: CMRR & Slew Rate

### 2.1 CMRR Numerical Calculation
*[Appeared in: 2023 Q6(c)]*

**Question:**
* **(c)** Define common-mode rejection ratio (CMRR). Calculate the CMRR in decibels (dB) for an op-amp with the following measurement parameters:
  * Differential: $V_d = 1\text{ mV}$ yields $V_o = 120\text{ mV}$
  * Common-mode: $V_c = 1\text{ mV}$ yields $V_o = 20\ \mu\text{V}$ **[03 Marks, CLO3]**

**Answer:**
**Definition:** CMRR evaluates an op-amp's ability to reject identical signals applied to both inputs (noise), defined as the ratio of differential gain to common-mode gain ($CMRR = |A_d / A_c|$).

**Calculation:**
1.  Calculate Differential Gain ($A_d$):
$$ A_d = \frac{V_{o(d)}}{V_d} = \frac{120\text{ mV}}{1\text{ mV}} = 120 $$
2.  Calculate Common-Mode Gain ($A_c$):
$$ A_c = \frac{V_{o(c)}}{V_c} = \frac{20\ \mu\text{V}}{1\text{ mV}} = \frac{20 \times 10^{-6}}{1 \times 10^{-3}} = 20 \times 10^{-3} = 0.02 $$
3.  Calculate CMRR in linear ratio:
$$ CMRR = \frac{A_d}{A_c} = \frac{120}{0.02} = 6000 $$
4.  Convert to Decibels (dB):
$$ CMRR_{dB} = 20 \log_{10}(CMRR) = 20 \log_{10}(6000) = 20 \times 3.778 \approx 75.56\text{ dB} $$

---

### 2.2 Output Voltage with CMRR
*[Appeared in: 2024 Q7(a)]*

**Question:**
* **(a)** Determine the output voltage of an operational amplifier for input voltages of $V_{i1} = 150\ \mu\text{V}$ and $V_{i2} = 140\ \mu\text{V}$. The amplifier has a differential gain of $A_d = 4000$ and the value of CMRR is: (i) 100, (ii) $10^5$. **[03 Marks, CO2]**

**Answer:**
First, define the differential and common-mode inputs:
$$ V_d = V_{i1} - V_{i2} = 150\ \mu\text{V} - 140\ \mu\text{V} = 10\ \mu\text{V} $$
$$ V_c = \frac{V_{i1} + V_{i2}}{2} = \frac{150\ \mu\text{V} + 140\ \mu\text{V}}{2} = 145\ \mu\text{V} $$

The total output voltage equation is:
$$ V_o = A_d V_d + A_c V_c $$
Since $CMRR = \frac{A_d}{A_c} \Rightarrow A_c = \frac{A_d}{CMRR}$, the equation becomes:
$$ V_o = A_d V_d + \left( \frac{A_d}{CMRR} \right) V_c = A_d \left( V_d + \frac{V_c}{CMRR} \right) $$

**Case (i): CMRR = 100**
$$ V_o = 4000 \left( 10\ \mu\text{V} + \frac{145\ \mu\text{V}}{100} \right) = 4000 (10\ \mu\text{V} + 1.45\ \mu\text{V}) = 4000 \times 11.45\ \mu\text{V} = 45,800\ \mu\text{V} = 45.8\text{ mV} $$

**Case (ii): CMRR = $10^5$**
$$ V_o = 4000 \left( 10\ \mu\text{V} + \frac{145\ \mu\text{V}}{100,000} \right) = 4000 (10\ \mu\text{V} + 0.00145\ \mu\text{V}) = 4000 \times 10.00145\ \mu\text{V} \approx 40,005.8\ \mu\text{V} = 40.0058\text{ mV} $$

---

### 2.3 Slew Rate and Maximum Frequency
*[Appeared in: 2021 Q7(a), 2022 Q3(b)]*

**Question:**
* **(a)** Define slew rate and common-mode rejection ratio (CMRR) for an operational amplifier. **[02 Marks, CLO1]**

**Answer:**
*   **Common-Mode Rejection Ratio (CMRR):** The ratio of the differential gain ($A_d$) to the common-mode gain ($A_c$). It indicates the amplifier's ability to reject common-mode noise.
*   **Slew Rate (SR):** The maximum rate of change of the op-amp's output voltage. It is $SR = \left. \frac{dv_o}{dt} \right|_{max}$ in $\text{V}/\mu\text{s}$. If the input demands a faster change, the output distorts. Sine waves turn into triangular waves.

**Slew Rate Maximum Frequency Formula:**
For a sinusoidal output $v_o(t) = V_p \sin(2\pi f t)$, the maximum rate of change is $2\pi f V_p$. To prevent distortion:
$$ SR \ge 2\pi f V_p \Rightarrow f_{max} = \frac{SR}{2\pi V_p} $$

---

## 3. High-Frequency Limitations

### 3.1 Gain-Bandwidth Product (GBW)
*[Appeared in: 2024 Q4(c)]*

**Question:**
* **(c)** Define the gain-bandwidth product ($GBW$). What are the main physical capacitances that limit the high-frequency response of BJT and FET amplifiers? **[02 Marks, CO1]**

**Answer:**
**Gain-Bandwidth Product (GBW):**
The Gain-Bandwidth Product ($GBW$ or $f_T$) is a constant parameter. It is the frequency where the open-loop gain drops to 1 ($0\text{ dB}$). The gain rolls off at $-20\text{ dB/decade}$. So the product of closed-loop gain ($A_{CL}$) and closed-loop bandwidth ($BW$) always equals this constant ($GBW = A_{CL} \times BW$).

**Limiting Physical Capacitances:**
1.  **Miller Capacitance:** The parasitic capacitance between the input and output nodes of an internal stage. The Miller effect multiplies this capacitance by the stage gain. This dominates the high-frequency roll-off.
2.  **Input Junction Capacitance:** The Base-Emitter capacitance ($C_{be}$ or $C_{\pi}$) in BJTs, and Gate-Source capacitance ($C_{gs}$) in FETs.
3.  **Wiring and Stray Capacitances:** Parasitic capacitances from the physical traces and packaging layout that shunt high-frequency signals to ground.

[Previous](03_Feedback_Amplifiers.md) | [Home](index.md) | [Next](05_OpAmp_Applications.md)
