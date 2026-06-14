
# General Form

A direct transition means that initial and final momenta are equal $\mathbf{k}_{u}=\mathbf{k}_{l}\equiv \mathbf{k}$

$$
\epsilon''(\omega) \propto \iiint f(E_{l}(\mathbf{k}))\Big[ 1-f(E_{u}(\mathbf{k})) \Big]\cdot\delta \big( E_{u}(\mathbf{k}) - E_{l}(\mathbf{k}) -\hbar \omega \big) \ d\mathbf{k}
$$
Where 

$$
\begin{align}
E_{u} &=   \hbar\omega_{X_{6}^{-}} + \frac{\hbar^{2}}{2m_{u\perp}}k_{\perp}^{2} + \frac{\hbar^{2}}{2m_{u\parallel}}k_{\parallel}^{2} \\
E_{l} &= -\hbar\omega_{X_{7}^{+}} - \frac{\hbar^{2}}{2m_{l\perp}}k_{\perp}^{2} + \frac{\hbar^{2}}{2m_{l\parallel}}k_{\parallel}^{2}
\end{align}
$$

The approximate cylindrical symmetry of the bands allow us to further reduce the dimensionality of the integral by changing to cylindrical coordinates $d\mathbf{k}\to 2\pi k_{\perp} \ dk_{\perp}dk_{\parallel}$. In what follows we drop the explicit momentum dependence of the dispersion relations for the sake of brevity, but recall that $E_{u}$ and $E_{l}$ 
-> $E_{u}(k_{\perp},k_{\parallel})$ and $E_{l}(k_{\perp},k_{\parallel})$.

$$
\epsilon''(\omega) \propto \iint f\Big( E_{l} \Big)\Big[ 1-f(E_{u}) \Big]\cdot\delta \Big( E_{u} - E_{l} -\hbar \omega \Big) \ 2\pi k_{\perp} \ dk_{\perp}dk_{\parallel}
$$

We define new variables we follows 

$$\begin{align}
E &\to E_{u} &&=\hbar\omega_{X_6^-} + A_u k_\perp^2 - B_u k_\parallel^2 \\
\Delta &\to E_{u} - E_{l}&&=\hbar\omega_{X} + \overline{A}k_\perp^2 + \bar{B} k_\parallel^2
\end{align}$$
With temporary compact notation for clarity

$$\begin{align}
A_u &= \frac{\hbar^2}{2m_{u\perp}}  &&A_l= \frac{\hbar^2}{2m_{l\perp}}  &\overline{A} = A_{u}+A_{l}  \\
B_u &= \frac{\hbar^2}{2m_{u\parallel}}   &&B_l = \frac{\hbar^2}{2m_{l\parallel}} &\overline{B} = B_{l}-B_{u} \\
\end{align}$$
And the energy gap at the X point defined as  $\hbar\omega_{X} = \hbar\omega_{X_{6}^{-}} + \hbar\omega_{X_{7}^{+}}$ 
Under a proper change of variables, the integral becomes

$$\epsilon''(\omega) \propto \iint f(E-\Delta)\Big[ 1-f(E) \Big] \cdot \delta \big( \Delta - \hbar \omega \big) \ \frac{2\pi k_{\perp}}{|\det(J)|}\ dE \ d\Delta$$

And since the integration variables are now explicit with regards to the arguments of the delta function it further simplifies into

$$
\epsilon''(\omega) \propto \int f(E-\hbar\omega)\Big[ 1-f(E) \Big] \mathcal{J}(E)\, dE 
$$

f(E-w)[1-f(E)] = 


# Finding the Jacobian & Integration Limits

$$
\mathcal{D}_{i\to u}(E,\hbar\omega) = (8\pi^{2}\hbar^{2})^{-1}\mathcal{F}_{l\to u} k_{\parallel}^{-1}
$$
and

$$
D = \left( \frac{\hbar^{2}}{2} \right)^{2}\mathcal{F}_{l \to u}^{-2}
$$
But Rosei's integrand is $\mathcal{D}_{i\to u}(E,\hbar\omega)[1-f(E)]$. He presents his results after having contracted the delta function.‘