![Morris Internet Worm](Worm.jpg)

>>> deploy:<br>
>>>  Journal.md<br>
>>>  +Worm.jpg<br>
>>>  +wormvax.gif<br>

# Morris Internet Worm

```
TO DO: I want to get the EXACT layout of the buffer contents byte for byte.
```

On November 2nd, 1988 the famous Internet Worm accidentally escaped author Morris's clutches before he had finished it. The worm was 
supposed to spread as a single, tiny process running in the background of each infected machine. Instead, the premature version 
proliferated on each machine quickly consuming all available CPU resources. In less than four days the virus brought over 60,000 
machines to their knees.

The virus exploited several holes in the UNIX operating system. One particularly gaping hole in the gets() library call, allowed the 
virus to create a root shell on a remote machine! Let's dig into that hole more closely.

Most C programmers are familiar with the C library call gets(char *buffer), which reads a line of text from the standard input (normally the keyboard) 
into the supplied buffer. But what happens if the line is too long to fit in the buffer? The library has no way of knowing how big the buffer is, and it 
blindly writes over whatever memory is beyond the end. If the buffer is at the end of a segment, you get a segmentation violation. If the buffer is on 
the stack, you overwrite the stack frame -- which is what happened in the case of the worm.

Programs written in C use the stack to create local variables upon entry to a function. (Storage that is malloced or newed comes from another area of the 
process memory called the heap.) Stacks grow from the bottom of the address space upwards towards the heap, which is growing downwards towards the stack. 
When a C program makes a call from function A to function B, the return address (the pointer to the next statement in function A) is pushed onto the stack. 
Then function B creates its variables on the stack and begins to do whatever function B does. At the end of the function, the local variables for B are pulled 
from the stack, and the CPU uses the return address to continue in function A.

Since the stack builds "backwards", a buffer-overflow on the stack overwrites variables defined earlier. But worst of all, a buffer-overflow on the stack 
overwrites the return address of the calling function. When the CPU tries to unwind the stack, it finds itself returning to a bogus location. A bogus location 
at best -- a clever programmer could plan the overwrite to return the CPU to another section of code, say a tiny program fragment embedded in the buffer overflow. A clever programmer could do this, if he of she could gain access to a running program that uses gets() to fill a stack buffer!

A program called inetd runs in the background of a UNIX workstation and listens for connection requests on several "well known" ports (see /etc/services). 
When a remote program connects to port 79, inetd launches the fingerd program to serve the incoming finger request. (Fingerd returns harmless information 
like what a specific user's real name is.) Inetd creates a socket for the communication and connects it to the standard input/output of the new process 
allowing fingerd to communicate with the client using the standard I/O routines -- like gets() -- as if the were simply talking to the console. When 
fingerd finishes its work, it terminates in the usual way by returning from main.

The virus connects to inetd on the target machine. The inetd server spawns fingerd to handle the request attaching the network socket to the standard I/O. 
The main routine of fingerd is called -- the normal return from main is pushed onto the stack. Then the local variables for main are pushed onto the stack. These 
include a fixed-size buffer for reading the request from the input stream. Next main reads a line of text from the standard input (coming from the virus) into the 
stack-buffer and looks up the given user name. Main sends the fetched "finger" information back to the virus and terminates -- or rather it tries to terminate -- by 
popping the return address from the stack.

The source code for fingerd is readily available, and Morris knew exactly what the stack frame looks like. The virus sends a carefully constructed string of 536-bytes 
to the fingerd process that overflows the stack-buffer spilling into the return address on the stack. The string includes a tiny binary program fragment (shown below) 
that lies near the middle of the input buffer. Surrounded by NOPs. (The NOP framing helps if the stack addresses are slightly different from run to run). The return 
address is overwritten with the address of the program in the buffer. When the fingerd process finishes and attempts to return normally from main, the CPU jumps to the 
program fragment instead! Quite clever.

What does the fragment do? It simply performs the function execve("/bin/sh",0,0) which abandons the currently running code and loads a new program -- in this case an 
interactive shell that inherits the file descriptors of the dying program. In other words, the fingerd server turns into a shell whose input is attached to the virus 
on the remote machine. The virus is free to send standard UNIX commands to the shell, and since fingerd runs as root, the new shell is a root shell with unrestricted 
access to the local machine.

A program downloaded like this is very machine-dependant. The author could have constructed other binary fragments to be sent to fingerd servers on other 
platforms (like SUNs), but for some reason he only assembled the VAX version. The virus could use several methods of attack, but this particular method worked 
only on VAXes.

In the end, the guard against the gets() hole was easy to make. Fingerd was simply re-written using fgets(), which allows the length of the buffer to be passed in. 
How a function like gets() made it into the standardized C library is a mystery.

# Code Walkthrough

```
; VAX binary code fragment from the Morris Internet Worm.
; Downloaded to the fingerd serving process via the gets() hole.
; Performs execve("/bin/sh",0,0)
pushl	$0068732f	; last half of name: "/sh\0"
pushl	$6e69622f	; first half of name: "/bin"
mov	sp,r10		; pointer to the string
pushl	$0		; 3rd parameter: environment = null
pushl	$0		; 2nd parameter: args = null
pushl	r10		; 1st parameter: pointer to the executable name
pushl	$3		; 3 parameters on the stack
movl	sp,ap		; ArgumentPointer points to arguments
chmk	$3b		; SoftwareException 0x3B = EXECVE call
```

The first two pushes create a single string on the stack (which happens to be exactly eight bytes, two longs). This string, "/bin/sh", is the filename to 
load in the execve() call.
We can tell a little about the VAX architecture from this string. The ASCII characters are encoded backwards in the hexadecimal constant. In order to arrange 
the string correctly in memory, the little end has to be written first - the VAX is a Little-Endian (like the PC).

The next instruction, the MOV instruction, records the stack pointer in R10. This looks backwards with the destination, R10, on the right side of the comma. 
This is the way VAX assembler (and most RISC assembler) is written.

The next three instructions push the arguments for execve() onto the stack in reverse order: first the environment-block and the command-line argument-list 
(null pointers) and then the pointer to the filename string.

The "pushl $3" pushes the value 3 onto the stack. This indicates the number of parameters that are being passed in the function call (some functions take a 
variable number of parameters). Next, the AP (the argument pointer) is set to point to the first parameter on the stack. Why not use the stack pointer as 
pointer to the arguments? Because the stack pointer is about to change as context information is pushed onto the stack with the software exception call.

The last instruction is the software-exception. It is similar to the PC software-interrupt in that it looks up a vector (vector 3B) in a table of jumps, but 
much more happens under the sheets. The CPU goes from USER mode to KERNEL mode giving the hardware permission to access resources that "normal code" cannot 
touch. Only the KERNEL mode can access the vector table, which prevents a virus from "hooking" into a system call.

Remember the filename string that got pushed onto the stack first? Where does it get removed? Normally, the instructions following the CHMK would have to 
clean the stack. However, this system call is an execve() call, which starts a new program. There is no next-instruction for this program! The string is 
cleaned when the original process is torn down.

# Preliminary work on the VAX stack frame 

![](wormvax.gif)
