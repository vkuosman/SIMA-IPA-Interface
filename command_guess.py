import numpy as np

# Once the list of commands, functions etc are finalized the hardcoded matrices should be moved to seperate files
# and the command executions should be done using dictionary switches.

lights_matrix = np.array([['laita', 'laiton', "laatta", 'laidan', 'lataa', 'aita'], ['valo', 'valot', 'palo', 'palot', 'palat', 'valkoinen'], ['päälle', 'päällä', 'täällä', 'tällä', 'pälli']])

music_matrix = np.array([['soita', 'soitin', 'soitan'], ['musiikkia', 'musiikki', 'musiikin']])

fire_matrix = np.array([['takka', 'taka']])

reminder_matrix = np.array([['muistutus', 'muistuta', 'murskata']])

toggle_matrix = np.array([['katkaisin', 'katkaise', 'kataisen', 'katainen']])

feeling_bot_matrix = np.array([['kuinka', 'kuka', 'kuikka'], ['sinä', 'sä', 'sie', 'nää', 'sieni', 'sää', 'sievä'], ['voit', 'voi', 'voin', 'koit', 'loit']])

feeling_me_matrix = np.array([['minä', 'mä', 'mää', 'mie'], ['voi', 'voin',], ['hyvin', 'hyvitä', 'hyvinä', 'hyvä']])

time_ask_matrix = np.array([['paljonko', 'paljon', 'palin', 'alan'], ['kokeella', 'kello', 'kelo', 'kiellon' 'kokeella', "kokeillaan", "kokeilla", 'kokeilu'], ['on']])

meaning_ask_matrix = np.array([['mikä', 'minkä'], ['on'], ['elämän', 'eläimen'], ['tarkoitus']])

news_matrix = np.array([['uutiset', 'uutisia', 'uutisen', "uutisissa"]])

name_ask_matrix = np.array([['mikä', 'miksi'], ['sinun', 'siun', 'sun'], ['nimesi', 'nimi']])

red_light_matrix = np.array([['valo', 'valot', 'palo', 'palot', 'palat'], ['punainen', "punaisiksi", 'punaiseksi', 'punertava', 'punertavaksi']])

blue_light_matrix = np.array([['valo', 'valot', 'palo', 'palot', 'palat'], ['sininen', "sinisiksi", 'siniseksi', 'sinertävä', 'sinertäviksi']])

green_light_matrix = np.array([['valo', 'valot', 'palo', 'palot', 'palat'], ['vihreä', "vihreiksi", 'vihreäksi', 'vihertävä', 'vihertäviksi']])

violet_light_matrix = np.array([['valo', 'valot', 'palo', 'palot', 'palat'], ['violetti', "violeteiksi", 'violetiksi', 'violetissa']])

say_command_matrix = np.array([['sano', 'sana', 'sanat', 'sanot', 'sanoit', 'sanoi', 'sanoa', 'sanomiin']])

introduction_matrix = np.array([['minun', 'mun'], ['nimi', 'nimeni'], ['on', 'olen', 'kovan']])

search_matrix = np.array([['mikä', 'mitä', 'kuka', 'kukka', 'kukaan', 'keitä', 'ketkä', 'mitkä', 'paljonko', 'milloin'], ['on', 'ovat']])

demo_matrix = np.array([['aloita'], ['esittely', 'esitellytila'], ['nyt']])

command_dict = {
    -3: "search_information",
    -2: "introduction",
    -1: "say_command",
    0: "null_case",
    1: "light",
    2: "music",
    3: "fire",
    4: "reminder",
    5: "toggle",
    6:"feeling",
    7: "feeling_me",
    8: "time_ask",
    9: "meaning_ask",
    10: "news_default",
    11: "name_ask",
    12: "red_light",
    13: "blue_light",
    14: "green_light",
    15: "violet_light",
    16: "demo_start"
}

complete_array = np.array([lights_matrix, 
music_matrix, 
fire_matrix, 
reminder_matrix, 
toggle_matrix, 
feeling_bot_matrix, 
feeling_me_matrix, 
time_ask_matrix, 
meaning_ask_matrix,
news_matrix,
name_ask_matrix,
red_light_matrix,
blue_light_matrix,
green_light_matrix,
violet_light_matrix,
demo_matrix])

# Most likely nonoptimal in the long run. Consider updating.
def question_pre_check(sentence_string):
    input_list = sentence_string.split()
    # Checking for repeat command.
    if input_list[0] in say_command_matrix:
        return sentence_string.lstrip(input_list[0])
    # Checking for introduction command.
    elif input_list[0] in introduction_matrix[0]:
        if input_list[1] in introduction_matrix[1]:
            if input_list[2] in introduction_matrix[2]:
                fixed_list = input_list
                del fixed_list[0:3]
                sentence_string = " ".join(fixed_list)
                return sentence_string
            else:
                fixed_list = input_list
                del fixed_list[0:2]
                sentence_string = " ".join(fixed_list)
                return sentence_string
    elif input_list[0] in introduction_matrix[1][1] and len(input_list) > 1:
        if input_list[1] in introduction_matrix[2]:
            fixed_list = input_list
            del fixed_list[0:2]
            sentence_string = " ".join(fixed_list)
            return sentence_string
        else:
            fixed_list = input_list
            del fixed_list[0:1]
            sentence_string = " ".join(fixed_list)
            return sentence_string
    # Checking for search
    elif input_list[0] in search_matrix[0] and len(input_list) > 1:
        if input_list[0] == search_matrix[0][4]:
            fixed_list = input_list
            del fixed_list[0:1]
            sentence_string = " ".join(fixed_list)
            return sentence_string
        elif input_list[1] in search_matrix[1]:
            fixed_list = input_list
            del fixed_list[0:2]
            sentence_string = " ".join(fixed_list)
            return sentence_string
        else:
            return "false"
    else:
        return "false"

# Current implementation is able to compensate for some cases of needless repetition but may still not be optimal.
def check_score(sentence_string):
    input_list = sentence_string.split()
    score_list = []
    # Implementing WER caused IndexErrors with blank inputs. Temporary fix.
    if sentence_string:
        check_sentence = question_pre_check(sentence_string)
    else:
        check_sentence = "false"
        
    if check_sentence != "false":

        # Change to dictionary "switch". Currently redoing checks for no practical reason.
        if input_list[0] in say_command_matrix:
            return command_dict[-1], check_sentence
        elif input_list[0] in introduction_matrix[0]:
            return command_dict[-2], check_sentence
        elif input_list[0] in introduction_matrix[1][1]:
            return command_dict[-2], check_sentence
        elif input_list[0] in search_matrix[0]:
            return command_dict[-3], check_sentence

    for matrix in complete_array:
        score = 0.0
        perma_num = matrix.shape
        for word in input_list:
            num_rows = matrix.shape
            i = 0
            loop_num = num_rows[0]
            while i < loop_num:
                if word in matrix[i]:
                    matrix = np.delete(matrix, i, 0)
                    loop_num -= 1
                    score += 1
                else:
                    i += 1
        # Making sure that single correct word will not triggger a multi-word command
        if score == 1 and perma_num[0] != 1:
            score = 0

        score_list.append(score/perma_num[0])
    highest_index = score_list.index(max(score_list))
    
    # This is can be deleted after checking for failures
    if (score_list.count(max(score_list)) != 1 and max(score_list) > 0):
        print("\nSCORING FAILED\n")
    if (max(score_list) > 0 and score_list.count(max(score_list)) == 1):
        return command_dict[highest_index + 1]
    else:
        return command_dict[0]
