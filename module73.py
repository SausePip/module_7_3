team1_num = 5
# print(f'В команде Мастера кода участников: {team1_num}')

team2_num = 6
# print(f'Итого сегодня в командах участников: {team1_num} и {team2_num}')


score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

# Форматирование с использованием %
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

team_total_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(team_total_str)

# Форматирование с использованием format()
score_team2_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score_team2_str)

time_team2_str = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(time_team2_str)

# Форматирование с использованием f-строк
scores_str = f"Команды решили {score_1} и {score_2} задач."
print(scores_str)

result_str = f"Результат битвы: {challenge_result}"
print(result_str)

tasks_time_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_time_str)