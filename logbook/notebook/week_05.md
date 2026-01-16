
---

## Scripts and Modules – Simple Summary

* Small programs can be written in **interactive mode**, but larger programs are saved as **Python files (.py)** called **scripts**.
* Scripts are executed using the Python interpreter, for example:
  `python program.py`
* Unlike interactive mode, scripts must use `print()` to show output.

### Command Line Arguments

* Extra values can be passed to a script when it runs.
* These values are accessed using `sys.argv`.
* `sys.argv[0]` is the program name; the rest are user inputs.

### Modules

* Any `.py` file can also be used as a **module**.
* Modules allow code (functions, variables) to be **reused** in other programs.
* Modules are imported using the `import` statement.

### Importing Modules

* Import a full module: `import math`
* Use an alias: `import math as m`
* Import specific items: `from math import sqrt`
* Importing everything (`*`) is not recommended.

### Module Search Path

* Python searches for modules using a list of directories called `sys.path`.
* This includes the current folder, built-in modules, and system paths.

### Useful Tools

* The `dir()` function lists all names in a module (mainly used in interactive mode).

### The `__name__` Variable

* `__name__` tells whether a file is run as a **script** or imported as a **module**.
* If `__name__ == "__main__"`, the file is running as a script.
* This allows one file to work as both a script and a module.

### Key Points

* Python files can act as scripts, modules, or both.
* Command-line arguments make programs flexible.
* Importing controls how module names are used.
* `__name__` helps write reusable programs.

---

