import random,data,art,os
all_list = data.data
def clear():
    os.system('clear')
print(art.logo)
def play():
    score_point = 0
    A = all_list[random.randint(0,49)]
    B = all_list[random.randint(0, 49)]
    if A == B:
        A = all_list[random.randint(0, 49)]
        B = all_list[random.randint(0, 49)]

    print(f" {A['name']} ,{A['description']}, from {A['country']}")
    print(art.vs)
    print(f" {B['name']} ,{B['description']}, from {B['country']}")
    player_answer = input("Who has more followers? Type 'A' or 'B': \n")
    answer_key = ""
    if A['follower_count'] > B['follower_count']:
        answer_key = "A"
    else:
        answer_key = "B"
    if answer_key == player_answer:
        score_point += 1
        print(f"You're right! Current score: {score_point}.")
        check = True
        clear()
        while check:

            print(art.logo)
            print(f"You're right! Current score: {score_point}.")
            A = B
            B = all_list[random.randint(0, 49)]
            if A == B:
                B = all_list[random.randint(0, 49)]
            print(f" {A['name']} ,{A['description']}, from {A['country']}")
            print(art.vs)
            print(f" {B['name']} ,{B['description']}, from {B['country']}")
            player_answer = input("Who has more followers? Type 'A' or 'B': \n")
            answer_key = ""
            if A['follower_count'] > B['follower_count']:
                answer_key = "A"
            else:
                answer_key = "B"

            if answer_key == player_answer:
                score_point += 1
                check = True
                clear()


            else:
                check = False

    else:
        print(f"Sorry, that's wrong. Final score: {score_point}.")


play()
