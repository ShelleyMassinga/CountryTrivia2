import sqlite3


def insert_into_user_info(username):
    connection = sqlite3.connect("Country_trivia.db")
    cursor = connection.cursor()

    row_list = ([username])

    cursor.execute("insert into user_info values (?)", row_list)
    connection.commit()
    for row in cursor.execute("select * from user_info"):
        print(row)
    connection.close


def insert_into_results(username, country, level, correct, incorrect):
    connection = sqlite3.connect("Country_trivia.db")
    game_results = connection.cursor()

    row_list = ([username, country, level, correct, incorrect])

    game_results.execute(
        "insert into game_results values (?,?,?,?,?)", row_list)
    connection.commit()
    for row in game_results.execute("select * from game_results"):
        print(row)
    connection.close

def top_three_correct_answers(country, level):
    connection = sqlite3.connect("Country_trivia.db")
    game_results = connection.cursor()

    query = """
        SELECT username, correct
        FROM game_results
        WHERE country = ? AND level = ?
        ORDER BY correct DESC
        LIMIT 3
    """
    game_results.execute(query, (country, level))

    top_three_correct_answers = game_results.fetchall()
    connection.close()

    return top_three_correct_answers
connection = sqlite3.connect("Country_trivia.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_info (username TEXT)")

connection.commit()
connection.close

connection = sqlite3.connect("Country_trivia.db")
game_results = connection.cursor()
game_results.execute(
    "CREATE TABLE IF NOT EXISTS game_results (username TEXT, country TEXT, level TEXT, correct INTEGER, incorrect INTEGER)")

connection.close
