def can_buy_alcohol(looks_over_25, id_age=None):
    if looks_over_25:
        return True
    elif id_age and id_age >= 18:
        return True
    return False