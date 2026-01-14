# Phase 1 - Recreation of Previous Results & Assessment of the Validity of Approximations
All analytic expressions rely on the constant eDOS approximation. We begin by comparing the numeric integrals to their analytic counterparts (thermal and non-thermal). Since numeric calculations appear to eventually be unavoidable, a simpler, more logical approach, would be to assess the validity of the constant eDOS approximation. If the constant eDOS approximation would prove invalid it would establish the analytic approximations irrelevant, or at least inaccurate, and save a couple of comparisons. But since we follow Yonatan's work [], and for the sake of completeness we choose to follow this path. First though,  we begin by establishing numeric convergence. Since the constant eDOS integral has an exact analytic solution, we can find the parameters that achieve machine precision.

$$
\begin{align}
I^{T}_{analytic \ exact}(\hbar \omega) &=\; \rho^{2}(\mathcal{E}_{F}) \frac{k_BT}{e^{\beta\hbar\omega}-1}\Big[\beta\hbar\omega+\ln\left(1+e^{-\beta\mu}\right)-\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right)\Big] \tag{\#} \\
I^{T}_{analytic \ approx}(\hbar \omega) &= \rho^{2}(\mathcal{E}_{F})\,\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\, \tag{AT} \\
I^{S}_{analytic \ approx}(\hbar \omega) &= ?       \tag{AS}  \\
I^{T}_{numeric \ const \ eDOS}(\hbar \omega) &=\rho^{2}(\mathcal{E}_{F})\int_{0}^{\infty}
f^{T}(\mathcal{E}+\hbar\omega)\big[1-f^{T}(\mathcal{E})\big]\,\, \tag{NT}
d\mathcal{E}  \\
I^{S}_{numeric \ const \ eDOS}(\hbar \omega)&=\rho^{2}(\mathcal{E}_{F})\int_{0}^{\infty}
f^{S}(\mathcal{E}+\hbar\omega)\big[1-f^{S}(\mathcal{E})\big]\,\,
d\mathcal{E} \tag{NS} \\
I^{T}(\hbar \omega) &= \int_{0}^{\infty}
f^{T}(\mathcal{E}+\hbar\omega)\big[1-f^{T}(\mathcal{E})\big]\,
\rho(\mathcal{E}+\hbar\omega)\, \rho(\mathcal{E})\, \tag{T}
d\mathcal{E} \\
I^{S}(\hbar \omega) &= \int_{0}^{\infty}
f^{S}(\mathcal{E}+\hbar\omega)\big[1-f^{S}(\mathcal{E})\big]\,
\rho(\mathcal{E}+\hbar\omega)\, \rho(\mathcal{E})\, \tag{S}
d\mathcal{E}
\end{align}
$$

Here A-analytic, N-numeric, T-thermal, S-steady-state (and later P-pulsed).

$$
\begin{align}
I^{\mathrm{eq}}_{6}(\hbar\omega,T) &= \rho^2(\mathcal{E}_F)\frac{k_BT}{e^{\beta\hbar\omega}-1}\Big[\beta\hbar\omega+\ln(1+e^{-\beta\mu})-\ln(1+e^{\beta(\hbar\omega-\mu)})\Big] \\
I^{\mathrm{eq}}_{7}(\hbar\omega,T) &= \rho^2(\mathcal{E}_F)\frac{\hbar\omega}{e^{\beta\hbar\omega}-1} \\
I^{\mathrm{eq}}_{5}(\hbar\omega,T) &= \rho^2(\mathcal{E}_F)\int_0^\infty f^{\mathrm{eq}}(\mathcal{E}+\hbar\omega)\big[1-f^{\mathrm{eq}}(\mathcal{E})\big]\,d\mathcal{E} \\
I^{\mathrm{neq}}_{5}(\hbar\omega,T) &= \rho^2(\mathcal{E}_F)\int_0^\infty f^{\mathrm{neq}}(\mathcal{E}+\hbar\omega)\big[1-f^{\mathrm{neq}}(\mathcal{E})\big]\,d\mathcal{E} \\
I^{\mathrm{eq}}_{4}(\hbar\omega,T) &= \int_0^\infty f^{\mathrm{eq}}(\mathcal{E}+\hbar\omega)\big[1-f^{\mathrm{eq}}(\mathcal{E})\big]\rho(\mathcal{E}+\hbar\omega)\rho(\mathcal{E})\,d\mathcal{E} \\
I^{\mathrm{neq}}_{4}(\hbar\omega,T) &= \int_0^\infty f^{\mathrm{neq}}(\mathcal{E}+\hbar\omega)\big[1-f^{\mathrm{neq}}(\mathcal{E})\big]\rho(\mathcal{E}+\hbar\omega)\rho(\mathcal{E})\,d\mathcal{E}
\end{align}

$$





