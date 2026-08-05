Here we aim to rederive explicitly, and compare, the imaginary interband permittivity provided in [GRW1975](references/PDFs/7%20-%20Rosei.pdf). Our starting point is a general Fermi golden rule for the transition from lower energy band 

$$
{\varepsilon}_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \int\limits_{\rm BZ}\!{\mathrm{d}}^3k\;
\bigl|P_{l\to u}(\mathbf k)\bigr|^{2}\,
\delta \bigl(\mathcal{E}_u(\mathbf k)-\mathcal{E}_l(\mathbf k)-{\hbar\omega}\bigr)\,
f\bigr(\mathcal{E}_{l}(\mathbf{k})\bigl)\Bigl[1-{f}\bigl(\mathcal{E}_u(\mathbf k)\bigr)\Bigr] \tag{1}
$$
Next, we assume that the transition dipole moment is $k$-independent in the regions where our transitions are concerned and that the emission is isotropic, namely $\bigl|P_{l\to u}(\mathbf k)\bigr| \to \frac{|\overline{P_{l \to u}}|^{2}}{3}$. We also follow suit in the assumption that the lower band is approximately full $f(\mathcal{E}_{l})\approx 1$ which results in:

$$
{\varepsilon}_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{|\overline{P_{l \to u}}|^{2}}{3}\int\limits_{\rm BZ}\!{\mathrm{d}}^3k\;
\delta \bigl(\mathcal{E}_u(\mathbf k)-\mathcal{E}_l(\mathbf k)-{\hbar\omega}\bigr)\,
\Bigl[1-{f}\bigl(\mathcal{E}_u(\mathbf k)\bigr)\Bigr] \tag{2}
$$
To solve analytically, Rossei introduces the parabolic band approximations at the points of high symmetry where the overwhelming majority of contribution to interband transition lives, namely the $X$ and $L$ points. The parabolic band approximations are given as such:

$$
\begin{align}
\mathcal{E}_{u}(\mathbf{k}) &=  +\mathcal{E}_{u_{0}}+\frac{\hbar^{2}}{2m_{u\perp}}\cdot k_{\perp}^{2} + s\frac{\hbar^{2}}{2m_{u\parallel}}\cdot k_{\parallel}^{2}\\
\mathcal{E}_{l}\mathbf{(k)}&=-\mathcal{E}_{l_{0}}- \ \frac{\hbar^{2}}{2m_{l\perp}}\cdot k_{\perp}^{2} \ - \  \frac{\hbar^{2}}{2m_{l\parallel}}\cdot k_{\parallel}^{2}
\end{align} \qquad\qquad s = \begin{cases}
-1 & \text{X point} \\
+1 & \text{L point}
\end{cases}
$$
here $k_{\parallel}$ is defined from the center of the facet to the center of the BZ along $\Gamma$, and $k_{\perp}$ is the radial coordinate, co-planar with the facet and parallel to $\Gamma$. This cylindrical symmetry enables us to reduce the dimensionality of $(2)$ by transitioning to cylindrical coordinates and integrating over the azimuthal coordinate

$$
{\varepsilon}_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{|\overline{P_{l \to u}}|^{2}}{3}\int\limits_{\rm BZ}\!2\pi k_{\perp}dk_{\perp}dk_{\parallel} \ 
\delta \bigl(\mathcal{E}_u(k_{\perp},k_{\parallel})-\mathcal{E}_l(k_{\perp},k_{\parallel})-{\hbar\omega}\bigr)\,
\Bigl[1-{f}\bigl(\mathcal{E}_u(k_{\perp},k_{\parallel})\bigr)\Bigr] \tag{2}
$$

The objective is finding the *EDJDOS*, $\mathcal{D}(\mathcal{E},\hbar\omega)$, and integration limits $\mathcal{E}_{\mathrm{min}}(\hbar\omega)$ and $\mathcal{E}_{\mathrm{max}}(\hbar\omega)$.
# I. EDJDOS & Integration Limits
Azimuthal symmetry allows us to integrate over $k_{\phi}$ and remain with only two integration variables.

$$
dk_{x}dk_{y} dk_{z}\to k_{\perp}dk_{\perp}dk_{\parallel}dk_{\phi}\to 2\pi k_{\perp} dk_{\perp} dk_{\parallel} \tag{1.1}
$$

