---
degree: MSc
research: photoluminescence
type: problem
---
We attempt to numerically evaluate an integral with a delta function approximated by a gaussian with vanishing width. The Gaussian is given in a standard fashion
$$
G_{\sigma}(x|\mu)=\frac{1}{\sigma \sqrt{ 2\pi }}{\Large e^{-\left( \frac{x-\mu}{\sqrt{ 2 }\sigma} \right)^{2}}}
$$
The exact, approximated and numeric integral values are given as follows

$$
\begin{align}
f(\mu) &= \int\limits_{-\infty}^{\infty} f(x)\delta(x-\mu)\, dx \tag{1}
 \\
f^{\text{approx}}_{\sigma}(\mu) & = \int\limits_{-\infty}^{\infty} f(x)\cdot G_{\sigma}(x|\mu) \, dx \tag{2}\\
f^{\text{numeric}}_{\sigma,N}(x_{0}) &= \sum\limits_{n=1}^{N} f(x_{n})\cdot G_{\sigma}(x_{n}|\mu) \cdot\Delta x\tag{3}
\end{align}
$$

Where $x_{n}= -L+n\Delta x$ and $\Delta x= \frac{{2L}}{N}$. Below is the order of convergence

$$
f(x_{0}) = \lim\limits_{\sigma\to_{0}} \  f^{\text{approx}}_{\sigma}(x_{0}) =  \lim\limits_{\begin{align}
\sigma&\to0 \\ {\small N}&\to \infty
\end{align}}  f^{\text{numeric}}_{\sigma, N}(x_{0})
$$
- it is worth noting that the infinite integration interval introduces yet another limit, which we don't rigorously consider, just take an interval range $2L$ that is much larger than $2\sigma$.

$$
\begin{align}
E^{\text{total}}_{N,\sigma} &= f-f^{\text{numeric}}_{\sigma,N} \\
&= \underbrace{ f-I^{\text{approx}}_{\sigma} }_{ E_{\sigma}^{\text{approx}} }+\underbrace{ I^{\text{approx}}_{\sigma}-f^{\text{numeric}}_{\sigma,N} }_{ E_{N,\sigma}^{\text{numeric}} } 
\end{align}
$$
The general deviation of the calculation from the desired result has two contributions, one 
The numeric error of a trapezoid integration is known and given by
$$
E_{{\small N},\sigma}^{\text{numeric}}  = \frac{F_{\sigma}''(\xi)(2L)^{3}}{12N^{2}}
$$

where $\xi\in(-L,L)$. We can set an upper bound for the error by seeking a certain $x^{*}$ such that $F_{\sigma}(x^{*})\geq F_{\sigma}(x) \quad \forall x\in(-L,L)$. I'm not sure that $E_{\sigma}^{\text{approx}}$ has a form that can be found, but it is clear that is depends only on $\sigma$. For a given $\sigma$
$$
E^{\text{total}}_{N,\sigma} = E_{\sigma}^{\text{approx}} + \frac{F_{\sigma}''(\xi)(2L)^{3}}{12N^{2}}
$$
$$
\delta_{N,\sigma}^{\text{total}}=\delta^{\text{approx}}_{\sigma} + \frac{F''_{\sigma}(\xi)}{f(x_{0})} \frac{(2L)^{3}}{12N^{2}}
$$

So for a given $\sigma$, as $N$ increases, $\delta_{N,\sigma}^{\text{total}}$ shrinks as $\propto N^{-2}$ and reaches $\delta^{\text{approx}}_{\sigma}$ asymptotically.

On the one hand, smaller $\sigma$ corresponds to smaller $\delta^{\text{approx}}_{\sigma}$ value. On the other hand, since $F''$ contains a $G''$ component (which scales with $\sigma^{-4}$) we expect the numeric convergence to become more gradual as $\sigma$ shrinks - namely, to require larger values of $N$ to reach numeric accuracy. This interplay between the approximation error and the numerical error requires us to simultaneously decrease $\sigma$ while increasing $N$ for the total error to negligible (?) values.


![](../9.%20Misc/attachments/Pasted%20image%2020250117125025.png)

The integration intervals here are $\Big[x_{0}-80\sigma, \ x_{0}+80\sigma\Big]$.

![](../9.%20Misc/attachments/Pasted%20image%2020250117140732.png)

The integration intervals here are $\Big[x_{0}-10\sigma, \ x_{0}+10\sigma\Big]$.

# 2D delta

