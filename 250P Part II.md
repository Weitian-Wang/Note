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
      - [Physical Address](#physical-address)
      - [Virtual Address](#virtual-address)
      - [Segmentation - Old School Solution](#segmentation---old-school-solution)
        - [Basics](#basics)
        - [Swapping](#swapping)
        - [Problem - External Fragmentation](#problem---external-fragmentation)
      - [Paged Virtual Memory](#paged-virtual-memory)
        - [Basics](#basics-1)
        - [Page Table](#page-table)
        - [Page Table Entry](#page-table-entry)
        - [Pros \& Cons](#pros--cons)
          - [Pros](#pros)
          - [Cons](#cons)
        - [Implementation](#implementation)
        - [Translation Lookaside Buffer - TLB](#translation-lookaside-buffer---tlb)
          - [Basics](#basics-2)
          - [Virtual Memory Access with TLB](#virtual-memory-access-with-tlb)
          - [Pros with TLB](#pros-with-tlb)
        - [Size of Page](#size-of-page)
          - [Large Page Size](#large-page-size)
          - [Small Page Size](#small-page-size)
          - [Solution](#solution)
        - [Hierarchical Page Table](#hierarchical-page-table)




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
This topic itself can be a whole section.  
#### Goal
1. Protection and privacy: processes can not access each other's data (memory space).  
2. Abstract memory resource: Provide private address space to processes. From processes' POV, they each have exclusive access to large, uniform address space.
#### Physical Address
Actual address on the physical DRAM. Managed & visible to 
#### Virtual Address
Virtual address generated by a process, points to its private address space. The translation between physical and virtual address is done by memory management unit (MMU hardware in CPU).
#### Segmentation - Old School Solution
##### Basics
Memory segmentations of **various sizes** are allocated to processes. The segmentation size depends on requirements of different processes. The OS maintains the base addresses and sizes of the segmentations. OS check segmentation bounds when accessing to avoid reading other processes' memory space.
$$\text{Physical Address} = \text{Virtual Address} + \text{Base Address}$$
##### Swapping
Entire segmentations are swapped between main memory and main storage to make space for other processes.
##### Problem - External Fragmentation
Variable sized sementation efficiently utilizes the memory space within the segmentation. But since the segmentation can't be split up when allocated or swapped in, unused chunks of memory fragments will appear main memory.  
Fragementation is hard to deal with and solutions can be costly.
#### Paged Virtual Memory
##### Basics 
Physical memory is divided into **fixed-size** pages.
> The size usually 4KiB, 4096 bytes


For the sake of translating virtual address to physical address, virtual memory address is interpreted as 
$$|\ \text{virtual page number}\ |\ \text{page internal offset}\ |$$
##### Page Table
OS uses a page table to translate (page table walk, handled by MMU) virtual page number to physical page number, then add page internal offset to get actual memory address.  
**OS** maintains a page table for **each** process.  
Physical address space may be larger than virtual address space.  
##### Page Table Entry
PTE is a single page line, page table is an array of page table entry.  
PTE holds the mapping between a single virtual page address and phyical page address.  
PTE also holds flags of each page, indicating page properties like read-only.  
##### Pros & Cons
###### Pros
Pages can be stored non-contiguously thanks to address lookup provided by page table. This greatly reduces external fragmentation. 
###### Cons
The storage and maintenance cost of page table is larger than segmentation (32bit base + 32bit size bound for each process). Page table is stored in DRAM.  
##### Implementation
Best case two main memory access is required for each virtual memory access.  
$$\text{Physical Page Number} = \text{Mem}[\text{Page Table Base}+\text{Virtual Page Numer}]$$  
$$\text{Physical Address} = \text{Physical Page Number} + \text{Offset}$$  

##### Translation Lookaside Buffer - TLB
One of the eight great ideas "Make the Common Case Fast". As we analysed in the page table implementation, there is a large speed overhead as two main memory accesses are executed for each virtual memory access.
###### Basics
Cache some virtual-to-physical address translations (just like how data cache works) to reduce memory access.  
Index by subset of virtual page number.  
Tagged by remainder of virtual page numer.  
Such mapping scheme has associativity issues.  
```
┌───────────────────────────────────────────────┐
│            Virtual Memory Address             │
└───────────────────────────────────────────────┘
┌───────────────────────────────────┬───────────┐
│        Virtual Page Number        │  Offset   │
└───────────────────────────────────┴───────────┘
┌────────────────────┬──────────────┬───────────┐
│     TBL Index      │   TBL Tag    │  Offset   │
└────────────────────┴──────────────┴───────────┘
* proportion of graph not accurately represent number of bits
```
###### Virtual Memory Access with TLB

1. TLB Hit - immediate address translation 
2. TLB Miss - walk entire page table, load page into TLB for future use

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStV-09pjH7NAP1XsYLW7VAUKgARzYw25Wl4g&usqp=CAU">
###### Pros with TLB
- Low miss rate result from benchmark, except for random access like graph
- Exploits the locality, TLB target is 4KiB page size, which is larger than cache target cache lines.

##### Size of Page
Why 4KiB page size?  
4GiB physical address space, 32 bit address  
4KiB page size  
number of pages (entries) = 4GiB/4KiB = $2^{32} \div 2^{12} = 2^{20}$  
page table size = #entries $\times$ entry size  
page table size = $2^{20}\times4\text{bytes}=2^{22}\text{byte} = 4\text{MiB}$, assume 4 byte page table entry   
> There is one full page table for each process. If there are 256 processes in the OS, the total size of page tables would be $4\times 265=1024\text{MiB}=1\text{GiB}$.
###### Large Page Size
Smaller number of entries, reduces page table size. Underutilized page internal memory will cause internal fragmentation.
###### Small Page Size
Reduce internal fragmentation. Number of entries will increase, result in large page table size and extra memory cost for maintaining the page table.
###### Solution
Hierarchical page tables.

##### Hierarchical Page Table
Most process doesn't use all the virtual memory available, which means most page table entries is not used.  
Split page table number into L1 and L2 page number. We can reduce the size of page table  by only creating corresponding L2 page tables when L1 page table entry is accessed.   
Downside: More memory access when TLB misses.  
```
┌───────────────────────────────────────────────┐
│            Virtual Memory Address             │
└───────────────────────────────────────────────┘
┌───────────────────────────────────┬───────────┐
│        Virtual Page Number        │  Offset   │
└───────────────────────────────────┴───────────┘
┌─────────────────┬─────────────────┬───────────┐
│  L1 Page Number │  L2 Page Number │  Offset   │
└─────────────────┴─────────────────┴───────────┘
* proportion of graph not accurately represent number of bits
```

Breakpoint: Hierarchical page tables