import os, sys


if __name__ == "__main__":
    for dir in os.listdir(sys.argv[1]):
        print("PARSING FOLDER " + dir)
        os.system("python ecise_generator.py 'ecise' "+ 
            os.path.abspath(os.path.join(sys.argv[1], dir))+ " andromeda.pdf")
