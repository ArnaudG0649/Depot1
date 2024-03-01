#!/bin/env python3

import sys, re, collections, encodings

if len(sys.argv)!=2:
  print(f"usage: {sys.argv[0]} regex")
  exit(1)

regex = re.compile(sys.argv[1])
for (k,v) in encodings.aliases.aliases.items():
  if regex.search(k) :
    print(f"{k:20} alias de {v}")

h = collections.defaultdict(list)
for (k,v) in encodings.aliases.aliases.items():
  if regex.search(k) :
    h[v].append(k)

for k,v in h.items():
  print(f"{k:20} canonique pour {v}")


# for (k,v) in encodings.aliases.aliases.items(): 
#     print(k,v)