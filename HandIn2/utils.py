import os

# 1
def writeFolderContent(folderPath, output):
    files = []
    for filename in os.listdir(folderPath):
        files.append(filename)

    with open(output, 'w') as f:
        for file in files:
            f.write("%s\n" % file)

# 2
def writeFolderContentRecursivly(folderPath, output):
    filePaths = []
    f= open(output,"w+")
    for root, subdirs, files in os.walk(folderPath):
        f.write('\nroot = ' + root)
    #list_file_path = os.path.join(root, 'directory-list.txt')
    for filename in files:
        file_path = os.path.join(root, filename)
        file_path = file_path.replace(root, '')
        f.write('\n\t ..' + file_path)
        filePaths.append(file_path)

# 3
def printFirstLineOfEachFilename(filename):
    with open(filename, 'r') as f:
        lines = (f.readlines())
    for l in lines:
        print(l)

# 4
def printEachEmailFilename(filename):
    with open(filename, 'r') as f:
        lines = (f.readlines())
    for l in lines:
        if '@' in l:
            print(l)

# 5
def writeHeadlinesFromMDfiles(mdList, output):
    headlines = []
    for i in range(len(mdList)):
        with open(mdList[1], 'r') as md:
            lines = md.readlines()
            for l in lines:
                if '#' in l:
                    headlines.append(l)
    with open(output, '+w') as f:
        for h in headlines:
            f.write(h)


if __name__ == '__main__':
    mdFiles = ['ListOfMDs/test1Readme.md', 'ListOfMDs/test2Readme.md']
    writeHeadlinesFromMDfiles(mdFiles, 'mdHeadlines')
    #printEachEmailFilename('handin2Contents')
    #printFirstLineOfEachFilename('handin2Contents')
    #writeFolderContentRecursivly('C:/Users/jonab/.ssh/4sem/python/', '../folderContents')
    