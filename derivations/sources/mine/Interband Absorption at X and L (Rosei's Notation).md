l

# Interband diAbsorption at X and L — Rosei's Notation

A self-contained, rigorous derivation of the interband contribution to $\epsilon_2(\hbar\omega,T)$ of gold from $d$-band → Fermi-surface transitions at the **X** and **L** critical points, written entirely in the notation of Guerrisi, Rosei & Winsemius, *Phys. Rev. B* **12**, 557 (1975) (ref 7). Band indices are $l$ (lower) and $u$ (upper); masses $m_{l\perp},m_{l\|},m_{u\perp},m_{u\|}$; energies $E$ measured from the Fermi level $E_F$.

Following Rosei, **X is the saddle (open CEDS, sub-gap tail)** and **L is the $M_0$ minimum (closed ellipsoid, sharp onset)**. The two share all machinery and differ only in the sign of the upper-band $k_\|^2$ curvature.

## 1. From $\epsilon_2$ to the energy-distributed JDOS

The interband imaginary dielectric function, with dipole matrix element $P(l\to u)$ assumed constant over the small active region around each critical point,

$$
\epsilon_2(\hbar\omega,T)=\frac{8\pi^{2}e^{2}\hbar^{4}}{3m^{2}(\hbar\omega)^{2}}
\sum_{P=X,L}\big|P_{P}(l\to u)\big|^{2}\,g_{P}(\hbar\omega,T),
\tag{9}
$$

where $g_P=N_P\,\mathcal{I}_{l\to u}^{P}$ carries the point multiplicity ($N_X=6$, $N_L=8$) and the thermally weighted **integrated joint density of states**

$$
\mathcal{I}_{l\to u}(\hbar\omega,T)=\int_{E_{\min}}^{E_{\max}}
D_{l\to u}(E,\hbar\omega)\,[1-f(E,T)]\,dE .
\tag{7}
$$

The central object is the **energy-distributed JDOS (EDJDOS)** $D_{l\to u}(E,\hbar\omega)$: the density of vertical $l\to u$ transitions of energy $\hbar\omega$ whose **final** (upper) state lies at energy $E$,

$$
D_{l\to u}(E,\hbar\omega)=\frac{1}{(2\pi)^{3}}\int d^{3}k\;
\delta\!\big(E-\hbar\omega_{u}(\mathbf k)\big)\,
\delta\!\big(\hbar\omega-\Omega_{lu}(\mathbf k)\big),
\qquad
\Omega_{lu}(\mathbf k)=\hbar\omega_u-\hbar\omega_l .
\tag{3}
$$

The statistical weight in (7) is the final-state-empty factor $[1-f(E,T)]$. It is the $f(E-\hbar\omega)\to 1$ limit of the full product $f(\hbar\omega_l)[1-f(\hbar\omega_u)]$, valid because the initial $d$-state sits at $\hbar\omega_l\simeq-\hbar\omega_{X_7^+}\ll E_F$ and is filled (see [[Equivalence of My Absorption Integral and Rosei's]] §5).

The whole problem is to reduce the 3-D integral (3) to the 1-D form (7). With rotational symmetry about the $\Gamma$–$X$ (or $\Gamma$–$L$) axis, $d^{3}k=2\pi\,k_\perp\,dk_\perp\,dk_\|$, and the two $\delta$'s collapse the remaining 2-D integral through one Jacobian.

## 2. The X point: $d\to\mathrm{sp}$ saddle

### 2.1 Dispersions

Quadratic bands about X, rotational symmetry about $\Delta=\Gamma X$ (Rosei Fig. 2). Upper (sp) band — a **saddle**, curving up in $k_\perp$, down in $k_\|$:

$$
E=\hbar\omega_{u}=\hbar\omega_{X_6^-}+\frac{\hbar^{2}k_\perp^{2}}{2m_{u\perp}}-\frac{\hbar^{2}k_\|^{2}}{2m_{u\|}} .
\tag{1}
$$

Lower ($d$) band — a **maximum**, curving down both ways:

$$
E-\hbar\omega=\hbar\omega_{l}=-\hbar\omega_{X_7^+}-\frac{\hbar^{2}k_\perp^{2}}{2m_{l\perp}}-\frac{\hbar^{2}k_\|^{2}}{2m_{l\|}} .
\tag{2}
$$

Introduce the curvature coefficients $A_i=\hbar^{2}/2m_{i\perp}$, $B_i=\hbar^{2}/2m_{i\|}$ ($i=l,u$). The transition energy is

$$
\Omega_{lu}(\mathbf k)=\mathcal{E}_g^{X}+\bar A_X\,k_\perp^{2}+\bar B_X\,k_\|^{2},
\qquad\bar A_X=A_u+A_l,\quad \bar B_X=B_l-B_u,
$$

with the **vertical gap** $\mathcal{E}_g^{X}=\hbar\omega_{X_6^-}+\hbar\omega_{X_7^+}=1.94\ \text{eV}$. Because the upper band carries the **minus** sign, $\Omega_{lu}$ is a **saddle** in $\mathbf k$: the constant-energy-difference surface (CEDS) $\Omega_{lu}=\hbar\omega$ is an **open hyperboloid**, and transitions exist on **both** sides of $\mathcal{E}_g^X$ — the origin of the sub-gap tail.

### 2.2 Reduction: the Jacobian, $\mathcal{F}$, and $k_\|$

Change variables $(k_\perp,k_\|)\to(E,\Omega)$ with $E$ from (1) and $\Omega$ from above. The Jacobian is

$$
\frac{\partial(E,\Omega)}{\partial(k_\perp,k_\|)}
=\begin{vmatrix} 2A_u k_\perp & -2B_u k_\| \\[2pt] 2\bar A_X k_\perp & 2\bar B_X k_\| \end{vmatrix}
=4k_\perp k_\|\,(A_u\bar B_X+B_u\bar A_X)
=4k_\perp k_\|\,\mathcal{D}_X,
$$

where the **band-curvature determinant** is a pure-mass constant,

$$
\boxed{\ \mathcal{D}_X=A_uB_l+A_lB_u
=\Big(\tfrac{\hbar^{2}}{2}\Big)^{2}\frac{m_{l\perp}m_{u\|}+m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}\ }
$$

(the **sum** is the saddle signature). Collapsing both $\delta$'s in (3),

$$
D_{l\to u}(E,\hbar\omega)=\frac{1}{(2\pi)^{3}}\,\frac{2\pi k_\perp}{4k_\perp k_\|\,\mathcal{D}_X}
=\frac{1}{16\pi^{2}\,\mathcal{D}_X}\,k_\|^{-1}.
$$

Writing $\mathcal{D}_X=(\hbar^2/2)^2\,\mathcal{F}_{l\to u}^{-2}$ recovers Rosei's compact form

$$
D_{l\to u}(E,\hbar\omega)=\big(8\pi^{2}\hbar^{2}\big)^{-1}\,\mathcal{F}_{l\to u}\,k_\|^{-1},
\qquad
\mathcal{F}_{l\to u}=\left(\frac{m_{l\perp}m_{u\|}+m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}\right)^{-1/2}.
\tag{4,5}
$$

> The step $\frac{1}{16\pi^2\mathcal{D}_X}\to(8\pi^2\hbar^2)^{-1}\mathcal F$ trades one power of $\mathcal D_X^{1/2}=\tfrac{\hbar^2}{2}\mathcal F^{-1}$ for the constant $\mathcal F$; the leftover $E,\omega$-independent factor of order $2m/\hbar^2$ is absorbed into the overall scale of (9). This is the bookkeeping reconciled in detail in [[Equivalence of My Absorption Integral and Rosei's]].

Solving (1) together with $\Omega_{lu}=\hbar\omega$ for the in-plane momentum gives the dimensionally clean

$$
\boxed{\ k_\|^{2}=\frac{1}{\mathcal{D}_X}\Big[A_u\,(\hbar\omega-\mathcal{E}_g^{X})-\bar A_X\,(E-\hbar\omega_{X_6^-})\Big]\ }
\tag{6$'$}
$$

so that $D_{l\to u}\propto k_\|^{-1}\propto\big(E_{\max}-E\big)^{-1/2}$ — an **inverse-square-root edge in $E$ at the $k_\|=0$ end**.

### 2.3 Limits and the saddle line shape

$k_\|^2\ge0$ in (6′) gives the upper limit ($k_\|=0$):

$$
E_{\max}=\hbar\omega_{X_6^-}+\frac{A_u}{\bar A_X}\,(\hbar\omega-\mathcal{E}_g^{X}),
\qquad \frac{A_u}{\bar A_X}=\frac{m_{l\perp}}{m_{u\perp}+m_{l\perp}} .
\tag{8}
$$

Because the CEDS is **open**, the companion condition $k_\perp^{2}\ge0$ does **not** bound $E$ froibelow; the lower limit is set by occupation, not geometry. Rosei therefore cuts the integral at a thermal floor

$$
E_{\min}=-20\,k_BT,
$$

below which $[1-f(E,T)]\to0$ kills the integrand. Equation (7) becomes

$$
\mathcal{I}^{X}_{l\to u}(\hbar\omega,T)=\frac{1}{8\pi^{2}\hbar^{2}}\,\mathcal{F}_{l\to u}
\int_{-20k_BT}^{E_{\max}}\frac{[1-f(E,T)]}{\sqrt{\,\tfrac{\bar A_X}{\mathcal D_X}\,}\,\sqrt{E_{\max}-E}}\;dE .
$$

The integrable $1/\sqrt{E_{\max}-E}$ singularity sits at $E_{\max}$, but the **wide, thermally limited** lower range makes the EDJDOS look **steplike (boxlike)** in $E$ (Rosei Fig. 6). Integrating, the absorption rises **smoothly and roughly linearly** above $\hbar\omega_X=1.94$ eV and leaves a **nearly exponential sub-gap tail** from the $E<E_F$ thermal occupation — the defining X signature.

---

## 3. The L point — $d\to\mathrm{sp}$ minimum ($M_0$)

### 3.1 Dispersions

Identical construction at L, **except the upper band is an ellipsoid** (curves **up** in $k_\|$ — the one sign change from X):

$$
\begin{aligned}
E&=\hbar\omega_{u}=\hbar\omega_{L_6^-}+\frac{\hbar^{2}k_\perp^{2}}{2m_{u\perp}}+\frac{\hbar^{2}k_\|^{2}}{2m_{u\|}},\\[4pt]
E-\hbar\omega&=\hbar\omega_{l}=-\hbar\omega_{L^+}-\frac{\hbar^{2}k_\perp^{2}}{2m_{l\perp}}-\frac{\hbar^{2}k_\|^{2}}{2m_{l\|}} .
\end{aligned}
$$

Hence

$$
\Omega_{lu}=\mathcal{E}_g^{L}+\bar A_L k_\perp^{2}+\bar B_L k_\|^{2},
\qquad \bar A_L=A_u+A_l,\quad \bar B_L=B_u+B_l ,
$$

with $\mathcal{E}_g^{L}=\hbar\omega_{L_6^-}+\hbar\omega_{L^+}=2.45\ \text{eV}$. Now **both** coefficients are positive, so $\Omega_{lu}$ is a **minimum** ($M_0$): the CEDS is a **closed ellipsoid**, and transitions exist only for $\hbar\omega>\mathcal{E}_g^{L}$ — a sharp onset, no sub-gap tail.

### 3.2 Reduction

The Jacobian goes through verbatim with the new sign, giving the **difference** form of the curvature determinant (the $M_0$ signature):

$$
\boxed{\ \mathcal{D}_L=A_uB_l-A_lB_u
=\Big(\tfrac{\hbar^{2}}{2}\Big)^{2}\frac{m_{l\perp}m_{u\|}-m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}\ },
\qquad
\mathcal{F}^{L}_{l\to u}=\left(\frac{m_{l\perp}m_{u\|}-m_{l\|}m_{u\perp}}{m_{l\perp}m_{l\|}m_{u\perp}m_{u\|}}\right)^{-1/2}.
$$

$D_{l\to u}^{L}=(8\pi^{2}\hbar^{2})^{-1}\mathcal{F}^{L}_{l\to u}\,k_\|^{-1}$ as before, with

$$
k_\|^{2}=\frac{1}{\mathcal{D}_L}\Big[A_u(\hbar\omega-\mathcal{E}_g^{L})-\bar A_L(E-\hbar\omega_{L_6^-})\Big].
$$

### 3.3 Limits and the $M_0$ onset

Now **both** positivity conditions bound $E$, so the closed ellipsoid yields a **finite** energy window:

$$
\begin{aligned}
k_\|^{2}\ge0:\quad & E\le E_{\max}^{L}=\hbar\omega_{L_6^-}+\tfrac{A_u}{\bar A_L}(\hbar\omega-\mathcal{E}_g^{L}),\\[2pt]
k_\perp^{2}\ge0:\quad & E\ge E_{\min}^{L}=\hbar\omega_{L_6^-}+\tfrac{B_u}{\bar B_L}(\hbar\omega-\mathcal{E}_g^{L}).
\end{aligned}
$$

The EDJDOS keeps its $1/\sqrt{E_{\max}^{L}-E}$ singularity at the $k_\|=0$ edge, but is now integrated over the **shrinking finite window** of width

$$
E_{\max}^{L}-E_{\min}^{L}=\Big(\tfrac{A_u}{\bar A_L}-\tfrac{B_u}{\bar B_L}\Big)(\hbar\omega-\mathcal{E}_g^{L})\;\propto\;(\hbar\omega-\mathcal{E}_g^{L}).
$$

With $[1-f]\approx$ const across the narrow window near onset,

$$
\mathcal{I}^{L}_{l\to u}(\hbar\omega,T)\;\propto\;
\int_{E_{\min}^{L}}^{E_{\max}^{L}}\frac{dE}{\sqrt{E_{\max}^{L}-E}}
=2\sqrt{E_{\max}^{L}-E_{\min}^{L}}
\;\propto\;\sqrt{\hbar\omega-\mathcal{E}_g^{L}} .
$$

This is the textbook $M_0$ **inverse-square-root edge** $\epsilon_2\propto\sqrt{\hbar\omega-\mathcal{E}_g^L}$ — geometrically, the onset CEDS is tangent to the Fermi surface along the **neck circle** at L, giving a line (not a point) of band-edge transitions and hence the steep rise at $2.45$ eV.

---

## 4. Assembly

$$
\epsilon_2(\hbar\omega,T)=\frac{8\pi^{2}e^{2}\hbar^{4}}{3m^{2}(\hbar\omega)^{2}}
\Big[\,|P_X|^{2}\,N_X\,\mathcal{I}^{X}(\hbar\omega,T)+|P_L|^{2}\,N_L\,\mathcal{I}^{L}(\hbar\omega,T)\,\Big]
+\epsilon_2^{\text{Drude}} .
$$

Both edges are **band-5 → band-6** transitions in different BZ regions; only the ratio of matrix elements is fitted, $|P_X/P_L|^{2}=0.370$, with $N_X=6$, $N_L=8$. Rosei's static parameters: $\hbar\omega_{X_7^+}=1.770$ eV, $\hbar\omega_{L^+}=1.560$ eV, onsets $\hbar\omega_X=1.94$ eV and $\hbar\omega_L=2.45$ eV; optical masses and gaps from Christensen & Seraphin (ref: C&S 1971). The intraband Drude tail $\epsilon_2^{\text{Drude}}=A_D/(\hbar\omega)^3$ is added separately (not multiplied by the interband scale).

|                                | **X**                    | **L**                                |
| ------------------------------ | ------------------------------ | ------------------------------------------ |
| upper band$k_\|^2$ sign      | $-B_u$ (saddle)              | $+B_u$ (ellipsoid)                       |
| $\Omega_{lu}$ critical point | saddle,**open** CEDS     | minimum,**closed** CEDS              |
| curvature det.                 | $\mathcal D_X=A_uB_l+A_lB_u$ | $\mathcal D_L=A_uB_l-A_lB_u$             |
| $E$ range                    | $[-20k_BT,\;E_{\max}]$       | $[E_{\min}^L,\;E_{\max}^L]$ finite       |
| EDJDOS in$E$                 | steplike (box)                 | inverse-$\sqrt{}$                        |
| edge shape                     | smooth, sub-gap tail           | sharp$\sqrt{\hbar\omega-\mathcal E_g^L}$ |
| onset                          | 1.94 eV                        | 2.45 eV                                    |

---

## 5. Notes on Rosei's printed equations

Two of Rosei's display equations are dimensionally inconsistent **as printed** in the OCR'd source (ref 7 `.tex`); the clean forms derived above should be used.

1. **Eq (6).** As printed,
   $k_\|=\big(\hbar\omega-\hbar\omega_{X_7^+}+\tfrac{\hbar^2}{2m_{l\perp}}(\hbar\omega_{X_6^-}-E)-\tfrac{\hbar^2}{2m_{u\perp}}E\big)^{1/2}$,
   adds an energy to terms of the form $(\hbar^2/2m)\times$energy $\sim\mathrm{J^2m^2}$, and the bracket cannot be a $k_\|^{2}\sim\mathrm{m^{-2}}$. The coefficients must carry $2m/\hbar^2$, not $\hbar^2/2m$. The dimensionally correct result is (6′): $k_\|^{2}=\mathcal D_X^{-1}[A_u(\hbar\omega-\mathcal E_g^X)-\bar A_X(E-\hbar\omega_{X_6^-})]$.
2. **Eq (8).** Printed with **parallel** masses $m_{u\|}/(m_{l\|}-m_{u\|})$; the clean derivation gives the $k_\|=0$ edge with **perpendicular** masses, $A_u/\bar A_X=m_{l\perp}/(m_{u\perp}+m_{l\perp})$. The $\perp\!\leftrightarrow\!\|$ swap is the same class of transcription slip as in (6).
3. **Statistical factor.** Rosei carries only $[1-f(E,T)]$; the general (non-equilibrium-ready) weight is $f(\hbar\omega_l)[1-f(\hbar\omega_u)]$, reducing to Rosei's under $f(\hbar\omega_l)\to1$ for the filled $d$ initial state. Keep the full product for the emission and pulsed extensions.

> Check the printed PDF (`PDFs/7 - Rosei.pdf`) against items 1–2: if it also shows $\hbar^2/2m$ and $\|$-masses, these are Rosei's own shorthand for constants reshuffled into $\mathcal F$ and the scale; if not, they are Mathpix artifacts to patch in the `.tex`.

---

*Companion notes:* [[Equivalence of My Absorption Integral and Rosei's]] · [[Absorption Integral (Using Rosei's Notations)]] · `code/main/rosei_model_formulas.md` · `code/main/2_RoseiAnalysis.ipynb` · ref 7 (`TEXs/7 - Rosei`).
==========================================
