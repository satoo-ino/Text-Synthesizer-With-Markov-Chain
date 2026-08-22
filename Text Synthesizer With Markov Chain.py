import os
import random
import time

os.system("")
print("mode 1: predicts the next word from single-word history, then refines it using word-pair history (starts from a one-word prompt).")
print("mode 2: predicts the next word using only word-pair history (starts from a two-word prompt).")
modo = input("mode (1 or 2): ")


with open("input.txt", "r", encoding="UTF-8") as file:
    input_text = file.read()

#word_list = input_text.replace("\n",' ').split(" ")


clean_up_clean_up = [("."," ."),(","," ,"),("?"," ? "),("!"," ! "),('"',' '),("\r"," "),("\n"," "),("  "," "),("    "," "),("   "," "),]
clean_up_after = [("."," ."),(","," ,"),("?"," ? "),("!"," ! ")]

for this,forthis in clean_up_clean_up:
    input_text = input_text.replace(this,forthis)
    #print(this,forthis)
print("-----------------------------------------------------------------------------------")

word_list = input_text.replace("\n",' ').lower().split(" ")

#print(input_text)
#input()


prediction_table = {}

#print(word_list)


for word_number in range(len(word_list)):
    
    current_word = word_list[word_number]
    try:
        next_word = word_list[word_number + 1]
    except:
        pass
    
    if (current_word in prediction_table.keys()) == False:   
        prediction_table.update({current_word: {next_word: 1}})  
    
    elif (next_word in prediction_table[current_word].keys()) == False:
        prediction_table[current_word].update({next_word: 1})
        
    else:
        prediction_table[current_word][next_word] += 1
    

    if word_number % 500 == 0:
        print("(1/4)Building word dictionary:", word_number,"/", len(word_list),f"{current_word[:10]}                    ",end='\r')
#print(prediction_table)
print("(1/4)Building word dictionary:", word_number+1,"/", len(word_list),f"{current_word[:10]}                        ",end='\r')
print()

ordered_p_table = {}
print_speed_fix = 0
for word,prediction in prediction_table.items():
        
    biggest = 0
    for pred_word, count in prediction.items():
        if count >= biggest:
            biggest = count
   
    print_speed_fix += 1
    for x in range(biggest+1):
        for pred_word, count in prediction.items():
            if x == count:
               if (word in ordered_p_table.keys()) == False:
                   ordered_p_table.update({word: {x: [pred_word]}  })
                   
               elif (x in ordered_p_table[word].keys()) == False:
                   ordered_p_table[word].update({x: [pred_word]})
               else:
                   ordered_p_table[word][x].append(pred_word)
                   #print("sdfgsdfgsdfg")
    
        if (x % 100 == 0) and (print_speed_fix % 100 == 0):
            print("(2/4)Building word connections:", x,"/",biggest,"  ",word[:10],"<-->",pred_word[:10],"                ",end='\r')
    if (print_speed_fix % 300 == 0):
        print("(2/4)Building word connections:", x,"/",biggest,"  ",word[:10],"<-->",pred_word[:10],"               ",end='\r')


print()

pair_prediction_table = {}

for w in range((len(word_list))-2):
    first = word_list[w]
    second = word_list[w+1]
    third = word_list[w+2]
    #print(first,second,third)
    
    word_pair = first + " " + second
    pair_pred = third
    
    

    if  (word_pair in pair_prediction_table.keys()) == False:
        pair_prediction_table.update({word_pair: {pair_pred: 1}})
    
    elif (pair_pred in pair_prediction_table[word_pair].keys()) == False:
        pair_prediction_table[word_pair].update({pair_pred: 1})
    
    else:
        pair_prediction_table[word_pair][pair_pred] += 1
        
    if w % 500 == 0:
        print("(3/4)Building word-pair dictionary:", w,"/", len(word_list),f"{word_pair[:10]}               ",end='\r')
print("(3/4)Building word-pair dictionary:", w,"/", len(word_list)+3,f"{word_pair[:10]}               ",end='\r')

print()

print_speed_fix = 0
ordered_pair_p_table = {}

for word_pair, pair_pred in pair_prediction_table.items():
    
    biggest = 0
    for word,number in pair_pred.items():
        if biggest <= number:
            biggest = number

    
    print_speed_fix += 1
    for x in range(biggest+1):
        
        for word,number in pair_pred.items():
            if x == number:
                
                
                
                if (word_pair in ordered_pair_p_table.keys()) == False:
                    ordered_pair_p_table.update({word_pair:{number: [word]}})
                
                elif (x in ordered_pair_p_table[word_pair]) == False:
                    ordered_pair_p_table[word_pair].update({x: [word]})
                
                else:
                    ordered_pair_p_table[word_pair][x].append(word)
                
        if (x % 100 == 0) and (print_speed_fix % 100 == 0):
            print("(4/4)Building word-pair connections:", x,"/",biggest,"  ",word_pair[:10],"<-->",word[:10],"                    ",end='\r')
    if (print_speed_fix % 100 == 0):
        print("(4/4)Building word-pair connections:", x,"/",biggest,"  ",word_pair[:10],"<-->",word[:10],"                      ",end='\r')
print()
    
    


# IF ACTIVATED, IT SHOWS THE CONNECTIONS BETWEEN THE WORDS

