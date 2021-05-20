# [Placeholder-Chan](https://mojo.highquality.rip)
[![invite-badge][]][invite]

### I am not done updating the source code yet. I will upload it here with a license when it's ready.


<p align="center">
  <img height=500 src="https://mojo.highquality.rip/wp-content/uploads/2019/08/placeholder-chan.png">
</p>
<p align="center">
  Illustration: Dead Line (<a href="https://twitter.com/DeddoRain">@DeddoRain</a>)
</p>


This is the source code for Placeholder-Chan, a failed project of mine from two years ago. I decided to finish it and upload it. What you're getting here isn't exactly what I left untouched for two years, but it's mostly unchanged aside from a few improvements to the code and updates to the character info. So aside from a few improvements and updates, you're getting esentially what was my horrible code from two years ago.

# The Story
So about two years ago, the [SiIvaGunner: King for Another Day Tournament](https://siivagunner.fandom.com/wiki/King_for_Another_Day_Tournament) was a thing. At the time, I was heavily-invested in high-quality rips and the shitposty nature of them, as I was a very shitposty person. I knew nothing of making music or art, but being the person I am, I still wanted to contribute *something*. So, I made a Discord bot and called it Placeholder-Chan, who is one half of the bonus character Fighting Placeholder Team. I used my [Mewtwo Bot](https://github.com/sks316/mewtwo-bot) as a base. The Placeholder-Chan bot essentially acts as a knowledge base for the tournament and can post the source list for each character on-demand. I made the bot, then proposed the idea of it to one of the official SiIvaGunner Discord admins. They shot me down, and I never touched the bot again.

Fast-forward to today. I was looking at old projects, and I saw Placeholder-Chan's files, sitting untouched. I thought I should finish it, so I did. I like to have all my projects be open-source, so it's here now. I also threw it up on my Raspberry Pi because why not.

# How to run the bot
Why are you people so invested in running my shitty projects... *sigh* okay, so...

## Cloning the repo
Clone the repo:
```
git clone https://github.com/sks316/placeholder-chan.git
```
## Installing dependencies
Make sure you've installed Python. If it's not installed, go install it and come back.

Once you've installed Python or if you already had it installed, cd into the cloned directory and run the following:
```
pip install -r requirements.txt
```
This will install everything that Placeholder-Chan needs to run.
## Config file
Since it's based on my Mewtwo bot, and since I'm not as much of an idiot as I like to think, Placeholder-Chan also needs a config file.

Go to the directory containing `placeholder-chan.py` then make a new file called `placeholder_config.py`. This will be our config file.
Next (hopefully you've already done this), go to the [Discord Developer Portal](https://discordapp.com/developers/applications/) and create an application. Once done, go to `Bot` and hit the `Add Bot` button. Once done, you should be able to get your token! **I SHOULDN'T HAVE TO SAY THIS, BUT DO NOT SHARE THIS TOKEN WITH ANYONE, IT WILL GIVE FULL ACCESS TO YOUR BOT.**

You'll also want to enable both the Presence Intent and Server Members Intent.

Now open `placeholder_config.py` in your favorite text editor and paste the following:
```
token = 'YOUR-TOKEN-HERE'
owner = YOUR-USER-ID-HERE
```
Replace `YOUR-TOKEN-HERE` with your bot's token and `YOUR-USER-ID-HERE` with ***your*** User ID, not your bot's.
## Running the bot
Finally, we run the bot. cd into the directory you cloned the repo to and run:
```
py placeholder-chan.py
```
Or, if you're using Linux:
```
python3 placeholder-chan.py
```


[invite]: https://example.com
[invite-badge]: https://img.shields.io/badge/invite%20placeholder—chan-click%20here-black.svg?style=for-the-badge&colorB=7289DA
