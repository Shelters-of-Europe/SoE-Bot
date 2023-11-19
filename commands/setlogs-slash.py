import  hikari
import  lightbulb
from    cmd_log     import cmd_log
from    permcheck   import permcheck

plugin = lightbulb.Plugin("Setlogs")

@plugin.command()
@lightbulb.option("action", "Was tun mit dem Channel?", choices=["set", "remove"] )
@lightbulb.option("channel", "Welchen Channel möchtest du setzen?", type=7, channel_types=0, default=None)
@lightbulb.command("setlogs", "Admin command to set the channel where logs should be sent")
@lightbulb.implements(lightbulb.SlashCommand)
async def setlogs(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx, True):
        ctx.respond("Boop!")
        return

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)