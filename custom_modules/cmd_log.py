import hikari
import lightbulb
import json

LOGIDS = "database/logids.json"

# Gets the ID of the Channel to log in. Dependant on Server
def get_logID(ctx):
    with open(LOGIDS, 'r') as f:
        logs = json.load(f)
    return logs.get(f'server_{ctx.guild_id}')

# Logs the executed Command
async def cmd_log(ctx):
    logchannelid = get_logID(ctx)
    if logchannelid != 0:
        logchannel = ctx.bot.cache.get_guild_channel(int(logchannelid))
    if logchannelid == 0:
        return
    else:
        try:
            await logchannel.send('{} nutzte den Slash-Befehl "{}".'.format(ctx.author, ctx.command.name))
        except AttributeError:
            await logchannel.send('{} nutzte den Befehl "{}"'.format(ctx.author, ctx.command.name))
