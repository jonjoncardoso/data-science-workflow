
# A Practical Workflow for Data Science Projects

This project is intended as a template structure for data science projects. Its main intended use is for teams within organizations but we see no reason why you would not benefit from it even if you are coding solo, participating in a data hackathon or are in an academic group, doing exploratory, statistical analysis or algorithm modelling.

This is a standalone **template project** that can be used as a starting point for any data science project. It is not a framework, a library, or a package. It is a template that you can use to start your own project. It is not intended to be a one-size-fits-all solution, but rather a starting point for you to build your own project structure.

# 👥 **Team**

- [Jon](http://github.com/jonjoncardoso) as the core developer

**People who have contributed to this course in the past:**

- [Natalia Del Coco](https://github.com/NataliaDelCoco). _She is taking her van to the mountains for a while._
- [Sara Luxmoore](https://github.com/SaraLuxmoore). _She can be seen doing cool research-related stuff in Italy these days._

# Initial repository setup

Follow the instructions below to make use of this template.

1. Create a new repository on GitHub using this template. You can do this by clicking on the green "Use this template" button on the top right of this page. 

    ![Illustration of how to use this template](https://user-images.githubusercontent.com/896254/224554953-9819f73a-fdd1-4045-a183-dfa7d3601121.png)

2. Give your project a name and description. You can also choose to make the repository **private** if you wish. 
    - Leave "Include all branches" unchecked.

3. GitHub will copy the files from this repository into your new repository and it will trigger an **Actions** workflow. This workflow will customize labels (to include emojis!) as well as Issues and Pull Request templates for your project.
    - If you are not familiar with GitHub Actions, you can read more about it [here](https://docs.github.com/en/actions).

4. Clone your new repository to your computer and start working on it!

# First steps

Once you have cloned your new repository to your computer, you might want to do the following:

1. Update the `README.md` file to remove all things related to this template and add information about your project.

2. Update the `LICENSE` file to reflect the license you want to use for your project. You can find a list of open-source licenses [here](https://choosealicense.com/).

3. Modify the name of the `src/python/pkg_name` folder to reflect the name of your project. You can also remove the `pkg_name` folder if you are not planning on using custom Python packages.

# More information

Click on the links below to learn how to best use this template, and how to contribute to it.

<details><summary>✋ How to contribute</summary>

## ✋ How to contribute

If you want to propose changes to the template, follow the steps below:

1. Set up your environment by following the instructions in the [Dev Setup](#dev-setup) section.
2. Create a new branch from `develop` and give it a meaningful name. Best practices involve using the following format: `<your-username>/<issue-number>-<short-description>`. For example, if you are working on issue #3, you could name your branch `jonjoncardoso/3-update-github-action`. Remember the [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) workflow!
3. Make your changes and commit them to your branch. Remember to commit often and to write meaningful commit messages. If you are working on a specific issue, you can use the following format: `<gitmoji> #<issue-number> <commit-message>`. For example, if you are working on issue #3, you could write `📝 #3 Update GitHub Action`. 
    - To add emojis on Windows, just type `Win + .` and then select the emoji you want. On Mac, it's the world symbol `⌘ + Ctrl + Space`.
    - You can find a list of gitmojis [here](https://gitmoji.dev/). If you are not sure what to write, you can use `📝` for documentation, `🐛` for bug fixes, `🌟` for new features, and `♻️` for refactoring. You can also use `🔧` for general changes. If you are not sure, just ask! 
4. When you are done, push all your commits and then open a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) to merge your branch into `develop`. You can do this by clicking on the "Compare & pull request" button on GitHub. Make sure to add a meaningful title and description to your pull request. If you are working on a specific issue, you can use the following format: `#<issue-number> <pull-request-title>`. For example, if you are working on issue #3, you could write `#3 Update GitHub Action`. Mark @jonjoncardoso as a reviewer.

</details>

<details><summary>🧰 Dev Setup</summary>
## 🧰 Dev Setup

### 🐍 The Python setup

1. Install [Python 3.9](python.org) or higher on your computer.
2. Install [anaconda](https://www.anaconda.com/products/individual) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) on your computer.
3. Create a new conda environment:

    ```bash
    conda create -y -n=venv-ds-workflow python=3.10.8
    ```
4. Activate the environment and make sure you have `pip` installed inside that environment:

  ```console
  # the exact `activate` command will vary depending on your OS
  conda activate venv-ds-workflow 
  ```

💡 Remember to activate this particular `conda` environment whenever you reopen VSCode/the terminal.

10. Install required libraries

  ```console
  pip install -r requirements.txt
  ```

Now, whenever you open a Jupyter Notebook, you should see the `venv-ds-workflow` kernel available. You can also run `jupyter kernelspec list` to see all the kernels available on your computer.


### 📊 The R setup

1. Clone this repository to your computer.
2. Open a terminal and navigate to the root of this repository.
3. Ensure you have **R version 4.2.2** or higher
4. Open the R console in this same directory and install `renv` package:
```r
install.packages("renv")
```
5. Run `renv::restore()` to install all the packages needed for this project

### The Quarto setup

If using quarto is not your thing, you can just ignore this section. If you want to use quarto, follow the steps below:

1. Install [Quarto](https://quarto.org/docs/getting-started/installation.html) on your computer.
2. Run the following command to start the website locally:
    ```bash
    quarto preview . --render all --no-browser
    ```
    This will read the instructions from `_quarto.yml` and render the website locally.
5. Open your browser and navigate to `http://localhost:<port>/`. That's it!

</details>

<details> <summary>⚒️ (Advanced) Jon's full setup</summary>

## ⚒️ (Advanced) Jon's full setup

I, [@jonjoncardoso](github.com/jonjoncardoso), like to use R on VSCode (WSL Ubuntu) instead of RStudio. It is a weird setup if you come from R, but it's a good setup for when you need to switch between R and Python all the time. Feel free to just ignore this stuff but if you want to replicate my setup, just follow the steps below:

1. Install [VSCode](https://code.visualstudio.com/Download)
2. Install [WSL on Windows](https://learn.microsoft.com/en-us/windows/wsl/install)
3. Install [WSL extension on VSCode](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
4. Open VSCode and open a new WSL window (Type `Ctrl+Shift+P` and type `WSL: New Window`)
6. Open the Ubuntu terminal on VSCode and install [R](https://cloud.r-project.org/)
**When doing R**
7. Install the [R extension on VSCode](https://marketplace.visualstudio.com/items?itemName=Ikuyadeu.r)
8. Install [Quarto](https://quarto.org/docs/getting-started/installation.html)
9. Install the [Quarto extension on VSCode](https://marketplace.visualstudio.com/items?itemName=quarto-dev.quarto-vscode)
10. When running R notebooks (either `.Rmd` or `.qmd`) manually, you will see that some plots do not render with adequate size. To fix this, follow [these instructions](https://stackoverflow.com/a/70817205/843365).
**When doing Python**
11. Install the [Python extension on VSCode](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
12. Install the [Jupyter extension on VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

I also use the following VSCode Extensions:

- [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
- [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Grammarly](https://marketplace.visualstudio.com/items?itemName=znck.grammarly)

</details>

