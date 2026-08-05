
*EDJDOS*:
- *DOS*: density of states - how many electron $\mathbf{k}$ states exist for a given energy
- *j*: joint - we're counting transitions of similar momenta $\mathbf{k}_{i}=\mathbf{k}_{f}=\mathbf{k}$
- *ED*: energy distribution - per-energy *JDOS*, not yet integrated over all energies
$$
\begin{align}
{\varepsilon}_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3}&\int\limits_{\rm BZ}\!{\mathrm{d}}^3k\;
\bigl|M_{ul}(\mathbf k)\bigr|^{2}\,
\delta \bigl(E_u(\mathbf k)-E_l(\mathbf k)-{\hbar\omega}\bigr)\,
f\bigr(E_{l}(\mathbf{k})\bigl)\Bigl[1-{f}\bigl(E_u(\mathbf k)\bigr)\Bigr]\; \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3}\, \frac{N|P|^{2}}{3}& \int\limits_{\rm BZ}  \!{\mathrm{d}}^{3}k \;  \delta \bigr(\Delta(\mathbf{k})-\hbar \omega \bigl) f\bigl(E(\mathbf{k})-\Delta(\mathbf{k})\bigr)\Bigl[1-{f}\bigl(E(\mathbf k)\bigr)\Bigr] \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \iint\limits_{E,\Delta} \; dE d\Delta \; \mathcal{D}(E,\Delta) \delta(\Delta-\hbar\omega)f(E-\Delta) \bigl[1-f(E)  \bigr] \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \int\limits_{E_{\rm min}(\hbar\omega)}^{E_{\rm max}(\hbar\omega)} dE \; \mathcal{D}(E, \hbar\omega) f(E-\hbar\omega)\bigl[1-f(E)\bigr]  \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \; \mathcal{J}(\hbar\omega)
\end{align}
$$

The objective is finding the *EDJDOS*, $\mathcal{D}(E,\hbar\omega)$, and integration limits $E_{\mathrm{min}}(\hbar\omega)$ and $E_{\mathrm{max}}(\hbar\omega)$.
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
As a final transformation, we define the new energy variables $E$ and $\Delta$ inspired by the quadratic dispersion relations (see below)
$$
\begin{align}
E &\to E_{u}(x,y) &&= E_{u_{0}}+A_{u}\cdot x + sB_{u}\cdot y  \\
\Delta &\to E_{u}(x,y) - E_{l}(x,y) &&= E_{g}  \  +  \ \overline{A}\cdot x  \ +  \ \overline{B}_{s}\cdot y
\end{align} \tag{1.4}
$$

> [!NOTE] Energy Bands & Notations
The upper and lower quadratically approximated bands are given by:$$\begin{align}
E_{u}(\mathbf{k}) &=  +E_{u_{0}}+A_{u}\cdot k_{\perp}^{2} + sB_{u}\cdot k_{\parallel}^{2}\\
E_{l}\mathbf{(k)}&=-E_{l_{0}}- \ A_{l}\cdot k_{\perp}^{2} \ - \  B_{l}\cdot k_{\parallel}^{2}
\end{align} \qquad s = \begin{cases}
-1 & \text{X point} \\
+1 & \text{L point}
\end{cases} \tag{1.5}$$where the following are denoted for clarity$$\begin{align}&A_{j} = \frac{\hbar^{2}}{2m_{j\perp}} && B_{j} = \frac{\hbar^{2}}{2m_{j\parallel}} \\ &\overline{A}= A_{l}+A_{u} && \overline{B}_{s}=B_{l}+sB_{u}\end{align} \tag{1.6}$$

We can write this in a matrix notation and identify the jacobian matrix

