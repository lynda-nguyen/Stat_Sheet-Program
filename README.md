# Stat_Sheet-Program

A Python program for data collection with a basketball Stat Sheet. 
Intended for live games or watching film. *Actions* are columns of the Stat Sheet.

**Menu Options** 
*Menu pops up when 'back' is entered as input*
1. See Table 
2. Export Data 
3. Record More Data (Go back) 
4. Look Up Team 
5. Look Up Actions
6. Change Date
-- To exit entire program type 'exit' --

Exports data into a .csv file.

**How to change/update team players list**
Change through config.py
Add/remove players from players_list array

**Automatic addition functions**
Each 'FG' gets instantly added to 'FGA' 
Each '3FG' gets instantly added to '3FGA' 
Each 'OREB' and 'DREB' instantly gets added to 'TREB'
Each 'FG' and '3FG' gets added per player's 'PTS' column
Totals are instantly calculated in the last row
