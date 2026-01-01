$$I(\hbar\omega) \propto \iint\limits_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{c}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{c}(\mathbf{k}_{2}) - \hbar\omega \Big)$$

$$I(\hbar\omega) \propto \iint\limits_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}) \Big[1-f(\mathcal{E}-\Delta)\Big] \; \delta\Big(\Delta - \hbar\omega \Big)$$
Now we need to find the proper transformation $d^{3}k_{1}d^{3}k_{2}\to\mathcal{J}d\mathcal{E}d\Delta$ and the proper integration limits.
### First COV (Cylindrical Symmetry)
Using the rotational symmetry of the saddle point near X
$$d^3k \to 2\pi k_{\perp} dk_{\perp} dk_{\parallel}$$
### Second COV (Linearization)
We introduce variables $x$ and $y$ to linearize the energy expression
$$\begin{align} x &= k_{\perp}^{2} &&\implies dx = 2k_{\perp}dk_{\perp} \\ y &= k_{\parallel}^{2} &&\implies \frac{1}{2}\frac{dy}{\sqrt{ y }} = dk_{\parallel} \end{align}$$
Accounting for the symmetry of $k_{\parallel}$ (integrating from $-\infty$ to $\infty$ is equivalent to $2 \times$ integrating $0$ to $\infty$), the volume element becomes
$$d^3k \to \pi \frac{dx dy}{\sqrt{y}}$$
### Third COV (Energy basis)
We introduce variables $\mathcal{E}$ and $\Delta$ for which the delta is explicit.
$$
\begin{align}
\mathcal{E}_{1}(x,y)&=\mathcal{E}_{0c} + Ax_{1}-By_{1} &&\equiv \mathcal{E} \\
\mathcal{E}_{1}(x,y)-\mathcal{E}_{2}(x,y)&= A(x_{1}-x_{2})+B(y_{2}-y_{1})&&\equiv\Delta
\end{align}
$$

$$
|\mathcal{J}|= \left|\frac{\partial(x_1, y_1, x_2, y_2)}{\partial(E, \Delta, y_1, y_2)}\right| =  \left| \left(\frac{1}{A}\right) \left(-\frac{1}{A}\right) \right| = \frac{1}{A^2}
$$

$$
d^{3}k_{1}d^{3}k_{2}\to \pi^{2} \frac{dx_{1}dy_{1}}{\sqrt{ y_{1} }}\frac{dx_{2}dy_{2}}{\sqrt{ y_{2} }} \to \frac{\pi^{2}}{A^{2}}d\mathcal{E}d\Delta  \frac{dy_{1}dy_{2}}{\sqrt{ y_{1}y_{2} }}
$$
### Putting it All Together

$$\begin{align}
I(\hbar\omega) &\propto \iint\limits_{\text{BZ}} d^{3}k_{1} d^{3}k_{2} \; f(\mathcal{E}) \Big[1-f(\mathcal{E}-\Delta)\Big] \; \delta\Big(\Delta - \hbar\omega \Big) \\
&= \iint\limits_{}^{}  \, \frac{\pi^{2}}{A^{2}}d\mathcal{E}d\Delta   f(\mathcal{E}) \Big[1-f(\mathcal{E}-\Delta)\Big] \; \delta\Big(\Delta - \hbar\omega \Big) \iint\limits_{y_{min}(\Delta)}^{y_{max}}    \frac{dy_{1}dy_{2}}{\sqrt{ y_{1}y_{2} }}  \\
&=\left( \frac{2\pi}{A} \right) \iint\limits_{-\infty}^{\infty}d\mathcal{E}d\Delta   f(\mathcal{E}) \Big[1-f(\mathcal{E}-\Delta)\Big] \; \delta\Big(\Delta - \hbar\omega \Big)\times \\
&\times \Big[ \sqrt{ y_{max}}-\sqrt{ y_{min} } \Big]
\end{align}$$