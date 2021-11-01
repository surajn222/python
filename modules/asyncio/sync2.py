#!/usr/bin/env python3
# countasync.py

import asyncio
import time

def count():
    print("One")
    time.sleep(1)
    print("Two")

def main():
    count()
    count()
    count()

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")