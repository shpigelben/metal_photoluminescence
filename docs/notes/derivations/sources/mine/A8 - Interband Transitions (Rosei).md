---
section: appendix
---
We begin by adopting the band approximation given by Rosei for the lower ($l$, the $d$-band) and upper ($u$, conduction) dispersion relations,

$$
\begin{align}
\mathcal{E}_{l}(\mathbf{k})&=-\mathcal{E}_{0l} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{l \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{l \parallel}} &&\implies-\mathcal{E}_{0 l}-A_{l}k_{\perp}^{2}-B_{l}k_{\parallel}^{2}  &&&(\mathcal{E}\le-\mathcal{E}_{0l})\\ \\
 \ \ \ \mathcal{E}_{u}(\mathbf{k})&= \ \ \mathcal{E}_{0 u} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{u \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{u \parallel}} && \implies \ \ \mathcal{E}_{0 u}+A_{u}k_{\perp}^{2}-B_{u}k_{\parallel}^{2} &&&(\mathcal{E}\ge\mathcal{E}_{0u})
\end{align}
 $$

Here $u$ ("upper") and $l$ ("lower") are Rosei's band labels; the coefficients $A_{i}=\hbar^{2}/2m_{i\perp}$ and $B_{i}=\hbar^{2}/2m_{i\parallel}$ ($i=u,l$) are all positive, and the curvature signs are carried by the explicit $\pm$ in the dispersions. The upper band curves **up** in the face ($+A_{u}k_{\perp}^{2}$) and **down** along $\Gamma X$ ($-B_{u}k_{\parallel}^{2}$): it is a **saddle**.

Our starting point is the interband emission integral given by Fermi's golden rule for the transition from an initial momentum state $\mathbf{k}_{1}$ to a final state $\mathbf{k}_{2}$

$$
\epsilon_{2}(\hbar\omega) \propto\int\limits_{\text{BZ}} d^{3}k_{1} \int\limits_{\text{BZ}} d^{3}k_{2} \; f(\mathcal{E}_{u}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{l}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{u}(\mathbf{k}_{1}) - \mathcal{E}_{l}(\mathbf{k}_{2}) - \hbar\omega  \Big)
$$

We consider only direct interband transitions $\mathbf{k}_{1}\approx\mathbf{k}_{2}$. The integral loses three degrees of freedom and the transition effectively takes place at a single $\mathbf{k}$ in phase space, giving

$$
\Gamma_{e}^{\text{ul}}(\hbar\omega) \propto\int\limits_{\text{BZ}} d^{3}k \; f(\mathcal{E}_{u}(\mathbf{k})) \Big[1-f(\mathcal{E}_{l}(\mathbf{k}))\Big] \; \delta\Big(\mathcal{E}_{u}(\mathbf{k}) - \mathcal{E}_{l}(\mathbf{k}) - \hbar\omega  \Big)
$$

The rest of the derivation is a sequence of changes of variables that makes the delta function explicit and reduces the integral to one dimension.

# Cylindrical Symmetry
The first change of variables is a trivial one that adopts the cylindrical symmetry in k-space near the X and L points.
$$
dk_{x}dk_{y} dk_{z}\to k_{\perp}dk_{\perp}dk_{\parallel}dk_{\phi}\to 2\pi k_{\perp} dk_{\perp} dk_{\parallel}
$$

# First Change of Variables
Next, we linearize the dispersion relation by performing yet another change of variables. We name the squared momenta $x$ and $y$ (rather than reusing $u,v$, which would clash with the band labels):

$$
\begin{align}
x &= k_{\perp}^{2} &&\implies dx = 2k_{\perp}dk_{\perp} &&& k_{\perp}\in[0,\infty)\to x\in[0,\infty)\\
y &= k_{\parallel}^{2} &&\implies \frac{1}{2}\frac{dy}{\pm\sqrt{ y }} = dk_{\parallel} &&& k_{\parallel}\in(-\infty,\infty)\to y\in[0,\infty)
\end{align}
$$

To account for $\pm\sqrt{ y }$ we can use the fact that the bands are even functions in momentum, and are therefore symmetric with respect to $k_{\parallel}$. The Jacobean is multiplied by a factor of $2$ to account for the two contributions
$$
2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi \frac{dx\,dy}{\sqrt{ y }}
$$
# Energy Space
Finally, we introduce another linear transformation from the linearized momenta $x$ and $y$ into the more physically meaningful variables $\mathcal{E}$ and $\Delta$ which are the upper-band energy and the energy difference between the upper and lower bands

$$
\begin{align}
\mathcal{E} &\equiv \mathcal{E}_{u}(x,y)  &&\implies\quad \mathcal{E}-\mathcal{E}_{0u} = A_{u}x - B_{u}y\\
\Delta &\equiv \mathcal{E}_{u}(x,y) - \mathcal{E}_{l}(x,y) &&\implies\quad\Delta - \mathcal{E}_{g} = \overline{A}x + \overline{B}y
\end{align}
$$

