# Docker Installation

## Mac installation

[Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac) System Requirements:
- 2010 or newer model with at least OS X 10.11
- At least 4GB Ram
- VirtualBox prior to version 4.3.30 must not be installed

## Windows

[Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows) System Requirements:
- Windows 10 Professional or Enterprise
- 64-bit and 4GB ram
- Virtualization and Hyper-V enabled

[Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/) (Windows) System Requirements:
- Windows 7 or later
- 64-bit and 4GB ram
- Must download VirtualBox (included in install)

Note: To use the `make setup` command in Windows natively, you'll also need to download and install [gnuwin32](http://gnuwin32.sourceforge.net/packages/make.htm) for Windows


_If you have difficulty getting things up and running, or any other technical issues that impede your ability to complete this exercise, please email us at [coding.challenge@amino.com](mailto:coding.challenge@amino.com)._

# Docker Troubleshooting 


## Docker for Windows version issues:
 
Error on installation:
> Docker for Windows requires Windows 10 Pro or Enterprise version 14393, or Windows server 2016 RTM to run

**FIX**: Install the Docker toolbox instead ([Windows 10 Home or Windows 7/8](https://docs.docker.com/toolbox/toolbox_install_windows/))

## Docker for Windows native virtualization error

Error on opening docker:
> Unable to stop: The running command stopped because the preference variable "ErrorActionPreference" or common parameter is set to Stop: The specified module 'Hyper-V' was not loaded because no valid module file was found in any module directory.
> at <ScriptBlock>, <No file>: line 79
>    at Docker.Backend.HyperV.RunScript(String action, Dictionary`2 parameters) in C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\HyperV.cs:line 177
>    at Docker.Backend.ContainerEngine.Linux.DoStop() in C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\ContainerEngine\Linux.cs:line 279
>    at Docker.Backend.ContainerEngine.Linux.Start(Settings settings, String daemonOptions) in C:\gopath\src\github.com\docker\pinata\win\src\Docker.Backend\ContainerEngine\Linux.cs:line 122
>    at Docker.Core.Pipe.NamedPipeServer.<>c__DisplayClass9_0.<Register>b__0(Object[] parameters) in C:\gopath\src\github.com\docker\pinata\win\src\Docker.Core\pipe\NamedPipeServer.cs:line 47
>    at Docker.Core.Pipe.NamedPipeServer.RunAction(String action, Object[] parameters) in C:\gopa

**FIX**: Consult resources on [enabling Hyper-V](https://www.howtogeek.com/213795/how-to-enable-intel-vt-x-in-your-computers-bios-or-uefi-firmware/) or use Docker Toolbox instead (reccomended).


## Docker Toolbox: VirtualBox not connected properly

When trying to open the Docker Quickstart Terminal:
> open C:\Users\user\.docker\machine\machines\default\config.json: The system cannot find the file specified.
> Looks like something went wrong in step ´Checking status on default´... Press any key to continue...

OR when referencing trying to use docker in shell:
> docker-compose -f docker-compose.yml -p amino-challenge stop
> [13464] Failed to execute script docker-compose
> Traceback (most recent call last):
>   File "docker-compose", line 6, in <module>
>   File "compose\cli\main.py", line 71, in main
>   File "compose\cli\main.py", line 124, in perform_command
>   File "compose\cli\command.py", line 38, in project_from_options
>   File "compose\cli\docker_client.py", line 84, in tls_config_from_options
>   File "site-packages\docker\tls.py", line 81, in __init__
> docker.errors.TLSParameterError: Path to a certificate and key files must be provided through the client_config param. TLS configurations should map the Docker CLI client configurations. See https://docs.docker.com/engine/articles/https/ for API details.
> docker-compose -f docker-compose.yml -p amino-challenge rm -f
> [3752] Failed to execute script docker-compose
> Traceback (most recent call last):
>   File "docker-compose", line 6, in <module>
>   File "compose\cli\main.py", line 71, in main
>   File "compose\cli\main.py", line 124, in perform_command
>   File "compose\cli\command.py", line 38, in project_from_options
>   File "compose\cli\docker_client.py", line 84, in tls_config_from_options
>   File "site-packages\docker\tls.py", line 81, in __init__
>   ...

**FIX**: Create an accessible machine
1. Open VirtualBox. The machine `default` should be running but not accessible (there may be a dialog warning)
2. Select `default` machine and CTRL+F (power off).
3. Click "Power Off". The machine is now off. 
4. With the `default` machine powered off, CTRL+R (remove). 
5. Delete all files. Now there should be no machines running or available
6. Open Docker Quickstart Terminal again. It will create and start up a new machine. Setup should now work.
