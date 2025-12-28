
$$
\mathcal{E}_{b}(\mathbf{k})  = \begin{cases}
-\mathcal{E}_{0v} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{V \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{V \parallel}} &&\implies\mathcal{E}_{0 v}-\alpha_{v}k_{\perp}^{2}-\beta_{v}k_{\parallel}^{2}  &&&(\mathcal{E<\mathcal{E_{0v}}})\\ \\
 \ \ \ \mathcal{E}_{0 c} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{C \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{C \parallel}} && \implies\mathcal{E}_{0 c}+\alpha_{c}k_{\perp}^{2}-\beta_{c}k_{\parallel}^{2} &&&(\mathcal{E>\mathcal{E_{0c}}})
\end{cases} 
 $$

General form 
$$
\begin{align}
\mathcal{E}_{1}(\mathbf{k}) &= \mathcal{E_{0}}+\alpha_{1} k_{x}^{2} + \beta_{1} k_{y}^{2}+\gamma_{1} k_{z}^{2} \\
\mathcal{E}_{2}(\mathbf{k}) &= \mathcal{E_{0}}+\alpha_{2} k_{x}^{2} + \beta_{2} k_{y}^{2}+\gamma_{2} k_{z}^{2}
\end{align}
$$
# General Derivation
$$
\int\limits_{\text{BZ}} d^{3}k_{1} \int\limits_{\text{BZ}} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{v}(\mathbf{k}_{2}) - \hbar\omega  \Big)
$$

We consider only direct interband transitions so $\mathbf{k}_{1}\approx\mathbf{k}_{2}$ and the integral immediately loses 3 degrees of freedom. The transition essentially takes place at a point $\mathbf{k}$ in phase space between two energy bands. The integral becomes

$$
\int\limits_{\text{BZ}} d^{3}k \; f(\mathcal{E}_{c}(\mathbf{k})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) - \hbar\omega  \Big)
$$

The proper change of variables
$d^{3}k  \to 2\pi dk_{\perp}dk_{\parallel} \to  \mathcal{D}(\mathcal{E;\hbar\omega})d\Delta d\mathcal{E}$ will allow us to transition into the following form

$$
\frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}\int\limits_{\mathcal{E_{min}(\hbar \omega)}}^{\mathcal{E_{max}(\hbar \omega)}}  \, \frac{f(\mathcal{E})\Big[ 1-f(\mathcal{E}-\Delta) \Big]}{\sqrt{ \mathcal{E}_{max}(\hbar\omega) -\mathcal{E}}} \; \delta \big( \Delta - \hbar\omega \big) \; d\Delta d\mathcal{E}
$$

this consequently allows us to directly resolve the delta reaching the "final" form

$$I(\hbar\omega)= \frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E_{min}(\hbar \omega)}}^{\mathcal{E_{max}(\hbar \omega)}} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E_{max}(\hbar\omega)}-\mathcal{E} }} \; d\mathcal{E}
$$
which still has to be solved numerically, but is a one-dimensional rather than a three-dimensional integral. And it totally avoids the problematic delta function.

# Detailed Derivation



==All models are wrong, but some are useful==