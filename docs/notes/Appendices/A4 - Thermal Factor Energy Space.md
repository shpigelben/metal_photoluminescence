# Equilibrium
$$
\begin{align}
I & = \; \int\limits_{0}^{\infty} f(\mathcal{E}+\hbar\omega)[1-f(\mathcal{E})]d\mathcal{E} \tag{1}\\
&= \; n_{B}(\hbar \omega) \left[ \int\limits_{0}^{\infty}f(\mathcal{E})d\mathcal{E}-\int\limits_{0}^{\infty}f(\mathcal{E}+\hbar\omega) d\mathcal{E}\right] \tag{2}   \\
&= \; n_{B}(\hbar \omega) \left[ \int\limits_{0}^{\infty}f(\mathcal{E})d\mathcal{E}-\int\limits_{\hbar\omega}^{\infty}f(\mathcal{E}) d\mathcal{E}\right] \tag{3}   \\
&= \; n_{B}(\hbar \omega) \int\limits_{0}^{\hbar\omega}f(\mathcal{E})d\mathcal{E} \tag{4}    \\
&= \; n_{B}(\hbar \omega) \int\limits_{0}^{\hbar\omega} \frac{1}{e^{\beta(\mathcal{E}-\mu)}+1}d\mathcal{E} \tag{5}    \\
&= \; n_{B}(\hbar \omega) \int\limits_{0}^{\hbar\omega} \left[ 1+ \frac{e^{\beta(\mathcal{E}-\mu)}}{e^{\beta(\mathcal{E}-\mu)}+1} \right] d\mathcal{E} \tag{6}    \\
&= \; n_{B}(\hbar \omega) \left[ \mathcal{E}- \frac{1}{\beta}\ln \left(e^{\beta(\mathcal{E}-\mu)}+1\right) \right]_{\mathcal{E=0}}^{\mathcal{E}=\hbar\omega} \tag{7}   \\
&= \; n_{B}(\hbar \omega)  \left[ \hbar\omega+ \frac{1}{\beta}\ln\left(1+e^{-\beta\mu}\right)-\frac{1}{\beta}\ln\left(1+e^{\beta(\hbar\omega-\mu)}\right) \right] \tag{8} \\
& \approx \; \frac{\hbar\omega}{e^{\beta \hbar\omega}-1}\tag{9}
\end{align}
$$

The transition $(1)\to(2)$ is a known identity
$$
f(\mathcal{E}+\hbar\omega) [1-f(\mathcal{E})] = n_{B}(\hbar\omega) \left[f(\mathcal{E})-f(\mathcal{E+\hbar \omega})\right]
$$
where $n_{B}(\hbar\omega)$ is the Bose-Einstein distribution

$$
n_{B}(\hbar\omega) = \frac{1}{e^{\beta \hbar\omega}-1}
$$
The $(8)\to(9)$ approximation is valid when the following conditions are met
$$
\mu \gg k_{\small B}T \quad\text{and}\quad \mu\gg \hbar\omega
$$

# Non-equilibrium

$$
f\big( { \mathcal{E} \ | \ \omega _{\scriptsize L} }\big) = f^{T}({ \mathcal{E}}) + \delta E(\omega _{\scriptsize L})\cdot B({ \mathcal{E}\ | \ \omega _{\scriptsize L}}) 
$$
$$
B({ \mathcal{E} \ |\ \omega _{\scriptsize L}}) = f^{T}({\mathcal{E} - \hbar\omega _{\scriptsize L}})\Big[ 1-f^{T}({\mathcal{E}}) \Big] - f^{T}(\mathcal{E})\Big[ 1- f^{T}(\mathcal{E}+\hbar\omega _{\scriptsize L}) \Big] \tag{2.1.2}
$$

$$I(\hbar\omega_{E}|\hbar\omega_{L}) \propto \int\limits_{0}^{\infty} f(\mathcal{E}+\hbar\omega)[1-f(\mathcal{E})]d\mathcal{E}$$