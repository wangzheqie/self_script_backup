#include <iostream>
#include <string>
#include <vector>

using namespace std;

int k = 2;
int size = 10;
//b.insert(b.begin(), a, a+10);
//copy(a.begin(), a.end(), b.begin());
std::vector<int> getData(){
    int a[] ={1,6,7,4,5,3,2,8,9,10};
    std::vector<int> b[10];
    for(int i =0; i<size; i++){
        cout<<a[i];
    }
    return *b;

}

void kdtree(std::vector<int> &data, int depth){
    int axis = (int) depth % k;
    //std::sort

}
int main()
{
    std::vector<int> data = getData();
    kdtree(data, 10);
    std::cout << "Hello world" << std::endl;
    return 0;
}

