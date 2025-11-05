from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table

def main():
    console = Console()
    console.print("NHL Statistics")
    
    season = console.input("Season [bold cyan][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]:").strip()
    nationality = console.input("Nationality [bold cyan][USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]:").strip().upper() 
    
    
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)
    
    if not players:
        console.print(f"No players found for {nationality} in season {season}.", style="red")

    
    table = Table(title="Players from {nationality} in season {season}")

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

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
