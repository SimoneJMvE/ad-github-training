def likes(team: list) -> str:
    if len(team) == 0:
        return "no one likes this"
    elif len(team) == 1:
        return f"{team[0]}likes this"
    elif len(team)  == 2:
        return f"{team[0]} en {team[1]} likes this"

    else:
        return  "To many people like your post"




