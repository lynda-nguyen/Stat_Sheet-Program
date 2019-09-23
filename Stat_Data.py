import datetime
import config
import pandas as pd

def dateInput():
    isValid = False
    retDateTime = None
    while not isValid:
        print("Please start by recording the date in the format mm/dd/yyyy:")
        date = input("Please type the film date: ")
        try:
            month,day,year = date.split('/')
            retDateTime = datetime.datetime(int(year), int(month), int(day))
            isValid = True
        except ValueError:
            print("Date was not in valid format!")
            isValid = False
    return retDateTime

def menu():
    print("----------------------------------------------------------------")
    print("Select one of the following options by typing the number of the command or help to see the options again:")
    print(" 1. See Table \n 2. Export Data \n 3. Record More Data (Go back) \n 4. Look Up Team \n 5. Look Up Actions"
    "\n 6. Change Date \n -- To exit entire program type 'exit' --")
    print("----------------------------------------------------------------")

def initializeDataframe(dateTime):
    try:
        date_time = dateTime.strftime("%m-%d-%Y") + '.csv'
        df = pd.read_csv(date_time, index_col=0)
    except FileNotFoundError:
        return pd.DataFrame(columns=config.action_list, index = config.players_list + ['Total']).fillna(0)
    return df

def displayDataframe(df):
    print(df)

def exportData(df, date):
    date_time = date.strftime("%m-%d-%Y") + '.csv'
    print("EXPORTING DATA to " + date_time)
    df.to_csv(r'./' + date_time)

def recordData(df):
    print("Type 'back' to return back to the menu at anytime ")
    def inputInitials():
        initials = input("Please input the players initials: ").upper()
        while initials not in config.players_list and (initials != 'BACK' and initials != 'EXIT'):
            print("There appears to be a typo please try again")
            print(initials)
            initials = input("Please input the players initials: \n").upper()
        return initials
    def inputActions():
        action = input("Please input the players action: ").upper()
        while action not in config.action_list and (action != 'BACK' and action != 'EXIT'):
            print("There appears to be a typo please try again")
            print(action)
            action = input("Please input the players action: \n").upper().replace(' ', "").replace('_', '')
        return action
    initials = ' '
    actions = ' '
    while(initials and actions):
        initials = inputInitials()
        if(initials == 'BACK' or initials == 'EXIT'):
            return initials
        actions = inputActions()
        if(actions == 'BACK' or initials == 'EXIT'):
            return actions
        if(actions == 'FG'):
            df.loc[initials, 'PTS']+=2
            df.loc[initials, 'FGA']+=1
        if(actions == '3FG'):
            df.loc[initials, 'PTS']+=3
            df.loc[initials, '3FGA']+=1
        if(actions == 'FT'):
            df.loc[initials, 'FTA']+=1
            df.loc[initials, 'PTS']+=1
        if(actions == 'OREB' or actions == 'DREB'):
            df.loc[initials, 'TREB']+=1

        df.loc[initials, actions]+=1
        df.loc['Total'] = df.loc[df.index != 'Total'].sum()
def lookUpTeam(df):
    print(config.players_list)

def lookUpActions(df):
    print(config.action_list)

def main():
    print("Hello, VT Women's Basketball.")
    print("\nStart by recording the date.")
    dateTime = dateInput()
    df = initializeDataframe(dateTime)
    command = 'help'
    commandOptions = [displayDataframe, exportData, recordData, lookUpTeam, lookUpActions]
    while command.lower() != 'quit' and command.lower() != 'exit':
        print(command)
        if(command.lower() == 'help'):
            menu()
        elif(command.isnumeric()):
            commandNum = int(command)
            if(commandNum == 6):
                dateTime = dateInput()
            elif(commandNum == 2):
                exportData(df, dateTime)
                return
            else:
                ret = commandOptions[commandNum - 1](df)
                if(ret == 'EXIT'):
                    return
                elif (ret == 'BACK'):
                    menu()
        else:
            print('There appears to be a typo, please try again.')
            menu()
        command = input('Please type a command: ')
    exportData(df, dateTime)
if __name__ == "__main__":
    main()
