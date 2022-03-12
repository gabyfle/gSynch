# File : git.py
# Created by gabys
# Date : 05/04/2020
# License : Apache 2.0

import git
from git import GitCommandError


class Git:
    repository: git.Repo

    def __init__(self, repo_path: str):
        self.repository = git.Repo(repo_path)

    @staticmethod
    def clone(link: str, path: str, branch: str = "master") -> bool:
        """
        Clone a repository from link and put it in path
        Args:
            branch: the branch to clone (default = master)
            link: the repository to clone
            path: the path in which the repository will be cloned

        Returns:
            bool: Whether or not the cloning has been done successfully
        """
        try:
            git.Repo.clone_from(link, path, branch=branch)
        except GitCommandError as e:
            print(f"An error occurred while trying to clone {link}. Error: {e}")
            raise e

        return True

    def get_last_update(self):
        """
        Get the latest commit time
        Returns:
            int: Last commit datetime since EPOCH
        """
        head = self.repository.head.commit

        return head.committed_datetime
