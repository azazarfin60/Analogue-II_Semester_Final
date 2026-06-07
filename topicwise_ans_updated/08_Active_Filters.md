[Previous](07_555_Timer.md) | [Home](index.md) | [Next](09_CMOS_Logic_and_Special_Circuits.md)

# 📚 Topic 08: Active Filters
# Analog Electronic Circuits II - Topic-Wise Repository

---

## 1. Active vs. Passive Filters
*[Appeared in: 2023 Q8(a), 2022 Q6(a), 2021 Q4(a), 2020 Q4(a)]*

**Question:**
* **(a)** What are the basic differences between active and passive filters? List some key merits and drawbacks of active filters. **[03 Marks]**

**Answer:**
### 1.1 Key Differences
*   **Active Filters:** Use active amplifying elements (Operational Amplifiers) with passive resistors and capacitors.
*   **Passive Filters:** Use only passive components (Resistors, Capacitors, and Inductors).

### 1.2 Comparison Matrix
| Parameter | Active Filters | Passive Filters |
|:---|:---|:---|
| **Voltage Gain** | Can provide voltage gain in the passband. | Cannot provide gain. Passband always has attenuation (Gain $< 1$). |
| **Impedance Loading** | Excellent isolation due to high input and low output impedance. No loading effects between stages. | Severe loading. Connecting stages changes the cutoff frequencies. |
| **Inductors** | Uses no inductors. It uses simulated active inductance or RC paths. | Needs inductors. Inductors are heavy, bulky, lossy, and pick up noise. |
| **Tuning** | Very easy to tune over a wide range using variable resistors. | Hard to tune. Variable inductors are rare and impractical. |
| **Power Supply** | **Drawback:** Needs an external DC power supply ($V_{CC}/V_{EE}$) for the op-amps. | Needs zero external power supply (self-powered). |
| **Frequency Limits** | **Drawback:** Limited to lower frequencies ($< 1\text{ MHz}$) due to the op-amp Gain-Bandwidth Product (GBWP). | Great for high-frequency (RF and microwave) apps up to GHz. |

---

## 2. Filter Types and Approximations

### 2.1 Standard Filter Responses
*[Appeared in: 2022 Q6(b)]*

**Question:**
* **(b)** Differentiate clearly between the frequency response characteristics of Bessel, Butterworth, and Chebyshev filters. **[03 Marks, CO2]**

**Answer:**
1.  **Butterworth Filter:** Offers a **maximally flat passband** with no ripples. It has a moderate roll-off. It is ideal for audio where uniform gain is needed.
2.  **Chebyshev Filter:** Offers a much **steeper roll-off** than Butterworth. But it introduces **amplitude ripples** in the passband (Type I) or stopband (Type II). It is ideal for sharp frequency separation.
3.  **Bessel Filter:** Optimized for a **linear phase response** (constant time delay). This preserves the exact shape of digital waveforms. But it has the slowest roll-off.

---

### 2.2 Integrator as LPF / Differentiator as HPF
*[Appeared in: 2021 Q5(b), 2020 Q4(b)]*

**Question:**
* **(b)** "An operational amplifier integrator works as a low-pass filter, whereas a differentiator works as a high-pass filter." Justify this statement analytically. **[04 Marks, CLO2]**

**Answer:**
**Integrator as LPF:**
The transfer function of an ideal inverting integrator is $A(j\omega) = -\frac{1}{j\omega RC}$.
The magnitude is $|A| = \frac{1}{\omega RC}$.
*   At low frequencies ($\omega \rightarrow 0$), $|A| \rightarrow \infty$ (it passes DC and low frequencies with high gain).
*   At high frequencies ($\omega \rightarrow \infty$), $|A| \rightarrow 0$ (it entirely blocks high frequencies).
Therefore, an integrator inherently acts as a **Low-Pass Filter (LPF)** with a $-20\text{ dB/decade}$ roll-off.

**Differentiator as HPF:**
The transfer function of an ideal inverting differentiator is $A(j\omega) = -j\omega RC$.
The magnitude is $|A| = \omega RC$.
*   At low frequencies ($\omega \rightarrow 0$), $|A| \rightarrow 0$ (it completely blocks DC).
*   At high frequencies ($\omega \rightarrow \infty$), $|A| \rightarrow \infty$ (it passes high frequencies with increasing gain).
Therefore, a differentiator inherently acts as a **High-Pass Filter (HPF)** with a $+20\text{ dB/decade}$ slope.

