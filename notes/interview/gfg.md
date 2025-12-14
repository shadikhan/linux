## [Linux Interview Questions and Answer](https://www.geeksforgeeks.org/linux-unix/linux-interview-questions/)

1. **Define the basic components of Linux.**

- Kernel: Linux kernel is a core part of the operating system that works as a bridge between hardware and software.
- Shell: Shell is an interface between a kernel and a user.


2. **How do you troubleshoot network connectivity issues in Linux?**

- **Check the Internet Connectivity:** First of all, please check if the internet connection option is on and also check the cables to find if there is any issue with it.
- **Verify the Network Configuration:**
    - Please check that your network is configured correctly and the network interface has your IP address. You can check it by running the ip addr or ifconfig commands.
    - You can also run the ip route command to check if the default gateway is set properly.
    - Finally, verify the DNS server configuration in the /etc/resolv.conf file.
- **Check the Firewall:**: Sometimes, firewall rules block the internet connection for the system's security. Hence, you can run the ufw or iptables command to modify the firewall rules.
- **Network Interface**: You can restart your network interface through the ifup and ifdown commands. Once you restart the network interface, please reboot the system to make changes successful.

*Shad: Next couple of questions are surface-level, RHEL deeper dives are in other notes.*

3. **How do you troubleshoot a Linux system that cannot connect to a remote server?**
Possible troubleshooting steps include checking network connectivity using tools like 'ping', verifying firewall rules, checking DNS settings, and examining relevant log files for error messages.

4. **What steps would you take to fix a network connectivity issue in Linux?**
Steps would include checking physical connections, verifying IP configuration, checking firewall settings, ensuring DNS resolution is working, and using network troubleshooting tools like 'ping', 'traceroute', or 'tcpdump'.

5. **How do you check the system logs in Linux?**
System logs can be checked using the 'tail' or 'less' command to view the contents of log files located in the '/var/log' directory, such as 'syslog', 'messages', or 'auth.log'. Also `journalctl -xe` for systemd based systems.

6. **How would you troubleshoot a slow-performing Linux server?**
Troubleshooting steps might involve checking system resource usage with tools like 'top' or 'htop', monitoring disk I/O, analyzing network traffic, identifying memory or CPU bottlenecks, and reviewing application logs.

7. **What are common causes of a Linux system running out of disk space?**
Common causes include large log files, excessive data storage, uncontrolled growth of temporary files, improper cleanup of old files, or runaway processes generating excessive output. Also i-nodes exhaustion. Also, hard links and/or processes holding deleted files open.

8. **How can you identify and terminate a process that is using a lot of CPU in Linux?**
The 'top' or 'htop' command can display the processes using the most CPU. To terminate a process, the 'kill' command followed by the process ID (PID) can be used.

9. **How would you troubleshoot a Linux system that cannot boot up?**
Troubleshooting steps might include checking hardware connections, verifying BIOS/UEFI settings, booting into a recovery mode or live system, analyzing boot logs, and diagnosing disk or file system errors.

## [Operating System Interview Questions](https://www.geeksforgeeks.org/operating-systems/operating-systems-interview-questions/)

1. **What is virtual memory?**

