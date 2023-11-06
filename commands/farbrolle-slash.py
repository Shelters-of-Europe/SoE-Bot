import  hikari
import  lightbulb
from    cmd_log     import cmd_log
from    permcheck   import permcheck

plugin = lightbulb.Plugin("Farbrolle")

@plugin.command()
@lightbulb.option("farbe", "Die Farbe welche deine Rolle haben soll (Als Hexcode)", type=str, default="000000")
@lightbulb.command("farbrolle", "Setze dir eine custom Nickname Farbe")
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx: lightbulb.Context) -> None:

    await cmd_log(ctx)

    if await permcheck(ctx):

        user = ctx.author.id

        rollen = await ctx.get_guild().fetch_roles()
        user_role = None
        
        farbe :str = ctx.options.farbe

        if farbe.startswith("#"):
            farbe = farbe[1:]
        
        if not len(farbe) == 6:
            await ctx.respond("Du hast keinen gültigen Hexcode eingegeben, bitte versuch es erneut.")
            return

        for role in rollen:
            if role.name == str(user):
                user_role = role
        
        if user_role is None:
            new_role = await ctx.bot.rest.create_role(
                ctx.guild_id,
                name=str(user),
                permissions=(
                hikari.Permissions.READ_MESSAGE_HISTORY
                | hikari.Permissions.SPEAK
                | hikari.Permissions.CONNECT
                | hikari.Permissions.USE_VOICE_ACTIVITY
                ),
                color=farbe
            )

            await ctx.bot.rest.add_role_to_member(
                ctx.guild_id,
                ctx.author,
                new_role
            )

            await ctx.bot.rest.reposition_roles(
                ctx.guild_id,
                {10:new_role}
            )

            await ctx.respond("Deine Rolle wurde erstellt.")
        
        if user_role is not None:

            await ctx.bot.rest.edit_role(
                ctx.guild_id,
                user_role,
                color=farbe
            )

            await ctx.respond("Deine Rolle wurde bearbeitet.")
def load(bot):
    bot.add_plugin(plugin)

def unload(bot):
    bot.remove_plugin(plugin)