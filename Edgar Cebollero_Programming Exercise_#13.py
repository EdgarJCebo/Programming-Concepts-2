import sqlite3
import random
import matplotlib.pyplot as plt

#Configuration and Florida cities chosen
DB_NAME = "population_XX.db"

FLORIDA_CITIES = [
    "Miami",
    "Orlando",
    "Tampa",
    "Jacksonville",
    "Tallahassee",
    "Cape Coral",
    "Fort Lauderdale",
    "Hialeah",
    "St. Petersburg",
    "Port St. Lucie"
]

#2023 population values
POP_2023 = {
    "Miami": 441713,
    "Orlando": 310875,
    "Tampa": 387450,
    "Jacksonville": 955408,
    "Tallahassee": 196250,
    "Cape Coral": 258210,
    "Fort Lauderdale": 182060,
    "Hialeah": 221300,
    "St. Petersburg": 258210,
    "Port St. Lucie": 218195
}



#Creates database
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    #Insert 2023 data
    for city, pop in POP_2023.items():
        cur.execute("INSERT INTO population VALUES (?, ?, ?)",
                     (city, 2023, pop))

    conn.commit()
    conn.close()
    print("Database created and 2023 population data inserted.")



#Simulate population growth for 20 years
def simulate_population_growth():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for city in FLORIDA_CITIES:
        #Gets the 2023 population
        cur.execute("SELECT population FROM population WHERE city=? AND year=2023", (city,))
        pop = cur.fetchone()[0]

        for year in range(2024, 2044):  # simulate next 20 years
            #Growth/decline rate between -2% and +3%
            rate = random.uniform(-0.02, 0.03)
            pop = int(pop * (1 + rate))

            cur.execute("INSERT INTO population VALUES (?, ?, ?)",
                        (city, year, pop))

    conn.commit()
    conn.close()
    print("20-year population simulation complete.")



#Plot population for selected city
def plot_population():
    print("\nChoose a city to display its population growth:")
    for i, city in enumerate(FLORIDA_CITIES, start=1):
        print(f"{i}. {city}")

    choice = int(input("\nEnter number (1–10): "))
    city = FLORIDA_CITIES[choice - 1]

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT year, population FROM population WHERE city=? ORDER BY year",
                (city,))
    rows = cur.fetchall()

    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    conn.close()


#Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(years, populations, marker="o")
    plt.title(f"Population Growth: {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


#Main program
if __name__ == "__main__":
    create_database()
    simulate_population_growth()
    plot_population()
