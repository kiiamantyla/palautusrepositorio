from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

def ask_user_input(console):
    season = console.input(
        "Season [bold cyan][2018-19/2019-20/2020-21/2021-22/"
        "2022-23/2023-24/2024-25/2025-26]:"
    ).strip()

    nationality = console.input(
        "Nationality [bold cyan][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/"
        "SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]:"
    ).strip().upper()

    return season, nationality


def build_table(players, nationality, season):
    table = Table(title=f"Players from {nationality} in season {season}")

    table.add_column("Name", justify="left", style="cyan", no_wrap=True)
    table.add_column("Team(s)", justify="left", style="magenta")
    table.add_column("Goals", justify="right", style="red")
    table.add_column("Assists", justify="right", style="red")
    table.add_column("Points", justify="right", style="red")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points)
        )

    return table

def fetch_players(season, nationality):
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(nationality)

def main():
    console = Console()
    console.print("NHL Statistics")

    season, nationality = ask_user_input(console)
    players = fetch_players(season, nationality)

    if not players:
        console.print(f"No players found for {nationality} in season {season}.", style="red")
        return

    table = build_table(players, nationality, season)
    console.print(table)

if __name__ == "__main__":
    main()
