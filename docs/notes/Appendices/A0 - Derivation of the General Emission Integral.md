# Radiative Transitions in Solids
Consider electrons in a solid. It's Hamiltonian consists of the kinetic energy term and the lattice term which embodies the periodic nature of the material. In the presence of an E&M field the Hamiltonian is
$$
\begin{align}
\hat{H} &= \frac{\big[\hat{\mathbf{p}}+e\mathbf{A}(\hat{\mathbf{r}},t)\big]^{2}}{2m_{e}} + V_{\text{lattice}}(\hat{\mathbf{r}}) \\
&\approx  \underbrace{ \frac{\hat{\mathbf{p}}\cdot\hat{\mathbf{p}}}{2m_{e}} + V_{\text{lattice}}(\hat{\mathbf{r}}) }_{ \hat{H}_{0} } + \underbrace{ \frac{e}{2m_{e}}\Big[\mathbf{A}(\hat{\mathbf{r}},t)\cdot \hat{\mathbf{p}}  +\hat{\mathbf{p}}\cdot\mathbf{A}(\hat{\mathbf{r}},t)\Big] }_{ \hat{H}_{\text{int}} }
\end{align}
$$
The diamagnetic terms, $|\mathbf{A}(\hat{\mathbf{r}},t)|^{2}$, term relates to a two-photon process which is negligible in the case of spontaneous emission and we take the common course of neglecting it.

- [ ] ==nonlinear effects for strong laser pumps \ pulsed dynamics? Well, for pulsed radiation $\mathbf{A}(\hat{\mathbf{r}},t)$ would be different).==
- [ ] Coulomb gauge - always have this freedom?
- [ ] Need to also account for phonon part in Hamiltonian for intraband transitions?

Under the Coulomb gauge $\nabla\cdot\mathbf{A}(\hat{\mathbf{r}},t)=0$ the interaction term can be written as follows
$$
\hat{H}_{\text{int}} = \frac{e}{2m_{e}}\mathbf{A}(\hat{\mathbf{r}},t)\cdot\hat{\mathbf{p}}
$$


# From a Single Transition to the Continuum
Consider an electronic transition between an initial state $\ket{\mathbf{k}_{1}, \alpha}$ and a final state $\ket{\mathbf{k}_{2}, \beta}$, mediated by an energy transfer $\hbar \omega$. The subscripts $\alpha$ and $\beta$represent specific energy bands (valence or conduction), allowing transitions between different branches of the dispersion relation. According to Fermi's Golden Rule, the microscopic transition rate is

$$
\Gamma_{1\to 2}(\hbar\omega) = \frac{2\pi}{\hbar} \left|\mu_{12}^{\alpha\beta}\right|^{2} \ \delta\left(\mathcal{E}_{\beta}(\mathbf{k}_{2}) - \mathcal{E}_{\alpha}(\mathbf{k}_{1}) + \hbar\omega \right)
$$

where $\mu_{12}^{\alpha\beta}$ is the transition dipole moment governing momentum conservation, and the Dirac delta function enforces energy conservation based on the band-specific dispersion relations $\mathcal{E}_{\alpha}$and $\mathcal{E}_{\beta}$.


For clarity, we temporarily suppress the band indices to derive the rate for a generic pair of bands. To determine the rate $\Gamma_{1}$ from a specific initial state $\ket{\mathbf{k}_{1}}$, we sum over all available final states $\ket{\mathbf{k}_{2}}$. This summation is weighted by the probability of the final state being vacant, $[1-f(\mathbf{k}_{2})]$, and accounts for spin degeneracy. In the continuum limit, the discrete summation over wave-vectors transforms into an integral over the Brillouin Zone (BZ) with a density of states factor $V/(2\pi)^{3}$:

$$\begin{align} \Gamma_{1}(\hbar\omega) &= 2 \cdot \sum_{\mathbf{k}_{2}} \ \Gamma_{1\to 2}(\hbar\omega) \Big[1-f(\mathbf{k}_{2})\Big] \\ &= 2V \int\limits_{\text{BZ}} \frac{d^{3}k_{2}}{(2\pi)^{3}} \ \Gamma_{1\to 2}(\hbar\omega) \Big[1-f(\mathbf{k}_{2})\Big] \end{align}$$

Similarly, to obtain the total rate for this band pair, we sum the single-state rates over all possible initial states $\ket{\mathbf{k}_{1}}$, weighted by the occupation probability $f(\mathbf{k}_{1})$

$$\begin{align} \Gamma (\hbar\omega) &= 2\cdot \sum_{\mathbf{k}_{1}} \ \Gamma_{1}(\hbar\omega) f(\mathbf{k}_{1}) \\ &= 2V \int\limits_{\text{BZ}} \frac{d^{3}k_{1}}{(2\pi)^{3}} \ \Gamma_{1}(\hbar\omega) \ f(\mathbf{k}_{1}) \end{align}$$

Finally, to account for all possible emission channels, we reintroduce the band indices and perform a general summation over all bands $\alpha$ and $\beta$. This covers all permutations, including interband (conduction-valence $\alpha\beta = cv$) and intraband (conduction-conduction $\alpha\beta =cc$) transitions. Defining $\overline{f_{\beta}(\mathbf{k})} \equiv 1 - f_{\beta}(\mathbf{k})$, the general expression is

$$\boxed{ \Gamma(\hbar\omega) = \frac{2\pi}{\hbar} \left( \frac{2V}{(2\pi)^{3}} \right)^{2} \sum_{\alpha, \beta} \iint\limits_{\text{BZ}} |\mu^{\alpha\beta}(\mathbf{k_{1}},\mathbf{k_{2}})|^{2} \ f_{\alpha}(\mathbf{k}_{1})\overline{f_{\beta}(\mathbf{k}_{2})} \ \delta\big(\mathcal{E}_{\beta}(\mathbf{k}_{2}) - \mathcal{E}_{\alpha}(\mathbf{k}_{1}) + \hbar\omega \big) \ d^{3}k_{1} \ d^{3}k_{2} }$$