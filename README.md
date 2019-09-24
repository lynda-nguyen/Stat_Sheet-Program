# Stat_Sheet-Program

A Python program for data collection with a basketball Stat Sheet. <br/>
Intended for live games or watching film. *Actions* are columns of the Stat Sheet.<br/>
<br/>
**Menu Options**
<br/>
*Menu pops up when 'back' is entered as input*<br/>
1. See Table 
2. Export Data 
3. Record More Data (Go back) 
4. Look Up Team 
5. Look Up Actions
6. Change Date <br/>
-- To exit entire program type 'exit' --
<br/>
Exports data into a .csv file.
<br/>
<br/>

 **How to change/update team players list:** 
<br/>Change through config.py <br/>
Add/remove players from players_list array <br/>
<br/>

 **Automatic addition functions:** 
<br/>Each 'FG' gets instantly added to 'FGA' <br/>
Each '3FG' gets instantly added to '3FGA' <br/>
Each 'OREB' and 'DREB' instantly gets added to 'TREB' <br/>
Each 'FG' and '3FG' gets added per player's 'PTS' column <br/>
Totals are instantly calculated in the last row<br/>
