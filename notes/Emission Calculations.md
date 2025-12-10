---
degree: MSc
research: photoluminescence
type: note
---

# Emission Derivation (Energy Space)
The transition rate of an electron from a **single** higher energy state $\ket{\mathcal{E_{i}}}$ to a **single** lower energy state $\ket{\mathcal{E_{f}}}$, accompanied by an emission of a photon with appropriate energy $\hbar\omega$, is given by [Fermi's golden rule](2.%20Notes/Fermi%20Golden%20Rule.md).
$$
\begin{align}
\Gamma_{i\to f}({\small\hbar\omega}) &= \frac{2\pi}{\hbar}|\braket{ \mathcal{E_{i}} |H' | \mathcal{E_{f}} } |^{2} \ \delta({\small \mathcal{E_{f}}-\mathcal{E_{i}}+\hbar\omega}) \\
&= \frac{2\pi}{\hbar}|\mu({\small\mathcal{E_{i}},\mathcal{E_{f}}}) |^{2} \ \delta({\small \mathcal{E_{f}}-\mathcal{E_{i}}+\hbar\omega}) \tag{1}
\end{align} 
$$

The transition rate from a single state $\ket{\mathcal{E}_{i}}$ to all possible final states is gained by integrating over all possible final energy states, weighed by the probability of **vacancy** at each state.
$$
\begin{align}
\Gamma_{i}({\small\hbar\omega}) &= \sum\limits_{\mathcal{E_{f}}} \ \Gamma_{i\to f}{\small (\hbar\omega) } \ \big[ 1-f{\small (\mathcal{E}_{f}) } \big]\\
&\Rightarrow V\int \Gamma_{i\to f}{\small (\hbar\omega) } \ \big[ 1-f{\small (\mathcal{E}_{f}) } \big] \  \rho{\small (\mathcal{E_{f}}) } \ d\mathcal{E_{f}} \tag{2}
\end{align}
$$
And the transition rate from all possible initial states to all possible final states is gain by again integrating over all possible initial energy states, weighed by the probability of **occupancy** at each state.
$$
\begin{align}
\Gamma(\hbar\omega) &= \sum\limits_{\mathcal{E_{i}}}  \ \Gamma_{i}{\small (\hbar\omega) } \ f{\small (\mathcal{E_{i}}) }\\
&\Rightarrow V \int\limits\Gamma_{i}{\small (\hbar\omega) } \ f{\small (\mathcal{E_{i}}) } \ \rho {\small (\mathcal{E_{i}}) } \ d\mathcal{E_{i}} \tag{3}
\end{align}
$$
This accounts for all the possible transitions that result in the emission of a photon with energy $\hbar \omega$, namely this is the emission spectra due to this process. Writing $(3)$ explicitly looks like

$$
\begin{align}
\Gamma(\hbar\omega) &=\frac{2\pi V^{2}}{\hbar} \iint\limits |\mu {\small (\mathcal{E_{i},\mathcal{E_{f}}}) }|^{2}\underbrace{ f{\small (\mathcal{E_{i}})}\rho {\small (\mathcal{E_{i}}) }\big[ 1-f{\small (\mathcal{E_{f}}) } \big]\rho {\small (\mathcal{E_{f}}) }  }_{\Large \equiv \rho _{\scriptsize J}{\small (\mathcal{E_{i},\mathcal{E_{f}}}) } } \ \delta {\small (\mathcal{E_{f}-\mathcal{E_{i}}+\hbar\omega}) } \ d\mathcal{E_{i}} \ d\mathcal{E_{f}} \\ \\
&= \frac{2\pi V^{2}}{\hbar}\int |\mu {\small (\mathcal{E_{i},\mathcal{E_{i}-\hbar\omega}}) }|^{2} \ \rho_{\scriptsize J}{\small (\mathcal{E_{i},\mathcal{E_{i}-\hbar\omega}}) } \ d\mathcal{E_{i}} \tag{4}
\end{align}
$$

Where in the last term we resolved the conservation of energy due to the delta, leaving us with the more practical expression in $(4)$.

When $\mathcal{E}(\mathbf{k})$ is not isotropic in $\mathbf{k}$, calculation such as this in energy space is not readily (if at all) possible, and working in k-space might be more doable.
# Emission Derivation (Momentum Space)
We'll follow the above steps, counting all energy-conserving transitions
$$
\begin{align}
\Gamma_{i\to f}{\small (\hbar\omega) } &= \frac{2\pi}{\hbar}|\braket{ k_{\text{i}} | H'|k_{\text{f}} } |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } })  \\
&= \frac{2\pi}{\hbar}|\mu_{\text{i,f}} |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } }) 
\end{align}
$$

$$
\begin{align}
\Gamma_{i}{\small (\hbar\omega) } &= \overbrace{2}^{\text{ spin states}} \cdot\sum\limits_{\mathbf{k_{f}}}\Gamma_{\text{i}\to \text{f}}{\small (\hbar\omega) }\Big[ 1-f ({\small \mathcal{E}(\mathbf{k_{f}})})  \Big] \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{\text{f}}}}{(2\pi)^{3}} \ \Gamma_{\text{i}\to \text{f}}{\small (\hbar\omega) }\Big[ 1-f ({\small \mathcal{E}(\mathbf{k_{f}})})  \Big] 
\end{align}
$$

$$
\begin{align}
\Gamma{\small (\hbar\omega) } &= 2 \cdot\sum\limits_{\mathbf{k_{f}}} \ \Gamma_{\text{i}}{\small (\hbar\omega) } \ f ({\small \mathcal{E}(\mathbf{k_{i}})}) \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{\text{i}}}}{(2\pi)^{3}} \  \ \Gamma_{\text{i}}{\small (\hbar\omega) } \ f ({\small \mathcal{E}(\mathbf{k_{i}})}) 
\end{align}
$$

