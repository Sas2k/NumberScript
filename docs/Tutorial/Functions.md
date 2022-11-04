# Functions

## What are functions?

Functions are like a mini-program, that you can call in your main program.

so like in some text editors, let's take word for example. there is a button in the top corner that makes the text bold. this is a function. like this there a lot of functions in Word.

## Defining Functions in NumberScript

now to define functions we need the `7` command.

so the basic syntax is this

```
7function-name$function-arguments$function-body
```

now the function-name is the name of the function. the function-arguments are the arguments that the function takes. and the function-body is the code that the function runs.

so here is a function that adds two numbers and prints them.

```
7add$number1,number2$2^number1+number2
```

now how do I call this function well just do this

```
add$5,5
```

and it will print 10.

so how can I have more then one command in the function body?
well simply you can add the function code split in between the commands.
the function split is the `$`.

so here is our function that prints the sum of two numbers. but this function is different.
I changed it to display the double of the sum.

```
7add$number1,number2$3sum:^number1+number2$2^sum*2
```

so if we call this with `add$5,5` it will print 20.

and that's about it for functions.

## Exercises

Now that you got the basics of the functions. try these exercises.

### 1) fisherman's problem

now A fisherman has a brand new programmable fishing rod. now the rod is programmed with NumberScript.
so now the fisherman asks you to program the rod. since he is a fisherman he doesn't know how to program.

so he asks you to make a program to take input. the options are `1` for `small fish` and `2` for `big fish`.

now when the fisherman sees a small fish he input the option (1 for small fish, 2 for big fish) and the rod will ask him to input the weight of the fish. then the rod will display how hard to pull the line.

now the calculation on how to pull the small fish is `weight/2 + 1`.

for big fish it's `weight * 2 / 4 + 1`.

so here is an example input and output.

```
Enter-Option>1
Enter-Weight>4
Pull-the-fish-with,
3
grams
```

```
Enter-Option>2
Enter-Weight>10
Pull-the-fish-with,
6
grams
```