- [CS250P Computer System Architecture Part II](#cs250p-computer-system-architecture-part-ii)
  - [Operating System](#operating-system)
    - [Old vs Mordern](#old-vs-mordern)
      - [Old OS](#old-os)
      - [Mordern OS](#mordern-os)
  - [Architectural Support for OS](#architectural-support-for-os)
    - [Privilege Levels](#privilege-levels)
      - [RISC-V](#risc-v)
      - [x86](#x86)
    - [Exceptions and Interrupts](#exceptions-and-interrupts)
      - [Exceptions](#exceptions)
      - [Interrupts](#interrupts)
      - [Handling](#handling)
      - [Utilization of Exception](#utilization-of-exception)
    - [Context Switching](#context-switching)
      - [Stack and Stack Pointer](#stack-and-stack-pointer)
      - [PCB - Process Control Block](#pcb---process-control-block)
    - [System Boot Process](#system-boot-process)
    - [Virtual Memory](#virtual-memory)
      - [Goal](#goal)
      - [Segmentation - Old School Solution](#segmentation---old-school-solution)
        - [Basics](#basics)
        - [Swapping](#swapping)
        - [Problem](#problem)
      - [Physical Address](#physical-address)
      - [Virtual Address](#virtual-address)




# CS250P Computer System Architecture Part II
## Operating System
### Old vs Mordern
#### Old OS
Old personal operating systems like MS-DOS are basic. 
1. OS and user software run together.
2. Software has all access to hardware.
3. Only one software runs at a time.
4. Software failure will lead to system crash.
#### Mordern OS
1. User Process Isolation
2. OS kernal provides a private address space to each process
3. OS kernal schedules processes into CPU
4. OS kernal let processes invoke system services via system calls
> Process's POV of mordern OS:
> 1. Has exclusive access to a contiguous address space
> 2. Can not access memory spaces of other processes or OS
> 3. Only run on CPU for allowed CPU time  

## Architectural Support for OS
What ISA needs to provide for mordern OS to function properly.
### Privilege Levels
#### RISC-V
The implementation of OS privilege levels needs ISA support. Special register "mstatus" and dedicated read & write instrucitons. 
1. Machine Level - full access
2. Hypervisor
3. Supervisor
4. User Level
#### x86
Protection Ring, inner ring kernal level, outer ring less privileged
### Exceptions and Interrupts
Exceptions and interrupts are events that needs to be processed by the OS kernal (in higher privilege than current process). The term exception and interrputs are used interchangeably.  
#### Exceptions
Events caused by the running process itself.
1. Segmentation fault, illegal memory access
2. Divide by zero
3. System call
4. etc
#### Interrupts
Events caused by the outside world.
1. I/O
2. Keystroke 
3. Timer
4. etc
#### Handling
Handling of exceptions is a purely hardware process, the handling method of each exception is **hardwired** and predefined.  
RISC - mtvec - Machine Trap Vector  
x86 - IDTR - Interrupt Descriptor Table Register  
1. Stop current process at instruction $I_i$, complete all instruction $I_{i-1}$
2. Save pc for instruction $I_i$, save interrupt number in register
3. Enter privilege mode, disable interrupts, transfer control to **predefined** exception handler PC  
4. Return control to user process instruction $I_i$
#### Utilization of Exception
The interrupts ISA provided can be utilized to achieve bunch of things.  
1. CPU Scheduling  
  Each process is given a fraction of CPU time. Kernal set timer, raise interrupt after timer runs out. Save process 1, set new timer, load process 2, return control to process 2.

2. Emulating Instructions  
  ISA can emulate unsupported instructions with interrupts. For example mul instruction from RISC-V M extension can run on RISC-V. Exception handler is invoked when mul is executed, emulate mul with repeated add in handling function.
  
3. System Calls  
  User process can use system call to request access of system resources.
     - File Access
     - Network Connection
     - Manage Memory
     - Manage Process
     - etc
### Context Switching  
**OS SOFTWARE SUPPORT**  
On a multitasked system, process execute in small increments on processor. Context switching is required for switching the execution of different processes. Processes are still sharing the same address memory space.   
**Context**: the state information of process. All the info need to restore execution of process.   
**Context Switching**:  Storing context of current process, load context of next process.  
#### Stack and Stack Pointer
In the interrupt handler, store all register value of the process in the stack.  
How to find the stored value after exiting the handler? Store the register address in PCB.  
#### PCB - Process Control Block
PCB is used to manage context information in the OS. Stores process ID, priority, registers, program counters, process states etc. Each process has its PCB.

### System Boot Process
1. When power on, start executing from address 0. 
2. Firmware is located at address 0, which would load bootoader into special address then hand over control.
3. Bootloader loads the actual OS kernal from storage to memory and transfer control.

### Virtual Memory
This topic itself is a whole chapter.  
#### Goal
1. Protection and privacy: processes can not access each other's data (memory space).  
2. Abstract memory resource: Provide private address space to processes. From processes' POV, they each have exclusive access to large, uniform address space.

#### Segmentation - Old School Solution
##### Basics
Memory segmentations of various sizes are allocated to processes. The segmentation size depends on requirements of different processes. The OS maintains the base addresses and sizes of the segmentations. OS check segmentation bounds when accessing to avoid reading other processes' memory space.
$$\text{Physical Address} = \text{Virtual Address} + \text{Base Address}$$
##### Swapping
Entire segmentations are swapped between main memory and main storage to make space for other processes.
##### Problem
Variable sized sementation efficiently utilizes the memory space within the segmentation. But since the segmentation can't be split up when allocated or swapped in, unused chunks of memory fragments will appear main memory.


#### Physical Address
Actual address on the physical DRAM. Managed & visible to 
#### Virtual Address
Virtual address generated by a process, points to its private address space. The translation between physical and virtual address is done by memory management unit (hardware in CPU).
