# divider_gamers_telegram_bot
Telegram bot, which will create a random list of players from the list of users who registered through the bot, for example, in Fifa

What we have:
There are users in the telegram group, which also includes the telegram bot. Every time they want to play Fifa, they need to split into teams. The bot menu opens and there are 3 buttons, the first button is “Register” and the second is “Start”, the third is “Clear the list of players”. Before the game, we press to clear the list of players and then everyone who wants to take part press “Registration”. To randomly distribute teams, you need to press "Start"
For example:
There is Vasya, Petya, Benjamin, Gena, Pasha and Grisha,
they all clicked on “Register”, after you press “Registration”, the bot displays the type of such message “Gena registered” in the chat (after each participant confirms that he is registered), in general, the bot has clicked on all the names who have registered.
After someone has clicked on "Start", the bot shuffles these names and gives out pairs of participants, something like this:

Game № 1
Petya vs Gena

Game № 2
Vasya vs Pasha

Game № 3
Veniamin vs Grisha


If no one has registered or less than 2 players have registered, then the bot issues the phrase “Not enough players”. After clicking on the button "Clear the list of players", the bot issues a phrase in the chat, "The list of players is cleared, register again for the next game"

If it so happened that an odd number of players registered, for example 5, then the bot will give out 2 pairs and the 5th player will be in reserve, something like this:

The first game
Petya vs Gena

Second game
Vasya vs Pasha

In reserve
Benjamin
