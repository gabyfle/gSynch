# File : __main__.py
# Created by gabys
# Date : 10/04/2020
# License : Apache 2.0

import argparse
import os
import shlex
import subprocess

from gsynch import helper
# CONFIGURATION : Configure your script here
from gsynch.api.api import Github
from gsynch.game.game import Gmod
from gsynch.git.git import Git

steam_key = ''  # Your Steam API key
github_key = '' # Your Github API key

# SUPPORTED
# Supported games
supported_games = {
    'gmod': Gmod
}

# Supported hosts
supported_hosts = {
    'github.com': Github
}


def get_arguments():
    """
    Creates a new ArgumentParser and returns the given arguments in a Namespace
    Returns:
        Namespace: arguments
    """
    parser = argparse.ArgumentParser(prog="gSynch",
                                     description="gSynch allow you to synchronise your Git code with the Steam Workshop")

    # Action group : what the user wants to do ?
    # TODO : Add a new parameter to --host to get the api key of the user
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--build', action="store", nargs=2, metavar=("<executable>", "<args>"),
                         help="Builds the workshop item with the given executable")
    actions.add_argument('--update', action="store", metavar="<item>",
                         help="Update the given workshop item to the Workshop")
    actions.add_argument('--synch', action="store", nargs=2, metavar=("<executable>", "<item>"),
                         help="Builds the workshop item with the given executable and push "
                              "it to the workshop")
    # Steam related things
    steam = parser.add_argument_group(title="Steam Workshop file and application IDs")
    steam.add_argument('--file', help="Workshop file unique identifier.", required=True)
    steam.add_argument('--app', help="Steam Application unique identifier.", required=True)

    # Git host or Git Repository
    git = parser.add_mutually_exclusive_group(required=True)
    git.add_argument("--host", action="store", nargs=2, metavar="<repository link> <api_key>", help="Link an API key "
                                                                                                    "to your repository")
    git.add_argument("--repo", action="store", help="Repository link")

    game = parser.add_mutually_exclusive_group(required=False)
    game.add_argument("--gmod", action="store_true", help="Synchronise a Garry's Mod addon")

    return parser.parse_args()


def build(executable: str, arguments: str, path: str) -> None:
    """
    Executes a build program and passing arguments to it.

    Args:
        executable: program to execute
        arguments: arguments to pass to this program
        path: path of the item to build

    Returns:
        Nothing
    """
    if not os.path.isfile(executable):
        raise Exception(f"Can't find {executable}. Be sure that the path is correct and that it's a file...")

    arguments = shlex.split(helper.replace(arguments, {'item_path': path}))
    process = subprocess.Popen(arguments)  # launch the build
    output, err = process.communicate()
    if not err:
        print(output)
    else:
        print(err)


def update(repository, steam: Steam) -> None:
    if helper.check_times(steam, repository):
        print('Everything is up to date. Your workshop file has already been synchronized with your Github repository.')
        return
    # if we're not up to date, then launch the synchronization
    #synch()

def synch() -> None:
    pass
    # TODO : Implement the synch() function


# Main function
def main():
    arguments = get_arguments()

    if arguments.build:
        build(arguments.build[0], arguments.build[1])
    elif arguments.update:
        repo = None
        if arguments.host:
            try:  # Handling host name
                repo = supported_hosts[helper.parse_host(arguments.host)](github_key, arguments.repo)
            except Exception as e:
                print(f"An internal error occurred. Error message : {e} \nHost {helper.parse_host(arguments.host)} is "
                    f"certainly not supported by gSynch.")
        elif arguments.repo:
            try:
                Git.clone(arguments.repo, 'git')

                repo = Git('git')
            except Exception as e:
                print(f'An error occurred while trying to clone your repo {arguments.repo}')
        
        steam = Steam(steam_key, arguments.app, arguments.app_id)
        update(repo, steam)
    elif arguments.synch:
        synch()

if __name__ == '__main__':
    main()
