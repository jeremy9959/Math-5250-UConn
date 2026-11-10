### Minkowski's Theorem

In fact, a theorem of Minkowski states that *all* norms on a finite dimensional vector space over $\R$ or $\C$ are equivalent.  This result is a consequence of the fact that $\R$ and $\C$ are locally compact fields, and the proof involves the application of the Heine-Borel theorem that any bounded sequence in these fields has a convergent subsequence.  The proof (of a more general result on valued fields) is given in Conrad's
[Equivalence of Norms](https://kconrad.math.uconn.edu/blurbs/gradnumthy/equivnorms.pdf).



Furthermore, a finite dimensional vector space is complete with respect to the metric topology coming from one (or any) norm. 



### Norms on Matrices

Now we consider norms on matrices and linear maps. 
Notice that if $V$ and $W$ are $n$ and $m$ dimensional vector spaces respectively over a field $F$, then the choice of a basis for $V$ and $W$ allows us to identify the space of linear maps from $V$ to $W$ with $M_{n\times m}(F)$.  This in turn is an $n\times m$ dimensional vector space over $F$.

When $F$ is $\R$ or $\C$, one choice for a norm
on a matrix $A=(a_{ij})$ is the sup norm: 
$$
\|A\|_{\mathrm{sup}} = \sup_{1\le i\le n, 1\le j\le m} \{|a_{ij}|\}
$$

A second choice is the $\ell^{2}$ norm, also called the *Frobenius norm*:
$$
\|A\|_{F} = \sqrt{\sum_{i,j} |a_{ij}|^2}.
$$

Observe for later that 
$$
\|A\|_{F}^2 = \mathrm{tr}(AA^{\top}) = \mathrm{tr}(A^{\top}A).
$$

Both of these norms are defined on matrices, not
linear maps; they depend on the choice of bases for $V$ and $W$.  

**Proposition:** Let $A$ by an $n\times m$ matrix over $\R$ or $\C$.  
Then there is a constant $C$ such that
the linear map $v\mapsto Av$ from $F^{m}$ to $F^{n}$ satisfies
$$
\|Av\|\le C\|v\|
$$
where $\|v\|$ is the Euclidean norm.

**Proof:** Following Conrad, we see that if $v=(c_1,\ldots, c_{m})$, then
$$\begin{aligned}
\|Av\| &\le \sqrt{m}\|Av\|_{\mathrm{sup}} \\
&\le \sqrt{m}\sup_{1\le i\le n} |\sum_{i=1}^{m} a_{ij}c_{j}|\\
&\le \sqrt{m}\sup_{1\le i\le n}\sum_{j=1}^{n}
 |a_{ij}|\|v\|_{\mathrm{sup}} \\
 &\le n\sqrt{m}\sup |a_{ij}|\|v\|_{\mathrm{sup}} \\
 &\le (n\sqrt{m}\sup_{i,j}|a_{ij}|)\|v\|
 \end{aligned}
 $$
 so we can use
 $$
 C = n\sqrt{n}\sup_{ij}|a_{ij}|
 $$



### The Operator Norm

The operator norm gives a basis-independent way to define a norm on linear maps from $V$ to $W$, given
norms on $V$ and $W$. 
Let $L:V\to W$ be such a linear map.  Define
$$
\|L\|_{\mathrm{op}} = \inf_{v\in V} \frac{\|L(v)\|}{\|v\|}.
$$




### The Frobenius norm



We are interested in norms on matrices and linear maps that enable us to measure "distance" between maps and therefore characterize the idea of "best approximation."  We will consider two different matrix norms, the *operator norm* and the *frobenius norm.*  The operator norm is invariant under change of basis and is therefore a norm on linear maps, while the frobenius norm is only invariant under unitary
change of basis.

### The operator norm

Let $L$ be a linear map $L:V\to W$ where $V$ is $n$-dimensional and $W$ is $m$-dimensional.  Define
$$
\|L\| = \sup_{v\in } \|Av\|
$$

