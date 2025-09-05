#!/usr/bin/python3
if __name__ == "__main__":
    import dis
    import marshal

    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)
        code = marshal.load(f)

    names = [name for name in code.co_names if not name.startswith("__")]

    for name in sorted(names):
        print(name)
