# 📚 Topic 08: Active Filters
# Analog Electronic Circuits II — Topic-Wise Repository

---

## 1. Active vs. Passive Filters
*[Appeared in: 2024 Q6(a), 2020 Q4(a), 2021 Q3(a)]*

### 1.1 Key Differences
*   **Active Filters:** Constructed using active elements (Operational Amplifiers) in combination with passive resistors and capacitors.
*   **Passive Filters:** Constructed exclusively using passive components (Resistors, Capacitors, and Inductors).

### 1.2 Comparison Matrix
| Parameter | Active Filters | Passive Filters |
|:---|:---|:---|
| **Voltage Gain** | Can provide voltage gain (signal amplification). | Cannot provide gain; passband always exhibits attenuation (Gain $< 1$). |
| **Impedance Loading** | Excellent isolation due to op-amp's high input and low output impedance. No loading between stages. | Severe loading. Connecting stages together alters the individual cutoff frequencies. |
| **Inductors** | Completely eliminates inductors, utilizing simulated active inductance or RC paths. | Requires inductors, which are heavy, bulky, lossy (high internal resistance), and prone to electromagnetic pickup. |
| **Tuning** | Extremely easy to tune over a wide frequency range using variable resistors (potentiometers). | Difficult to tune; variable inductors are rare and physically impractical. |
| **Power Supply** | Requires an external DC power supply ($V_{CC}/V_{EE}$) to bias the operational amplifiers. | Requires zero external power supply (completely self-powered). |
| **Frequency Limits** | Limited to lower frequencies ($< 1\text{ MHz}$) due to the Gain-Bandwidth Product (GBWP) of the op-amps. | Excellent for high-frequency (RF and microwave) applications up to GHz. |

---

## 2. Filter Types and Approximations

### 2.1 Standard Filter Responses
*[Appeared in: 2024 Q6(b)]*

1.  **Butterworth Filter:** Offers a **maximally flat passband** response with no ripples. It has a moderate roll-off transition region.
2.  **Chebyshev Filter:** Offers a **steep roll-off** transition region, but introduces noticeable **amplitude ripples** in either the passband (Type I) or stopband (Type II).
3.  **Bessel Filter:** Offers a **linear phase response** (constant time delay), preserving the shape of pulsed/digital waveforms. However, it has the slowest roll-off rate in the transition region.

---

### 2.2 Third-Order Active LPF Response Curves
*[Appeared in: 2017 Q8(b)]*

A 3rd-order active LPF consists of a 2nd-order active stage cascaded with a 1st-order active stage.

```
        Vi o---[ 2nd-Order LPF ]---o---[ 1st-Order LPF ]---o Vo
```

If designed with identical $R = 10\text{ k}\Omega$ and $C = 0.1\ \mu\text{F}$:
*   **Cutoff Frequency ($f_c$):**
    $$
    f_c = \frac{1}{2\pi R C} = \frac{1}{2\pi (10\text{ k}\Omega)(0.1\ \mu\text{F})} \approx 159.15\text{ Hz}
    $$
*   **Frequency Response Curve Description:**
    *   **Passband ($f < 159\text{ Hz}$):** The gain is completely flat at $0\text{ dB}$ (unity).
    *   **Cutoff Point ($f = 159\text{ Hz}$):** The gain is down by exactly $-3\text{ dB}$.
    *   **Stopband ($f > 159\text{ Hz}$):** The roll-off is extremely steep. Because it is a 3rd-order filter, the asymptotic slope is:
        $$
        \text{Roll-off} = -60\text{ dB/decade} \quad (\text{or } -18\text{ dB/octave})
        $$

---

## 3. First-Order Active Filters
*[Appeared in: 2019 Q6(b)]*

### 3.1 First-Order Active HPF Design
A first-order active High-Pass Filter consists of a passive series capacitor and shunt resistor connected to the non-inverting input of an op-amp, with the op-amp configured as a non-inverting gain stage.

```
                    Rf
              +---[  ]---+
              |          |
        Vi o-[C]--(+)--[ Av ]---+---o Vo
                   |
                  [R]
                   |
                  Gnd
```

The cutoff frequency is:
$$
f_c = \frac{1}{2\pi R C}
$$
The passband voltage gain is:
$$
A_{CL} = 1 + \frac{R_f}{R_1}
$$

### 3.2 Drawback & Mitigation
*   **Drawback:** An operational amplifier does not have infinite bandwidth. Its open-loop gain rolls off at high frequencies due to the Gain-Bandwidth Product (GBWP) limitation. Therefore, at very high frequencies, the active HPF's gain will drop, transforming the high-pass filter into a bandpass filter in reality.
*   **Mitigation:** Select high-speed, high-bandwidth operational amplifiers (e.g., BiFET or current-feedback op-amps) for high-frequency designs.

---

## 4. Sallen-Key Second-Order Filters

