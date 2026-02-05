We work with the quadratic (Rosei) band approximation and then reduce the direct inter-band integral to a single energy integral by a sequence of explicit changes of variables.

$$
\mathcal{E}_{b}(\mathbf{k})  = \begin{cases}
-\mathcal{E}_{0v} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{V \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{V \parallel}} &&\implies-\mathcal{E}_{0 v}-A_{v}k_{\perp}^{2}-B_{v}k_{\parallel}^{2}  &&&(\mathcal{E<\mathcal{E_{0v}}})\\ \\
 \ \ \ \mathcal{E}_{0 c} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{C \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{C \parallel}} && \implies\mathcal{E}_{0 c}+A_{c}k_{\perp}^{2}-B_{c}k_{\parallel}^{2} &&&(\mathcal{E>\mathcal{E_{0c}}})
\end{cases}
 $$

Our starting point is the inter-band emission integral

$$
\int\limits_{\text{BZ}} d^{3}k_{1} \int\limits_{\text{BZ}} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{v}(\mathbf{k}_{2}) - \hbar\omega  \Big)
$$

We consider only direct inter-band transitions so $\mathbf{k}_{1}\approx\mathbf{k}_{2}$. The integral loses three degrees of freedom and the transition effectively takes place at a single $\mathbf{k}$ in phase space, giving

$$
\int\limits_{\text{BZ}} d^{3}k \; f(\mathcal{E}_{c}(\mathbf{k})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) - \hbar\omega  \Big)
$$

Below, each change of variables states (i) the Jacobian and (ii) the resulting integration limits.

## First COV: Cartesian $\to$ Cylindrical

**Definition.**
$$
k_{\perp}=\sqrt{k_{x}^{2}+k_{y}^{2}}, \quad k_{\parallel}=k_{z}, \quad \phi=\tan^{-1}(k_{y}/k_{x})
$$

**Jacobian.**
$$
d^{3}k = dk_{x}dk_{y}dk_{z} = k_{\perp}dk_{\perp}dk_{\parallel}d\phi
$$
Azimuthal symmetry makes the integrand $\phi$-independent, so
$$
\int_{0}^{2\pi} d\phi \to 2\pi, \qquad d^{3}k \to 2\pi k_{\perp}dk_{\perp}dk_{\parallel}
$$

**Limits.**
$$
k_{\perp}\in[0,\infty), \quad k_{\parallel}\in(-\infty,\infty), \quad \phi\in[0,2\pi)
$$

## Second COV: $(k_{\perp},k_{\parallel}) \to (u,v)$

**Definition.**
$$
u=k_{\perp}^{2}, \quad v=k_{\parallel}^{2}
$$
$$
du=2k_{\perp}dk_{\perp}, \quad dv=2k_{\parallel}dk_{\parallel}
$$

**Jacobian.**
From $k_{\perp}dk_{\perp}=du/2$ and the evenness in $k_{\parallel}$,
$$
\int_{-\infty}^{\infty} dk_{\parallel}\,g(k_{\parallel}^{2}) = \int_{0}^{\infty} \frac{dv}{\sqrt{v}}\,g(v)
$$
so the measure becomes
$$
2\pi k_{\perp}dk_{\perp}dk_{\parallel} \to \pi \frac{du\,dv}{\sqrt{v}}
$$

**Limits.**
$$
u\in[0,\infty), \quad v\in[0,\infty)
$$

## Third COV: $(u,v) \to (\mathcal{E},\Delta)$

**Definition.**
$$
\mathcal{E} \equiv \mathcal{E}_{c}(u,v)=\mathcal{E}_{0c}+A_{c}u-B_{c}v
$$
$$
\Delta \equiv \mathcal{E}_{c}(u,v)-\mathcal{E}_{v}(u,v)=\mathcal{E}_{g}+\overline{A}u+\overline{B}v
$$
with
$$
\mathcal{E}_{g}=\mathcal{E}_{0c}+\mathcal{E}_{0v}, \quad
A_{c}=\frac{\hbar^{2}}{2m_{C\perp}},\; A_{v}=\frac{\hbar^{2}}{2m_{V\perp}},\; B_{c}=\frac{\hbar^{2}}{2m_{C\parallel}},\; B_{v}=\frac{\hbar^{2}}{2m_{V\parallel}}
$$
$$
\overline{A}=A_{c}+A_{v}, \quad \overline{B}=B_{v}-B_{c}
$$

