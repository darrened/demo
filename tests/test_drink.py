import drink

def test_no_id_no_sale():
    assert drink.canBuyAlcohol(False) == False

def test_too_young_to_buy_alcohol():
    assert drink.canBuyAlcohol(False, 17) == False

def test_id_check_can_buy_alcohol():
    assert drink.canBuyAlcohol(False, 18) == True