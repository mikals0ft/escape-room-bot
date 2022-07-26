# Discord Py Bot Template

Discord.py is a library that allows you to make discord bots with python and this repo is a template of a bot which is made by using Discord.Py.
- ✨I am trying to help the bot developing community with this template✨

## Features

- 10+ ready to use functions.
- Easy start for begginer bot developers.

## Notes From The Developer
> It is recommended to use other sources to get started with the bot developement process and use this repo to take a look when you strugle or when you need to see a finished bot structure.

> The code written in this project was in my very early times of coding so don't rely on its organization and code layout.

> I will be releasing a comprehensive update about the file organization and clean code when i have the time for it.
# Setup

Bot requires [Python 3](https://www.python.org/) to run.

### Install the dependencies

```sh
pip install -r requirements.txt
```
> Or you can use the setup.bat file to run this code automatically.

### Setting up the bot properties

```python
#Set the bot status below.
BotStatus = "Example Bot"

#Set your bots prefix.
Prefix = "."
```

# Discord Bot Setup
Create an application at https://discord.com/developers/applications.
Under the app, create a Bot.
Under Bot/Privileged Gateway Intents, enable both presence intent and server members intent.
Add the token from the Bot page to the `BOT_TOKEN` environment variable.
```bash
export BOT_TOKEN=[bot token]
```
Invite your bot to your test server via https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&permissions=432114318432&scope=bot, where the client id is found in your General Information page.

# How to run
The bot can be started with a python command:
```sh
python Bot.py
```

# Contribution
You can always pull request to this repo, if you report or fix a bug or if you add more commands to the template I'll be happy to implement them.

