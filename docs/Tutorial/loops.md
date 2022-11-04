# Loops

## What are loops?

now what loops do is repeat an instruction a number of time.

now imagine you have an instruction you have to do a 100 times.
you can write it 100 times. but that's not efficient. and it's not fun.
so instead you can use loops.

now in NumberScript there is only 1 type of loop. which is the for loop.

## Loops in NumberScript

now the syntax for loops is this

```
6loop-variable\repeat-count\loop-code
```

now the loop-variable is the variable that will be used to count the number of times the loop has been repeated.
the repeat count is the times it will repeat. the loop code is the instruction that will be repeated.

now let's see an example

```
6i\10\2i
```

here this will print the numbers from 0 to 9.

> Loops start from 0 so the first number will be 0. and the end number will be one less then the placed amount.

now let's see another example

```
6i\10\?i=5:2i|2i-is-5
```

here this will print the numbers from 0 to 9. but if the number is 5 it will print `i-is-5` instead.

## Exercises

### 1) Odd or Even

now, we made a program to see if the number is even or odd in the [If-Else](NumberScript/Tutorial/if-else/#even-or-odd) section. but now your task is to make it so the program loops through the numbers from 0 to 99 and prints if the number is even or odd.

here is the output.

```
0
is even
1
is odd
2
is even
3
is odd
...
```

### 2) FizzBuzz

Now your task is to create a FizzBuzz program where it loops over the numbers from 1 to 100 and prints `Fizz` if the number is divisible by 3, `Buzz` if the number is divisible by 5, `FizzBuzz` if the number is divisible by 3 and 5, and the number if it's not divisible by 3 or 5.

here is the output.

```
1
2
Fizz
4
Buzz
Fizz
7
8
...
```