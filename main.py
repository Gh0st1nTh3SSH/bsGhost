import os, time
from getpass import getpass
from sys import stdout

#################################
#           COLORS              #
#################################

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)

def yellow():
    YELLOW = "\033[1;33m"
    stdout.write(YELLOW)

def purple():
    PURPLE = "\033[38;5;135m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

def error():
    white()
    print("[", end = "")
    red()
    print("!", end = "")
    white()
    print("]", end = " ")

def step():
    white()
    print("[", end = "")
    yellow()
    print("+", end = "")
    white()
    print("]", end = " ")

def install():
    white()
    print("[", end = "")
    purple()
    print("*", end = "")
    white()
    print("]", end = " ")

def success():
    white()
    print("[", end = "")
    green()
    print("✔", end = "")
    white()
    print("]", end = " ")

#################################
#           FUNCTIONS           #
#################################
def header():
    os.system("clear")
    purple()
    banner = """
 ▄▀▀▀▀▄   ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄      ▄▀▀▀▀▄   ▄▀▀▀▀▄ 
█        █  █   ▄▀ █      █ █ █   ▐ █    █  ▐     █      █ █ █   ▐ 
█    ▀▄▄ ▐  █▄▄▄█  █      █    ▀▄   ▐   █         █      █    ▀▄        by Gh0st1nTh3SSH
█     █ █   █   █  ▀▄    ▄▀ ▀▄   █     █          ▀▄    ▄▀ ▀▄   █  
▐▀▄▄▄▄▀ ▐  ▄▀  ▄▀    ▀▀▀▀    █▀▀▀    ▄▀             ▀▀▀▀    █▀▀▀   
▐         █   █              ▐      █                       ▐      
          ▐   ▐                     ▐                                                                                
    """
    print(banner)
    white()
    print()    
        
def requeriments():
    step()
    print("Installing requirements...", end = " ")
    try:
        # Update & Upgrade system
        os.system("sudo apt update -y > /dev/null 2>&1 && sudo apt upgrade -y > /dev/null 2>&1")
        # Install packages and dependencies
        os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y > /dev/null 2>&1")
        os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y > /dev/null 2>&1")
        os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y > /dev/null 2>&1")
        os.system("sudo apt install bspwm polybar fzf neovim rofi sxhkd kitty caja feh scrot neovim xclip scrub bat wmname rxvt-unicode zsh-autosuggestions zsh-autocomplete zsh-syntax-highlighting -y > /dev/null 2>&1")
        # Install LSD
        os.system("wget -q https://github.com/Peltoche/lsd/releases/download/0.21.0/lsd_0.21.0_amd64.deb")
        os.system("sudo apt install lsd_0.21.0_amd64.deb -y > /dev/null/ 2>&1")
        os.system("rm lsd_0.21.0_amd64.deb")
        # Install Hack Nerd Fonts
        os.system("sudo wget -q https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip /usr/share/fonts/")
        os.system("sudo mkdir /usr/share/fonts/Hack/ && sudo unzip /usr/share/fonts/Hack.zip")
        os.system("sudo rm /usr/share/fonts/Hack.zip") 
        success()
    except Exception as debug:
        error()
        print("There was an error installing requirements:")
        print(debug)
    print()
    
def bspwm():
    step()
    print("Configuring BSPWM...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/bspwm/")
        os.system("cp -R Dotfiles/bspwm/* ~/.config/bspwm/")
        os.system("chmod +x ~/.config/bspwm/bspwmrc")
        # Copy Wallpaper
        os.system("cp Dotfiles/wall.jpg ~/Pictures/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring BSPWM:")
        print(debug)
    print()

def polybar():
    step()
    print("Configuring Polybar...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/polybar/")
        os.system("mkdir ~/.config/bin/")
        os.system("cp -R Dotfiles/polybar/* ~/.config/polybar/")
        os.system("cp -R Dotfiles/bin/* ~/.config/bin/")
        os.system("chmod +x ~/.config/polybar/launch.sh")
        os.system("chmod +x ~/.config/bin/*")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Polybar:")
        print(debug)
    print()

def rofi():
    step()
    print("Configuring Rofi...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/rofi/")
        os.system("cp -R Dotfiles/rofi/* ~/.config/rofi/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Rofi:")
        print(debug)
    print()

def picom():
    step()
    print("Configuring Picom...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/picom/")
        os.system("cp -R Dotfiles/picom/* ~/.config/picom/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Picom:")
        print(debug)
    print()

def sxhkd():
    step()
    print("Configuring Sxhkd...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/sxhkd/")
        os.system("cp -R Dotfiles/sxhkd/* ~/.config/sxhkd/")
        os.system("chmod +x ~/.config/sxhkd/sxhkd-help")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Sxhkd:")
        print(debug)
    print()

def kitty():
    step()
    print("Configuring Kitty terminal...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("mkdir ~/.config/kitty/")
        os.system("cp -R Dotfiles/kitty/* ~/.config/kitty/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Kitty terminal:")
        print(debug)
    print()

def zsh():
    step()
    print("Configuring ZSH shell...", end = " ")
    try:
        # Assign ZSH as default shell for user and root
        os.system("chsh -s /bin/zsh && sudo chsh -s /bin/zsh")
        # Install powerlevel10k for user
        os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k > /dev/null/ 2>&1")
        os.system("cp Dotfiles/zsh/user/.zshrc ~/.zshrc")
        # Install powerlevel10k for root
        os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k > /dev/null/ 2>&1")
        os.system("sudo rm -rf /root/.zshrc && sudo ln -s $HOME/.zshrc /root/.zshrc")
        os.system("sudo cp Dotfiles/zsh/.p10k.zsh /root/.p10k.zsh")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring ZSH shell:")
        print(debug)
    print()

def urxvt():
    step()
    print("Configuring urxvt terminal...", end = " ")
    try:
        # Create directory and move configuration files
        os.system("cp -R Dotfiles/.Xresources ~/")
        os.system("chmod +x ~/.Xresources")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring urxvt terminal:")
        print(debug)
    print()

def nvim():
    step()
    print("Installing & configuring Nvim...", end = " ")
    try:
        # Install and load NVIM theme
        os.system("sudo apt remove --autoremove neovim -y > /dev/null 2>&1")
        os.system("wget -q https://github.com/neovim/neovim/releases/download/v0.7.0/nvim-linux64.deb")
        os.system("sudo apt install ./nvim-linux64.deb -y > /dev/null 2>&1")
        os.system("sudo rm -rf ~/.config/nvim && git clone https://github.com/NvChad/NvChad ~/.config/nvim --depth 1 > /dev/null 2>&1")
        os.system("nvim +'hi NormalFloat guibg=#1e222a' +PackerSync")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Nvim:")
        print(debug)
    print()

#################################
#           EXECUTION           #
#################################

if __name__ == '__main__': 
    id = os.getuid()

    if id != 0:
        error()
        print("You need to execute the script with sudo")
    else:
        header()
        try:
            requeriments()
            bspwm()
            polybar()
            rofi()
            picom()
            sxhkd()
            kitty()
            zsh()
            urxvt()
            nvim()
            success()
            print("Configuration successfully applied. Please, restart system and select bspwm on the next login.")
        except Exception as debug:
            error()
            print("Something went wrong during the configuration.")
