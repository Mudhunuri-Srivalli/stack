import os

print("=== FILE HANDLING PRACTICE PROGRAM ===")


# 1. Create and Write to a File

print("\n1. Creating and writing to file...")

f = open("sample.txt", "w")
f.write("Hello, this is a file.\n")
f.write("We are practicing file handling in Python.\n")
f.close()



# 2. Append to File

print("2. Appending to file...")

f = open("sample.txt", "a")
f.write("This line is added using append mode.\n")
f.close()



# 3. Read Entire File
print("\n3. Reading entire file content:")
f = open("sample.txt", "r")
print(f.read())
f.close()



# 4. Read Line by Line (readline)

print("\n4. Reading line by line using readline:")
f = open("sample.txt", "r")
print("Line 1:", f.readline(), end="")
print("Line 2:", f.readline(), end="")
f.close()


# 5. Read Lines as List (readlines)

print("\n5. Reading file as list of lines:")
f = open("sample.txt", "r")
lines = f.readlines()
print(lines)
f.close()



# 6. Using with open()

print("\n6. Using 'with' to read file:")
with open("sample.txt", "r") as f:
    for line in f:
        print(line, end="")


# 7. Check if file exists

print("\n7. Checking if file exists:")
if os.path.exists("sample.txt"):
    print("sample.txt exists!")
else:
    print("sample.txt does NOT exist!")


# 8. Renaming File

print("\n8. Renaming file to renamed_sample.txt ...")
os.rename("sample.txt", "renamed_sample.txt")
print("File renamed.")



# 9. Delete File

print("\n9. Deleting renamed_sample.txt ...")
if os.path.exists("renamed_sample.txt"):
    os.remove("renamed_sample.txt")
    print("File deleted.")
else:
    print("File not found!")



# 10. Create a Directory

print("\n10. Creating a directory named 'test_folder'...")
os.mkdir("test_folder")
print("Directory created.")



# 11. Listing Files in Current Directory

print("\n11. Listing all files and folders:")
print(os.listdir("."))



# 12. Removing a Directory

print("\n12. Removing directory 'test_folder'...")
os.rmdir("test_folder")
print("Directory removed.")



# 13. Writing Binary Data

print("\n13. Writing binary data into binary_file.bin ...")
with open("binary_file.bin", "wb") as f:
    f.write(b"\x00\x01\x02\x03\x04")
print("Binary file created.")



# 14. Reading Binary Data

print("\n14. Reading binary file:")
with open("binary_file.bin", "rb") as f:
    data = f.read()
    print("Binary data:", data)



# 15. Delete binary file

print("\n15. Deleting binary_file.bin ...")
os.remove("binary_file.bin")
print("Binary file deleted.")


print("\n=== PROGRAM FINISHED SUCCESSFULLY ===")
