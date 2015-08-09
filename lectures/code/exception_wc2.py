import sys

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        k = int(sys.argv[2])
        print topkwords(filename, k)
    except IOError:
        print "File does not exist"
    except (ValueError, IndexError):
        print "Error in command line input"
        print "Run as: python wc.py <filename> <k>"
        print "where <k> is an integer"
