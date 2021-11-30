counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")



voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for group in voting_data:
        print(f"{group['county']} county has {group['registered_voters']:,} registered voters.")




bag = [{"name":"Aviar", "stats": 2301},
                {"name":"Roc3", "stats": 5503},
                {"name":"Teebird", "stats": 7402}]

for discs in bag:
    print(f"{discs['name']} has these stat numbers {discs['stats']}.")
