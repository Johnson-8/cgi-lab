#!/usr/bin/env python3
import sys
import os

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")