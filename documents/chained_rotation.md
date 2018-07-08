# Davenport chained rotation 

* three chained intrinsic rotations about body-fixed specific axes
* generalized Euler rotations, first and third axes are overlapping
* generalized Tait-Bryan rotation, three different axes, most of cases



# Theorem

* decomposing a rotation into three composed movement about **intrinsic axes**
*  equivalent to the decomposition problem of matrices
* extrinsic rotations -> the axes of the fixed coordinate system 
* intrinsic rotations -> initially aligned with the fixed one, and modified after each rotation
* a unique decomposition is possible, axes 1 and 3 must be in the plane orthogonal to axes 2
* Tait-Bryan: 1 and 3 are perpendicular, Euler: 1 and  3 are overlapping 

# Tait-Bryan chained

| rotation elements                                            | effect on a base coordinate |
| ------------------------------------------------------------ | --------------------------- |
| in order yaw, pitch', roll'';  z-y'-x''                      | around intrinsic X,Y,Z axes |
| $\psi$ , $\theta$, $\phi$                                    | around intrinsic X,Y,Z axes |
| $M=R_x(\phi)R_y(\theta)R_z(\psi)$ <br /> $M=roll(\phi)pitch(\theta)yaw(\psi)$ | around intrinsic X,Y,Z axes |

# Direction

| direction                                                    | result |
| ------------------------------------------------------------ | ------ |
| 用B左乘A <br /> pre-multiply A by B<br /> B is used to pre-multiply A | BA     |
| 用A右乘B<br />post-multiply B by A<br /> A is used to post-multiply B | BA     |

### when pre-multiply and when post-multiply

* pre-multiply
  * announce a point in a coordinate to another coordinate
  * coordinate system {B} (base), translate M based on itself to {A}
  * a point under {A} is Pa, want to announce under {B} as Pb, Pb = MPa

# To Extrinsic rotations 

* Any extrinsic rotation is equivalent to an intrinsic rotation by the same angle but with inverted order of elemental rotations, and vice versa

| rotation elements order                        | effect and result on a base coordinate | usage           | direction     |
| ---------------------------------------------- | -------------------------------------- | --------------- | ------------- |
| intrinsic<br />x-y'-z'', $\alpha-\beta-\gamma$ | R=X($\alpha$)Y($\beta$)Z($\gamma$)     | v' = Rv         | pre-multiply  |
| extrinsic<br />z-y-x, $\gamma-\beta-\alpha$    | R=X($\alpha$)Y($\beta$)Z($\gamma$)     | v' = Rv         | pre-multiply  |
|                                                | $w=v^T$<br />use transpose $R^T$       | $(v')^T =wR^T $ | post-multiply |

* the rotation matrix of an intrinsic element rotation sequence is the same as that of the inverse extrinsic element rotation sequence
* intrinsic rotation order x-y'-z'', $R=XY'Z''=ZYX$


# Ambiguities

* Alias or alibi, (passive or active). opposite direction, clockwise or counterclockwise
* pre-multiply or post multiply
* right- or left-handed coordinates
* vectors or forms, the vector space has a dual space of linear forms, and the matrix can act  on either vectors or forms.

# Decomposition

$Rv=\lambda v$

| inverse order                                  | result                               |
| ---------------------------------------------- | ------------------------------------ |
| intrinsic: $R=R_1R_2$                          | $R_1$ become to $R_2$                |
| intrinsic: $R=R_1R_2^{-1}$=$R_1R_2^{-1}R_2R_2$ | $R_1$ become to $R_2^{-1}$           |
| intrinsic: $R_2$ and $R_2^{-1}$                | $R_2^{-1}$ is double effect of $R_2$ |

# Basic 

$$
(AB)^{-1} = A^{-1}B^{-1} \\
(ABC)^T=C^TB^TA^T \\
R^T=R^{-1} \\
(A+B)^T = A^T+B^T \\
$$

# Based outside point



