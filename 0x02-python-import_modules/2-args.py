#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argueNUms = len(sys.argv) - 1
    list_arg = sys.argv[1:]

    if argueNUms == 0:
        print("0 arguments.")
    else:
        if argueNUms == 1:
            arg_str = "argument:"
        else:
            arg_str = "arguments:"
        print("{} {}{}".format(argueNUms, arg_str, " " if argueNUms == 1 else ":"))
        for i, arg in enumerate(list_arg):
            print("{}: {}".format(i+1, arg))