$$
\Gamma {\small (\hbar\omega) } = 4V^{2} \iint\limits_{\text{BZ}} \frac{2\pi}{\hbar}|\mu {\small (k_{\text{i}},k_{\text{f}}) }|^{2} \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{i}}}) }}) \Big[ 1 - \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{f}}}) }}) \Big] \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } }) \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}} \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}}
$$
$$
\Gamma {\small (\hbar\omega) } = 4V^{2} \int\limits_{\text{BZ}} \frac{2\pi}{\hbar}  \ f(\mathcal{E}{\small (\mathbf{k_{i}}) }) \left[ \int\limits_{\text{BZ}} |\mu {\small (k_{\text{i}},k_{\text{f}}) }|^{2} \Big[1-f(\mathcal{E}{\small (\mathbf{k_{f}}) })  \Big] \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } })  \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}} \right]  \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}}
$$

The integral in the square brackets is where I've been stuck.
There is the following identity which I've been meaning to use
$$
\int H(\mathcal{E}(k)) \cdot \delta(\mathcal{E}(k) - \mathcal{E_{0}}) \, dk = \int H(\mathcal{E}(k)) \cdot \sum_{\begin{align}
&\ \ \ \ \ k_0\\ &\mathcal{E}(k_{0})=\mathcal{E_{0}}
\end{align}} \frac{\delta(k - k_0)}{|\mathcal{E}'(k_0)|} \, dk.
$$
but haven't managed to derive or find a proper adaptation for the 3D case $\mathcal{E}(k)\to \mathcal{E}(\mathbf{k})$
![](app://515c212a6abe91b7991b486b9f42f9f93f5f/Users/ben/Desktop/[%201%20]%20Studies/[%206%20]%20Obsidian/[%201%20]%20Second%20Brain/4.%20Misc/attachments/Pasted%20image%2020241021094539.png?1729493139000)
# In regions where bands do not
$$\Gamma^{\small X}(\hbar\omega) =  \frac{2\pi}{\hbar} |\mu^{\small X}_{cv}|^{2}\int_{\text{BZ}} \int_{\text{BZ}} f(E^{\small X}_c(\mathbf{k})) \left[1 - f(E^{\small X}_v(\mathbf{k'}))\right] \delta(E^{\small X}_v(\mathbf{k'}) - E^{\small X}_c(\mathbf{k}) + \hbar\omega) \frac{d^3k}{(2\pi)^3} \frac{d^3k'}{(2\pi)^3}$$
cylindrical symmetry can reduce the 6D integral into a 4D integral
$$
d^{3}k \to 2\pi k_{\scriptsize \perp} \ dk_{\scriptsize \perp}dk_{\scriptsize \parallel}
$$

$$
\Gamma_{total}\approx 6\Gamma _{\scriptsize X}+4\Gamma _{\scriptsize L}
$$
# Questions

![](../../../9.%20Misc/attachments/Pasted%20image%2020241021094539.png)

![center|400](../../../9.%20Misc/attachments/Pasted%20image%2020241021101200.png)

$$
\Gamma_{e} = \Gamma _{\scriptsize I\to II}{\small (k<k_{0}) } + \Gamma _{\scriptsize II \to I}{\small (k>k_{0}) }
$$
in 3D $k_{0}$ becomes a 2D surface that distinguished between regions where one band is energetically favorable than the other.

- FGR is derived with harmonic EM perturbations in mind, yet we use it for the calculation of spontaneous emission.
$$
\Gamma {\small (\hbar\omega) } = \frac{8\pi V^{2}}{\hbar} |\mu_{\text{if}}|^{2} \iint\limits_{\text{BZ}}  \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{i}}}) }}) \Big[ 1 - \  f({\small \mathcal{E}{\small (\mathbf{k_{\text{f}}}) }}) \Big] \ \delta(\mathcal{E}{\small (\mathbf{k_{f}}) - \mathcal{E}{\small (\mathbf{k_{i}})+\hbar\omega } }) \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}} \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}}
$$
$$
\delta(\mathcal{E}(k_{\text{f}})-\mathcal{E}(k_{\text{i}})+\hbar\omega)=\frac{1}{2\pi}\int\limits_{-\infty}^{\infty} {\large e^{  ix(\mathcal{E}(k_{\text{f}})-\mathcal{E}(k_{\text{i}})+\hbar\omega)}} \ dx
$$
$$
\Gamma {\small (\hbar\omega) } = \frac{4 V^{2}}{\hbar}|\mu_{if}|^{2}\int\limits_{-\infty}^{\infty}  {\large e^{ ix\hbar\omega }}\,\left\{   \left[ \int\limits_{\text{BZ}}  f(k_{\text{f}}) {\large e^{ ix\mathcal{E} { (k_{\text{f}}) } }} \, \frac{d^{3}k_{\text{f}}}{(2\pi)^{3}} \right]\cdot\left[ \int\limits_{\text{BZ}} \Big( 1-f(k_{\text{i}}) \Big) {\large e^{ -ix\mathcal{E} { (k_{\text{i}}) } }} \, \frac{d^{3}k_{\text{i}}}{(2\pi)^{3}} \right]    \right\} \ dx
$$

Not sure if changing the order of integration is allowed given the non-converging nature of the delta Fourier integral.

$$
\int\limits_{\text{BZ}} \int\limits_{\text{BZ}} \int\limits_{-\infty}^{{\infty}} \quad\longmapsto\quad \int\limits_{-\infty}^{{\infty}}\int\limits_{\text{BZ}} \int\limits_{\text{BZ}}
$$