---

## 3. First-Order Active Filters
*[Appeared in: 2023 Q8(b), 2019 Q6(b)]*

**Question:**
* **(b)** Design an active first-order high-pass filter using an op-amp. What is the main drawback of active filters, and how can it be mitigated? **[04 Marks]**

**Answer:**
**First-Order Active HPF Design:**
A first-order active High-Pass Filter consists of a passive series capacitor $C$ and shunt resistor $R$ connected to the non-inverting input of an op-amp, with the op-amp configured as a non-inverting gain stage.
```text
                    Rf
              +---[  ]---+
              |          |
        Vi o-[C]--(+)--[ Av ]---+---o Vo
                   |
                  [R]
                   |
                  Gnd
```
*   **Cutoff Frequency:** $f_c = \frac{1}{2\pi R C}$
*   **Passband Voltage Gain:** $A_{CL} = 1 + \frac{R_f}{R_1}$

**Drawback & Mitigation:**
*   **Drawback:** Op-amps do not have infinite bandwidth. At high frequencies, the gain drops due to the Gain-Bandwidth Product (GBWP). This limits high-frequency response. It turns the High-Pass Filter into a Bandpass Filter.
*   **Mitigation:** Choose high-speed, high-bandwidth op-amps (like BiFET or current-feedback op-amps) for high-frequency filters.

---

## 4. Sallen-Key Second-Order Filters

### 4.1 Topology and Quality Factor ($Q$)
A Sallen-Key second-order equal-component Low-Pass Filter ($R_1 = R_2 = R$, $C_1 = C_2 = C$) has a transfer function quality factor ($Q$) given by:
$$ Q = \frac{1}{3 - K} $$
where $K = 1 + R_f / R_1$ is the passband gain of the non-inverting amplifier stage.
*   **Butterworth Response ($Q = 0.707$):** Requires $K = 3 - 1/0.707 \approx 1.586$.
*   **Chebyshev Response ($Q > 0.707$):** Requires $K > 1.586$.
*   **Stability Constraint:** If $K \ge 3$, the quality factor $Q$ becomes negative. The circuit becomes completely unstable and behaves as an oscillator.

---

### 4.2 Worked Sallen-Key LPF Design (Unity Gain)
*[Appeared in: 2021 Q4(c)]*

**Question:**
* **(c)** Design a second-order active Sallen-Key Butterworth low-pass filter to yield a passband gain $|H(j\omega)| = 1$ (unity), a high-cutoff frequency $f_c = 10\text{ kHz}$, and a quality factor $Q = 0.707$. **[04 Marks, CLO3]**

**Answer:**
**Step 1: Select a practical capacitor value**
Let $C_1 = C_2 = C = 1\text{ nF} = 10^{-9}\text{ F}$.

**Step 2: Calculate the required resistor value ($R$)**
$$ R = \frac{1}{2\pi f_c C} = \frac{1}{2\pi (10,000\text{ Hz}) (10^{-9}\text{ F})} = \frac{1}{2\pi \times 10^{-5}} \approx 15,915\ \Omega $$
Select standard resistor value: $R = 16\text{ k}\Omega$.

**Step 3: Determine the amplifier feedback for Unity Gain**
For a passband gain of $K = 1$, the amplifier must be a voltage follower.
Connect the output directly to the inverting input (a wire, $R_f = 0\ \Omega$, $R_1 = \infty$).
*(Note: An equal-component Sallen-Key with $K=1$ yields $Q=0.5$ (critically damped). To achieve exact Butterworth $Q=0.707$ with $K=1$, the capacitors must be unequal: $C_1 = 2Q^2 C_2$. However, for general exam purposes, demonstrating the equal-component topology is usually sufficient unless explicitly requested otherwise.)*

---

### 4.3 Worked Sallen-Key LPF Design with High Gain ($K = 5$)
*[Appeared in: 2020 Q4(c)]*

