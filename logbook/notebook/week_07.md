

---

## Sets and Dictionaries – Simple Summary

### Sets

* A **set** stores multiple values **without duplicates**.
* Sets are **unordered**, so no indexing or slicing.
* Only **immutable values** (like numbers, strings) are allowed.
* Sets are **mutable** (values can be added or removed).
* Used for **membership testing** and set operations.
* Common operations:

  * **Union** (`|`)
  * **Intersection** (`&`)
  * **Difference** (`-`)
  * **Symmetric Difference** (`^`)
* An **empty set** is created using `set()`.
* **frozenset** is an **immutable set**.
* Set comprehensions use `{ }`.

### Dictionaries

* A **dictionary** stores data as **key : value** pairs.
* **Keys are unique and immutable**.
* Values can be of any type and **can repeat**.
* Dictionaries are **mutable** and **ordered** (Python 3.7+).
* Created using `{}` or `dict()`.
* Dictionary comprehensions create key-value pairs.
* Access values using **keys**, not index numbers.
* Useful methods: `get()`, `pop()`, `update()`, `keys()`, `values()`, `items()`.

### Dictionaries in Functions

* `*args` → tuple (positional arguments).
* `**kwargs` → dictionary (keyword arguments).
* `**` can unpack a dictionary when calling a function.

### Choosing the Right Collection

* **List** → ordered, mutable, allows duplicates.
* **Tuple** → ordered, immutable, fixed data.
* **Set** → unordered, no duplicates, fast checking.
* **Dictionary** → key-value mapping, fast lookup.

### Key Points

* Sets remove duplicates and support set operations.
* Dictionaries map keys to values.
* Comprehensions can create sets and dictionaries.
* Choosing the right data type makes code better.

---


