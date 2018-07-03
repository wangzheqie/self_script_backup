#include <iostream>
#include <vector>
#include <math.h>


int main(){
    std::vector<int> w{0,2,2,6,5,4};
    std::vector<int> v{0,6,3,5,4,6};
    std::vector<std::vector<int> > b;
    int k = 6;
    bool first_flag = true;

    b.resize(6);
    for(int i=0; i<k; i++){
	b[i].resize(10);
    }
    int max_weight = 10;

    for(int i=1; i<6; i++){
        for(int j=1; j<11; j++){
            if(first_flag){
                if(w[i] <=j){
                    b[i][j] = v[j];
                    first_flag=false;
                }
            }else{
                if(w[i] >j){
                    b[i][j] = b[i-1][j];
                }else{
                    b[i][j] = std::max(b[i-1][j], b[i-1][j-w[i]]+v[i]);
                }
            }
        }
    }
    for(int i=0; i<6; i++){
        for(int j=0;j<11;j++){
            std::cout<<i<<j<<":"<<b[i][j]<<std::endl;
        }
    }

    return 0;
}
