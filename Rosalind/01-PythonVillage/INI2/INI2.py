"""
http://rosalind.info/problems/ini2/
Variables and Some Arithmetic

Problem
Given: Two positive integers aa and bb, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths aa and bb.

Sample Dataset
3 5
Sample Output
34
"""
# preparing file 
num = open ( "/Users/VickyVu/Desktop/Rosalind/01-PythonVillage/rosalind_ini2.txt")
num =  num.read().replace('\n','')
n = num.split() 

# selecting variables for calculation and turning them into integers 
a = ( int ( n [0])) 
print ( a)
b = ( int ( n [1])) 
print ( b )

# Calculate squared hypothenuse 

c = a**2 + b**2 
print ( c )
