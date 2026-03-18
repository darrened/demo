def can_buy_alcohol(id_age=None):
    if id_age and id_age >= 18:
        return True
    return False