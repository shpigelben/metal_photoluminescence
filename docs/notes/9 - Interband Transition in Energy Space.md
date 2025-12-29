
$$
\mathcal{E}_{b}(\mathbf{k})  = \begin{cases}
-\mathcal{E}_{0v} - \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{V \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{V \parallel}} &&\implies\mathcal{E}_{0 v}-\alpha_{v}k_{\perp}^{2}-\beta_{v}k_{\parallel}^{2}  &&&(\mathcal{E<\mathcal{E_{0v}}})\\ \\
 \ \ \ \mathcal{E}_{0 c} + \frac{{\hbar ^{2}k_{\perp}^{2}}}{2m_{C \perp}} - \frac{{\hbar ^{2}k_{\parallel}^{2}}}{2m_{C \parallel}} && \implies\mathcal{E}_{0 c}+\alpha_{c}k_{\perp}^{2}-\beta_{c}k_{\parallel}^{2} &&&(\mathcal{E>\mathcal{E_{0c}}})
\end{cases} 
 $$

# General Derivation

$$
\int\limits_{\text{BZ}} d^{3}k_{1} \int\limits_{\text{BZ}} d^{3}k_{2} \; f(\mathcal{E}_{c}(\mathbf{k}_{1})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}_{2}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}_{1}) - \mathcal{E}_{v}(\mathbf{k}_{2}) - \hbar\omega  \Big)
$$
We consider only direct inter-band transitions so $\mathbf{k}_{1}\approx\mathbf{k}_{2}$ and the integral immediately loses 3 degrees of freedom. The transition essentially takes place at a point $\mathbf{k}$ in phase space between two energy bands. The integral becomes

$$
\int\limits_{\text{BZ}} d^{3}k \; f(\mathcal{E}_{c}(\mathbf{k})) \Big[1-f(\mathcal{E}_{v}(\mathbf{k}))\Big] \; \delta\Big(\mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) - \hbar\omega  \Big)
$$

The proper change of variables
$d^{3}k  \to 2\pi dk_{\perp}dk_{\parallel} \to  \mathcal{D}(\mathcal{E;\hbar\omega})d\Delta d\mathcal{E}$ will allow us to transition into the following form

$$
\frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}\int\limits_{\mathcal{E_{min}(\hbar \omega)}}^{\mathcal{E_{max}(\hbar \omega)}}  \, \frac{f(\mathcal{E})\Big[ 1-f(\mathcal{E}-\Delta) \Big]}{\sqrt{ \mathcal{E}_{max}(\hbar\omega) -\mathcal{E}}} \; \delta \big( \Delta - \hbar\omega \big) \; d\Delta d\mathcal{E}
$$

this consequently allows us to directly resolve the delta reaching the "final" form
$$
I(\hbar\omega)= \frac{\pi^{2}|\mu|^{2}}{\hbar \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E_{min}(\hbar \omega)}}^{\mathcal{E_{max}(\hbar \omega)}} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E_{max}(\hbar\omega)}-\mathcal{E} }} \; d\mathcal{E}
$$
which still has to be solved numerically, but is a one-dimensional rather than a three-dimensional integral. And it totally avoids the problematic delta function.

==All models are wrong, but some are useful==
# Detailed Derivation

## First COV
Using the cylindrical symmetry in k-space near the X and L points the first transformation is
$$
dk_{x}dk_{y} dk_{z}\to k_{\perp}dk_{\perp}dk_{\parallel}dk_{\phi}\to 2\pi k_{\perp} dk_{\perp} dk_{\parallel}
$$
where the $2\pi$ factor arrives from azimuthal symmetry. 

## Second COV
Next, we define new variables based on the individual dispersion relations

