

---

## Functions in Python – Simple Summary

* **Functions** are blocks of code that perform a task and can be reused.
* Python has many **built-in functions** like `print()`, `input()`, `range()`, `type()`.
* Extra functions are stored in **modules** and must be **imported** before use.

### Importing Functions

* Import a whole module:

  * `import math` → use as `math.sqrt()`
* Import a single function:

  * `from math import sqrt`
* Avoid `from module import *` because it makes code messy.

### Defining Your Own Functions

* Use the `def` keyword.
* Functions can take **parameters** and **return values**.
* If no `return` is used, the function returns `None`.
* Variables inside a function are **local**.

### Docstrings

* A **docstring** explains what a function does.
* Written using **triple quotes** as the first line in a function.

### Default Arguments

* Parameters can have default values.
* If not passed, the default is used.
* Default parameters must come **after** normal parameters.

### Keyword Arguments

* Arguments can be passed using their **names**.
* Order does not matter.
* Missing arguments use default values.

### Variable Length Arguments

* Use `*args` to accept **many positional arguments**.
* Use `**kwargs` to accept **many keyword arguments**.
* `*` → tuple
* `**` → dictionary

### Lambda Expressions

* **Lambda** is a small, anonymous function.
* Written in **one line** only.
* Useful when passing a function as an argument.
* Example use: sorting lists.

### Key Points

* Import only what you need.
* Functions help reuse code.
* Python supports flexible arguments.
* Lambda functions are short and powerful.

---

