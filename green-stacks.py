import os

# Path to the file to modify
file_path = 'always-green.txt'

# Function to add a character to the file
def modify_file():
    with open(file_path, 'a') as f:
        f.write('a')

# Function to commit and push changes to GitHub
def git_push():
    os.system('git add .')
    os.system('git commit -m "Fake News"')
    os.system('git push')

# Loop to modify and upload the file 15 times at 10am everyday
for i in range(15):
    modify_file()
    git_push()

