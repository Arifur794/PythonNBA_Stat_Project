from nba_py import shotchart
from nba_py.player import get_player

def test():
    pid = get_player('Lebron', 'James') #find errror handler for invalid name
    assert shotchart.ShotChart(pid)     #find any case-sensitive/player names including " - " , " ' "
    
