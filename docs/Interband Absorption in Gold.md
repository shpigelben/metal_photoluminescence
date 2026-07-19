$$
\begin{align}
{\varepsilon}_2(\omega)=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3}&\int\limits_{\rm BZ}\!{\mathrm{d}}^3k\;
\bigl|M_{ul}(\mathbf k)\bigr|^{2}\,
\delta\!\bigl(E_u(\mathbf k)-E_l(\mathbf k)-{\hbar\omega}\bigr)\,
f\bigr(E_{l}(\mathbf{k})\bigl)\Bigl[1-{f}\bigl(E_u(\mathbf k)\bigr)\Bigr]\; \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3}\, & \int\limits_{\rm BZ}  \!{\mathrm{d}}^{3}k \;  \delta \bigr(\Delta(\mathbf{k})-\hbar \omega \bigl) f\bigl(E(\mathbf{k})-\Delta(\mathbf{k})\bigr)\Bigl[1-{f}\bigl(E(\mathbf k)\bigr)\Bigr] \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \iint\limits_{E,\Delta} \; dE d\Delta \; \mathcal{D}(E,\Delta) \delta(\Delta-\hbar\omega)f(E-\Delta) \bigl[1-f(E)  \bigr] \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \int\limits_{E_{\rm min}}^{E_{\rm max}} dE \; \mathcal{D}(E, \hbar\omega) f(E-\hbar\omega)\bigl[1-f(E)\bigr]  \\
=\frac{4\pi^2 e^2}{m^2\omega^2}\,
\frac{2}{(2\pi)^3} \frac{N|P|^{2}}{3}& \; \mathcal{J}(\hbar\omega)
\end{align}
$$

1. $E_{u}-E_{l}\equiv \Delta \qquad E_{u}\equiv E \qquad\Rightarrow E_{l}=E-\Delta$
2. $d^{3}k \longrightarrow \mathcal{D}(E,\Delta) \, dE d\Delta$ this is a standard change of coordinates, why does Rosei term it with the unique term EDJDOS?

The main challenge here, really, is to explicitly and properly find the EDJDOS $\mathcal{D}$ and integration limits $E_{\mathrm{min}}$ and $E_{\mathrm{max}}$.