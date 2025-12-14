# linux

## todos

- python: file io, main, (maybe: os stuff, threading)
- grep/awk/sed

## really nice tidbits:

- `grep -E "HEADER_PATTERN|SEARCH_PATTERN"` is a great way to find what you're looking for, and include the header line!!!
- `man` helpful scrolling tips:
    - Press `Space` to go down one page, `b` to go back one page.
    - Press `u` to go up half a page, `d` to go down half a page.
    - Press `g` to go to the beginning of the document, `G` to go to the end.
    - Press `/keyword` to search for "keyword" forward, `?keyword` to search backward.
    - Press `n` to go to the next search result, `N` to go to the previous search result.
    - Press `q` to quit.
- By the way, if we want to not see `permission denied` errors from `du`, we can redirect stderr to /dev/null as such: `du / 2>/dev/null | head`

``` bash
shad@linux:~/linux$ journalctl --help | grep -e '-x ' -e '-u ' -e '-e '
  -u --unit=UNIT             Show logs from the specified unit
  -x --catalog               Add message explanations where available
  -e --pager-end             Immediately jump to the end in the pager
```

- `command &> filename` redirects both stdout and stderr to `filename`. Musch simpler than `command > filename 2>&1`
- `wc -l < filename` is more efficient than `cat filename | wc -l` because it avoids the unnecessary use of `cat` and a pipe.

## things i wanna know

- setuid, setgid
- tmux


## The major timer-based counter tools

| Tool     | Focus area           | Typical use                              |
|----------|----------------------|------------------------------------------|
| iostat -x 1 | Block I/O devices    | Disk latency, throughput, %util               |
| pidstat 1   | Tasks (per-PID)     | CPU, memory, context switches per process  |
| mpstat 1    | CPUs / cores        | CPU usage per processor or aggregate       |
| vmstat 1    | Memory, processes, I/O | Paging, run queue, swap, I/O waits         |
| sar -n DEV 1 | Network interfaces  | RX/TX packets, throughput                 |
| sar -u 1    | CPU utilization (like mpstat) | User/system/idle breakdown              |
| sar -d 1    | Block devices (like iostat) | Disk throughput and latency                 |
