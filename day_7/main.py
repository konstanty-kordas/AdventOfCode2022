class Structure():
    def __init__(self, name: str, size: int, file: bool) -> None:
        self.children = []
        self.size = size
        self.name = name
        self.file = file

    def addChild(self, name, size, file):
        self.children.append(Structure(name, size, file))

    def getSize(self):
        if self.size is not None:
            return self.size
        s = 0
        for i in self.children:
            s += i.getSize()
        self.size = s
        return s

    def getChild(self, name):
        for i in range(len(self.children)):
            if self.children[i].name == name:
                return self.children[i]
        return None


with open('input.txt', 'r') as f:
    listing = False
    current = []
    for i in f.read().split('\n'):
        cmd = i.split()
        print(cmd)
        if cmd[0] == "$":
            listing = False
            if cmd[1] == "ls":
                listing = True
                continue
            if cmd[1] == "cd":
                if cmd[2] == '..':
                    current.pop()
                else:
                    if len(current) == 0:
                        current.append(Structure("/", None, False))
                        continue
                    current.append(current[-1].getChild(cmd[2]))
                print((current[-1].name))
        if listing:
            if cmd[0] == "dir":
                current[-1].addChild(cmd[1], None, False)
            else:
                current[-1].addChild(cmd[1], int(cmd[0]), True)
disk_size = 70000000
unused = disk_size - current[0].getSize()
print(unused)
needed = 30000000 - unused
a = 0
total = 0
sizes = []
stack = []
stack.append(current[0])
while len(stack) > 0:
    c = stack.pop()
    for i in c.children:
        if i.file==False:
            if i.size >= needed:
                print(i.size)
                sizes.append(i.size)
            stack.append(i)

print(sizes.sort())
print(sizes)
print(a)
print(total)
