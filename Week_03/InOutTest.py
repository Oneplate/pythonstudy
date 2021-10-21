def print_file(filename):
    infile = open(filename)

    for line in infile:
        print(line, end = "")
    print()
    infile.close()

def copy_file(infilename, outfilename):
    infile = open(infilename)
    outfile = open(outfilename, 'w')

    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()

print_file("HumptyDumpty.txt")

copy_file("HumptyDumpty.txt", "Copied.txt")

print_file("Copied.txt")
