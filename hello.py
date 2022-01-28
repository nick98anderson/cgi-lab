#!/usr/bin/env python3
import json
import os 


#print("Content-type: application/json")
#print()
#print(json.dumps(dict(os.environ), indent=2))

browser = os.getenv("HTTP_USER_AGENT")

print("Content-type text/html")
print()
print(f"<p>HTTP_USER_AGENT={browser}</p>")






