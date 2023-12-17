# Hotel booking application

## Program planing
- User can see a list of hotels
- User can book a hotel
- User can get a reservation ticket

# Classes
- User
- Hotel
- ReservationTicket


# When you create methods you should ask yourself "Where i can use it", for example book hotels or generate reservation
# If you have the value from x column in dataframe and you want to find the value from another one you can use .loc pandas concept 
In [2]: df
Out[2]:
    A  B
0  p1  1
1  p1  2
2  p3  3
3  p2  4

In [3]: df.loc[df['B'] == 3, 'A']
Out[3]:
2    p3
Name: A, dtype: object

In [4]: df.loc[df['B'] == 3, 'A'].iloc[0]
Out[4]: 'p3'

# Method squeeze() extract only needed value 