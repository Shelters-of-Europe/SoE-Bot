import hikari
import lightbulb

# Checks if Bot is able to DM specified User
async def can_dm_user(user: hikari.User) -> bool:
    try:
        await user.send("")
    except hikari.ForbiddenError:
        return False
    except hikari.HTTPError:
        return True