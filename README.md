# Anonypy
A handy Python program to anonymize strings via hash functions (SHA-256) -- not meant for passwords!

## Usage
(Randomly) generate a pepper and store it in a new file called `pepper.txt` with one line only. Then simply run `anonypy.py`.

Do not share the pepper: it is meant to be private and generated only once. This is not suitable for storing passwords (use a salt instead), but it is useful in those cases in which two identical strings must have the same hash. 

## Dependencies
* [PyCryptodome](https://pypi.org/project/pycryptodome) is required. Run `pip install pycryptodomex`.

* Make sure [tkinter](https://docs.python.org/3/library/tkinter.html) is installed. Run ```python -m tkinter``` from the command line to show a demo of a Tk window and to check whether `tkinter` is properly installed.
