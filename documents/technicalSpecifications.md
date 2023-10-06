# Technical Specifications - Team 3

- [Technical Specifications - Team 3](#technical-specifications---team-3)
  - [Room configuration](#room-configuration)
    - [Problems](#problems)
  - [Timelaspe](#timelaspe)
  - [Rubik's cubes configuration](#rubiks-cubes-configuration)
  - [Transport](#transport)
  - [Set up](#set-up)
    - [Library setup](#library-setup)
    - [Fresco set up](#fresco-set-up)
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
  - [Software](#software)
    - [Open source](#open-source)
  - [Code architecture](#code-architecture)
  - [Architecture diagram](#architecture-diagram)
  - [Risks](#risks)
  - [Tests](#tests)
  - [Security](#security)
  - [Contact](#contact)
  - [Sources](#sources)
  - [Glossary](#glossary)

## Room configuration

The room is a rectangle of 8.3m of length and 3.8m of width. The wall is 2.5m of height.

According to the following pictures, the fresco will be placed against the white wall to be seen from the outside, or at least from the entrance of the building.

<img src="../images/external.jpg" alt="external" width="55%"/>

<img src="../images/northEastView.jpg" alt="northEastView" width="55%"/>

The size of the fresco is delimited by the tape of the wall.

<img src="../images/IMG_3585.jpg" alt="Fresco location" width="55%"/>

### Problems

There is a problem with the wall. With a bubble level, we found that the wall was not perfectly straight. The wall is inclined of 1cm from the top to the bottom. This problem is minor, but it will be necessary to take it into account when placing the cubes.

Another problem is the presence of roughness on the wall. It's important to notice it when we will place the tape on the wall.

<img src="../images/roughness.jpg" alt="roughness" width="55%"/>

And last but not least, the fact that even inside B3 (outside the library), the upper part of the fresco is barely visible to those looking at it, which is why we had to load the upper part as little as possible, so as to lose as few details as possible, but also to change the contrast between the filled lower part and the empty upper part.

## Timelaspe

To record the timelapse, we will use a GoPro 3 owned by one of our team member. 

The timelapse record will last for around 2 weeks. Starting when the final fresco will be selected, and will last until the fresco is finished.

We will be recording the different groups building the fresco, with their agreement, we could also record them doing the Rubik's cubes in their rooms, then follow them transporting the cubes to the library. 

The point of this timelapse will be to show to the other groups and keep memory of what we built, it will also be an interesting communication point for the school on social medias. 

The editing of the timelapse will be done with iMovie.

## Rubik's cubes configuration

To create the fresco, we need to know exactly how every face on the fresco will look like, that's why in the [Program](#program) section, we will explain how Laurent created a software that, with an image in input, outputs the configuration of the Rubik's cube of your choice.

The Rubik's cubes will be placed on the wall with double-sided tape, the tape will be placed on the corners of the rubik's cubes, making a big grid on the wall. Each tape will stick 4 cubes in one time, reducing the amount of tape used.

## Transport

The transfer between the project rooms and library will be done in 2 steps, the first one consisting on writing the coordinates of the place where the cube should be on the fresco with a pencil, in order to simplify the process if a cube is lost during the transport, it will be written on the opposite cube face of the one exposed in the fresco. The second step will be to take a cardboard to bring the cubes in the library.

## Set up

### Library setup

To prepare the library for the Rubik's cubes arrival, a grid will be drawn with a pencil on the wall.

The squares on the grid will have a size of 5.6 x 5.6 cm each, which is the size of a Rubik's cube. On each square, the number of the case will be written to easily find the right place for the Rubik's cubes. 

The same grid should be drawn on the printed fresco to have a reference for the actual fresco.

### Fresco set up

To 

## Removal

When the fresco will be removed or changed, it will probably leave some tape or marks on the wall. Removing the tape without damaging the wall will require a hair dryer. 

- Heat the corners and edges of the adhesive to soften the glue,
- Peel it off using a card or a spatula from the edge,
- Heat again if it doesn't peel off,
- If there is some glue left on the wall, use a sponge soaked in soapy water.

## Python Coding Conventions and Best Practices (PEP 8)

Our code will outline the coding conventions and best practices for writing Python code, according to the Python Enhancement Proposal 8 (PEP 8). Following these guidelines ensures code consistency and readability, making it easier for developers to collaborate on the project.

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

- Use descriptive variable and function names to minimize the need of comments.
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

For detailed guidelines and additional recommendations, refer to the full PEP 8 document at [PEP 8, Style Guide for Python Code](https://peps.python.org/pep-0008/).


## Software

The software that our group want to develop is meant to help people that want to create a Rubik's cubes pixel art reduce their searching time for colors. It will take a full image where total pixels can be divided by 3 and name each 3 by 3 with a grid name (e.g. "G23"). From that point, by selecting the grid name you want to check, the program will return an image of the face that will have to be at this adress on the pixel art. If the image's size can"t be divided by 3, it will mean that the size is not right, and it should return an error written in the "lastest.log" file.

The software should already have the image's path in the code as it is meant to be used by people with knowledge in software developement.

The software will be written in [Python 3.10.11](https://www.python.org/downloads/release/python-31011/) and will be compatible Windows and MacOs.

As it was decided by the group, the softawre will be open source to allow other people or co-workers to speed-up their work.

To develop this software, we will use libraries that are:
- Pillow : a library that manage images that will be useful to create the output image or to separate the pixels of the input image.
- Sys : The sys library is meant to allow the program to return system errors when a problem occurs.
- Datetime : This library allows the program to get the exact date and time and will serve when an error occurs to return the exact time of the error in the "lastest.log" file.
- Wxpython : It is a library that is used to render Graphical User Interfaces (GUI). We will use it to make our software more user friendly.

### Open source

We use an open source software developped by a team's member.

You can find our project on GitHub at the following repository:

[2023-2024-project-1-rubiks-art-team-3](https://github.com/AlexisLasselin/2023-2024-project-1-rubiks-art-team-3)

## Code architecture

## Architecture diagram

## Risks

- Wall not straight -> Use a bubble level to verify -> The wall is a bit inclined but it will works.
- Imperfections on the wall -> Avoid putting tape on those imperfections.

## Tests
<!-- size rubik -->
<!-- quality assurance of the other groups -->
<!-- test of the program -->
<!-- link to the mana doc -->

To ensure proper functioning of the program, you can find a Test plan on our [GitHub](https://github.com/AlexisLasselin/2023-2024-project-1-rubiks-art-team-3/tree/main).

To ensure proper installation of the fresco, there is a [documentation](#) in pdf where you can find how to use our program, how the ffresco will be set up with all the details.

## Security

This solution must not affect the security of other services, and systems.

The privacy of the users being very important, we decided to not save any kind of data in our programs.

## Contact

If you have questions during the project, you can contact the members of the teams depending of yours questions.

|Name|Mail|Domain relate|
|----|----|------|
|Clémentine Curel|clementine.curel@algosup.com|Management|
|Laura-Lee Hollande|laura-lee.hollande@algosup.com|Management|
|Mathis Kakal|mathis.kakal@algosup.com|Design|
|Victor Leroy|victor.leroy@algosup.com|Rubik's cubes|
|Laurent Bouqin|laurent.bouquin@algosup.com|Programs|
|Alexis Lasselin|alexis.lasselin@algosup.com|Programs, Rubik's cubes|

## Sources

[GitHub project](https://github.com/AlexisLasselin/2023-2024-project-1-rubiks-art-team-3/tree/main)

## Glossary

|Word|Definition|Source|
|-|-|-|
|PEP| A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.|[RealPython](https://realpython.com/python-pep8/#:~:text=The%20primary%20focus%20of%20PEP,and%20style%2C%20for%20the%20community.)|
|PEP 8|The primary focus of PEP 8 is to improve the readability and consistency of Python code.|[PEP 8 – Style Guide for Python Code](https://realpython.com/python-pep8/#:~:text=The%20primary%20focus%20of%20PEP,and%20style%2C%20for%20the%20community.)|
|PEP 20|The Zen of Python is a collection of 19 "guiding principles" for writing computer programs that influence the design of the Python programming language.|[PEP 20 – The Zen of Python](https://en.wikipedia.org/wiki/Zen_of_Python)|
|iMovie|iMovie is an editing software designed for iOS and MacOS, it allows the user to organize, edit and share videos. |[iMovie](https://www.apple.com/fr/imovie/)|
|GitHub|GitHub is a code hosting platform for version control and collaboration.|[GitHub](https://github.com/)|
|Open source|Open source is source code that is made freely available for possible modification and redistribution.|[Wikipedia](https://en.wikipedia.org/wiki/Open_source#:~:text=Open%20source%20is%20source%20code,model%20that%20encourages%20open%20collaboration.)|
|License|||