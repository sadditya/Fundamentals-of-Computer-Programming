

---

## I/O and File Handling – Simple Summary

### Input and Output (I/O)

* Every program works as **input → process → output**.
* Basic I/O uses `input()` and `print()`.
* Real programs also use **files, networks, and GUIs**.

---

## Formatting Output

### F-Strings (Best & Modern)

* Easy and readable.
* Use **`f" "`** and `{}` for variables.
* Supports formatting like decimal places and alignment.
* Example:
  `f"{price:.2f}"` → 2 decimal places.

### `str.format()`

* Older but still used.
* Uses `{}` placeholders.
* More complex than f-strings.

### Manual Formatting

* Uses methods like `ljust()`, `rjust()`, `center()`, `zfill()`.
* Less flexible than f-strings.

### `%` Formatting (Old Style)

* Based on C language.
* Works but **not recommended** now.

---

## File Handling

### Files

* Files store data as **text or binary**.
* Python can **read and write** both types.

### Opening Files

* Use `open()` to open a file.
* Common modes:

  * `r` → read
  * `w` → write
  * `a` → append
  * `r+` → read & write
  * `b` → binary mode
* Always **close files** after use.

### Reading Files

* `read()` → read all content.
* `readline()` → read one line.
* `readlines()` → read all lines as a list.
* Files can be read using a **for loop**.

### Writing Files

* Use `write()` to write text.
* Convert non-strings using `str()` before writing.

### File Position

* `tell()` → current position in file.
* `seek()` → move position in file.

---

## Safe File Handling

* Use **`with open()`** to handle files safely.
* File closes automatically, even if errors occur.

---

## Key Points

* I/O is essential in all programs.
* F-strings are the best way to format output.
* Files must be opened before reading or writing.
* Use `with` statement for safe file handling.

---

