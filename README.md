# tcp-port-scanner
A fast multi-threaded TCP port scanner written in Python

# Python Port Scanner(TCP)

A fast, multithreaded TCP port scanner built with Python. Supports custom port ranges, thread control, and verbosity for professional use in ethical hacking and CTFs.

##Features
- Multi-threaded for speed
- Port range support (e.g. 1-65535)
- Service detection (`getservbyport`)
- Verbose output for debugging

## Usage

## bash
python3 scanner.py <target> -p <port-range> -t <threads> -v


## Example
python3 scanner.py scanme.nmap.org -p 1-1024 -t 200 -v
