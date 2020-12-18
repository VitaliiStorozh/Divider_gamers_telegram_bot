from aiogram import types

from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from loader import dp

from random import shuffle

players = {}  # For registration users for game
players_l = []  # Temporary list for dividing players on rivals


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    """This command starts bot"""
    await message.answer("Register to play", reply_markup=menu)


@dp.message_handler(text="Registration")
async def register(message: types.Message):
    """This handler add players as a future rivals"""
    await message.reply("Congratulations, you have successfully registered.")
    answer = message.from_user.full_name
    key = str(message.from_user.id)

    players[key] = answer


@dp.message_handler(text="Start")
async def start(message: types.Message):
    """This handler divides players on rivals"""
    for elem in players:
        players_l.append(players[elem])
    shuffle(players_l)
    if len(
            players_l) < 2:  # If one or no players are registered, a message will be returned that there are not enough players
        await message.answer("Not enough players")
    else:
        z = 0
        while len(players_l) > 1:
            z += 1
            n = 0
            team = []
            while n < 2:
                team.append(players_l.pop())
                n += 1
            await message.answer(
                f"Game № {z}\n"
                f"{team[0]} vs {team[1]}"
            ) # Divides opponents into pairs and the group is issued messages with pairs of opponents
        else:
            if len(players_l) == 1: # If the number of players is not even. A message will be issued for a player who has not had enough money that he is in reserve
                await message.answer(f"In reserve: \n"
                                     f"{players_l[0]}")

    players_l.clear()


@dp.message_handler(text="Clear player list")
async def clear(message: types.Message):
    """This hadler clears list of gamers for restarting with new players"""
    await message.answer("The list of players has been cleared, register again for the next game")
    players.clear()
