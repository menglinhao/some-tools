import os
import re
import subprocess

install_tool = 'yum'
sys_info = subprocess.run('cat /etc/os-release', shell=True, capture_output=True).stdout.decode()
if 'Ubuntu' in sys_info:
    install_tool = 'apt'

# https://blog.csdn.net/MrKorbin/article/details/124777136?spm=1001.2014.3001.5506
os.system(f'{install_tool} -y install vim')
os.system(f'{install_tool} -y install gcc')
if not os.path.exists('~/.oh-my-zsh'):
    os.system(f'{install_tool} -y install zsh')
    os.system('git clone https://gitee.com/Hey_friends/ohmyzsh.git ~/.oh-my-zsh')
    os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc')
    # plugins
    os.system(
        'git clone https://gitee.com/Hey_friends/zsh-autosuggestions.git ~/.oh-my-zsh//plugins/zsh-autosuggestions')
    os.system(
        'git clone https://gitee.com/Hey_friends/zsh-syntax-highlighting.git ~/.oh-my-zsh//plugins/zsh-syntax-highlighting')
    os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc')

plugins_pattern = r"plugins=\(git\)"
plugins_str = "plugins=(git zsh-autosuggestions zsh-syntax-highlighting)"
theme_pattern = r'ZSH_THEME=(.*)?\n'
theme_str = 'ZSH_THEME="dst"'
auto_update_pattern = r"# zstyle ':omz:update' mode auto"
auto_update = r"zstyle ':omz:update' mode auto"

# amuse 也不错 需要安装
# dnf install powerline-fonts
# new_theme = 'ZSH_THEME="bureau"'

zsh_path = '/root/.zshrc'
if os.path.exists(zsh_path):
    with open(zsh_path, mode='r+') as f:
        content = f.read()
        new_content = re.sub(plugins_pattern, plugins_str, content)
        new_content = re.sub(theme_pattern, theme_str, new_content)
        new_content = re.sub(auto_update_pattern, auto_update, new_content)
        new_content += '\nDISABLE_UPDATE_PROMPT=true'  # 将环境变量DISABLE_UPDATE_PROMPT=true设置为始终答复是并自动升级。
        f.write(new_content)

print("""终端输入 `zsh` 启用. 
chsh -s $(which zsh)  # 设置 zsh 默认shell
""")

