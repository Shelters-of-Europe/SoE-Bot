from    random                                  import randint
from    colorama                                import Fore, Back, Style
from    pathlib                                 import Path
import  os
import  sys
import  hikari
import  lightbulb

# adding additional paths
sys.path.insert(1, '{}/database'.format(os.getcwd()))
sys.path.insert(1, '{}/assets'.format(os.getcwd()))
sys.path.insert(1, '{}/commands'.format(os.getcwd()))
sys.path.insert(1, '{}/custom_modules'.format(os.getcwd()))

# custom modules:
from    important           import  token, DevID, BotID, prefix
from    permcheck           import  permcheck

# Creates the BotApp object that will be used everywhere after this point
bot         = lightbulb.BotApp(token=token, prefix=lightbulb.when_mentioned_or(prefix), help_class=None, intents=hikari.Intents.ALL)

# Prints a message that the Bot has logged in, and also prints the current Setting of the global command toggle
@bot.listen()
async def on_ready(event: hikari.StartedEvent) -> None:
    print(Fore.GREEN + 'We have logged in as {}'.format(bot.cache.get_user(BotID)) + Style.RESET_ALL)
    if await permcheck():
        print(Fore.GREEN + 'Command Toggle : {}'.format(await permcheck()) + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Command Toggle : {}'.format(await permcheck()) + Style.RESET_ALL)

@bot.listen()
async def on_member_join(event: hikari.MemberCreateEvent) -> None:
    print("Member joined!")
    member = event.member
    rollenname = str(member.id)
    rolle = None
    guild = event.get_guild()
    for role in bot.cache.get_roles_view_for_guild(guild):
        role = guild.get_role(role)
        if role.name == rollenname:
            rolle = role
    if rolle is not None:
        await member.add_role(rolle)

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent) -> None:
    if event.context.command == None:
        print(Fore.RED + "Ein User ({}) hat versucht einen Command ({}{}) der nicht existiert zu benutzen.".format(event.context.author, event.context.prefix, event.context.invoked_with) + Style.RESET_ALL)
        await event.context.respond("Dieser Befehl existiert nicht")
    else:
        await event.context.respond("Ein Fehler ist aufgetreten. <@{}>".format(DevID), user_mentions=True)
        raise event.exception

@bot.listen(hikari.GuildMessageCreateEvent)
async def on_message(message: hikari.MessageEvent) -> None:

    if message.author.id == BotID:
        return
    if message.content is None:
        return
    
    nachricht = message.content.lower().split(' ')
    channel = message.get_channel()
    guild = message.get_guild()
    category = guild.get_channel(channel.parent_id)

    if category.name.lower() not in ["team stuff uwu", "allgemein", "charaktere", "voice channelsx"]:
        return
    
    if "rico" in nachricht or "rigge" in nachricht:
        if message.author.id != 123825591161061380:
            banngifs = ["https://tenor.com/view/ban-button-keyboard-press-the-ban-button-gif-16387934", 
                        "https://tenor.com/view/subscribe-to-my-onlyfans-onlybans-banned-ban-gif-20504981", 
                        "https://tenor.com/view/bongocat-banhammer-ban-hammer-bongo-gif-18219363", 
                        "https://tenor.com/view/when-your-team-too-good-ban-salt-bae-gif-7580925", 
                        "https://tenor.com/view/spongebob-ban-pubg-lite-banned-rainbow-gif-16212382", 
                        "https://tenor.com/view/bane-no-banned-and-you-are-explode-gif-16047504"]
            banngif = banngifs[randint(0, len(banngifs)-1)]
            await message.message.respond("{}".format(banngif), reply=True)
        else:
            await message.message.respond("{}".format("https://tenor.com/view/mr-muffin-kill-me-somebody-kill-me-gif-9195488"), reply=True)

bot.load_extensions_from("commands/")

# Starts the bot and logs in using the specified token
bot.run()