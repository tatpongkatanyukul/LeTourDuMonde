# Linear Algebra

---
Trefethen and Bau

# Lecture 3

> the induced matrix norm $\lVert A x \rVert_{(m,n)}$ is the smallest number $C$ for which the following inequality holds for all $x \in \mathbb{C}^n$:
> $\lVert A x \rVert_{(m)} \leq C \lVert x \rVert_{(n)}$ .

$\lVert A x \rVert_{(m,n)} = \arg\min_C C$ 

s.t. $\lVert A x \rVert_{(m)} \leq C \lVert x \rVert_{(n)}$ for all $x \in \mathbb{C}^n$.

> In other words, $\lVert A x \rVert_{(m,n)}$ is the supremum of the ratios $\lVert A x \rVert_{(m)}/\lVert x \rVert_{(n)}$ over all vectors $x \in \mathbb{C}^n$ --- the maximum factor by which $A$ can "stretch" a vector $x$.
