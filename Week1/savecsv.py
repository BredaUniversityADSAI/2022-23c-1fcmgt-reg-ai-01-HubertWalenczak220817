import pandas as pd
import json

def get_verb_agent(json_file,  agent_custom):
    train = json.load(open(json_file))
    verb_value = []
    agent_key = []
    agent_value = []
    file_path = []
    count = 0
    j = 0
    for i in train:
            j = j + 1
            print(str(j) + ' / ' + str(len(train)+1))
            verb = train[i]['verb']
            frames = train[i]['frames']
            for frame in frames:
                for key, value in frame.items():
                    if key == 'agent':
                        if value in agent_custom:
                            if i not in file_path:
                                agent_key.append(key)
                                agent_value.append(value)
                                file_path.append(i)
                                verb_value.append(verb)
                                count += 1
                        else:
                            continue
                    else:
                        continue
    return(file_path, verb_value, agent_key, agent_value, count)

def lists_to_df(dirs_destination, col1_name, col2_name, col3_name):
    col1 = get_verb_agent('train.json', agent_custom = ['n10288763', 'n10289039', 'n10289176', 'n10287213', 'n03716327', 'n10288516', 'n10788852', 'n10787470', 'n09900153', 'n02121620', 'n10023039', 'n02084071', 'n07644382', 'n01503061'])[0]
    col2 = get_verb_agent('train.json', agent_custom = ['n10288763', 'n10289039', 'n10289176', 'n10287213', 'n03716327', 'n10288516', 'n10788852', 'n10787470', 'n09900153', 'n02121620', 'n10023039', 'n02084071', 'n07644382', 'n01503061'])[1]
    col3 = get_verb_agent('train.json', agent_custom = ['n10288763', 'n10289039', 'n10289176', 'n10287213', 'n03716327', 'n10288516', 'n10788852', 'n10787470', 'n09900153', 'n02121620', 'n10023039', 'n02084071', 'n07644382', 'n01503061'])[3]
    df = pd.DataFrame(list(zip(col1, col2, col3)), columns=[col1_name, col2_name, col3_name])
    df.to_csv(dirs_destination, index=False)
    return df

lists_to_df('./train/train.csv', 'file_name','verb', 'agent')

