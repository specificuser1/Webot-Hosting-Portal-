import discord

def get_activity(activity_type: str, text: str):
    activity_type = activity_type.lower()

    if activity_type == "playing":
        return discord.Game(name=text)

    elif activity_type == "watching":
        return discord.Activity(type=discord.ActivityType.watching, name=text)

    elif activity_type == "listening":
        return discord.Activity(type=discord.ActivityType.listening, name=text)

    elif activity_type == "competing":
        return discord.Activity(type=discord.ActivityType.competing, name=text)

    elif activity_type == "streaming":
        return discord.Streaming(name=text, url="https://twitch.tv/xyz")

    return discord.Game(name=text)
