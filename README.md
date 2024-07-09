# blogprj_02
The purpose of creating this repository is to learn how to link the virtual environment of vs code with github. Method (1) is to first create a repository on Github and clone the repository "under the root folder" of the local computer.
Method (2) is to first create a repository on Github and clone the repository "in the virtual environment" under the root folder of the local computer.
The repository name of method (1) (same as the project name) is blogprj_01, and the repository name of method (2) (same as the project name) is named blogprj_02.

The process and results of method (2) are as follows.
1) Copy the address of the newly created repository to the local computer.
2) Create a virtual environment (env) and write the changed .gitignore file there.
3) Write a project and app under env.
4) In the env folder, execute the git add -A, git status, and git commit commands in order.
5) Execute the git push -u origin main command to reflect it to the remote repository.

Result: As a result of checking the repository on github, the entire virtual environment folder (including the changed contents) was uploaded.

** Differences from method (1):
The repository is copied the same, but in method (1), all git operations were performed in the root directory (the location of the .gitignore file). In method (2), all git operations were performed in the virtual environment directory (the location of the .gitignore file). As a result, the entire virtual environment folder was uploaded.
