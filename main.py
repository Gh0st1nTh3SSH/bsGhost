import os
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
    print("]", end = " ", flush = True)

def step():
    white()
    print("[", end = "")
    yellow()
    print("+", end = "")
    white()
    print("]", end = " ", flush = True)

def install():
    white()
    print("[", end = "")
    purple()
    print("*", end = "")
    white()
    print("]", end = " ", flush = True)

def success():
    white()
    print("[", end = "")
    green()
    print("✔", end = "")
    white()
    print("]", end = " ", flush = True)

#################################
#           FUNCTIONS           #
#################################
def header():
    os.system("clear")
    purple()
    banner = """
 ▄▀▀█▄▄   ▄▀▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄ 
▐ ▄▀   █ █ █   ▐ █        █  █   ▄▀ █      █ █ █   ▐ █    █  ▐ 
  █▄▄▄▀     ▀▄   █    ▀▄▄ ▐  █▄▄▄█  █      █    ▀▄   ▐   █     
  █   █  ▀▄   █  █     █ █   █   █  ▀▄    ▄▀ ▀▄   █     █       By Gh0st1nTh3SSH
 ▄▀▄▄▄▀   █▀▀▀   ▐▀▄▄▄▄▀ ▐  ▄▀  ▄▀    ▀▀▀▀    █▀▀▀    ▄▀       
█    ▐    ▐      ▐         █   █              ▐      █         
▐                          ▐   ▐                     ▐         
▐                                                                                
    """
    print(banner)
    white()

def requeriments():
    step()
    print("Installing requirements...", end = " ", flush = True)
    try:
        # Update & Upgrade system
        os.system("sudo apt update -y > /dev/null 2>&1 && sudo apt -y upgrade > /dev/null 2>&1")
        # Install packages and dependencies
        # os.system("sudo apt install net-tools libuv1-dev build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev -y > /dev/null 2>&1")
        # os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev -y > /dev/null 2>&1")
        # os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev -y > /dev/null 2>&1")
        os.system("sudo apt install neofetch bspwm polybar fzf neovim rofi sxhkd kitty feh xclip bat rxvt-unicode zsh-autosuggestions zsh-autocomplete zsh-syntax-highlighting -y > /dev/null 2>&1")
        # Install LSD
        os.system("wget -q https://github.com/Peltoche/lsd/releases/download/0.21.0/lsd_0.21.0_amd64.deb")
        os.system("sudo apt ./install lsd_0.21.0_amd64.deb -y > /dev/null 2>&1")
        os.system("rm lsd_0.21.0_amd64.deb")
        # Install Hack Nerd Fonts
        os.system("sudo wget -q https://github.com/ryanoasis/nerd-fonts/releases/download/v2.1.0/Hack.zip -O /usr/share/fonts/Hack.zip")
        os.system("sudo mkdir /usr/share/fonts/Hack/ && sudo unzip /usr/share/fonts/Hack.zip -d /usr/share/fonts/Hack/ > /dev/null 2>&1 && fc-cache -v > /dev/null 2>&1")
        os.system("sudo rm /usr/share/fonts/Hack.zip") 
        success()
    except Exception as debug:
        error()
        print("There was an error installing requirements:")
        print(debug)
    print()
    
def bspwm():
    step()
    print("Configuring BSPWM...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/bspwm/")
        os.system("cp -R Dotfiles/bspwm/* $HOME/.config/bspwm/")
        os.system("chmod +x $HOME/.config/bspwm/bspwmrc")
        # Copy Wallpaper
        os.system("cp Dotfiles/wall.jpg $HOME/Pictures/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring BSPWM:")
        print(debug)
    print()

def polybar():
    step()
    print("Configuring Polybar...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/bin/")
        os.system("cp -R Dotfiles/polybar/* $HOME/.config/polybar/")
        os.system("cp -R Dotfiles/bin/* $HOME/.config/bin/")
        os.system("chmod +x $HOME/.config/polybar/launch.sh")
        os.system("chmod +x $HOME/.config/bin/*")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Polybar:")
        print(debug)
    print()

def rofi():
    step()
    print("Configuring Rofi...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/rofi/")
        os.system("cp -R Dotfiles/rofi/* $HOME/.config/rofi/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Rofi:")
        print(debug)
    print()

def picom():
    step()
    print("Configuring Picom...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/picom/")
        os.system("cp -R Dotfiles/picom/* $HOME/.config/picom/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Picom:")
        print(debug)
    print()

