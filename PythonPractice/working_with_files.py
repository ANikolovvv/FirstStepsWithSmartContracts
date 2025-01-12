import os

file_path ="Tasks/test.txt";
create_file_path="Tasks/output.txt";

txt_data="I like pizza!";

try:
    with open(file=create_file_path, mode="r") as file:
        content=file.read();
        print(content);
    #    file.write("\n" + txt_data);
    #    print(f"txt file '{create_file_path}' was created");
except FileExistsError:
   print("That file already exists")

if os.path.exists(file_path):
    print(f"The location {file_path} exists");
    
    if os.path.isfile(file_path):
        print("That is a file");
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist");  