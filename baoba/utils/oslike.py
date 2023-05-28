def osLike():
    os_release="/etc/os-release"
    with open(os_release, "r") as f:
        file = f.read()
        f.close()
    return file.split("\n")
