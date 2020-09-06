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
