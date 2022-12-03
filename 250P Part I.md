- [CS250P Computer System Architecture Part I](#cs250p-computer-system-architecture-part-i)
  - [Grading](#grading)
  - [Motivation](#motivation)
    - [End of Moore's Law](#end-of-moores-law)
    - [End of Dennard Scaling](#end-of-dennard-scaling)
    - [Solution](#solution)
  - [Hardware - Software Interface](#hardware---software-interface)
    - [Concept of Abstraction](#concept-of-abstraction)
    - [ISA - Instruction Set Architecture](#isa---instruction-set-architecture)
      - [Definition](#definition)
      - [Where is ISA](#where-is-isa)
      - [Types of ISA](#types-of-isa)
    - [Performance Measurements](#performance-measurements)
      - [CPU Clock](#cpu-clock)
      - [CPU Time](#cpu-time)
      - [Instruction Count](#instruction-count)
      - [Cycle per Instruction - CPI](#cycle-per-instruction---cpi)
      - [Conclusion](#conclusion)
  - [ISA Classification](#isa-classification)
    - [RISC - Reduced Instruction Set Computer](#risc---reduced-instruction-set-computer)
    - [CISC - Complex Instruction Set Computer](#cisc---complex-instruction-set-computer)
  - [RISC-V](#risc-v)
  - [x86](#x86)
  - [RISC-V Assembly \& x86 Assembly](#risc-v-assembly--x86-assembly)
  - [Digital Circuits](#digital-circuits)
    - [Why Digital Over Analog](#why-digital-over-analog)
      - [Disadvantage of Analog Computer](#disadvantage-of-analog-computer)
      - [Advantage of Digital Computer](#advantage-of-digital-computer)
    - [Types of Digital Circuits](#types-of-digital-circuits)
    - [Combinational Circuit](#combinational-circuit)
      - [Timing Specifications of Combinational Circuits](#timing-specifications-of-combinational-circuits)
      - [Propagation Delay of Combinational Circuits](#propagation-delay-of-combinational-circuits)
      - [Contamination Delay of Combinational Circuits](#contamination-delay-of-combinational-circuits)
    - [Sequential Circuit](#sequential-circuit)
  - [Pipeline](#pipeline)
    - [Improve Combinational Circuit](#improve-combinational-circuit)
      - [Problem With Combinational Circuit Without Pipeline](#problem-with-combinational-circuit-without-pipeline)
      - [Goal](#goal)
      - [Measurement of System Performance](#measurement-of-system-performance)
    - [Solution - Pipeline](#solution---pipeline)
      - [Definition](#definition-1)
      - [Latency \& Throughput in K-Stage Pipeline](#latency--throughput-in-k-stage-pipeline)
    - [Example Pipelining Question](#example-pipelining-question)
      - [Latency and Throughput without Pipelining](#latency-and-throughput-without-pipelining)
      - [Latency with 4-Stage Pipeline](#latency-with-4-stage-pipeline)
    - [RISC Pipeline](#risc-pipeline)
      - [Von Neumann Model](#von-neumann-model)
      - [Five Stage Pipeline](#five-stage-pipeline)
      - [3-Stage Pipeline Analysis](#3-stage-pipeline-analysis)
      - [Why 5-Stage? Ideally Balanced Pipeline](#why-5-stage-ideally-balanced-pipeline)
  - [Pipeline Hazard](#pipeline-hazard)
    - [Read-After-Write Data Hazard](#read-after-write-data-hazard)
      - [Example 1](#example-1)
      - [Example 2](#example-2)
    - [Load-Use Data Hazard](#load-use-data-hazard)
      - [Example](#example)
    - [Control Hazard](#control-hazard)
      - [Example](#example-1)
    - [Other Situations and Hazards](#other-situations-and-hazards)
    - [Solution](#solution-1)
      - [Stall](#stall)
      - [Forward](#forward)
      - [Non-architecture Solution](#non-architecture-solution)
      - [Branch Delay Slot](#branch-delay-slot)
  - [Branch Prediction](#branch-prediction)
    - [Branch Predictor](#branch-predictor)
      - [Static Branch Prediction](#static-branch-prediction)
      - [Dynamic Branch Prediction](#dynamic-branch-prediction)
    - [Handle Mis-prediction](#handle-mis-prediction)
      - [Example Handle Method - Epoch Based](#example-handle-method---epoch-based)
    - [Example 1-bit Predictor](#example-1-bit-predictor)
    - [Example 2-bit Predictor](#example-2-bit-predictor)
    - [Other Improvements](#other-improvements)
      - [Branchless Programming](#branchless-programming)
      - [Compiler Loop Unrolling](#compiler-loop-unrolling)
  - [Superscale](#superscale)
  - [Memory System and Cache](#memory-system-and-cache)
    - [Motivation](#motivation-1)
    - [SRAM \& DRAM](#sram--dram)
      - [SRAM](#sram)
      - [DRAM](#dram)
    - [Cache](#cache)
      - [Multi-Layer Cache Architecture](#multi-layer-cache-architecture)
    - [Cache Operation](#cache-operation)
      - [Basic Unit of Cache Operation](#basic-unit-of-cache-operation)
      - [Fetch Data to Cache](#fetch-data-to-cache)
      - [Access Data](#access-data)
    - [Cache Miss](#cache-miss)
      - [Compulsory Misses](#compulsory-misses)
      - [Capacity Misses](#capacity-misses)
      - [Conflic Misses](#conflic-misses)
    - [Cache Schemes](#cache-schemes)
      - [Direct Mapped Cache](#direct-mapped-cache)
        - [Why use lower bits?](#why-use-lower-bits)
        - [How do we know block in cache?](#how-do-we-know-block-in-cache)
        - [How to load a multi-byte block?](#how-to-load-a-multi-byte-block)
      - [Fully Associative](#fully-associative)
      - [N-way Set Associative](#n-way-set-associative)
    - [Cache Replacement Policies](#cache-replacement-policies)
      - [Idea](#idea)
      - [LRU](#lru)
    - [CPI of Memory Access with Cache](#cpi-of-memory-access-with-cache)
    - [Cache Coherency](#cache-coherency)
    - [Cache Prefetching](#cache-prefetching)
      - [Hardware Prefetching](#hardware-prefetching)
      - [Software Prefetching](#software-prefetching)
    - [Cache and OOP](#cache-and-oop)
      - [OOP Friendly](#oop-friendly)
      - [OOP Unfriendly](#oop-unfriendly)

# CS250P Computer System Architecture Part I
## Grading
1. Homework 50%
2. Mid term 25%
3. Final 25%
## Motivation
```
Moore's Law
The number of transistors on an integrated circuit will double every two years.

   +

Dennard Scaling
As transistors get smaller, their power density stays constant.
Length▼ Voltage▼ Current▼

   │
   ▼

The tech journalists' narrative:
"Hardware performace doubles each year."
```
### End of Moore's Law
Due to physical limitations and rising costs, the transistors can't be smaller.
### End of Dennard Scaling
$$
power \propto leakage_{(static)} + \alpha * {CFV^2}_{(dynamic)}\\ 
\alpha = constant\\ 
C = Capacitance\\ 
F = Frequency\\ 
V = Voltage\\ 
$$
> $\propto$: proportional to 

Idealy, as the size of transistor shrinks, voltage was reduced. So we can affort to operate the chip at higher frequency at the same power.  
However leakage power (static baseline power) is proportional to ${1}\over{voltage}$.  
Therefore power density of chip is increased as transistors get smaller.
### Solution
1. Multicore + Multithread - has limitations too!
2. Larger Chip - M1 Chip
3. Task specific chips - i.e. video encode/decode 

## Hardware - Software Interface
### Concept of Abstraction
Hide low level detail to deal with more complicated stuff.  
Examples:
1. API - Application Programming Interface
2. System Calls
3. ABI - Application Binary Interface
4. **ISA** - Instruction Set Architecture

### ISA - Instruction Set Architecture
#### Definition  
The abstraction between software and hardware (Hardware/Software Interface).  
#### Where is ISA
```
High-level Language        a = a + 1

     │
     │  compiler
     ▼

Assembly Language          add x6,1,x6

     │
     │  assembler
     ▼

Hardware Representation    000101011 <-ISA-> Hardware
```
#### Types of ISA
1. RISC - Reduceed Instruction Set Computer
2. CISC - Complex Instruction Set Computer  

### Performance Measurements
Define $\text{Performance} = \frac{1}{\text{Execution Time}}$, the measurements of performance is corelated to the measurements of execution time. We will ignore I/O time, idle time and focus on **CPU time**.  
#### CPU Clock
The constant-rate clock governing digital hardwares.
* Clock Cycle Time(Clock Period): Duration of one clock cycle. Unit nanoseconds. 
* Clock Frequency(Clock Rate): Cycles per second. Unit Giga Hertz.
$$\text{Period} = \frac{1}{\text{Frequency}}$$
#### CPU Time
$$\text{CPU Time} = \text{\#Cycles} \times \text{Period} = \frac{\text{\#Cycles}}{\text{Frequency}} $$
To improve CPU time (performance)
1. Reduce number of cycles
2. Reduce cycle time by increasing frequency
#### Instruction Count
Total number of instructions of a program, determined by program, ISA and compiler.
#### Cycle per Instruction - CPI
Number of clock cycle per instruction is determined by CPU hardware and the type of instruction. For RISC CPI is constant and for CISC we are talking about **average** CPI.  
$$\text{\#Cycles} = \text{\#Instruction} \times \text{Cycle per Instruction}$$
#### Conclusion
$$\text{CPU Time} = \frac{\text{\#Instruction} \times \text{CPI}}{\text{Frequency}} $$
Factors that influence performance:
1. Algorithm: instruction count
2. Programming Language: instruction count
3. Compiler: instruction count & CPI
4. Instruction Set Architecture: instruction count & CPI & clock speed  

To improve CPU time, as the measurement of performance, the ISA design needs to feature:
1. Low instruction count
2. Low CPI
3. High frequency (clock speed)

## ISA Classification
### RISC - Reduced Instruction Set Computer
* Small number of general instructions
* Computation performed in register
* Memory acceess is different instructions
* Fixed length instruction encoding
* Complex instruction was composed of general instructions  

Examples: RISC-V, ARM(Advanced RISC Machine)
### CISC - Complex Instruction Set Computer
* Large number of complex instructions
* Various memory and register modes per instruction
* Varible length instruction encoding  

Examples: Intel x86

## RISC-V
[RISC-V](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec3%20-%20RISC-V,%20x86%20Assembly.pdf)
## x86
[x86](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec3%20-%20RISC-V,%20x86%20Assembly.pdf)
## RISC-V Assembly & x86 Assembly
[ISA Encoding Comparison(Red Commented Part)](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec3.5%20-%20RISC-V,%20x86%20Assembly%20Encoding.pdf)

## Digital Circuits
### Why Digital Over Analog
#### Disadvantage of Analog Computer
Analog computers are susceptible to noise, distortion, and interference. Noise is accumulated at each component.  
#### Advantage of Digital Computer
1. Noise is cancelled at each digital component, as each digital component can generate a new & cleaner signal.
2. Complex designs can be achieved on the abstraction of digital behavior.


### Types of Digital Circuits
1. Combinational - output is function of current input
2. Sequential - output depends on the sequence of past inputs

### Combinational Circuit
Components:
1. Input
2. Output
3. Function Specifications
4. Timing Specifications

#### Timing Specifications of Combinational Circuits
1. Propagation Delay $t_{PD}$    
   - The **maximum** time delay from **valid** input to **valid** output.  
   - Restrict of how fast an input can be comsumed. The input signal must be held long enough for generating an valid output.
2. Contamination Delay $t_{CD}$  
   - The **minimum** time delay from when input **starts** to change to output **starts** to change.  
   - Within contamination delay time, change to input will not affect output signal.  

#### Propagation Delay of Combinational Circuits
Overall delay of a circuit is determined by **critical path**, which is the longest possible path of a circuit. Longer delay will limit the clock speed (longer period & lower frequency).
$$\text{Overall } t_{PD} = \sum_{i=1}^{n} t_{PD_i} \text{  for each component in critical path}$$
#### Contamination Delay of Combinational Circuits
Determined by shortest path in a circuit.
### Sequential Circuit
Rather trivial.

## Pipeline
### Improve Combinational Circuit
#### Problem With Combinational Circuit Without Pipeline
Complex Logic ─► Long Critical Path ─► High Propagation Delay ─► Reduced Clock Speed  
Inputs and outputs of each gate component have to be held until the final output is stable.
#### Goal
Run complex processor at higher clock speed, and achieve higher performance.

#### Measurement of System Performance
1. Latency - The time delay between an entered input and its associated output.
2. Throughtput - The rate at which input or output is processed.  

### Solution - Pipeline
#### Definition
1. **K-Stage pipeline** is an acyclic circuit having exactly k **registers** on **every** input/ouput path.  
2. Each pipeline stage needs a register on the output.  
3. The clock period $t_{CLK}$ only needs to cover the **longest** propagation time from previous stage register to the next stage register.
#### Latency & Throughput in K-Stage Pipeline
1. $\text{Latency} = K \times t_{CLK}$
2. $\text{Throughtput} = \frac{1}{t_{CLK}}$  
> #### Understand the Advantage of Pipeline
> The clock period only needs to cover the propagation delay between two registers from two adjacent stages, instead of the entire critical path. Therefore, we can shorten the clock period (higher clock rate), which increases throughput at cost of latency (not by much).

> [Pipelining Methodology Page 10](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec5%20-%20The%20processor.pdf)  
> [Number of Stages Balancing Between L and T Page 11](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec5%20-%20The%20processor.pdf)  
> [IMPORTANT Exam Question Page 13](https://www.ics.uci.edu/~swjun/courses/2022F-CS250P/materials/lec5%20-%20The%20processor.pdf)  

### Example Pipelining Question
Each module in the diagram is labeled with its latency.  
Request: Pipe this circuit to maximize throught put and minimize latency.
```
     ┌─┐    ┌─┐    ┌─┐    ┌─┐    ┌─┐
────►│2├───►│3├───►│4├───►│2├───►│1├───►
     └┬┘    └─┘    └─┘    └─┘    └─┘
      │             ▲
      │     ┌─┐     │
      └────►│4├─────┘
            └─┘
```

#### Latency and Throughput without Pipelining
0-Stage or 1-Stage pipeline, the length of critical path is going down at first branch.
$$t_{PD} = 13$$
$$\text{Throughput} = \frac{1}{13}$$
$$\text{Latency} = 13$$
#### Latency with 4-Stage Pipeline
How do we come to the pipeline staging design? By instinction?
```
         1      2      3             4

         │      │      │             │
     ┌─┐ │  ┌─┐ │  ┌─┐ │  ┌─┐    ┌─┐ │
────►│2├─┼─►│3├─┼─►│4├─┼─►│2├───►│1├─┼─►
     └┬┘ │  └─┘ │  └─┘ │  └─┘    └─┘ │
      │  │      │   ▲  │             │
      │  │  ┌─┐ │   │  │             │
      └──┼─►│4├─┼───┘  │             │
         │  └─┘ │      │             │
         │      │      │             │
```
The longest register to register propagation delay is 4 time unit.
$$t_{CLK} = 4$$
$$\text{Throughput} = \frac{1}{t_{CLK}} = \frac{1}{4}$$
$$\text{Latency} = K\times t_{CLK} = 4\times 4 = 16$$  
### RISC Pipeline
#### Von Neumann Model
**Data** and **instruction** stored in the same main memory. Treating programs as data.  
**CPU** fetches, interprets, and executes intructions from **memory**.
#### Five Stage Pipeline
```
   ┌───────┐    ┌────────┐   ┌─────────┐   ┌────────┐   ┌────────────┐
   │       │    │        │   │         │   │        │   │            │
┌─►│ Fetch ├───►│ Decode ├──►│ Execute ├──►│ Memory ├──►│ Write Back ├─┐
│  │       │    │        │   │         │   │        │   │            │ │
│  └───────┘    └────────┘   └─────────┘   └────────┘   └────────────┘ │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```
1. Fetch - Get instruction
2. Decode - Instruction decode & register read
3. Execute - Execute operation or calculate address
4. Memory Access - Request memory read or write
5. Write Back - Write execution result or memeory access result back to register  
> Assuming every stage takes a single clock cycle for simplicity's sake.


#### 3-Stage Pipeline Analysis
Memeory is not part of combinational circuit, memory accesses should be separate stages. 3-Stage is the most basic staging.  
1. Fetch - Fetch instruction from memory
2. Execute - Decode, Execute(ALU), Register File Access, Memory **Request**
3. Write Back - Memory Read (Response to Request)

The second stage is disproportionately long. The clock period needs to be long enough to cover the propagation delay of second stage. Some CPU time in first and third stage is idle.  
```
          ┌───┐----┌───────┬───┐----┐
instr. 1  │ F │    │  Exe  │ W │    |
          └───┘----└───────┴───┘----┘
                   ┌───┐----┌───────┬───┐----┐
instr. 2           │ F │    │  Exe  │ W │    |
                   └───┘----└───────┴───┘----┘
```
#### Why 5-Stage? Ideally Balanced Pipeline
```
           ┌─────┬─────┬─────┬─────┬─────┐
instr. 1   │ Fet │ Dcd │ Exe │ Mem │ Wrt │
           └─────┴─────┴─────┴─────┴─────┘
                 ┌─────┬─────┬─────┬─────┬─────┐
instr. 2         │ Fet │ Dcd │ Exe │ Mem │ Wrt │
                 └─────┴─────┴─────┴─────┴─────┘
                       ┌─────┬─────┬─────┬─────┬─────┐
instr. 3               │ Fet │ Dcd │ Exe │ Mem │ Wrt │
                       └─────┴─────┴─────┴─────┴─────┘
```
Every stage have similar propagation delay and CPU is kept busy at each clock period.

## Pipeline Hazard
### Read-After-Write Data Hazard
When the following instruction depends on register yet to be updated by previous instruction.  

Register can be read in:  
Decode Stage - Register read

Register can be written in:  
Write Back Stage - Result write back to register

#### Example 1
```
instruction 1: add s0, s1, s2   <- write to s0 at write back stage
instruction 2: add s4, s0, s3   <- read s0 at decode stage
```
> add vs addi:  
> add - two registers and stores the result in a register  
> addi - add the register to an immediate value, store result in register


Instruction 2 reads 3 cycle to early.
```
           ┌──────┐
cycle 1    │ Fet1 │
           └──────┘
           ┌──────┬──────┐
cycle 2    │ Fet2 │ Dcd1 │
           └──────┴──────┘
                  ┌──────┬──────┐
cycle 3           │ Dcd2 │ Exe1 │
                  └──────┴──────┘
   .                 ▲
   .                 │
   .               read
                    r0                 ┌──────┐
cycle 5                                │ Wrt1 │
                                       └──────┘
                                          ▲
                                          │
                                        write
                                         r0
```
r0 is correct at cycle 4, the cycle after instruction 1 execution stage.
#### Example 2
```
instruction 1: addi s0, zero, 1   <- write to s0 at write back stage
instruction 2: addi s1, s0, 0   <- read s0 at decode stage
```
Instruction 2 reads 3 cycle to early.
```
           ┌──────┐
cycle 1    │ Fet1 │
           └──────┘
           ┌──────┬──────┐
cycle 2    │ Fet2 │ Dcd1 │
           └──────┴──────┘
                  ┌──────┬──────┐
cycle 3           │ Dcd2 │ Exe1 │
                  └──────┴──────┘
   .                 ▲
   .                 │
   .               read
                    r0                 ┌──────┐
cycle 5                                │ Wrt1 │
                                       └──────┘
                                          ▲
                                          │
                                        write
                                         r0
```
r0 is correct in cycle 6, the cycle after instruction 1 write back stage.
### Load-Use Data Hazard
Data loaded by a **load instruction** yet available by the following instruction. Only solution is to stall.  
#### Example
```
instruction 1: lw s0, o(s2)     <- load word to s0, write back stage
instruction 2: addi s1, s0, 1   <- use data from s0, decode stage
```
Similar to [RAW hazard example 2](#example-2).
```
           ┌──────┐
cycle 1    │ Fet1 │
           └──────┘
           ┌──────┬──────┐
cycle 2    │ Fet2 │ Dcd1 │
           └──────┴──────┘
                  ┌──────┬──────┐
cycle 3           │ Dcd2 │ Exe1 │
                  └──────┴──────┘
   .                 ▲
   .                 │
   .               read
                    r0                 ┌──────┐
cycle 5                                │ Wrt1 │
                                       └──────┘
                                          ▲
                                          │
                                        load
                                         r0
```
### Control Hazard
Which instruction to fetch next depends on the previous execution result. Incorrect **branch prediction**.
#### Example
```
instruction 1: beq s0, zero, elsewhere  <- get next inst addr, execution stage
instruction 2: addi s1, s0, 1           <- next instruction if no branch
```
```
           ┌──────┐
cycle 1    │ Fet1 │
           └──────┘
           ┌──────┬──────┐
cycle 2    │ Fet2 │ Dcd1 │
           └──────┴──────┘
              ▲
              │
      which instruction? 
```
> BEQ Instruction:  
> Jump to elsewhere if s0 == zero, else execute next instruction in line.
### Other Situations and Hazards
1. RAW - Hazard
2. WAW - No Hazard
3. WAR - No Hazard
4. RAR - No Hazard
### Solution
#### Stall
Stall the next instruction until the depended data is updated. Stalling will result in some components at stalled cycles not doing anything, **Pipeline Bubbles**.
#### Forward
Forward **execution stage** result (of previous instruction) to the *corresponding stages* (of following instrucion). Also known as bypassing.  
> Corresponding Stage of Each Hazard:  
> 1. RAW: forward to decode stage
> 2. Control: forward to fetch stage
> 3. Load-Use: result materialized only after write back stage, forwarding won't work

Forwarding may still cause stalling in *deeper pipeline*, if the execution stage takes multiple cycles.
> Deeper Pipeline:  
> Pipeline scheme with more stages
#### Non-architecture Solution
Code scheduling done with **best effort** by compiler. Reorder the register to avoid hazards.
#### Branch Delay Slot
Try fetch another useful instruction in the next cycle following a branch instruction. Not working great IRL.

## Branch Prediction
Brach prediction is one of the countmesures of control hazard. 
### Branch Predictor
#### Static Branch Prediction
Make fixed predicition.  
Example:  
1. Take backward branch
2. Not take forward branch
#### Dynamic Branch Prediction
Predict future branch at run-time based on prediction history.

### Handle Mis-prediction
Nullify all mis-predicted previous stages. 
#### Example Handle Method - Epoch Based
1. All fetched instruction belong to ane **Epoch** number
2. Instruction retains epoch number throught the pipeline
3. In case of mispredictions, increase global epoch number by one
4. Ignore all instruction with older epoch number arrived at execution stage
### Example 1-bit Predictor
1-bit brach history table.
```
0 not taken
1 taken
```
```
              T
           ┌───┐
       T   │   │
   ┌─┬───►┌┴┐  │
┌─►│0│    │1│◄─┘
│  └┬┘◄───┴─┘
│   │   NT
└───┘
 NT
```
### Example 2-bit Predictor
2-bit branch history table.
```
00 strongly not taken
01 weakly not taken
10 weakly taken
11 strongly taken
```
```
                           T
                          ┌───┐
       T      T      T    │   │
   ┌──┬──►┌──┬──►┌──┬──►┌─┴┐  │
┌─►│00│   │01│   │10│   │11│◄─┘
│  └┬─┘◄──┴──┘◄──┴──┘◄──┴──┘
│   │   NT     NT     NT
└───┘
 NT
```
Question type: given an sequence of Ts, Ns, and initial predictor value, find the mispredictions.
### Other Improvements
#### Branchless Programming
#### Compiler Loop Unrolling

## Superscale
Idealy pipelined processor can handle one instruction per cycle. 1 IPC, 1 CPI.  
Superscaler's goal is to process multiple instructions per cycle, which requires multiple pipeline hardware instances. N-way superscaler processor handles N instructions per cycle. N IPC, $\frac{1}{\text{N}}$ CPI.
> Ideal is nice, but in reality the design is complicated and performs badly if program has many hazards, or has short-distance dependencies.  


## Memory System and Cache
### Motivation
CPU fast Memory slow.
### SRAM & DRAM
#### SRAM
Static Random Access Memory. Used for register files and caches.
1. Expensive 
2. Fast
4. Transistor
> Large SRAM subjects to propagation delay, which not only drives up cost but also slows down the speed.

#### DRAM
Dynamic Random Access Memory. Used for main memory.
1. Cheap
2. Slow
3. Capacitor, needs refreshing
> Can afford to make large DRAM.

### Cache
Cache hierarchy sets between processor and main memory. It abstracts the memory as single countinuous address space and speeds up data operations.
#### Multi-Layer Cache Architecture
```
Level    Size     Latency
─────────────────────────
L1       64KB     <5  
L2       256KB    <20 
L3       ~2MB     <50 
DRAM     ~GBs     Slow AF
```
```
┌─────────────────────────────────┐
│ ┌─────────────┐ ┌─────────────┐ │
│ │ ┌─────────┐ │ │ ┌─────────┐ │ │
│ │ │  Core1  │ │ │ │  Core2  │ │ │
│ │ └─────────┘ │ │ └─────────┘ │ │
│ │ ┌───┐ ┌───┐ │ │ ┌───┐ ┌───┐ │ │
│ │ │L1i│ │L1d│ │ │ │L1i│ │L1d│ │ │
│ │ └───┘ └───┘ │ │ └───┘ └───┘ │ │
│ │ ┌─────────┐ │ │ ┌─────────┐ │ │
│ │ │   L2    │ │ │ │   L2    │ │ │
│ │ └─────────┘ │ │ └─────────┘ │ │
│ └─────────────┘ └─────────────┘ │
│   ┌─────────────────────────┐   │
│   │           L3            │   │
│   └─────────────────────────┘   │
└─────────────────────────────────┘
```
### Cache Operation
#### Basic Unit of Cache Operation
Block or Cache line, multi-word data.
#### Fetch Data to Cache
Prefetch data might be used in the future to fastest level of cache.  
Two phenomena we can use to our advantage:  
- Temporal Locality  

  If a address location has been accessed recently, it's likely to be **accessed again** soon.  
  Methond: Cache recently accessed address. 
- Spatial Locality  

  If a address location has been accessed recently, its **nearby locations** will be accessed soon.  
  Method: Pre-fetch predicted future data.
#### Access Data
Try find data in the highest cache level. If misses try block data from subsequent lower (and slower) level, time taken was called cache miss penalty. 

### Cache Miss
#### Compulsory Misses
Initial access of a block.
#### Capacity Misses
Replaced a block due to limited cache size, which is later accessed.
#### Conflic Misses
Several blocks mapped to the same cache set.

### Cache Schemes
#### Direct Mapped Cache
Use the lower bits of block address as cache address. Each block in main memory mapped to **one** location in cache.
##### Why use lower bits?  
Allow consecutive memeory location to coexist in cache, take advantage of spacial locality.  
$$\text{Cache\_Addr} = \text{Memory\_Addr}\ mod\ \text{Cache\_Size}$$
##### How do we know block in cache?
Use the high-order bits as **Tag**, mapped to **Valid Bit**, indicating the presence of block.
##### How to load a multi-byte block?
If cache line size is n bytes, used the lowest n address bit as **Byte Offset Bits**. 

#### Fully Associative 
Any memory address can be mapped to any cache location. No conflict misses, but large management overhead.

#### N-way Set Associative
In an effort to reduce conflict misses, design a cache system using multiply parallel Direct Map Caches.  
\#Row = \#Set  
\#Column = \#Way = Set Size  
Each address can be mapped to any *way* of the specific *set*. Fixed row, any column.
$$\text{Cache\_Index} = \text{Memory\_Addr}\ mod\ (\frac{\text{Cache\_Size}}{\text{\#Ways}})$$

### Cache Replacement Policies
#### Idea
Evict the line accessed furthest in the **future**. Predict future use by looking at the past.
#### LRU
Least recently used. Replace the line accessed furthest in the **past**. Given the temporal locality of programs, this works pretty well.
> Limitation of LRU:  
> Working memory space larger than cache size, every cache access is miss.  

### CPI of Memory Access with Cache
$$CPI = \text{L1} + \text{L1 Miss Rate}*\text{L2} + \text{L2 Miss Rate}*\text{Main Memory} $$  
> The cache access time is added to the overall time, regardless of miss or hit.

### Cache Coherency
The read to each address must return the most recent value. All writes must be visible at **some point** to ensure correct read. When a core writes a **cache line**, all other instances needs to be invalidated and updated.
> Coherency: logically correct and consistent.  
> When to update write is defined by Cache Coherency Protocals.  

### Cache Prefetching
CPU speculatively prefetch cache lines for potential future uses. 
#### Hardware Prefetching
Take advantage of runtime information.
1. Sequential Prefetch - adjacent cache lines
2. Strided Prefetch - distant cache lines 
#### Software Prefetching
Take advantage of compile time information.

### Cache and OOP
Object oriented programming collects entity data in a class/structure, which are located together in the memory
#### OOP Friendly 
All instance variables are accessed when an instance is accessed.
#### OOP Unfriendly
Access small number of instance variables per instance accesse.