# Conduction Band
The conduction band as given by [5 - Rosei](../../../resources/5%20-%20Rosei.pdf) is as follows

$$
\mathcal{E}_{c}(\mathbf{k}) = \mathcal{E}_{0c} + \frac{\hbar^2 k_{\perp}^2}{2m_{c\perp}} - \frac{\hbar^2 k_{\parallel}^2}{2m_{c\parallel}} 
$$
For intraband transitions it is natural too set $\mathcal{E}_{0c}=0$, and reassign the quadratic coefficients which leaves us with the following dispersion relation

$$
\mathcal{E}_{c}(\mathbf{k}) = Ak_{\perp}^{2} -  Bk_{\parallel}^{2} 
$$
## General Derivation

$$I(\hbar\omega) \propto \iint_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{c}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{c}(\mathbf{k}_{2}) - \hbar\omega \Big)$$
Unlike the inter-band case, this process is phonon-assisted (or defect-assisted), meaning momentum is **not conserved** ($\mathbf{k}_1 \neq \mathbf{k}_2$) even approximately. We assume that whatever momentum is missing for an energetic transition to occur is readily available through various mediators (as mentioned above). The initial and final states are independent vectors in the Brillouin Zone. This allows us to decouple the six-dimensional integral into a product of two independent densities of states. By using the following
$$
\delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{c}(\mathbf{k}_{2}) - \hbar\omega \Big) = \iint\limits \delta(\mathcal{E}_1 - \mathcal{E}_c(\mathbf{k}_1)) \times \delta(\mathcal{E}_2 - \mathcal{E}_c(\mathbf{k}_2))  \times \delta(\mathcal{E}_1 - \mathcal{E}_2 - \hbar\omega) \; d\mathcal{E}_{1}d\mathcal{E}_{2}
$$
We can write
$$\begin{align} I(\hbar\omega) \propto \int\limits_{-\infty}^{\infty} d\mathcal{E}_1 d\mathcal{E}_2 \;& f(\mathcal{E}_1) \Big[1-f(\mathcal{E}_2)\Big] \; \delta(\mathcal{E}_1 - \mathcal{E}_2 - \hbar\omega) \\ &\times \underbrace{\left( \int\limits_{\text{BZ}} d^3k_1 \; \delta(\mathcal{E}_1 - \mathcal{E}_c(\mathbf{k}_1)) \right)}_{\rho_c(\mathcal{E}_1)} \underbrace{\left( \int\limits_{\text{BZ}} d^3k_2 \; \delta(\mathcal{E}_2 - \mathcal{E}_c(\mathbf{k}_2)) \right)}_{\rho_c(\mathcal{E}_2)} \end{align}$$
and we retrieve the familiar 1D expression for emission
$$
I(\hbar\omega)\propto \int\limits_{-\infty}^{\infty} f(\mathcal{E})\Big[ 1-f(\mathcal{E-\hbar\omega}) \Big] \rho_{c}(\mathcal{E})\rho_{c}(\mathcal{E}-\hbar\omega)\,\, d\mathcal{E}
$$
The challenge here is to properly find a closed expression for the electronic density of states (eDOS).
# Finding the Conduction Band eDOS
First COV (Cylindrical Symmetry) - Using the rotational symmetry of the saddle point near X
$$d^3k \to 2\pi k_{\perp} dk_{\perp} dk_{\parallel}$$
Second COV (Linearization) - We introduce variables $u$ and $v$ to linearize the energy expression
$$\begin{align} u &= Ak_{\perp}^{2} &&\implies \frac{du}{A} = 2k_{\perp}dk_{\perp} \\ v &= Bk_{\parallel}^{2} &&\implies \frac{1}{2\sqrt{ B }}\frac{dv}{\sqrt{ v }} = dk_{\parallel} \end{align}$$

Accounting for the symmetry of $k_{\parallel}$ (integrating from $-\infty$ to $\infty$ is equivalent to $2 \times$ integrating $0$ to $\infty$), the volume element becomes
$$d^3k \to \frac{\pi}{A\sqrt{ B }} \frac{du dv}{\sqrt{v}}$$

Next, we find the proper integration limits on $u$

$$
\begin{align}
0\leq k_{\parallel}\leq k_{max} &\implies 0\leq v\leq \underbrace{ Bk_{max}^{2} }_{ \mathcal{E_{\parallel}^{max}} }\\
0\leq k_{\perp}\leq k_{max} &\implies \underbrace{ \max\Big[0,\mathcal{E}_{j}\Big] }_{ \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}}) }\leq u \leq \underbrace{ Ak_{max}^{2} }_{ \mathcal{E_{\perp}^{max}} }
\end{align}
$$

