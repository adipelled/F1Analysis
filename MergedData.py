import pandas as pd

# Load CSV files
results = pd.read_csv("AllData/results.csv")
qualifying = pd.read_csv("AllData/qualifying.csv")
races = pd.read_csv("AllData/races.csv")
drivers = pd.read_csv("AllData/drivers.csv")
driver_standings = pd.read_csv("AllData/driver_standings.csv")
# Make sure 'number' is the same type across files
results["number"] = results["number"].astype(str)
qualifying["number"] = qualifying["number"].astype(str)
drivers["number"] = drivers["number"].astype(str)


# Preview structure (optional)
print("Results preview:\n", results[['raceId', 'number', 'positionOrder']].head())
print("Qualifying preview:\n", qualifying[['raceId', 'number', 'position']].head())
print("Races preview:\n", races[['raceId', 'year', 'round', 'circuitId', 'name']].head())
print("Drivers preview:\n", drivers[['driverRef', 'number', 'code', 'forename', 'surname']].head())
print("Driver Standings preview:\n",
      driver_standings[['driverStandingsId', 'raceId', 'points', 'position']].head())

# Merge results with qualifying data
merged = pd.merge(results, qualifying, on=["raceId", "number"], suffixes=('_race', '_qual'))

# Filter to necessary columns
print("Columns in merged DataFrame:", merged.columns.tolist())
merged = merged[['raceId', 'number', 'positionOrder', 'position_qual']]

# Create binary column: 1 if podium (top 3), else 0
merged['podium_finish'] = merged['positionOrder'].apply(lambda x: 1 if x <= 3 else 0)

# Rename for clarity
merged.rename(columns={'position_qual': 'qualifying_position'}, inplace=True)
merged.dropna(subset=['qualifying_position', 'positionOrder'], inplace=True)

# Convert to numeric if needed
merged['qualifying_position'] = pd.to_numeric(merged['qualifying_position'], errors='coerce')
merged['positionOrder'] = pd.to_numeric(merged['positionOrder'], errors='coerce')

# Merge with races to get year and track info
merged = pd.merge(merged, races[['raceId', 'year', 'name']], on='raceId')
merged = merged[merged['year'] > 2019]
merged.reset_index(drop=True, inplace=True)  # optional

# add driver ID into merged dataset
merged = pd.merge(merged, drivers[['number', 'forename', 'surname']], on='number')
merged['driver_name'] = merged['forename'] + ' ' + merged['surname']
driver_standings = driver_standings[['raceId', 'points', 'position']]
merged = pd.merge(merged, driver_standings, on=['raceId'], how='left')
merged.rename(columns={'position': 'championship_position'}, inplace=True)

pd.set_option('display.max_columns', None)
print(merged[['driver_name', 'year', 'name', 'qualifying_position', 'positionOrder', 'podium_finish', 'points',
              'championship_position']].head())
# Save to CSV

merged.to_csv("AllData/f1_merged_cleaned1.csv", index=False)

# Data cleaning complete — ready for modeling in the next step
