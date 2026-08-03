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

$$
\begin{bmatrix}
E \ \\ \Delta \vphantom{\frac{A_{c}}{\overline{A}}}
\end{bmatrix} = \begin{bmatrix}
E_{0u} \\ E_{g} \vphantom{\frac{A_{c}}{\overline{A}}} 
\end{bmatrix} + \underbrace{ \begin{bmatrix}
A_{u} & sB_{u} \\ \overline{A} & \overline{B}
\end{bmatrix} }_{ \large J } \begin{bmatrix}
\ x \ \\ \  y \  \vphantom{\frac{A_{c}}{\overline{A}}}
\end{bmatrix}
$$
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

# The EDJDOS and Rosei's $\varepsilon_2$
The one-dimensional integral above is already Rosei's result in disguise. No new coordinates are needed — everything below is read off the measure and inverse map we already built.

Look at the emission integral just before the delta was resolved. The measure produced by the two changes of variables was
$$
d^{3}k \;\to\; \frac{\pi}{\sqrt{ \overline{A}D }}\,\frac{d\Delta\,d\mathcal{E}}{\sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }} .
$$
Resolving $\delta(\Delta-\hbar\omega)$ eats the $\Delta$-integral and leaves a kernel that multiplies $d\mathcal{E}$:
$$
\Gamma_{e}^{\text{cv}}(\hbar\omega) \propto \int_{\mathcal{E}_{min}}^{\mathcal{E}_{max}} \underbrace{ \frac{1}{\sqrt{ \overline{A}D }}\,\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} }_{\displaystyle \propto\; \mathcal{D}_{cv}(\mathcal{E},\hbar\omega)} \; f(\mathcal{E})\,\big[1-f(\mathcal{E}-\hbar\omega)\big]\, d\mathcal{E} .
$$
The underbraced factor is Rosei's **energy-distributed joint density of states** (EDJDOS): direct transitions per unit final (conduction) energy $\mathcal{E}$ and per unit photon energy $\hbar\omega$. It appears for free, because the variable $\mathcal{E}\equiv\mathcal{E}_{c}(u,v)$ we introduced *is* the final energy that Rosei distributes the JDOS over.

## Rosei's form of the kernel — where $\bar A$ hides
Rosei does not write the kernel in energy; he writes it as $\mathcal{D}_{cv}\propto\mathcal{F}^{2}/k_{\parallel}$, inversely proportional to the axial momentum on the constant-energy-difference surface. The two forms are the same object, and the bridge is the relation for $v=k_{\parallel}^{2}$ we already derived,
$$
k_{\parallel}^{2}=v(\mathcal{E},\Delta)=\frac{\bar{A}}{D}\big(\mathcal{E}_{max}(\Delta)-\mathcal{E}\big)
\qquad\Longrightarrow\qquad
\frac{1}{k_{\parallel}}=\sqrt{\frac{D}{\bar{A}}}\,\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} .
$$
**This is the only place $\bar A$ enters Rosei's expression.** He leaves it buried inside $k_{\parallel}$; passing to the energy variable pulls it out and sets it beside $D$ in the prefactor $\sqrt{\bar A D}$. Physically $\bar A=A_{c}+A_{v}=\hbar^{2}/2\mu_{\perp}$ is the transverse reduced mass of the gap — it fixes the rate at which the surface closes ($k_{\parallel}\to0$) as $\mathcal{E}$ reaches the singular edge $\mathcal{E}_{max}$.

## The mass factor — Rosei's Eq. (5)
The Jacobean determinant of the energy-space transformation is
$$
D \equiv \det M = A_{c}\bar{B}+B_{c}\bar{A} = A_{c}B_{v}+A_{v}B_{c} > 0 ,
$$
which Rosei repackages into a single quantity with units of mass, the mass factor $\mathcal{F}\equiv\hbar^{2}/2\sqrt{D}$. Inserting $A_{i}=\hbar^{2}/2m_{i\perp}$, $B_{i}=\hbar^{2}/2m_{i\parallel}$ the $\hbar^{2}/2$ cancels and his **Eq. (5)** falls out:
$$
\mathcal{F}=\left[\frac{1}{m_{C\perp}m_{V\parallel}}+\frac{1}{m_{V\perp}m_{C\parallel}}\right]^{-1/2}. \tag{5}
$$
Reading it backwards, $D=\hbar^{4}/4\mathcal{F}^{2}$, so the kernel is Rosei's **Eq. (4$'$)**
$$
\mathcal{D}_{cv}(\mathcal{E},\hbar\omega)=\frac{1}{16\pi^{2}D}\,\frac{1}{k_{\parallel}}=\frac{\mathcal{F}^{2}}{4\pi^{2}\hbar^{4}}\,\frac{1}{k_{\parallel}(\mathcal{E},\hbar\omega)}, \tag{4$'$}
$$
and substituting $1/k_{\parallel}$ from above returns the energy form we started from,
$$
\mathcal{D}_{cv}(\mathcal{E},\hbar\omega)=\frac{1}{16\pi^{2}\sqrt{\bar{A}D}}\,\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} .
$$
So $\mathcal{F}$ (a *product* of masses, factored out front) and $\bar A$ (a *sum of reciprocal* masses, controlling the energy dependence) are the same determinant $D$ seen from two sides — they only look independent because Rosei keeps $\bar A$ inside $k_{\parallel}$. (Rosei's *printed* (4) is linear in $\mathcal{F}$; it differs from (4$'$) only by the constant $2\mathcal{F}/\hbar^{2}$, which cannot bend a line shape and is absorbed into the fitted strength $S=\mathcal{F}|P|^{2}$ below.)

