#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    std::vector<int> w{2,3,4,5,9};
    std::vector<int> v{3,4,5,8,10};
    std::vector<vector<int> > w_order;
    int k = (int)w.size();
    w_order.resize(k);
    int max_weight = 20;
    
    for(int i =0 ;i < k; i++){
        w_order[i].resize(1);
    }

    w_order[k-1][0] = max_weight;

    for(int i =k-2; i>=0; i--){
        int sum_w = 0; 
        for(int j = i; j>=0; j--){
            sum_w += w[j];
        }

        cout<<"sum_w: "<< sum_w<<endl;
        //over weight 
        if(max_weight - w[i+1]  < sum_w){
            w_order[i][0] = w_order[i+1][0];
        }else{
            //not over weight 
            w_order[i][0] = w_order[i+1][0] - w[i+1]; 
            max_weight =  max_weight - w[i+1];
        }
        
    }
    for(int i =0;i < k ;i++){
        cout<<w_order[i][0]<<endl;
    }
    cout<<"该算法饶了个大圈，结果是错的，只要前i项之和不超过重量限制，前i项就都是计算结果"<<endl;
    return 0;
}

