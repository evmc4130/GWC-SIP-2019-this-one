# friendsAndFam = {"mom1":54,"mom2":45,"dad1":58,"dad2":56,"Brian":28,"Travis":27,"Jeffrey":25,"Khadima":12, "Aissatou":15, "Mareme":1,"Etta":16,"Connie":19}
#
# friendsAndFam["Nicole"] = {"I":17.5,"M":17}
#
#
# print(friendsAndFam["Nicole"]["I"])


#
# def survey():
#     a1 = input("what is your favorite color: ")
#     if type(a1) == str:
#         question1[a1]
#     print(question1)
#
# while True:
#     survey()





#
#
# answers_storage = []
#
# questions = ["What's your name? ", "What's your favorite color? ", "What was the most recent movie you watched? ", "Do you like pineapple on pizza? ", "How old are you? "]
# answer = {}
# while True:
#
#
#     for q in questions:
#         answer[q] = input(q)
#         answers_storage.append(answer)
#     print(answers_storage)
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


import json

def takesurvey(bananas, apples):
    answer = {}
    for q in bananas:
        answer[q] = input(q)
    apples.append(answer)



a = []
q = ["What's your name? ", "What's your favorite color? ", "What was the most recent movie you watched? ", "Do you like pineapple on pizza? ", "How old are you? "]

while (input("Take survey? enter BEGIN. If survey completed, enter DONE ").lower() == "begin"):
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    takesurvey(q,a)

f = open("survey.json", "w")
f.write(json.dumps(a))
f.close()
print(a)
