### 1. The Model Setup
For the intraband case, where the conduction band is "out of the picture" it is more natural and easy to set $\mathcal{E_{0c}=0}$ 

$$
\mathcal{E}_{c}(\mathbf{k}) = \frac{\hbar^2 k_{\perp}^2}{2m_{c\perp}} - \frac{\hbar^2 k_{\parallel}^2}{2m_{c\parallel}} \equiv Ak_{\perp}^{2}-Bk_{\parallel}^{2}
$$

**Linearized Variables:**

- $x = k_{\perp}^2$
    
- $y = k_{\parallel}^2$
    
- Energies: $A = \frac{\hbar^2}{2m_{c\perp}}$, $B = \frac{\hbar^2}{2m_{c\parallel}}$
    

Energy Equation:

$$\mathcal{E} = Ax - By$$

Volume Element:

$$d^3k = \frac{\pi}{\sqrt{y}} \, dx \, dy$$

---

### 2. Deriving the Density of States $\rho(\mathcal{E})$

We seek the transformation $d^3k \to \rho(\mathcal{E})d\mathcal{E}$.

$$\rho(\mathcal{E}) = \pi \iint \delta(\mathcal{E} - (Ax - By)) \frac{dx \, dy}{\sqrt{y}}$$

Step 2a: Resolve the Delta Function (Integrate $y$)

The delta function fixes $y$ in terms of $x$ and $\mathcal{E}$:

$$y(x) = \frac{Ax - \mathcal{E}}{B}$$

The Jacobian for the delta function scaling by $B$ puts a factor of $1/B$ in the integral, or equivalently we substitute $dy$:

$$\rho(\mathcal{E}) = \frac{\pi}{B} \int \frac{dx}{\sqrt{y(x)}} = \frac{\pi}{B} \int \frac{dx}{\sqrt{\frac{Ax - \mathcal{E}}{B}}} = \frac{\pi}{\sqrt{B}} \int \frac{dx}{\sqrt{Ax - \mathcal{E}}}$$

Step 2b: Determine Integration Limits (The Dual Cutoff)

We must integrate over all valid $x$. The validity is constrained by the physical cutoffs of the Brillouin Zone ($x_{max}, y_{max}$) and the positivity of squared momenta ($x\ge0, y\ge0$).

1. From $y$ ($0 \le y \le y_{max}$):
    
    $$0 \le \frac{Ax - \mathcal{E}}{B} \le y_{max}$$
    
    $$\mathcal{E} \le Ax \le \mathcal{E} + B y_{max}$$
    
    $$\frac{\mathcal{E}}{A} \le x \le \frac{\mathcal{E} + B y_{max}}{A}$$
    
2. From $x$ ($0 \le x \le x_{max}$):
    
    $$0 \le x \le x_{max}$$
    

Combining these yields the rigorous integration interval $[x_{start}, x_{end}]$:

$$x_{start} = \max\left( 0, \frac{\mathcal{E}}{A} \right)$$

$$x_{end} = \min\left( x_{max}, \frac{\mathcal{E} + B y_{max}}{A} \right)$$

Step 2c: Perform the Integration

$$\rho(\mathcal{E}) = \frac{\pi}{\sqrt{B}} \int_{x_{start}}^{x_{end}} (Ax - \mathcal{E})^{-1/2} \, dx$$

Using $\int u^{-1/2} du = 2\sqrt{u}$ (with $du = A dx \implies dx = du/A$):

$$\rho(\mathcal{E}) = \frac{\pi}{\sqrt{B}} \left[ \frac{2}{A} \sqrt{Ax - \mathcal{E}} \right]_{x_{start}}^{x_{end}}$$

$$\rho(\mathcal{E}) = \frac{2\pi}{A\sqrt{B}} \left( \sqrt{Ax_{end} - \mathcal{E}} - \sqrt{Ax_{start} - \mathcal{E}} \right)$$

Step 2d: Simplify the Kernel

Substituting the limits back into the square roots simplifies the expressions physically:

- Upper Term: $\sqrt{A x_{end} - \mathcal{E}} = \sqrt{\min(A x_{max} - \mathcal{E}, B y_{max})}$
    
- Lower Term: $\sqrt{A x_{start} - \mathcal{E}} = \sqrt{\max(0, -\mathcal{E})}$
    

---

### 3. Validity Region (Integration Bounds for $\mathcal{E}$)

The DOS is non-zero only when $x_{start} < x_{end}$. This defines the physically allowed energy range for the master integral.

1. Bottom of Band ($\mathcal{E}_{min}$):
    
    Occurs when the "top" limit $\frac{\mathcal{E} + B y_{max}}{A}$ rises above $0$.
    
    $$\frac{\mathcal{E} + B y_{max}}{A} > 0 \implies \mathcal{E} > -B y_{max}$$
    
2. Top of Band ($\mathcal{E}_{max}$):
    
    Occurs when the "bottom" limit $\frac{\mathcal{E}}{A}$ is below $x_{max}$.
    
    $$\frac{\mathcal{E}}{A} < x_{max} \implies \mathcal{E} < A x_{max}$$
    

Validity Interval:

$$\mathcal{E} \in [-B y_{max}, \ A x_{max}]$$

---

### 4. Final Analytic Result

We substitute the derived DOS into the general convolution integral:

$$I(\hbar\omega) \propto \int d\mathcal{E} \, f(\mathcal{E})[1-f(\mathcal{E}-\hbar\omega)] \rho(\mathcal{E}) \rho(\mathcal{E}-\hbar\omega)$$

The integration bounds are the intersection of the validity regions for $\rho(\mathcal{E})$ and $\rho(\mathcal{E}-\hbar\omega)$.

- $\mathcal{E}_{lower} = -B y_{max} + \hbar\omega$
    
- $\mathcal{E}_{upper} = A x_{max}$
    

$$\boxed{ \begin{align} I(\hbar\omega) \propto \left( \frac{2\pi}{A\sqrt{B}} \right)^2 \int_{-B y_{max} + \hbar\omega}^{A x_{max}} d\mathcal{E} \;& f(\mathcal{E}) \Big[1-f(\mathcal{E}- \hbar\omega)\Big] \\ &\times \Bigg[ \sqrt{\min(A x_{max} - \mathcal{E}, B y_{max})} - \sqrt{\max(0, -\mathcal{E})} \Bigg] \\ &\times \Bigg[ \sqrt{\min(A x_{max} - (\mathcal{E}-\hbar\omega), B y_{max})} - \sqrt{\max(0, -(\mathcal{E}-\hbar\omega))} \Bigg] \end{align} }$$

**Key Features of this Result:**

1. **Explicit:** All variables are physical constants ($A, B, x_{max}, y_{max}$) or the integration variable $\mathcal{E}$. No hidden $\Delta$s.
    
2. **Robust:** The `min` and `max` functions prevent complex numbers inside the square roots.
    
3. **Correct Units:** The prefactor $\propto (1/A\sqrt{B})^2$ ensures correct dimensionality.
    
4. **Reference:** $\mathcal{E}=0$ is exactly the saddle point energy. Energies $\mathcal{E} < 0$ correspond to the "neck" of the hyperboloid, and $\mathcal{E} > 0$ correspond to the disjoint surfaces.