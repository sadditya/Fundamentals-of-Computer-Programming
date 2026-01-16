
---

## Variables and Types – Simple Summary

* **Variables** store values so they can be used later.
* A variable name must start with a **letter or underscore**, not a number, and should be **meaningful**.
* Values are assigned using `=` (assignment), not comparison.

### Updating Variables

* Variable values can change:

  * `age = age + 1`
* Short forms (augmented assignment) make code easier:

  * `count += 1`, `score *= 5`

### Data Types in Python

* Python uses **dynamic typing** (type depends on value).
* Common types:

  * `int` → whole numbers
  * `float` → decimal numbers
  * `bool` → True / False
  * `str` → text (strings)
* Use `type()` to check a value’s type.

### Functions

* Functions perform tasks, e.g. `print()`, `type()`, `input()`.
* Functions can take **arguments** and may **return values**.

### Input and Output

* `print()` displays output.
* `input()` gets user input and always returns a **string**.
* Convert input when needed:

  * `int()`, `float()`

### Strings

* Strings can use **single**, **double**, or **triple quotes**.
* Special characters use **escape sequences** (`\n`, `\t`, `\"`).
* Strings support:

  * **Indexing** (`name[0]`)
  * **Negative indexing** (`name[-1]`)
  * **Slicing** (`name[1:4]`)
* Strings are **immutable** (cannot be changed).

### Lists

* Lists store **multiple values** in order.
* Written using square brackets `[ ]`.
* Lists support indexing, slicing, concatenation, and repetition.
* Lists are **mutable** (can be changed).
* Use `append()` to add elements.
* Slices can be used to **insert, replace, or remove** items.

### Length

* `len()` finds the number of elements in a string or list.

### Key Points

* Variables store typed values.
* Python types change dynamically.
* Strings cannot be changed; lists can.
* Indexing and slicing are powerful tools.

---