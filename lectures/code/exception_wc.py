import sys

def topkwords(filename, k):
    # Returns k most common words in filename
    pass

if __name__ == "__main__":
    filename = sys.argv[1]
    k = int(sys.argv[2])
    print topkwords(filename, k)
