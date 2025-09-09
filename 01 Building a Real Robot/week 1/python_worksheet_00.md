# Python Basics - Introduction

**Instructions:** This worksheet will introduce you to the fundamental concepts of Python programming.
Complete all exercises and answer the questions thoughtfully.
Don’t worry about getting everything perfect, just focus on understanding the basics!

## **1. Data Types**

Python is fundamentally about creating and manipulating *objects*. Think of an object as anything you can represent: a number,
a word, a shape, or even a whole program! These objects are built using fundamental *data types*, like integers (numbers), 
strings (text), lists (collections of items), and dictionaries (key-value pairs). 
Each data type has its own properties and behaviors, but when combined with methods (functions that operate on the object),
they can create complex and useful representations in Python.  Essentially, objects are a way to represent real-world things
or abstract concepts, allowing you to build programs that interact with them effectively.

### Examples

| Data Type | Description | Example |
|---|---|---|
| Integer    | A whole number. | 10        |
| Float      | A number with a decimal point. | 3.14    |
| String     |  A sequence of characters. | "Hello" |
| List     |  A list of objects | [ 0, 1, "A string" ] |

## **2. Functions**

Functions are the building blocks of Python programs! They're like mini-scripts that perform specific tasks.
A function is essentially a block of code organized around a name (the function itself) and parameters: input values 
needed to execute the code.  Python has a powerful feature called duck typing, meaning you can treat any object as if 
it’s a function if it has the right methods. This allows you to define functions that take different data types as 
arguments, making your code much more flexible and reusable. Functions are essential for breaking down complex problems 
into manageable steps, promoting modularity and making your programs easier to understand and maintain.

<div style="page-break-after: always;"></div>

### Example

*   A *function* called `greet` that takes one argument (the person's name) and prints a greeting message.
```python
def greet(name):
  print("Hello, " + name + "!")

greet("Alice") # Output: Hello, Alice!
```


## **3. Control Flow - If-Else Statements**

If-else statements are the cornerstone of conditional logic in Python! They allow you to execute different blocks 
of code based on whether a condition is true or false.  The if statement checks a condition; if it's true, then the
code block following it executes; otherwise, the code block after else (or the implicit ‘else’ if no elif is present)
executes. The else clause provides an alternative course of action when the condition in the if statement is false. This 
code will be executed only if none of the conditions within the if statement are met.  These statements are incredibly useful 
for creating decision-making logic and controlling program flow, making your programs more dynamic and adaptable.

### Example

*   An if statement to check if a number is positive or negative.  Return "Positive" if true, "Negative" if false.
```python
def check_number(number):
  if number > 0:
    return "Positive"
  else:
    return "Negative"

print(check_number(5)) # Output: Positive
print(check_number(-3)) # Output: Negative
```

## **4. Loops - For and While Loops**

Loops are essential tools for repeating blocks of code multiple times. Python offers a couple loop types: `for` loops 
(used to iterate over sequences like lists or strings), `while` loops (used to execute code as long as a condition is true).
A for loop repeatedly executes a block of code for each item in a sequence, while a while loop continues executing the block 
until a certain condition becomes false. Python’s `break` and `continue` statements allow you to control the flow within these 
loops, enabling you to execute different parts of your program based on conditions and patterns.

### Examples

*   A program that prints the numbers from 1 to 5 using a `for` loop.
```python
for i in range(1, 6):  # Print numbers from 1 to 5
  print(i)
```

*   A program that calculates the sum of numbers from 1 to 10 using a `while` loop.  Stop when the number is 10.
```python
count = 1
while count <= 10:
  print(count)
  count += 1
```

---

**Questions:**

1.  What is the difference between an integer and a float?
2.  How do you print the output of a function in Python?
3.  Explain what happens when you try to run a program that doesn’t have any code.
