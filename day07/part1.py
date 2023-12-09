import sys
sample_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def interpret_ls(lines: list, dirlisting: dict):
    for line in lines:
        if(line.startswith('dir')):
            dirName = line.split(" ", 1)[1]
            subdir = {'name':dirName, 'files':[], 'subdirectories':[], 'parentdirectory': dirlisting}
            dirlisting['subdirectories'].append(subdir)
        elif line[0].isnumeric():
            filesize, filename = line.split(" ")
            filesize = int(filesize)
            dirlisting['files'].append({'name': filename, 'size': filesize})

def determine_next_command_line(lines: list, currentCommandLine: int):
    nextCommandLine = currentCommandLine + 1
    if nextCommandLine == len(lines):
        return -1
    while not lines[nextCommandLine].startswith("$"):
        nextCommandLine += 1
        if nextCommandLine >= len(lines):
            return -1
    return nextCommandLine

def get_dir_index(subdirectories: list, name: str):
    for i, subdirectory in enumerate(subdirectories):
        if subdirectory['name'] == name:
            return i
    return -1

def get_size_of_directory(currentDirectory: dict):
    totalSize = 0
    for file in currentDirectory['files']:
        totalSize += file['size']
    for directory in currentDirectory['subdirectories']:
        totalSize += get_size_of_directory(directory)
    return totalSize

def sum_small_directories(currentDirectory: dict, sizeThreshhold: int):
    "returns the sum of sizes of directories if they are above a threshhold"
    currentDirectorySize = get_size_of_directory(currentDirectory)
    if(currentDirectorySize >= sizeThreshhold):
        currentDirectorySize = 0
    for subdirectory in currentDirectory['subdirectories']:
        currentDirectorySize += sum_small_directories(subdirectory, sizeThreshhold)
    return currentDirectorySize


if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    rootDir = {'name':'/', 'files':[], 'subdirectories':[]}
    currentCommandLine = 1
    nextCommandLine = determine_next_command_line(lines, currentCommandLine)
    currentDirectory = rootDir
    while currentCommandLine != -1:
        currentCommand = lines[currentCommandLine]
        if currentCommand == '$ ls':
            if nextCommandLine == -1:
                outputLines = lines[currentCommandLine + 1:]
            else:
                outputLines = lines[currentCommandLine + 1: nextCommandLine]
            interpret_ls(outputLines, currentDirectory)
        elif currentCommand == "$ cd ..":
            currentDirectory = currentDirectory['parentdirectory']
        elif currentCommand.startswith('$ cd '):
            targetDirectory = currentCommand[5:]
            targetIndex = get_dir_index(currentDirectory['subdirectories'], targetDirectory)
            currentDirectory = currentDirectory['subdirectories'][targetIndex]
        else:
            print("encountered unknown command:", currentCommand)

        currentCommandLine = nextCommandLine
        nextCommandLine = determine_next_command_line(lines, currentCommandLine)
    print(sum_small_directories(rootDir, 100000))
    

