# Shebang
###### date 4/10/2020, 7:11:43 AM
---
it is common on UNIX like systems that have special type comment on the first line.
```python
#!/usr/bin/env python3  
```

- #! ---shhbang
- python --- allows the program loader to identify the interpreter should be used to run the program
- env --- the UNIX program to locate Python3 on path env var. #is compatible with python virtual envs

!!! note Mac or Linux
we must make script executable:
```bash
$ chmod +x words.py
$ ./words.py http://sixty-north.com/c/t.txt
```
!!!

!!! note Pylauncher for Windows
PEP 397 read it!
!!!
