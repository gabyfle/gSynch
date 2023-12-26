# gSynch
gSynch allows you to synchronise your Git repository with your Steam Workshop publication in few clicks.

## Development state : <span class="badge badge-danger" color="red !important">Unsupported, stopped</span>

This is a public archive of the gSynch project.

## Information

gSynch is entirely coded in *Python*, this mean that you have to install it before using gSynch.
#### Requirements
*  `Python 3.7` or higher **with** the following libraries :
    * `urllib.request`
    * `zipfile`
    * `requests` 
* A valid **Steam API Key** : https://steamcommunity.com/dev/apikey
* A valid **API Key** of one of the supported code hosting services :
    * **Github** : https://github.com/settings/tokens

## How to use
#### 1. Getting the App and File IDs
  ##### App ID
To get your Application ID, go to the [Steam Store](https://store.steampowered.com) and then go to your application's page.
Then, look at the URL, you should get something like this :

![appid](https://user-images.githubusercontent.com/18049206/77967797-2b234e00-72e6-11ea-9182-1c8beef5f4f0.png)

The App ID is what's circled in red.

  ##### File ID

Now that you have your App ID, you need to find your the File ID that will be used to update your Workshop Item. To get it, go to your Workshop Item page.
You should get an URL similar to this :

![fileid](https://user-images.githubusercontent.com/18049206/77968151-e0560600-72e6-11ea-8cbc-eb0360365110.png)

Again, the File ID is what's circled in red.

#### 2. Launching the script

* Open a new **Terminal** and change the current working directory to where gSynch is installed (use the `cd <path>` command to do so).
* You can now launch **gSynch** by typing this command in your command-prompt :

````
python main.py <steam_app_id> <steam_workshop_file_id> <repository_public_link>
````

And replace `<steam_app_id>`, `<steam_workshop_file_id>`, `<repository_public_link>` with their respective values

## Misc
#### Credits
* [Gabriel Santamaria](https://github.com/Gabyfle)  : original code
#### Used softwares
* Jetbrains PyCharm 2019.3 Professional
