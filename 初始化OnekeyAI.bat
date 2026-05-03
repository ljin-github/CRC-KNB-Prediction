setx KMP_DUPLICATE_LIB_OK TRUE
setx ONEKEY_HOME %cd%\
setx ONEKEY_VIDEO %cd%\OnekeyVideo
setx R_HOME %cd%\onekey_envs\Lib\R
setx R_USER %cd%\onekey_envs\Lib\site-packages\rpy2

%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate '%ONEKEY_HOME%\onekey_envs'; python -m pip install -U pip --upgrade --force-reinstall -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com; pip uninstall jupyter jupyter_core jupyter-client jupyter-console notebook==6.4.11 qtconsole nbconvert nbformat -y; pip install jupyter -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com; pip install moviepy -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com"

pause