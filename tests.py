# from functions.get_files_info import get_files_info

# print("Result for current directory:")
# print(get_files_info("calculator", "."))

# print("Result for 'pkg' directory:")
# print(get_files_info("calculator", "pkg"))

# print("Result for '/bin' directory:")
# print(get_files_info("calculator", "/bin"))

# print("Result for '../' directory:")
# print(get_files_info("calculator", "../"))



#from functions.get_file_content import get_file_content

#print(get_file_content("calculator", "lorem.txt"))

# print("Results for 'main.py':")
# print(get_file_content("calculator", "main.py"))

# print("Results for 'pkg/calculator.py':")
# print(get_file_content("calculator", "pkg/calculator.py"))

# print("Results for '/bin/cat':")
# print(get_file_content("calculator", "/bin/cat"))

# print("Results for 'pkg/does_not_exist.py':")
# print(get_file_content("calculator", "pkg/does_not_exist.py"))



# from functions.write_file import write_file

# print("Test 1")
# print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

# print("Test 2")
# print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

# print("Test 3")
# print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))



from functions.run_python_file import run_python_file

def test():
    print("Test 1 (should print the calculator's usage instructions):")
    print(run_python_file("calculator", "main.py"))
                                                    
    print("Test 2 (should run the calculator... which gives a kinda nasty rendered result)")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Test 3")
    print(run_python_file("calculator", "tests.py"))

    print("Test 4 (this should return an error)")
    print(run_python_file("calculator", "../main.py"))

    print("Test 5 (this should return an error)")
    print(run_python_file("calculator", "nonexistent.py"))

if __name__ == "__main__":
    test()