# PnP Problem



## Direct Least Squares

* N is the number of point pairs, n , n+1 represent the coordinates or camera frames
* the measurement unit vector direction of frame {n} and points position equation from {n+1} to {n}
* z is fixed , and r is used to optimize

$$
{}^{n}z_i = {}^nr_i + \eta _i \\
{}^{n}p_i = {}^{n} R_{n+1} {}^{n}p_i + {}^{n+1}t_n
$$

* the cost function and constraints

$$
\underset{}{\operatorname{arg min}} J
$$

$$
s.t \qquad \\ R^TR=I \\
det(R)=1\\
d_i = ||{}^n{p}_{i}|| = ||{}^{n}R_{n+1}{}^{n+1}p_{i} + {}^{n}t_{n+1}||
$$

* cost function 

$$
J = \sum_{i=1}^{N} ||{}^{n}z_i - {}^{n}r_i|| \\
= \sum_{i=1}^{N} |||{}^{n}z_i -  \frac{1}{d_i} ({}^{n}R_{n+1}{}^{n+1}p_{i} + {}^{n}t_{n+1}) ||
$$



* J is nonlinear, computing all of its local minimum is quite challenging

> Approach:
>
> * initial guess + iteration
>   * only one local minimum will converged, even with multiple restarts
> * use KKT optimality,
>   * to much unknowns
> * reduce the number of unknowns

* noise-free station

$$
d_i \  {}^{n}r_i ={}^{n}R_{n+1}{}^{n+1}p_{i} + {}^{n}t_{n+1}
$$

* in terms of fewer unknowns
* matrix-vector form

$$
\left[ \begin{matrix}
{}^{n}r_1& &  & -I \\
 & \ddots & &  \vdots \\
 & & {}^{n}r_N & -I
\end{matrix} \right]
\left[ \begin{matrix}
d_1 \\
\vdots \\
d_N \\
{}^{n} t_{n+1} \\
\end{matrix} \right]
=
\left[ \begin{matrix}
{}^{n} R_{n+1} && \\
& \ddots & \\
& & {}^{n} R_{n+1}\\
\end{matrix} \right]
\left[ \begin{matrix}
{}^{n+1}p_1 \\
\vdots \\
{}^{n+1}p_N \\
\end{matrix} \right]
$$

$$
Ax=Wb
$$

* $A$ and $b$ comprise quantities that are known or measured, $d_i$  also known
* $x$ contains unknown translation matrices,  $W$ contains unknown rotation matrices

$$
x=(A^TA)^{-1}A^TWb =\left[ \begin{matrix} U\\V \end{matrix} \right]Wb
$$

$$
A^TA = 
$$



* the scalar parameters $d_i$ are a function of U 

* and the translation ${}^{n}t_{n+1}$ is a function of V

* > what are U and V ? 

* > the close form of x=[U V]^T Wb ?



* linear functions

$$
d_i = u_i^T Wb \\
{}^{n}t_{n+1} = VWb 
$$

* $u_i^T$ correspondences to the i-th row of U

$$
u_i^TWb \  {}^{n}r_i = {}^{n}R_{n+1}{}^{n+1}p_i  + VWb
$$

* ${}^{n}R_{n+1}$ appears linearly in the above equation
* express the rotation matrix in terms of the CGR parameters

$$
s=[s_1, s_2, s_3]^T \\
{}^{n}R_{n+1} = \frac{\bar{R}}{1+s^Ts} \\
\bar{R} = ((1-s^Ts)I +2[s]_\times +2ss^T )
$$

$$
u_i^TW({}^{n}R_{n+1})b \  {}^{n}r_i = {}^{n}R_{n+1}{}^{n+1}p_i  + VW({}^{n}R_{n+1})b
$$

* ${}^{n}R_{n+1}$ appears linearly, and can cancel the $1+ss^T$ 

* > why can cancel ?

* the rotation matrix become a form $\bar{R}$

$$
u_i^TW[{}^{n}\bar{R}(s)_{n+1}]b \  {}^{n}r_i = {}^{n}\bar{R}(s)_{n+1}{}^{n+1}p_i  + VW[{}^{n}\bar{R}(s)_{n+1}]b
$$

* which renders constraints that are quadratic in s 
* ​

## SVD and Eigen Vectors 



## Grobner  Basis Method

* ​

## Gauss Newton Method

* expand the object function $x^TAx$ , and calculate the first , second order derivations directly





## Reference

1. http://rosclub.cn/post-566.html 
2. [minimal problems](http://cmp.felk.cvut.cz/mini/)
3. [Grobner Basis Solver](http://cmp.felk.cvut.cz/~kukelova/publications/Kukelova-etal-ECCV-2008.pdf)
4. [DLS PnP Solver](http://www-users.cs.umn.edu/%7Estergios/papers/ICCV-11-DLS-PnP.pdf)
5. [OPnP Solver](https://sites.google.com/site/yinqiangzheng/)
6. [EPnP Solver](http://icwww.epfl.ch/~lepetit/papers/lepetit_ijcv08.pdf)