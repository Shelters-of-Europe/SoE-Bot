import  hikari
import  lightbulb
from    can_dm_user import can_dm_user
from    cmd_log     import cmd_log
from    permcheck   import permcheck

plugin = lightbulb.Plugin("Test")

@plugin.command()
@lightbulb.command("test", "nur ein Test")
@lightbulb.implements(lightbulb.PrefixCommand)
async def test(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx, True):
        can_dm = await can_dm_user(ctx.author)
        await ctx.respond("Ergebnis: {}".format(can_dm))

def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)