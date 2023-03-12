# This is where your reusable code will live.
# If you have code that is used in multiple notebooks, you can put it here.

def example_package_function():
    """
    An example of package function.
    """
    msg = ("This is just an example of a package function.\n"
           "To import this package and run this function in a notebook, "
           "go to the root directory and run `pip install ./src/python`\n"
           "Then, open a notebook and import `from pkg_name import example_package_function` "
           "so you can run `example_package_function()`.")
    print(msg)
