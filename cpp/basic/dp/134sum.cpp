#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> a(10,0);
    int n =10;

    for(size_t i=0 ;i<a.size(); i++){
        cout<<a[i]<<endl;
    }
    a[0] = a[1] = a[2] = 1;
    a[3] =2;
    for(size_t i =4 ; i<=n; i++){
        a[i] = a[i-1]+a[i-3]+a[i-4];
    }
    for(size_t i=0 ;i<a.size(); i++){
        cout<<a[i]<<endl;
    }

    std::cout << "Hello world" << std::endl;
    return 0;
}

