import os
import re
# https://blog.csdn.net/MrKorbin/article/details/124777136?spm=1001.2014.3001.5506
os.system('yum -y install zsh')
os.system('git clone https://gitee.com/whereabouts-fork/ohmyzsh.git ~/.oh-my-zsh')
# plugins
os.system('git clone https://gitee.com/whereabouts-fork/zsh-autosuggestions.git ~/.oh-my-zsh//plugins/zsh-autosuggestions')
os.system('git clone https://gitee.com/whereabouts-fork/zsh-syntax-highlighting.git ~/.oh-my-zsh//plugins/zsh-syntax-highlighting')
"""
# vim ~/.zshrc
# plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
# source ~/.zshrc
with open ('~/.zshrc', mode='w') as f:
    res = f.read()
    ..
"""