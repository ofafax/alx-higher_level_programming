#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    answer = 0
    for arg in sys.argv[1:]:
        answer += int(arg)

        print(answer)
