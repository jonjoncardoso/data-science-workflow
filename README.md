
# A Practical Workflow for Data Science Projects

This project is intended as a template structure for data science projects. Its main intended use is for teams within organizations but we see no reason why you would not benefit from it even if you are coding solo, participating in a data hackaton or are in a academic group, doing exploratory, statistical analysis or algorithm modelling.

(WIP: This README page will be updated with more elements suited for data science projects)

# Set up (virtualenv)

Follow the instructions below to setup the development environment and all required packages used in this project

1. [Clone this repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to a directory in your machine
2. [Set up Python, Pip and Virtualenv](http://timsherratt.org/digital-heritage-handbook/docs/python-pip-virtualenv/)
3. Open the terminal and build the dependencies:
```{console}
cd <project_name>
python3 -m virtualenv venv
python3 -m pip install -r requirements.txt
```
The first time you run this build, it will take several minutes to complete. Trust me, it is better to run this and wait the building time than having to install each multiple python dependencies by hand and having to figure out why your colleague gets a weird and mysterious, previously unseen Exception when running the same code as you!

4. Still on the terminal, run Jupyter server with the command:
```{console}
source venv/bin/activate
jupyter lab
```

A URL will show up on your screen, either click on it or copy-paste to your browser and run the notebooks.
