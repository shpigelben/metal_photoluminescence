---
section: appendix
---
Kirchhoff showed that the ratio between specular emission and absorption is always the same regardless of what type of material emits.
$$
\frac{E(\omega)}{\alpha(\omega)} = B_{\scriptsize T} (\omega)
$$
Plank came later to show what $B_{\scriptsize T}(\omega)$ is and solved the ultraviolet catastrophe
___
In thermodynamics equilibrium (TDE) a material body emits according to the expression
$$
\mathcal{E}(\omega) = A(\omega)\cdot u_{\small\text{BB}}(\omega)
$$

The Planck Blackbody law is composed of two distinct parts:
$$u_{\small \text{BB}}(\omega)= \underbrace{\frac{\hbar\omega^3}{\pi^2 c^3}}_{\text{Photonic}} \times \underbrace{\frac{1}{e^{\hbar\omega/k_B T} - 1}}_{\text{Statistical}}$$
**The Photonic Part ($\omega^3$)** Comes from the ratio of vacuum modes to material absorption cross-section **The Statistical Part ($e^x - 1$)** Comes exactly from the ratio of the Fermi factors. Here is the mathematical proof that your Fermi factors generate the Bose-Einstein statistics necessary for Kirchhoff's Law.

### From Fermi-Dirac to Bose-Einstein

- **Spontaneous Emission Rate ($\Gamma_{sp}$):** Electron starts at $\mathcal{E}+\hbar\omega$ (Upper) and ends at $\mathcal{E}$ (Lower).
    
    $$\Gamma_{sp} \propto f(\mathcal{E}+\hbar\omega) [1 - f(\mathcal{E})]$$
    
- **Net Absorption Rate ($\Gamma_{abs}$):** This is tricky. To get the exact Planck law, you must calculate **Net Absorption** (Absorption minus Stimulated Emission).
    
    $$\Gamma_{abs} \propto \underbrace{f(\mathcal{E}) [1 - f(\mathcal{E}+\hbar\omega)]}_{\text{Absorption}} - \underbrace{f(\mathcal{E}+\hbar\omega) [1 - f(\mathcal{E})]}_{\text{Stimulated Emission}}$$
    

Now, let's take the ratio of **Emission to Net Absorption** and see if we get the Planck statistical factor.

$$\text{Ratio} = \frac{\text{Spontaneous}}{\text{Absorption} - \text{Stimulated}}$$

$$\text{Ratio} = \frac{f(U)[1-f(L)]}{f(L)[1-f(U)] - f(U)[1-f(L)]}$$

_(Using shorthand: $U = \mathcal{E}+\hbar\omega$, $L = \mathcal{E}$)_

Divide the numerator and denominator by the numerator ($f(U)[1-f(L)]$):

$$\text{Ratio} = \frac{1}{ \frac{f(L)[1-f(U)]}{f(U)[1-f(L)]} - 1 }$$

### The Magic of the Fermi Function

Now we evaluate the fraction in the denominator using the definition $f(\mathcal{E}) = \frac{1}{e^{(\mathcal{E}-\mathcal{E}_F)/kT} + 1}$.

A useful identity for Fermi functions is:

$$\frac{1-f(\mathcal{E})}{f(\mathcal{E})} = e^{(\mathcal{E}-\mathcal{E}_F)/k_B T}$$

Let's plug this into our fraction:

$$\frac{f(L)[1-f(U)]}{f(U)[1-f(L)]} = \left( \frac{f(L)}{1-f(L)} \right) \times \left( \frac{1-f(U)}{f(U)} \right)$$

$$= \left( e^{-(L-\mathcal{E}_F)/kT} \right) \times \left( e^{(U-\mathcal{E}_F)/kT} \right)$$

$$= e^{(U - L)/k_B T}$$

Since $U - L = (\mathcal{E}+\hbar\omega) - \mathcal{E} = \hbar\omega$, the fraction becomes exactly:

$$e^{\hbar\omega/k_B T}$$

### The Result

Substitute this back into our Ratio equation:

$$\text{Ratio} = \frac{1}{e^{\hbar\omega/k_B T} - 1}$$

This is exactly the **Bose-Einstein distribution**.

### Conclusion

Your intuition regarding the Fermi factors is correct and crucial.

- **The $\omega^3$ factor** (from the Density of States) explains why the Blackbody spectrum rises polynomially at low frequencies.
    
- **The Fermi factor ratio** (which you identified) explains why it rolls over and dies exponentially at high frequencies ($e^{-\hbar\omega/kT}$).
    

Both are required to perfectly reproduce the Planck law from microscopic principles.
    


    

---
    


    

### The Role of Stimulated Emission
    

It is worth noting that this derivation fails to produce the Planck law if **stimulated emission** is neglected. If we were to compare spontaneous emission directly to absorption (ignoring the stimulated term in the denominator), the ratio would simplify to:

$\text{Ratio} = \frac{\Gamma_{sp}}{\Gamma_{abs, \text{total}}} = \frac{f(U)[1-f(L)]}{f(L)[1-f(U)]} = e^{-\hbar\omega/k_B T}$

This result is known as **Wien's approximation**. While it correctly describes the high-energy (exponential decay) tail of the spectrum, it fails at low energies because it misses the "$-1$" in the denominator. 
    


    

Physically, stimulated emission is the mechanism that accounts for the **bosonic nature** of photons. Neglecting it is equivalent to treating photons as classical, distinguishable particles (Maxwell-Boltzmann statistics) rather than Bosons. To recover the full **Bose-Einstein distribution**, the net absorption must account for the photons' tendency to induce further transitions.
    
