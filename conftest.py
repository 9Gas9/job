import pytest
import sqlite3
import random


# Создаем новый параметр запуска теста: --all (Пример: pytest -s -v test_game.py --all)
def pytest_addoption(parser):
    parser.addoption("--all", action="store_true", help="run all combinations")


# Генератор повтора тестов в кол-ве 200 шт. для каждого теста,
# если не использовать --all проход будет 1 шт. для каждого теста.
# 1 == индекс 0, 2 == индекс 1, ... ,  201 == индекс 200
def pytest_generate_tests(metafunc):
    if "param1" in metafunc.fixturenames:
        if metafunc.config.getoption("all"):
            end = 200
        else:
            end = 1
        metafunc.parametrize("param1", range(end))


@pytest.fixture(scope='session')
def run_global_base():
    big_global_base = []

    con_origin = sqlite3.connect("mygame.db")
    cur_origin = con_origin.cursor()
    ship_original_out = ("""SELECT * FROM {table}""")
    cur_origin.execute(ship_original_out.format(table="ships"))
    ship_original = cur_origin.fetchall()

    if con_origin:

        con_new = sqlite3.connect(":memory:")
        cur_new = con_new.cursor()

        if con_new:
            cur_new.execute("""CREATE TABLE IF NOT EXISTS ships(
                              ship TEXT PRIMARY KEY, 
                              weapon TEXT, 
                              hull TEXT, 
                              engine TEXT)
                           """)
            con_new.commit()

            cur_new.execute("""CREATE TABLE IF NOT EXISTS weapons(
                              weapon TEXT PRIMARY KEY, 
                              reload_speed INT, 
                              rotation_speed INT, 
                              diameter INT,
                              power_volley INT,
                              count INT)
                           """)
            con_new.commit()

            cur_new.execute("""CREATE TABLE IF NOT EXISTS hulls(
                              hull TEXT PRIMARY KEY, 
                              armor INT, 
                              type INT, 
                              capacity INT)
                           """)
            con_new.commit()

            cur_new.execute("""CREATE TABLE IF NOT EXISTS engines(
                              engine TEXT PRIMARY KEY, 
                              power INT, 
                              type INT)
                           """)
            con_new.commit()

            weapons = ("""SELECT * FROM {table}""")
            cur_origin.execute(weapons.format(table="weapons"))
            weapons_out = cur_origin.fetchall()

            hulls = ("""SELECT * FROM {table}""")
            cur_origin.execute(hulls.format(table="hulls"))
            hulls_out = cur_origin.fetchall()

            engines = ("""SELECT * FROM {table}""")
            cur_origin.execute(engines.format(table="engines"))
            engines_out = cur_origin.fetchall()

            ship = ("""SELECT * FROM {table}""")
            cur_origin.execute(ship.format(table="ships"))
            ship_out = cur_origin.fetchall()

            for i in range(-1, 19):
                j = i + 1

                weapon_set = [weapons_out[j][0],
                              weapons_out[j][1],
                              weapons_out[j][2],
                              weapons_out[j][3],
                              weapons_out[j][4],
                              weapons_out[j][5]]

                weapon_index = random.randint(1, 5)
                weapon_new_option = random.randint(1, 20)
                weapon_set[weapon_index] = weapon_new_option

                weapon_set_add = """ INSERT INTO {table} (weapon, reload_speed, rotation_speed,
                                                        diameter, power_volley, count)
                                        VALUES (?,?,?,?,?,?)"""
                cur_new.execute(weapon_set_add.format(table="weapons"), weapon_set)
                con_new.commit()

            for i in range(-1, 4):
                j = i + 1

                hull_set = [hulls_out[j][0],
                            hulls_out[j][1],
                            hulls_out[j][2],
                            hulls_out[j][3]]

                hull_index = random.randint(1, 3)
                hull_new_option = random.randint(1, 20)
                hull_set[hull_index] = hull_new_option

                hull_set_add = """ INSERT INTO {table} (hull, armor, type, capacity)
                                        VALUES (?,?,?,?)"""
                cur_new.execute(hull_set_add.format(table="hulls"), hull_set)
                con_new.commit()

            for i in range(-1, 5):
                j = i + 1

                engine_set = [engines_out[j][0],
                              engines_out[j][1],
                              engines_out[j][2]]

                engine_index = random.randint(1, 2)
                engine_new_option = random.randint(1, 20)
                engine_set[engine_index] = engine_new_option

                engine_set_add = """ INSERT INTO {table} (engine, power, type)
                                        VALUES (?,?,?)"""
                cur_new.execute(engine_set_add.format(table="engines"), engine_set)
                con_new.commit()

            for i in range(-1, 199):

                j = i + 1

                ship_weapon_id = random.randint(1, 20)
                ship_weapon_variation_query = ("""SELECT weapon FROM {table} WHERE ROWID = ?""")
                cur_new.execute(ship_weapon_variation_query.format(table="weapons"), [ship_weapon_id])
                ship_weapon_variation_out = cur_new.fetchone()

                ship_hull_id = random.randint(1, 4)
                ship_hull_variation_query = ("""SELECT hull FROM {table} WHERE ROWID = ?""")
                cur_new.execute(ship_hull_variation_query.format(table="hulls"), [ship_hull_id])
                ship_hull_variation_out = cur_new.fetchone()

                ship_engine_id = random.randint(1, 5)
                ship_engine_variation_query = ("""SELECT engine FROM {table} WHERE ROWID = ?""")
                cur_new.execute(ship_engine_variation_query.format(table="engines"), [ship_engine_id])
                ship_engine_variation_out = cur_new.fetchone()

                ship_set = [ship_out[j][0],
                            ship_out[j][1],
                            ship_out[j][2],
                            ship_out[j][3]]

                ship_index = random.randint(1, 3)

                if ship_index == 1:
                    ship_new_option = ship_weapon_variation_out[0]
                elif ship_index == 2:
                    ship_new_option = ship_hull_variation_out[0]
                elif ship_index == 3:
                    ship_new_option = ship_engine_variation_out[0]

                ship_set[ship_index] = ship_new_option

                ship_set_add = """ INSERT INTO {table} (ship, weapon, hull, engine)
                                            VALUES (?,?,?,?)"""
                cur_new.execute(ship_set_add.format(table="ships"), ship_set)
                con_new.commit()

    check = ("""SELECT * FROM {table}""")
    cur_new.execute(check.format(table="ships"))
    ship_new = cur_new.fetchall()

    # __________________________________________________________________________
    for i in range(-1, 199):
        j = i + 1

        weapon_options_original_out = ("""SELECT * FROM {table} WHERE weapon = ?""")
        cur_origin.execute(weapon_options_original_out.format(table="weapons"), [ship_original[j][1]])
        weapons_original = cur_origin.fetchall()

        hull_options_original_out = ("""SELECT * FROM {table} WHERE hull = ?""")
        cur_origin.execute(hull_options_original_out.format(table="hulls"), [ship_original[j][2]])
        hulls_original = cur_origin.fetchall()

        engine_options_original_out = ("""SELECT * FROM {table} WHERE engine = ?""")
        cur_origin.execute(engine_options_original_out.format(table="engines"), [ship_original[j][3]])
        engines_original = cur_origin.fetchall()

        weapon_options_new_out = ("""SELECT * FROM {table} WHERE weapon = ?""")
        cur_new.execute(weapon_options_new_out.format(table="weapons"), [ship_new[j][1]])
        weapons_new = cur_new.fetchall()

        hull_options_new_out = ("""SELECT * FROM {table} WHERE hull = ?""")
        cur_new.execute(hull_options_new_out.format(table="hulls"), [ship_new[j][2]])
        hulls_new = cur_new.fetchall()

        engine_options_new_out = ("""SELECT * FROM {table} WHERE engine = ?""")
        cur_new.execute(engine_options_new_out.format(table="engines"), [ship_new[j][3]])
        engines_new = cur_new.fetchall()

        big_train_global_base =[]

        big_original_base = [ship_original[j][0],
                             ship_original[j][1], weapons_original[0],
                             ship_original[j][2], hulls_original[0],
                             ship_original[j][3], engines_original[0]
                             ]

        big_new_base = [ship_new[j][0],
                        ship_new[j][1], weapons_new[0],
                        ship_new[j][2], hulls_new[0],
                        ship_new[j][3], engines_new[0]
                        ]

        big_train_global_base.append(big_original_base)
        big_train_global_base.append(big_new_base)

        big_global_base.append(big_train_global_base)

    return big_global_base