def sxhkd():
    step()
    print("Configuring Sxhkd...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/sxhkd/")
        os.system("cp -R Dotfiles/sxhkd/* $HOME/.config/sxhkd/")
        os.system("chmod +x $HOME/.config/sxhkd/sxhkd-help")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Sxhkd:")
        print(debug)
    print()

def kitty():
    step()
    print("Configuring Kitty terminal...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("mkdir $HOME/.config/kitty/")
        os.system("cp -R Dotfiles/kitty/* $HOME/.config/kitty/")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Kitty terminal:")
        print(debug)
    print()

def zsh():
    step()
    print("Configuring ZSH shell...", end = " ", flush = True)
    try:
        if id != 0:
            # Install powerlevel10k for user
            os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $HOME/.powerlevel10k > /dev/null 2>&1")
            os.system("cp Dotfiles/zsh/.zshrc $HOME/.zshrc")
        else:
            # Assign ZSH as default shell
            os.system("usermod --shell /usr/bin/zsh $USER && usermod --shell /usr/bin/zsh root")
            # Install powerlevel10k for root
            os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k > /dev/null 2>&1")
            os.system("cp Dotfiles/zsh/.zshrc $HOME/.zshrc")
            os.system("sudo cp Dotfiles/zsh/.p10k.zsh /root/.p10k.zsh")
            # Install sudo plugin
            os.system("wget -q https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/plugins/sudo/sudo.plugin.zsh -O /usr/share/zsh-sudo/sudo.plugin.zsh")           
        success()
    except Exception as debug:
        error()
        print("There was an error configuring ZSH shell:")
        print(debug)
    print()

def urxvt():
    step()
    print("Configuring urxvt terminal...", end = " ", flush = True)
    try:
        # Create directory and move configuration files
        os.system("cp -R Dotfiles/.Xresources $HOME/")
        os.system("chmod +x $HOME/.Xresources")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring urxvt terminal:")
        print(debug)
    print()

def nvim():
    step()
    print("Installing & configuring Nvim...", end = " ", flush = True)
    try:
        if id == 0:
            # Install and load NVIM theme
            os.system("sudo apt remove --autoremove neovim -y > /dev/null 2>&1")
            os.system("wget -q https://github.com/neovim/neovim/releases/download/v0.7.0/nvim-linux64.deb")
            os.system("sudo apt install ./nvim-linux64.deb -y > /dev/null 2>&1 && rm -rf ./nvim-linux64.deb")
        os.system("rm -rf $HOME/.config/nvim && git clone https://github.com/NvChad/NvChad $HOME/.config/nvim --depth 1 > /dev/null 2>&1")
        os.system("nvim +'hi NormalFloat guibg=#1e222a' +PackerSync")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring Nvim:")
        print(debug)
    print()

def htbExplorer():
    step()
    print("Installing & configuring htbExplorer...", end = " ", flush = True)
    try:
        # Install and load NVIM theme
        os.system("mkdir -p $HOME/Workspace/HackTheBox/VPN && mkdir $HOME/Workspace/HackTheBox/Machines && mkdir $HOME/Workspace/HackTheBox/Challenges")
        os.system("wget -q https://raw.githubusercontent.com/s4vitar/htbExplorer/master/htbExplorer -O $HOME/Workspace/HackTheBox/.htbExplorer")
        os.system("chmod +x $HOME/Workspace/HackTheBox/.htbExplorer")
        success()
    except Exception as debug:
        error()
        print("There was an error configuring htbExplorer:")
        print(debug)
    print()
   
#################################
#           EXECUTION           #
#################################

if __name__ == '__main__': 
    id = os.getuid()
    header()
    if id != 0:
        try:
            bspwm()
            polybar()
            rofi()
            picom()
            sxhkd()
            kitty()
            zsh()
            urxvt()
            nvim()
            htbExplorer()
            success()
            print("Configuration successfully applied.\nIf you already executed the script with sudo, please restart system and select bspwm on the next login.")
        except Exception as debug:
            error()
            print("Something went wrong during the configuration.")
    else:
        try:
            requeriments()
            zsh()
            nvim()
            success()
            print("Configuration successfully applied.\nIf you already executed the script as user, please restart system and select bspwm on the next login.")
        except Exception as debug:
            print("Something went wrong during the configuration.")
        