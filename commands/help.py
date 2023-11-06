import  hikari
import  lightbulb
from    cmd_log     import cmd_log
from    permcheck   import permcheck
from    commandhelp import  command_help

plugin = lightbulb.Plugin("Help")

@plugin.command()
@lightbulb.option("befehl", "Der Befehl zu welchem du Hilfe brauchst", type=str, default="help")
@lightbulb.command("help", "Hilfe zu Commands")
@lightbulb.implements(lightbulb.PrefixCommand)
async def help(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx):
        await ctx.respond("{}".format(command_help(ctx.options["befehl"])))

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)