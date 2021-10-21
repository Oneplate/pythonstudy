def write_to_file(filename, myname, myage, major):
    outfile = open(filename, 'w')
    outfile.write("My name is "+myname+"\n")
    outfile.write("My age is "+myage+"\n")
    outfile.write("I am majoring in "+major+"\n")
    outfile.close()

write_to_file("namefile.txt", "Jisoo Byeon", "25", "Electrical Engineering")
