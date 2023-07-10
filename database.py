import sqlite3


# def insert_into_user_info(first_name, last_name, username):
#     connection = sqlite3.connect("Country_trivia")
#     game_results = connection.cursor()
  
#     row_list = (first_name, last_name, username)
  
#     game_results.execute("insert into user_info values (?,?,?)", row_list)
#     connection.commit()
#     connection.close


# def insert_into_results(username, country, level, correct, incorrect, percentage):
#   connection = sqlite3.connect("Country_trivia")
#   game_results = connection.cursor()
  
#   row_list = (username, country, level, correct, incorrect, percentage)
  
#   game_results.execute("insert into game_results values (?,?,?,?,?,?)", row_list)
#   connection.commit()
#   for row in game_results.execute("select * from game_result"):
#     print(row)
#   connection.close

# def top_three_scores(username, name, level, correct, incorrect, percentage):
#     SELECT username, name, level, correct, incorrect, percentage
#     FROM game_result
#     WHERE country_name = name AND level = 'YourLevel'
#     ORDER BY percentage DESC
#     LIMIT 3;

# connection = sqlite3.connect("Country_trivia")
# game_results = connection.cursor()
# game_results.execute("create table user_info (first_name text, last_name text, username text, country text, level text, correct integer, incorrect integer, percentage)")

# connection.close

connection = sqlite3.connect("Country_trivia")
game_results = connection.cursor()
game_results.execute("create table game_results (username text, country text, level text, correct integer, incorrect integer, percentage)")

connection.close