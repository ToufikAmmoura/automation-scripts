import sys

def createLocalRepo():
    raise NotImplementedError()

def createGithubRepo():
    raise NotImplementedError()

def main():
    repoTitle = str(sys.argv[1])

    print(repoTitle)

main() 