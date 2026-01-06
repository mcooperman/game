# shellcheck shell=bash
## !/bin/bash

# Customize this file for a specific project/repo

# DEFENSIVE (bash) SCRIPTING SETTINGS
# set -u  # no unset variable use
# set -o pipefail  # not available in standard sh
# set -e  # automatic exit on error

# CUSTOMIZE PER-PROJECT
#  - py_venv_name
#  - git_user_name
#  - git_user_email
#  - git_signingkey
#  - git_remote_origin_url

platform=UNKNOWN

# $OSTYPE may also provide platform info
# docker ubuntu image = linux-gnu
# mac os = darwin18/19
# amazon linux = linux-gnu

platform=${OSTYPE:UNKNOWN}

if [[ "$OSTYPE" == "linux-gnu" ]]; then
  echo "OSTYPE: gnu linux"
elif [[ "$OSTYPE" == "linux" ]]; then
    echo "OSTYPE: linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "OSTYPE: Mac OS X"
elif [[ "$OSTYPE" == "cygwin" ]]; then
  echo "OSTYPE: cygwin - POSIX compatibility layer and Linux environment emulation for Windows"
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "OSTYPE: Lightweight shell and GNU utilities compiled for Windows (part of MinGW)"
elif [[ "$OSTYPE" == "win32" ]]; then
  echo "OSTYPE: win32"
elif [[ "$OSTYPE" == "freebsd"* ]]; then
  echo "OSTYPE: freebsd"
else
  echo "OSTYPE: UNKNOWN"
  # exit from sourced shell script without exiting caller?
fi

# uname
# docker ubuntu image = Linux
# mac os = Darwin
# amazon linux = Linux

unamestr=$(uname -ap)
echo "OS info: ${unamestr}"
if [[ $platform == 'linux' ]]; then
  alias ls='ls --color=auto'
elif [[ $platform == 'freebsd' ]]; then
  alias ls='ls -G'
fi

# SSH Agent
# make sure it's running
eval "$(ssh-agent -s)"
ssh-add  # adds all default keys in ~/.ssh
ssh-add -A

# git - *** MODIFY AS PER DEVELOPER ***
git_commit_gpgsign=true # true if you want to sign commits, requires a pub/priv keypair
git_user_name="mcooperman" # github user id
git_user_email="4791030+mcooperman@users.noreply.github.com"
git_signingkey="C15660CCC3FFAA034515169591830149EF94E22D" # gpg signing key ID
git_remote_origin_url="git@github.com:mcooperman/game.git"
# upstream?

# Push new repo
# echo "# game" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:mcooperman/game.git
# git push -u origin main

# Push existing repo
# git remote add origin git@github.com:mcooperman/game.git
# git branch -M main
# git push -u origin main

git config --local commit.gpgsign "${git_commit_gpgsign}"
git config --local user.name "${git_user_name}"
git config --local user.email "${git_user_email}"
git config --local user.signingkey "${git_signingkey}"
git remote add origin "${git_remote_origin_url}"
git remote set-url origin "${git_remote_origin_url}"
# git remote set-url origin "${git_remote_origin_url}"
# upstream?

# Python - virtual env
# name of the project/repo
py_venv_name=game
export PATH=/opt/anaconda3/envs/${py_venv_name}/bin:${PATH}
GITROOT=$(git rev-parse --show-toplevel)
export GITROOT
# setup PYTHONPATH to support Flask finding application packages
# this can be modified per Application, if more than 1
# but a 'default' is set here
PYTHONPATH=$(pwd)
export PYTHONPATH

# Julia
export PATH="$PATH:/Applications/Julia-1.6.app/Contents/Resources/julia/bin"

# Flask
echo Flask app package search path: PYTHONPATH="${PYTHONPATH}"
export FLASK_APP=wsgi.py:create_app
echo FLASK_APP=[${FLASK_APP}]
export FLASK_ENV=development
echo FLASK_ENV=[${FLASK_ENV}]

export PS1="[\u@\h:\w \s]\$ "
conda_init_shell=$(basename "${SHELL}")
conda_shell_path=/opt/anaconda3/etc/${py_venv_name}.d/
conda_shell=conda.sh
echo "which conda: $(command -v conda)"
echo "conda init shell: ${conda_init_shell}"
echo "initializing conda for use in shell"

if . ${conda_shell_path}/${conda_shell}; then
  echo "initialized conda for use in shell"
else
  echo -e "\x1B[1;31mconda shell initialization failed\x1B[0m"
fi
test "$(command -v conda)" && conda deactivate || echo -e "\x1B[1;31conda deactivate: conda not present\x1B[0m"
test "$(command -v conda)" && conda activate "${py_venv_name}" || echo -e "\x1B[1;31conda activate ${py_venv_name}: conda not present\x1B[0m"


