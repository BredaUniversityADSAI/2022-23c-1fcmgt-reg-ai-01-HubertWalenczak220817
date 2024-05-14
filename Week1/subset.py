

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

#print(get_verb_agent('train.json', agent_custom = ['n10288763', 'n10289039', 'n10289176', 'n10287213', 'n03716327', 'n10288516', 'n10788852', 'n10787470', 'n09900153', 'n02121620', 'n10023039', 'n02084071', 'n07644382', 'n01503061']))

import shutil

def img_to_folder(dirs_original, dirs_destination):
    image_list = get_verb_agent('train.json', agent_custom = ['n10288763', 'n10289039',
        'n10289176', 'n10287213', 'n03716327', 'n10288516', 'n10788852', 'n10787470',
        'n09900153', 'n02121620', 'n10023039', 'n02084071', 'n07644382', 'n01503061',
        'n10288763', 'n10289039', 'n10289176', 'n10287213', 'n03716327', 'n10288516',
        'n10788852', 'n10787470', 'n06326797', 'n00007846', 'n05217688', 'n07971141',
        'n07942152', 'n09918554', 'n09918762', 'n09918248', 'n09917593', 'n03538037',
        'n02374451', 'n10084295', 'n10285313'])[0]
    dirs_list = [(dirs_original, dirs_destination)]
    for img in image_list:
        for source_folder, destination_folder in dirs_list:
            shutil.copy(source_folder+img, destination_folder+img)

img_to_folder("./original/", "./train/")