**Jacobian.**
The linear map is
$$\begin{pmatrix} \mathcal{E}-\mathcal{E}_{0c} \\ \Delta-\mathcal{E}_{g} \end{pmatrix}=
\begin{pmatrix} A_{c} & -B_{c} \\ \overline{A} & \overline{B} \end{pmatrix}
\begin{pmatrix} u \\ v \end{pmatrix}$$
with determinant
$$
D=A_{c}\overline{B}+B_{c}\overline{A}=A_{c}B_{v}+A_{v}B_{c}>0
$$
The inverse transformation is
$$
\begin{pmatrix} u \\ v \end{pmatrix}=\frac{1}{D}
\begin{pmatrix} \overline{B} & B_{c} \\ -\overline{A} & A_{c} \end{pmatrix}
\begin{pmatrix} \mathcal{E}-\mathcal{E}_{0c} \\ \Delta-\mathcal{E}_{g} \end{pmatrix}
$$
so
$$
du\,dv=\frac{1}{D}d\mathcal{E}\,d\Delta
$$
and
$$
v(\mathcal{E},\Delta)=\frac{1}{D}\Big[-\overline{A}(\mathcal{E}-\mathcal{E}_{0c})+A_{c}(\Delta-\mathcal{E}_{g})\Big]
$$

**Limits.**
The constraints $u\ge0$ and $v\ge0$ imply
$$
\overline{B}(\mathcal{E}-\mathcal{E}_{0c})+B_{c}(\Delta-\mathcal{E}_{g})\ge0
$$
$$
-\overline{A}(\mathcal{E}-\mathcal{E}_{0c})+A_{c}(\Delta-\mathcal{E}_{g})\ge0
$$
which give, for fixed $\Delta$,
$$
\mathcal{E}_{\min}(\Delta)=\mathcal{E}_{0c}-\frac{B_{c}}{\overline{B}}(\Delta-\mathcal{E}_{g})\quad(\overline{B}>0)
$$
$$
\mathcal{E}_{\max}(\Delta)=\mathcal{E}_{0c}+\frac{A_{c}}{\overline{A}}(\Delta-\mathcal{E}_{g})
$$
If $\overline{B}<0$ the ordering of the bounds swaps, and the admissible window is the intersection of the two inequalities above.

Using
$$
\mathcal{E}_{\max}(\Delta)=\mathcal{E}_{0c}+\frac{A_{c}}{A_{c}+A_{v}}(\Delta-\mathcal{E}_{g})
$$
we can rewrite
$$
v(\mathcal{E},\Delta)=\frac{\overline{A}}{D}\Big(\mathcal{E}_{\max}(\Delta)-\mathcal{E}\Big)
$$
so the measure becomes
$$
\pi\frac{du\,dv}{\sqrt{v}} \to \frac{\pi}{\sqrt{\overline{A}D}}\,\frac{d\Delta\,d\mathcal{E}}{\sqrt{\mathcal{E}_{\max}(\Delta)-\mathcal{E}}}
$$

Putting everything together, the integral reads

$$
\int\limits_{\text{BZ}}  \; f(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) }^{ \mathcal{E} }) \Big[1-f(\overbrace{ \mathcal{E}_{v}(\mathbf{k}) }^{\mathcal{E-\Delta}})\Big] \; \delta\Big(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) }^{ \Delta } - \hbar\omega  \Big) \; \underbrace{ \quad\quad d^{3}k \quad\quad }_{\Large \frac{\pi}{\sqrt{ \overline{A}D }}  \frac{d\Delta d\mathcal{E}}{ \sqrt{ \mathcal{E}_{\max}(\Delta)-\mathcal{E} }} }
$$
The delta function now eliminates the $\Delta$ integral, leaving a one-dimensional expression,

$$
I(\hbar\omega)= \frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E_{\min}(\hbar \omega)}}^{\mathcal{E_{\max}(\hbar \omega)}} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E_{\max}(\hbar\omega)}-\mathcal{E} }} \; d\mathcal{E}
$$
which still must be solved numerically, but is a one-dimensional rather than a three-dimensional integral and it avoids the problematic delta function.

==All models are wrong, but some are useful==

Substituting back the physical parameters gives
$$
\boxed{I(\hbar\omega)=\frac{2\sqrt{2}\,\pi^{2}|\mu|^{2}}{\hbar^{4}}
\frac{1}{\sqrt{\left(\frac{1}{m_{C\perp}}+\frac{1}{m_{V\perp}}\right)
\left(\frac{1}{m_{C\perp}m_{V\parallel}}+\frac{1}{m_{V\perp}m_{C\parallel}}\right)}}
\int\limits_{\mathcal{E_{\min}(\hbar \omega)}}^{\mathcal{E_{\max}(\hbar \omega)}} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E_{\max}(\hbar\omega)}-\mathcal{E} }} \, d\mathcal{E}}
$$
with
$$
\mathcal{E}_{\max}(\hbar\omega)=\mathcal{E}_{0c}+\frac{m_{V\perp}}{m_{C\perp}+m_{V\perp}}\,\big(\hbar\omega-\mathcal{E}_{g}\big)
$$
$$
\mathcal{E}_{\min}(\hbar\omega)=\mathcal{E}_{0c}-\frac{\frac{1}{m_{C\parallel}}}{\frac{1}{m_{V\parallel}}-\frac{1}{m_{C\parallel}}}\,\big(\hbar\omega-\mathcal{E}_{g}\big)\quad(\overline{B}>0)
$$
