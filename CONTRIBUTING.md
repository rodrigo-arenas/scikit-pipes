# Contributing

Scikit-pipes is an open-source project and contributions of all kinds
are welcome.

You can contribute with documentation, examples/tutorials, reviewing pull requests, code,
helping answer questions in issues, creating visualizations, maintaining project
infrastructure, and creating new tests. 

Code contributions are always welcome, from simple bug fixes to new features.
Also, consider contributing to the documentation, 
and reviewing open issues, it is the easiest way to get started.

When working on your local computer, make sure to install the development dependencies with:
```bash
pip install -r dev-requirements.txt
```

If you have questions, you can open an issue (tag it as a question).

We encourage you to follow these guidelines:

* Fork this project, make the changes you expect to merge and make a pull request 
* If the work you are making is related to some issue, please mention in the comments 
  that you are working on it, so other people know and no duplicate your work.
* If you are working on a new feature, or have an idea, consider first opening an issue
  so people know what you are working on and possibly give some guidelines
* Commit all changes by pull request (PR)
* A PR solves one problem (do not mix problems in one PR) with the
  minimal set of changes
* The changes should come with their respective tests and documentation
* Describe why you are proposing those changes 
* Please run black on top of the package to keep the formatting style
    ```bash
    black .
    ```
* Make sure all the tests are passing, by running in the root of the project
    ```bash
    pytest skpipes
    ```
* We can not merge if the tests fail.

## Thank you for being part of this project!