$$
\begin{pmatrix}
E \\ \Delta
\end{pmatrix} = \begin{pmatrix}
E_{u_{0}} \\ E_{g}
\end{pmatrix} + \underbrace{ \begin{pmatrix}
A_{u} & sB_{u} \\ \overline{A} & \overline{B}_{s}
\end{pmatrix} }_{ J_{s} }\begin{pmatrix}
x \\ y
\end{pmatrix} \tag{1.7}
$$
The integration measure is therefore
$$
dx \ dy = \frac{1}{|D_{s}|} dE\ d\Delta \qquad D_{s} =\det{J_{s}} =  A_{u}B_{l} - sB_{u}A_{l} \tag{1.8}
$$
> [!NOTE] Connection to Rosei's $\mathcal{F_{l\to u}}$
> $$\begin{align}
D_{s} &= \frac{\hbar^{4}}{4}\left( \frac{1}{m_{u\perp}m_{l\parallel}}-\frac{s}{m_{u\parallel}m_{l\perp}} \right) \\ &= \left( \frac{\hbar^{2}}{2} \right)^{2}\left( \frac{m_{u\parallel}m_{l\perp}-s\cdot m_{u\perp}m_{l\parallel}}{m_{u\parallel}m_{l\perp}m_{u\perp}m_{l\parallel}} \right) = \left( \frac{\hbar^{2}}{2\mathcal{F_{s}}} \right)^{2} \tag{1.9}
\end{align}$$

The inverse transformation, allows us to find...
$$\begin{pmatrix} x_{s} \\ y_{s} \end{pmatrix} = \underbrace{ \frac{1}{D_{s}} \begin{pmatrix} \overline{B}_{s} & -sB_u \\ -\overline{A} & A_u \end{pmatrix} }_{ J_{s}^{-1} } \begin{pmatrix} E - E_{u_0} \\ \Delta - E_g \end{pmatrix} \tag{1.10} $$
The $s$ subscript in the new variables is just for the sake of clarity regarding the dependence of their form on the transition point in k-space.

$$
\begin{align}
x_{s}({E,\Delta}) &= \frac{\overline{B_{s}}(E-E_{u_{0}})+sB_{u}(E_{g}-\Delta)}{D_{s}} \\
y_{s}(E,\Delta) & = \frac{{\overline{A}(E_{u_{0}}-E)+A_{u}(\Delta-E_{g})}}{D_{s}}
\end{align} \tag{1.11}
$$
From (3.8) and (2.3) we find the integration bounds in $E$
$$
\begin{align}
x_{s}&\geq 0 &&\to  \quad E \geq \overbrace{E_{u_{0}} - s \frac{B_{u}}{\overline{B}_{s}}(E_{g}-\Delta)}^{E_{min}^{s}(\Delta)} \\
y_{s}&\geq 0 &&\to  \quad E \leq \underbrace{ E_{u_{0}} +  \frac{A_{u}}{\overline{A}}(\Delta-E_{g}) }_{ {E_{max}(\Delta)} }
\end{align}\tag{1.12}
$$
We use the new bounds defined in the above to write (3.8) more neatly
$$
\begin{align}
x_{s}(E,\Delta) &= \frac{\overline{B}_{s}}{D_{s}}\Big[ E-E_{\text{min}}^{s}(\Delta) \Big] \\

y_{s}(E,\Delta) &= \frac{\overline{A}}{D_{s}}\Big[  E_{\text{max}}(\Delta)-E\Big] 
\end{align}\tag{1.13}
$$

Finally, the EDJDOS can be spotted to be
$$
d^{3}k\to2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi  \ \frac{dx\ dy}{\sqrt{ y }} \to \underbrace{ \frac{\pi}{|D_{s}|\sqrt{ y_{s}(E,\Delta) }} }_{ \mathcal{D_{s}(E,\Delta)} }{dE \ d\Delta} \tag{1.14}
$$
or more explicitly, using Rosei's $\mathcal{F}$:
$$
\boxed{\mathcal{D}_{s}(E,\hbar\omega) = \frac{4\pi \mathcal{F}_{s}^{2}}{\hbar^{4}\sqrt{ y_{s}(E,\hbar\omega) }}}\tag{1.15}
$$
# II. Discrepancies
1. Integration limits (explicit (units))
2. $E_{\text{min}}$ difference due to saddle\min (C&S)
3. EDJDOS factor

