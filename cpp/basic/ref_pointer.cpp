#include <iostream>
using namespace std;
/**
 * when we pass a pointer to the function as its parameter, 
 * we in true copy the pointer to the function 
 * when we change the pointer inside the function, 
 * we in true change the 'copy', the pointer outside will not change 
 */
int m_value = 1;
void from_pointer(int *p){ // need a pointer
   p = &m_value;
}
int t_from_pointer()
{
    int n =2;
    int *p = &n;
    cout<<&n<<endl;
    cout<<p<<endl;
    cout<<n<<endl;
    cout<<*p<<endl;

    from_pointer(p);
    cout<<*p<<endl;
    std::cout << "Hello world" << std::endl;
    return 0;
}

/**
 * use the pointer of a pointer as the parameter 
 */

void pp_func(int **p){
    *p = &m_value;
    
    //or 
    *p = new int;
    **p = 5;
}
int t_pp_func(){
    int n = 2;
    int *p = &n;
    cout<<*p<<endl;
    pp_func(&p);
    cout<<*p<<endl;
    return 0;
}

/**
 * use the reference of a pointer 
 */
 void ref_pointer(int *&p){
     p = &m_value;

     //or 
     p = new int;
     *p = 5;
 }
 int t_ref_pointer(){
     int n = 2;

     int *p = &n;
     cout<<*p<<endl;
     ref_pointer(p);
     cout<<*p<<endl;
     return 0;
 }

/**
 * copy the value
 * not change the original value
 */
int use_value(int a){
    cout<<a<<endl;
    return 0;
}
/**
 * copy the pointer 
 * will change the original value 
 */
int use_pointer(int* p){
    cout<<*p<<endl;
    *p = 10;
    cout<<m_value<<endl;
    return 0;
}
void t_use_pointer(){
    int n = 2;
    int* p = &n;
    use_pointer(p);
}
/**
 * use the reference,
 * will change original value
 */
int use_reference(int& p){
    cout<<p<<endl;
    p = 10;
    cout<<m_value<<endl;
    return 0;
}
/**
 * return pointer 
 */
 int* return_pointer(){
     int n  = 2;
     int *p = &n;
     cout<<"&n"<<&n<<endl;
     cout<<"p"<<p<<endl;
     return p;
 }
/** 
 * return reference 
 */
 int& return_reference(){
     /* int n = 2; */
     //must static or global value
     static int n=2;
     cout<<&n<<endl;
     return n;
 }

int main(int argc, char** argv){
    /* t_from_pointer(); */
    /* t_pp_func(); */
    /* t_ref_pointer(); */
    /* use_value(2); */
    /* use_pointer(&m_value); */
    /* t_use_pointer(); */
    /* use_reference(m_value); */
    /* cout<<return_pointer()<<endl; */
    cout<<&return_reference()<<endl;
    return 0;
}




























