class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.size} {self.name}"


class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
        self.size = 0
        self.parent = None

    def add_file(self, file: File):
        self.files.append(file)
        self.increase_size(file.size)

    def add_directory(self, directory: "Directory"):
        self.directories.append(directory)
        directory.parent = self
        self.increase_size(directory.size)

    def increase_size(self, size: int):
        self.size += size
        if self.parent:
            self.parent.increase_size(size)

    def get_directory(self, name: str):
        for directory in self.directories:
            if directory.name == name:
                return directory
        raise ValueError(f"Directory {name} not found")

    def print_deep(self, indent=0):
        for file in self.files:
            print(" " * indent, "-", file)
        for directory in self.directories:
            print(" " * indent, "-", directory)
            directory.print_deep(indent + 4)

    def get_directory_by_relative_path(self, path):
        if path == "..":
            return self.parent
        elif path == ".":
            return self
        elif "/" in path:
            raise "Not supported"
        else:
            return self.get_directory(path)

    def __repr__(self):
        return f"dir {self.name}"


def build_filesystem_tree_from_lines(lines):
    if lines[0] != "$ cd /":
        raise ValueError("First line must be $ cd /")
    root = Directory("/")

    listing = False
    current_dir = root

    for line in lines[1:]:
        if line.startswith("$ cd"):
            listing = False
            path = line[5:]
            current_dir = current_dir.get_directory_by_relative_path(path)

        elif line.startswith("$ ls"):
            listing = True

        elif listing and line.startswith("dir"):
            new_dir = Directory(line[4:])
            current_dir.add_directory(new_dir)

        elif listing:
            # We know here that the line specifies a flie
            (size, name) = line.split(" ")
            new_file = File(name, int(size))
            current_dir.add_file(new_file)
        else:
            raise "Should not be reachable"

    return root


def breadth_first_traversal(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        yield node
        queue.extend(node.directories)


with open("input.txt") as fd:
    lines = fd.read().split("\n")

root = build_filesystem_tree_from_lines(lines)
traversal = [n for n in breadth_first_traversal(root)]

TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000
FREE_SPACE = TOTAL_SPACE - root.size

SPACE_TO_CLEAN = REQUIRED_SPACE - FREE_SPACE

directories = [
    d for d in traversal if isinstance(d, Directory) and d.size >= SPACE_TO_CLEAN
]
directory_to_remove = min(directories, key=lambda d: d.size)
print(directory_to_remove.size)
