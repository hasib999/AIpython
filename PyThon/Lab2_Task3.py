def vacuum_cleaner(list1):
    action = dict()
    for list in list1:
        if(list[1]=='clean'):
            if(list[0]=='loc_A'):
                action[list[0],list[1]]='Right'
            else:
                action[list[0],list[1]]='Left'
        elif(list[1]=='dirty'):
            action[list[0],list[1]]='Suck'
    return action

percept_sequence=[['loc_A', 'clean'],['loc_A','dirty'], ['loc_B', 'clean'],['loc_B','dirty']]
Action = ['Right', 'Suck', 'Left', 'Suck']

action_perform = vacuum_cleaner(percept_sequence)
print(action_perform)
