# Quickstart (Linux)

This setup requires you have both 
[Conda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) 
and
[git](https://git-scm.com/download/linux) 
installed.

By default, this setup will install the game folder under the user's home 
directory (~).

Change to home directory

`$ cd ~`

Clone repo

`$ git clone https://github.com/jakekrol/aibou.git`

Change to game directory

`$ cd aibou`

Setup environment to install game dependencies

`$ conda create --prefix $PWD/aibou-env --file requirements.txt`

Run the game (sudo is required for keyboard module)

`$ sudo aibou-env/bin/python aibou/src/main.py`

## Optional

optional bash alias

`$ vim ~/.bash_aliases`

add this line to .bash_aliases file

`alias xaibou="cd ~/aibou && sudo aibou-env/bin/python aibou/src/main.py"`

source the alias file

`$ source ~/.bash_aliases`

Now, the game can be executed with `xaibou`. 

