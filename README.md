
# A Practical Workflow for Data Science Projects

This project is intended as a template structure for data science projects. Its main intended use is for teams within organizations but we see no reason why you would not benefit from it even if you are coding solo, participating in a data hackaton or are in a academic group, doing exploratory, statistical analysis or algorithm modelling.

# Principles

There are technical and management-oriented principles that orient this template:

1. **[Technical] Development environment should be reproducible.** Person A and Person B should be able to run code in their own independent computers and obtain the same output.
2. **[Technical] Exploratory code is different from maintained code.** Exploratory analysis are guided _mostly_ by one-shot notebooks, which often needs to be read, understood and replicated by others but the code itself will not necessarily have to be integrated into a pipeline nor deployed to a cloud server. We believe that exploratory code should be more about communicating its findings to others, the emphasis should be placed more on good markdown and results documentation rather than on code beauty. When this code "evolves" and one identifies the need for it to be extended, adapted to different users and/or integrated to other pieces of software, we need to pay a greater deal of attention on curating this code and making sure it is as efficient and well-documented as possible. This will happen, for example, when we need to serve the code as an API or to build it inside a software product or to deploy it to the cloud.

\# TODO: Write other guiding principles

# Setup

To guarantee that people will be able to replicate analysis and results even when they are using different base operating systems and IDE setups, we use **Docker containers**.
By containerizing our workflow, we won't have to pay _too much attention_ to errors that arise from having different environment setups, different library versions and the like.

The only software that needs to be installed in your machine is Docker and Docker-compose. All the rest (python, environment variables, pandas, numpy, etc.) will be installed automatically within the containers.

To reproduce the algorithm and run the notebooks with **exactly the same setup** we have used to develop, just follow the steps below. Docker will read the relevant configuration files (docker-compose.yml, notebooks/Dockerfile, notebooks/requirements) and install all python dependencies automatically.

1. [Clone the repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to a directory in your machine
2. Install [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/) on your machine
3. Open the terminal and build the project:
```{console}
cd data-science-workflow
docker-compose build
```
The first time you run this build, it will take several minutes to complete. Trust me, it is better to run build this and wait than to install each multiple python dependencies by hand and having to figure out why your colleague gets a weird and mysterious, previously unseen Exception when running the same code than you.

4. Still in the terminal, run Jupyter server with the command:
```{console}
docker-compose up
```
A URL will show up on your screen, either click on it or copy-paste to your browser and run the notebooks.
