---
section: thesis
---
- We now consider intraband transitions namely $\mathcal{E}_{n}=\mathcal{E}_{m}$.
- We also assume a constant transition dipole matrix $\mu_{cc}(\mathbf{k}_{1},\mathbf{k}_{2})\to\mu_{cc}$.

These two allow us to write the general emission integral (omitting the photonic contribution and TDM for brevity) as follows
$$
\begin{align}
I_{e}(\hbar\omega) \approx\;& \iint\limits_{\text{BZ}} 
f(\mathbf{k}_{1})\big[1-f(\mathbf{k}_{2})\big]\,
\delta\!\left(\mathcal{E}(\mathbf{k}_{1})-\mathcal{E}(\mathbf{k}_{2})-\hbar\omega\right)\,
d^{3}k_{1}\, d^{3}k_{2} \tag{1}
\end{align}
$$
For now we assume the free electron approximation which means our dispersion relation is isotropic and the integral can be trivially reduced to a 1D integral in energy space
$$
\begin{align}
I_{e}(\hbar\omega) =& \iint\limits_{0}^{\infty} \,
f(\mathcal{E}(k_{1}))\big[1-(\mathcal{E}(k_{2}))\big]\,
\delta\!\left(\mathcal{E}(k_{1})-\mathcal{E}(k_{2})-\hbar\omega\right)(4\pi k_{1}^{2})(4\pi k_{2}^{2}) \ \,
dk_{1}\, dk_{2} \tag{2}\\ \\ 
=\;& \iint\limits_{0}^{\infty}
f(\mathcal{E}_{1})\big[1-f(\mathcal{E}_{2})\big]\,
\rho(\mathcal{E}_{1})\, \rho(\mathcal{E}_{2})\,
\delta\!\left(\mathcal{E}_{1}-\mathcal{E}_{2}-\hbar\omega\right)\,
d\mathcal{E}_{1}\, d\mathcal{E}_{2} \tag{3}\\ \\ 
=\;& \int\limits_{0}^{\infty}
f(\mathcal{E}+\hbar\omega)\big[1-f(\mathcal{E})\big]\,
\rho(\mathcal{E}+\hbar\omega)\, \rho(\mathcal{E})\,
d\mathcal{E} \tag{4}\\ 
\end{align}
$$
Another approximation we now make is the constant electronic density of states
$$
\begin{align}
I_{e}(\hbar\omega)\approx\; &\rho^{2}(\mathcal{E}_{F})\int_{0}^{\infty}
f(\mathcal{E}+\hbar\omega)\big[1-f(\mathcal{E})\big]\,
\,
d\mathcal{E} \tag{5}
\end{align}
$$
For thermal electronic distribution $f^{T}$ this allows us to write the emission integral in both an exact and an approximate analytic forms
$$
\begin{align} 
I^{T}_{e}(\hbar\omega)=\; &\rho^{2}(\mathcal{E}_{F}) \frac{k_BT}{e^{\beta\hbar\omega}-1}\Big[\beta\hbar\omega+\ln\left(1+e^{-\beta\mu}\right)-\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right)\Big] \tag{6}\\ \\
\approx\;& \rho^{2}(\mathcal{E}_{F})\,\underbrace{ \frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\, }_{ \mathcal{E}_{BB}(\omega) } \tag{7}
\end{align}
$$
And for a steady-state distribution $f^{S}$ we can approximate the result by

$$
\begin{align}
I_{e}^{S}(\hbar\omega)\approx \rho^{2}(\mathcal{E}_{F})\Big[ \mathcal{E}_{BB}(\omega) + \delta_{E} \ A(\omega, \omega_{L}) + \delta^{2}_{E} \ B(\omega, \omega_{L}) \Big] \tag{8}
\end{align}
$$
Where 
$$
\begin{align}
A(\omega, \omega_{L}) &= 2\mathcal{E}_{BB}(\omega-\omega_{L}) \\
B(\omega, \omega_{L}) &= \mathcal{E}_{BB}(\omega-2\omega_{L}) - 4\mathcal{E}_{BB}(\omega-\omega_{L})
\end{align}
$$
