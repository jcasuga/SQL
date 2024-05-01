import psycopg2

# CS 457 Final Project
# Coded by Justin Casuga

def connect():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def get_info(game, choice):
    conn = None
    output = " "
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        input = " "
        if choice == '1':
            input = "select gameid from game where game_name = \'%s\'" % (game)
        elif choice == '2':
            input = "select distinct genreid from genre where genre_name = \'%s\'" % (game)
        elif choice == '4':
            input = "select publisherid from publisher where publishername = \'%s\'" % (game)
        elif choice == '5':
            input = "select platformid from platform where platformname = \'%s\'" % (game)
        cur.execute(input)
        row = cur.fetchone()
        output = row

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
    return output

def get_game_sales(gameID, region):
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        if region == '1':
            input = "select n_sales from game e full outer join region_sales f on e.gameid = f.game_id where e.gameid = \'%s\' " % (gameID)
        elif region == '2':
            input = "select e_sales from game e full outer join region_sales f on e.gameid = f.game_id where e.gameid = \'%s\' " % (gameID)
        elif region == '3':
            input = "select j_sales from game e full outer join region_sales f on e.gameid = f.game_id where e.gameid = \'%s\' " % (gameID)
        elif region == '4':
            input = "select g_sales from game e full outer join region_sales f on e.gameid = f.game_id where e.gameid = \'%s\' " % (gameID)
        cur.execute(input)
        row = cur.fetchone()
        output = row
        if cur.rowcount > 0:
            print("Values represent millions, ie 1.0 = 1 million")
            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        else:
            print("Nothing found")
            cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
def get_genre_sales(genreID, region):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        if region == '1':
            input = "select n_sales from genre e full outer join game d on e.genreid = d.genreid full outer join region_sales f on d.gameid = f.game_id where e.genreid = \'%s\' " % (genreID)
        elif region == '2':
            input = "select e_sales from genre e full outer join game d on e.genreid = d.genreid full outer join region_sales f on d.gameid = f.game_id where e.genreid = \'%s\' " % (genreID)
        elif region == '3':
            input = "select j_sales from genre e full outer join game d on e.genreid = d.genreid full outer join region_sales f on d.gameid = f.game_id where e.genreid = \'%s\'" % (genreID)
        elif region == '4':
            input = "select g_sales from genre e full outer join game d on e.genreid = d.genreid full outer join region_sales f on d.gameid = f.game_id where e.genreid = \'%s\'" % (genreID)
        cur.execute(input)
        row = cur.fetchone()
        output = row
        if cur.rowcount > 0:
            print("Values represent millions, ie 1.0 = 1 million")
            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        else:
            print("Nothing found")
            cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_year_sales(year, region):
    
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        if region == '1':
            input = "select n_sales from game_platform e full outer join game d on e.gamesid = d.gameid full outer join region_sales f on d.gameid = f.game_id where e.release_year = \'%s\'" % (year)
        elif region == '2':
            input = "select e_sales from game_platform e full outer join game d on e.gamesid = d.gameid full outer join region_sales f on d.gameid = f.game_id where e.release_year = \'%s\'" % (year)
        elif region == '3':
            input = "select j_sales from game_platform e full outer join game d on e.gamesid = d.gameid full outer join region_sales f on d.gameid = f.game_id where e.release_year = \'%s\'" % (year)
        elif region == '4':
            input = "select g_sales from game_platform e full outer join game d on e.gamesid = d.gameid full outer join region_sales f on d.gameid = f.game_id where e.release_year = \'%s\'" % (year)
        cur.execute(input)
        row = cur.fetchone()
        output = row
        if cur.rowcount > 0:
            print("Values represent millions, ie 1.0 = 1 million")
            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        else:
            print("Nothing found")
            cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_publisher_sales(year, region):
    
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        if region == '1':
            input = "select n_sales from publisher e full outer join game_publisher d on e.publisherid = d.publisherid full outer join region_sales f on d.gameid = f.game_id where e.publisherid = \'%s\'" % (year)
        elif region == '2':
            input = "select e_sales from publisher e full outer join game_publisher d on e.publisherid = d.publisherid full outer join region_sales f on d.gameid = f.game_id where e.publisherid = \'%s\'" % (year)
        elif region == '3':
            input = "select j_sales from publisher e full outer join game_publisher d on e.publisherid = d.publisherid full outer join region_sales f on d.gameid = f.game_id where e.publisherid = \'%s\'" % (year)
        elif region == '4':
            input = "select g_sales from publisher e full outer join game_publisher d on e.publisherid = d.publisherid full outer join region_sales f on d.gameid = f.game_id where e.publisherid = \'%s\'" % (year)
        cur.execute(input)
        row = cur.fetchone()
        output = row
        if cur.rowcount > 0:
            print("Values represent millions, ie 1.0 = 1 million")
            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        else:
            print("Nothing found")
            cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_platform_sales(platform, region):
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="videogames", user="postgres", password="tumbagA@101601")
        cur = conn.cursor()
        if region == '1':
            input = "select n_sales from platform e full outer join game_platform d on e.platformid = d.platform_id full outer join region_sales f on d.gamesid = f.game_id where e.platformid = \'%s\'" % (platform)
        elif region == '2':
            input = "select e_sales from platform e full outer join game_platform d on e.platformid = d.platform_id full outer join region_sales f on d.gamesid = f.game_id where e.platformid = \'%s\'" % (platform)
        elif region == '3':
            input = "select j_sales from platform e full outer join game_platform d on e.platformid = d.platform_id full outer join region_sales f on d.gamesid = f.game_id where e.platformid = \'%s\'" % (platform)
        elif region == '4':
            input = "select g_sales from platform e full outer join game_platform d on e.platformid = d.platform_id full outer join region_sales f on d.gamesid = f.game_id where e.platformid = \'%s\'" % (platform)
        cur.execute(input)
        row = cur.fetchone()
        output = row
        if cur.rowcount > 0:
            print("Values represent millions, ie 1.0 = 1 million")
            while row is not None:
                print(row)
                row = cur.fetchone()

            cur.close()
        else:
            print("Nothing found")
            cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

