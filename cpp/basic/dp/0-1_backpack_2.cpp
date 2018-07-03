#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

int main()
{
    std::vector<int> w{2,3,4,5,9};
    std::vector<int> v{3,4,5,8,10};
    int k = 4;
    int left_weight = 20;
    std::vector<int> b(k, 0); // all value 
    std::vector<bool> is_choice(k, false);
    
    for (int i = k; i >= 0; i-- ){
        //not choice 
        int not_choice = b[i];  
        //choice 
        int choice = b[i] + v[i];

        if(choice> not_choice){
            left_weight = left_weight - w[i];
            cout<<"left_weight: "<<left_weight<<endl;
            if(left_weight >= 0){
                b[i-1] = choice;
                is_choice[i] = true;
            }
        }else{
            b[i-1] = not_choice;
            is_choice[i] = false;
        }

    }
    for(int i =0 ;i<=k; i++){
        cout<<b[i]<<" "<<is_choice[i]<<endl;
    }
    std::cout << "Hello world" << std::endl;
    return 0;
}

