#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            if arg.isdigit():
                result += int(arg)
            else:
                print("Skipping non-integer argument: '{}'".format(arg))
    print(result)
