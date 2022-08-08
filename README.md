# NumberScript

![PyPI - Downloads](https://img.shields.io/pypi/dm/NumberScript?color=blue&style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dw/NumberScript?color=blue&style=for-the-badge)
![Discord](https://img.shields.io/discord/1005410273609400402?label=Discord&style=social)

[NumberScript Discord-Invite](https://discord.gg/wRXR72zJ6W)

possibly the world's most simplest and restricted language.

## Installation

### pip

```bash
pip install NumberScript
```

## Features

- No spaces (Yup, you read that right)
- Comments
- Only 8 commands
- A shell and a runner

## Docs

## CLI and repl

To use the repl just run,

`python -m NumberScript`

To run a file just use this,

`python -m NumberScript -f Path/To/File`

### commands

```
commands:  0  |  1  |  2  |  3  |  4  |  5  |  6 |  7
input: ~
comments: %
arithmetic: ^
Compare: = | ! | < | >
operations: + | - | * | / |
If-Else: ? :
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
?a=Hello:2a:2Bye %Check-A-If-Its-Hello-Then-Display-It-Else-Display-Bye
1 %Ends %The %program
```
You can also have that program like this
`0 3a:Hello 2a 4a=Hello:2a:2Bye 1`

Here is another program where it loops over digits to check if it's lucky
```
%Is-This-lucky:Checks-If-The-Number-Is-Lucky
0
3lucky_num:9
6n\10\?n=lucky_num:2n|2Is-The-Lucky-Number:2n|2Is-Not-The-Number
1
```

You can find more examples in the examples folder.

>So, since there aren't any spaces what can we use instead of them?
>You can use _ or -.

## To-Do

- [ ] Import and library system
- [ ] Possibly OOP