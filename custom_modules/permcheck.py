import json
import hikari
import lightbulb

OFF_SWITCH  = "database/off-switch.json"

# Checks if all Command toggles are turned on, and, if specified, if the commands Author has Admin privileges
async def permcheck(ctx=None, adminrequired=False):

    with open(OFF_SWITCH, 'r') as f:
        settings = json.load(f)
        g_setting = settings.get(f"GLOBAL")
        if not ctx == None:
            try:
                command = ctx.name
            except AttributeError:
                command = ctx.command
 
        else: return g_setting
        c_setting = settings.get(f"{command}")
        if g_setting == "False":
            return False
        if c_setting == "False":
            return False
        if adminrequired is False:
            return True
        else:
            try:

                roles = await ctx.event.get_member().fetch_roles()
                permissions = hikari.Permissions.NONE
                for role in roles:
                    permissions |= role.permissions


                if (permissions & hikari.Permissions.ADMINISTRATOR) == hikari.Permissions.ADMINISTRATOR:
                    return True
                else:
                    return False
            except AttributeError:
                guild_id = ctx.guild_id

                


                if ctx.event.interaction.permissions_for(ctx.author).administrator:
                    return True
                else:
                    return False