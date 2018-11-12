# About the project
I just want to do some small tools to make my life better (maybe someone else too).

# Prerequisites
To run this quickstart, you’ll need:
+ Python 3.6.5 or greater.    
+ The pip package management tool (Anaconda is better).     
+ A good knowlegde about Powershell or Bash.  

# How I set up my programming environment.
## Visual Studio Code

### Extension
Because I'm main on Python and sometimes with C++. So any package related to Java is optional depend on when I use it.
  + **Anaconda Extension** by Microsoft
  + **autoDocstring** by Nils Werner
  + **Better Comments** by Aaron Bond
  + **C/C++** by Microsoft
  + **Code Runner** by Jun Han (Optional)
  + **Dark+ Material** by vangware (My favourite theme)
  + **Djaneiro - Django Snippets** by Scott Barkman **(Only when have Django project)**
  + **Django Template** by bibhasdn **(Only when have Django project)**
  + **Java Extension Pack** by Microsoft (only if learning OOP at university)
  + **GitLens** by Eric Amodio (Handful ext for Git)
  + **LaTeX Workshop** by James Yu (Disable vscode-pdf when use it)
  + **Material Icon Theme** by Philipp Kief
  + **Polacode** by P & P (Useful for sharing code)
  + **Python** by Microsoft
  + **Shell launcher** by Daniel Imms 
  + **vscode-pdf** by tomoki207

### Settings
This settings is for VSCode, some paths are needed to check because of difference in version.
```json
{
  "git.ignoreMissingGitWarning": true,
  "[cpp]": {},
  "files.autoSave": "afterDelay",
  "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe",
  "workbench.iconTheme": "material-icon-theme",
  "latex-workshop.view.pdf.viewer": "tab",
  "latex-workshop.latex.recipes": [
    {
      "name": "texify",
      "tools": [
        "texify"
      ]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "texify",
      "command": "texify",
      "args": [
        "--synctex",
        "--pdf",
        "--tex-option=\"-interaction=nonstopmode\"",
        "--tex-option=\"-file-line-error\"",
        "%DOC%.tex"
      ]
    }
  ],
  "workbench.colorTheme": "Dark+ Material",
  "gitlens.advanced.messages": {
    "suppressShowKeyBindingsNotice": true
  },
  "python.linting.pylintArgs": [
    "--load-plugins",
    "pylint_django"
  ],
  "editor.formatOnSave": true,
  "python.venvPath": "D:\\Miniconda3\\envs",
  "shellLauncher.shells.windows": [
    {
      "shell": "C:\\Windows\\System32\\cmd.exe",
      "label": "cmd"
    },
    {
      "shell": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
      "label": "PowerShell"
    },
    {
      "shell": "C:\\Program Files\\Git\\bin\\bash.exe",
      "label": "Git bash"
    },
  ],
  "java.home": "C:\\Program Files\\Java\\jdk1.8.0_181",
  "workbench.colorTheme": "Dark+ Material",
  "workbench.iconTheme": "material-icon-theme",
  "window.titleBarStyle": "custom",
  "markdown.previewFrontMatter": "show",
}
```

## Environment variables path
### Java
Create 2 more system variables:
```
JAVA_HOME: C:\Program Files\Java\jdk1.8.0_181
JRE_HOME: C:\Program Files\Java\jre1.8.0_181
```

Add this to Path:
```
PATH: C:\Program Files\Java\jre1.8.0_181
```

### Python (Anaconda)
When installed Anaconda, everything will be updated in Environment variables, so don't need to worry about it.

### C++ (MinGW)
Add this to Path in System variables:
```
PATH: C:\MinGW\bin
```

### LaTeX (MikTex)
Install only MikTex to compile .tex file
Add this to user variables PATH:
```
PATH: C:\Users\DELL\AppData\Local\Programs\MiKTeX 2.9\miktex\bin\x64\
```
But sometimes, it will be automatically added in.

## C++
Install MinGW with basic packages.
When need to compile .cpp and debug it, I use vs-support.py with well-fixed .json which I had uploaded to GitHub.

## Python
I use Miniconda 3 as my package management which very handul. But remember `conda update conda python` after install.
There are 3 must-have packages I installed in every environments:
  + pylint
  + autopep8 (channel **conda-forge**)
  + ipython
  + pyinstaller (channel **conda-forge**) (optional)
  + nuitka (optional but must need **mingw_w64** in system)

