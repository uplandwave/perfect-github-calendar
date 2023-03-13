import git

# Replace these with your own values
local_directory = "/Users/lukebriggs/Documents/GitHub/perfect-github-calendar"
repo_url = "https://github.com/uplandwave/perfect-github-calendar.git"
branch_name = "main"
commit_message = "Fake news"

# Clone the repository to a local directory
repo = git.Repo.clone_from(repo_url, local_directory, branch=branch_name)

# Pull any changes from the remote repository
origin = repo.remote(name="origin")
origin.pull()

# Modify the file and push changes 15 times
for i in range(15):
    # Modify the file by appending one character to the end of the file
    with open(local_directory + "always-green.txt", "a") as file:
        file.write("a")
    
    # Stage the changes
    repo.git.add("-A")
    
    # Commit the changes with a commit message that includes the iteration number
    repo.index.commit(commit_message + "Fake News" + str(i+1))
    
    # Push the changes to the remote repository
    origin = repo.remote(name="origin")
    origin.push()