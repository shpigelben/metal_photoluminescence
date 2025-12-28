# Conduction Band

$$\mathcal{E}_{c}(\mathbf{k}) = \mathcal{E}_{0c} + \frac{\hbar^2 k_{\perp}^2}{2m_{c\perp}} - \frac{\hbar^2 k_{\parallel}^2}{2m_{c\parallel}} $$
## General Derivation

$$I(\hbar\omega) \propto \iint_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{c}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{c}(\mathbf{k}_{2}) - \hbar\omega \Big)$$
Unlike the inter-band case, this process is phonon-assisted (or defect-assisted), meaning momentum is **not conserved** ($\mathbf{k}_1 \neq \mathbf{k}_2$). The initial and final states are independent vectors in the Brillouin Zone. This allows us to decouple the six-dimensional integral into a product of two independent densities of states.

Using the following identity
$$
\delta(\mathcal{E}_{1}-\mathcal{E}_{2}-\hbar\omega) = \int\limits \delta(\mathcal{E}-\mathcal{E}_{2}-\hbar\omega)\delta(\mathcal{E}-\mathcal{E}_{1}) d\mathcal{E}
$$
We can separate the integral into two distinct parts in $\mathbf{k}_{1}$ and $\mathbf{k}_{2}$.

$$
\int d\mathcal{E} \left( \int_{\text{BZ}} f(\mathcal{E}_1) \delta(\mathcal{E}_1 - \mathcal{E}) d^3k_1 \right) \left( \int_{\text{BZ}} [1-f(\mathcal{E}_2)] \delta(\mathcal{E}_2 - (\mathcal{E}-\hbar\omega)) d^3k_2 \right)
$$