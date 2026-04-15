---
section: appendix
---
We begin by adopting the band approximation Given by Rossei for the valence and conduction dispersion relations,

$$
\begin{align}
\mathcal{E}_{v}(\mathbf{k})&=-\mathcal{E}_{0v} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{V \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{V \parallel}} &&\implies-\mathcal{E}_{0 v}-A_{v}k_{\perp}^{2}-B_{v}k_{\parallel}^{2}  &&&(\mathcal{E<\mathcal{E_{0v}}})\\ \\
 \ \ \ \mathcal{E}_{c}(\mathbf{k})&= \ \ \mathcal{E}_{0 c} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{C \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{C \parallel}} && \implies \ \ \mathcal{E}_{0 c}+A_{c}k_{\perp}^{2}-B_{c}k_{\parallel}^{2} &&&(\mathcal{E>\mathcal{E_{0c}}})
\end{align}
 $$

Our starting point is the interband emission integral given by Fermi's golden rule for the transition from an initial momentum state $\mathbf{k}_{1}$ to a final state $\mathbf{k}_{2}$

$$
\Gamma_{e}^{\text{cv}}(\hbar\omega) \propto\int\limits_{\text{BZ}} d^{3}k_{1} \int\limits_{\text{BZ}} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{v}(\mathbf{k}_{2}) - \hbar\omega  \Big)
$$

We consider only direct interband transitions $\mathbf{k}_{1}\approx\mathbf{k}_{2}$. The integral loses three degrees of freedom and the transition effectively takes place at a single $\mathbf{k}$ in phase space, giving

$$
\Gamma_{e}^{\text{cv}}(\hbar\omega) \propto\int\limits_{\text{BZ}} d^{3}k \; f(\mathcal{E}_{c}(\mathbf{k})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) - \hbar\omega  \Big)
$$

The rest of the derivation is a sequence of changes of variables that makes the delta function explicit and reduces the integral to one dimension.

# Cylindrical Symmetry
The first change of variables is a trivial one that adopts the cylindrical symmetry in k-space near the X and L points.
$$
dk_{x}dk_{y} dk_{z}\to k_{\perp}dk_{\perp}dk_{\parallel}dk_{\phi}\to 2\pi k_{\perp} dk_{\perp} dk_{\parallel}
$$

# Linearization of Momenta
Next, we linearize the dispersion relation by performing yet another change of variables

$$
\begin{align}
u &= k_{\perp}^{2} &&\implies du = 2k_{\perp}dk_{\perp} &&& k_{\perp}\in[0,\infty)\to u\in[0,\infty)\\
v &= k_{\parallel}^{2} &&\implies \frac{1}{2}\frac{dv}{\pm\sqrt{ v }} = dk_{\parallel} &&& k_{\parallel}\in(-\infty,\infty)\to v\in[0,\infty)
\end{align}
$$

To account for $\pm\sqrt{ v }$ we can use the fact that the bands are even functions in momentum, and are therefore symmetric with respect to $k_{\parallel}$. The Jacobean is multiplied by a factor of $2$ to account for the two contributions
$$
2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi \frac{dudv}{\sqrt{ v }}
$$
# Energy Space
Finally, we introduce another linear transformation from the linearized momenta $u$ and $v$ into the more physically meaningful variables $\mathcal{E}$ and $\Delta$ which are the conduction band energy and the energy difference between the conduction and valence

$$
\begin{align}
\mathcal{E} &\equiv \mathcal{E}_{c}(u,v)  &&\implies\quad \mathcal{E}-\mathcal{E}_{0c} = A_{c}u - B_{c}v\\
\Delta &\equiv \mathcal{E}_{c}(u,v) - \mathcal{E}_{v}(u,v) &&\implies\quad\Delta - \mathcal{E}_{g} = \overline{A}u + \overline{B}v
\end{align}
$$

