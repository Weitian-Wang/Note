- [1 Array](#1-array)
  - [1.1 One-Dimensional Array Declaration/Initialization](#11-one-dimensional-array-declarationinitialization)
    - [1.1.1 By Specifying Size](#111-by-specifying-size)
    - [1.1.2 By Initializing All Elements](#112-by-initializing-all-elements)
    - [1.1.3 By Size and Initializing Elements](#113-by-size-and-initializing-elements)
  - [1.2 One-Dimensional Array as Parameters/Arguments](#12-one-dimensional-array-as-parametersarguments)
    - [1.2.1 Parameter](#121-parameter)
    - [1.2.2 Argument](#122-argument)
  - [1.3 Two-Dimensional Array Declaration/Initialization](#13-two-dimensional-array-declarationinitialization)
    - [1.3.1 Initialize with Element Values](#131-initialize-with-element-values)
    - [1.3.2 Initialize all Elements](#132-initialize-all-elements)
    - [1.3.2 Understand 2-D Array](#132-understand-2-d-array)
  - [1.4 Two-Dimensional Array as Parameters/Arguments](#14-two-dimensional-array-as-parametersarguments)
- [2 Structure](#2-structure)
  - [2.1 Definition](#21-definition)
    - [2.1.1 Definition of Structure Then Define Variable](#211-definition-of-structure-then-define-variable)
    - [2.1.2 Define Variable When Defining Structure](#212-define-variable-when-defining-structure)
    - [2.1.3 Define Structure Variable Without Defining Structure Type](#213-define-structure-variable-without-defining-structure-type)
    - [2.1.4 Alias for Structure](#214-alias-for-structure)
  - [2.2 Initialize Members of Structure](#22-initialize-members-of-structure)
    - [2.2.1 Initialize at Declaration](#221-initialize-at-declaration)
    - [2.2.2 Declare then Initialize](#222-declare-then-initialize)
    - [2.2.3 Initialize Each Member Individually](#223-initialize-each-member-individually)
  - [2.3 Access Members](#23-access-members)
    - [2.3.1 Normal Structure Variable](#231-normal-structure-variable)
    - [2.3.2 Pointer Structure Variable](#232-pointer-structure-variable)
- [3 Object Oriented](#3-object-oriented)
  - [3.1 Classes and Objects](#31-classes-and-objects)
    - [3.1.1 Define Classes](#311-define-classes)
    - [3.1.2 Declare Objects](#312-declare-objects)
    - [3.1.3 Access Members](#313-access-members)
  - [3.2 Inheritance](#32-inheritance)
  - [3.3 Encapsulation](#33-encapsulation)
  - [3.4 Abstraction](#34-abstraction)
  - [3.5 Polymorphism](#35-polymorphism)
- [4 Algorithmic Libraries](#4-algorithmic-libraries)
  - [4.1 Vector](#41-vector)
    - [4.1.1 Template Specializations](#411-template-specializations)
    - [4.1.2 Member Types](#412-member-types)
    - [4.1.3 Member Functions](#413-member-functions)
    - [4.1.3 Non-Member Functions](#413-non-member-functions)
  - [4.2 Maps](#42-maps)
  - [4.3 List](#43-list)
  - [4.4 List Map Unordered List etc. etc.](#44-list-map-unordered-list-etc-etc)
- [Appendix of Acronyms](#appendix-of-acronyms)

## 1 Array

### 1.1 One-Dimensional Array Declaration/Initialization

#### 1.1.1 By Specifying Size

```c
// declaration by constant size
int arr1[10];

// in recent c/c++ version
// declaration by variable is possible
// not safe to use
int size = 10;
int arr1[size];
```

#### 1.1.2 By Initializing All Elements

```c
int arr2[] = [1, 2, 3]
```

#### 1.1.3 By Size and Initializing Elements

```
int arr3[6] = [1, 2, 3]
// the uninitialized elements will be filled with 0s in cases of int array type
// or other default value of data type
```

### 1.2 One-Dimensional Array as Parameters/Arguments

> Parameters are listed when the function is defined.
>
> Arguments are passed/supplied to the function at function calls.

#### 1.2.1 Parameter

**Caution: no size given when defining parameters!**

```c
// Caution: no size given as param
return_type func_name(arr_elem_type arr[]){
  // function body
};
```

#### 1.2.2 Argument

```c
int arr[10] = {1, 2, 3};
// supply name of array as argument
func_name(arr, max_idx);
```

Name of the array is the equivalent of the **address of the first byte** of the array.

In case of index goes out of bounds, conventionally we supply the size of the array as a argument.

> ```sizeof()``` function calculates the byte size of the target
>
> ```array_size = sizeof(arr) / sizeof(arr[0])``` **won't** work after ```arr``` passed into the func as arg

**Access** the elements of the array within a function:

```c
// access with corresponding index
return_type func_name(arr_elem_type arr[], int max_idx){
	for(int idx = 0; idx <= max_idx; idx ++){
	printf("%d ",arr[idx]);
  }
};

// access & traverse by manipulating address(pointer)
return_type func_name(arr_elem_type arr[], int max_idx){
	arr_elem_type *it = arr;
  while(it <= arr+sizeof(arr_elem_type*max_idx)){
    printf("%d ", *(it++));
  }
};
```

### 1.3 Two-Dimensional Array Declaration/Initialization

#### 1.3.1 Initialize with Element Values

```c
int arr1[2][3] = {{1, 2}, {4}};
// the size of 1st dimension can be ignored
// just like the declaration and initialization of one-dimensional array
int arr2[][3] = {{1, 2}, {4}};
```

#### 1.3.2 Initialize all Elements

```c
int arr3[][3] = {1, 2, 3, 4, 5, 6};
```

Although to a programmer the array appears to be two dimensional, they are actually stored **consecutively** one row following another. The relative "distance" away from the first element can be calculated like:

Assume array defined like:
$$
type\ arr[m][n];
$$
When access ```arr[i][j]```, the compiler will convert the row number i and column number j into the actual physical address it should access:
$$
distance = i\times n + j
$$

$$
addr = arr\_start\_addr + distance
$$

#### 1.3.2 Understand 2-D Array

We can perceive the 2-D array as a array with 1-D arrays as its elements. 

For instance ```data_type arr[m][n]``` contains m data_type 1-D arrays, ```arr[0] - arr[m-1]``` each stores the first byte of its address
$$
{\underline{arr[0][1]\ arr[0][2]\dots arr[0][n-1]}\\
arr[0]}
\\
{\underline{arr[1][1]\ arr[1][2]\dots arr[1][n-1]}\\
arr[1]}
\\
\vdots
\\
{\underline{arr[m-1][1]\ arr[m-1][2]\dots arr[m-1][n-1]}\\
arr[m-1]}
$$
Now we can see ```arr[0] - arr[m-1]```  as a 1-D array with addresses as its elements. Therefore, extend the theory of 1-D array name, 2-D array name refers to an address where the first address is stored. (lmao confusing)

The following equations hold true for 2-D arrays.
$$
arr[i] = \&arr[i][0]
$$

$$
arr = \&arr[0]
$$

> & gets the address of the operand variable name

### 1.4 Two-Dimensional Array as Parameters/Arguments

Have to specify the size of second dimension of 2-D array when defining the parameters of a function.

```c
void func(int arr[][10]){
// function body
}
```

## 2 Structure

Structure is a user defined data type that allows the combination of items of different kinds. 

### 2.1 Definition

#### 2.1.1 Definition of Structure Then Define Variable

```c
// definition of structure type struct_tag
struct struct_tag{
  member_type1 member1;
  member_type2 member2;
  // ...
};
// definition of corresponing variable
struct struct_tag var1, var2;
```

#### 2.1.2 Define Variable When Defining Structure

```c
struct struct_tag{
  member_type1 member1;
  member_type2 member2;
  // ...
} var1, var2;
```

#### 2.1.3 Define Structure Variable Without Defining Structure Type

Similar to the previous method, hold the struct_tag.

```c
struct { 
  member_type1 member1;
  member_type2 member2;
  // ...
} var1, var2;
```

#### 2.1.4 Alias for Structure

```c
typedef struct [struct_tag]{
  member_type1 member1;
  member_type2 member2;
  // ...
} structure;
// 'sturcture' is now a type name rather than a variable
structure var1, var2;
```

Breakdown: this method =  1.2.1 definition of structure + typedef an additional name for the structure

> **definition** is used when you describe a variable, **declaration** is when you allocate memory for it, **initialization** is when you give it a first value during declaration.

### 2.2 Initialize Members of Structure

#### 2.2.1 Initialize at Declaration

```c
struct struct_tag var1 = {m1_val, m2_val, ...};
struct struct_tag var2[] = {{m11_val, m12_val, ...},{m21_val, m22_val, ...}};
```

#### 2.2.2 Declare then Initialize

```
struct struct_tag var;
var = {m_val, m_val, ...};
```

#### 2.2.3 Initialize Each Member Individually

```c
struct struct_tag var1;
var.member1 = val1;
var.member2 = val2;
```

### 2.3 Access Members

#### 2.3.1 Normal Structure Variable

```c
struct struct_tag var1 = {m1_val, m2_val, ...};
struct struct_tag var2[] = {{m11_val, m12_val, ...},{m21_val, m22_val, ...}};

auto target = var1.member1;
auto target = var2[0].member1;
```

#### 2.3.2 Pointer Structure Variable

```c
struct struct_tag *var = &var1;

auto target = var->member1;
```

## 3 Object Oriented

**Object-oriented programming (OOP)** is a programming paradigm that relies on the concept of **classes** and **objects**. The four principles of OOP are **Inheritance**, **Encapsulation**, **Abstraction** and **Polymorphism**.

> Inheritance: child classes inherit data and behaviors from parent classes
>
> Encapsulation: containing information in an object, exposing only selected information
>
> Abstraction: only exposing high level public methods for accessing an object
>
> Polymorphism: many methods can do the same task

### 3.1 Classes and Objects

Classes are the building block in object-oriented programming languages like C++ and Java. A class holds its own data members and member functions, which we can access by creating an instance of the class. Metaphorically, classes are blueprints whereas their corresponding objects/instances are tangible products manufactured according to the blueprints.

> An object works as an instance of the class.

#### 3.1.1 Define Classes

```cpp
class class_name{
  [public:|private:|protected:]
  data_type data_member;
  // constructor
  class_name(para1, para2, ...){
    this.member1 = para1;
    this.member2 = para2;
    // this is a keyword refers to current instance of the class
  }
  // destructor
  ~class_name(){
    cout<<"Destructor called"<<endl;
	}
  return_type function_memeber(){
    // function body
  }
};
```

Define a function outside class:

```cpp
class Resident{
  public:
  string name;
	// the declaration of the function is within the definition of class
  // function body not implemented
  void print_name();
};

// scope resolution operator ::
void Resident::print_name(){
	cout<<"Resident name is: "<<name;
}
```

#### 3.1.2 Declare Objects

Declare an object of the class and initialize the instance using the corresponding constructor.

```cpp
class_name obj(arg1, arg2, ...);
```

#### 3.1.3 Access Members

Access Data Members

The public data members are also accessed in the same way given however the private data members are not allowed to be accessed directly by the object. Accessing a data member depends solely on the access control of that data member.

```cpp
// within classes
class class_name{
	data_type member1;
  void print(){
		cout<<member1<<endl;
  }
}
// outside classes
cout<<obj.member1<<endl;
```

Access Functions

```cpp
obj.print();
```

### 3.2 Inheritance

Child classes inherit information (data members) and behavior (function members) from parent classes. C++ supports multiple inheritance, as a child class can be derived from multiple parent classes.

```cpp
class p1{ p1(){cout<<"p1 constructor called"<<endl;} };
class p2{ p2(){cout<<"p2 constructor called"<<endl;} };
class p3{ p3(){cout<<"p3 constructor called"<<endl;} };

class child: public p1, public p2, public p3{
  public:
  child(){
    cout<<"child constructor called"<<endl;
  }
}

child c();
```

Output:

```
p1 constructor called
p2 constructor called
p3 constructor called
child constructor called
```

Constructors of parent classes are call in the same order as they are inherited. The destructors are called in reverse order of constructors.

### 3.3 Encapsulation

In OOP encapsulation refers to binding the data and the function that manipulates them together. As using encapsulation also hides the data (abstraction), as they can only be accessed or manipulated  with corresponding functions.

```cpp
class student{
  private:
  string name;
 	int id;
  public:
  print_name(){cout<<name<<endl;}
  change_id(int new_id){id = newid;}
}
```

### 3.4 Abstraction

Abstraction means displaying only essential information and hiding the details. Data abstraction refers to providing only essential information about the data to the outside world, hiding the background details or implementation. 

Abstraction can be accomplished by using access specifiers like public, protected and private which enforces restrictions on class members. 

For instance, the private data member ```width``` and ```height``` in the following code block can be accessed only by the function within the class. Therefore achieving some level of abstraction.

```cpp
class rectangle{
  private:
  int width;
  int height;
  public:
  // constructor
  rectangle(int w, int h)}{
  	width = w;
  	height = h;
  }
	int get_area(){
		return width*height;
  }
	int get_perimeter(){
    return 2*width+2*height;
  }
}
```

### 3.5 Polymorphism

Polymorphism refers to the same entity (function or object)  behaves differently in different scenarios.

Types of polymorphism:

1. Compile Time Polymorphism

   * function overloading

      ```cpp
      class cal{
        // assume this function as base line
        int add(int a, int b){return a+b;}
      	// different numbers of arguments  
        int add(int a){return a+1;}
        // different argument types
        string add(string s1,string s2){return s1+s1;}
      }
      ```

   * operator overloading

      ```cpp
      // ++var
      rectangular& rectanglar::operator ++(){
        width++;
        height++;
        return this;
      }
      
      // var++
      rectangular rectangular::operator ++(int){
        rectangular prev = this;
        width++;
        height++;
        return prev;
      }
      ```

2. Runtime Polymorphism

   * function overriding
   
     ```cpp
     class Animal {  
       public:  
       void function(){    
         cout<<"Eating ..."<<endl;    
       }      
     };   
     
     class Man: public Animal{ 
       public:  
      	void function(){    
     		cout<<"Walking ..."<<endl;    
     	}    
     };  
     int main(void){
      	Man m();
       m.function();
     }
     
     output:
     Walking ...
     ```
   
   * virtual function
   
     Use a pointer to base class that refers to all derived objects to achieve runtime polymorphism.
   
     ```cpp
     class Base{
     	virtual void print(){
         cout<<"base function"<<endl;
       }
     };
     
     class Derived: public Base{
     	void print(){
         cout<<"derived function"<<endl;
       }
     };
     
     int main(void){
       Base *ptr;
       Derived d;
       ptr = &d;
       d->print();
     }
     
     output:
     derived function
       
     if no virtual keyword in base class function:
     base function
     ```

> Override: give new definition to the function in the derived classes
>
> Overwrite:  arguable, have a closer meaning to **override**, when the two or more parents shares the same base class, use virtual keyword to be overridden in derived class
>
> Overload: a single function can perform multiple tasks given different types and numbers (signature) of arguments

## 4 Algorithmic Libraries

### 4.1 Vector

Header: ```<vector>```

Vectors are sequence containers representing arrays that can change in size.

#### 4.1.1 Template Specializations

 ```vector<data_type>```

#### 4.1.2 Member Types

1. ```iterator```
2. ```reverse_iterator```

#### 4.1.3 Member Functions 

1. constructor

   ```cpp
   vector<int> vec = {0,1,2,3};
   vector<vector int> matrix = {{1,3,4},{2,1},{0,1,2,3,4}};
   ```

2. = (assign content)

3. 

#### 4.1.3 Non-Member Functions

### 4.2 Maps



### 4.3 List



### 4.4 List Map Unordered List etc. etc.

Random Azure Tech Lead: don't use predefined library

## Appendix of Acronyms

| **Acronym**      | **Full Form**                                         |
| ---------------- | ----------------------------------------------------- |
| -R               | Recordable                                            |
| -RW              | ReWritable                                            |
| AI               | Artificial Intelligence                               |
| AP               | Access Point                                          |
| API              | Application Programming Interface                     |
| AR               | Augmented Reality                                     |
| ATM              | Automatic Teller Machine                              |
| CAD              | Computer-aided Design                                 |
| CD               | Compact Disc                                          |
| CISC             | Complex Instruction Set Computer                      |
| CPU              | Central Processing Unit                               |
| CSS              | Cascading Style Sheets                                |
| DAP              | Distributed Array Processor                           |
| DB               | Database                                              |
| DBMS             | Database Management System                            |
| DNN              | Deep Neural Network                                   |
| DNS              | Domain Name System                                    |
| DOM              | Document Object Model                                 |
| DOS              | Disk Operating System                                 |
| DRAM             | Dynamc                                                |
| DS               | Distributed System                                    |
| DTD              | Document Type Definition                              |
| E-R Model        | Entity-Relationship                                   |
| EEPROM           | Electrically Programmable Read Only Memory            |
| EPROM            | Erasable Programmable Read Only Memory                |
| ES               | Expert System                                         |
| FTP              | File Transfer Protocol                                |
| GIF              | Graphic Interchange Format                            |
| GIS              | Geographic Information System                         |
| GPS              | Global Positioning System                             |
| GPU              | Graphics Processing Unit                              |
| GUI              | Graphic User Interface                                |
| HD               | High Definition                                       |
| HIFI             | High Fidelity                                         |
| HTML             | Hypertext Markup Language                             |
| HTTP             | Hypertext Transfer Protocol                           |
| I/O              | input/output                                          |
| IP               | Internet Protocol                                     |
| ISP              | Internet Service Provider                             |
| JIT              | Just in Time                                          |
| JPEG             | Joint Photographic Experts Group                      |
| LAN              | Local Area Network                                    |
| LSI              | Large-Scale Integrated Circuit                        |
| MIDI             | Musical Instrument Digital Interface                  |
| MIPS             | Million Instructions Per Second                       |
| MISD             | Multiple Instruction Single Data Stream               |
| MPEG             | Motion Pictures Experts Group                         |
| MRI              | Magnetic Resonance Imaging                            |
| NN               | Neural Network                                        |
| OEM              | Original Equipment Manufacturer                       |
| OS               | Operating System                                      |
| PAN              | Personal Area Network                                 |
| PC               | Personal Computer                                     |
| PDA              | Personal Digital Assistant                            |
| PnP              | Plug and Play                                         |
| PROM             | Programmable Read Only Memory                         |
| RAM              | Random Access Memory                                  |
| RDF              | Resource Description Format                           |
| RISC             | Reduced Instruction Set Computer                      |
| ROM              | Read Only Memory                                      |
| RTOS             | Real Time OS                                          |
| SE               | Software Engineering                                  |
| SIMD(DAP)        | Single Instruction Multiple Data Stream               |
| SISD von Neumann | Single Instruction Single Data Stream                 |
| SMS              | Short Message Service                                 |
| SQL              | Structured Query Language                             |
| SRAM             | Static                                                |
| SSD              | Solid State Drive                                     |
| SSI              | Small-Scale Integrated Circuit                        |
| TCP              | Transmission Control Protocol                         |
| UML              | Unified Modeling Language                             |
| URI              | Uniform Resource Identifier                           |
| URL              | Uniform Resource Locator                              |
| USB              | Universal Serial Bus                                  |
| VDT              | Video Display Terminal                                |
| VM               | Virtual Machine                                       |
| VR               | Virtual Reality                                       |
| VSLI             | Very Large Scale Integrated Circuit                   |
| WAN              | Wide Area Network                                     |
| WAP              | Wireless Access Point / Wireless Application Protocol |
| WLAN / Wi-Fi     | Wireless Local Area Network                           |
| WML              | Wireless Markup Language                              |
| WORM             | Write Only Read Many                                  |
| WWW              | World Wide Web                                        |
| XHTML            | Extensible Hypertext Markup Language                  |
| XML              | Extensible Markup Language                            |
| XSL              | Extensible Stylesheet Language                        |                                              |