# Longest Common Subsequence 

we are given two string, string S of length n, and string T of length m, our
goal is to produce their `longest common subsequence`.

For example, consider:
```txt
S = ABAZDC
T = BACBAD
```
In this case , the LCS has length 4 and is the string `ABAD` 

* LCS[i,j] is the length of LCS of S[1..i] with T[1..j]
1. S[i] != T[j], the desired subsequence has to ignore one of S[i] or T[j], so:
LCS[i,j] = max(LCS[i-1, j] , LCS[i, j-1])
2. S[i] = T[j],   
