import os

def add_files_to_list(suffix, path, output_list):
    if not os.path.isdir(path):
        print("Invalid input: expecting path to be a directory.")
        return

    sub_dirs = os.listdir(path)
    for el in sub_dirs:
        new_path = os.path.join(path, el)
        if os.path.isfile(new_path) and el.endswith(suffix):
            output_list.append(new_path)
        elif os.path.isdir(new_path):
            add_files_to_list(suffix, new_path, output_list)

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    out = []
    add_files_to_list(suffix, path, out)
    return out


# Test 1
print("Test 1\n")
testdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testdir")
cfiles = find_files(".c", testdir)
for el in cfiles:
    print(el)
# Expected output:
# /path/to/testdir/subdir1/a.c
# /path/to/testdir/t1.c
# /path/to/testdir/subdir3/subsubdir1/b.c
# /path/to/testdir/subdir5/a.c

# Test 2
print("\nTest 2\n")
hfiles = find_files(".h", testdir)
for el in hfiles:
    print(el)
# Expected output:
# /path/to/testdir/t1.h
# /path/to/testdir/subdir1/a.h
# /path/to/testdir/subdir3/subsubdir1/b.h
# /path/to/testdir/subdir5/a.h

# Test 3
print("\nTest 3\n")
xfiles = find_files(".x", testdir)
for el in xfiles:
    print(el)
# Expected output: Nothing, because there are no files ending with ".x"

# Test 4
print("\nTest 4\n")
files = find_files("", testdir)
for el in files:
    print(el)
# Expected output: All files beneath the path, since empty string is a suffix of all files
