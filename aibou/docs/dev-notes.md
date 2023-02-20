## Creating requirements.txt file

Use the instructions in the README on github to make a cloned repo. Don't use 
the same environment you work in to develope the game; this includes ipython for 
testing and a bunch of other unnecessary packages. After following the full 
instructions, try running the main file then start adding the missing packages to 
the local environment with `./aibou-test-env/bin/pip3 install PACKAGE`. You can also 
remove the local requirements.txt now. Once the new pacakages have been added, 
run `/aibou-test-env/bin/pip3 freeze --exclude-editable > requirements.txt` to 
create the new requirements.txt. Finally, copy or move it to your local dev repo 
and push the changes.
