# NumberScript

![PyPI - Downloads](https://img.shields.io/pypi/dm/NumberScript?color=blue&style=for-the-badge)

possibly the world's most simplest and restricted language.

## Installation

### pip

```bash
pip install NumberScript
```

## Features

- No spaces (Yup, you read that right)
- Comments
- Only 5 commands
- A shell and a runner
- No loops or If-else (Who needs 'em)

## Docs

### commands

```
commands:  0  |  1  |  2  |  3  | 4
comments: %
arithmetic: ^
Compare: = | ! | < | >
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
4a=Hello|2a|2Bye %Check-A-If-Its-Hello-Then-Display-It-Else-Display-Bye
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