import datetime
import config 
import pandas as pd

def dateInput():
    isValid = False #bool var to check date format
    retDateTime = None #returns dateInput()

    while not isValid:
        #initial question
        print("-- Record date in mm/dd/yyyy. --")
        date = input("Type film date: ")
        # check date format; runs while loop until correct format
        try:
            month, day, year = date.split('/')
            retDateTime = datetime.datetime(int(year), int(month), int(day))
            isValid = True
        except ValueError:
            print("Date is not in the valid format!")
            isValid = False  
    return retDateTime

def menu():
    #displays the options in numerical order
    print("-------------------------------------------------------------------------------")
    print("Select one of the options by typing the number of the command. ")
    print("-- Or 'help' to see options again. --")
    print(" 1. See Table \n 2. Export Data \n 3. Record More Data (Go Back) \n 4. Look Up Team \n" 
    " 5. Look up Actions \n 6. Delete Action \n 7. Change Date \n -- To exit program type 'exit' anytime--")
    print("-------------------------------------------------------------------------------")

def initializeDataFrame(dateTime): 
    try: 
        date_time = dateTime.strftime("%m-%d-%y") + '.csv'
        df = pd.read_csv(date_time, index_col = 0)
    except: #
        return pd.DataFrame(columns = config.actions_list, \
            index = config.players_list + ['Total']).fillna(0)
    return df

def displayDataFrame(df):
    print(df)

def exportData(df, date):
    date_time = date.strftime("%m-%d-%y") + '.csv'
    print("EXPORTING DATA TO " + date_time)
    df.to_csv(r'./' + date_time)

def inputInitials(): #rows
    initials = input("Input player initials: ").upper()
    while initials not in config.players_list and \
        (initials != 'BACK' and initials != 'EXIT'): 
        print("Invalid player initials: " + initials)
        initials = input("Input player initials: ").upper()
    return initials
def inputActions(): #columns
    action = input("Input player action: ").upper()
    while action not in config.actions_list and \
        (action != 'BACK' and action != 'EXIT'):
        print("Invalid action: " + action) 
        action = input("Input player action: ").upper()
    return action

def recordData(df):
    print("-- Type 'back' to return back to the menu at anytime. --")
    
    initials = ' '
    action = ' '

    while (initials and action):
        initials = inputInitials()
        if (initials == 'BACK' or initials == 'EXIT'):
            return initials
        action = inputActions()
        if (action == 'BACK' or action == 'EXIT'): 
            return action
        # automatic additional features
        if (action == 'FG'):
            df.loc[initials, 'PTS']+=2
            df.loc[initials, 'FGA']+=1
        if (action == '3FG'):
            df.loc[initials, 'PTS']+=3
            df.loc[initials, '3FGA']+=1
        if (action == 'FT'):
            df.loc[initials, 'PTS']+=1
            df.loc[initials, 'FTA']+=1
        if (action == 'OREB' or action == 'DREB'):
            df.loc[initials, 'TREB']+=1

        df.loc[initials, action]+=1 #each action input
        df.loc['Total'] = df.loc[df.index != 'Total'].sum() #sums up the team columns

def lookUpTeam(df):
    print(config.players_list)

def lookUpActions(df):
    print(config.actions_list)

def deleteInput(df):
    print("-- Type player and action inputs to be DELETED. --")
    
    act = inputActions()
    if (act == 'BACK' or act == 'EXIT'): 
        return act 
    init = inputInitials()
    if (init == 'BACK' or init == 'EXIT'):
        return init 

    print("Are you sure you want to delete " + act + " for " + init)
    choice = input("Type y/n: ").lower()
    if (choice == "y"):
        if (act == 'FG'):
            df.loc[init, 'PTS']-=2
            df.loc[init, 'FGA']-=1
        if (act == '3FG'):
            df.loc[init, 'PTS']-=3
            df.loc[init, '3FGA']-=1
        if (act == 'FT'):
            df.loc[init, 'PTS']-=1
            df.loc[init, 'FTA']-=1
        if (act == 'OREB' or act == 'DREB'):
            df.loc[init, 'TREB']-=1

        df.loc[init, act]-=1 
        df.loc['Total'] = df.loc[df.index != 'Total'].sum()
    else:
        return

def main():
    print("-- Hello, VT Women's Basketball! --")
    print("\n-- Start by recording the date. This how the exported data will be saved as. --")
    dateTime = dateInput()
    df = initializeDataFrame(dateTime)
    command = 'help'
    commandOptions = [displayDataFrame, exportData, recordData, lookUpTeam, lookUpActions, deleteInput]

    while command.lower() != 'quit' and command.lower() != 'exit':
        #print(command)
        if(command.lower() == 'help'):
            menu()
        elif(command.isnumeric()):
            commandNum = int(command)
            if(commandNum == 7):
                dateTime = dateInput()
            elif(commandNum == 2):
                exportData(df, dateTime)
                return
            else:
                ret = commandOptions[commandNum - 1](df)
                if(ret == 'EXIT'):
                    return
                elif(ret == 'BACK'):
                    menu()
        else:
            print("-- There appears to be a type, please try again. --")
            menu()
        command = input('Please type a command: ')
    exportData(df, dateTime)
if __name__ == "__main__":
    main()

