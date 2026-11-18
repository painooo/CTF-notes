# Linux Luminarium
> Manpages -> documentation (aka "your best friend")

## The Prompt
- `<username>@<hostname>:<cwd><$ or #> <cmd> <argument(s)>`
    - Called the "prompt" because it's prompting for a command
    - username -> Name of the current user
    - hostname -> Name of the host
    - cwd -> Current Working Directory
    - $ -> User, unprivileged
    - \# -> Root, privileged
    - cmd -> command (e.g. ls)
    - argument(s) -> passes additional data to the command (e.g. ls **-la**)

## Linux Filesystem
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

## File Globbing
> By default, if nothing is matched the glob itself will be returned
- `*` -> Matches anything of anylength
- `?` -. Matches anything of 1 char length
- `[]` -> Matches anything within the bracket of 1 char length
    - Append ^ (on newer versions) or ! will invert this glob

## Piping & IO
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
- You can create your own permanent named pipe w/ mkfifo


## Bash Variables
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

## Linux Processes CMDs
- `ps` -> To list processes
- `kill` -> To kill processes
- `CTRL-C` -> Hotkey to kill the current process
- `CTRL-Z` -> Hotkey to suspend the current process
- `fg` -> Brings suspended/backgrounded process back to foreground
- `bg` -> Brings suspended processses into the background
- `$?` -> Exit code of the previous command

## Changing users & /etc/passwd + /etc/shadow
- `username:password:uid:gid:home_directory:default_shell`
- Actual password is stored in `/etc/shadow`
- `/etc/passwd` exists for historical reasons

- `su <username>` -> To change user
- `sudo <CMD>` -> To run `CMD` as root

## Permissions
- Authorization -> What can you do in the system?
- Authentication -> Who are you?
- In a system @ a high level one must think about: who can do what? Do we trust them to do that? Can we eliminate risk? 

- Authorization is the policy
- Access Control implements Authorization
    - Ex: Door & Lock: Only I can access the door; I implement that policy with lock 

- How to model access control?
    - Subjects S -> Things in the system which can act
    - Objects O -> Things S can act on
    - Rights R -> What can S do to O?
    - Access Control Matrix -> Column (O), Row (S), and Cell (R)
        - We can use this to think about how to attack a system 

- In the (simplified) UNIX model:
    - Subjects are processes
    - Files are objects
    - Rights are rights
        - Read (r) -> A process can read the contents of this file
        - Write (w) -> A process can change the contents of this file 
        - Execute (x) -> A process can create a new process from this file (scripts & programs)
        - Append (a) -> A process can add to the contents of the file
        - Own (o) -> As the owner, I can grant rights to other processes

- POSIX ACL:
    - 12 bits to represesnt permission per file
    - First 3 bits -> [0]SUID, [1]SGID, [2]Sticky-bit
    - Next 3 bits
        - Owner [3..5]
        - Group [6..8]
        - All [9..11]
            - Read [first], write [second], and execute [third]
- Commands:
    - chown -> change the owner of a file (can also change group: `chown owner:group /file`)
    - chgrp -> change the group of a file
    - chmod -> change the permission mode of a file (format: WHO + or - or = WHAT, WHO: u, g, o, a; WHAT: r,w,x; you can link them together with commas)
- the SUID bit allows running the file as the owner of the file, SGID as the group
- the sticky bit prevents non-owner to change the content of a directory

## Chaining Commands
- ; -> seperates commands on after the previous
- && -> runs the next command if the previous was successful (exits with code 0)
- || -> runs the next command if the previous was unsuccessful (exits with a non-zero code)

## Bash Scripting
- #! -> placed in the beginning a file to indicate it as an interpreted program; the path following the "shebang" is the path to the interpeter
    - Executed: /path/to/interpreter executable
- Arguments w/ $0 (name of file), $1 (arg1), $2 (arg2), $3 (arg3), ...
- If statement: (syntax is very unforgiving; follow the example spaces and all)
```
if [ "$1" == "test" ]
then
    echo "test2"
# Multiple conditions:
#elif [ "$1"=="test2" ]
#then
#   echo "test"
#
# Optional else statement:
#else
#    echo "What?"
fi
```

## Terminal Multiplexing
- Commands:
    - screen -> creates a virtual terminal within the already existing terminal (work keeps running if connection is dropped)
        - Detach a session w/ Ctrl-A then d
        - Attach a session w/ screen -r <screen>
        - List sessions w/ screen -ls
        - Create a new window w/ Ctrl-A then c
        - Go to the next window w/ Ctrl-A then n
        - Go to the previous window w/ Ctrl-A then p
        - Jump to a window w/ Ctrl-A 0-9
        - See a selection of windows w/ Ctrl-A then "
    - tmux -> the newer screen
        - Uses Ctrl-B instead of Ctrl-A
        - List sessions w/ tmux ls
        - Attach a session w/ tmux a
        - See a selection of windows w/ Ctrl-B then w

## PATH
- The PATH contains a list of directories where the shell will search through to find the program which corresponds to a command
- Commands:
    - which <cmd> -> prints where the cmd actually is

## Shenanigans And Destruction (;
- In a bash shell, when starting up, it runs ~/.bashrc as a startup script -> this can be abused by an attacker 
- Fork Bomb -> An executable which continuously launches a copy of itself to oblivion
- Disk-Space Taker Upper -> `yes > file` takes up disk spae
- Root wrecker -> `rm -rf /`
    - Builtin commands will still remain
