#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

export GOPATH=$HOME/.go
alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
