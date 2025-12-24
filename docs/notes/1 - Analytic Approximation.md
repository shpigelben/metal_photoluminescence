# Stage 1 — Analytic approximation: Eq. (7) vs Eq. (6)

$$
\begin{align}
I^{T}(\hbar\omega) = \; & \rho^{2}(\mathcal{E}_{F}) \frac{1}{e^{\beta\hbar\omega}-1}\left[\hbar\omega+ \frac{1}{\beta}\ln\left(1+e^{-\beta\mu}\right)-\frac{1}{\beta}\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right)\right] \tag{6}\\ \\
I^{T}(\hbar\omega)\;=& \; \rho^{2}(\mathcal{E}_{F})\,\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\, \tag{7}
\end{align}
$$

In Eq. (6) we obtained a closed-form expression for the constant-eDOS integral, and in Eq. (7) we introduced an additional approximation. To assess how agreeable the two functions are we calculate their relative error as a function of emission energy $\hbar\omega$ and temperature $T$.

$$
\delta_{\mathrm{rel}}(\hbar\omega,T)
=\left|\frac{I_{(7)}(\hbar\omega,T)-I_{(6)}(\hbar\omega,T)}{I_{(6)}(\hbar\omega,T)}\right| \tag{8}
$$

where $I_{(6)}$ and $I_{(7)}$ denote expressions (6) and (7), respectively. Below is the plot of $(8)$ 


![center](../figures/stage_1_analytic_approx_rel_error.png)

Figure 1.1: Heat map of $\log_{10}|\delta_{\mathrm{rel}}^{(1)}|$ for Eq. (7) relative to Eq. (6), evaluated at $\mathcal{E}_F=3\,\mathrm{eV}$. The vertical axis is plotted in $k_B T$ (with a secondary axis in $T$) to make the controlling dimensionless ratios explicit.

$$
\begin{align}
&\ln\left(1+e^{\beta(\hbar\omega - \mu)}\right)&\approx 0 \\ &\iff e^{\beta(\hbar\omega - \mu)} &\approx 0  \\
&\iff \beta(\hbar\omega-\mu)&\ll0 \\
&\iff \beta(\hbar\omega-\mu)&\ll-1  \\
&\iff \hbar\omega(T) &\ll \mu-k_{\small B}T \\
\end{align}
$$



## Results and discussion
If one is concerned with low electron temperatures and emission energies $\hbar\omega < \mathcal{E}_{F}$ the approximation. Still, it is not clear why on

==perhaps one of the main takeaways is not computing the ratio between two exact expressions, especially when they're nearly vanishing this leads to NaNs==
___
The reduction of Eq. (6) to Eq. (7) corresponds to neglecting the two $\mu$-dependent logarithmic terms in the bracket of Eq. (6). In the degenerate limit $\beta\mu\gg 1$ and for $\mu>\hbar\omega$, these terms scale as
$$
\ln\!\left(1+e^{-\beta\mu}\right)\sim e^{-\beta\mu},
\qquad
\ln\!\left(1+e^{\beta(\hbar\omega-\mu)}\right)\sim e^{-\beta(\mu-\hbar\omega)},
$$
so the approximation is controlled by the two parameters $\beta\mu$ and $\beta(\mu-\hbar\omega)$.
Two qualitative conclusions follow and are consistent with Figure 1.1:

- For fixed $\mathcal{E}_F$, the approximation improves rapidly as $T$ is lowered (increasing $\beta\mu$), and remains accurate as long as $\hbar\omega$ stays sufficiently below $\mu$.
- The approximation breaks down as $\hbar\omega\to\mu$ from below, where the second logarithm becomes order unity and cannot be dropped.

In the remainder of the pipeline we will use Eq. (6) as the “exact” constant-eDOS reference. The next stage therefore establishes that the numerical evaluation of Eq. (5) converges to Eq. (6) for a practical (and not overly conservative) choice of integration step $\Delta\mathcal{E}$.
