# 动态规划

​	假设问题由交叠的子问题所构成，我们就能用动态规划来解决它。动态规划建议，与其对交叠子问题一次重新的求解，不如把每一个较小子问题仅仅求解一次，并把结果记录在表中，以空间换时间。这样就可以从表中得到原始问题的解。

​	能采用动态规划求解问题的一般具有3个性质：

* 最优化原理： 具有最优子结构
* 无后效性： 某阶段状态一旦确定，就不再受这个状态以后的决策影响。
* 有重叠子问题： 子问题之间是不独立的，一个问题在下一阶段决策中可能被多次用到。

## 步骤





##  技巧



## 典型案例

> 计算二项式系数

```c++
#include <stdio.h>
#define MAX 100
int BinoCoef(int n, int k);
int main(){
    int n, k, result;
    scanf("%d %d", &n, &k );
    result = BinoCoef(n,k);
    printf(result);
    return 0;
}
int BinoCoef(int n, int k){
    int data[MAX][MAX];
    int i,j;
    for(i=0;i<=n; i++){
        for(j=0;j<=((i<K)?i:k);j++){
            if(i==0 || i==j){
                data[i][j] =1;
            }else{
                data[i][j]=data[i-1][j]+data[i-1][j-1];
            }
        }
    }
    return data[n][k];
}
```





Reference:

[cnblogs](https://www.cnblogs.com/brucemengbm/p/6875340.html)