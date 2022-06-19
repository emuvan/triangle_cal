from calculation import Result

"""
    the user is being asking to type in the the name of the data file and if they have enter 'exit' then it will terminate the program entire
   It is using the if statements and if they have enter the right name of the data document from the directory will start the class result process method from the calculation.py file
    or 
"""

def main():
    print("\n")
    print("Enter 'EXIT' to close program")
    file = input("Enter file name: ") + ".csv".lower()
    print("\n")
    if file == "exit.csv" or file == "Exit.csv":
        exit()
    else:
        Result(file)
        main()
 

"""
this is the main method of the program execution starts. 
much like in C# with the     static public void Main(String[] args)
and it calling out def main() functions
"""

if __name__ == "__main__":
    main()