# if modo == "1":

    #########################################################################################

    # for print_helper in ordered_p_table.keys():
        # print(f" \033[38;2;255;100;255m{print_helper}\033[0m",r'---->   ', end=' ')
        # for kuk,kik in ordered_p_table[print_helper].items():
            # print(f"\033[38;2;255;255;100m{f"weight {kuk}:"}\033[0m",r'{ ', end='')
            # for palava in kik:
                # print(f"\033[38;2;100;255;255m{palava}\033[0m", end=' ')
            # print(f"{r'}'}     ", end='')        
        # print()

    ##########################################################################################

# if modo == "2":
    #########################################################################################

    # for print_helper in ordered_pair_p_table.keys():
        # print(f" \033[38;2;255;100;255m{print_helper}\033[0m",r'---->   ', end=' ')
        # for kuk,kik in ordered_pair_p_table[print_helper].items():
            # print(f"\033[38;2;255;255;100m{f"weight {kuk}:"}\033[0m",r'{ ', end='')
            # for palava in kik:
                # print(f"\033[38;2;100;255;255m{palava}\033[0m", end=' ')
            # print(f"{r'}'}     ", end='')        
        # print()

    ##########################################################################################
print()
print("TRAINING COMPLETE!")

print("-----------------------------------------------------------------------------------")


if modo == "1":
    while True:
        print()
        print()
        first_word = input('Prompt (one word): ').lower()
        skip_line = 0
        try:
            while True: 
                pick_one_from_here = []
                
                for count,word_list in ordered_p_table[first_word].items():
                    for word in word_list:
                        for x in range(count):
                            pick_one_from_here.append(word)
                #print(pick_one_from_here)

                second_word = pick_one_from_here[(random.randint(0,(len(pick_one_from_here)-1)))]

                #print("first method:",first_word, "----->",second_word)
                #input()
                
                if (first_word == "<|endoftext|>") or (second_word == "<|endoftext|>"):
                    break
                
                pair_first_second = first_word + " " + second_word
                
                
                
                
                pick_one_from_here = []
                
                for count,word_list in ordered_pair_p_table[pair_first_second].items():
                    for word in word_list:
                        for x in range(count):
                            pick_one_from_here.append(word)
                #print(pick_one_from_here)            
                
                third_word = pick_one_from_here[(random.randint(0,(len(pick_one_from_here)-1)))]
                
                #input()
                #print("second method:",first_word,second_word,f'||{pair_first_second}||',"------>",third_word)
                
                
                skip_line += len((first_word+ " "+ second_word)) +1
                if skip_line >= 110:
                    print()
                    skip_line = 0
                
                for char in first_word+ " "+ second_word:
                    print(f"\033[38;2;100;255;100m{char}\033[0m", end="", flush=True );time.sleep(0.01)
                print(end=' ')
                #input()
                

                
                first_word = third_word
        except:
            
            print()
            
            
            print(f"ERROR --> Type a word that appears in the training data. Here are some examples of word pairs (picked at random):")
            print(f"Prompt examples: {list(prediction_table.keys())[random.randint(0,len(list(prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(prediction_table.keys())[random.randint(0,len(list(prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(prediction_table.keys())[random.randint(0,len(list(prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(prediction_table.keys())[random.randint(0,len(list(prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(prediction_table.keys())[random.randint(0,len(list(prediction_table.keys()))-1)]}")
            pass
            
if modo == "2":
    
    while True:
        try:
            
            print()
            print()
            two_words = input('Prompt (two words): ').lower()
            skip_line = 0

            while True: 
                first_word = two_words.split(' ')[0]
                second_word = two_words.split(' ')[1]
                pair_first_second = first_word + " " + second_word
                #print(first_word,second_word)
                #input()
                
                if first_word == "<|endoftext|>":
                    break
                
                pick_one_from_here = []
                
                for count,word_list in ordered_pair_p_table[pair_first_second].items():
                    for word in word_list:
                        for x in range(count):
                            pick_one_from_here.append(word)
                #print(pick_one_from_here)            
                
                third_word = pick_one_from_here[(random.randint(0,(len(pick_one_from_here)-1)))]
                
                #input()
                #print("second method:",first_word,second_word,f'||{pair_first_second}||',"------>",third_word)
                
                
                
                
                skip_line += len(first_word) + 1
                if skip_line >= 110:
                    print()
                    skip_line = 0
                
                for char in first_word:
                    
                    
                    print(f"\033[38;2;100;255;100m{char}\033[0m", end="", flush=True );time.sleep(0.01)
                    
                    
                print(end=' ')
                #input()
                
                two_words = second_word + " " + third_word
        except:
            print()
            
            
            print(f"ERROR --> Type 2 words that appear in the training data. Here are some examples of word pairs (picked at random):")
            print(f"Prompt examples: {list(pair_prediction_table.keys())[random.randint(0,len(list(pair_prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(pair_prediction_table.keys())[random.randint(0,len(list(pair_prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(pair_prediction_table.keys())[random.randint(0,len(list(pair_prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(pair_prediction_table.keys())[random.randint(0,len(list(pair_prediction_table.keys()))-1)]}     -     " , end = '')
            print(f"{list(pair_prediction_table.keys())[random.randint(0,len(list(pair_prediction_table.keys()))-1)]}",end = '')
            
            pass
            