For convenience, we orient the z, and $\parallel$ axes in the direction pointing to BZ center such that the positive part of $k_{\parallel}$ is inside BZ, and the negative is outside. We care only about what's inside the first BZ, and therefore our integration limits in the remaining two variables are:

$$
\begin{align}
k_{\perp} &>0  \\
k_{\parallel}& > 0
\end{align}
$$

Next, we change to variables for which the dispersion relation is linear, and for whom the integration range remains similar:
$$
\begin{align}
k_{\perp}^{2} &\to x&& x>0\\
k_{\parallel}^{2} &\to y&&y>0
\end{align} \tag{1.2}
$$
The measure is as follows:
$$
2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi  \ \frac{dx\ dy}{\sqrt{ y }} \tag{1.3}
$$
As a final transformation, we define the new energy variables $\mathcal{E}$ and $\Delta$ inspired by the quadratic dispersion relations (see below)
$$
\begin{align}
\mathcal{E} &\to \mathcal{E}_{u}(x,y) &&= \mathcal{E}_{u_{0}}+A_{u}\cdot x + sB_{u}\cdot y  \\
\Delta &\to \mathcal{E}_{u}(x,y) - \mathcal{E}_{l}(x,y) &&= \mathcal{E}_{g}  \  +  \ \overline{A}\cdot x  \ +  \ \overline{B}_{s}\cdot y
\end{align} \tag{1.4}
$$

> [!NOTE] Energy Bands & Notations
The upper and lower quadratically approximated bands are given by:$$\begin{align}
\mathcal{E}_{u}(\mathbf{k}) &=  +\mathcal{E}_{u_{0}}+A_{u}\cdot k_{\perp}^{2} + sB_{u}\cdot k_{\parallel}^{2}\\
\mathcal{E}_{l}\mathbf{(k)}&=-\mathcal{E}_{l_{0}}- \ A_{l}\cdot k_{\perp}^{2} \ - \  B_{l}\cdot k_{\parallel}^{2}
\end{align} \qquad s = \begin{cases}
-1 & \text{X point} \\
+1 & \text{L point}
\end{cases} \tag{1.5}$$where the following are denoted for clarity$$\begin{align}&A_{j} = \frac{\hbar^{2}}{2m_{j\perp}} && B_{j} = \frac{\hbar^{2}}{2m_{j\parallel}} \\ &\overline{A}= A_{l}+A_{u} && \overline{B}_{s}=B_{l}+sB_{u}\end{align} \tag{1.6}$$

We can write this in a matrix notation and identify the jacobian matrix

$$
\begin{pmatrix}
\mathcal{E} \\ \Delta
\end{pmatrix} = \begin{pmatrix}
\mathcal{E}_{u_{0}} \\ \mathcal{E}_{g}
\end{pmatrix} + \underbrace{ \begin{pmatrix}
A_{u} & sB_{u} \\ \overline{A} & \overline{B}_{s}
\end{pmatrix} }_{ J_{s} }\begin{pmatrix}
x \\ y
\end{pmatrix} \tag{1.7}
$$
The integration measure is therefore
$$
dx \ dy = \frac{1}{|D_{s}|} d\mathcal{E}\ d\Delta \qquad D_{s} =\det{J_{s}} =  A_{u}B_{l} - sB_{u}A_{l} \tag{1.8}
$$
> [!NOTE] Connection to Rosei's $\mathcal{F_{l\to u}}$
> $$\begin{align}
D_{s} &= \frac{\hbar^{4}}{4}\left( \frac{1}{m_{u\perp}m_{l\parallel}}-\frac{s}{m_{u\parallel}m_{l\perp}} \right) \\ &= \left( \frac{\hbar^{2}}{2} \right)^{2}\left( \frac{m_{u\parallel}m_{l\perp}-s\cdot m_{u\perp}m_{l\parallel}}{m_{u\parallel}m_{l\perp}m_{u\perp}m_{l\parallel}} \right) = \left( \frac{\hbar^{2}}{2\mathcal{F_{s}}} \right)^{2} \tag{1.9}
\end{align}$$

