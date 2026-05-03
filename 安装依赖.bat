if exist C:\Users\onekey\.conda\envs\onekey (
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate onekey; pip install pyecharts einops pingouin -i https://mirrors.ustc.edu.cn/pypi/web/simple"
) else (
%windir%\System32\WindowsPowerShell\v1.0\powershell.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\ProgramData\Anaconda3\shell\condabin\conda-hook.ps1' ; conda activate %ONEKEY_HOME%onekey_envs; pip install pyecharts einops pingouin  -i https://mirrors.ustc.edu.cn/pypi/web/simple"
)
pause