capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
print(capitals)

# Nesting a list in a dictionary:-
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamsburg", "Stuttgart"]
}
print(travel_log)

# Nesting dictionary in a dictionary:-
travel_log_modified = {
    "France": {
        "Cities Visited" : ["Paris", "Lille", "Dijon"],
        "Number of Visits": 2,
    },
    "Germany": {
        "Cities Visited" : ["Berlin", "Hamsburg", "Stuttgart"],
        "Number of Visits": 1,
    }
}
print(travel_log_modified)

# Nesting dictionary in a list:-
log = [
    {
        "country": "France", 
        "Cities Visited" : ["Paris", "Lille", "Dijon"],
        "Number of Visits": 2,
    },
    {
        "country": "Germany",
        "Cities Visited" : ["Berlin", "Hamsburg", "Stuttgart"],
        "Number of Visits": 1,
    }
]
print(log)