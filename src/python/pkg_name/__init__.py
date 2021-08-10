# This is where your reusable code will live.
#
# TODO: Add a script to the root directory so that it renames this directory to a package name chosen by the user of this template

def example_package_function():
    """
    An example of package function.
    """
    msg = ("This is just an example of a package function.\n"
           "To import this package and run this function in a notebook, "
           "go to the root directory and start the Docker container which contains the Jupyter server:"
           "`docker-compose up`.\n"
           "Then, open a notebook and import `from pkg_name import example_package_function` "
           "so you can run `example_package_function()`.")
    print(msg)
