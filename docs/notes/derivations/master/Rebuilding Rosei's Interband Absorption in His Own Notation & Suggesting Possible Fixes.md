---
tags: [rosei, interband, epsilon2, emission, PL, gold, GRW]
---

- [ ] explain that the detour through energy space is to explicitly arrive at Rosei's exact expressions and assess their validity.
- [ ] distill exactly how better is the integration scheme for $k_{\parallel}$

# 1 Introduction & Remarks

This note rebuilds Rosei's interband $\epsilon_2(\hbar\omega,T)$ of gold from Fermi's Golden Rule, in his own notation, so that the ten numbered equations of Guerrisi, Rosei & Winsemius ("GRW", *Phys. Rev. B* **12**, 557 (1975)) all come out of one derivation. To do so we take a detour through energy space, changing variables in an explicit, rigorous and (hopefully) convincing manner. In the final section we offer an alternative integration route which is simpler and more stable.

Everything canters around Rosei's main equations (7) and (9). The former is the thermally weighted JDOS in energy space, the latter is the imaginary part of the interband permittivity.

$$\mathcal{J}_{l\to u}(\hbar\omega,T)=\int_{E_{\min}}^{E_{\max}} D_{l\to u}(E,\hbar\omega)\,[1-f(E,T)]\,\mathrm{d}E,\tag{7}$$
$$\epsilon_2(\hbar\omega,T)=\frac{8\pi^2 e^2\hbar^4}{3m^2(\hbar\omega)^2}\bigg[\,|P_X(l\to u)|^2\,\mathcal{J}_X(\hbar\omega,T)+|P_L(l\to u)|^2\,\mathcal{J}_L(\hbar\omega,T)\,\bigg]\tag{9}$$

**The plan:**
- Build $D_{l\to u}$, integrate it against occupation to get $\mathcal{J}$ (Eq. 7), drop that into $\epsilon_2$ (Eq. 9).
- §6 finishes the job the paper leaves to the reader: it assembles the one fully explicit energy-space integral, Eq. (11), gives the short numerical recipe for it, Eq. (12), and (§6.3) settles why evaluating (11) in $k_\parallel$ is bookkeeping, not apostasy.

**X vs L:** In this 1975 paper Rosei really only works out the $X$ point — the saddle and its sub-gap tail, the new physics here. The $L$ point he takes from his earlier papers (Refs. 10 and 12, i.e. Rosei 1974): he says outright that the $L$ procedure "will not be repeated here." Here we redo $L$ anyway with the same tools, so both edges sit in one place.

**Three equations look off:** Working through the algebra we noticed that three of the printed equations — (4), (6) and (8) — don't come out as written; most likely they are typos in the 1975 print. We flag each in a red box where it comes up, show the printed form, and suggest the corrected version.

**Signs and magnitudes.**
- Every level ($\hbar\omega_{X_6^-},\hbar\omega_{X_7^+},\hbar\omega_{L_6^-},\hbar\omega_{L^+}$) and every mass ($m_{u\perp},m_{u\parallel},m_{l\perp},m_{l\parallel}$) here is a *positive number*.
- Which way a band curves, and which side of $E_F$ a level sits on, is set entirely by the explicit $\pm$ in front of each term — never by a sign hidden in the symbol.
- (The C&S table we read curvatures off writes some masses with a minus, e.g. $m_{u\parallel}\simeq-0.40$; that only records a downward curvature, and here it becomes a positive $m_{u\parallel}=0.40$ with the minus moved out in front, as in Eq. (1).)

## 2  Fermi's Golden Rule in k-space

Standard starting point. Minimal coupling in the Coulomb gauge gives $\hat H_{\rm int}=(e/mc)\,\mathbf{A}\cdot\hat{\mathbf{p}}$ (the $A^2$ term is interband-inert). Photon momentum is negligible on the zone scale, so transitions are vertical. FGR summed over $\mathbf{k}$ (spin explicit), set equal to the dissipated power $\omega\epsilon_2E_0^2/8\pi$ per unit volume, gives
$$\epsilon_2(\omega)=\frac{4\pi^2e^2}{m^2\omega^2}\,\frac{2}{(2\pi)^3}\int_{\mathrm{BZ}}\mathrm{d}^3k\;\big|\hat{\boldsymbol{\epsilon}}\cdot\mathbf{p}_{ul}(\mathbf{k})\big|^{2}\,\delta\big(\hbar\omega_u(\mathbf{k})-\hbar\omega_l(\mathbf{k})-\hbar\omega\big)\,[f(\hbar\omega_l)-f(\hbar\omega_u)].$$
Matrix elements are taken to be constant in the region of interest, and the polarization is averaged over.
$$|P|^2\equiv\big|\langle u|\nabla|l\rangle\big|^2\quad(\text{dimension }\mathrm{length}^{-2}),\qquad\overline{\big|\hat{\boldsymbol{\epsilon}}\cdot\mathbf{p}_{ul}\big|^2}=\frac{\hbar^2|P|^2}{3},$$
this becomes, per critical-point family,
$$\epsilon_2(\hbar\omega,T)=\frac{4\pi^2e^2\hbar^2}{3m^2\omega^2}\cdot\frac{2}{(2\pi)^3}\,N\,|P|^2\int\limits_{\text{half-nbhd}}\mathrm{d}^3k\;\delta\big(\Omega_{lu}(\mathbf{k})-\hbar\omega\big)\,[f(E-\hbar\omega)-f(E)]\big|_{E=\hbar\omega_u(\mathbf{k})},\tag{$\star$}$$

where:
- $N$ counts equivalent *half*-neighborhoods ($N_X=6$, $N_L=8$) — paired with the half-space density of states below, or a factor of 2 goes missing.
- The occupation factor is the full $f(E-\hbar\omega)-f(E)$; for the deep $d$ bands it reduces to Rosei's $[1-f]$, kept general here for the non-equilibrium case ($f^S$, $f^P$). This is the *absorption* weight — a difference; the *emission* (PL) weight is a product, $f(E)[1-f(E-\hbar\omega)]$. Appendix B derives both, shows they coincide up to a Bose–Einstein factor in equilibrium, and shows that factor breaking out of equilibrium.

## 3  The X point — the part Rosei actually derives

### 3.1 Setup & Change of Variables
Rosei's parabolic band pair at $X$, exactly as they write it (energies from $E_F$; $k_\parallel$ runs along $\Delta=\Gamma X$, $k_\perp$ lies in the zone face). The upper $X_6^-$ ($sp$) band curves *up* in the face and *down* along $\Delta$ — a saddle:

$$
\begin{align}
E=\hbar\omega_u(\mathbf{k})&=+\hbar\omega_{X_6^-}+\frac{\hbar^2k_\perp^2}{2m_{u\perp}}-\frac{\hbar^2k_\parallel^2}{2m_{u\parallel}}\tag{1} \\
E-\hbar\omega=\hbar\omega_l(\mathbf{k})&=-\hbar\omega_{X_7^+}-\frac{\hbar^2k_\perp^2}{2m_{l\perp}}-\frac{\hbar^2k_\parallel^2}{2m_{l\parallel}}\tag{2}
\end{align}
$$

Vertical transitions of energy $\hbar\omega$ live on the constant-energy-difference surface (CEDS),
$$\Omega_{lu}(\mathbf{k})-\hbar\omega=\hbar\omega_u(\mathbf{k})-\hbar\omega_l(\mathbf{k})-\hbar\omega=0.\tag{3}$$
Subtract (2) from (1), with the curvature shorthands $A_i=\hbar^2/2m_{i\perp}$, $B_i=\hbar^2/2m_{i\parallel}$:

$$\Omega_{lu}=\mathcal{E}_g^{X}+\bar{A}_X\,k_\perp^2+\bar{B}_X\,k_\parallel^2,\qquad\bar{A}_X=A_u+A_l>0,\qquad\bar{B}_X=B_l-B_u.$$
> [!NOTE] Remark
> The sign of $\bar{B}_X$ decides the whole $X$ story.
> - Rosei's own apparatus — the open CEDS, the sub-gap tail, the $-20k_BT$ floor of their Eq. (7), the step-like onset near $1.8$ eV — only makes sense if $$\bar{B}_X<0 \quad \Leftrightarrow \quad m_{u\parallel}<m_{l\parallel}$$ the $sp$ band falls along $\Delta$ *faster* than the $d$ band (the "flat-$d$" picture).
> - The main text follows this branch; our own C&S extraction currently disagrees on this one assignment, which we flag honestly in the mass-fork note at the end of §3.3 rather than bury.

Setting
$$u=k_\perp^2,\qquad v=k_\parallel^2\qquad(u,v\ge0).$$
equations $(1)$ and $(3)$ become
$$
\begin{align}
\hbar\omega-\mathcal{E}_g^{X}&=\bar{A}_X k_\perp^2+\bar{B}_X k_\parallel^2&&\Rightarrow\bar{A}_X\,u+\bar{B}_X\,v \\
E-\hbar\omega_{X_6^-}&=A_u k_\perp^2-B_u k_\parallel^2 &&\Rightarrow A_u\,u-B_u\,v
\end{align}
$$

