# NumberScript

possibly the world's most simplest and restricted language.

## Features

- No spaces (Yup, you read that right)
- Comments
- Only 4 commands
- A shell and a runner

## Docs

### commands

```
commands:  0  |  1  |  2  |  3  |
comments: %
arithmetic: ^
operations: + | - | * | / |
```

>NOTE: You can't have different arithmetic signs in a single ^
>    : so you can do this 1+1+2 but not 1+1*2
>    : Also NO SPACES.

### syntax

A basic program
```
%Test.ns
0 %Starts %The %Program
3a:Hello %Sets %The %Variable %a %to %Hello
2a %Displays %a
1 %Ends %The %program
```

Addition
```
%calculating
0
3a:4
3b:8
^a+b %NoSpacesPlease
1
```
>So, since there aren't any spaces what can we use instead of them?

You can use _ or -.

## To-Do

- [ ] If-Else