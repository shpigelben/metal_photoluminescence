An electronic transition between momentum states $\ket{\mathbf{k}_{1}}$ and $\ket{\mathbf{k}_{2}}$, separated by energy $\hbar \omega$, is given by [Fermi Golden Rule](2.%20Notes/Fermi%20Golden%20Rule.md) as follows
$$
\begin{align}
\Gamma_{1\to 2}{\small (\hbar\omega) } &= \frac{2\pi}{\hbar}|\braket{ k_{\text{1}} | H'|k_{\text{2}} } |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k}_{2}) - \mathcal{E}{\small (\mathbf{k}_{1})+\hbar\omega } })  \\
&= \frac{2\pi}{\hbar}|\mu_{\text{12}} |^{2} \ \delta(\mathcal{E}{\small (\mathbf{k}_{2}) - \mathcal{E}{\small (\mathbf{k}_{1})+\hbar\omega } }) 
\end{align}
$$
$\mu_{12}$ is the transition dipole moment and it expresses conservation of momentum. $\mathcal{E}(\mathbf{k})$ is the dispersion relation and the expression in the delta function embodies conservation of energy.

Given an electron probability distribution $\Big(f(\mathcal{E}(\mathbf{k}))\to f(\mathbf{k})\Big)$ we can find the total rate of transitioning from state $\ket{\mathbf{k}_{1}}$ into all possible states

$$
\begin{align}
\Gamma_{1}(\hbar\omega) &= \overbrace{2}^{\text{spin states}}\cdot\sum\limits_{\mathbf{k}_{2}} \ \Gamma_{1\to 2}{\small (\hbar\omega) }\Big[1-f(\mathbf{k}_{2})\Big] \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{2}}}{(2\pi)^{3}} \ \Gamma_{1\to 2}{\small (\hbar\omega) }\Big[ 1-f (\mathbf{k}_{2})  \Big] 
\end{align}
$$
Similarly, to find all possible transitions we simply sum over all transitions from all initial states
$$
\begin{align}
\Gamma(\hbar\omega) &= 2\cdot\sum\limits_{\mathbf{k}_{1}} \ \Gamma_{1}{\small (\hbar\omega) }\Big[1-f(\mathbf{k}_{1})\Big] \\
&= 2V\int\limits_{\text{BZ}} \frac{{d^{3}k_{1}}}{(2\pi)^{3}} \ \Gamma_{1}{\small (\hbar\omega) }\Big[ 1-f (\mathbf{k}_{1})  \Big] 
\end{align}
$$

Finally, when plugging $\Gamma_{1\to 2} \to \Gamma_{1}\to \Gamma$, for the continuous case we get 

$$
\boxed{ \ \Gamma(\hbar\omega) = \frac{2\pi}{\hbar}\left( \frac{2V}{(2\pi)^{3}} \right)^{2} \iint\limits_{BZ} |\mu(\mathbf{k}_{1},\mathbf{k}_{2})|^{2} \  f(\mathbf{k}_{1})\overline{f(\mathbf{k}_{2})} \  \delta(\mathcal{E}{\small (\mathbf{k}_{2}) - \mathcal{E}{\small (\mathbf{k}_{1})+\hbar\omega } }) \  dk_{1}^{3} \ dk_{2}^{3} \ }
$$