where, $\mathcal{E}_{g} \equiv \mathcal{E}_{0u}+\mathcal{E}_{0l} \quad\quad\overline{A}   \equiv A_{u}+A_{l} \quad\quad\overline{B}   \equiv B_{l}-B_{u}$. To find the Jacobean, the integration limits in terms of the new variables and the inverse transformation we write the linear change of variables in matrix notation
$$\begin{pmatrix} \mathcal{E} - \mathcal{E}_{0u} \\ \Delta - \mathcal{E}_g \end{pmatrix} = \underbrace{ \begin{pmatrix} A_u & -B_u \\ \bar{A} & \bar{B} \end{pmatrix}  }_{ M }\begin{pmatrix} x \\ y \end{pmatrix}$$

**Here is $D$.** The Jacobean of this transformation is the determinant of $M$,
$$
D \equiv \det M = A_{u}\bar{B} + B_{u}\bar{A} = A_{u}B_{l} + A_{l}B_{u} > 0 .
$$
It is positive because every curvature coefficient is positive — this is the $X$-point value of the (signed) determinant $\mathcal{D}$ of the master derivation, which stays positive here for *either* sign of $\bar{B}_{X}$. The inverse transformation is given by
$$
\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{D}\begin{pmatrix}
\bar{B} & B_{u} \\ -\bar{A} & A_{u}\end{pmatrix}\begin{pmatrix} \mathcal{E} - \mathcal{E}_{0u} \\ \Delta - \mathcal{E}_g \end{pmatrix}
$$

This allows us to extract $x(\mathcal{E},\Delta)$ and $y(\mathcal{E},\Delta)$.

$$
\begin{align}
&x(\mathcal{E}, \Delta)= \frac{1}{D} \left[ \bar{B}(\mathcal{E} - \mathcal{E}_{0u}) + B_u(\Delta - \mathcal{E}_g) \right]
\\  
&y(\mathcal{E}, \Delta) = \frac{1}{D} \left[ -\bar{A}(\mathcal{E} - \mathcal{E}_{0u}) + A_u(\Delta - \mathcal{E}_g) \right]
\end{align}
$$

Integration limits can be found by posing the constraints $x>0$ and $y>0$ deduced in the previous transformation
$$
\begin{align}
\mathcal{E}_{max}(\Delta) &= \mathcal{E}_{0u } + \frac{A_{u}}{A_{u} + A_{l}}(\Delta - \mathcal{E}_{g}) &&\text{(from } y>0\text{)} \\
\mathcal{E}_{min}(\Delta) &= \mathcal{E}_{0u } - \frac{B_{u}}{B_{l} - B_{u}}(\Delta - \mathcal{E}_{g}) &&\text{(from } x>0\text{)}
\end{align}
$$

Note the $\mathcal{E}_{min}$ denominator is $B_{l}-B_{u}=\bar{B}$, straight from $x=0$ above. On gold's actual $X$ masses $\bar{B}_{X}<0$, so this "floor" is really where the window opens *downward* and the true lower cut is set by occupation rather than geometry — the master derivation handles that branch carefully; here we keep the clean geometric edge.

We can now neatly write $y(\mathcal{E}, \Delta)$ in terms of $\mathcal{E}_{max}$
$$
y(\mathcal{E}, \Delta) = \frac{\bar{A}}{D}\Big(\mathcal{E}_{max}(\Delta)-\mathcal{E}\Big)
$$
and insert it into the transformation (including the $1/D$ Jacobean factor from this current transformation). The new measure becomes
$$
\pi \frac{dx\,dy}{\sqrt{ y }} \to \frac{\pi}{\sqrt{ \overline{A}D }} \frac{d\Delta d\mathcal{E}}{\sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }}
$$
Putting everything together, the emission integral turns into
$$
\Gamma_{e}^{\text{ul}}(\hbar\omega) \propto\int\limits_{\text{BZ}}  \; f(\overbrace{ \mathcal{E}_{u}(\mathbf{k}) }^{ \mathcal{E} }) \Big[1-f(\overbrace{ \mathcal{E}_{l}(\mathbf{k}) }^{\mathcal{E-\Delta}})\Big] \; \delta\Big(\overbrace{ \mathcal{E}_{u}(\mathbf{k}) - \mathcal{E}_{l}(\mathbf{k}) }^{ \Delta } - \hbar\omega  \Big) \; \underbrace{ \quad\quad d^{3}k \quad\quad }_{\Large \frac{\pi}{\sqrt{ D \bar{A} }}  \frac{d\Delta d\mathcal{E}}{ \sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }} }
$$
The delta function, now explicit in its arguments with respect to the integration variables can finally be resolved, eliminating the $\Delta$ integral, leaving a one-dimensional expression
$$
\bbox[]{\Gamma_{e}^{\text{ul}}(\hbar\omega) =\frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E}_{min}(\hbar \omega)}^{\mathcal{E}_{max}(\hbar \omega)} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} \; d\mathcal{E}}
$$