Stacking those two equations *is* the construction of the transition matrix $M$, and the Jacobian of the map is nothing but its determinant:
$$\begin{pmatrix} E-\hbar\omega_{X_6^-}\\[2pt] \hbar\omega-\mathcal{E}_g^{X}\end{pmatrix}=\underbrace{\begin{pmatrix} A_u & -B_u\\[2pt] \bar{A}_X & \bar{B}_X\end{pmatrix}}_{M}\begin{pmatrix} u\\ v\end{pmatrix},\qquad\det M=A_u\bar{B}_X+B_u\bar{A}_X=A_uB_l+A_lB_u\equiv\mathcal{D}_X>0.$$
So $\mathcal{D}_X\equiv\det M$ is exactly the Jacobian that will collapse the two $\delta$-functions in the definition of $D$ below; it is built entirely from (1) and (3). Note it is positive for *either* sign of $\bar{B}_X$. Inverting the $2\times2$ system,

$$u=\frac{\bar{B}_X\,(E-\hbar\omega_{X_6^-})+B_u(\hbar\omega-\mathcal{E}_g^{X})}{\mathcal{D}_X},\qquad v=k_\parallel^2=\frac{A_u(\hbar\omega-\mathcal{E}_g^{X})-\bar{A}_X\,(E-\hbar\omega_{X_6^-})}{\mathcal{D}_X}.$$

