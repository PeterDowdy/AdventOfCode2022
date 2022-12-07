data = []
with open("day7.txt") as f:
    data = [x.strip() for x in f.readlines()]


class DirectoryNode:
    def __init__(self, name, contents, parent):
        self.name = name
        self.contents = contents
        self.parent = parent
        self.child_size = 0


class FileNode:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


data = data[1:]

fs = DirectoryNode("/", [], None)
current = fs
while data:
    this_command = data[0]
    data = data[1:]
    if this_command[0] == "$":
        toks = this_command.split(" ")
        if toks[1] == "cd":
            if toks[2] == "..":
                current = current.parent
            else:
                for x in current.contents:
                    if x.name == toks[2]:
                        current = x
                        break
        elif toks[1] == "ls":
            while data[0][0] != "$":
                dir_content = data[0]
                dir_toks = dir_content.split(" ")
                if dir_toks[0] == "dir":
                    current.contents.append(DirectoryNode(dir_toks[1], [], current))
                else:
                    current.contents.append(
                        FileNode(dir_toks[1], int(dir_toks[0]), current)
                    )
                data = data[1:]
                if not data:
                    break

directory_sizes = []


def get_size(node):
    if isinstance(node, FileNode):
        return node.size
    else:
        total = 0
        for x in node.contents:
            total += get_size(x)
        node.child_size = total
        directory_sizes.append((node.name, node.child_size))
        return total


total_size_used = get_size(fs)

remaining = 70000000 - total_size_used

needed = 30000000 - remaining

print(sorted([x[1] for x in directory_sizes if x[1] >= needed]))
