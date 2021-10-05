from django.http import HttpResponse, response
from django.http.request import HttpRequest
from django.shortcuts import render
from dataclasses import dataclass
from typing import Dict, List

# Create your views here.
@dataclass
class Game:
    name: str
    description: str
    players: List[str]

def sports(request: HttpRequest, sport):
    context = {
        "Game": sport,
        "fav": {
            "Baseball": Game("Baseball", "Baseball is a game where the pitcher throws the ball to a batter. The batter wants to hit the ball. If the ball is thrown where the batter can easily hit it and the batter doesn't hit it, then it is a strike. If the player swings and misses it is also a strike. Otherwise it is a ball. if you get 4 ballso then you can take your base However if you get 3 strikes is an out and if you get 3 outs then you switch from offense to defense. Some great baseball players are", ["Greg Maddux", "Derrick Jeter", "Babe Ruth", "Barry bonds"]),
            "Football": Game("Football", "Football is a game where you try to score touchdowns. A touchdown is when you are on Offense and you are able to go all the way down to the other side of the field and get the ball in the endzone. However you have a defense trying to stop you from scoring and get their Offense back on the field. Some great football players are", ["Joe Montana", "Tom Brady", "Barry Sanders", "Jerry Rice"]),
            "Basketball": Game("Basketball", "Basketball is a sport where you try to score points by putting the ball through the hoop. If you shoot in front of the arc you get 2 points but if you are behind it you get 3. You are trying to do this against a defense. Your positions are point guard, shooting guard, small forward, power forward, and center. These players all have different roles on the court. For example the center is most likely going to be your biggest player. He get open around the rim and when he is on defense he will try to defend the post from the other team trying to get an easy bucket. Some great basketball players are", ["Michael Jordan", "Kobe Bryant", "Lebron James", "Kevin Durant"])
        }
    }
    return render(request, "details.html", context)


def home(request: HttpRequest):
    return render(request, "index.html")
