[![Build Status](https://travis-ci.org/TRIQS/tests_for_triqs.svg?branch=unstable)](https://travis-ci.org/TRIQS/tests_for_triqs)

# tests_for_triqs - A skeleton for a TRIQS application

Initial Setup
-------------

To adapt this skeleton for a new TRIQS application, the following steps are necessary:

* Create a repository, e.g. https://github.com/username/appname

* Run the following commands in order after replacing **appname** accordingly

```bash
git clone https://github.com/triqs/tests_for_triqs --branch unstable appname
cd appname
./share/squash_history.sh
./share/replace_and_rename.py appname
git add -A && git commit -m "Adjust tests_for_triqs skeleton for appname"
```

You can now add your github repository and push to it

```bash
git remote add origin https://github.com/username/appname
git remote update
git push origin unstable
```

If you prefer to use the [SSH interface](https://help.github.com/en/articles/connecting-to-github-with-ssh)
to the remote repository, replace the http link with e.g. `git@github.com:username/appname`.

### Merging tests_for_triqs skeleton updates ###

You can merge future changes to the tests_for_triqs skeleton into your project with the following commands

```bash
git remote update
git merge tests_for_triqs_remote/unstable -m "Merge latest tests_for_triqs skeleton changes"
```

If you should encounter any conflicts resolve them and `git commit`.
Finally we repeat the replace and rename command from the initial setup.

```bash
./share/replace_and_rename.py appname
git commit --amend
```

Getting Started
---------------

After setting up your application as described above you should customize the following files and directories
according to your needs (replace tests_for_triqs in the following by the name of your application)

* Adjust or remove the `README.md` and `doc/ChangeLog.md` file
* In the `c++/tests_for_triqs` subdirectory adjust the example files `tests_for_triqs.hpp` and `tests_for_triqs.cpp` or add your own source files.
* In the `test/c++` subdirectory adjust the example test `basic.cpp` or add your own tests.
* In the `python/tests_for_triqs` subdirectory add your Python source files.
  Be sure to remove the `tests_for_triqs_module_desc.py` file unless you want to generate a Python module from your C++ source code.
* In the `test/python` subdirectory adjust the example test `Basic.py` or add your own tests.
* Adjust any documentation examples given as `*.rst` files in the doc directory.
* Adjust the sphinx configuration in `doc/conf.py.in` as necessary.
* The build and install process is identical to the one outline [here](https://triqs.github.io/tests_for_triqs/unstable/install.html).

### Optional ###
----------------

* If you want to wrap C++ classes and/or functions provided in the `c++/tests_for_triqs/tests_for_triqs.hpp` rerun the `c++2py` tool with
```bash
c++2py -r tests_for_triqs_module_desc.py
```
* Add your email address to the bottom section of `Jenkinsfile` for Jenkins CI notification emails
```
End of build log:
\${BUILD_LOG,maxLines=60}
    """,
    to: 'user@domain.org',
```
