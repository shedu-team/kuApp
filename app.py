import pandas as pd

d = {'col1': [1, 2, 3, 4, 7],
     'col2': [4, 5, 6, 9, 5],
     'col3': [8, 8, 7, 2, 5],
     'col4': [4, 5, 6, 7, 5],
     'col5': [8, 5, 3, 9, 5],
     'col6': [4, 5, 3, 9, 5],
     'col7': [4, 6, 5, 9, 5],
     'col8': [7, 8, 12, 1, 11]
     }
df = pd.DataFrame(data=d)

print(df)

# this function is returning the number of rows.
print(f"No of Rows = {df.shape[0]}. and No of columns = {df.shape[1]}.")


pulseMax = max(80, 50, 82, 95)
print(pulseMax)