$$
\begin{align}
\delta\left( \frac{\hbar^{2} k_{1}^{2}}{2m}-\frac{\hbar^{2} k_{2}^{2}}{2m} -\hbar\omega\right) &= \lim\limits_{\sigma\to 0} \frac{1}{\sigma_{\mathcal{E}}\sqrt{ 2\pi }} \exp\left[-\frac{1}{2} \left(\frac{\frac{\hbar^{2} k_{1}^{2}}{2m}-\frac{\hbar^{2} k_{2}^{2}}{2m} -\hbar\omega}{\sigma_{\mathcal{E}}} \right)^{2} \right] \\ \\
&= \lim\limits_{\sigma\to 0} \frac{1}{\sigma_{\mathcal{E}}\sqrt{ 2\pi }} \exp\left[-\frac{1}{2} \left(\frac{k_{1}^{2}- k_{2}^{2} -\frac{2m\omega}{\hbar}}{\sigma_{k}^{2}} \right)^{2} \right] \equiv \lim\limits_{\sigma\to 0} G_{\sigma}(k_{1}, k_{2};\omega)
\end{align}
$$

$$
\begin{align}
I&=\iint\limits \underbrace{ \underbrace{ f(k_{1},k_{2}) }_{ \text{includes Jacobian} } G_{\sigma}(k_{1}, k_{2})  }_{ F_{\sigma}(k_{1},k_{2}) }\  dk_{1} \ dk_{2} \\
&\sum\limits_{\substack{n\in [1,N]  \\ m \in [1,M]}}\left( \sum\limits_{m=1}^{M} \frac{F_{\sigma}(k_{n-1},k_{m-1})+F_{\sigma}(k_{n-1},k_{m})+F_{\sigma}(k_{},k_{m-1})+F_{\sigma}(k_{n},k_{m})}{4} \right) 
\end{align}
$$

# Nondimensionality

$$
\int\limits f(x) \frac{1}{\sigma \sqrt{ 2\pi }} {\Large e^{- \left( \frac{x-\mu}{\sqrt{ 2 }\sigma} \right)^{2} }} \, dx 
$$
$$
\chi \to \frac{x}{\sqrt{ 2 }\sigma} \quad \tilde{\mu}\to \frac{\mu}{\sqrt{ 2 }\sigma} 
$$
$$
\int\limits f(\sqrt{ 2 }\sigma\chi) {\Large e^{ -(\chi-\tilde{\mu})^{2} }} \, d\chi
$$
Maybe think in terms of Riemann sums since it is closer to a numerical integral?

$$
\sum\limits_{n=}^{N}f(x_{n})  \frac{\Delta x}{\sigma \sqrt{ 2\pi }} {\Large e^{- \left( \frac{x_{n}-\mu}{\sqrt{ 2 }\sigma} \right)^{2} }}
$$
$$
\Delta x = \frac{b-a}{N} \quad x_{n} = x_{0}+\Delta x\cdot n
$$

If we wish for our $x$ interval to sample over the "interesting" part of the Gaussian and not miss it, we should demand that for every $\sigma$ the interval need be smaller. If we demand that $\Delta x \leq 0.1\sigma$ we guarantee at least 10 samples inside the significant portion of the integral. More generally, we can set the demand the $\Delta x\leq s\cdot\sigma$ where $0<s\leq 1$ then
$$
s\cdot\sigma \geq \Delta x = \frac{b-a}{N} \  \Longrightarrow \ N \geq \frac{b-a}{s\cdot\sigma}
$$

Since the Gaussian is symmetric and vanishes quickly far from $\mu$ we can conveniently integrate over an interval of width, say, $10\sigma$ or more generally $m\cdot\sigma$ where $m \in\mathbb{N}$ Namely $[\mu-m\cdot\sigma, \mu+m\cdot\sigma]$ which changes the demand on $N$ to be
$$
N\geq \left\lceil\frac{2m}{s} \right\rceil
$$

The above summation can be then written as

$$
\Delta x = \frac{2m\sigma}{2m/s} = s\cdot\sigma \quad\Rightarrow\quad \begin{align}
x_{n} &= (\mu-m\cdot\sigma)+  (s\cdot\sigma)n \\
&= \mu - \sigma(m-s\cdot n)
\end{align}
$$

This leaves us with the following control parameters:
- $\sigma$ - gaussian delta approximation
- $s$ - sampling points inside gaussian (essentially $\Delta x$)
- $m$ - interval width in terms of $\sigma$

___
By appropriately decreasing our relevant integration range with the shrinking $\sigma$, we're making sure enough sample points remain within the non-negligible parts of the Gaussian.

Essentially we have two control parameters:
- $\sigma$ determines how closely the Gaussian approximates the delta numerically
- $N$ determines how well the numerical integration converges to the actual integral.

Ideally 

$$
\lim\limits_{\begin{align} 
&N \to \infty  \\
&\sigma \  \to \  0
\end{align}}
$$

- If we choose $\Delta x = \alpha\sigma$ where $0<\alpha\leq 0.1$ the normalization factor becomes constant and the gaussian no longer appears to properly approximate a delta function, as it's height is not increased with decreasing $\sigma$

==We could consider a varying interval density, such that more sample points are dedicated around the mean and fewer as we get further away.==

