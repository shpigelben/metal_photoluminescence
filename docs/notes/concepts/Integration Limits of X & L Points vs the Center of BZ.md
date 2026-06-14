---
section: working-notes
---
**Neither the Rosei paper nor the standard texts explicitly treat the geometric transformation of the Brillouin Zone (BZ) boundaries when switching coordinates.**

The transition from a BZ-centered integral ($\int d^3k$ over a truncated octahedron) to a critical-point-centered integral ($\int dk_{\perp} dk_{\parallel}$ over a cylinder) usually involves an implicit mathematical leap.

### 1. The "Partitioning" Assumption
In rigorous theory, the total integral over the Brillouin Zone is partitioned:
$$\int_{\text{BZ}} (...) \, d^3k = \underbrace{\sum_{i=1}^{N_{valleys}} \int_{\text{Valley } i} (...) \, d^3k}_{\text{The Analytic Model}} + \underbrace{\int_{\text{Rest of BZ}} (...) \, d^3k}_{\text{The Background}}$$

- **The Analytic Part:** The papers assume that the "action" (the resonant absorption or emission) is concentrated entirely in small pockets near the $X$ and $L$ points. They replace the complex BZ polyhedron boundary with a "soft" infinite boundary or a simplified cylinder, assuming the integrand dies off (due to energy conservation limits or Fermi factors) _before_ it hits the actual geometric edge of the zone.
    
- **The Background:** The "rest" of the BZ is either assumed to be zero (for interband, because energy conservation isn't met elsewhere) or is lumped into a separate "Drude" background term (for intraband).


### 2. Center-to-Face Coordinate Shift
You noted the coordinates change from center-based ($k_x, k_y, k_z$) to face-based ($k_{\perp}, k_{\parallel}$).

- **Mathematically:** This is a simple translation: $\mathbf{k}_{new} = \mathbf{k}_{old} - \mathbf{k}_{X}$.
- **The Limits:** If you translated the limits rigorously, the integration bounds would become complex planes defining the facets of the truncated octahedron (e.g., $k_x + k_y + k_z = \text{const}$).
- **The Approximation:** The authors explicitly ignore these planar boundaries. Instead, they assume the validity region is a **sphere** (or cylinder) centered at $X$ with a radius $k_{cutoff} \ll k_{\Gamma}$.
    - _Rosei Quote:_ "Note that the paraboloid approximation made in (1) is accurate only if $k_{\perp}, k_{\parallel} \ll k_{\Gamma}$".

### 3. Why they get away with it

They don't treat the boundary limits because the **Energy Limits ($E_{min}, E_{max}$)** usually act as a stricter cutoff than the **Geometric Limits**.

- **Interband:** The condition $\mathcal{E}_c - \mathcal{E}_v = \hbar\omega$ defines a closed surface (or line). As long as this surface fits entirely inside the validity region (the local valley), the BZ boundaries are irrelevant. The integral naturally cuts itself off.
    
- **Intraband:** This is where the approximation is most dangerous. The "Saddle" surface is open (hyperbolic). It _never_ closes. This is why we **must** introduce the manual bandwidth cutoff ($R$ or $y_{cut}$) in our derivation. If we didn't, the integral would diverge, exposing the failure to treat the BZ boundary.
    

There is no "treatment" in the text because they are effectively replacing the BZ crystal with a "model solid" composed of infinite parabolic valleys, calculating the result, and then saying "this is valid only where the valleys are deep." The error introduced by this geometry mismatch is considered part of the "constant matrix element" approximation error, which is often much larger than the boundary error.