### 4.1 Topology and Quality Factor ($Q$)
A Sallen-Key second-order equal-component Low-Pass Filter ($R_1 = R_2 = R$, $C_1 = C_2 = C$) has a transfer function quality factor ($Q$) given by:
$$
Q = \frac{1}{3 - K}
$$
where $K = 1 + R_f / R_1$ is the passband gain of the non-inverting amplifier stage.
*   **Butterworth Response ($Q = 0.707$):** Requires $K = 3 - 1/0.707 \approx 1.586$.
*   **Chebyshev Response ($Q > 0.707$):** Requires $K > 1.586$.
*   **Stability Constraint:** If $K \ge 3$, the quality factor $Q$ becomes infinite or negative. The circuit becomes unstable and behaves as an oscillator rather than a stable filter.

---

### 4.2 Worked Sallen-Key LPF Design with Gain ($K > 1$)
*[Appeared in: 2020 Q4(c)]*

**Problem Details:**
Design a second-order active Sallen-Key low-pass filter with cutoff frequency $f_H = 1.5\text{ kHz}$, passband gain $K = 5$, and quality factor $Q = 0.707$.

#### Step-by-Step Design Strategy:
If we try to design an equal-component Sallen-Key filter with a gain of $K = 5$:
$$
Q = \frac{1}{3 - 5} = -0.5
$$
This negative value means the circuit is unstable and will oscillate.
**The Engineering Solution:** To achieve both $Q=0.707$ (Butterworth flatness) and a total passband gain of $K=5$, we must split the circuit into two cascaded stages:
1.  **Stage 1:** An equal-component Sallen-Key filter stage optimized strictly for $Q = 0.707$ (requiring a gain of $K_1 = 1.586$).
2.  **Stage 2:** A standard non-inverting gain stage designed to supply the remaining gain ($K_2 = K_{total} / K_1 \approx 3.15$).

```
        Vi o---[ Stage 1: Sallen-Key (K1 = 1.586) ]---o---[ Stage 2: Gain (K2 = 3.15) ]---o Vo
```

#### Calculations:

##### Stage 1 (Sallen-Key Filter Stage):
1.  **Select a practical capacitor value:** Let $C = 10\text{ nF}$.
2.  **Calculate the resistor values ($R$):**
    $$
    R = \frac{1}{2\pi f_H C} = \frac{1}{2\pi (1500\text{ Hz}) (10 \times 10^{-9}\text{ F})} \approx 10.61\text{ k}\Omega
    $$
3.  **Determine the feedback resistors for $K_1 = 1.586$:**
    $$
    K_1 = 1 + \frac{R_f}{R_1} = 1.586 \Rightarrow R_f = 0.586 R_1
    $$
    Let $R_1 = 10\text{ k}\Omega$:
    $$
    R_f = 5.86\text{ k}\Omega
    $$

##### Stage 2 (Gain Amplifier Stage):
1.  **Calculate required gain ($K_2$):**
    $$
    K_2 = \frac{K_{total}}{K_1} = \frac{5}{1.586} \approx 3.15
    $$
2.  **Determine feedback resistors for $K_2 = 3.15$:**
    $$
    K_2 = 1 + \frac{R_{f2}}{R_{12}} = 3.15 \Rightarrow R_{f2} = 2.15 R_{12}
    $$
    Let $R_{12} = 10\text{ k}\Omega$:
    $$
    R_{f2} = 21.5\text{ k}\Omega
    $$

---

## 5. Active Bandpass Filter Cascade
*[Appeared in: 2022 Q6(c), 2019 Q6(c)]*

An active Bandpass Filter can be constructed by cascading a High-Pass Filter (HPF) and a Low-Pass Filter (LPF) stage in series, provided the low cutoff frequency ($f_L$) is less than the high cutoff frequency ($f_H$).

```
        Vi o---[ High-Pass Filter (fL) ]---o---[ Low-Pass Filter (fH) ]---o Vo
```

### Example Design: $50\text{ kHz}$ to $100\text{ kHz}$ Bandpass
1.  **High-Pass Stage ($f_L = 50\text{ kHz}$):**
    Let $C_H = 1\text{ nF}$.
    $$
    R_H = \frac{1}{2\pi f_L C_H} = \frac{1}{2\pi (50 \times 10^3\text{ Hz}) (1 \times 10^{-9}\text{ F})} \approx 3.18\text{ k}\Omega
    $$
2.  **Low-Pass Stage ($f_H = 100\text{ kHz}$):**
    Let $C_L = 1\text{ nF}$.
    $$
    R_L = \frac{1}{2\pi f_H C_L} = \frac{1}{2\pi (100 \times 10^3\text{ Hz}) (1 \times 10^{-9}\text{ F})} \approx 1.59\text{ k}\Omega
    $$
Connecting these two stages in series yields a flat bandpass filter spanning $50\text{ kHz}$ to $100\text{ kHz}$.
