# Working with Google Cloud Source Repositories

Google has [great documentation](https://cloud.google.com/source-repositories/docs/create-code-repository) walking you through how to create a repository and then push code to it, but we also wanted to create a guide to walk you through it. This [GitHub tutorial](https://docs.github.com/en/get-started/using-git/about-git) is also a nice introduction to working with git. 

## Creating a source repository

1. Search for Source Repositories at the top of your console. Click **Source Repositories**.

<img src="/images/1_search_source.png" width="550" height="200">

2. Click **Add repository** in the upper right corner.

<img src="/images/2_create_repository.png" width="550" height="150">

3. Select *Create new repository* then click **Continue**

<img src="/images/3_new_repository.png" width="550" height="225">

4. Name your repository and enter your project name. Click **Create**.

<img src="/images/4_name_repo.png" width="550" height="300">

5. Add code following the instructions on your screen. You only get this help the first time, so for adding code in the future, use our instructions in the next section. Note that here we are using gcloud, but you can also use SSH keys and traditional git commands.

<img src="/images/5_add_code.png" width="550" height="500">

## Clone and push to a Google Cloud Source Repository

1. Open your terminal (requires Google SDK) or Cloud Shell (or a VM). Type `gcloud init`. Configure gcloud. 

2. Clone the source repository locally. 

`gcloud source repos clone <REPO_NAME> --project=<YOUR_PROJECT_NAME>`

3. CD into your repository.

`cd <REPO_NAME`

4. Add files to your local git repo. You can clone another repo, like this `git clone https://github.com/STRIDES/NIHCloudLabGCP.git or you can just add files manually to the local directory.

5. If you get an error message about git config, just follow the on screen propts to add your email and name. 

6. Now add your new directory/file to staging

`git add <DIR>`.

7. Now commit your new directory/file to the repository. You will need to add a commit message. 

`git commit -m "Add a Commit Message"` This will add all updated files (since last push) to the repository.

8. Now push the local git reposoitory to the master branch. 

`git push origin master`
