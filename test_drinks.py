import drink

def test_person_looks_over_25():
    assert drink.can_buy_alcohol(True) == True

def test_no_id_no_sale():
    assert drink.can_buy_alcohol(False) == False

def test_too_young_to_buy_alcohol():
    assert drink.can_buy_alcohol(False, 17) == False

def test_id_check_can_buy_alcohol():
    assert drink.can_buy_alcohol(False, 18) == True