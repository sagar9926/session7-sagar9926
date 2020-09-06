# Created By : Sagar Agrawal

# EPAI : Session 7

### Question 1 . Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 PTS:100

```
#### Using lambda and reduce first create a function that to create Fibonacci series given number of series elements as inputs

fib  = lambda n : reduce(lambda x , _ :  x + [x[-1] + x[-2]] ,range(n-2), [0 , 1])

FIB_10000 = fib(10000)

Fib_Tester = lambda x : bool(list(filter(None ,  list([x in FIB_10000]))))

```
