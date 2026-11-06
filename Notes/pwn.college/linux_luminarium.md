# Linux Luminarium
> Manpages -> documentation (aka "your best friend")

# The Prompt
- `<username>@<hostname>:<cwd><$ or #> <cmd> <argument(s)>`
    - Called the "prompt" because it's prompting for a command
    - username -> Name of the current user
    - hostname -> Name of the host
    - cwd -> Current Working Directory
    - $ -> User, unprivileged
    - # -> Root, privileged
    - cmd -> command (e.g. ls)
    - argument(s) -> passes additional data to the command (e.g. ls **-la**)

# Linux Filesystem
- Files -> Locations the computer stores data in
- Directories -> Provides a way to store and organize files or other directories
- Path -> The route it takes to reach a file or directory
    - Absolute Path -> The direct route from root
    - Relative Path -> The route from the cwd
        - `.` -> Current directory
        - `..` -> Previous directory
        - `~` -> Home directory
- Typical Linux filesystem layout:
    - `/` -> The "anchor" of the filesystem, pronounced "root"
        - `/usr` -> The Unix System Resource, contains all system files
            - `/usr/bin` -> Executable files for programs installed onto the system
            - `/usr/lib` -> Shared librarries for use by programs on the computer
            - `/usr/share` -> Program resources (icons, assets, etc)
        - `/etc` -> System configuration
        - `/var` -> Logs, caches, etc
        - `/home` -> User-owned data
        - `/proc` -> Runtime process data
        - `/tmp` -> Temporary data storage
- Navigation
    - `pwd` -> Prints cwd
    - `ls` -> Lists files in cwd
    - `cd` -> Change directory

# File Globbing
> By default, if nothing is matched the glob itself will be returned
- `*` -> Matches anything of anylength
- `?` -. Matches anything of 1 char length
- `[]` -> Matches anything within the bracket of 1 char length
    - Append ^ (on newer versions) or ! will invert this glob

# Piping & IO
> On linux everything is a file
- file descriptor (fd) -> A unique non-negative number for identifying a file
- Linux has three standard streams:
    - Standard Input / stdin
        - fd: 0
        - file: /dev/stdin
    - Standard Output / stdout
        - fd: 1
        - file: /dev/stdout
    - Standard Error / stderr
        - fd: 2
        - file: /dev/stderr
- Redirect output with `CMD > FILE`
- Redirect & append output with `CMD >> FILE`
- Redirect output of other standard streams by fd with `CMD (fd) > FILE` `CMD 2 > FILE`
- Redirect input from a file with `CMD < FILE`
- Pipe stdout into stdin with `CMD | CMD`
- Redirect to different fd with (fd1 -> fd2) `CMD (fd1)>&(fd2)` `CMD 2>&1`
- `tee` -> Duplicates data in the pipes into files provided as argument
- Process Substitution -> Allows a process's IO to be referred to with a temporary file known as a named pipe
    - Named pipe: `/dev/fd/??`
    - `<(CMD)` -> Reading the file obtains output of CMD
    - `>(CMD)` -> Writing to the file provides input to CMD

# Bash Variables
- May contain numbers, a character, or a string of characters
- Defined by `VAR=value`
- Variables are called by prepending $ `echo $VAR`
- Local variables are defined by preprending `local` `local VAR=value`
- `export VAR` -> EXports variable into child processes
- `env` -> Prints every *exported* variables
- `read` -> Reads inpput to set a variable
    - `-p` to defined a prompt
- Command Substitution -> Replaces `$(CMD)` w/ the output of `CMD`
    - `VAR=$(CMD)`

# Linux Processes
- `ps` -> To list processes
- `kill` -> To kill processes
- `CTRL-C` -> Hotkey to kill the current process
- `CTRL-Z` -> Hotkey to suspend the current process
- `fg` -> Brings suspended/backgrounded process back to foreground
- `bg` -> Brings suspended processses into the background
- `$?` -> Exit code of the previous command

# Temp (glob)
- `username:password:uid:gid:home_directory:default_shell`
- Actual password is stored in `/etc/shadow`
- `/etc/passwd` exists for historical reasons

- `su <username>` -> To change user
- `sudo <CMD>` -> To run `CMD` as root 
