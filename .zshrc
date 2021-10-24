# Path to your oh-my-zsh installation.
export ZSH="/Users/elizabethwise/.oh-my-zsh"

# Plugins
plugins=(git zsh-autosuggestions git-open zsh-syntax-highlighting)

# Set name of the theme to load, see https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"

# Uncomment the following line to use case-sensitive completion.
CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion: _ and - will be interchangeable.
HYPHEN_INSENSITIVE="true"

# Aliases
alias zshrc="code ~/.zshrc"
alias dcd='docker-compose down --remove-orphans'
alias dclean='docker stop $(docker ps -a -q);docker rm -v $(docker ps -a -q); docker rmi -f $(docker images -q)'
alias dcu='docker-compose down; docker-compose up'
alias dcub='docker-compose down; docker-compose up --build'
alias reload="exec $SHELL -l"
alias dc="docker-compose -f compose/docker-notebook-mac.yml run id_update python master.py"
alias aws_auth='aws-google-auth -p $aws_profile -d 3600 -u $email -I $google_idp_id -S $google_sp_id --no-cache -a --resolve-aliases'

#Functions
dex(){
  docker exec -ti "$1" bash
}
dbash() {
  docker exec -ti $(docker ps -qf "name=$1") bash;
}


# UNIX commands
mkdir *name* # make new directory
cd *name* # change directory
pwd # list current directory
ls # list files in directory
mv *name* # move file
cv *name* # copy file
chmod *name* # lets you change read, write and execute permissions of file
gzip *name* # compresses file
gunzip *name* # uncompress files

# github
git init
git pull
git checkout -b ramseywise/add_series_to_542
git status
git add items/item542.json
git commit -m 'message'
git push --set-upstream origin #set repo local location
git rebase origin/master
# to recover deleted branch
git reflog
git branch DSCIENCE-564 9a68576