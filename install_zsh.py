import os
import re
# https://blog.csdn.net/MrKorbin/article/details/124777136?spm=1001.2014.3001.5506


os.system('yum -y install vim')
os.system('yum -y install gcc')
if not os.path.exists('~/.oh-my-zsh'):
    os.system('yum -y install zsh')
    os.system('git clone https://gitee.com/whereabouts-fork/ohmyzsh.git ~/.oh-my-zsh')
    # plugins
    os.system('git clone https://gitee.com/whereabouts-fork/zsh-autosuggestions.git ~/.oh-my-zsh//plugins/zsh-autosuggestions')
    os.system('git clone https://gitee.com/whereabouts-fork/zsh-syntax-highlighting.git ~/.oh-my-zsh//plugins/zsh-syntax-highlighting')
    os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc')

re_pattren = r"plugins=\(git\)"
subst = "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)"
zsh_path = '/root/.zshrc'
if os.path.exists(zsh_path):
    with open(zsh_path, mode='r+') as f:
        content =  f.read()
        new_content = re.sub(re_pattren, subst, content)
        f.write(new_content)

os.system(f'source {zsh_path}')
print("git ok")

"""
# vim ~/.zshrc
# plugins=(git zsh-autosuggestions zsh-syntax-highlighting)
# source ~/.zshrc
with open ('~/.zshrc', mode='w') as f:
    res = f.read()
    ..
"""