> [!WARNING] DISCREPANCY #1 - PARALLEL MOMENTUM
> Rosei's expression for the parallel wave-vector is given by equation (6) in the paper:
$$k_{\parallel} = \left( \hbar\omega - \hbar\omega_{{\scriptsize X}_{7^{+}}} + \frac{\hbar^{2}}{2m_{l\perp}}(\hbar\omega_{{\scriptsize X}_{6^{-}}} - E ) - \frac{\hbar^{2}}{2m_{u\perp}}E\right)^{1/2}$$Before drawing the comparison two issues become evidently clear
>1. there's an inconsistent addition of units in the brackets
>2. this expression is not dimensionally equivalent to $1/L$ as one would expect
Looking at our expression$$
k_{\parallel} =\sqrt{ y_{s}(E,\hbar\omega) }  = \left( \frac{{\overline{A}(E_{u_{0}}-E)+A_{u}(\hbar\omega-E_{g})}}{D_{s}}\right)^{1/2}$$A quick check reveals that it is equivalent to one over length, and needless to say that there is no weird addition of different units. There is clearly (hopefully just) a typo in the paper. Arranging our expression in a similar fashion to his: $$k_{\parallel} =\left( \frac{A_{l}(E_{u_{0}}-E) + A_{u}(\hbar\omega - E_{l_{0}}-E)}{D_{s}} \right)^{1/2}$$ It appears that the $A_{u} = \frac{\hbar^{2}}{2m_{u\perp}}$ was omitted (as well as the Jacobian in the denominator).

> [!WARNING] DISCREPANCY #2 - INTEGRATION LIMITS
> Let us unpack the upper integration limit derived in this article and compare to Rosei's equation number (8) in the paper:
> $$\begin{align}E_{\text{max}}(\hbar\omega) &= E_{u_{0}} +  \frac{A_{u}}{\overline{A}}(\hbar\omega-E_{g}) \\ &= E_{u_{0}} + \frac{{\frac{\hbar^{2}}{2m_{u\perp}}}}{\frac{\hbar^{2}}{2m_{u\perp}} + \frac{\hbar^{2}}{2m_{u\parallel}}}(\hbar\omega-E_{u_{0}}-E_{l_{0}})\\&=E_{u_{0}} + \frac{{m_{u\parallel}}}{{m_{u\perp}} + {m_{u\parallel}}}(\hbar\omega-E_{u_{0}}-E_{l_{0}}) \\ \\ E^{\text{rosei}}_{\text{max}}(\hbar\omega) &= E_{u_{0}} + \frac{{m_{u\parallel}}}{{m_{u\parallel}} - {m_{u\perp}}}(E_{u_{0}}+E_{l_{0}}-\hbar\omega) \end{align}$$ This difference stems from the sign of $m_{u\parallel}$. Here we assume absolute values (based on C&S) and absorb the sign into the dispersion relation, not sure what Rosei did, but from our expression it appears as though he's taken $m_{u\parallel}<0$ ==(doesn't align with C&S data though which he himself cites)==


> [!WARNING] DISCREPANCY #3 - EDJDOS
> This EDJDOS differs from Rosei's (equation 4 in the paper) which is given by:$$\mathcal{D}_{l\to u}^{\text{rosei}}(E,\hbar\omega) = (8\pi^{2}\hbar^{2})^{-1}\mathcal{F}_{l\to u} \ k_{\parallel}^{-1}$$The discrepancy boils down to:$$\frac{\mathcal{D}_{\text{mine}}}{\mathcal{D}_{\text{rosei}}} = \frac{\frac{4{\pi \mathcal{F^{2}}}}{\hbar^{4}k_{\parallel}}}{\frac{\mathcal{F}}{8\pi^{2}\hbar^{2}k_{\parallel}}} = \frac{2\pi\mathcal{F}}{\hbar^{2}} = \frac{\pi}{\sqrt{ D }}$$ In terms of units $$\left[ \frac{1}{\sqrt{ D }} \right]\propto \left[ \frac{1}{A} \right]\propto \left[ \frac{m}{\hbar^{2}} \right]$$ The ratio depends on the determinant, it is unclear whether and if Rosei absorbed it into one of his fit parameters, it seems however unlikely and I can't spot an issue with my derivation.
# Notes
in the numeric integration we're simply going to take $E_{max}^{int}=\min(E_{max},E_{approx})$ and $E_{min}^{int}=\max(E_{min},-E_{approx})$

$$
k_{\text{approx}}=\frac{\pi}{10a} ; E_{\text{approx}}= \frac{\hbar^{2}k_{\text{approx}}^{2}}{2m} \tag{5.1} $$

- C&S data extraction - not a great idea; second derivative from a sparse digital data will be very noisy and unreliable.