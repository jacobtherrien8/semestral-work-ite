LBS_TO_KG = 0.453592

"""
Convert lbs to kg 
Weight(float) type by the player
Unit(string) : kg or lbs
"""

def convert_lbs_to_kg(weight, unit):

    if unit == 'lbs':
        return weight*LBS_TO_KG

    return weight


"""
Returns (float) the weight in kg
"""
    