From $k_{\parallel}$ we can identify the analogue of Rosei's Eq. (6) in a primed tag.
$$k_\parallel^{2}=\frac{2\mathcal{F}^{2}}{\hbar^{2}}\left[\frac{\hbar\omega-\hbar\omega_{X_7^+}-E}{m_{u\perp}}+\frac{\hbar\omega_{X_6^-}-E}{m_{l\perp}}\right].\tag{6$'$}$$

> [!warning] Printed Eq. (6) is inconsistent
> Rosei prints this line as
> $$k_\parallel=\left(\hbar\omega-\hbar\omega_{X_7^+}+\frac{\hbar^{2}}{2m_{l\perp}}\big(\hbar\omega_{X_6^-}-E\big)-\frac{\hbar^{2}}{2m_{u\perp}}E\right)^{1/2}.\tag{6, as printed}$$
> The problem: this sets a wavevector $k_\parallel$ equal to the square root of a sum of *energies*, and inside the bracket adds a bare energy $\hbar\omega-\hbar\omega_{X_7^+}$ to terms of the form $(\hbar^2/2m)\times$energy — mismatched units throughout. The coefficients read $\hbar^2/2m$ where they should read $2m/\hbar^2$, for the bracket to come out as $k_\parallel^2\sim\mathrm{length}^{-2}$.
>
> Three small fixes turn the printed line into $(6')$:
> - square the left-hand side ($k_\parallel\to k_\parallel^2$);
> - invert the coefficients and pull out the overall $2\mathcal{F}^2/\hbar^2$;
> - restore the missing $1/m_{u\perp}$ on the first term.
>
> The three numerator slots then line up with the print term by term — confirmation that $(6')$ is what was meant: most likely a typo, but a disabling one, since the printed formula is unusable as written.

### 3.2  The energy-distributed JDOS

Now the central object, built rather than dropped on the reader. In the Golden-Rule expression (★), the $k$-integral already carries *one* $\delta$-function — energy conservation, $\delta(\Omega_{lu}(\mathbf{k})-\hbar\omega)$ — alongside the occupation factor $[f(E-\hbar\omega)-f(E)]$, read at the final-state energy $E=\hbar\omega_u(\mathbf{k})$ and so drifting from point to point across the surface. That final energy is where temperature enters (it's the argument of $f$), so before touching any geometry we *sort the transitions by their final energy $E$*. The clean way: slip in the identity

$$1=\int\mathrm{d}E\;\delta\big(\hbar\omega_u(\mathbf{k})-E\big)$$

into (★). This new $\delta$ does nothing but *label* each $\mathbf{k}$ by its upper-band energy; it lets us carry the occupation outside the $k$-integral as a plain function of $E$,

$$\begin{align}
&\int_{k_\parallel>0}\mathrm{d}^3k\;\delta(\Omega_{lu}-\hbar\omega)\,[f(E-\hbar\omega)-f(E)]\big|_{E=\hbar\omega_u} \\
=&\int\mathrm{d}E\;[f(E-\hbar\omega)-f(E)]\underbrace{\int_{k_\parallel>0}\mathrm{d}^3k\;\delta(\hbar\omega_u-E)\,\delta(\Omega_{lu}-\hbar\omega)}_{(2\pi)^3\,D_{l\to u}(E,\hbar\omega)}.
\end{align}$$

The inner integral now carries *both* $\delta$'s — energy conservation, already present, and the final-energy one just inserted — and is Rosei's central object: the number of $l\to u$ transitions per unit crystal volume, per unit final energy $E$, per unit transition energy $\hbar\omega$ (one half-neighborhood, one spin):

$$D_{l\to u}(E,\hbar\omega)\equiv\frac{1}{(2\pi)^3}\int_{k_\parallel>0}\mathrm{d}^3k\;\delta\big(\hbar\omega_u(\mathbf{k})-E\big)\,\delta\big(\Omega_{lu}(\mathbf{k})-\hbar\omega\big).$$

Both $\delta$'s have a traceable origin: the energy-conservation one already sat in (★); the other is the resolution of identity, binning transitions by final energy $E$. That binning is what makes $D$ *energy-distributed*, and it is what later lets $\mathcal{J}$ (Eq. 7) weight each $E$ by its own occupation $[1-f(E,T)]$.

Worth reducing this all the way: it is where both $\mathcal{D}_X$ and $\mathcal{F}$ come from. Axial symmetry about $\Gamma X$ gives $\mathrm{d}^3k=2\pi k_\perp\mathrm{d}k_\perp\,\mathrm{d}k_\parallel$; in the squared variables $k_\perp\mathrm{d}k_\perp=\tfrac12\mathrm{d}u$, $\mathrm{d}k_\parallel=\mathrm{d}v/(2\sqrt v)$, so the measure becomes

$$\frac{1}{(2\pi)^3}\int_{k_\parallel>0}\mathrm{d}^3k=\frac{1}{(2\pi)^3}\,\frac{\pi}{2}\int_0^\infty\mathrm{d}u\int_0^\infty\frac{\mathrm{d}v}{\sqrt v}=\frac{1}{16\pi^2}\int_0^\infty\mathrm{d}u\int_0^\infty\frac{\mathrm{d}v}{\sqrt v}.$$

The two $\delta$-functions are exactly the two rows of the transition matrix: arguments $A_u u-B_u v-(E-\hbar\omega_{X_6^-})$ (top) and $\bar{A}_X u+\bar{B}_X v-(\hbar\omega-\mathcal{E}_g^{X})$ (bottom). Linear $\delta$'s in $(u,v)$ collapse onto the unique solution $(u_*,v_*)$ — the inversion above — divided by the Jacobian modulus $|\det M|=\mathcal{D}_X$:

$$\delta\!\big(A_u u-B_u v-(E-\hbar\omega_{X_6^-})\big)\,\delta\!\big(\bar{A}_X u+\bar{B}_X v-(\hbar\omega-\mathcal{E}_g^{X})\big)=\frac{1}{\mathcal{D}_X}\,\delta(u-u_*)\,\delta(v-v_*).$$

Doing the $u,v$ integrals sets $\sqrt{v_*}=k_\parallel(E,\hbar\omega)$ from $(6')$, and everything telescopes to
$$D_{l\to u}(E,\hbar\omega)=\frac{1}{16\pi^2\,\mathcal{D}_X}\,\frac{1}{k_\parallel(E,\hbar\omega)}.$$

**This is the whole result of the reduction: it contains only $\mathcal{D}_X$ and $k_\parallel$ — no $\mathcal{F}$ yet.** Rosei's $\mathcal{F}_{l\to u}$ is not an independent input; it is a repackaging of $\mathcal{D}_X$, manufactured right here. Expand $\mathcal{D}_X$ in the masses, $A_i=\hbar^2/2m_{i\perp}$, $B_i=\hbar^2/2m_{i\parallel}$:

$$\mathcal{D}_X=A_uB_l+A_lB_u=\Big(\frac{\hbar^2}{2}\Big)^{2}\left[\frac{1}{m_{u\perp}m_{l\parallel}}+\frac{1}{m_{l\perp}m_{u\parallel}}\right]=\Big(\frac{\hbar^2}{2}\Big)^{2}\frac{m_{l\perp}m_{u\parallel}+m_{l\parallel}m_{u\perp}}{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}}.$$

Define $\mathcal{F}_{l\to u}\equiv\hbar^2/(2\sqrt{\mathcal{D}_X})$ as pure shorthand. Substituting the expansion, $\hbar^2/2$ cancels top and bottom and the mass form falls out — Rosei's Eq. (5), now derived rather than assumed:

$$\mathcal{F}_{l\to u}\equiv\frac{\hbar^2}{2\sqrt{\mathcal{D}_{X}}}=\left[\frac{m_{l\perp}m_{u\parallel}+m_{l\parallel}m_{u\perp}}{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}}\right]^{-1/2}.\tag{5}$$

Reading the same definition the other way, $\mathcal{D}_X=\hbar^4/(4\mathcal{F}_{l\to u}^2)$, and substituting it back into the intermediate result rewrites the EDJDOS in Rosei's own notation:

$$\boxed{\;D_{l\to u}(E,\hbar\omega)=\frac{1}{16\pi^2\,\mathcal{D}_{X}}\,\frac{1}{k_\parallel(E,\hbar\omega)}=\frac{\mathcal{F}^2_{l\to u}}{4\pi^2\hbar^4}\,\frac{1}{k_\parallel(E,\hbar\omega)}\;}\tag{4$'$}$$

supported on $u,v\ge0$, with $k_\parallel$ from $(6')$. To be clear:
- $\mathcal{F}$ is never an input — the Jacobian hands us $\mathcal{D}_X$; (5) just renames it.
- $\mathcal{F}$ appears in $(4')$ only because we chose to write $\mathcal{D}_X$ that way.
- Eq. (5) comes out untouched; Eq. (4) does not.

> [!warning] Printed Eq. (4) is off by a constant — likely a typo
> Rosei prints
> $$D_{l\to u}(E,\hbar\omega)=\big(8\pi^2\hbar^2\big)^{-1}\,\mathcal{F}_{l\to u}\,k_\parallel^{-1}.\tag{4, as printed}$$
> Subtler than a dropped symbol: if $|P|^2$ is a squared gradient (momentum) matrix element, {printed (4), printed (9)} don't balance dimensionally, while $(4')$ — forced, with nothing left to choose, by the definition of $D$ — closes the FGR chain exactly through to $\epsilon_2$ (§5). The two forms differ only by
> $$\frac{\text{printed (4)}}{\text{correct }(4')}=\frac{2\mathcal{F}_{l\to u}}{\hbar^2},$$
> a constant for each critical point (typesetting slip or convention mismatch, unclear which — but it changes nothing):
> - a per-critical-point constant can't bend a line shape, so it's absorbed into the fitted strength $S=\mathcal{F}|P|^2$ of Eq. (10);
> - every published number keeps its meaning; only the bookkeeping between $D$, $\mathcal{F}$, $|P|^2$ shifts;
> - $(4')$ is simply the form consistent with the definition of $D$.

### 3.3  Topology, integration limits, and GRW (7)–(8)

Now the part that makes $X$ physically interesting. On Rosei's branch $\bar{B}_X<0$ the CEDS is an *open* hyperboloid at every $\hbar\omega$: transitions exist on both sides of $\mathcal{E}_g^{X}$, and $E$ decreases without bound away from the top edge ($\mathrm{d}E\propto-\mathcal{D}_X\,\mathrm{d}v<0$). Nothing bounds the window from below geometrically, so it is cut only by *occupation* — the practical thermal floor $E_{\min}=-20k_BT$, below which $[1-f]\to0$ kills the integrand.

The upper edge $E_{\max}(\hbar\omega)$ is geometric and changes character at the gap. Above it ($\hbar\omega\ge\mathcal{E}_g^{X}$) the edge is the $k_\parallel\to0$ circle ($v=0$), where $D_{l\to u}$ diverges as an inverse square root. Below it ($\hbar\omega<\mathcal{E}_g^{X}$) that circle no longer exists ($v>0$ everywhere on the CEDS); the edge is instead the $k_\perp=0$ point ($u=0$), where $k_\parallel$ — and $D_{l\to u}$ — stay finite. Both cases in one piece:

$$E_{\max}(\hbar\omega)=\hbar\omega_{X_6^-}+\begin{cases}\dfrac{A_u}{\bar{A}_X}\,(\hbar\omega-\mathcal{E}_g^{X})=\dfrac{m_{l\perp}}{m_{u\perp}+m_{l\perp}}\,(\hbar\omega-\mathcal{E}_g^{X}), & \hbar\omega\ge\mathcal{E}_g^{X},\\[12pt]-\dfrac{B_u}{|\bar{B}_X|}\,(\mathcal{E}_g^{X}-\hbar\omega)=\dfrac{m_{l\parallel}}{m_{u\parallel}-m_{l\parallel}}\,(\mathcal{E}_g^{X}-\hbar\omega), & \hbar\omega<\mathcal{E}_g^{X},\end{cases}\tag{8$'$}$$

whose lower line (the sub-gap edge) is Rosei's Eq. (8).

> [!warning] Printed Eq. (8) has two subscripts swapped — again likely a typo
> Rosei prints the upper limit as
> $$\begin{align}E_{\max}&=\hbar\omega_{X_6^-}+\big(\hbar\omega_{X_7^+}+\hbar\omega_{X_6^-}-\hbar\omega\big)\,\frac{m_{u\parallel}}{m_{l\parallel}-m_{u\parallel}} \\
&=\hbar\omega_{X_6^-}+\big(\mathcal{E}_g^{X}-\hbar\omega\big)\,\frac{m_{u\parallel}}{m_{l\parallel}-m_{u\parallel}}.\tag{8, as printed}\end{align}$$
> - **The swap:** print carries $m_{u\parallel}/(m_{l\parallel}-m_{u\parallel})$ where the clean derivation gives $m_{l\parallel}/(m_{u\parallel}-m_{l\parallel})$ — one consistent $m_{u\parallel}\leftrightarrow m_{l\parallel}$ swap, specific to (8): the subscripts of (6) aren't swapped, so it isn't the same slip repeated.
> - **The tell:** on the $\bar{B}_X<0$ branch $m_{u\parallel}<m_{l\parallel}$, so the printed denominator $m_{l\parallel}-m_{u\parallel}>0$ sends $E_{\max}$ *above* $\hbar\omega_{X_6^-}$ as $\hbar\omega$ drops below the gap — but the sub-gap CEDS has no states up there. $(8')$ instead puts the sub-gap edge sensibly *below* $\hbar\omega_{X_6^-}$, which is what makes the tail work.

That finite sub-gap edge is why the $X$ onset is *step-like* (Rosei's own word) rather than a sharp divergence: at $T=0$ absorption switches on when the sub-gap edge crosses $E_F$,

$$\hbar\omega_{\rm on}=\mathcal{E}_g^{X}-\hbar\omega_{X_6^-}\,\frac{m_{l\parallel}-m_{u\parallel}}{m_{l\parallel}}\;\simeq\;1.94-0.17\times\frac{0.40-0.15}{0.40}=1.83\ \text{eV},$$

the piezomodulation threshold, with the low-energy tail filling $1.83$–$1.94$ eV purely geometrically — no broadening put in by hand.

And finally the thermally weighted integral, verbatim as Rosei writes it — Eq. (7), the first of the two headline results from the opening:

$$\mathcal{J}(\hbar\omega,T)=\int_{E_{\min}}^{E_{\max}} D_{l\to u}(E,\hbar\omega)\,[1-f(E,T)]\,\mathrm{d}E,\tag{7}$$

with $D_{l\to u}$ from $(4')$, $E_{\max}$ from $(8')$, $E_{\min}=-20k_BT$, and $[1-f]\to f(E-\hbar\omega)-f(E)$ out of equilibrium. (Fully substituted — no symbols left to chase — this is Eq. (11) in §6.)

> [!note] Remark — the one mass assignment I'm not sure of at $X$
> Honesty check, since it flips a sign.
> - My extraction of the C&S Fig. 5 curvatures gives $m_{u\parallel}=0.40$, $m_{l\parallel}=0.15$ — the opposite $\parallel$ ordering to Rosei's branch — giving $\bar{B}_X>0$: a *closed* window $\big[\hbar\omega_{X_6^-}-\tfrac{B_u}{\bar{B}_X}(\hbar\omega-\mathcal{E}_g^{X}),\;E_{\max}\big]$, no geometric sub-gap tail, and a $\sqrt{\hbar\omega-\mathcal{E}_g^{X}}$ onset sitting exactly at $\mathcal{E}_g^{X}$.
> - Above the gap both branches give the same line shape and singular edge $(8')$ — the $\parallel$ masses enter only through $\mathcal{F}_X$, absorbed by the fit into $S_X$ — so an optical fit alone can't distinguish them; only the sub-gap physics and extracted $|P_X|^2$ can.
> - Both orderings make the $d$ band the lighter one, against the flat-$d$ prior, so a transcription swap in my own mass table is the likeliest fix.
> - Until C&S Fig. 5 is re-measured, this note follows Rosei ($\bar{B}_X<0$) and flags every spot where the branch matters.

## 4  The L point — the part Rosei borrows

**Rosei does not derive $L$ in the 1975 paper.** He states plainly that the procedure "has been presented in a number of papers and will not be repeated here," citing his own earlier work (Refs. 10, 12; the machinery is Rosei 1974, *Phys. Rev. B* **10**, 474) — so while $X$ was fresh work, $L$ is inherited wholesale. We re-derive it anyway: the same squared-momentum substitution gives it in three lines, putting both edges in one framework and showing exactly where $L$ differs from $X$ — in essentially one sign.

At $L$ the $L_6^-$ conduction band is a *minimum* in both local directions ($k_\parallel$ along $\Gamma L$) — not a saddle — and the top $d$ band is again a maximum:

$$\begin{aligned}E&=\hbar\omega_u(\mathbf{k})=\hbar\omega_{L_6^-}+\frac{\hbar^2k_\perp^2}{2m_{u\perp}}+\frac{\hbar^2k_\parallel^2}{2m_{u\parallel}},\\[2pt]E-\hbar\omega&=\hbar\omega_l(\mathbf{k})=-\hbar\omega_{L^+}-\frac{\hbar^2k_\perp^2}{2m_{l\perp}}-\frac{\hbar^2k_\parallel^2}{2m_{l\parallel}}.\end{aligned}$$

The only change from $X$ is the sign of the upper-band $k_\parallel^2$ term: $+$ here versus $-$ at $X$ (Eq. 1). That one flip cascades through everything:

$$\Omega_{lu}=\mathcal{E}_g^{L}+\bar{A}_L k_\perp^2+\bar{B}_L k_\parallel^2,\qquad\bar{B}_L=B_u+B_l>0\ \ \text{unconditionally.}$$

Because $\bar{B}_L>0$ regardless of the masses, the CEDS is a *closed ellipsoid* existing only for $\hbar\omega\ge\mathcal{E}_g^{L}$: **there is no sub-gap tail at $L$** — the sharp-versus-tailed contrast between the two edges is baked in right here. The straight-line system is the same transition matrix with $-B_u\to+B_u$, $\bar{B}_X\to\bar{B}_L$; the curvature determinant is now a *difference* rather than a sum — the ellipsoid's fingerprint:

$$\mathcal{D}_L=A_uB_l-A_lB_u,\qquad\mathcal{F}_L=\frac{\hbar^2}{2\sqrt{|\mathcal{D}_L|}}=\left[\frac{\big|m_{l\perp}m_{u\parallel}-m_{l\parallel}m_{u\perp}\big|}{m_{l\perp}m_{l\parallel}m_{u\perp}m_{u\parallel}}\right]^{-1/2}.$$

For gold the two products are $m_{l\perp}m_{u\parallel}=0.70\times0.12=0.084$ and $m_{l\parallel}m_{u\perp}=1.03\times0.24=0.247$, so $\boxed{\mathcal{D}_L<0}$. Running the inversion with the sign of $\mathcal{D}$ reversed (which flips both positivity inequalities) gives

$$k_\parallel^2=\frac{\bar{A}_L}{|\mathcal{D}_L|}\big(E-E_{\min}\big),\qquad D_{l\to u}(E,\hbar\omega)=\frac{1}{16\pi^2|\mathcal{D}_L|\,k_\parallel}=\frac{\mathcal{F}_L^2}{4\pi^2\hbar^4 k_\parallel},$$

$$E_{\min}=\hbar\omega_{L_6^-}+\frac{A_u}{\bar{A}_L}(\hbar\omega-\mathcal{E}_g^{L}),\qquad E_{\max}=\hbar\omega_{L_6^-}+\frac{B_u}{\bar{B}_L}(\hbar\omega-\mathcal{E}_g^{L}),$$

with slopes $A_u/\bar{A}_L=0.745$, $B_u/\bar{B}_L=0.896$ for Au. **The punchline of the $X$ vs. $L$ comparison:** the $k_\parallel\to0$ edge — the inverse-square-root singularity in $D_{l\to u}$ — is now the *lower* limit $E_{\min}$, exactly opposite $X$. Nothing physical was added; the swap is purely because $\mathcal{D}_L<0$ while $\mathcal{D}_X>0$. The $L$ line shape is then

$$\mathcal{J}_L(\hbar\omega,T)=\int_{E_{\min}}^{E_{\max}} D_{l\to u}(E,\hbar\omega)\,[1-f(E,T)]\,\mathrm{d}E,$$

and its integrable divergence sits right on the onset edge. So: $L$ is *sharp and strong*, $X$ *soft and tailed* — Rosei's "splitting of the interband absorption edge," now both halves from one formula set instead of two separate papers.

> [!note] Remark — a tension in the $L$ level scheme, recorded on purpose
> - Fitted levels ($\mathcal{E}_g^{L}=2.45$, $\hbar\omega_{L^+}=1.56\Rightarrow\hbar\omega_{L_6^-}=+0.89$ eV) put the whole $L$ window *above* $E_F$: the Fermi factor is inert at $L$, and the model's $L$ temperature dependence enters only through broadening and gap shift.
> - But Rosei's own qualitative picture of the $L$ singularity — the onset CEDS tangent to the Fermi surface along the neck — needs $L_6^-$ *below* $E_F$. Both can't hold in one parabolic model.
> - The fitted scheme is what the code implements; the tension is recorded here rather than papered over.

## 5  Putting it together: GRW (9)–(10)

Now we cash in: insert the revised EDJDOS $(4')$ into the FGR result (★). The bridge is the definition of $D$ itself — $\int\mathrm{d}^3k\,\delta(\Omega-\hbar\omega)[\cdots]=(2\pi)^3\int\mathrm{d}E\,D_{l\to u}(E,\hbar\omega)[\cdots]$ per half-neighborhood — so the $(2\pi)^3$ cancels, and

$$\epsilon_2(\hbar\omega,T)=\frac{4\pi^2e^2\hbar^2}{3m^2\omega^2}\cdot2\cdot\sum_{i=X,L}N_i\,|P_i|^2\,\mathcal{J}_i(\hbar\omega,T)$$

which tidies to

$$\boxed{\;\epsilon_2(\hbar\omega,T)=\frac{8\pi^2e^2\hbar^4}{3m^2(\hbar\omega)^2}\sum_{i=X,L}N_i\,|P_i|^2\,\mathcal{J}_i(\hbar\omega,T)\;}\tag{9}$$

— Rosei's Eq. (9), the second headline result, recreated with no leftover constant. That clean landing needs three things at once:
- $|P|^2$ is the squared $\nabla$ matrix element of §2;
- $D_{l\to u}$ is the revised $(4')$, not the printed one;
- spin (the explicit 2) and the half-point counts $N_X=6$, $N_L=8$ are kept where shown.

(Rosei leaves the $N_i$ implicit, so the fitted $|P_i|^2$ really means $N_i|P_i|^2$ up to normalization — harmless for the quoted ratio.) The quantities the data actually fix are the strengths,

$$S_X=\mathcal{F}_X|P_X|^2,\qquad S_L=\mathcal{F}_L|P_L|^2,\tag{10}$$

with $|P_X/P_L|^2=0.370$ from the fit to Johnson–Christy. Under the revised (4) the combination the data really pin down is $N_i\mathcal{F}_i^2|P_i|^2$; it maps onto the printed $S_i$ through exactly the constant $2\mathcal{F}_i/\hbar^2$ of the note below — the published numbers keep their meaning.

**Parameters** (levels: Rosei's fit; masses: C&S, with the $X$ row subject to the mass-fork note in §3.3; $\mathcal{F}$ in units of the free-electron mass):

| | $\mathcal{E}_g$ (eV) | upper level (eV) | lower level (eV) | $m_{u\perp}$ | $m_{u\parallel}$ | $m_{l\perp}$ | $m_{l\parallel}$ |
|---|---|---|---|---|---|---|---|
| $X$ (GRW branch) | 1.94 | $\hbar\omega_{X_6^-}=0.17$ | $\hbar\omega_{X_7^+}=1.77$ | 0.19 | 0.15 | 0.31 | 0.40 |
| $L$ | 2.45 | $\hbar\omega_{L_6^-}=0.89$ | $\hbar\omega_{L^+}=1.56$ | 0.24 | 0.12 | 0.70 | 1.03 |

| | $\mathcal{D}$ (units $(\hbar^2/2m)^2$) | $\mathcal{F}/m$ | window slopes | singular edge |
|---|---|---|---|---|
| $X$ | $+34.7$ | 0.170 | $E_{\max}$ (above gap): 0.38–0.62 $^{\dagger}$ | upper ($k_\parallel\to0$) |
| $L$ | $-7.86$ | 0.357 | $E_{\min}$: 0.745, $E_{\max}$: 0.896 | lower ($k_\parallel\to0$) |

$^{\dagger}$ $0.38$ with my $\perp$ assignment ($m_{u\perp}=0.31$), $0.62$ fully $u\leftrightarrow l$ swapped ($m_{u\perp}=0.19$); $\mathcal{F}_X$ is invariant under the full swap. $\mathcal{D}_X$, $\mathcal{F}_X$ are quoted for the full-swap/Rosei assignment; mine gives the same values by the symmetry of (5).

**Scorecard — the ten Rosei equations, one by one** (three flagged rows to watch):

| GRW  | here   | status            | issue as printed                                                                                                        |
| ---- | ------ | ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| (1)  | (1)    | recreated         | —                                                                                                                       |
| (2)  | (2)    | recreated         | —                                                                                                                       |
| (3)  | (3)    | recreated         | —                                                                                                                       |
| (4)  | $(4')$ | **suggested fix** | prefactor $(8\pi^2\hbar^2)^{-1}\mathcal{F}\to(4\pi^2\hbar^4)^{-1}\mathcal{F}^2$; off by $2\mathcal{F}/\hbar^2$ (const.) |
| (5)  | (5)    | recreated         | —                                                                                                                       |
| (6)  | $(6')$ | **suggested fix** | dimensionally impossible as printed                                                                                     |
| (7)  | (7)    | recreated         | occupation generalized                                                                                                  |
| (8)  | $(8')$ | **suggested fix** | $u\parallel\leftrightarrow l\parallel$ subscripts swapped                                                               |
| (9)  | (9)    | recreated         | $N_i$ made explicit                                                                                                     |
| (10) | (10)   | recreated         | units note (see the callout below)                                                                                      |

> [!note] Remark — the constant that hides the (4) discrepancy
> Collecting the (4) discussion in one place, since it's the subtle one.
> - Rosei prints $D_{l\to u}=(8\pi^2\hbar^2)^{-1}\mathcal{F}/k_\parallel$; the definition of $D$ forces $D_{l\to u}=(16\pi^2\mathcal{D})^{-1}/k_\parallel=\mathcal{F}^2/(4\pi^2\hbar^4 k_\parallel)$.
> - Their ratio is $2\mathcal{F}/\hbar^2$, a pure constant per critical point — it can't touch any line shape, and is absorbed once and for all into the fitted strength $S=\mathcal{F}|P|^2$ of Eq. (10).
> - That's why the discrepancy is easy to miss and costs nothing physically — but the assembly only reproduces Eq. (9) with no leftover constant if the revised form $(4')$ is used, as here.

## 6  The assembled integral, and how to compute it

Everything so far was parts and assembly instructions — that was the point of tracking Rosei's equations one by one. But neither the paper nor the sections above put the finished object on the page: the explicit, fully-substituted energy-space integral a computer would actually evaluate. Here it is, followed by the one change of variable that makes evaluating it trivial.

### 6.1  The energy-space integral in full glory

Insert the EDJDOS $(4')$ into (9); the $\hbar^4$'s cancel, and with the occupation written in its general form $\Delta f(E)\equiv f(E-\hbar\omega)-f(E)$ (Rosei's equilibrium $d$-band case: $\Delta f\to[1-f]$):

$$\boxed{\;\epsilon_2(\hbar\omega,T)=\frac{2e^{2}}{3m^{2}(\hbar\omega)^{2}}\sum_{i=X,L}N_i\,\mathcal{F}_i^{2}\,|P_i|^{2}\int_{E_{\min}^{(i)}}^{E_{\max}^{(i)}}\frac{\Delta f(E,T)}{k_\parallel^{(i)}(E,\hbar\omega)}\,\mathrm{d}E\;}\tag{11}$$

with the two edge functions fully written out — $X$ is $(6')$, $L$ is the same inversion run in §4:

$$k_\parallel^{X}(E,\hbar\omega)=\frac{\sqrt{2}\,\mathcal{F}_X}{\hbar}\left[\frac{(\hbar\omega-\hbar\omega_{X_7^+})-E}{m_{u\perp}}+\frac{\hbar\omega_{X_6^-}-E}{m_{l\perp}}\right]^{1/2},$$

$$k_\parallel^{L}(E,\hbar\omega)=\frac{\sqrt{2}\,\mathcal{F}_L}{\hbar}\left[\frac{E-(\hbar\omega-\hbar\omega_{L^+})}{m_{u\perp}}+\frac{E-\hbar\omega_{L_6^-}}{m_{l\perp}}\right]^{1/2}.$$

The same bracket twice, every slot sign-reversed — the single sign of §4, one last time. At $X$ the bracket *falls* with $E$, so the $k_\parallel\to0$ singularity sits at the *top* of the window; at $L$ it *rises*, and the singularity sits at the *bottom*. The windows are exactly where the inversion gives $u,v\ge0$, so inside them the brackets are automatically nonnegative:

|                                        | $E_{\min}$                                                                 | $E_{\max}$                                                                 | edge behaviour                         |
| -------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------- |
| $X$, $\hbar\omega\ge\mathcal{E}_g^{X}$ | occupation floor, $-20k_BT$                                                | $\hbar\omega_{X_6^-}+\dfrac{A_u}{\bar A_X}(\hbar\omega-\mathcal{E}_g^{X})$ | $1/\sqrt{\ }$ divergence at $E_{\max}$ |
| $X$, $\hbar\omega<\mathcal{E}_g^{X}$   | occupation floor, $-20k_BT$                                                | sub-gap line of $(8')$                                                     | finite everywhere                      |
| $L$, $\hbar\omega\ge\mathcal{E}_g^{L}$ | $\hbar\omega_{L_6^-}+\dfrac{A_u}{\bar A_L}(\hbar\omega-\mathcal{E}_g^{L})$ | $\hbar\omega_{L_6^-}+\dfrac{B_u}{\bar B_L}(\hbar\omega-\mathcal{E}_g^{L})$ | $1/\sqrt{\ }$ divergence at $E_{\min}$ |
| $L$, $\hbar\omega<\mathcal{E}_g^{L}$   | —                                                                          | —                                                                          | no states                              |

Eq. (11) with this table *is* the whole model: per critical point, the reciprocal square root of a straight line in $E$, integrated against occupation over a window that slides with $\hbar\omega$. Every constant sits in the parameter table of §5.

### 6.2  Numerics: integrate in $k_\parallel$, not in $E$

First, the status of what follows, because it matters: Eq. (12) is **not a rival derivation and does not replace (11)** — it is a *quadrature scheme for* (11), one exact change of variable inside the same one-dimensional integral. (§6.3 takes the "doesn't this pull the rug from under energy space?" objection head-on.) The $1/\sqrt{\ }$ edges of (11) would otherwise force adaptive quadrature or endpoint-weighted rules, but the divergence is a pure coordinate artifact — manufactured in §3.2, when the smooth $k$-space geometry was re-parametrized by final energy $E$ — and one substitution undoes it. Take $k\equiv k_\parallel$ itself as the integration variable: $E$ is linear in $k^2$, so $\mathrm{d}E=\mp(\mu_{i\perp}\hbar^{2}/\mathcal{F}_i^{2})\,k\,\mathrm{d}k$ while $D\propto1/k$ — the factors of $k$ cancel identically, and (7) flattens to

$$\boxed{\;\mathcal{J}_i(\hbar\omega,T)=\frac{\mu_{i\perp}}{4\pi^{2}\hbar^{2}}\int_{k_1^{(i)}}^{k_2^{(i)}}\Delta f\big(E_i(k),T\big)\,\mathrm{d}k\;}\qquad\frac{1}{\mu_{i\perp}}\equiv\frac{1}{m_{u\perp}}+\frac{1}{m_{l\perp}},\tag{12}$$

$$E_i(k)=\underbrace{\hbar\omega_{i_6^-}+\frac{\mu_{i\perp}}{m_{u\perp}}\big(\hbar\omega-\mathcal{E}_g^{i}\big)}_{k_\parallel=0\ \text{intercept}}\;\mp\;\frac{\mu_{i\perp}\hbar^{2}}{2\mathcal{F}_i^{2}}\,k^{2}\qquad(-\ \text{at }X,\ +\ \text{at }L).$$

The limits are just the $u=0$/$v=0$ endpoints of §3.3 and §4; since they're the first thing an implementation touches, here they are in full. At $X$ (on the $\bar B_X<0$ branch) the lower limit is geometric only below the gap; the upper limit is the occupation floor:

$$k_1^{X}=\begin{cases}0, & \hbar\omega\ge\mathcal{E}_g^{X},\\[8pt]\sqrt{\dfrac{\mathcal{E}_g^{X}-\hbar\omega}{\lvert\bar B_X\rvert}}\;=\;\dfrac{1}{\hbar}\left[\dfrac{2\,(\mathcal{E}_g^{X}-\hbar\omega)\,m_{u\parallel}m_{l\parallel}}{m_{l\parallel}-m_{u\parallel}}\right]^{1/2}, & \hbar\omega<\mathcal{E}_g^{X}\ \text{(sub-gap tail)},\end{cases}$$

$$k_2^{X}=k_\parallel^{X}(E_{\rm floor},\hbar\omega)=\frac{\sqrt2\,\mathcal{F}_X}{\hbar}\left[\frac{\hbar\omega-\hbar\omega_{X_7^+}-E_{\rm floor}}{m_{u\perp}}+\frac{\hbar\omega_{X_6^-}-E_{\rm floor}}{m_{l\perp}}\right]^{1/2},$$

where $E_{\rm floor}$ is the energy below which the occupation factor is dead: $-20k_BT$ in equilibrium (Rosei's floor); for a pumped distribution, low enough that $|\Delta f|<\mathrm{tol}$ everywhere below it — for the CW $f^S$, whose smearing reaches $E_F\pm\hbar\omega_{\rm pump}$, take $E_{\rm floor}=-(\hbar\omega_{\rm pump}+20k_BT)$. Generosity is cheap: below the true floor the integrand is $\approx0$, so an over-deep floor wastes a few nodes, never accuracy. At $L$ both limits are geometric, and the window exists only above the gap:

$$k_1^{L}=0,\qquad k_2^{L}=\sqrt{\frac{\hbar\omega-\mathcal{E}_g^{L}}{\bar B_L}}=\frac{1}{\hbar}\sqrt{2\mu_{L\parallel}\big(\hbar\omega-\mathcal{E}_g^{L}\big)},\qquad\frac{1}{\mu_{L\parallel}}\equiv\frac{1}{m_{u\parallel}}+\frac{1}{m_{l\parallel}}.$$

$E_i(k)$ is the single display above on *both* sides of the $X$ gap — all the branch logic lives in $k_1^X$. (And notice where the $\parallel$ masses now sit: at $L$ only in $k_2^L$, at $X$ above the gap only inside $\mathcal{F}_X$ — §3.3's fit-degeneracy remark, made visible in the formula.)

No singularity survives anywhere: the integrand of (12) is a bounded, smooth occupation profile whose only feature is the Fermi step, of width $\sim k_BT$. That makes **composite Simpson on a uniform grid** — the rule this project uses — entirely adequate; nothing fancier is required. The recipe:

1. grid: $k=\mathrm{linspace}(k_1(\hbar\omega),\,k_2(\hbar\omega),\,N)$, $N$ odd;
2. integrand: $\Delta f\big(E_i(k)\big)$ — Fermi–Dirac in equilibrium, interpolation of the tabulated $f^S$/$f^P$ otherwise;
3. `simpson(y, x=k)`, times $\mu_{i\perp}/4\pi^{2}\hbar^{2}$; then into (9).

Measured against a converged reference (equilibrium, $\hbar\omega=2.4$ eV): at 300 K the $X$ integral sits at $5\times10^{-10}$ relative error with $N=101$ and reaches machine precision by $N=201$; the $L$ integrand at equilibrium is constant to machine precision (the fitted window lies entirely above $E_F$), and even for a hot 2000 K distribution $N=101$ gives $3\times10^{-14}$.

Two things to watch:
- **Resolve the step.** The integrand's only feature sits at $k_{\rm step}=k(E{=}0)$ — trivial to locate, since $E_i(k)$ is affine in $k^2$. At 100 K, $N=201$ gives $5\times10^{-9}$ and $N=401$ machine precision; or split the interval at $k_{\rm step}$ and Simpson each panel.
- **Respect the kinks of $\Delta f$.** Simpson's $O(N^{-4})$ assumes smoothness between nodes, and a pumped $f^S$ has slope discontinuities at $E_F\pm\hbar\omega_{\rm pump}$ — put panel boundaries at their images $k(E_F\pm\hbar\omega_{\rm pump})$. These are *distribution* features, not geometry: no choice of variable removes them; panel placement does.

Error control is one doubling: recompute at $2N$, compare. Vectorization: $k_{1,2}$ depend on $\hbar\omega$, so build the grid as an $(N_\omega\times N)$ array, `k1[:,None] + (k2-k1)[:,None]*s[None,:]` with $s$ uniform on $[0,1]$, and Simpson along the last axis — the whole spectrum in one call. (Gauss–Legendre with 48–64 nodes does the same job with fewer points, if node count ever matters.)

Two closed-form checks come free with (12):

- **Empty-window arithmetic.** Wherever $\Delta f\equiv1$ across the window, $\mathcal{J}_i=\frac{\mu_{i\perp}}{4\pi^{2}\hbar^{2}}(k_2-k_1)$ exactly. At $L$ with $T\to0$ (the fitted window sits entirely above $E_F$; §4 remark) this reads $\mathcal{J}_L=\frac{\mu_{L\perp}}{4\pi^{2}\hbar^{2}}\sqrt{(\hbar\omega-\mathcal{E}_g^{L})/\bar B_L}$ — the textbook $M_0$ square-root onset, recovered in closed form.
- **Two-forms agreement.** (11) and (12) are the same integral; evaluated independently (say, (11) by adaptive quadrature with the endpoint declared) they must agree to quadrature accuracy at every $(\hbar\omega,T)$ — a one-line unit test.

### 6.3  Pushback: does $k_\parallel$ pull the rug from under energy space?

A fair objection: §§3–5 work hard to *reach* an energy-space integral, and §6.2 then seems to walk away from it. It doesn't. The objection splits into three questions, in order.

**1. "If $k_\parallel$ is the integration variable, where did $k_\perp$ go? What is the second variable?"**

There is no second variable — the $\delta$-function ate it, and $k_\perp$ is precisely what it ate. Count dimensions in (★): three-dimensional; axial symmetry removes the azimuth (the factor $2\pi$, with $2\pi k_\perp\,\mathrm{d}k_\perp\,\mathrm{d}k_\parallel=\pi\,\mathrm{d}u\,\mathrm{d}k_\parallel$); the energy-conservation $\delta$ consumes one more. The natural variable to spend the $\delta$ on is $k_\perp$, since at fixed $k_\parallel$ the CEDS condition (3) is linear in $u=k_\perp^2$ with constant coefficient $\bar A$. Doing just that — no energy variable introduced — collapses (★) in one step:

$$\int_{k_\parallel>0}\mathrm{d}^3k\;\delta(\Omega_{lu}-\hbar\omega)\,\Delta f=\pi\int_0^\infty\!\mathrm{d}k_\parallel\int_0^\infty\!\mathrm{d}u\;\delta\big(\bar A\,u+\bar B\,k_\parallel^2-(\hbar\omega-\mathcal{E}_g)\big)\,\Delta f=\frac{\pi}{\bar A}\int_{k_1}^{k_2}\Delta f\big(E_i(k_\parallel)\big)\,\mathrm{d}k_\parallel,$$

which reproduces (12), constants and all (chase them through (★) and (9) if you like); the $u_*\ge0$ constraint and the occupation floor reproduce exactly the $k_{1,2}$ of §6.2. On the transition surface $k_\perp$ is not free but *slaved*: $k_\perp^2=\big[(\hbar\omega-\mathcal{E}_g)-\bar B\,k_\parallel^2\big]/\bar A$. After symmetry and the $\delta$, exactly one one-dimensional family of transitions survives, and $E$, $k_\parallel$, $k_\perp$ are three ways of labeling the same family. ($k_\perp$ would be a legal label too, but a bad one: it leaves a $k_\perp/k_\parallel$ weight in the measure, so the edge singularity survives. Only $k_\parallel$ flattens the measure, since the $1/k_\parallel$ in $D$ and the $k_\parallel$ in $\mathrm{d}E$ both descend from the same $v=k_\parallel^2$.)

**2. "So do we go to energy space to resolve the $\delta$, and then transition back for ease of integration?"**

No — this is the crux. The $\delta$ never needed energy space: the one-step collapse above resolves it entirely in $k$. Energy space is entered for exactly one reason, stated in §3.2: **the occupation depends on $\mathbf{k}$ only through the final-state energy.**

- **Not** spherical symmetry. $f(\mathbf{k})=f(E(\mathbf{k}))$'s level sets are the constant-energy surfaces themselves — anisotropic ellipsoids and hyperboloids — so $f$ inherits exactly the anisotropy of $E$, no more, no less. The claim is only that $f$ carries no $\mathbf{k}$-dependence beyond $E(\mathbf{k})$: every state on one constant-energy surface is equally occupied.
- **Why it holds.** Elastic momentum scattering ($\sim10$ fs) outruns energy relaxation ($\gtrsim100$ fs), so occupation equalizes across each iso-energy surface long before the energy distribution thermalizes — precisely the regime $f^S$ and $f^P$ describe. (In the hot-carrier literature the underlying gas is free-electron-like, $E\propto k^2$, where "function of $E$" and "isotropic" coincide; in Rosei's band geometry they don't, and function-of-$E$-only is the correct statement.)
- **Shared by (7), (11), and (12) alike;** a distribution with genuine extra $\mathbf{k}$-dependence — the first $\sim10$ fs after an anisotropically polarized pump, say — would break the factorization upstream of any choice of integration variable.

Sorting transitions by $E$ is what lets the electronic physics factor out of the geometry as a reusable weight $D(E,\hbar\omega)$ — the object Rosei tabulates, the one to plot and compare. And (12) hasn't abandoned that structure: it still evaluates $\Delta f$ at energies $E_i(k)$; the geometry hands each node its energy label. The tightest statement of the relationship is the differential identity behind the flattening,

$$D_{l\to u}\,\mathrm{d}E=\mp\frac{\mu_{\perp}}{4\pi^{2}\hbar^{2}}\,\mathrm{d}k_\parallel,$$

i.e. $k_\parallel$ is, up to constants, the antiderivative — the cumulative count — of the EDJDOS: integrating in $k_\parallel$ **is** integrating in $E$, with the known weight $D(E)$ absorbed exactly into the node placement. Nothing from §§3–5 is discarded — (12) consumes the §3.2 inversion (as $E_i(k)$), the §3.3/§4 window analysis (as $k_1,k_2$), and $D$ itself (as the flat measure). The two routes are the same two operations in opposite order:

| route | FGR $\delta$ resolved against | surviving label | Jacobian left behind |
|---|---|---|---|
| §3.2 $\to$ (7)/(11) | $(u,v)$ jointly, at fixed inserted $E$ | $E$ | $1/(16\pi^{2}\mathcal{D}\,k_\parallel)$ — the van Hove $1/\sqrt{\ }$ |
| §6.2 $\to$ (12) | $u=k_\perp^{2}$, at fixed $k_\parallel$ | $k_\parallel$ | $1/\bar A$ — a constant |

A natural follow-up: if the one-step route is this direct, shouldn't it be the *master* derivation, with energy space demoted to an afterthought? For $\epsilon_2(\hbar\omega)$ alone, it could be — nothing numerical would change. But not for this note's job, which is recreating Rosei.

- Eqs. (4), (5), (7) — the EDJDOS, its mass parameter, the thermal integral — are energy-space statements that never form on the direct route: the $1/\bar A$ Jacobian contains no $\parallel$ masses at all, and $\mathcal{D}$ surfaces only as an anonymous coefficient inside $E_i(k)$. It's the energy route that exposes $\mathcal{D}$ as a Jacobian and names it $\mathcal{F}$ (Eq. 5) — the quantity through which even the fitted strengths of (10), $S=\mathcal{F}|P|^2$, are defined.
- Beyond fidelity to the paper, $D(E,\hbar\omega)$ earns its keep downstream — geometry ($D$) times electronics ($\Delta f$) — because it answers which final energies a given photon probes: the working question of thermomodulation analysis, and of the pumped-PL problem, where the pump reshapes $f(E)$ and one wants to see at a glance which spectral window feels it.

Hence the division of labor this section settles on: **derive and reason in $E$; evaluate in $k_\parallel$.**

**3. "How superior is $k_\parallel$-integration, really — for $X$ and for $L$?"**

Measured, not argued (relative error of composite Simpson at fixed $N$, equilibrium 300 K, against a converged reference):

| regime | Simpson in $E$, uniform grid | Simpson in $k_\parallel$, uniform grid |
|---|---|---|
| $X$ above gap ($\hbar\omega=2.4$ eV) | edge node is infinite; zeroing it stalls at $9\times10^{-2}$ ($N{=}101$) $\to$ $1\times10^{-2}$ ($N{=}6401$); nudging it inward instead gives answers that depend on the nudge | $5\times10^{-10}$ at $N{=}101$; machine precision by $N{=}201$ |
| $X$ below gap ($\hbar\omega=1.9$ eV) | fine — integrand smooth | equally fine — no advantage |
| $L$ above gap ($\hbar\omega=2.6$ eV) | singular lower edge — same stall as $X$ above gap | exact at any $N$ in equilibrium ($\Delta f$ const across the window); $3\times10^{-14}$ at $N{=}101$ for a 2000 K distribution |

Three conclusions:
- **(i)** Against fixed grids in $E$ — Simpson very much included — the $k$-form is decisive wherever the window has a singular edge: the $E$-space error decays like $O(\sqrt h)$ (halves per *quadrupling* of nodes; still $\sim1\%$ at $N=6401$), versus Simpson's clean $O(N^{-4})$ in $k$. The same ranking holds for Gauss–Legendre: $10^{-2}$ versus $2\times10^{-8}$ at 64 nodes.
- **(ii)** Against energy space *done properly* — substituting $t=\sqrt{E_{\rm edge}-E}$, or a Gauss–Jacobi rule carrying the $1/\sqrt{\ }$ weight — there is **no advantage at all**: the errors come out bit-identical, because $t\propto k_\parallel$ *exactly* (at $L$, and at $X$ above the gap; verified to machine epsilon). The claim was never that energy space is wrong; it is that its correct quadrature substitution, written out, *is* $k_\parallel$ — the geometry had already named it. Staying in $E$ with the $t$-substitution loses nothing.
- **(iii)** Where no singular edge is in play ($X$ below the gap; $L$ in equilibrium, where $\Delta f\approx1$ makes the integral nearly the closed form of §6.2 anyway), the two variables perform identically. What the $k$-form buys overall is *uniformity*: one branch-free scheme at fixed $N$, accurate straight through both onsets — where the $E$-window shrinks or its edge softens, exactly the spectral region the PL problem lives in — and indifferent to the form of $\Delta f$, equilibrium or pumped.

## Appendix A  Dimensional audit (Gaussian)

Keeping myself honest. $[e^2]=\mathrm{erg\,cm}$, $[|P|^2]=\mathrm{cm}^{-2}$, $[\mathcal{D}]=\mathrm{erg}^2\mathrm{cm}^4$, $[\mathcal{F}]=\mathrm{g}$, $[D_{l\to u}]=\mathrm{erg}^{-2}\mathrm{cm}^{-3}$ (states per volume per energy$^2$), $[\mathcal{J}]=\mathrm{erg}^{-1}\mathrm{cm}^{-3}$.

- $(4')$: $\mathcal{F}^2/\hbar^4 k_\parallel\sim\mathrm{g}^2/(\mathrm{erg}^4\mathrm{s}^4\,\mathrm{cm}^{-1})=\mathrm{erg}^{-2}\mathrm{cm}^{-3}$. ✓
- $(9)$: $\dfrac{\mathrm{erg\,cm}\cdot\mathrm{erg}^4\mathrm{s}^4}{\mathrm{g}^2\,\mathrm{erg}^2}\cdot\mathrm{cm}^{-2}\cdot\mathrm{erg}^{-1}\mathrm{cm}^{-3}=\mathrm{erg}^2\mathrm{s}^4\,\mathrm{g}^{-2}\mathrm{cm}^{-4}=1$. ✓
- $(12)$: $\mu_\perp k/\hbar^2\sim\mathrm{g\,cm^{-1}}/(\mathrm{erg^2 s^2})=\mathrm{erg}^{-1}\mathrm{cm}^{-3}$ (using $\mathrm{erg\,s^2}=\mathrm{g\,cm^2}$) $=[\mathcal{J}]$. ✓

## Appendix B  From absorption to emission: where the Bose–Einstein factor hides

**Why this appendix.** Everything above computes $\epsilon_2$ — *absorption* — and there the occupation weight is the difference $\Delta f(E)=f(E-\hbar\omega)-f(E)$ (Eq. 11). The observable this project ultimately wants is *photoluminescence* — spontaneous *emission* — whose occupation weight is not a difference but a *product*, $f(E)\,[1-f(E-\hbar\omega)]$. This appendix derives that product, shows it collapsing in equilibrium back onto the same $\Delta f$ times a Bose–Einstein factor (so absorption and emission share one $\epsilon_2$, as Kirchhoff demands), and — the point for the pumped problem — isolates exactly which step of the collapse fails out of equilibrium, leaving the product irreducible.

Name the two states by the energies already used in the note: lower (initial, $d$-band) at $E_l\equiv E-\hbar\omega$, upper (final, $sp$-band) at $E_u\equiv E$, so $E_u-E_l=\hbar\omega$ on every transition. Write $f_l\equiv f(E-\hbar\omega)$, $f_u\equiv f(E)$, $\beta\equiv1/k_BT$.

### B.1  The three microscopic rates

One matrix element $|M|^2\propto|\hat{\boldsymbol\epsilon}\cdot\mathbf p_{ul}|^2$ (§2) drives three distinct processes at each vertical pair $(l,u)$. Fermi's Golden Rule dresses it with the occupations of the two levels and of the photon field:

- **Absorption** (photon in, $l\to u$): lower level filled, upper empty,
  $$W_{\rm abs}\ \propto\ |M|^2\,N_{\rm ph}\,f_l\,(1-f_u).$$
- **Stimulated emission** ($u\to l$, photon into the driving mode): upper filled, lower empty — same $|M|^2$, same field factor,
  $$W_{\rm stim}\ \propto\ |M|^2\,N_{\rm ph}\,f_u\,(1-f_l).$$
- **Spontaneous emission** ($u\to l$, photon into any empty mode): the $+1$ of $(N_{\rm ph}+1)$, independent of the driving field,
  $$W_{\rm spon}\ \propto\ |M|^2\,\rho_{\rm ph}(\hbar\omega)\,f_u\,(1-f_l).$$
  This last is the PL rate; $\rho_{\rm ph}$ is the photonic LDOS — the photonic half factored off at the very top of the note.

Two facts sit in these three lines and drive everything below: absorption and stimulated emission carry *opposite* electronic factors, whereas stimulated and spontaneous emission carry the *same* one, $f_u(1-f_l)$.

### B.2  Absorption: why the product becomes a difference

$\epsilon_2$ measures the *net* power removed from the beam — upward minus stimulated-downward. The common $|M|^2N_{\rm ph}$ cancels out of the *response function* (that is the whole content of defining $\epsilon_2$ as power per unit field, §2), leaving the electronic factor

$$f_l(1-f_u)-f_u(1-f_l)=\big(f_l-f_lf_u\big)-\big(f_u-f_uf_l\big)=f_l-f_u=\Delta f(E).$$

The cross term $f_lf_u$ is common to both processes and subtracts to zero. *This* is the origin of the difference in Eq. (11): it is not the raw absorption rate but the raw rate net of stimulated emission. Nothing here assumed equilibrium — $\Delta f$ is the correct absorption weight for any $f$, pumped or thermal, which is why the body of the note carries it unmodified into the $f^S,f^P$ case (§2).

### B.3  Emission in equilibrium: the Bose–Einstein factor, explicitly

The PL weight $f_u(1-f_l)$ has no subtraction to collapse it — it is irreducibly a product. In *thermal equilibrium*, though, it is tied to $\Delta f$ by a single algebraic identity of the Fermi function. From

$$1-f(E)=\frac{e^{\beta(E-\mu)}}{e^{\beta(E-\mu)}+1}=e^{\beta(E-\mu)}f(E)\qquad\Longrightarrow\qquad\frac{1-f(E)}{f(E)}=e^{\beta(E-\mu)},$$

apply it at both levels and take the ratio of the two products:

$$\frac{f_u(1-f_l)}{f_l(1-f_u)}=\frac{f_u}{1-f_u}\cdot\frac{1-f_l}{f_l}=e^{-\beta(E_u-\mu)}\,e^{+\beta(E_l-\mu)}=e^{-\beta(E_u-E_l)}=e^{-\beta\hbar\omega}.$$

The chemical potential cancels and the *level* energies cancel — only the *transition* energy $\hbar\omega$ survives. This is detailed balance: $f_u(1-f_l)=e^{-\beta\hbar\omega}\,f_l(1-f_u)$. Feed it back into the absorption difference of B.2,

$$\Delta f=f_l(1-f_u)-f_u(1-f_l)=f_l(1-f_u)\big(1-e^{-\beta\hbar\omega}\big),$$

and solve for the emission weight:

$$f_u(1-f_l)=e^{-\beta\hbar\omega}f_l(1-f_u)=\frac{e^{-\beta\hbar\omega}}{1-e^{-\beta\hbar\omega}}\,\Delta f=\frac{1}{e^{\beta\hbar\omega}-1}\,\Delta f.$$

That last fraction is the Bose–Einstein occupation of a photon of energy $\hbar\omega$, and the result is exactly the factor the difference "was missing":

$$\boxed{\;f_u(1-f_l)\;=\;n_{\rm BE}(\hbar\omega)\,\Delta f(E),\qquad n_{\rm BE}(\hbar\omega)=\frac{1}{e^{\beta\hbar\omega}-1}\;}$$

with the twin identity for the absorption channel, $f_l(1-f_u)=\big(1+n_{\rm BE}\big)\Delta f$ — the familiar $n$ vs. $n+1$ of emission vs. absorption, here read straight off the electron occupations. Note $n_{\rm BE}$ is *not* the occupation of the driving field ($N_{\rm ph}$ was divided out in B.2); it is manufactured purely from the two Fermi factors, and only *coincides* with a photon Bose function because both bands share one $(\mu,T)$. This is the fluctuation–dissipation / KMS structure specialized to two parabolic bands.

Assembling the PL spectrum is then a one-line edit of Eq. (11): replace the absorption weight $\Delta f(E)$ by the emission weight $f_u(1-f_l)$ and restore the photonic prefactor,

$$R_{\rm PL}(\hbar\omega,T)\ \propto\ \rho_{\rm ph}(\hbar\omega)\sum_{i=X,L}N_i\,\mathcal F_i^2|P_i|^2\int_{k_1^{(i)}}^{k_2^{(i)}}\frac{\mu_{i\perp}}{4\pi^2\hbar^2}\,f(E)\,[1-f(E-\hbar\omega)]\,\mathrm dk_\parallel,$$

evaluated on exactly the same geometry, windows, and slaved $k_\parallel(E,\hbar\omega)$ of §6 — only the electronic weight in the integrand changes. In equilibrium the box turns this into $\rho_{\rm ph}(\hbar\omega)\,n_{\rm BE}(\hbar\omega)\times[\text{the very }\epsilon_2\text{ integral of Eq. }11]$, i.e. $R_{\rm PL}\propto\rho_{\rm ph}\,n_{\rm BE}\,\epsilon_2$ — Kirchhoff's law recovered.

### B.4  Out of equilibrium: the factor that will not factor

> [!warning] The Bose–Einstein collapse is equilibrium-only
> Every step of B.3 used the Fermi form $1-f=e^{\beta(E-\mu)}f$ — *twice*, at $E_l$ and $E_u$, with **one shared** $\beta$ and $\mu$. That is what made the level energies and the chemical potential cancel and left a function of $\hbar\omega$ alone. Under a pumped $f^S$ (CW) or $f^P$ (pulsed) — non-thermal, with the slope breaks near $E_F\pm\hbar\omega_{\rm pump}$ that §6.2 flags — no single $(\mu,T)$ exists, the identity fails, and the ratio
> $$n_{\rm eff}(E,\hbar\omega)\ \equiv\ \frac{f(E)\,[1-f(E-\hbar\omega)]}{f(E-\hbar\omega)-f(E)}$$
> is **no longer a function of $\hbar\omega$ alone**: it retains genuine $E$-dependence and cannot be pulled out of the energy integral as any Bose factor. The PL integrand must be carried as the full product $f(E)[1-f(E-\hbar\omega)]$, node by node on the tabulated distribution — the same object the scheme of §6.2 already evaluates $\Delta f$ against, now with the emission weight in its place.
>
> This is the physics the pumped problem is *about*, not a technicality. Equilibrium PL is enslaved to absorption ($R_{\rm PL}\propto n_{\rm BE}\,\epsilon_2$) and carries no independent information. The non-equilibrium emission is *not* $\propto\epsilon_2$: the pump reshapes $f(E)$ so that $n_{\rm eff}(E,\hbar\omega)$ varies across the very window Eq. (11) integrates, and the emission line shape parts company with the absorption line shape. Reproducing the collapse $n_{\rm eff}\to n_{\rm BE}$ under $f=f_{\rm FD}$ is a good unit test; *taking* it is throwing the signal away.

**Consistency check.** With $f=f_{\rm FD}$, confirm $n_{\rm eff}(E,\hbar\omega)\to n_{\rm BE}(\hbar\omega)$ independent of $E$ — a one-liner against B.3, and the emission analogue of the "two-forms agreement" test of §6.2.

## References

- M. Guerrisi, R. Rosei, P. Winsemius, *Phys. Rev. B* **12**, 557 (1975) — the paper recreated here ($X$ derived, $L$ delegated).
- R. Rosei, *Phys. Rev. B* **10**, 474 (1974) — the $L$ machinery (and the EDJDOS recipe) Rosei borrows.
- N. E. Christensen, B. O. Seraphin, *Phys. Rev. B* **4**, 3321 (1971) — band structure; source of the masses.
- P. B. Johnson, R. W. Christy, *Phys. Rev. B* **6**, 4370 (1972) — the data Rosei fits.