where, $\mathcal{E}_{g} \equiv \mathcal{E}_{c0}+\mathcal{E}_{v 0} \quad\quad\overline{A}   \equiv A_{c}+A_{v} \quad\quad\overline{B}   \equiv B_{v}-B_{c}$. To find the Jacobean, the integration limits in terms of the new variables and the inverse transformation we write the linear change of variables in matrix notation
$$\begin{pmatrix} \mathcal{E} - \mathcal{E}_{c0} \\ \Delta - \mathcal{E}_g \end{pmatrix} = \underbrace{ \begin{pmatrix} A_c & -B_c \\ \bar{A} & \bar{B} \end{pmatrix}  }_{ M }\begin{pmatrix} u \\ v \end{pmatrix}$$
The inverse transformation is given by
$$
\begin{pmatrix} u \\ v \end{pmatrix} = \frac{1}{D}\begin{pmatrix}
\bar{B} & B_{c} \\ -\bar{A} & A_{c}\end{pmatrix}\begin{pmatrix} \mathcal{E} - \mathcal{E}_{c0} \\ \Delta - \mathcal{E}_g \end{pmatrix}
$$

This allows us to extract extract $u(\mathcal{E},\Delta)$ and $v(\mathcal{E},\Delta)$. 

$$
\begin{align}
&u(\mathcal{E}, \Delta)= \frac{1}{D} \left[ \bar{B}(\mathcal{E} - \mathcal{E}_{c0}) + B_c(\Delta - \mathcal{E}_g) \right]
\\  
&v(\mathcal{E}, \Delta) = \frac{1}{D} \left[ -\bar{A}(\mathcal{E} - \mathcal{E}_{c0}) + A_c(\Delta - \mathcal{E}_g) \right]
\end{align}
$$

Integration limits can be found by posing the constraints $u>0$ and $v>0$ deduced in the previous transformation
$$
\begin{align}
\mathcal{E}_{max}(\Delta) &= \mathcal{E}_{c 0 } + \frac{A_{c}}{A_{c} + A_{v}}(\Delta - \mathcal{E}_{g}) \\
\mathcal{E}_{min}(\Delta) &= \mathcal{E}_{c 0 } - \frac{B_{c}}{B_{v} + B_{c}}(\Delta - \mathcal{E}_{g})
\end{align}
$$

We can now neatly write $v(\mathcal{E}, \Delta)$ in terms of $\mathcal{E}_{max}$
$$
v(\mathcal{E}, \Delta) = \frac{\bar{A}}{D}\Big(\mathcal{E}_{max}(\Delta)-\mathcal{E}\Big)
$$
and insert it into the transformation (including the $1/D$ Jacobean factor from this current transformation). The new measure becomes
$$
\pi \frac{dudv}{\sqrt{ v }} \to \frac{\pi}{\sqrt{ \overline{A}D }} \frac{d\Delta d\mathcal{E}}{\sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }}
$$
Putting everything together, the emission integral turns into
$$
\Gamma_{e}^{\text{cv}}(\hbar\omega) \propto\int\limits_{\text{BZ}}  \; f(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) }^{ \mathcal{E} }) \Big[1-f(\overbrace{ \mathcal{E}_{v}(\mathbf{k}) }^{\mathcal{E-\Delta}})\Big] \; \delta\Big(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) }^{ \Delta } - \hbar\omega  \Big) \; \underbrace{ \quad\quad d^{3}k \quad\quad }_{\Large \frac{\pi}{\sqrt{ D \bar{A} }}  \frac{d\Delta d\mathcal{E}}{ \sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }} }
$$
The delta function, now explicit in its arguments with respect to the integration variables can finally be resolved, eliminating the $\Delta$ integral, leaving a one-dimensional expression
$$
\bbox[]{\Gamma_{e}^{\text{cv}}(\hbar\omega) =\frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E}_{min}(\hbar \omega)}^{\mathcal{E}_{max}(\hbar \omega)} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} \; d\mathcal{E}}
$$

which still must be solved numerically, but is a one-dimensional rather than a three-dimensional integral and it avoids the problematic delta function.
