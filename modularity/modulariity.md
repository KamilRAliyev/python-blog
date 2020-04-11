# Modularity
###### date: 4/8/2020, 9:45:00 PM
---

!!! note ```__name__```
Specially named var allowing us to detect whether a module is run as script or imported to another module.
!!!

Our Python file:
- if running as a script the ```__name__``` will be equal to ```"__main__"```.
- if it is running in REPL the ```__name__``` will be equal to package name (e.g. words)

To see how:
```python 
if __name__ == "__main__":
    fetch_words()
```
---
 
 !!! note When the module imports or exucetes, all the top level statements will run
 !!!
 
 Python script --- Convenient execution from CMD
 Python module --- Convenient import with API
 Python program --- Perhaps composed of many modules
 
 Ps. Any .py file constitutes a Python module
 