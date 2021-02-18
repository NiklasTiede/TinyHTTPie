# This installation script moves the files into a MyScripts folder into your home dir
# Python version checked, pipenv installed if not existent
# pipenv venv created, shebang line added, giving permissions
# create permanent alias 


if [[ ! -d ~/MyScripts ]]; then
    mkdir ~/MyScripts
    folder1=~/MyScripts
    echo "${folder1} was generated."
fi
if [[ ! -d ~/MyScripts/tinyhttp ]]; then
    mkdir ~/MyScripts/tinyhttp
    folder2=~/MyScripts/tinyhttp
    echo "${folder2} was generated."
fi

# copy files into ~/MyScripts/tihttp
PWD=$(pwd)
REQUIREMENTS="$PWD/requirements.txt"
SCRIPT="$PWD/tinyhttp.py"
TARGET=~/MyScripts/tinyhttp

cp "$REQUIREMENTS" "$TARGET"
cp "$SCRIPT" "$TARGET"
cd ~/MyScripts/tinyhttp

# check python version
PYVER=$(python --version)
CURRENT_PY_VERSION=${PYVER:7:11}
testvercomp ${CURRENT_PY_VERSION} 3.0.0 '>'
if [[ $(echo $CURRENT_PY_VERSION | grep '2.'*) ]]; then
    echo "first digit is 2, you're python version is too low"
elif [[ $(echo $CURRENT_PY_VERSION | grep '3.'*) ]]; then
    echo "first digit is 3, you're python versions fulfills the requirements!"
fi

# check pipenv
if [[ ! $(pipenv) ]]; then
    echo "pipenv not existent, so installing via pip..."
    pip install pipenv
    echo "...pipenv was installed?"
fi

# rebuild virtual env from requirements-file
pipenv install -r requirements.txt

# adding shebang line to top of script:
pybin=$(pipenv --py)
echo -e "#\!${pybin}\n\n$(cat tinyhttp.py.py)" > tinyhttp.py

# check if shebang line represents the pipenv environemtn:
EXIS_HEADLINE=$(head -n 1 tinyhttp.py)
EXP_HEADLINE="#!${pybin}"
if [[ $EXIS_HEADLINE == $EXP_HEADLINE && ${#EXIS_HEADLINE} == ${#EXP_HEADLINE} ]]; then
    echo "shebang line was added correctly!"
elif [[ $EXIS_HEADLINE != $EXP_HEADLINE || ${#EXIS_HEADLINE} != ${#EXP_HEADLINE} ]]; then
    echo "shebang was NOT added correctly!"
fi

# change file permissions
chmod +x ~/MyScripts/tiniHTTP/tiny_HTTPie_clone.py

# add alias to file containing the aliases 
SHELL=$(printenv SHELL)
MYSHELL=${SHELL:5:10}
ALIASFILE=~/.bashrc

if [[ $MYSHELL  == "zsh" ]]; then
    echo "You're default shell is ZSH."
    if [[ -e ~/.aliases ]]; then
        ALIASFILE=~/.aliases
        echo "You're storing your files within the .aliases file."
    elif [[ -e ~/.zshrc ]]; then
        ALIASFILE=~/.zshrc
        echo "You're storing your files within the .zshrc file."
    fi
elif [[ $MYSHELL  == "bash" ]]; then
    echo "You're default shell is BASH."
    if [[ -e ~/.aliases ]]; then
        ALIASFILE=~/.aliases
        echo "You're storing your files within the .aliases file."
    elif [[ -e ~/.bashrc ]]; then
        ALIASFILE=~/.bashrc
        echo "You're storing your files within the .bashrc file."
    fi
fi

echo "$ALIASFILE is where we placed the alias."

# change permissions
SCRIPTPATH=~/MyScripts/tinyhttp/tinyhttp.py
chmod +x $SCRIPTPATH

# adding alias (I prefer using an alias, instead of polluting my PATH)
echo $SCRIPTPATH
echo "\n# alias for the tinyHTTP script (stored within ~/MyScripts/tinyhttp)\nalias tihttp='$SCRIPTPATH'" >> $ALIASFILE
source $ALIASFILE

# test
if [[ ! $(tihttp) ]]; then
    echo "tihttp alias is not working"
    echo "Instead this scripts tries to add tihttp to your PATH"
fi

# I prefer using an alias, instead of adding it to the PATH!
# export PATH="$HOME/MyScripts/tinyhttp:$PATH"

# test (tihttp --version)
EXIS_TEST=$(tihttp --version)
EXP_TEST
if [[ $EXIS_TEST != $EXP_TEST ]]; then
    echo "Not properly installed"
elif [[ $EXIS_TEST != $EXP_TEST ]]; then
    echo "tihttp was installed successfully!"
