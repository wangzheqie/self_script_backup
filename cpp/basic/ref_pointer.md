# reference pointer 

to function , from function



## to function

```c++
//functions
func(a);
func(int* p);
func(int& p);
func(int** p);
func(int*& p);
// variables
int a = 2;
int* p = &a;
//use 
func(a); //copy the value
func(p); //copy the pointer, can change value
func(a); //use the pointer, can change value
func(&p); //copy the pointer of a pointer, can change pointer, can change value
func(&a /* or p */);//use the pointer, can change pointer, can change value

```

## from tunction

```c++
int* return_pointer(){
    int n = 2;
    static sn = 2;
    int* p = &n;
    return &n; // error, local variable
    return &sn; // ok
    return p; // ok
}// address: p = &n = (return p)

int& return_reference(){
    int n = 2;
    static sn = 2;
    return n; // error, local variable
    return sn; // ok
}// address: &sn = &return_reference()
```

