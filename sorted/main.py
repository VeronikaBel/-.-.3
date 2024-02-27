with open ("1.txt", "r") as f1:
    lines1 = f1.readlines()
    num_lines1 = len(lines1)

with open ("2.txt", "r") as f2:
    lines2 = f2.readlines()
    num_lines2 = len(lines2)

if num_lines1 > num_lines2:
    fewer_file_name = "2.txt"
    more_file_name = "1.txt"
    fewer_lines = lines2
    more_lines = lines1
else:
    fewer_file_name = "1.txt"
    more_file_name = "2.txt"
    fewer_lines = lines1
    more_lines = lines2

with open ("3.txt", "w") as f3: 
    f3.write (fewer_file_name)
    f3.write (f'{num_lines1 if num_lines1 < num_lines2 else num_lines2}')
    f3.writelines (fewer_lines)
    f3.write (more_file_name)
    f3.write (f'{num_lines2 if num_lines1 < num_lines2 else num_lines1}')
    f3.writelines (more_lines)