countries = [
    ["USA", 340_000_000, "Washington, D.C."],
    ["UK", 70_000_000, "London"],
    ["France", 69_000_000, "Paris"],
    ["Germany", 83_000_000, "Berlin"],
    ["Turkey", 88_000_000, "Ankara"],
    ["Russia", 146_000_000, "Moscow"],
    ["India", 1_450_000_000, "New Delhi"],
    ["China", 1_400_000_000, "Beijing"],
    ["Japan", 120_000_000, "Tokyo"],
]

for name, _population, capital in countries:
    if name == "France":
        print(capital)
        break
