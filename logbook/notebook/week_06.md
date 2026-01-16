

---

## Lists and Tuples – Simple Summary

### Lists

* **Lists** store multiple values in an ordered way.
* Written using **square brackets** `[ ]`.
* Lists support **indexing, slicing, looping**, and **concatenation**.
* Lists are **mutable**, meaning they can be changed after creation.
* Lists have useful **methods** like:

  * `append()`, `extend()`, `insert()`
  * `remove()`, `pop()`, `clear()`
  * `sort()`, `reverse()`
  * `index()`, `count()`, `copy()`
* The `del` keyword can remove elements or the whole list.

### List Comprehensions

* A **short way** to create lists using a loop.
* Example:
  `[x*x for x in range(5)]`
* Can include **conditions** using `if`.
* Makes code **clean and readable**.

### Tuples

* **Tuples** are similar to lists but are **immutable** (cannot be changed).
* Written using **parentheses** `( )` or commas.
* Often store **different types of values**.
* Tuples are commonly used for **fixed data**.
* Elements are accessed using **indexing or unpacking**.

### Tuple Packing and Unpacking

* **Packing**: putting values into a tuple.
* **Unpacking**: assigning tuple values to variables.
* Number of variables must match tuple size.

### Tuples in Functions

* Tuples are used for **variable-length arguments** (`*args`).
* `*` can unpack a tuple when calling a function.

### Lists vs Tuples

* Lists → mutable, usually same type values.
* Tuples → immutable, usually different type values.
* Use **lists** when data needs to change.
* Use **tuples** when data should stay fixed.

### Key Points

* Lists and tuples are powerful data structures.
* Lists can change, tuples cannot.
* List comprehensions save time and code.
* Tuples are useful for grouping fixed data.

---

