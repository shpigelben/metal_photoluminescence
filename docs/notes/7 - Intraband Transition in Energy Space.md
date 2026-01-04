# Conduction Band
The conduction band as given by [5 - Rosei](../resources/5%20-%20Rosei.pdf) is as follows

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
Second COV (Linearization) - We introduce variables $x$ and $y$ to linearize the energy expression
$$\begin{align} x &= Ak_{\perp}^{2} &&\implies \frac{dx}{A} = 2k_{\perp}dk_{\perp} \\ y &= Bk_{\parallel}^{2} &&\implies \frac{1}{2\sqrt{ B }}\frac{dy}{\sqrt{ y }} = dk_{\parallel} \end{align}$$

Accounting for the symmetry of $k_{\parallel}$ (integrating from $-\infty$ to $\infty$ is equivalent to $2 \times$ integrating $0$ to $\infty$), the volume element becomes
$$d^3k \to \frac{\pi}{A\sqrt{ B }} \frac{dx dy}{\sqrt{y}}$$

Next, we find the proper integration limits on $x$
$$
\begin{align}
0\leq k_{\parallel}\leq k_{max} &\implies 0\leq y\leq Ak_{max}^{2}\equiv \mathcal{E_{\perp}^{max}}\\
0\leq k_{\perp}\leq k_{max} &\implies \mathcal{E}_{j}\leq x_{j} \leq Bk_{max}^{2}\equiv \mathcal{E_{\parallel}^{max}}
\end{align}
$$

> [!NOTE]- $\mathbf{(b)\to(c)}$ transition
> The delta function forces its argument to vanish$$
\begin{align}
\mathcal{E}_{j}-\mathcal{E}_{c}(x,y) &\stackrel{!}{=} 0 \\
\mathcal{E}_{j} -x + y&\stackrel{!}{=} 0 \\
y - (x-\mathcal{E}_{j})&\stackrel{!}{=} 0
\end{align}$$
The subscript $j=1, 2$ refers to the initial and final state energies. All three equations serve as equivalent arguments for the delta function. To eliminate the $y$ component we chose the last.

Let us apply the COV to the density of states
$$
\begin{align}
\rho(\mathcal{E}_{j}) &= \int\limits_{\text{BZ}}  \; \delta \Big( \mathcal{E}_{j}-\mathcal{E}_{c}(\mathbf{k}) \Big)\, d^{3}k \tag{a}\\
&= \frac{\pi}{A\sqrt{ B }}\int\limits_{\mathcal{E_{j}}}^{\mathcal{E}_{\perp}^{max}}\int\limits_{0}^{\mathcal{E_{\parallel}^{max}}} \, \delta \Big[ \mathcal{E}_{j}-\mathcal{E}_{c}(x,y) \Big] \; \frac{dxdy}{\sqrt{ y }} \tag{b}\\
&=\frac{\pi}{A\sqrt{ B }}\int\limits_{\mathcal{E_{j}}}^{\mathcal{E}_{\perp}^{max}}\int\limits_{0}^{\mathcal{E_{\parallel}^{max}}} \,  \delta \Big[ y - (x-\mathcal{E}_{j}) \Big]\; \frac{dxdy}{\sqrt{ y }} \tag{c} \\
&= \frac{\pi}{A\sqrt{ B }}\int\limits_{\mathcal{E}_{j}}^{\mathcal{E_{\perp}^{max}}} \frac{dx}{\sqrt{ x - \mathcal{E}_{j} }} \tag{d}
\end{align}
$$


> [!NOTE]- Integration Limits
> 
First, lets us express $y$ in terms of $x$ $$y_{j}(x) = \frac{1}{B}\Big[ Ax - \mathcal{E}_{j} \Big]$$we apply both integration limits brought from $k_{\perp}$ and $k_{\parallel}$ $$
\begin{align} 
k_{\perp}^{2}\geq0 &\implies x\geq 0  && \\ k_{\parallel}^{2}\geq0 &\implies y(x)\geq 0 
\end{align}$$ we apply both conditions to $x(y)$ $$x\geq \frac{\Delta}{A} \quad x\geq 0$$ This provides a lower limit on the $x$ integration, and we choose the the upper lower bound, namely $$x_{min}(\Delta) = \max \left[ 0, \frac{\Delta}{A} \right] = \frac{1}{A}\max[0,\Delta]$$


$$
\rho(\mathcal{E}_{j})=\frac{\pi}{A\sqrt{ B }}\int \limits_{\mathcal{E}_{j}}^{\mathcal{E_{\perp}^{max}}}\frac{dx}{\sqrt{ x - \mathcal{E}_{j} }} 
$$
where $x_{max}$ is determined by the range of validity of the quadratic band approximation.

$$
\begin{align}
\rho(\mathcal{E}_{j}) &= \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ Ax_{max}-\Delta_{j} } - \sqrt{ Ax_{min}(\Delta_{j})-\Delta_{j} } \Bigg] \\
&= \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ Ax_{max}-\Delta_{j} } - \sqrt{ \max\big[0,\Delta_{j}\big]-\Delta_{j} } \Bigg]
\end{align}
$$
### Offset COV
This change of variables is merely for the sake of convenience

$$
\begin{cases}
\Delta_{1}&=\mathcal{E}_{1}-\mathcal{E}_{0}  &&d\Delta_{1}=d\mathcal{E}_{1}\\
\Delta_{2}&=\mathcal{E}_{2}-\mathcal{E}_{0} && d\Delta_{2}=d\mathcal{E}_{2}
\end{cases}
$$
This makes the integral a little simpler

$$\begin{align} I(\hbar\omega) \propto \iint\limits_{-\infty}^{\infty} d\Delta_1 d\Delta_2 \;& f(\Delta_1) \Big[1-f(\Delta_2)\Big] \; \delta(\Delta_1 - \Delta_2 - \hbar\omega) \times \\ &\times \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ Ax_{max}-\Delta_{1} } - \sqrt{ \max\big[0,\Delta_{1}\big]-\Delta_{1} } \Bigg] \\
&\times \frac{2\pi}{A\sqrt{ B }}\Bigg[ \sqrt{ Ax_{max}-\Delta_{2} } - \sqrt{ \max\big[0,\Delta_{2}\big]-\Delta_{2} } \Bigg]\end{align}$$
After resolving the delta function for $\Delta_{2}$, and setting $\Delta_{1}\equiv\Delta$, we're left with
$$\boxed{\begin{align} \\  \quad  I(\hbar\omega) \propto \left( \frac{2\pi}{A\sqrt{ B }} \right)^{2} \int\limits_{-\infty}^{\infty} d\Delta \;& f(\Delta) \Big[1-f(\Delta- \hbar\omega)\Big] \; \times \\ &\times \Bigg[ \sqrt{ Ax_{max}-\Delta } - \sqrt{ \max\big[0,\Delta\big]-\Delta } \Bigg] \\
&\times \Bigg[ \sqrt{ Ax_{max}-\Delta +\hbar\omega } - \sqrt{ \max\big[0,\Delta-\hbar\omega\big]-\Delta +\hbar\omega } \Bigg] \quad\\  \\ \end{align}}$$