> [!NOTE]- $\mathbf{(b)\to(c)}$ transition
> The delta function forces its argument to vanish$$
\begin{align}
\mathcal{E}_{j}-\mathcal{E}_{c}(u,v) &\stackrel{!}{=} 0 \\
\mathcal{E}_{j} -u + v&\stackrel{!}{=} 0 \\
v - (u-\mathcal{E}_{j})&\stackrel{!}{=} 0
\end{align}$$
The subscript $j=1, 2$ refers to the initial and final state energies. All three equations serve as equivalent arguments for the delta function. To eliminate the $v$ component we chose the last.

Let us apply the COV to the density of states
$$
\begin{align}
\rho(\mathcal{E}_{j}) &= \int\limits_{\text{BZ}}  \; \delta \Big( \mathcal{E}_{j}-\mathcal{E}_{c}(\mathbf{k}) \Big)\, d^{3}k \tag{a}\\
&= \frac{\pi}{A\sqrt{ B }}\int\limits_{ \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}})}^{\mathcal{E}_{\perp}^{max}}\int\limits_{0}^{\mathcal{E_{\parallel}^{max}}} \, \delta \Big[ \mathcal{E}_{j}-\mathcal{E}_{c}(u,v) \Big] \; \frac{dudv}{\sqrt{ v }} \tag{b}\\
&=\frac{\pi}{A\sqrt{ B }}\int\limits_{ \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}})}^{\mathcal{E}_{\perp}^{max}}\int\limits_{0}^{\mathcal{E_{\parallel}^{max}}} \,  \delta \Big[ v - (u-\mathcal{E}_{j}) \Big]\; \frac{dudv}{\sqrt{ v }} \tag{c} \\
&= \frac{\pi}{A\sqrt{ B }}\int\limits_{ \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}})}^{\mathcal{E_{\perp}^{max}}} \frac{du}{\sqrt{ u - \mathcal{E}_{j} }} \tag{d}
\end{align}
$$


> [!NOTE]- Integration Limits
> 
First, lets us express $v$ in terms of $u$ $$v_{j}(u) = u-\mathcal{E}_{j}$$we apply both integration limits brought from $k_{\perp}$ and $k_{\parallel}$ $$
\begin{align} 
k_{\perp}^{2}\geq0 &\implies u\geq 0  && \\ k_{\parallel}^{2}\geq0 &\implies v(u)\geq 0 
\end{align}$$ we apply both conditions to $u$ $$u\geq \mathcal{E}_{j} \quad u\geq 0$$ This provides a lower limit on the $u$ integration, and we choose the the upper lower bound, namely $$u_{min}(\mathcal{E}_{j}) = \max \left[ 0, \mathcal{E}_{j} \right]$$

$$
\begin{align}
\rho(\mathcal{E}_{j})&=\frac{\pi}{A\sqrt{ B }}\int \limits_{ \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}})}^{\mathcal{E_{\perp}^{max}}}\frac{du}{\sqrt{ u - \mathcal{E}_{j} }}  \\
 & =\frac{2\pi}{A\sqrt{ B }} \Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E_{j}} } -\sqrt{  \mathcal{E_{\perp}^{min}}(\mathcal{E_{j}})-\mathcal{E}_{j} }\  \Bigg] \\
& =\frac{2\pi}{A\sqrt{ B }} \Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E_{j}} } -\sqrt{  \max(0,\mathcal{E}_{j})-\mathcal{E}_{j} }\  \Bigg]
\end{align}
$$

### Putting it All Together
$$\begin{align} I(\hbar\omega) \propto \iint\limits_{-\infty}^{\infty} d\mathcal{E}_1 d\mathcal{E}_2 \;& f(\mathcal{E}_1) \Big[1-f(\mathcal{E}_2)\Big] \; \delta(\mathcal{E}_1 - \mathcal{E}_2 - \hbar\omega) \times \\ &\times \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E}_{1} } - \sqrt{ \max\big[0,\mathcal{E}_{1}\big]-\mathcal{E}_{1} } \Bigg] \\
&\times \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E}_{2} } - \sqrt{ \max\big[0,\mathcal{E}_{2}\big]-\mathcal{E}_{2} } \Bigg]\end{align}$$
After resolving the delta function for $\mathcal{E}_{2}$, and setting $\mathcal{E}_{1}\equiv\mathcal{E}$, we're left with
$$\boxed{\begin{align} \\  \quad  I(\hbar\omega) \propto \left( \frac{2\pi}{A\sqrt{ B }} \right)^{2} \int\limits_{-\infty}^{\infty} d\mathcal{E} \;& f(\mathcal{E}) \Big[1-f(\mathcal{E}- \hbar\omega)\Big] \; \times \\ &\times \Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E} } - \sqrt{ \max\big[0,\mathcal{E}\big]-\mathcal{E} } \Bigg] \\
&\times \Bigg[ \sqrt{ \mathcal{E}_{\perp}^{max}-\mathcal{E} +\hbar\omega } - \sqrt{ \max\big[0,\mathcal{E}-\hbar\omega\big]-\mathcal{E} +\hbar\omega } \Bigg] \quad\\  \\ \end{align}}$$
