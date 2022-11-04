# If Else in NumberScript

In this section we will cover If and Else in NumberScript.

## What's If Else?

An If Else statement is a statement where is checks a statement and see whether it's True or False.
If the Statement is False it will do the Else statement.

like If you have a movie-ticket you can watch a movie else you can't watch it.

## Defining and Using If-Else in NumberScript

now the basic structure of an If-Else is like this.

```
?statement|Do-If-True|else-do-this
```

now this is like the basic structure.
You can nest if-else inside if-elses, to check more cases if needed.

Here is an example of a program using If-Else,

```
%Password-Checker
0
3password:ThisIsCool
3input:~Enter-Password>
?input=password|2Access-Granted|2Wrong-Password
2Good-Bye
1
```

> Side-Note: You can have variables, math (and even inputs(~)) for the statement. The logic gates aren't yet implemented for these (and, or, not ones).

## Exercises

Now that you got the basics of the If-Else Sentences. try these exercises.

### 1) Even or Odd

In this exercise you must create a program where it will take an input and checks whether it is Even or Odd.

```
Enter-Number>4
It's Even
```

```
Enter-Number>5
It's Odd
```