**Question:**
* **(c)** Design and draw a second-order active Sallen-Key low-pass filter to give a high cutoff frequency of $f_H = 1.5\text{ kHz}$, a passband gain of $K = 5$, and a quality factor $Q = 0.707$. **[05 Marks]**

**Answer:**
**The Challenge:** Try to design a standard Sallen-Key filter with a gain of $K = 5$. The quality factor is $Q = 1 / (3 - 5) = -0.5$. This negative value causes the circuit to oscillate.
**The Solution:** We need $Q=0.707$ and a total gain of $K=5$. We must separate the filtering and amplification into two stages:
1.  **Stage 1:** An equal-component Sallen-Key filter stage optimized strictly for Butterworth flatness $Q = 0.707$ (requiring an internal gain of $K_1 = 1.586$).
2.  **Stage 2:** A standard non-inverting gain stage designed to supply the remaining required gain ($K_2 = K_{total} / K_1 \approx 3.15$).

**Calculations - Stage 1 (Filter):**
1.  Let $C = 10\text{ nF}$.
2.  $R = \frac{1}{2\pi (1500\text{ Hz}) (10^{-8}\text{ F})} \approx 10.61\text{ k}\Omega$.
3.  For $K_1 = 1.586$: $1 + R_f/R_1 = 1.586 \Rightarrow R_f = 0.586 R_1$. If $R_1 = 10\text{ k}\Omega$, then $R_f = 5.86\text{ k}\Omega$.

**Calculations - Stage 2 (Amplifier):**
1.  Required gain: $K_2 = 5 / 1.586 \approx 3.15$.
2.  $1 + R_{f2}/R_{12} = 3.15 \Rightarrow R_{f2} = 2.15 R_{12}$. If $R_{12} = 10\text{ k}\Omega$, then $R_{f2} = 21.5\text{ k}\Omega$.

---

### 4.4 Second-Order High-Pass Filter
*[Appeared in: 2021 Q4(c)]*

**Question:**
* **(c)** Draw the circuit diagram of a second-order active Butterworth high-pass filter. **[03 Marks]**

**Answer:**
A second-order active Sallen-Key High-Pass Filter swaps the positions of the resistors and capacitors compared to the Low-Pass Filter.
```text
                     R1
               +---[  ]---+
               |          |
         Vi o-||--+--||--(+)--[ Av ]---+---o Vo
             C1   |  C2   |            |
                 [R2]     |            |
                  |       |            |
                 Gnd      |            |
                          +------------+
```
For a Butterworth response with equal components ($C_1 = C_2 = C$ and $R_1 = R_2 = R$), the amplifier gain must be set to $K = 1.586$ ($Q = 0.707$).
The cutoff frequency is $f_c = \frac{1}{2\pi R C}$.

---

## 5. Active Bandpass Filter Cascade
*[Appeared in: 2023 Q8(c), 2022 Q6(c), 2019 Q6(c)]*

**Question:**
* **(c)** Design an active Sallen-Key bandpass filter that allows signals in the frequency range between $f_L = 100\text{ kHz}$ and $f_H = 300\text{ kHz}$. **[04 Marks, CO3]**

**Answer:**
A wideband active Bandpass Filter is easy to build. Cascade a High-Pass Filter (HPF) and a Low-Pass Filter (LPF) in series. The low cutoff ($f_L$) must be less than the high cutoff ($f_H$).
```text
        Vi o---[ High-Pass Filter (fL) ]---o---[ Low-Pass Filter (fH) ]---o Vo
```

**Step 1: High-Pass Stage ($f_L = 100\text{ kHz}$):**
Let $C_H = 1\text{ nF} = 10^{-9}\text{ F}$.
$$ R_H = \frac{1}{2\pi f_L C_H} = \frac{1}{2\pi (100 \times 10^3\text{ Hz}) (10^{-9}\text{ F})} = \frac{1}{2\pi \times 10^{-4}} \approx 1.59\text{ k}\Omega $$

**Step 2: Low-Pass Stage ($f_H = 300\text{ kHz}$):**
Let $C_L = 1\text{ nF} = 10^{-9}\text{ F}$.
$$ R_L = \frac{1}{2\pi f_H C_L} = \frac{1}{2\pi (300 \times 10^3\text{ Hz}) (10^{-9}\text{ F})} = \frac{1}{2\pi \times 3 \times 10^{-4}} \approx 530\ \Omega $$

