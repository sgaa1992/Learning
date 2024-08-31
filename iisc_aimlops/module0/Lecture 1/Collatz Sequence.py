"""
7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1
19, 58, 29, 88, 44, 22, 11, 34 ....
Collatz Sequence
Write a function that takes the strating number as the parameter and returns the Collatz sequence.

Collatz sequence starts with the given number and ends in 4,2,1
"""


#Start

def collatz_fun (n: int) -> list[int]:
    seq=[n]
    while n>=2:
        if (n%2)==0:
            n=n//2
        else: 
            n=(3*n+1)
        seq.append(n)
    return(seq)
print(collatz_fun(7))
print(collatz_fun(19))


"""
Output: 
[7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
"""