"""
http://rosalind.info/problems/ini3/
Strings and lists
Problem
Given: A string ss of length at most 200 letters and four integers aa, bb, cc and dd.
Return: The slice of this string from indices aa through bb and cc through dd (with space in between), inclusively. In other words, we should include elements s[b]s[b] and s[d]s[d] in our slice.
Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102
Sample Output
Humpty Dumpty
"""
file = open ( "/Users/VickyVu/Desktop/Rosalind/rosalind_ini3.txt")
print ( file.read().replace( '\n', '' ))