The inverse transformation, allows us to find...
$$\begin{pmatrix} x_{s} \\ y_{s} \end{pmatrix} = \underbrace{ \frac{1}{D_{s}} \begin{pmatrix} \overline{B}_{s} & -sB_u \\ -\overline{A} & A_u \end{pmatrix} }_{ J_{s}^{-1} } \begin{pmatrix} \mathcal{E} - \mathcal{E}_{u_0} \\ \Delta - \mathcal{E}_g \end{pmatrix} \tag{1.10} $$
The $s$ subscript in the new variables is just for the sake of clarity regarding the dependence of their form on the transition point in k-space.

$$
\begin{align}
x_{s}({\mathcal{E},\Delta}) &= \frac{\overline{B_{s}}(\mathcal{E}-\mathcal{E}_{u_{0}})+sB_{u}(\mathcal{E}_{g}-\Delta)}{D_{s}} \\
y_{s}(\mathcal{E},\Delta) & = \frac{{\overline{A}(\mathcal{E}_{u_{0}}-\mathcal{E})+A_{u}(\Delta-\mathcal{E}_{g})}}{D_{s}}
\end{align} \tag{1.11}
$$
From (3.8) and (2.3) we find the integration bounds in $\mathcal{E}$
$$
\begin{align}
x_{s}&\geq 0 &&\to  \quad \mathcal{E} \geq \overbrace{\mathcal{E}_{u_{0}} - s \frac{B_{u}}{\overline{B}_{s}}(\mathcal{E}_{g}-\Delta)}^{\mathcal{E}_{min}^{s}(\Delta)} \\
y_{s}&\geq 0 &&\to  \quad \mathcal{E} \leq \underbrace{ \mathcal{E}_{u_{0}} +  \frac{A_{u}}{\overline{A}}(\Delta-\mathcal{E}_{g}) }_{ {\mathcal{E}_{max}(\Delta)} }
\end{align}\tag{1.12}
$$
We use the new bounds defined in the above to write (3.8) more neatly
$$
\begin{align}
x_{s}(\mathcal{E},\Delta) &= \frac{\overline{B}_{s}}{D_{s}}\Big[ \mathcal{E}-\mathcal{E}_{\text{min}}^{s}(\Delta) \Big] \\

y_{s}(\mathcal{E},\Delta) &= \frac{\overline{A}}{D_{s}}\Big[  \mathcal{E}_{\text{max}}(\Delta)-\mathcal{E}\Big] 
\end{align}\tag{1.13}
$$

Finally, the EDJDOS can be spotted to be
$$
d^{3}k\to2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi  \ \frac{dx\ dy}{\sqrt{ y }} \to \underbrace{ \frac{\pi}{|D_{s}|\sqrt{ y_{s}(\mathcal{E},\Delta) }} }_{ \mathcal{D_{s}(\mathcal{E},\Delta)} }{d\mathcal{E} \ d\Delta} \tag{1.14}
$$
or more explicitly, using Rosei's $\mathcal{F}$:
$$
\boxed{\mathcal{D}_{s}(\mathcal{E},\hbar\omega) = \frac{4\pi \mathcal{F}_{s}^{2}}{\hbar^{4}\sqrt{ y_{s}(\mathcal{E},\hbar\omega) }}}\tag{1.15}
$$
# II. Discrepancies
1. Integration limits (explicit (units))
2. $E_{\text{min}}$ difference due to saddle\min (C&S)
3. EDJDOS factor

> [!WARNING] DISCREPANCY #1 - PARALLEL MOMENTUM
> Rosei's expression for the parallel wave-vector is given by equation (6) in the paper:
$$k_{\parallel} = \left( \hbar\omega - \hbar\omega_{{\scriptsize X}_{7^{+}}} + \frac{\hbar^{2}}{2m_{l\perp}}(\hbar\omega_{{\scriptsize X}_{6^{-}}} - \mathcal{E} ) - \frac{\hbar^{2}}{2m_{u\perp}}\mathcal{E}\right)^{1/2}$$Before drawing the comparison two issues become evidently clear
>1. there's an inconsistent addition of units in the brackets
>2. this expression is not dimensionally equivalent to $1/L$ as one would expect
Looking at our expression$$
k_{\parallel} =\sqrt{ y_{s}(\mathcal{E},\hbar\omega) }  = \left( \frac{{\overline{A}(\mathcal{E}_{u_{0}}-\mathcal{E})+A_{u}(\hbar\omega-\mathcal{E}_{g})}}{D_{s}}\right)^{1/2}$$A quick check reveals that it is equivalent to one over length, and needless to say that there is no weird addition of different units. There is clearly (hopefully just) a typo in the paper. Arranging our expression in a similar fashion to his: $$k_{\parallel} =\left( \frac{A_{l}(\mathcal{E}_{u_{0}}-\mathcal{E}) + A_{u}(\hbar\omega - \mathcal{E}_{l_{0}}-\mathcal{E})}{D_{s}} \right)^{1/2}$$ It appears that the $A_{u} = \frac{\hbar^{2}}{2m_{u\perp}}$ was omitted (as well as the Jacobian in the denominator).

