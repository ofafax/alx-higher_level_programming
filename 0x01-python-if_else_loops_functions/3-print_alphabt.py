#!/usr/bin/python3
for aphbt in range(ord('a'), ord("z")+1):
    if chr(aphbt) not in ['q', 'e']:
        print("{0}" .format(chr(aphbt)), end='')