## Unpacking $A,\bar A,B,\bar B$
Every object above is built from four curvature coefficients and two combinations:

| symbol | definition | in masses | meaning |
|:---|:---|:---|:---|
| $A_{c},A_{v}$ | $\dfrac{\hbar^{2}}{2m_{C\perp}},\ \dfrac{\hbar^{2}}{2m_{V\perp}}$ | single-band transverse curvatures | how each band bends in the face ($k_{\perp}$) |
| $B_{c},B_{v}$ | $\dfrac{\hbar^{2}}{2m_{C\parallel}},\ \dfrac{\hbar^{2}}{2m_{V\parallel}}$ | single-band axial curvatures | how each band bends along the axis ($k_{\parallel}$) |
| $\bar{A}$ | $A_{c}+A_{v}=\dfrac{\hbar^{2}}{2\mu_{\perp}}$ | $\mu_{\perp}=\big(m_{C\perp}^{-1}+m_{V\perp}^{-1}\big)^{-1}$ | **transverse reduced mass** — sets the edge strength, hidden in $k_{\parallel}$ |
| $\bar{B}$ | $B_{v}-B_{c}$ | difference of axial curvatures | the saddle character at X ($\bar B_{X}<0$ on Au's masses) |
| $D$ | $A_{c}B_{v}+A_{v}B_{c}$ | $\big(\tfrac{\hbar^{2}}{2}\big)^{2}\!\big(\tfrac{1}{m_{C\perp}m_{V\parallel}}+\tfrac{1}{m_{V\perp}m_{C\parallel}}\big)$ | Jacobean determinant; $>0$ at X |
| $\mathcal{F}$ | $\hbar^{2}/2\sqrt{D}$ | Eq. (5) | product-type mass factored out front |

The one asymmetry worth noting: $\bar A$ is always a **sum** of reciprocal masses (a genuine reduced mass), while $\bar B=B_{v}-B_{c}$ is a **difference** — that difference is what makes the upper band a saddle at X and, ultimately, what distinguishes the soft X edge from the sharp L edge.

## Tie to $\varepsilon_2$ — Rosei's Eq. (9)
The absorptive dielectric function is this same kernel summed over the equivalent critical points and weighted by occupation. Writing the thermally weighted JDOS — Rosei's **Eq. (7)** —
$$
\mathcal{J}_{cv}(\hbar\omega,T)=\int_{\mathcal{E}_{min}}^{\mathcal{E}_{max}}\mathcal{D}_{cv}(\mathcal{E},\hbar\omega)\,\big[1-f(\mathcal{E})\big]\,d\mathcal{E}, \tag{7}
$$
the interband contribution assembles into Rosei's **Eq. (9)**
$$
\bbox[]{\;\varepsilon_{2}(\hbar\omega,T)=\frac{8\pi^{2}e^{2}\hbar^{4}}{3m^{2}(\hbar\omega)^{2}}\sum_{i=X,L}N_{i}\,|P_{i}|^{2}\,\mathcal{J}_{i}(\hbar\omega,T)\;} \tag{9}
$$
with $N_{X}=6$, $N_{L}=8$ equivalent points, $|P_{i}|^{2}=|\langle c|\nabla|v\rangle|^{2}$ the frozen interband matrix element (our $|\mu|^{2}$), and the whole line shape of each edge carried by $\mathcal{J}_{i}$ — i.e. by $\bar A$, the window, and the occupation. Rosei bundles the per-point constants into a fitted strength $S_{i}=\mathcal{F}_{i}|P_{i}|^{2}$ (his **Eq. (10)**).
