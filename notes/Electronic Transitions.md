---
degree: MSc
research: photoluminescence
---
#  First Steps
Let us consider a transition between the first branch of a free electron dispersion relation (in the empty lattice approximation) and one of the branches that originate in the reciprocal cells to the right of the 1st Brillouin zone (a 1D lattice).

$$
\begin{align}
\hbar \omega =\Delta E_{n}(k) &= \frac{\hbar^{2}(k-K_{n})^{2}}{2m} - \frac{\hbar^{2}k^{2}}{2m}  \\
&=\frac{\hbar^{2}}{2m}K_{n}(K_{n}-2k)  \\
& = \frac{\hbar^{2}}{2m} \frac{2\pi n}{a} \left(\frac{2\pi n}{a}-2k\right) \\
& = \frac{\hbar^{2}}{m} \frac{\pi n}{a} \left(\frac{\pi n}{a}-k\right)  \\
&= \frac{\hbar^{2}}{m} K_{b}(K_{b}-k) \quad\quad k\in(0,K_{b})
\end{align}
$$

---
# Further Considerations
At the edge of the Brillouin zone the energy difference vanished (for a transition between the first and second band)

$$
\Delta_{\text{min}}=\Delta E(K_{b})=0
$$

while at the center of the transition is
$$
\Delta E_{\text{max}}=\Delta E(0) = \frac{1}{m}\left( \frac{h}{a} \right)^{2} 
$$
The effective mass is the inverse second derivative of the energy, therefore in parabolic dispersion relations (free electrons) the effective mass is, not surprisingly, a free electron mass.

$$
a_{\text{Au}} \approx 0.4 \ [\text{nm}]
$$

$\Delta E_{\text{}{max, Au}}\approx 18 \ \ \text{[eV]}$

---
# Photon Electron Energy Momentum Conservation in Intraband Transitions

Let us deal with the case of an absorption of a photon of energy $E=\hbar\omega$ and a corresponding momentum $q = \omega / c$. An electron with an initial energy $E_{i}$ ends up in a final energy state such that $E_{f}-E_{i}=\hbar \omega$. The electron has a corresponding initial and final momenta
$$
k_{i} = \frac{\sqrt{ 2m E_{i} }}{\hbar} \quad \quad k_{f}= \frac{\sqrt{ 2mE_{f} }}{\hbar}
$$

conservation of energy
$$
\begin{align}
E_{f}-E_{i}&\Rightarrow \hbar \omega_{f}-\hbar\omega_{i}\stackrel{!}{=}\hbar \omega \\
&\Rightarrow \omega_{f}-\omega_{i}=\omega  \\
&\Rightarrow q= \frac{1}{c}(\omega_{f}-\omega_{i})\tag{1}
\end{align}
$$

---

# Conservation (continued)

and conservation of momentum dictates that
$$
\begin{align}
k_{i}+q=k_{f} \quad \Rightarrow \quad q&\stackrel{!}{=}\frac{\sqrt{ 2m }}{\hbar}\left(  \sqrt{E_{\small f} }-\sqrt{ E_{i} }\right) \\
q&= \sqrt{ \frac{2m}{\hbar} } \left( \sqrt{ \omega_{f} }-\sqrt{ \omega_{i} } \right) \tag{2}
\end{align}
$$
Give that we know what the photonic momentum is, are there initial and final electronic energies that satisfy both $(1)$ and $(2)$? Namely, the conservation of energy and momentum.

From $(1)$ we can have $\omega_{f}=\omega_{i}+ qc$. Plugging this into $(2)$ gives

$$
q = \sqrt{ \frac{2m}{\hbar} }\left( \sqrt{ \omega_{i}+qc } -\sqrt{ \omega_{i} } \right)
$$
solution for $\omega_{i}$ is

$$
\begin{align}
\omega_i &= \left(\frac{q \sqrt{\hbar}}{2\sqrt{2m}} - \frac{c\sqrt{m}}{\sqrt{2\hbar}}\right)^2 \\
&= \frac{\hbar}{2m} \left( \frac{q}{2} - \frac{mc}{\hbar} \right)^{2} 
\end{align}
$$

---

# Is energy even conserved?
Is energy even conserved in this process? is it considered scattering? If so is it elastic or not?

In the following the conservation of momentum is not shown in a reduced scheme and thus the momentum is not yet considered to be crystal momentum.

$$
\begin{align}
P_{i}=P_{f} \quad&\Rightarrow\quad k^{i}+q=k^{f} \\
\mathcal{E}_{i}=\mathcal{E}_{f} \quad&\Rightarrow\quad \mathcal{E_{e}^{i}}+\mathcal{E_{ph}}=\mathcal{E_{e}^{f}} \\
&\Rightarrow \quad \frac{\hbar^{2}k_{i}^{2}}{2m_{e}} + \hbar qc = \frac{\hbar^{2}k_{f}^{2}}{2m_{e}}  \\
&\Rightarrow\quad \hbar qc=\frac{\hbar^{2}}{2m_{e}}\underbrace{ (k_{f}-k_{i}) }_{ = q }(k_{f}+k_{i})
\end{align}
$$

Where $q$ and $k$ are the photonic and electronic wave-vectors respectively. Notice in the last transition in the conservation of energy we already inserted the conservation of momentum which ultimately leaves us with

$$
k_{f}+k_{i}=\frac{2m_{e}c}{\hbar}
$$

conclusions:
- Free electrons **cannot** absorb photons due to inability of energy and momentum to be simultaneously conserved. 
- Conduction electrons, while nearly free, can absorb photons thanks to the less strict conservation of crystal momentum. In practice the lattice acts as
- In essence, it is the periodic potential that allows for a redistribution of momentum within the constraints of the crystal's symmetry.

---




$$
\begin{align}

\end{align}
$$