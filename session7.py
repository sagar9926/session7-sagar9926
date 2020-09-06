from functools import reduce , partial
import random
from math import exp
import string

"""
Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not.
You can use a pre-calculated list/dict to store fab numbers till 10000 
"""

fib  = lambda n : reduce(lambda x , _ :  x + [x[-1] + x[-2]] ,range(n-2), [0 , 1])

FIB_10000 = fib(10000)

Fib_Tester = lambda x : bool(list(filter(None ,  list([x in FIB_10000]))))


## Using list comprehension (and zip/lambda/etc if required) write an expression that:

"""
1.) add 2 iterables a and b such that a is even and b is odd

"""

iter1 = [random.randint(0 , 100) for x in range(10)]
iter2 = [random.randint(0 , 100) for x in range(10)]

Result_2_1 = [a + b for a , b in zip(iter1,iter2) if (a%2 == 0) and (b%2 != 0)]

"""
2.) strips every vowel from a string provided (tsai>>t s)

"""

input_string = 'sagar'

print("".join([x if x.lower() not in ['a', 'e' , 'i' ,'o','u'] else " " for x in input_string]))

"""

3.) acts like a ReLU function for a 1D array

"""

Relu_input = [random.randint(-100 , 100) for x in range(10)]
print(Relu_input)
print([x if x>0 else 0 for x in Relu_input ])

"""

4.) acts like a sigmoid function for a 1D array

"""

Sigmoid_input = [random.random() for x in range(10)]
print(Sigmoid_input)
print([1 / (1 + exp(-x)) if x>0 else 0  for x in Sigmoid_input  ])


"""

5.) takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

"""
input_string = 'tsai'

print("".join([chr(ord(x) + 5 ) if ord(x) <= 117 else chr(96 + 5 - 122 - ord(x))  for x in input_string]))





## A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in 
##https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200

 
f = open("Swear_Words.txt",'r')
Swear_Words = f.read()
f.close()

Swear_Words = set(Swear_Words.split())

f = open("Paragraph.txt",'r')
Paragraph = f.read()
f.close()

Paragraph = set(Paragraph.split())

print(any([x for x in Swear_Words if x in Paragraph]))


## Using reduce function:

"""
1.) add only even numbers in a list

"""
list1 = [random.randint(0,100) for x in range(10)]
print(list1)
print(reduce(lambda a,b : a + b if b%2 == 0 else a ,list1))


"""
2.) find the biggest character in a stri

"""

sample_string = "".join([string.printable[random.randint(0,100)] for x in range(10)])
print(sample_string)

print(reduce(lambda a,b : a if ord(a) > ord(b) else b ,sample_string))


"""

3.) adds every 3rd number in a list

"""
list1 = [random.randint(0,100) for x in range(10)]

z = list(zip( list(range(1,len(list1) + 1)) , list1))

print(reduce(lambda a , b : a + b, [item[1] for item in list(filter(lambda  x : True if x[0]%3 == 0 else False ,z))]))


## Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates,
## where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

Alphabets = [chr(x) for x in range(65,91)]

["KA" + str(random.randint(10,99)) + random.choice(Alphabets) + random.choice(Alphabets) + str(random.randint(1000,9999)) for _ in range(15)]


## Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such 
## that 1000/9999 are hardcoded, but KA can be provided

def number_plate_generation(KA, DD, DDDD):
    return([ KA + str(random.randint(10,99)) + random.choice(Alphabets) + random.choice(Alphabets) + str(DDDD) for _ in range(15)])

f = partial(number_plate_generation, DDDD = '1234')