(using $1-f(\mathcal{E}-\hbar\omega)=f(\hbar\omega-\mathcal{E})$ for the lower-band occupation). This still must be solved numerically, but is a one-dimensional rather than a three-dimensional integral and it avoids the problematic delta function.

# Rosei's Notation: how $\mathcal{D}$, $F$, $D$, and $\varepsilon_2$ emerge
Everything Rosei publishes is already contained in the measure and inverse map above — this section only renames the pieces into his symbols. No new change of variables.

## The EDJDOS emerges from the measure
Look at the emission integral one step before the delta is resolved. The measure the two changes of variables produced,
$$
d^{3}k \;\to\; \frac{\pi}{\sqrt{ \overline{A}D }}\,\frac{d\Delta\,d\mathcal{E}}{\sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }},
$$
already carries a density in $\mathcal{E}$. Resolving $\delta(\Delta-\hbar\omega)$ eats the $\Delta$-integral and leaves the kernel that multiplies $d\mathcal{E}$:
$$
\Gamma_{e}^{\text{ul}}(\hbar\omega)\;\propto\;\int_{\mathcal{E}_{min}}^{\mathcal{E}_{max}} \underbrace{ \frac{1}{\sqrt{\overline{A}D}}\,\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} }_{\displaystyle \propto\;\mathcal{D}_{l\to u}(\mathcal{E},\hbar\omega)}\; f(\mathcal{E})\,\big[1-f(\mathcal{E}-\hbar\omega)\big]\,d\mathcal{E}.
$$
The underbraced factor is Rosei's **energy-distributed joint density of states** (EDJDOS) $\mathcal{D}_{l\to u}$: direct transitions per unit final energy $\mathcal{E}$ and per unit photon energy $\hbar\omega$. It appears for free because the coordinate $\mathcal{E}\equiv\mathcal{E}_{u}(x,y)$ is exactly the final energy Rosei distributes the JDOS over.

## Rosei writes the same kernel as $F^{2}/k_{\parallel}$
Rosei does not write the kernel in energy; he writes it $\propto F^{2}/k_{\parallel}$, inversely proportional to the axial momentum on the constant-energy-difference surface. The bridge is the inverse-map result we already have for $y=k_{\parallel}^{2}$:
$$
k_{\parallel}^{2}=y(\mathcal{E},\Delta)=\frac{\overline{A}}{D}\big(\mathcal{E}_{max}(\Delta)-\mathcal{E}\big)
\qquad\Longrightarrow\qquad
\frac{1}{k_{\parallel}}=\sqrt{\frac{D}{\overline{A}}}\,\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} .
$$
**This is the only place $\overline{A}$ appears in Rosei's expression** — he leaves it buried inside $k_{\parallel}$; passing to the energy variable pulls it out and sets it beside $D$ in the prefactor $\sqrt{\overline{A}D}$. Physically $\overline{A}=A_{u}+A_{l}=\hbar^{2}/2\mu_{\perp}$ is the transverse reduced mass of the gap: the rate at which the surface closes ($k_{\parallel}\to0$) as $\mathcal{E}$ reaches the singular edge $\mathcal{E}_{max}$.

