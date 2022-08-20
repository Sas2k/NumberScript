# Variables

## What are variables?

variables are like boxes, in these boxes you can store stuff, for later.

- Strings
- Numbers

> Now you maybe asking, How does the interpreter check if the value contains String or Numbers. Well it firsts checks if the entire value contains only integers and is more then 1 character big. If this is so. It will turned into a number. If not it will be a string.

## Defining Variables in NumberScript

Now to define variables we need to use the `3` command.

so how to works is like this

`3Variable_name:Variable_Value`

now you can call variables in the display to If-Else commands, or just by them-selves to display the value.

Example:
```
    0
    3name:NumeroMan
    2name
    1
```

You can also have calculations in the vars with `^` we covered in the Basics.

`3one_plus_one:^1+1`

or user-input with the `~`

`3Name:~What's-your-name?`

## Exercise

Now that you learnt the basics of Variables.
Here is an exercise to try it out.

### 1) What's your name?

Here is a very easy exercise.
Using the input (~), Try and make a program where it asks for a name then prints it.

```
What's_your_name?NumeroMan
Hello,
NumeroMan
That's a good name
```

### 2) Bags of Bread.

In this one you have to write a program where it takes an input (which will be stored in a variable), and divides it by 2.
And tell you the equivalent amount of bags of bread.

```
Enter the amount of bread loaves>4
There are
2
bags of bread worth of bread.
```