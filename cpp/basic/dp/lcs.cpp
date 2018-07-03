#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool same(char s1, char s2){
    return s1==s2 ? 1 : 0;
}
int main()
{
    string x="abcd";
    string y="acqb";
    int n = x.length();
    int m = y.length();

    // store matrix 
    vector<vector<int > > f;
    f.resize(n+1);
    for(int i=0; i<n; i++){
        f[i].resize(m+1);
    }
    
    //initialize value 
    f[0][0] = same(x[0], y[0]);

    // fill matrix 
    // start position , end position 
    for (int i=1; i<=n; i++){
        for(int j =1; j<=m; j++){
            //jump direction
            if(x[i-1] == y[j-1]){
                f[i][j] = f[i-1][j-1] +1;

            }else if(f[i-1][j] > f[i][j-1]){
                f[i][j] = f[i-1][j];
//                f[i][j] = max(f[i][j-1], f[i-1][j-1]);
            }else{
                f[i][j] = f[i][j-1];
            }
            cout<<i<<j<<": "<<f[i-1][j-1]<<endl;
        }
    }
    std::cout << "Hello world" << std::endl;
    return 0;
}

