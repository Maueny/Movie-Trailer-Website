import fresh_tomatoes # fresh_tomatoes.py
import media # media.py



# movie 1(John wick2)

John_wick2 = media.Movie('John wick2',
                         'After returning to the criminal underworld to repay \
                          a debt, John Wick discovers that a large bounty has \
                          been put on his life',
                         'https://goo.gl/yvz57J',
                         'https://youtu.be/XGk2EfbD_Ps')
                         # Related info(Name/Storyline/Poster/trailer)

# movie 2(Kingsman)

Kingsman = media.Movie('Kingsman',
                       'Kingsman: The Secret Service Official Trailer#1(2015)',
                       'https://goo.gl/v5ffpG',
                       'https://www.youtube.com/watch?v=hN0JkFrvO_M')
                       # Related info(Name/Storyline/Poster/trailer)

# movie 3(Mad Max: Fury Road)

Mad_Max_Fury_Road = media.Movie('Mad Max: Fury Road',
                                'A woman rebels against a tyrannical ruler in\
                                 postapocalyptic Australia in search for her\
                                 home-land with the help of a group of female\
                                 prisoners, a psychotic worshipper, and a \
                                 drifter named Max',
                                'https://goo.gl/JZvQqh',
                                'https://www.youtube.com/watch?v=hEJnMQG9ev8')
                                 # Related info(Name/Storyline/Poster/trailer)

movies = [John_wick2,Kingsman,Mad_Max_Fury_Road]
fresh_tomatoes.open_movies_page(movies) ## open the output file in the browser