# mac specific
# scutil --dns | awk -f dns-config.awk | grep -E "search domain" | grep -E "adp.com" 2> /dev/null

# Firefox path - specific to this project
export PATH=/Applications/Firefox.app/Contents/MacOS:${PATH}

# Proxy config
# technically, proxy can vary dynamically per url
# but we are going to simplify and force to US proxy
# barring a dynamic lookup if we determine we are on ADP Intranet
#if [ $? -eq 0 ];
if scutil --dns | awk -f dns-config.awk | grep -E "search domain" | grep -E "adp.com" 2> /dev/null;
then
  # detected a resolver with search domain containing adp.com
  # this signals we are on ADP Intranet
  # setup proxy
  echo "ON ADP NETWORK, USE PROXY"

  export no_proxy="127.0.0.1,localhost,*.local,169.254/16, *.adp.com, *.adpcorp.com, *.pi-adp.com, *.oneadp.com, *.whc"

  _user="$(id -u -n)"

  _default_proxy_host="usproxy.es.oneadp.com"
  _default_proxy_port="8080"
  read -r -p "proxy host [${_default_proxy_host}]: " _proxy_host
  [ -z "${_proxy_host}" ] && _proxy_host=$_default_proxy_host

  read -r -p "proxy port [${_default_proxy_port}]: " _proxy_port
  [ -z "${_proxy_port}" ] && _proxy_port=$_default_proxy_port

  read -r -p "use proxy basic auth (y/n) [n]: " _basic_auth

  if [ "${_basic_auth}" = "y" ];
  then

    read -r -p "proxy username [$_user]: " _proxy_user
    [ -z "${_proxy_user}" ] && _proxy_user=$_user

    echo -n "proxy password: "; stty -echo; read -r _proxy_passwd; stty echo; echo
    #echo $_proxy_user $_proxy_passwd

    export https_proxy=http://"${_proxy_user}:${_proxy_passwd}"@${_proxy_host}:${_proxy_port}
    export http_proxy=http://"${_proxy_user}:${_proxy_passwd}"@${_proxy_host}:${_proxy_port}
    _proxy_passwd= # get rid of passwd

  else
    export https_proxy=http://${_proxy_host}:${_proxy_port}
    export http_proxy=http://${_proxy_host}:${_proxy_port}
    # export ftp_proxy=
    if [ -f screenshot/eb-local-proxy-onnet.sh ]; then
      cp screenshot/eb-local-proxy-onnet.sh screenshot/eb-local-proxy.sh
    fi
  fi

  echo "check https_proxy environment variable to confirm"
  echo "proxy environment variables may contain sensitive information (credentials)"

else
  echo "NOT ON ADP NETWORK, NO PROXY"
  unset https_proxy
  unset http_proxy
  unset ftp_proxy
  export no_proxy="127.0.0.1,localhost,*.local,169.254/16, *.adp.com, *.adpcorp.com, *.pi-adp.com, *.oneadp.com, *.whc"
  if [ -f screenshot/eb-local-proxy-offnet.sh ]; then
    cp screenshot/eb-local-proxy-offnet.sh screenshot/eb-local-proxy.sh
  fi
fi

echo SHELL="${SHELL}"
# export DOCKER_BUILDKIT=1
# git_path=$(command -v git)
if command -v git; then
  echo "git path: $(command -v git)"
  echo "git version: $(git --version)"
  echo git config: commit.gpgsign="$(git config commit.gpgsign)"
  echo git config: commit.gpgsign="$(git config user.name)"
  echo git config: commit.gpgsign="$(git config user.email)"
  echo git config: commit.gpgsign="$(git config user.signingkey)"
  git remote -v
else
  echo "git not found on path"
fi
# ssl_path=$(command -v openssl)
if command -v openssl; then
  echo "OpenSSL path: $(command -v openssl)"
  echo "OpenSSL version: $(openssl version)"
  echo "SSH Keys"
  ssh-add -l
else
  echo "openssl not found on path"
fi
# python3_path=$(command -v python3)
if command -v python3; then
  echo "Python interpreter path: $(command -v python3)"
  echo "Python version: $(python3 --version)"
  echo "Python CA certificates: $(python3 -m certifi)"
else
  echo "python3 not found on path"
fi
# aws_path=$(command -v aws)
if command -v aws; then
  echo "aws path: $(command -v aws)"
  echo "aws version: $(aws --version)"
  # eb_path=$(command -v eb)
  if command -v eb; then
    echo "aws eb path: $(command -v eb)"
    echo "aws eb version: $(eb --version)"
  else
    echo "AWS Elastic Beanstalk CLI (eb) not on path"
  fi
else
  echo "AWS CLI (aws) not on path"
fi
if command -v julia; then
  echo "julia path: $(command -v julia)"
  echo "julia version: $(julia --version)"
fi

# set +e  # turn off automatic exit on error
