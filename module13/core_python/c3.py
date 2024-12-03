
"""
What are operators and operands in python?

Operators are used to perform operations on variables/operands and values. They are classified into arithmetic, assignment, comparison, logical, bitwise, membership, and identity operators.

Arithmetic operators: +, -, *, /, //, %, **
Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
Comparison operators: ==,!=, <, >, <=, >=
Logical operators: and, or, not
Membership operators: in, not in
Identity operators: is, is not
Bitwise operators: &, |, ^, ~, <<, >>


"""
#arithmetic 
x=int(input("number:"))
y=int(input("number:"))
print("sum =" ,x+y)
print("sub =" ,x-y)
print("maltiply =" ,x*y)
print("division =" ,x/y)
print("floor division =" ,x//y)
print("Exception=" ,x**y)
  

#logical  and,or,not
c1=False
c2=True
c3=3.60<90 or False
c4=9.78<4.5 and True or 8.9>5.2

print(c4)
print(c1 and c2)
print(c2 and c3)
print(c3 and c4)
print(c4 and c1)
print(c1 or c2 and c4)


#assinging operator +=,==,-=,/=,*=,**=,//=,
num=40
print(num)
num+=20
print(num)
num-=10
print(num)
num/=2
print(num)
num//=3 #3*8=24 # ans=8.0
print(num)
num*=4
print(num)

# Bitwise operators: &, |, ^, ~, <<, >> 
print(7 & 4)
print(7 | 4)
print(7 ^ 4)
print(7 << 4)
print(7 >> 4)

  
