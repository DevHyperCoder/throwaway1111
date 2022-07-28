def copy_files(in_name,out_name):
    infile = open(in_name,"r")
    outfile = open(out_name,"w")

    outfile.write(infile.read())
    print("Successfully copied contents.")
    infile.close()
    outfile.close()

in_name = input("Enter input filename: ")
out_name = input("Enter output filename: ")
copy_files(in_name,out_name)
