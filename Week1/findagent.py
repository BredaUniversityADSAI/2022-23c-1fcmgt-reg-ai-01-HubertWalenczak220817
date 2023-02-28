

import json

# load imsitu_space.json file
imsitu_space = json.load(open("./imsitu_space.json"))

nouns = imsitu_space["nouns"]
verbs = imsitu_space["verbs"]

# function to get all agent codes for a specific agent/noun
def get_agent_codes(agent = "person"):
    for noun in nouns:
        if nouns[noun]['gloss'][0] == agent:
            print(f"{agent} found")
            print(noun)

# get all agent codes for men (use your own nouns here)
get_agent_codes("man")
get_agent_codes("woman")
get_agent_codes("human")
get_agent_codes("person")
get_agent_codes("people")
get_agent_codes("child")
get_agent_codes("horse")
get_agent_codes("female child")
get_agent_codes("male child")
print("----------------------")
get_agent_codes("cat")
get_agent_codes("dog")
get_agent_codes("bird")


