#include <iostream>
#include <vector>


using namespace std;
int main(){
    std::vector<int> w{0,2,2,6,5,4};
    std::vector<int> v{0,6,3,5,4,6};
    // std::vector<int> w{0, 1,2,3};
    // std::vector<int> v{0,60, 100,120};

    vector<vector<int> > b;
    int k = 6;
    int max_weight = 10;
    
    b.resize(k+1);
    w.resize(k+1);
    v.resize(k+1);
    
    for(int i=0;i<=k;i++){
        b[i].resize(max_weight+1);
        for(int j=0; j<=max_weight; j++){
            b[i][j] = 0;
        }
    }


    // //b[i][j] when the weight is j, the shopping can be 1~i

    // method 1
    b[0][0] = 0;
    for(int j=1; j<=max_weight; j++){
        b[0][j] = 0;
        for(int i =1; i<=k; i++){
            b[i][0] = 0;
            if(j<w[i]){
                b[i][j] = b[i-1][j];
            }else{
                b[i][j] = max(b[i-1][j], b[i-1][j-w[i]]+v[i]);
            }
        }
    } 
    cout<<"method 1"<<endl;
    cout<<b[k-1][max_weight]<<endl;

    // method 2
    b[0][0] = 0;
    for(int i=1; i<=k; i++){ //i the number of shopping, the left number of shopping
        b[i][0] = 0;
        for(int j=1; j<=max_weight; j++){ //the left weight
            b[0][j] = 0;
            if(j<w[i]){
                b[i][j] = b[i-1][j];
            }else{
                b[i][j]  = std::max(b[i-1][j], b[i-1][j-w[i]]+v[i]);
            }
        }
    }
    cout<<"method 2"<<endl;
    cout<<b[k-1][max_weight]<<endl;


    // for(int i=0;i<=k;i++){
    //     for(int j=0; j<=max_weight;j++){
    //         cout<<i<<j<<":"<<b[i][j]<<endl;
    //     }
    // }
    return 0;
}