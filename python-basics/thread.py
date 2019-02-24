"""Thread is basically a lightweight sub-process, a smallest unit of processing.

Multithreading is a process of executing multiple threads simultaneously.

Green thread: green threads are threads that are scheduled by a runtime library or virtual machine (VM) instead of natively by the underlying operating system.

The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread to hold the control of the Python interpreter. This means that only one thread can be in a state of execution at any point in time.

 GIL allows only one thread to execute at a time even in a multi-threaded architecture """