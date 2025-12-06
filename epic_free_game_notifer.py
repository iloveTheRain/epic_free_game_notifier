import requests
from pathlib import Path
from colorama import Fore, init
from time import sleep

# This is cli project that sends current free games on epic games to a discord webhook

init(autoreset=True)

class GetEpicFreeGames:

    def fetch_free_games(self):
        source = requests.get(
            "https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?country=US"
        )

        # ---------- Checking for erros...---------------

        if not source.status_code == 200:
            print(Fore.RED + "Source is down")
            return

        source_data = source.json()

        if not source_data:
            return
        # ------------------------------------------------

        game_info = []

        games = source_data["data"]["Catalog"]["searchStore"]["elements"]

        for game in games:

            is_free = game["price"]["totalPrice"]["fmtPrice"]["discountPrice"]

            if is_free == "0":
                game_img = (
                    game["keyImages"][0]["url"] if game.get("keyImages") else None
                )
                game_name = game["title"]

                game_info.append({"name": game_name, "image": game_img})

        return game_info

    def sent_games(self):  # reading the file to check if the game exits

        try:
            main_file = Path(__file__).resolve().parent
            file_loc = Path.joinpath(main_file, "sent_games.txt")

            with open(file_loc, "r", encoding="utf-8") as f:
                return [line.strip() for line in f.readlines()]

        except FileNotFoundError:
            return []

    def save_game(self, game_name):  # saving new games

        main_file = Path(__file__).resolve().parent
        file_loc = Path.joinpath(main_file, "sent_games.txt")

        with open(file_loc, "a", encoding="utf-8") as f:
            f.write(f"{game_name}\n")

    def send_to_discord(self, web_hook):
        games_data = self.fetch_free_games()

        if not games_data:
            print(Fore.RED + "There are no game data")
            return

        embeds = []
        for game in games_data:
            embeds.append(
                {
                    "title": "🎁Epic games FREE GAME🎁",
                    "description": f"Game name: **{game['name']}**",
                    "color": 0x2ECC71,  # green
                    "image": {"url": game["image"]} if game["image"] else {},
                }
            )

        payload = {"embeds": embeds}

        try:

            if game["name"] in self.sent_games():  # checking if the game is already sent if so retrun
                print(Fore.RED+"Already sent the games in discord server if you want to send them again remove them from the sent_games.txt file")
                sleep(2)
                return

            # if this code below run then it means game doesn't exits
            response = requests.post(web_hook, json=payload, timeout=10)  # sending the new free game to discord

            for game_name in games_data:
                self.save_game(game_name["name"])  # saving the game name in the file so when the code run again it doesn't send the same game

            if response.status_code not in (200, 204):
                print(Fore.RED + f"Discord Error {response.status_code}")
            else:
                print(Fore.GREEN + "Sent free games to Discord!")
                sleep(1)

        except Exception as e:
            print(Fore.RED + f"Error sending to discord: {e}")

#--------------- MAIN ---------------
if __name__ == "__main__":
    main_file = Path(__file__).resolve().parent
    web_hook_file = Path.joinpath(main_file,"webhook.txt")

    if not web_hook_file.exists():
        webhook = input(Fore.LIGHTGREEN_EX+"Enter the webhook: ").strip()
        
        with open(web_hook_file, 'w',encoding='utf-8') as file:
            file.write(webhook)


    file_content = web_hook_file.read_text(encoding='utf-8')

    freegames = GetEpicFreeGames()
    freegames.send_to_discord(file_content)