$$
\begin{align}
x &= k_{\perp}^{2} &&\implies dx = 2k_{\perp}dk_{\perp} &&& k_{\perp}\in[0,\infty)\to x\in[0,\infty)\\
y &= k_{\parallel}^{2} &&\implies \frac{1}{2}\frac{dy}{\pm\sqrt{ y }} = dk_{\parallel} &&& k_{\parallel}\in(-\infty,\infty)\to y\in[0,\infty)
\end{align}
$$
To account for $\pm\sqrt{ y }$ we can use the fact that the bands are even, and therefore symmetric relative to $k_{\parallel}$. We can simply multiply the Jacobian by a factor of $2$ to account for the two contributions
$$
2\pi k_{\perp} dk_{\perp} dk_{\parallel} \to \pi \frac{dxdy}{\sqrt{ y }}
$$
Finally, we define two new variables
$$
\begin{align}
\mathcal{E} &\equiv \mathcal{E}_{c}(x,y)  &&\implies\quad \mathcal{E}-\mathcal{E}_{0c} = A_{c}x - B_{c}y\\
\Delta &\equiv \mathcal{E}_{c}(x,y) - \mathcal{E}_{v}(x,y) &&\implies\quad\Delta - \mathcal{E}_{g} = \overline{A}x - \overline{B}y
\end{align}
$$
where the following are defined for the sake of brevity
$$
\begin{cases}
\mathcal{E}_{g} &\equiv \mathcal{E}_{c0}+\mathcal{E}_{v 0} \\
\overline{A}  & \equiv A_{c}+A_{v} \\
\overline{B}  & \equiv B_{v}-B_{c}
\end{cases}
$$
The transformation can be written in terms of matrices
$$\begin{pmatrix} \mathcal{E} - \mathcal{E}_{c0} \\ \Delta - \mathcal{E}_g \end{pmatrix} = \begin{pmatrix} A_c & -B_c \\ \bar{A} & \bar{B} \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
from which the inverse transformation is easily calculable
$$
\begin{pmatrix} x \\ y \end{pmatrix} = \frac{1}{D}\begin{pmatrix}
\bar{B} & B_{c} \\ -\bar{A} & A_{c}\end{pmatrix}\begin{pmatrix} \mathcal{E} - \mathcal{E}_{c0} \\ \Delta - \mathcal{E}_g \end{pmatrix}
$$
where $D$ is the determinant of the original transformation. It is positive since it consists of the values of the effective masses which are themselves positive.
$$
D = A_{c}B_{v}-A_{v}B_{c} = \frac{m_{c \perp}}{m_{v \perp}} + \frac{m_{c \parallel}}{m_{v \parallel}}
$$
from the inverse transformation we extract the definitions $x(\mathcal{E},\Delta)$ and $y(\mathcal{E},\Delta)$. With those definitions we can impose the known integration limits previously discussed to find the integration limits of the new integration variables

$$
\begin{align}
&x(\mathcal{E}, \Delta)>0  &&\implies  \quad \frac{1}{D} \left[ \bar{B}(\mathcal{E} - \mathcal{E}_{c0}) + B_c(\Delta - \mathcal{E}_g) \right] >0
\\  
&y(\mathcal{E}, \Delta)>0 &&\implies  \quad \frac{1}{D} \left[ -\bar{A}(\mathcal{E} - \mathcal{E}_{c0}) + A_c(\Delta - \mathcal{E}_g) \right] >0
\end{align}
$$

Notice that in the first inequality $\mathcal{E}$ appears with a positive sign and in the second it appears with a negative sign. Also, both $\mathcal{E}$ and $\Delta$ are present in the expressions which is the case since the new variables were defined as linear combinations of the previous variables. This means that the integration limit of one variable (here we chose to focus on $\mathcal{E}$ for obvious reasons) depends on the other variable. The first inequality results in a lower limit on $\mathcal{E}$, and the second results in an upper limit, namely
$$
\begin{align}
\mathcal{E}_{max}(\Delta) &= \mathcal{E}_{c 0 } + \frac{A_{c}}{A_{c} + A_{v}}(\Delta - \mathcal{E}_{g}) \\
\mathcal{E}_{min}(\Delta) &= \mathcal{E}_{c 0 } - \frac{B_{c}}{B_{v} + B_{c}}(\Delta - \mathcal{E}_{g})
\end{align}
$$
It is also useful explicitly write $y(\mathcal{E}, \Delta)$ since it appears in the Jacobian of the $(k_{\perp},k_{\parallel})\to(x,y)$ transformation. It can be shown that it is simply

$$
y(\mathcal{E}, \Delta) = \frac{\bar{A}}{D}\Big(\mathcal{E}_{max}(\Delta)-\mathcal{E}\Big)
$$

with those definitions we can now show that 

$$
\pi \frac{dxdy}{\sqrt{ y }} \to \frac{\pi}{D} \sqrt{ \frac{D}{\bar{A}} }\; \frac{d\Delta d\mathcal{E}}{\sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }}
$$
Finally we can present the initial integral in terms of variables that are explicit in the delta function
$$
\int\limits_{\text{BZ}}  \; f(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) }^{ \mathcal{E} }) \Big[1-f(\overbrace{ \mathcal{E}_{v}(\mathbf{k}) }^{\mathcal{E-\Delta}})\Big] \; \delta\Big(\overbrace{ \mathcal{E}_{c}(\mathbf{k}) - \mathcal{E}_{v}(\mathbf{k}) }^{ \Delta } - \hbar\omega  \Big) \; \underbrace{ \quad\quad d^{3}k \quad\quad }_{\Large \frac{\pi}{\sqrt{ D \bar{A} }}  \frac{d\Delta d\mathcal{E}}{ \sqrt{ \mathcal{E}_{max}(\Delta)-\mathcal{E} }} }
$$
This allows us to eliminate the delta for the $\Delta$ variable, leaving us with

$$
\boxed{I(\hbar\omega)\propto \frac{\pi}{ \sqrt{ \overline{A}D }}
\int\limits_{\mathcal{E_{min}(\hbar \omega)}}^{\mathcal{E_{max}(\hbar \omega)}} \frac{{f(\mathcal{E})f(\hbar\omega-\mathcal{E})}}{\sqrt{ \mathcal{E_{max}(\hbar\omega)}-\mathcal{E} }} \; d\mathcal{E}}
$$

