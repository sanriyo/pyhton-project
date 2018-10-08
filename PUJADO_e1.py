# filename    : Maria.e1.py
# author      : Maria Angelica Pujado
# description : char
message = "I am {}. \n" + \
        "My spirit animal is {}. \n" + \
        "because {}.\n" + \
        "When not in school, I love  {}.\n" + \
        "I dream of being a/an {} in the future."
data = {"name"          : "Maria",
        "spirit_animal" : "snake",
        "reason"        : "bet ko lang",
        "hobby"         : "sleeping",
        "profession"    : "Teacher"}
print (message.format(data["name"], \
       data["spirit_animal"], \
       data["reason"], \
       data["hobby"], \
       data["profession"]
       ))