> [!WARNING] DISCREPANCY #2 - INTEGRATION LIMITS
> Let us unpack the upper integration limit derived in this article and compare to Rosei's equation number (8) in the paper:
> $$\begin{align}\mathcal{E}_{\text{max}}(\hbar\omega) &= \mathcal{E}_{u_{0}} +  \frac{A_{u}}{\overline{A}}(\hbar\omega-\mathcal{E}_{g}) \\ &= \mathcal{E}_{u_{0}} + \frac{{\frac{\hbar^{2}}{2m_{u\perp}}}}{\frac{\hbar^{2}}{2m_{u\perp}} + \frac{\hbar^{2}}{2m_{u\parallel}}}(\hbar\omega-\mathcal{E}_{u_{0}}-\mathcal{E}_{l_{0}})\\&=\mathcal{E}_{u_{0}} + \frac{{m_{u\parallel}}}{{m_{u\perp}} + {m_{u\parallel}}}(\hbar\omega-\mathcal{E}_{u_{0}}-\mathcal{E}_{l_{0}}) \\ \\ \mathcal{E}^{\text{rosei}}_{\text{max}}(\hbar\omega) &= \mathcal{E}_{u_{0}} + \frac{{m_{u\parallel}}}{{m_{u\parallel}} - {m_{u\perp}}}(\mathcal{E}_{u_{0}}+\mathcal{E}_{l_{0}}-\hbar\omega) \end{align}$$ This difference stems from the sign of $m_{u\parallel}$. Here we assume absolute values (based on C&S) and absorb the sign into the dispersion relation, not sure what Rosei did, but from our expression it appears as though he's taken $m_{u\parallel}<0$ ==(doesn't align with C&S data though which he himself cites)==


> [!WARNING] DISCREPANCY #3 - EDJDOS
> This EDJDOS differs from Rosei's (equation 4 in the paper) which is given by:$$\mathcal{D}_{l\to u}^{\text{rosei}}(\mathcal{E},\hbar\omega) = (8\pi^{2}\hbar^{2})^{-1}\mathcal{F}_{l\to u} \ k_{\parallel}^{-1}$$The discrepancy boils down to:$$\frac{\mathcal{D}_{\text{mine}}}{\mathcal{D}_{\text{rosei}}} = \frac{\frac{4{\pi \mathcal{F^{2}}}}{\hbar^{4}k_{\parallel}}}{\frac{\mathcal{F}}{8\pi^{2}\hbar^{2}k_{\parallel}}} = \frac{2\pi\mathcal{F}}{\hbar^{2}} = \frac{\pi}{\sqrt{ D }}$$ In terms of units $$\left[ \frac{1}{\sqrt{ D }} \right]\propto \left[ \frac{1}{A} \right]\propto \left[ \frac{m}{\hbar^{2}} \right]$$ The ratio depends on the determinant, it is unclear whether and if Rosei absorbed it into one of his fit parameters, it seems however unlikely and I can't spot an issue with my derivation.
# Notes
in the numeric integration we're simply going to take $\mathcal{E}_{max}^{int}=\min(\mathcal{E}_{max},\mathcal{E}_{approx})$ and $\mathcal{E}_{min}^{int}=\max(\mathcal{E}_{min},-\mathcal{E}_{approx})$

$$
k_{\text{approx}}=\frac{\pi}{10a} ; \mathcal{E}_{\text{approx}}= \frac{\hbar^{2}k_{\text{approx}}^{2}}{2m} \tag{5.1} $$

- C&S data extraction - not a great idea; second derivative from a sparse digital data will be very noisy and unreliable.