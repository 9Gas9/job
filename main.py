import sqlite3
import random


def test_CREATE_Table_in_DB():
    connection = sqlite3.connect('mygame.db')  # Подключаемся к базе
    cursor = connection.cursor()

    # Проектируем запрос на создание таблицы, если таблица уже существует, пропустит.
    cursor.execute("""CREATE TABLE IF NOT EXISTS ships(
                      ship TEXT PRIMARY KEY, 
                      weapon TEXT, 
                      hull TEXT, 
                      engine TEXT)
                   """)
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS weapons(
                      weapon TEXT PRIMARY KEY, 
                      reload_speed INT, 
                      rotation_speed INT, 
                      diameter INT,
                      power_volley INT,
                      count INT)
                   """)
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS hulls(
                      hull TEXT PRIMARY KEY, 
                      armor INT, 
                      type INT, 
                      capacity INT)
                   """)
    connection.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS engines(
                      engine TEXT PRIMARY KEY, 
                      power INT, 
                      type INT)
                   """)
    connection.commit()

    cursor.close()
    connection.close()


test_CREATE_Table_in_DB()


def test_ADD_Engines_in_Table():
    print('#' * 40, "ENGINE====>")

    connection = sqlite3.connect('mygame.db')  # Подключаемся к базе
    cursor = connection.cursor()

    for i in range(6):
        engine_name = 'Engine-' + str(i + 1)
        engine_power = random.randint(1, 20)
        engine_type = random.randint(1, 20)

        print("name: ", engine_name,
              " / power: ", engine_power,
              " / type: ", engine_type)

        engine_set = [engine_name, engine_power, engine_type]

        engine_set_query = """ INSERT INTO {table} (engine, power, type)
                                    VALUES (?,?,?)"""
        try:
            cursor.execute(engine_set_query.format(table="engines"), engine_set)
        except sqlite3.IntegrityError as e:
            print("Запись была добавлена ранее: ", e)
        connection.commit()

    cursor.close()
    connection.close()


test_ADD_Engines_in_Table()


def test_ADD_Hulls_in_Table():
    print('#' * 40, "HULLS====>")
    connection = sqlite3.connect('mygame.db')  # Подключаемся к базе
    cursor = connection.cursor()
    for i in range(5):
        hull_name = 'Hull-' + str(i + 1)
        hull_armor = random.randint(1, 20)
        hull_type = random.randint(1, 20)
        hull_capacity = random.randint(1, 20)

        print("name: ", hull_name,
              " / armor: ", hull_armor,
              " / type: ", hull_type,
              " / capacity: ", hull_capacity)

        hull_set = [hull_name, hull_armor, hull_type, hull_capacity]

        hull_set_query = """ INSERT INTO {table} (hull, armor, type, capacity)
                                    VALUES (?,?,?,?)"""
        try:
            cursor.execute(hull_set_query.format(table="hulls"), hull_set)
        except sqlite3.IntegrityError as e:
            print("Запись была добавлена ранее: ", e)
        connection.commit()

    cursor.close()
    connection.close()


test_ADD_Hulls_in_Table()


def test_ADD_Weapons_in_Table():
    print('#' * 40, "WEAPONS====>")

    connection = sqlite3.connect('mygame.db')  # Подключаемся к базе
    cursor = connection.cursor()

    for i in range(20):
        weapon_name = 'Weapon-' + str(i + 1)
        weapon_reload_speed = random.randint(1, 20)
        weapon_rotation_speed = random.randint(1, 20)
        weapon_diameter = random.randint(1, 20)
        weapon_power_volley = random.randint(1, 20)
        weapon_count = random.randint(1, 20)

        print("name: ", weapon_name,
              " / reload: ", weapon_reload_speed,
              " / rotation: ", weapon_rotation_speed,
              " / diameter: ", weapon_diameter,
              " / power: ", weapon_power_volley,
              " / count ", weapon_count)

        weapon_set = [weapon_name, weapon_reload_speed, weapon_rotation_speed, weapon_diameter,
                      weapon_power_volley, weapon_count]

        weapon_set_query = """ INSERT INTO {table} (weapon, reload_speed, rotation_speed, 
                                                    diameter, power_volley, count)
                                    VALUES (?,?,?,?,?,?)"""
        try:
            cursor.execute(weapon_set_query.format(table="weapons"), weapon_set)
        except sqlite3.IntegrityError as e:
            print("Запись была добавлена ранее: ", e)
        connection.commit()

    cursor.close()
    connection.close()


test_ADD_Weapons_in_Table()



def test_ADD_Ships_in_Table():
    print('#' * 40, "SHIPS====>")

    connection = sqlite3.connect('mygame.db')  # Подключаемся к базе
    cursor = connection.cursor()

    for i in range(200):
        ship_name = 'Ship-' + str(i + 1)

        ship_weapon_id = random.randint(1, 20)
        ship_weapon_variation_query = ("""SELECT weapon FROM {table} WHERE ROWID = ?""")
        cursor.execute(ship_weapon_variation_query.format(table="weapons"), [ship_weapon_id])
        ship_weapon_variation_out = cursor.fetchone()

        ship_hull_id = random.randint(1, 5)
        ship_hull_variation_query = ("""SELECT hull FROM {table} WHERE ROWID = ?""")
        cursor.execute(ship_hull_variation_query.format(table="hulls"), [ship_hull_id])
        ship_hull_variation_out = cursor.fetchone()

        ship_engine_id = random.randint(1, 6)
        ship_engine_variation_query = ("""SELECT engine FROM {table} WHERE ROWID = ?""")
        cursor.execute(ship_engine_variation_query.format(table="engines"), [ship_engine_id])
        ship_engine_variation_out = cursor.fetchone()

        print("name: ", ship_name,
              " / weapon: ", ship_weapon_variation_out[0],
              " / hull: ", ship_hull_variation_out[0],
              " / engine: ", ship_engine_variation_out[0])

        ship_set = [ship_name,
                    ship_weapon_variation_out[0],
                    ship_hull_variation_out[0],
                    ship_engine_variation_out[0]]

        ship_set_query = """ INSERT INTO {table} (ship, weapon, hull, engine)
                                    VALUES (?,?,?,?)"""
        try:
            cursor.execute(ship_set_query.format(table="ships"), ship_set)
        except sqlite3.IntegrityError as e:
            print("Запись была добавлена ранее: ", e)
        connection.commit()

    cursor.close()
    connection.close()


test_ADD_Ships_in_Table()
