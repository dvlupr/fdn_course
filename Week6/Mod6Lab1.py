import os

print(os.getcwd())
os.chdir(r"C:/users/jim/documents")
print(os.getcwd())

cnt = 0
for file in os.listdir():
    if file.endswith('.txt'):
        cnt = cnt + 1
        print(file)
print('There were {} file(s) found'.format(cnt))

cnt2 = 0
for root, dirs, files in os.walk('.', topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        cnt2 = cnt2 + 1
        print(os.path.join(root, name))
print('There were {} subdirectories found'.format(cnt2))
