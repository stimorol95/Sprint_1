world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions ['2022'] = 'Аргентина'

for year, champion in world_champions.items():
    print(f"{year} - {champion}")

country = 'Италия'

if country in world_champions.values():
    print(f"{country} становилась чемпионом мира по футболу в 21 веке!")
else:
    print(f"{country} не выигрывала чемпионат мира по футболу в 21 веке.")