import sqlite3
import matplotlib.pyplot as plt
import numpy as np

# Create the database and cursor
conn = sqlite3.connect('population_vb.db')
cursor = conn.cursor()

# The table_setup() function sets up the population table in
# population_vb.db.
def table_setup():
    # Deletes table if it already exists (which is convenient for writing
    # and testing!)
    conn.execute("DROP TABLE IF EXISTS population")
    # Creates a table with fields city, year, and pop (population)
    conn.execute("""CREATE TABLE population(city TEXT,
                                            year INTEGER,
                                            pop INTEGER)""")

    # List of tuples containing all city data
    florida_city_data = [("Jacksonville", 2025, 1024310),
                      ("Miami", 2025, 498060),
                      ("Tampa", 2025, 421042),
                      ("Orlando", 2025, 341600),
                      ("St. Petersburg", 2025, 269059),
                      ("Hialeah", 2025, 238630),
                      ("Port St. Lucie", 2025, 271511),
                      ("Tallahassee", 2025, 206877),
                      ("Cape Coral", 2025, 242422),
                      ("Fort Lauderdale", 2025, 192610)]

    # Inserts all data for a city at once for each city
    cursor.executemany('INSERT INTO population VALUES (?, ?, ?)', florida_city_data)
    conn.commit()

    return florida_city_data

# The simulation() function simulates population shift and inserts new data
# into the table.
def simulation(city_data):
    # For every city, for every year, calculate a realistic possible
    # population, and insert the data into the table
    for name, year, pop in city_data:
        for next_year in range (2026, 2046):
            pop = int(pop * np.random.uniform(0.98, 1.04))
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)", (name, next_year, pop))
    conn.commit()

# The graph() function graphs a user-selected city's data.
def graph(cities):
    # Creates a list of just the city names
    city_names = [city[0] for city in cities]

    # Creates a list of cities for the user to choose from.
    print("City options:")
    for index, city_name in enumerate(city_names):
        print(f"{index + 1}. {city_name}")

    # The infinite loop will break when the user types in a valid integer.
    while True:
        try:
             choice = int(input("Enter the number city you'd like to see (e.g. 1, 2) : "))
             if 1 <= choice <= len(city_names):
                 break
             else:
                 print(f"ERROR: Please enter an integer in the correct range.")
        except Exception:
            print("ERROR: Please enter an integer.")
    # Picks the right city out of the list
    user_city = city_names[choice - 1]

    # Finds the year and population for the selected city, and order by year
    cursor.execute("SELECT year, pop FROM population WHERE city=? ORDER BY year", (user_city,))
    rows = cursor.fetchall()

    # Creates lists of years and populations from the above data using
    # comprehensions
    years = [row[0] for row in rows]
    # Population divided by 1,000,000 so matplotlib doesn't use
    # scientific notation
    pops = [row[1] / 1000000 for row in rows]

    # Creates the graph
    plt.plot(years, pops)
    plt.title(f"{user_city} Population Prediction")
    plt.xticks(range(2025, 2046, 5))
    plt.xlabel("Year")
    plt.ylabel("Population (millions)")
    plt.show()

def main():
    cities = table_setup()
    simulation(cities)
    graph(cities)

if __name__ == "__main__":
    main()