def get_user_input():
    print("Welcome to the Video Game Database!")
    print("Gather information about video game sales")
    print("1) Specific game sales")
    print("2) Specific genre sales")
    print("3) Specific year sales")
    print("4) Specific publisher game sales")
    print("5) Specific platform game sales")
    print("6) Exit")
    x = input("Please select an option: ")
    
    return x


if __name__ == '__main__':

    x = get_user_input()

    while (x != '6'):
        if x == '1':
            user = input("Please enter game name: ")
            gameID = get_info(user, x)
            print("Would you like to see specific region sales, or global sales?")
            choice = input("Choose region or global: ")
            choice.lower

            if choice == 'region':
                print("Which region?")
                print("1) North America")
                print("2) Europe")
                print("3) Japan")
                region = input("Please choose an option: ")

                get_game_sales(gameID, region)
            else:
                region = '4'
                get_game_sales(gameID, region)

        elif x == '2':
            print("Genres Included")
            
            print("1) Adventure")
            print("2) Puzzle")
            print("3) Strategy")
            print("4) Role-Playing")
            print("5) Simulation")
            print("6) Fighting")
            print("7) Racing")
            print("8) Sports")
            print("9) Action")
            print("10) Shooter")
            print("11) Platform")
            print("12) Misc")
            user = input("Please type a genre name: ")
            genreID = get_info(user, x)
            print("Would you like to see specific region sales, or global sales?")
            choice = input("Choose region or global: ")
            choice.lower 

            if choice == 'region':
                print("Which region?")
                print("1) North America")
                print("2) Europe")
                print("3) Japan")
                region = input("Please choose an option: ")

                get_genre_sales(genreID, region)
            else:
                region = '4'
                get_genre_sales(genreID, region)
        
        elif x == '3':
            user = input("Please enter the year: ")
            print("Would you like to see specific region sales, or global sales?")
            choice = input("Choose region or global: ")
            choice.lower

            if choice == 'region':
                print("Which region?")
                print("1) North America")
                print("2) Europe")
                print("3) Japan")
                region = input("Please choose an option: ")

                get_year_sales(user, region)
            else:
                region = '4'
                get_year_sales(user, region)
            
        elif x == '4':
            user = input("Please enter a publisher name: ")
            publisherID = get_info(user, x)
            print("Would you like to see specific region sales, or global sales?")
            choice = input("Choose region or global: ")
            choice.lower

            if choice == 'region':
                print("Which region?")
                print("1) North America")
                print("2) Europe")
                print("3) Japan")
                region = input("Please choose an option: ")

                get_publisher_sales(publisherID, region)
            else:
                region = '4'
                get_publisher_sales(publisherID, region)

        elif x == '5':
            user = input("Please enter a platform: ")
            platformID = get_info(user, x)
            print("Would you like to see specific region sales, or global sales?")
            choice = input("Choose region or global: ")
            choice.lower

            if choice == 'region':
                print("Which region?")
                print("1) North America")
                print("2) Europe")
                print("3) Japan")
                region = input("Please choose an option: ")

                get_platform_sales(platformID, region)
            else:
                region = '4'
                get_platform_sales(platformID, region)

        x = get_user_input()
                



