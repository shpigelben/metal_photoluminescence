# Conduction Band

$$\mathcal{E}_{c}(\mathbf{k}) = \mathcal{E}_{0c} + \frac{\hbar^2 k_{\perp}^2}{2m_{c\perp}} - \frac{\hbar^2 k_{\parallel}^2}{2m_{c\parallel}} $$
## General Derivation

$$I(\hbar\omega) \propto \iint_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{c}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{c}(\mathbf{k}_{2}) - \hbar\omega \Big)$$
Unlike the inter-band case, this process is phonon-assisted (or defect-assisted), meaning momentum is **not conserved** ($\mathbf{k}_1 \neq \mathbf{k}_2$). The initial and final states are independent vectors in the Brillouin Zone. This allows us to decouple the six-dimensional integral into a product of two independent densities of states.

Using the following identity
$$
\delta(\mathcal{E}_{1}-\mathcal{E}_{2}-\hbar\omega) = \int\limits \delta(\mathcal{E}-\mathcal{E}_{2}-\hbar\omega)\delta(\mathcal{E}-\mathcal{E}_{1}) d\mathcal{E}
$$
this enables us to separate the integral into two distinct parts in $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$.
$$
\int d\mathcal{E} \left( \int_{\text{BZ}} f(\mathcal{E}_1) \delta(\mathcal{E}_1 - \mathcal{E}) d^3k_1 \right) \left( \int_{\text{BZ}} \Big[1-f(\mathcal{E}_2)\Big] \delta(\mathcal{E} - \mathcal{E}_{2}-\hbar\omega) d^3k_2 \right)
$$

$$
d^{3}k_{1}\to d\mathcal{E}_{1}d\mathcal{E} \quad\quad d^{3}k_{1}\to d\mathcal{E}_{2}d\Delta
$$

now the electronic occupation factors can be taken out of the integral


$$
\int d\mathcal{E}  \;  f(\mathcal{E}) \Big[1-f(\mathcal{E}-\hbar \omega)\Big] \left( \int_{\text{BZ}}\delta\big(\mathcal{E}_1(\mathbf{k}_{1}) - \mathcal{E}\big) d^3k_1 \right) \left( \int_{\text{BZ}} \delta(\mathcal{E}_{2}(\mathbf{k}) - \mathcal{E} +\hbar\omega) d^3k_2 \right)
$$


## 2. Detailed Derivation of Saddle Point DOS

We now calculate $\rho(\mathcal{E})$ for a single saddle-point valley, incorporating the **finite validity range** of the approximation.

### A. Coordinate Transformation

We define the energy-unit variables to normalize the effective masses
$$\begin{align} x &= \frac{\hbar^2 k_{\perp}^2}{2m_{c\perp}} &&\implies dx = \frac{\hbar^2}{m_{c\perp}} k_{\perp} dk_{\perp} \\ y &= \frac{\hbar^2 k_{\parallel}^2}{2m_{c\parallel}} &&\implies \frac{dy}{\sqrt{y}} = \sqrt{\frac{2\hbar^2}{m_{c\parallel}}} dk_{\parallel} \end{align}$$

Using cylindrical symmetry ($2\pi k_{\perp} dk_{\perp}$) and summing $\pm k_{\parallel}$ (factor of 2)

$$d^3k = 2\pi k_{\perp} dk_{\perp} (2 dk_{\parallel}) = \underbrace{ \frac{2\pi  m_{c\perp} \sqrt{2m_{c\parallel}}}{\hbar^3} }_{\mathcal{C}_{geo}} \frac{dx dy}{\sqrt{y}}$$



$$\mathcal{E}_{c}(x,y) = \mathcal{E}_{0c} + x - y$$