# Technical Specifications - Team 3

- [Technical Specifications - Team 3](#technical-specifications---team-3)
  - [Overview](#overview)
  - [Cubes](#cubes)
  - [Tools](#tools)
  - [Room configuration](#room-configuration)
    - [Problems](#problems)
  - [Timelapse](#timelapse)
  - [Rubik's cubes configuration](#rubiks-cubes-configuration)
  - [Transport](#transport)
  - [Set up](#set-up)
  - [Removal](#removal)
  - [Python Coding Conventions and Best Practices (PEP 8)](#python-coding-conventions-and-best-practices-pep-8)
    - [Code Layout](#code-layout)
      - [Indentation](#indentation)
      - [Maximum Line Length](#maximum-line-length)
      - [Imports](#imports)
    - [Whitespace](#whitespace)
    - [Naming Conventions](#naming-conventions)
    - [Comments](#comments)
    - [Function and Method Signatures](#function-and-method-signatures)
    - [Coding Style](#coding-style)
  - [Program](#program)
    - [Open source](#open-source)
    - [Licence](#licence)
    - [Programming language](#programming-language)
  - [Code architecture](#code-architecture)
  - [Architecture diagram](#architecture-diagram)
  - [Risks](#risks)
  - [Tests](#tests)
  - [Security](#security)
  - [Trouble shooting](#trouble-shooting)
  - [Contact](#contact)
  - [Sources](#sources)
  - [Glossary](#glossary)


## Overview
<!-- link to github -->


## Cubes
- In order to realize our fresco, we have at our disposal 3000 Rubik's cubes of the 3x3x3 model. 
- These cubes are available in 6 colors: 
  - white <span style="color:#ffffff"> (#ffffff)</span>, 
  - red <span style="color:#f8001b"> (#f8001b)</span>, 
  - blue <span style="color:#0070dc"> (#0070dc)</span>, 
  - orange <span style="color:#ff6600"> (#ff6600)</span>, 
  - green <span style="color:#00e37a"> (#00e37a)</span>, 
  - yellow <span style="color:#dcd23c"> (#dcd23c)</span>.

- The dimensions of the cubes are 5.6cm x 5.6cm x 5.6cm, and their weight is 64g. 

## Tools

## Room configuration
<!-- plan 3D library -->
<!-- analyze of the wall -->
<!-- ALEXIS -->

The room is a rectangle of 8.3m of length and 3.8m of width. The wall is 2.5m of height.

According to the following pictures, the fresco will be placed against the white wall to be seen from the outside, or at least from the entrance of the building.

<img src="../images/external.jpg" alt="external" width="55%"/>

<img src="../images/northEastView.jpg" alt="northEastView" width="55%"/>

Unfortunately, we didn't have the idea of where put the bookshelves after the fresco installation.

<img src="../images/IMG_3585.jpg" alt="Fresco location" width="55%"/>

### Problems

There is a problem with the wall. With a bubble level, we found that the wall was not perfectly straight. The wall is inclined of 1cm from the top to the bottom. This problem is minor, but it will be necessary to take it into account when placing the cubes.

Another problem is the presence of roughness on the wall. It's important to notice it when we will place the tape on the wall.

## Timelapse

## Rubik's cubes configuration

## Transport

## Set up

## Removal

## Python Coding Conventions and Best Practices (PEP 8)


Our code will outlines the coding conventions and best practices for writing Python code, in accordance with the Python Enhancement Proposal 8 (PEP 8). Adhering to these guidelines ensures code consistency and readability, making it easier for developers to collaborate on the project.

### Code Layout

#### Indentation

- Use 4 spaces for indentation levels, not tabs.

```py
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

```py
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

#### Maximum Line Length

- Limit lines to a maximum of 79 characters for code and comments.
- For long lines, break lines at a suitable point and continue on the next line with a 4-space indentation.

#### Imports

- Import standard library modules first, followed by third-party libraries, and finally your project's modules.
- Separate import groups with a blank line.
- Avoid wildcard imports (`from module import *`) as they can lead to namespace pollution.

### Whitespace

- Use blank lines to separate functions, classes, and blocks of code within functions.
- Surround operators with a single space on each side (e.g., `x = 10`, not `x=10`).
- Avoid extraneous whitespace at the end of lines.

### Naming Conventions

- Use `lowercase_with_underscores` for variable and function names.
- Use `CamelCase` for class names.
- Use `UPPERCASE` for constants.
- Prefix non-public attributes and methods with a single underscore (e.g., `_private_variable`).
- Avoid using single-character variable names, except for temporary variables (e.g., `i`, `j`, `x`, `y`).

### Comments

- Use descriptive variable and function names to minimize the need for comments.
- Write comments in clear, concise English.
- Use docstrings to document classes, functions, and modules.
- Keep comments up to date with the code they describe.

### Function and Method Signatures

- Use meaningful parameter names.
- Include type hints for function and method arguments and return values.
- Use default values for optional function arguments instead of mutable objects (e.g., lists or dictionaries).

### Coding Style

- Follow the [Zen of Python (PEP 20)](https://peps.python.org/pep-0020/) principles.
- Be consistent with your code style throughout the project.
- Use spaces around operators for clarity.
- Use parentheses to clarify the order of operations, even if they are not required.

By adhering to these Python coding conventions and best practices as outlined in PEP 8, we can ensure that our code is consistent, readable, and maintainable. This promotes efficient collaboration among developers and enhances the overall quality of our project.

💡 For detailed guidelines and additional recommendations, refer to the full PEP 8 document at [PEP 8, Style Guide for Python Code](https://peps.python.org/pep-0008/).


## Program
<!-- no code in the doc-->
<!-- program open source -->
<!-- dependencies -->
<!-- use of API, open source code,... -->

<!-- LAURENT -->

### Open source
<!-- LL -->

### Licence
<!-- LL -->

### Programming language
<!-- why this one and the other + version-->

## Code architecture

## Architecture diagram

## Risks
-> wall not straight

<!-- MATHIS -->

## Tests
<!-- size rubik -->
<!-- quality assurance of the other groups -->
<!-- test of the program -->

<!-- MATHIS -->

## Security

## Trouble shooting
<!-- if you encounter this do that -->

## Contact

<!-- question about the program, this person, about the mana, this one, ... -->

|Name|Mail|Domain relate|
|----|----|------|
|Clémentine Curel|clementine.curel@algosup.com|Management|
|Laura-Lee Hollande|laura-lee.hollande@algosup.com|Management|
|Mathis Kakal|mathis.kakal@algosup.com|Design|
|Victor Leroy|victor.leroy@algosup.com|Rubik's cube|
|Laurent Bouqin|laurent.bouquin@algosup.com|Programs|
|Alexis Lasselin|alexis.lasselin@algosup.com|Programs, Rubik's cube|

## Sources
<!-- github link -->
[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
[PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)

## Glossary
github
open source
license
[PEP](https://realpython.com/python-pep8/#:~:text=The%20primary%20focus%20of%20PEP,and%20style%2C%20for%20the%20community.) : A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.
[PEP 8 – Style Guide for Python Code](https://realpython.com/python-pep8/#:~:text=The%20primary%20focus%20of%20PEP,and%20style%2C%20for%20the%20community.) : The primary focus of PEP 8 is to improve the readability and consistency of Python code.
[PEP 20 – The Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python) : The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language.

<!-- Create a table with "word", "definition" and "source" -->