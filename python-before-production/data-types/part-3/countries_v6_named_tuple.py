from collections import namedtuple

Country = namedtuple("Country", ["population", "capital"])

countries = {
    "USA": Country(340_000_000, "Washington, D.C."),
    "UK": Country(70_000_000, "London"),
    "France": Country(69_000_000, "Paris"),
    "Germany": Country(83_000_000, "Berlin"),
    "Turkey": Country(88_000_000, "Ankara"),
    "Russia": Country(146_000_000, "Moscow"),
    "India": Country(1_450_000_000, "New Delhi"),
    "China": Country(1_400_000_000, "Beijing"),
    "Japan": Country(120_000_000, "Tokyo"),
}

print(countries["France"].capital)
