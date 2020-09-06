# Created By : Sagar Agrawal

# EPAI : Session 7

### Question 1 : Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100

```
#### Using lambda and reduce first create a function that to create Fibonacci series given number of series elements as inputs
fib  = lambda n : reduce(lambda x , _ :  x + [x[-1] + x[-2]] ,range(n-2), [0 , 1])

#### Create a list containing first 10000 elements of a fibonacci series 
FIB_10000 = fib(10000)

#### Testing whether a number is fibonacci series or not
Fib_Tester = lambda x : bool(list(filter(None ,  list([x in FIB_10000]))))

```

### Question 2.1 : Using list comprehension (and zip/lambda/etc if required) write an expression that add 2 iterables a and b such that a is even and b is odd

```
#### Creating two lists of size 10 with random numbers
iter1 = [random.randint(0 , 100) for x in range(10)]
iter2 = [random.randint(0 , 100) for x in range(10)]

#### adding 2 iterables a and b such that a is even and b is odd
Result_2_1 = [a + b for a , b in zip(iter1,iter2) if (a%2 == 0) and (b%2 != 0)]

```

### Question 2.2 : Using list comprehension (and zip/lambda/etc if required) write an expression that strips every vowel from a string provided (tsai>>t s)

```
input_string = 'sagar'

#### An expression that strips every vowel from a string provided
print("".join([x if x.lower() not in ['a', 'e' , 'i' ,'o','u'] else " " for x in input_string]))

#### Output : s g r
```

### Question 2.3 : Using list comprehension (and zip/lambda/etc if required) write an expression that acts like a ReLU function for a 1D array

![](https://www.techvariable.com/wp-content/uploads/2018/11/7nn.png)

```
Relu_input = [random.randint(-100 , 100) for x in range(10)]
print(Relu_input)

#### Clipping the negative inputs and fixing them to zero
print([x if x>0 else 0 for x in Relu_input ])
```

### Question 2.4 : Using list comprehension (and zip/lambda/etc if required) write an expression that acts like a Sigmoid function for a 1D array

![](https://github.com/sagar9926/session7-sagar9926/blob/master/sigmoid.png)

```

Sigmoid_input = [random.random() for x in range(10)]
print(Sigmoid_input)

#### Sigmoid implementation
print([1 / (1 + exp(-x)) if x>0 else 0  for x in Sigmoid_input  ])

```

### Question 2.5 : Using list comprehension (and zip/lambda/etc if required) write an expression that takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn

```
input_string = 'tsai'

#### Expression that takes a small character string and shifts all characters by 5
print("".join([chr(ord(x) + 5 ) if ord(x) <= 117 else chr(96 + 5 - 122 - ord(x))  for x in input_string]))

```

### Question 3 : A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt PTS:200

```
#### Reading the data from file containing Swear texts
f = open("Swear_Words.txt",'r')
Swear_Words = f.read()
f.close()

Swear_Words = set(Swear_Words.split())


#### Reading the data from file containing Paragraph texts
f = open("Paragraph.txt",'r')
Paragraph = f.read()
f.close()

Paragraph = set(Paragraph.split())

#### A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words
print(any([x for x in Swear_Words if x in Paragraph]))

```