There are some environments I'm working on it:
  + **IMG_MANIP**: *pillow* and *opencv2*
  + **WEB_TEST**: *selenium*
  + **CRAWL**: *BeautifulSoup4*, *requests* and *PyQT*
  <!-- + **WEB**: *Django* -->

There are some problems with **pyinstaller** and **opencv2**. They don't work well with each other much, where compile python script, **pyinstaller** will miss some dll module in **opencv2**. So must check it out and copy to *dist* folder:
  + opencv_datasets*.dll
  + opencv_dnn_objdetect*.dll
  + opencv_dpm*.dll
  + opencv_ffmpeg*.dll
  + opencv_stereo*.dll
  + opencv_structured_light*.dll
  + opencv_superres*.dll
  + opencv_videostab*.dll
  + opencv_xobjdetect*.dll

(* are depend on *opencv2* version)

But if in portable mode, it can be resolved as:
```
pyinstaller --onefile <Python-script.py> --add-binary <env/Library/bin/opencv_ffmpeg*.dll>
```

## Java
I only use Java in few months maybe (hope so) because this is in my curriculum.
I just install Java Development Kit SE 8. And that's it, nothing more.

## LaTeX
Basically, I just install MikTex and when writing report, if I need any packages, I install it. There is no configuration I made for LaTeX.

## Bash on Ubuntu on Windows (WSL)
I installed Bash from Windows Store and look up on the internet to download **oh my zsh**.
*robbyrussell* theme is pretty perfect for me. Simple and clean.
**NOTE**:  Remember to install *DejaVu Sans Mono for Powerline* font, because Windows always miss that for Bash.

## Git
Just install it, I don't use Git Bash much. It just support for *Source Control* in Visual Studio Code.

## Evernote:
This is a quite handy application for taking note. I have a lot of lesson and technique in programming so it helps me keep things clean and organize.

# How I set up my programming smartphone (Google Pixel)
So recently, I just bought new Google Pixel for better workflow and maybe explore something new. To make it suits best for me, I upgraded it to Android 9 Pie (Android rootless - maybe will root it later for Black Subtratum Theme). And remember that should always **FACTORY RESET** after updating Android.
```
Everything I wrote down here just for backup in future (most of it). I still can use Restore & Backup from Google but careful is better.
```

Also because Google is developing Dark mode in all apps so I don't need to install Subtratum Theme Engine anymore. Now I just go to Settings -> Display -> Advanced -> Device Theme.

Also I will turn on Dark mode in Youtube and Message. And modify, turn on some built-in gestures. 

Last but not least, I must create voice recognition for Google Assistant.

## Code
### Pydroid 3
I think this is the best Python editor on Android. Great Intellisense, great typing keyboard, can install packages from pip and I think there are more.

Although, when rotate from horizontal to vertical, I experienced lag and sometimes froze. 

### CPP N-IDE
It worked out of the box. But there is something wrong with font size, I want to make it smaller because sometimes my code too long to fit in phone size.

But besides that, everything is fine, I think I will have a long time experience with it.

### Termux
Well I think it's great, I don't need to root my phone to use Terminal. And fun thing is that, it can install package with command line. 

I checked that I can install **Python** from it but sadly not **IPython**. Hope that **IPython** can come to this soon.

### OpenHub
Just a unofficial app for GitHub, I can check my workflow with my team and find some interesting repository in free times. But with current job, I think I will install something works with BitBucket.

### Codeforces
Because my current job relates all about Algorithm & Competitive Programming, so with this I always have problems to practice in free times.

## Workflow
### Dropbox
Because my team used this, so I installed it to make myself up-to-date with my team.

### Slack
This is an awesome app. A lot of things happen here, group chat with team, tags for controlling workflow, add-ons for everything (literally EVERYTHING)

### Evernote
As always my awesome notebook, my book of secret. The great thing about it is that I can sync notes between my laptop and phone.

Ugly thing is that it don't allow you to read old notes offline (not even write for upload later). DAMMIT!!!

## Others
 + Adobe Acrobat Reader
 + Google Sheets (Google Docs is builtin but not this :D ?)
 + Spotify
 + Shazam
 + FX File Explorer
 + Turn Off Screen (Lock Screen)
 + Any kind of Offline English Dictionary 
 + AccuBattery
 + Medium Blog
 + Send Anywhere