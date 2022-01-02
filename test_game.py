
def test_ships_weapons(run_global_base, param1):

    assert run_global_base[param1][0][1] == run_global_base[param1][1][1], \
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]}  " \
                                                f"expected  {run_global_base[param1][0][1]}, " \
                                                f"was {run_global_base[param1][1][1]} "

    assert run_global_base[param1][0][2][1] == run_global_base[param1][1][2][1],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]} " \
                                                f"reload speed: expected " \
                                                f"{run_global_base[param1][0][2][1]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][2][1]} "

    assert run_global_base[param1][0][2][2] == run_global_base[param1][1][2][2],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]} " \
                                                f"rotation speed: expected " \
                                                f"{run_global_base[param1][0][2][2]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][2][2]} "

    assert run_global_base[param1][0][2][3] == run_global_base[param1][1][2][3],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]} " \
                                                f"diameter: expected " \
                                                f"{run_global_base[param1][0][2][3]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][2][3]} "

    assert run_global_base[param1][0][2][4] == run_global_base[param1][1][2][4],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]} " \
                                                f"power volley: expected " \
                                                f"{run_global_base[param1][0][2][4]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][2][4]} "

    assert run_global_base[param1][0][2][5] == run_global_base[param1][1][2][5],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][1]} " \
                                                f"count: expected " \
                                                f"{run_global_base[param1][0][2][5]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][2][5]} "


def test_ships_hulls(run_global_base, param1):
    assert run_global_base[param1][0][3] == run_global_base[param1][1][3], \
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][3]}  " \
                                                f"expected  {run_global_base[param1][0][3]}, " \
                                                f"was {run_global_base[param1][1][3]} "

    assert run_global_base[param1][0][4][1] == run_global_base[param1][1][4][1],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][3]} " \
                                                f"armor: expected " \
                                                f"{run_global_base[param1][0][4][1]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][4][1]} "

    assert run_global_base[param1][0][4][2] == run_global_base[param1][1][4][2],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][3]} " \
                                                f"type: expected " \
                                                f"{run_global_base[param1][0][4][2]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][4][2]} "

    assert run_global_base[param1][0][4][3] == run_global_base[param1][1][4][3],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][3]} " \
                                                f"capacity: expected " \
                                                f"{run_global_base[param1][0][4][3]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][4][3]} "


def test_ships_engines(run_global_base, param1):
    assert run_global_base[param1][0][5] == run_global_base[param1][1][5], \
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][5]}  " \
                                                f"expected  {run_global_base[param1][0][5]}, " \
                                                f"was {run_global_base[param1][1][5]} "

    assert run_global_base[param1][0][6][1] == run_global_base[param1][1][6][1],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][5]} " \
                                                f"power: expected " \
                                                f"{run_global_base[param1][0][6][1]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][6][1]} "

    assert run_global_base[param1][0][6][2] == run_global_base[param1][1][6][2],\
                                                f"{run_global_base[param1][0][0]}, " \
                                                f"{run_global_base[param1][0][5]} " \
                                                f"type: expected " \
                                                f"{run_global_base[param1][0][6][2]}, " \
                                                f"was " \
                                                f"{run_global_base[param1][1][6][2]} "
