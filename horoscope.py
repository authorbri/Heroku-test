# import random

# times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
# advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
# promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
#             "неожиданного праздника", "приятных перемен"]


# def generate_prophecies(total_num=5, num_sentences=3):
#     prophecies = []

#     i = 0
#     while i < total_num:
#         j = 0
#         forecast = ""
#         while j < num_sentences:
#             t = random.choice(times)
#             a = random.choice(advices)
#             p = random.choice(promises)

#             full_sentence = t.title() + " " + a + " " + p + "."
#             if j != num_sentences - 1:
#                 full_sentence = full_sentence + " "

#             forecast = forecast + full_sentence
#             j = j + 1

#         prophecies.append(forecast)
#         i = i + 1

#     return prophecies

import random

times = ["утром", "днем", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=6, num_sentences=2):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies


#Пытался понять можно ли в команде "return" давать распоряжения типа for  и тд. Так не сработало...

# prophecies = []
# prophecies = generate_prophecies()

# print(len(prophecies))
# for j in range(len(prophecies)):
#     print (prophecies[j])

# def test():

#     prophecies = []
#     prophecies = generate_prophecies()
#     return {
#         "predictions": [
#         for k in range(len(prophecies)):
#         prophecies[k],
#         ],
#       }