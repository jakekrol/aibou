# Quickstart (Linux)

This setup requires you have both 
[Conda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) 
and
[git](https://git-scm.com/download/linux) 
installed.

By default, this setup will install the game folder under the user's home 
directory (~).

Change to home directory

`cd ~`

Clone repo

`git clone https://github.com/jakekrol/aibou.git`

Change to game directory

`cd aibou`

Create and activate virtual environment

`conda create --prefix $PWD/aibou-env && conda activate ./aibou-env/`

Install the aibou package to the virtual environment.

`./aibou-test-env/bin/python -m pip install -e .`

Install external dependencies, too

`./aibou-env/bin/pip3 install -r requirements.txt`

Run the game (sudo is required for keyboard module)

`sudo aibou-env/bin/python aibou/src/main.py`

## Optional

optional bash alias

`vi ~/.bash_aliases`

add this line to .bash_aliases file

`alias xaibou="cd ~/aibou && sudo aibou-env/bin/python aibou/src/main.py"`

source the alias file

`source ~/.bash_aliases`

Now, the game can be executed with `xaibou`. 