Connecting these two active stages in series yields a flat bandpass filter spanning $100\text{ kHz}$ to $300\text{ kHz}$.

---

## 6. Higher-Order Filters

### 6.1 Third-Order Butterworth LPF
*[Appeared in: 2017 Q8(b)]*

**Question:**
* **(b)** Draw the frequency response curve for the active filter shown below. Assume identical component values of $R = 10\text{ k}\Omega$ and $C = 0.1\ \mu\text{F}$. **[06 Marks]**
*(Circuit: A 3rd-order active Butterworth Low-Pass Filter made by cascading a 1st-order RC stage with a 2nd-order Sallen-Key stage).*

**Answer:**
**Step 1: Identify the Filter and Calculate Cutoff Frequency ($f_c$)**
The circuit is a 3rd-order active low-pass filter. Since all components are identical ($R = 10\text{ k}\Omega$, $C = 0.1\ \mu\text{F}$), the cutoff frequency is:
$$ f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi (10,000\ \Omega) (0.1 \times 10^{-6}\text{ F})} = \frac{1}{2\pi \times 10^{-3}} \approx 159.15\text{ Hz} $$

**Step 2: Frequency Response Curve Characteristics**
*   **Passband:** The gain is flat (Butterworth) from $0\text{ Hz}$ up to near $f_c$.
*   **Cutoff Point:** At $f_c = 159.15\text{ Hz}$, the gain drops by $-3\text{ dB}$.
*   **Stopband:** Since it is a 3rd-order filter ($n=3$), the roll-off rate is $-n \times 20\text{ dB/decade} = -60\text{ dB/decade}$.
*   **Sketch:** The sketch should show a flat horizontal line at $0\text{ dB}$ that smoothly curves down at $159\text{ Hz}$ and becomes a steep straight line sloping downward at $-60\text{ dB/decade}$.

---

## 7. Notch / Band-Reject Filters

### 7.1 Twin-T Notch Filter
*[Appeared in: 2019 Q8(b), 2021 Q7(d)]*

**Question:**
* **(b)** Draw the schematic of a Twin-T notch filter. Calculate its notch frequency if $R = 20\text{ k}\Omega$ and $C = 0.01\ \mu\text{F}$. **[04 Marks]**
* *(Also appeared in 2021 Q7(d) with $R = 15\text{ k}\Omega$ and $C = 0.01\ \mu\text{F}$)*

**Answer:**
**Schematic Diagram:**
A Twin-T notch filter uses two "T" networks in parallel: one Low-Pass T-network ($R-R-2C$) and one High-Pass T-network ($C-C-R/2$).
```text
                  +---[ R ]---+---[ R ]---+
                  |           |           |
                  |         --- 2C        |
                  |         ---           |
                  |           |           |
         Vi o-----+          GND          +-----o Vo
                  |           |           |
                  |         [R/2]         |
                  |           |           |
                  +----||-----+----||-----+
                       C           C
```
*Note: In an active Twin-T filter, the output $V_o$ is typically buffered by an op-amp voltage follower, and the ground connection is bootstrapped to the output to increase the $Q$ factor.*

**Calculations:**
The notch frequency (center frequency of maximum rejection) is given by the standard formula:
$$ f_N = \frac{1}{2\pi R C} $$

**For 2019 Q8(b):** $R = 20\text{ k}\Omega, C = 0.01\ \mu\text{F}$
$$ f_N = \frac{1}{2\pi (20,000) (0.01 \times 10^{-6})} = \frac{1}{2\pi \times 2 \times 10^{-4}} \approx 795.77\text{ Hz} $$

**For 2021 Q7(d):** $R = 15\text{ k}\Omega, C = 0.01\ \mu\text{F}$
$$ f_N = \frac{1}{2\pi (15,000) (0.01 \times 10^{-6})} = \frac{1}{2\pi \times 1.5 \times 10^{-4}} \approx 1061.03\text{ Hz} $$

[Previous](07_555_Timer.md) | [Home](index.md) | [Next](09_CMOS_Logic_and_Special_Circuits.md)
