# Intraband transitions

$$
\boxed{\begin{align}
\Gamma^{T}(\hbar\omega) \propto\;& \iint_{\text{BZ}} 
f^{T}(\mathbf{k}_{1})\big[1-f^{T}(\mathbf{k}_{2})\big]\,
\delta\!\left(\mathcal{E}(\mathbf{k}_{1})-\mathcal{E}(\mathbf{k}_{2})+\hbar\omega\right)\,
d^{3}k_{1}\, d^{3}k_{2} \tag{1}\\ \\
\approx\;& \iint_{0}^{\infty} \,
f^{T}(\mathcal{E}(k_{1}))\big[1-f^{T}(\mathcal{E}(k_{2}))\big]\,
\delta\!\left(\mathcal{E}(k_{1})-\mathcal{E}(k_{2})+\hbar\omega\right)(4\pi k_{1}^{2})(4\pi k_{2}^{2}) \ \,
dk_{1}\, dk_{2} \tag{2}\\ \\ 
=\;& \iint_{0}^{\infty}
f^{T}(\mathcal{E}_{1})\big[1-f^{T}(\mathcal{E}_{2})\big]\,
\rho(\mathcal{E}_{1})\, \rho(\mathcal{E}_{2})\,
\delta\!\left(\mathcal{E}_{1}-\mathcal{E}_{2}+\hbar\omega\right)\,
d\mathcal{E}_{1}\, d\mathcal{E}_{2} \tag{3}\\ \\ 
=\;& \int_{0}^{\infty}
f^{T}(\mathcal{E}+\hbar\omega)\big[1-f^{T}(\mathcal{E})\big]\,
\rho(\mathcal{E}+\hbar\omega)\, \rho(\mathcal{E})\,
d\mathcal{E} \tag{4}\\   \\
\approx\; &\rho^{2}(\mathcal{E}_{F})\int_{0}^{\infty}
f^{T}(\mathcal{E}+\hbar\omega)\big[1-f^{T}(\mathcal{E})\big]\,
\,
d\mathcal{E} \tag{5}\\ \\ 
=\; &\rho^{2}(\mathcal{E}_{F}) \frac{k_BT}{e^{\beta\hbar\omega}-1}\Big[\beta\hbar\omega+\ln\left(1+e^{-\beta\mu}\right)-\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right)\Big]. \tag{6}\\ \\
\approx\;& \rho^{2}(\mathcal{E}_{F})\,\frac{\hbar\omega}{e^{\beta\hbar\omega}-1}\, \tag{7}
\end{align}}
$$
- [ ] add an explanation appendix (in a new A2_derivation_of_analytic_expression.md note in this folder) that details all the steps and assumptions required to reach from $(1)\to(7)$

After we assume that the transition dipole matrix is a constant of $k$, we're left with $(1)$. From there the transition into Yonatan's analytic expression is outlined below

- $(1)\to(2)$ parabolic band **approximation**
- $(2)\to(3)$ k-$\mathcal{E}$ basis transfer
- $(3)\to(4)$ delta resolution
- $(4)\to(5)$ constant eDOS **approximation**
- $(5)\to(6)$ analytic integration
- $(6)\to(7)$ low emission energy / temperature **approximation**

To assess the regimes of validity of this approximation we proceed from the bottom up

| stage                                                                                     | comparison                | purpose                                                  |
| ----------------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------- |
| [1 - Analytic Approximation](1%20-%20Analytic%20Approximation.md)                         | $$(6)\leftrightarrow(7)$$ | establish validity regime of analytic approx             |
| [2 - Numeric Convergence](2%20-%20Numeric%20Convergence.md)                               | $$(5)\leftrightarrow(6)$$ | establish numeric convergence under constant eDOS approx |
| [3 - Constant eDOS Approximation](3%20-%20Constant%20eDOS%20Approximation.md)             | $$(4)\leftrightarrow(5)$$ | establish validity of constant eDOS approx               |
| [4 - Delta (2D) Approximation E-Space](4%20-%20Delta%20(2D)%20Approximation%20E-Space.md) | $$(4)\leftrightarrow(3)$$ | establish validity of delta approx in e-space            |
| [5 - Delta (2D) Approximation K-Space](5%20-%20Delta%20(2D)%20Approximation%20K-Space.md) | $$(4)\leftrightarrow(2)$$ | establish validity of delta approx in k-space 2D         |
| [6 - Delta (4D) Approximation K-Space](6%20-%20Delta%20(4D)%20Approximation%20K-Space.md) | $$(4)\leftrightarrow(1)$$ | establish validity of delta approx in k-space 4D         |

Under the parabolic band approximation, and due to it's central role in our [main reference material](../resources/1%20-%20theory-of-hot-photoluminescence-from-drude-metals.pdf), equation $(4)$ serves as our point of reference during all comparisons. Since in equations $(3)$ and $(4)$ the delta function has to be approximated, its validity must be ascertained in both energy and momentum space. Only then can we use it in equation $(1)$ to calculate the non-parabolic (and more accurate) case and, finally, the interband transition.
