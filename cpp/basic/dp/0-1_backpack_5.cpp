#include <iostream>
#include <vector>

using namespace  std;
int main()
{
    vector<int> w{2,3,4,5,9};
    vector<int> v{3,4,5,8,10};
    int k=5;
    int max_weight = 20;
    vector<int> b;
    vector<bool> is_choice(k, false);

    b.resize(k);
    b[k-1] = max_weight;

    for(int i=k-1; i>=0; i--){
        //not choice 
        b[i-1] = b[i];
        //choice 
        b[i-1] = max(b[i] + v[i] , b[i]);
    }
    std::cout << "Hello world" << std::endl;
    return 0;
}

