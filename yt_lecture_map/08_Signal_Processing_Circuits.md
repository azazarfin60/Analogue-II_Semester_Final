# 08: Signal Processing Circuits

## All About Electronics
All About Electronics covers diode-based, op-amp-based signal modification, and active filtering circuits:
- **Diode Clippers**: Waveform clipping concepts with passive diodes are explained in "Clipper Circuit Explained" starting at [0:10](https://www.youtube.com/watch?v=S76CnEJMl5E&t=10s).
- **Diode Clampers**: DC restoring/shifting waves using capacitors and diodes are analyzed in "Clamper Circuit Explained" starting at [0:10](https://www.youtube.com/watch?v=7O3Hbkkt624&t=10s).
- **Precision Rectifier**: Eliminating the cut-in voltage ($V_\gamma = 0.7\text{ V}$) of practical diodes using op-amps is explained in "What is Precision Rectifier" starting at [0:10](https://www.youtube.com/watch?v=5HweBajP-5g&t=10s).
- **Log & Antilog Amplifiers**: Performing mathematical calculations like multiplication and division on analog signals using exponential transistor characteristics is shown in "Log and Antilog Amplifiers Explained" starting at [0:10](https://www.youtube.com/watch?v=Nrfb-s0wl6g&t=10s).
- **Active Filters**:
  - **Active LP & HP Filters**: Introduction to active Low-Pass and High-Pass filters using op-amps, illustrating buffering benefits (preventing loading effects) and frequency roll-offs, is covered in "Active Low Pass Filter and Active High Pass Filter Explained" starting at [0:10](https://www.youtube.com/watch?v=gEeF8sEQTEc&t=10s).
  - **Butterworth Filter Design**: Design procedures, frequency response parameters, and cascading rules for Low-Pass and High-Pass Butterworth filters are discussed in "Butterworth Filter : Design of Low Pass and High Pass Filters" starting at [0:10](https://www.youtube.com/watch?v=lc6QT8VjqVc&t=10s).
  - **Sallen-Key 2nd-Order Filters**: Design, analysis, and frequency responses of second-order active low-pass filters utilizing the Sallen-Key topology are shown in "Low-Pass Filter Frequency Response (Sallen-Key Filter Topology)" starting at [0:10](https://www.youtube.com/watch?v=KawlPpyvy9M&t=10s).

## Ankit Goyal Sir
Ankit Goyal Sir covers non-linear diode and op-amp circuits with a strong emphasis on network analysis, transient responses, active filters, and operational limitations:
- **Clippers & Clampers (Passive)**: Diode caking, wave-shaping limits, and reference bias networks are analyzed in "Clippers Part -1" starting at [03:00](https://www.youtube.com/watch?v=yf4OGnr7t90&t=180s) and "Clampers and Voltage Multipliers" starting at [04:00](https://www.youtube.com/watch?v=WSv4x7WYRQY&t=240s).
- **Precision Rectifiers**: The design of half-wave and full-wave precision rectifiers, explaining how negative feedback eliminates diode threshold limitations, is analyzed in "Non-Linear Applications of Op-Amp" starting at [38:29](https://www.youtube.com/watch?v=X2qRaM9ET1c&t=2309s) (Half Wave) and [56:22](https://www.youtube.com/watch?v=X2qRaM9ET1c&t=3382s) (Full Wave).
- **Peak Detector**: Storing the highest value of a transient signal using a precision rectifier combined with a capacitive filter is covered in "Non-Linear Applications of Op-Amp" starting at [78:05](https://www.youtube.com/watch?v=X2qRaM9ET1c&t=4685s).
- **Log & Antilog Amplifiers**: Detailed analytical model derivations of logarithmic and exponential amplifiers, including analog multiplication and division using logarithmic operations, are derived in "Non-Linear Applications of Op-Amp" starting at [85:38](https://www.youtube.com/watch?v=X2qRaM9ET1c&t=5138s).
- **Active Filters**:
  - **First-Order Filters & Scaling**: Mathematical derivations of Low-Pass/High-Pass Butterworth active filters, transfer functions, and frequency scaling are discussed in "Active Filters | Part 1" starting at [13:21](https://www.youtube.com/watch?v=uyNkaSlDBfE&t=801s).
  - **Sallen-Key 2nd-Order Filters**: Complete mathematical model derivations of the general Sallen-Key filter topology, followed by specific transfer function calculations for Low-Pass and High-Pass 2nd-order filters, corner frequency ($\omega_0 = \frac{1}{\sqrt{R_1 R_2 C_1 C_2}}$), and quality factor ($Q$) are derived in "Active Filters | Part 2" starting at [34:50](https://www.youtube.com/watch?v=I4-bHpHwlWw&t=2090s).

---

### 💡 Syllabus Supplement: Negative Impedance Converter (NIC)
*Since Negative Impedance Converters are a pure theoretical component of the ECE 2105 syllabus not covered explicitly in either playlist, this study guide is provided here for your complete exam revision.*

#### 1. Concept and Circuit Configuration
A **Negative Impedance Converter (NIC)** is an active op-amp configuration that utilizes positive feedback to present an input impedance that is the negative of the load impedance attached to its output.

The basic circuit consists of:
- An op-amp.
- A feedback resistor $R_1$ from the output to the non-inverting terminal ($V^+$).
- A feedback resistor $R_2$ from the output to the inverting terminal ($V^-$).
- The non-inverting terminal is connected to the input source $V_{in}$.
- The inverting terminal is connected to a resistor (or load) $Z_L$ to ground.

#### 2. Mathematical Derivation
By virtual short (assuming ideal op-amp):
$$
V^- = V^+ = V_{in}
$$

The current flowing through the inverting branch to the load $Z_L$ is:
$$
I_L = \frac{V^-}{Z_L} = \frac{V_{in}}{Z_L}
$$

The output voltage of the op-amp is:
$$
V_{out} = V^- + I_L R_2 = V_{in} \left(1 + \frac{R_2}{Z_L}\right)
$$

Now, the current entering the input node ($V^+$ terminal) from the input source $V_{in}$ through the feedback resistor $R_1$ is:
$$
I_{in} = \frac{V_{in} - V_{out}}{R_1}
$$

Substituting the expression for $V_{out}$:
$$
I_{in} = \frac{V_{in} - V_{in} \left(1 + \frac{R_2}{Z_L}\right)}{R_1} = -\frac{V_{in} R_2}{R_1 Z_L}
$$

The equivalent input impedance seen by the source is:
$$
Z_{in} = \frac{V_{in}}{I_{in}} = -Z_L \left(\frac{R_1}{R_2}\right)
$$

If $R_1 = R_2$, then:
$$
Z_{in} = -Z_L
$$

#### 3. Key Applications
- **Cancelling Resistance**: Used to cancel positive resistance in telephone transmission lines to minimize signal attenuation.
- **Active Filters**: Employed in active filter design to simulate inductors (gyrators) or create stable high-Q resonators.
- **Oscillators**: Used as a negative resistance element to sustain oscillation in LC resonant tanks.
