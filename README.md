<h1 align="center">AutoGitSync</h1>

## 📜 About
AutoGitSync is an automated tool that pushes the git repo to a remote git repo.

## ⚒️ Start contributing
I wanted to make the setup of the environment as easy as possible. To start the environment you need the 
following prerequisites:

### Prerequisites
  * GitPython
  * loguru
  * requests
  
### Start environment
You only (_fingers crossed_) need to execute the following to start the environment:

```commandline
pip install -r requirements.txt
```
You need to modify `AutoGitSync/setting.conf` to specify the git repo you want to back up.
Of course, you can also change `AutoGitSync/util/util.py` to design your own notification module.

## Architecture and patterns

The structure of the code is the following:
  * `AutoGitSync/git`: git repo are kept here.
  * `AutoGitSync/Log`: log files
    
## FAQ
**What can this tool do?**

 * You can use it to back up your project.
 
## 🚩 License
The code is available under the [Apache-2.0 license](LICENSE.md).
