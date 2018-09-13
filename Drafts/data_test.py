import pandas as pd
from get_u_input_test import get_genre

genres = get_genre()
length = len(genres)

for x in range(0, length, 1):
    print(str(genres[x]))