## $D$ and $F$ → Rosei's Eqs. (5) and (4$'$)
The determinant $D=\det M = A_{u}B_{l}+A_{l}B_{u}$ (defined at the Jacobean above) is the only place the masses enter the prefactor. Rosei repackages it into a single quantity with units of mass, the **mass factor** $F\equiv\hbar^{2}/2\sqrt{D}$. Inserting $A_{i}=\hbar^{2}/2m_{i\perp}$, $B_{i}=\hbar^{2}/2m_{i\parallel}$ the $\hbar^{2}/2$ cancels and his **Eq. (5)** drops out:
$$
F \equiv \frac{\hbar^{2}}{2\sqrt{D}} = \left( \frac{1}{m_{u\perp}m_{l\parallel}} + \frac{1}{m_{l\perp}m_{u\parallel}} \right)^{-1/2}. \tag{5}
$$
Reading it backwards, $D=\hbar^{4}/4F^{2}$, so the kernel is Rosei's **Eq. (4$'$)**
$$
\mathcal{D}_{l\to u}(\mathcal{E},\hbar\omega)=\frac{1}{16\pi^{2}D}\frac{1}{k_{\parallel}}=\frac{F^{2}}{4\pi^{2}\hbar^{4}}\frac{1}{k_{\parallel}(\mathcal{E},\hbar\omega)}, \tag{4$'$}
$$
and substituting $1/k_{\parallel}$ returns the energy form we read off the measure,
$$
\mathcal{D}_{l\to u}(\mathcal{E},\hbar\omega)=\frac{1}{16\pi^{2}\sqrt{\overline{A}D}}\frac{1}{\sqrt{ \mathcal{E}_{max}(\hbar\omega)-\mathcal{E} }} .
$$
So $F$ (a *product* of masses, factored out front) and $\overline{A}$ (a *sum of reciprocal* masses, controlling the energy dependence) are the same determinant $D$ seen from two sides — they only look independent because Rosei keeps $\overline{A}$ inside $k_{\parallel}$. (Rosei's *printed* (4) is linear in $F$; it differs from (4$'$) only by the constant $2F/\hbar^{2}$, which cannot bend a line shape and is absorbed into the fitted strength $S=F|P|^{2}$ below. Equivalently, the note's prefactor is $\tfrac{1}{\sqrt{\overline{A}D}}=\tfrac{2F}{\hbar^{2}\sqrt{\overline{A}}}$.)

## Unpacking $A,\overline{A},B,\overline{B}$ (and $D,F$)
Every object above is built from four curvature coefficients and two combinations:

| symbol | definition | in masses | meaning |
|:---|:---|:---|:---|
| $A_{u},A_{l}$ | $\dfrac{\hbar^{2}}{2m_{u\perp}},\ \dfrac{\hbar^{2}}{2m_{l\perp}}$ | single-band transverse curvatures | how each band bends in the face ($k_{\perp}$) |
| $B_{u},B_{l}$ | $\dfrac{\hbar^{2}}{2m_{u\parallel}},\ \dfrac{\hbar^{2}}{2m_{l\parallel}}$ | single-band axial curvatures | how each band bends along the axis ($k_{\parallel}$) |
| $\overline{A}$ | $A_{u}+A_{l}=\dfrac{\hbar^{2}}{2\mu_{\perp}}$ | $\mu_{\perp}=\big(m_{u\perp}^{-1}+m_{l\perp}^{-1}\big)^{-1}$ | **transverse reduced mass** — sets the edge strength, hidden in $k_{\parallel}$ |
| $\overline{B}$ | $B_{l}-B_{u}$ | difference of axial curvatures | the saddle character at X ($\overline{B}_{X}<0$ on Au's masses) |
| $D$ | $A_{u}B_{l}+A_{l}B_{u}$ | $\big(\tfrac{\hbar^{2}}{2}\big)^{2}\!\big(\tfrac{1}{m_{u\perp}m_{l\parallel}}+\tfrac{1}{m_{l\perp}m_{u\parallel}}\big)$ | Jacobean determinant; $>0$ at X |
| $F$ | $\hbar^{2}/2\sqrt{D}$ | Eq. (5) | product-type mass factored out front |

The one asymmetry worth reading off: $\overline{A}$ is always a **sum** of reciprocal masses (a genuine reduced mass), while $\overline{B}=B_{l}-B_{u}$ is a **difference** — that difference is what makes the upper band a saddle at X, and ultimately what splits the soft X edge from the sharp L edge.

## Tie to $\varepsilon_2$ — Rosei's Eq. (9)
The absorptive dielectric function is this same kernel summed over the equivalent critical points and weighted by occupation. Writing the thermally weighted JDOS — Rosei's **Eq. (7)** —
$$
\mathcal{J}_{l\to u}(\hbar\omega,T)=\int_{\mathcal{E}_{min}}^{\mathcal{E}_{max}}\mathcal{D}_{l\to u}(\mathcal{E},\hbar\omega)\,\big[1-f(\mathcal{E})\big]\,d\mathcal{E}, \tag{7}
$$
the interband contribution assembles into Rosei's **Eq. (9)**
$$
\bbox[]{\;\varepsilon_{2}(\hbar\omega,T)=\frac{8\pi^{2}e^{2}\hbar^{4}}{3m^{2}(\hbar\omega)^{2}}\sum_{i=X,L}N_{i}\,|P_{i}|^{2}\,\mathcal{J}_{i}(\hbar\omega,T)\;} \tag{9}
$$
with $N_{X}=6$, $N_{L}=8$ equivalent points, $|P_{i}|^{2}=|\langle u|\nabla|l\rangle|^{2}$ the frozen interband matrix element (our $|\mu|^{2}$), and the line shape of each edge carried entirely by $\mathcal{J}_{i}$ — i.e. by $\overline{A}$, the window, and the occupation. Rosei bundles the per-point constants into a fitted strength $S_{i}=F_{i}|P_{i}|^{2}$ (his **Eq. (10)**).
