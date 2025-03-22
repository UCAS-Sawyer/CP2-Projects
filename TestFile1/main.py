import pandas as pd

# Load the entire CSV
df = pd.read_csv('BattleSimulator/csvs/characters.csv')

# Display the DataFrame
print(df.memory_usage(deep=True))  # Check memory usage

# Load the entire CSV
df = pd.read_csv('BattleSimulator\\csvs\\easy_monsters.csv')

# Display the DataFrame
print(df.memory_usage(deep=True))  # Check memory usage

# Load the entire CSV
df = pd.read_csv('BattleSimulator\\csvs\\medium_monsters.csv')

# Display the DataFrame
print(df.memory_usage(deep=True))  # Check memory usage