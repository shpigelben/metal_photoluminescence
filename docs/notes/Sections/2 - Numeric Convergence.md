
$$
\boxed{\begin{align}
&\rho^{2}(\mathcal{E}_{F})\int_{0}^{\infty}
f^{T}(\mathcal{E}+\hbar\omega)\big[1-f^{T}(\mathcal{E})\big]\,
\,
d\mathcal{E} \tag{5}\\ \\ 
\; &\rho^{2}(\mathcal{E}_{F}) \frac{k_BT}{e^{\beta\hbar\omega}-1}\Big[\beta\hbar\omega+\ln\left(1+e^{-\beta\mu}\right)-\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right)\Big] \tag{6}
\end{align}}
$$

This comparison is between equivalent (rather than approximate) expressions and it serves as a good testing ground for numerical convergence as we expect to be able to reach near machine accuracy.

# Integration Scheme
Unsurprisingly, for the same integration interval and step size, Simpson integration is much more reliable. I have also tested a quadrature which resulted in a very unstable result.

![stage_2_rel_error_grid](../../figures/stage_2_rel_error_grid.png)

Figure 2.2: Point-wise error $\delta_{\mathrm{rel}}^{(2)}(\hbar\omega)$ evaluated on the default energy grid, for the same set of $(T,\mathcal{E}_F)$ cases used in the convergence scan.

Two things are equivalent between the two integration schemes
- a cone of higher relative error emerges from the Fermi energy and spreads with the increase of temperature.
- There is a triangular region which is consistently

![center](../../figures/stage_2_step_convergence_T300K.png)

Step size for machine accuracy is 1e-4

![center](../../figures/stage_2_length_convergence_T300K.png)

relative error settles rapidly around 5.8 eV as an upper integration limit for some reason. 

![center](../../figures/stage_2_rel_error_grid_50x50.png)

Ultimately we manage to converge to the analytic solution, and establish an integration scheme.

## Log-stable thermal factor
The factor $f^{T}(\mathcal{E}+\hbar\omega)[1-f^{T}(\mathcal{E})]$ is evaluated in log form to avoid overflow/underflow. Let
$$
a=\beta(\mathcal{E}-\mu),\qquad b=a+\beta\hbar\omega.
$$
Then
$$
f^{T}(\mathcal{E}+\hbar\omega)\,[1-f^{T}(\mathcal{E})]
=\frac{e^{a}}{(1+e^{a})(1+e^{b})},
$$
and therefore
$$
\log\!\Big(f^{T}(\mathcal{E}+\hbar\omega)\,[1-f^{T}(\mathcal{E})]\Big)
=a-\log(1+e^{a})-\log(1+e^{b}).
\tag{S2.2}
$$
In code, $\log(1+e^x)$ is computed as $\mathrm{logaddexp}(0,x)$, and the exponentiation is performed once at the end.
## Results and discussion
The numerical convergence of the integration scheme is summarized in the figures above. 

**Step Size Convergence:** The step convergence plot demonstrates that refining the grid size $\Delta\mathcal{E}$ leads to a rapid exponential reduction in error. A step size of $\Delta\mathcal{E} \approx 10^{-4}$ eV is sufficient to reach the noise floor, where the error becomes dominated by floating-point precision rather than discretization.

**Integration Range:** The length convergence analysis indicates that the integral value saturates quickly as the upper integration limit is increased. An upper limit of approximately $5.8$ eV relative to the Fermi level is found to be sufficient; extending the range further yields diminishing returns due to the exponential decay of the thermal occupation factors.

**Error Distribution:** Figure 2.2 maps the relative error across the $(T, \hbar\omega)$ plane. A distinct "cone" of higher relative error is observed expanding from the Fermi energy with increasing temperature. This behavior is expected because at large photon energies ($\hbar\omega \gg k_B T$), the transition rates are exponentially suppressed. In these regions, the relative error calculation involves dividing by a near-zero reference value, making it highly sensitive to machine epsilon and finite truncation effects. However, in the physically significant spectral region (high signal), the scheme maintains excellent accuracy.

With a numerically stable and demonstrably converged treatment of Eq. (5) in hand, we have established robust integration parameters ($d\mathcal{E}=10^{-4}$ eV, range limit $\approx 5.8$ eV). We now turn to the *physics approximation* itself: replacing $\rho(\mathcal{E}+\hbar\omega)\rho(\mathcal{E})$ by $\rho^2(\mathcal{E}_F)$ in Eq. (4). This is the focus of Stage 3.


