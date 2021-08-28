import numpy as np
import pandas as pd


def getuser():
    data = {'name': 'Oumar Diaby', 'age': 20, 'country': 'Mali'}
    data = pd.DataFrame(data=data)
    return data