![virtual memory](https://media.geeksforgeeks.org/wp-content/uploads/20251111111126366287/virtual_memory.webp)
Virtual memory creates an illusion that each user has one or more contiguous address spaces, each beginning at address zero. The sizes of such virtual address spaces are generally very high. The idea of virtual memory is to use disk space to extend the RAM. Running processes don't need to care whether the memory is from RAM or disk. The illusion of such a large amount of memory is created by subdividing the virtual memory into smaller pieces, which can be loaded into physical memory whenever they are needed by a process.

2. What is demand paging and how it works?
The process of loading the page into memory on demand (whenever a page fault occurs) is known as demand paging.

Working of Demand paging:

- Process: Only the required memory pages of a process are loaded into RAM when needed, not the entire process.
- Page Table: Keeps track of which pages are in memory and which are on disk.
- Page Fault: Occurs when a referenced page is not in RAM, the OS loads it from secondary storage.
- Loading: The missing page is brought into an empty frame in memory, and the page table is updated.
- Execution Resumes: After the page is loaded, the process continues execution from where it was interrupted.

3. **What is fragmentation?**
![fragmentation](https://media.geeksforgeeks.org/wp-content/uploads/20251110180834475063/internal_fragmentation.webp)
Processes are stored and removed from memory, which makes free memory space, which is too little to even consider utilizing by different processes.  Suppose, that process is not ready to dispense to memory blocks since its little size and memory hinder consistently staying unused is called fragmentation. This kind of issue occurs during a dynamic memory allotment framework when free blocks are small, so it can't satisfy any request.

4. **What is the basic function of paging?**
Paging is a method or technique which is used for non-contiguous memory allocation. It is a fixed-size partitioning theme (scheme). In paging, both main memory and secondary memory are divided into equal fixed-size partitions. Paging is a memory management technique where secondary memory is divided into pages and main memory into frames. Each process is split into fixed-size pages that are loaded into available frames in main memory. The last page may be smaller than the standard page size. This method enables efficient and flexible use of memory.

5. **How does swapping result in better memory management?**

[swapping](https://media.geeksforgeeks.org/wp-content/uploads/20251111153545783608/swapping.webp)
Swapping is a simple memory/process management technique used by the operating system(os) to increase the utilization of the processor by moving some blocked processes from the main memory to the secondary memory thus forming a queue of the temporarily suspended processes and the execution continues with the newly arrived process. During regular intervals that are set by the operating system, processes can be copied from the main memory to a backing store and then copied back later. Swapping allows more processes to be run that can fit into memory at one time.

6. **When does thrashing occur?**
Thrashing occurs when processes on the system frequently access pages, not available memory.

7. **What is the zombie process?**
A process that has finished the execution but still has an entry in the process table to report to its parent process is known as a zombie process. A child process always first becomes a zombie before being removed from the process table. The parent process reads the exit status of the child process which reaps off the child process entry from the process table.

8. **What are orphan processes?**
A process whose parent process no more exists i.e. either finished or terminated without waiting for its child process to terminate is called an orphan process.

9. **What is Context Switching?**
Switching of CPU to another process means saving the state of the old process and loading the saved state for the new process. In Context Switching the process is stored in the Process Control Block to serve the new process so that the old process can be resumed from the same part it was left.

The process control block (PCB) is a block that is used to track the process’s execution status. It contains information about the process, i.e. registers, quantum, priority, etc. The process table is an array of PCBs, that means logically contains a PCB for all of the current processes in the system.

10. **What is internal vs external fragmentation?**
- Internal Fragmentation: Inefficient use of space within allocated memory blocks. It occurs when allocated memory may have some unused space due to fixed-size allocation.
    - A book compartment can only fit a book of size A, but if a book of size B (where B < A) is placed in it, the remaining space (A - B) is wasted.
    - To fix, it's like adjusting your bookshelf compartments to better fit the sizes of your books (dynamic partitioning).
    - **Wasted space INSIDE allocated regions. Ex. `Page_Size = 4KB, Process requests 3KB, 1KB wasted inside the page`**
- External Fragmentation: Scattered, unallocated space between blocks. It occurs when free memory is divided into small blocks and cannot satisfy memory allocation requests, even if the total free memory is sufficient.
    - Imagine having several small empty spaces on your bookshelf that are too small to fit any of your books, even though the total empty space is enough for a book.
    - To fix, think of ways to reorganize your books so that they're more likely to be returned together, reducing gaps on the shelfs.
    - **Wasted space OUTSIDE allocated regions. Ex. `[used][free][used][free]`**

## [Network Fundamentals Interview Questions - Computer Networks](https://www.geeksforgeeks.org/blogs/top-50-ip-addressing-interview-questions-and-answers/#)

1. **What is the LOOPBACK address?**
Loopback Address is used to let a system send a message to itself to make sure that the TCP/IP stack is installed correctly on the machine.

2. **What is a Default Gateway?**
A Default Gateway is the device (usually a router) that connects your local network to other networks, including the internet.

When a computer in a local network wants to send data to an IP address outside its own network, it doesn’t know where to send it directly.
In this case, the data is forwarded to the default gateway, which then routes it towards the correct destination.
Example:

- Your PC’s IP: 192.168.1.10
- Your network’s default gateway: 192.168.1.1 (the router)
- If you try to access 8.8.8.8 (Google DNS), your PC sends the packet to the gateway (192.168.1.1), and the router forwards it to the internet.

3. **What is a Default Gateway?**
A Default Gateway is the device (usually a router) that connects your local network to other networks, including the internet.

When a computer in a local network wants to send data to an IP address outside its own network, it doesn’t know where to send it directly.
In this case, the data is forwarded to the default gateway, which then routes it towards the correct destination.
Example:

Your PC’s IP: 192.168.1.10
Your network’s default gateway: 192.168.1.1 (the router)
If you try to access 8.8.8.8 (Google DNS), your PC sends the packet to the gateway (192.168.1.1), and the router forwards it to the internet.

4. **What is Network Address Translation?**
- NAT allows multiple devices in a private network to access the internet using a single public IP address.
- It translates private IPs ↔ public IPs and also modifies port numbers to keep connections unique.
- The mapping of private IP/port to public IP/port is stored in a NAT table.
- NAT is usually implemented on routers or firewalls.

5. **What is the difference between TCP and UDP?**

TCP:
- Connection-oriented.
- Reliability via sequence numbers, ACKs, retransmissions.
- Provides error-checking and congestion/flow control.
- Higher overhead.

UDP:
- Connectionless, unreliable (no ACKs, retransmissions).
- Low overhead, faster delivery.
- No congestion/flow control.

Why UDP Preferred:
- Real-time apps (VoIP, gaming, streaming) value low latency over reliability.
- Minor packet loss is tolerable; retransmissions would hurt performance more than they help.

6. **What is the role of port numbers in transport layer communication and how are ephemeral ports used?**

Role of Port Numbers:
- Identify specific applications/services on a host.
- Example: HTTP -> port 80, HTTPS -> 443, DNS -> 53.
- Allow multiplexing of multiple services on the same IP.

Ephemeral Ports:
- Temporary, dynamically allocated by client OS (range: ~49152–65535).
- Used for outgoing connections.
- Each session uniquely identified by (Source IP, Source Port, Destination IP, Destination Port).
- Allow multiple simultaneous connections (e.g., opening many browser tabs).

7. **Explain how congestion control in TCP differs from flow control.**

Flow Control (Receiver-Side):
- Ensures sender doesn’t overwhelm receiver’s buffer.
- Managed using receiver window (rwnd) field in TCP header.
- Protects end-hosts.

Congestion Control (Network-Side):
- Prevents sender from flooding the network with too much traffic.
- Algorithms: Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery.
- Protects network paths.

Difference:
- Flow control = end-to-end buffer management.
- Congestion control = managing bandwidth and preventing congestion collapse.

8. **How does HTTP/2 improve upon HTTP/1.1 in terms of application layer performance?**

HTTP/1.1 Limitations:
- Head-of-line blocking (one request per connection).
- High overhead with repeated headers.
- Inefficient multiple connections per page.

HTTP/2 Improvements:
- Multiplexing: Multiple streams over a single TCP connection, removing head-of-line blocking at app layer.
- Header Compression (HPACK): Reduces repetitive header overhead.
- Server Push: Server can proactively send resources before client requests them.
- Binary Framing: More efficient parsing vs. text-based HTTP/1.
- Result: Reduced latency, faster page loads, better performance on high-latency or lossy networks.

9. **How does DNS caching work and what risks does it introduce?**

Mechanism:
- DNS responses are cached at different levels:
  - Browser cache
  - OS resolver cache
  - ISP recursive DNS server cache. This reduces query time and avoids repetitive lookups.

Risks:
- DNS cache poisoning: An attacker injects forged DNS records, redirecting users to malicious websites.
- Stale cache entries: Users may reach outdated IPs if records aren’t refreshed.
- Mitigation: DNSSEC (digital signatures), short TTL values and cache flushing.

10. **Explain how QUIC differs from TCP + TLS in terms of transport layer operations.**

Traditional TCP + TLS:
- Requires 3-way TCP handshake + TLS handshake before secure data transmission.
- Susceptible to head-of-line blocking (a lost packet delays the entire stream).

QUIC (on UDP):
- Combines transport + encryption (TLS 1.3) in a single handshake -> faster setup.
- Multiplexing streams independently avoids head-of-line blocking.
- Connection migration: QUIC identifies connections by IDs, not IP/port, so mobility (switching Wi-Fi -> 4G) is seamless.
- Note: QUIC provides faster, more reliable transport optimized for web traffic -> backbone of HTTP/3.
