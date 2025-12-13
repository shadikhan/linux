#!/usr/bin/env python3

'''
- Write the output of `df -h` into a log file (output.log)
- Walk through a file tree
- For each file, log the | filename | file size | line number | line that contains [Error]



Structure:

logs/
    - 2025-12-10/
        - 2025-12-10T00:00:00Z.log
        - 2025-12-10T01:00:00Z.log
logs.py
errors.log

(Automate below):
    - Remove top level logs: rm *.log
    - Remove logs: rm -r  logs/*

Usage: ./log-aggregator.py ./logs/


'''
from datetime import datetime, timezone
from pathlib import Path

import json
import random
import time
import subprocess
import sys


MESSAGES = [
    "DEBUG: Worker 3 picked up job 128",
    "INFO: Service heartbeat",
    "ERROR: Unhandled exception in scheduler",
    "WARNING: CPU throttling detected",
]


def record_stats(logs_path):
    with open('stats.log', 'a') as f:
        result = subprocess.run(['du', '-h', logs_path], capture_output = True, text = True)
        f.write(result.stdout + '\n')

def parse_logs(logs_path: str, processed_files: list[str]) -> None:
    with open('errors.log', 'a') as f:
        for path in Path(logs_path).rglob("*"):
            if path.is_file() and ".log" in path.name:
                log_file = path.name

                with open(path.absolute(), 'r') as flog:

                    if log_file in processed_files:
                        continue
                    
                    processed_files.append(log_file)

                    for entry in flog:
                        if 'ERROR' in entry:
                            f.write(f'{log_file}: {entry}')


def write_logs(logs_path: str) -> None:
    now = datetime.now(timezone.utc).isoformat()
    now_second = now.split('.')[0]
    now_minute = now_second[:now_second.rindex(':')]

    minute_dir = Path(f'{logs_path}/{now_minute}')
    minute_dir.mkdir(parents = True, exist_ok = True)

    entries = MESSAGES[:]
    random.shuffle(entries)

    log_file = f'{minute_dir.absolute()}/{now_second}.log'
    print(log_file)

    with open(log_file, 'a') as f:
        for entry in entries:
            f.write(f'{now} {entry}\n')

def main(logs_path : str) -> None:
    processed_files = []

    while True:
        try:
            with open('processed_files.json', 'r') as f:
                processed_files = json.load(f)
        except FileNotFoundError:
            processed_files = []

        write_logs(logs_path)
        time.sleep(5)
        write_logs(logs_path)
        
        record_stats(logs_path)
        parse_logs(logs_path, processed_files)

        with open('processed_files.json', 'w') as f:
            print(processed_files)
            json.dump(processed_files, f)

if __name__ == "__main__":
    logs_path = Path(sys.argv[1]).absolute()
    main(logs_path)


