from aiogram import types


# We have one command for starting bot

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", "Show game menu")
        ]
    )