# This file is for populating the database with few items

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture=('https://pbs.twimg.com/profile_images/2671170543/'
                      '18debd694829ed78203a5a36dd364160_400x400.png'))
session.add(User1)
session.commit()

# Questions in the category of History
category1 = Category(name="History")

session.add(category1)
session.commit()

item1 = Item(user_id=1, air_date="2004-12-31",
             question=("For the last 8 years of his life, Galileo was under"
                       " house arrest for espousing this man\'s theory"),
             value="$200", answer="Copernicus", game_round="Jeopardy!",
             show_number="4680", category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="1996-12-06",
             question=("Historians refer to the Golden Age as the time during"
                       "which Pericles ruled this city"),
             value="$200", answer="Athens", game_round="Double Jeopardy!",
             show_number="2825", category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="1993-06-29",
             question=("In 1991 B.C. Amenemhet, a former vizier, "
                       "founded this country\'s 12th dynasty"),
             value="$200", answer="Egypt", game_round="Double Jeopardy!",
             show_number="2047", category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="1988-01-11",
             question=("Peregrine White, the 1st child born in New England of"
                       " English parents, was born on this ship"),
             value="$200", answer="the Mayflower",
             game_round="Double Jeopardy!",
             show_number="776", category=category1)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="1997-10-09",
             question=("In 1898 Britain leased the New Territories from China,"
                       "adding to the area of this dependency"),
             value="$100", answer="Hong Kong", game_round="Jeopardy!",
             show_number="3014", category=category1)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="2001-07-18",
             question="In 1429, she was given control of troops in France",
             value="$100", answer="Joan of Arc", game_round="Jeopardy!",
             show_number="3903", category=category1)

session.add(item6)
session.commit()


# Questions in the category of Annual Events
category2 = Category(name="Annual Events")

session.add(category2)
session.commit()


item1 = Item(user_id=1, air_date="1996-12-06",
             question=("Dog lovers look forward to the Westminster Kennel Club"
                       " dog show, held each February in this city"),
             value="$300", answer="New York City", game_round="Jeopardy!",
             show_number="2825", category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="2007-10-09",
             question=("Several different islands choose their own kings & "
                       "queens as part of this state\'s Aloha festivals"),
             value="$400", answer="Hawaii", game_round="Double Jeopardy!",
             show_number="5307", category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="1998-10-30",
             question=("Dating back at least 100 years, "
                       "\"drowning the shamrock\", or going drinking, "
                       "is a tradition on this holiday"),
             value="$100", answer="St. Patrick\'s Day", game_round="Jeopardy!",
             show_number="3255", category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="1996-12-20",
             question=("The Queen Liliuokalani Canoe Races take place on "
                       "Labor Day weekend in this state"),
             value="$100", answer="Hawaii", game_round="Jeopardy!",
             show_number="2835", category=category2)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="1997-03-03",
             question=("The Jackson Hole Shootout in this state features a"
                       " stagecoach robbery reenactment"),
             value="$400", answer="Wyoming", game_round="Double Jeopardy!",
             show_number="2886", category=category2)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="1997-06-19",
             question=("The Fiesta Bowl Parade & Prescott Bluegrass Festival"
                       " are annual events in this state"),
             value="$500", answer="Arizona", game_round="Jeopardy!",
             show_number="2964", category=category2)

session.add(item6)
session.commit()


# Questions in the category of World Geography
category3 = Category(name="World Geography")

session.add(category3)
session.commit()


item1 = Item(user_id=1, air_date="1993-06-28",
             question=("The main part of Cairo lies on 2 islands"
                       " & the East Bank of this river"),
             value="$200", answer="the Nile", game_round="Double Jeopardy!",
             show_number="2046", category=category3)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="1996-06-21",
             question=("Large aboriginal populations live in this country\'s"
                       " states of Queensland & New South Wales"),
             value="$200", answer="Australia", game_round="Double Jeopardy!",
             show_number="2735", category=category3)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="1990-04-10",
             question="This country is named after the town of Oporto",
             value="$200", answer="Portugal", game_round="Double Jeopardy!",
             show_number="1302", category=category3)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="1996-07-18",
             question=("Brocken is the highest peak in this German"
                       " mountain range known for its canaries"),
             value="$200", answer="Hartz Mountains",
             game_round="Double Jeopardy!",
             show_number="2754", category=category3)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="1990-03-05",
             question="It\'s the lowest, flattest & smallest continent",
             value="$100", answer="Australia", game_round="Jeopardy!",
             show_number="1276", category=category3)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="2001-05-10",
             question=("Lying on the east bank of the Nile, Tahrir Square"
                       " is the center of this capital's downtown"),
             value="$200", answer="Cairo", game_round="Double Jeopardy!",
             show_number="3854", category=category3)

session.add(item6)
session.commit()


# Questions in the category of People in History
category4 = Category(name="People in History")

session.add(category4)
session.commit()


item1 = Item(user_id=1, air_date="1997-11-26",
             question=("This president was nicknamed the"
                       " \"Sage Of The Hermitage\""),
             value="$100", answer="Andrew Jackson", game_round="Jeopardy!",
             show_number="3048", category=category4)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="1998-11-17",
             question=("Talleyrand resigned from this emperor\'s service in "
                       "1807 & began intriguing against him"),
             value="$100", answer="Napoleon",
             game_round="Jeopardy!", show_number="3267", category=category4)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="1997-06-02",
             question=("In 1502, during his last voyage to the Americas, "
                       "he sighted what is now Nicaragua"),
             value="$100", answer="Christopher Columbus",
             game_round="Jeopardy!", show_number="2951", category=category4)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="1996-04-12",
             question=("Saint Hyacinth, whose uncle was the bishop of Krakow,"
                       " is the apostle of this country"),
             value="$200", answer="Poland", game_round="Jeopardy!",
             show_number="2685", category=category4)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="2005-05-30",
             question=("Britain\'s Edmund Burke called for peace with the"
                       "colonies the day before this man demanded liberty"
                       " or death"),
             value="$400", answer="Patrick Henry",
             game_round="Double Jeopardy!",
             show_number="4786", category=category4)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="1999-05-24",
             question=("This alumnus of Plato\'s Academy went on to found his"
                       " own school, the Lyceum"),
             value="$100", answer="Aristotle", game_round="Jeopardy!",
             show_number="3401", category=category4)

session.add(item6)
session.commit()


# Questions in the category of U.S. Cities
category5 = Category(name="U.S. Cities")

session.add(category5)
session.commit()


item1 = Item(user_id=1, air_date="1999-05-24",
             question=("When football\'s Saints go marching in for a"
                       " home game, it\'s in this city"),
             value="$100", answer="New Orleans", game_round="Jeopardy!",
             show_number="3401", category=category5)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="1990-11-07",
             question=("This Colorado resort city was named for a type of"
                       " poplar tree growing in the area"),
             value="$200", answer="Aspen", game_round="Double Jeopardy!",
             show_number="1423", category=category5)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="2010-01-04",
             question=("This city\'s Haight-Ashbury District emerged in the"
                       " 1960s as a Mecca of the counterculture scene"),
             value="$400", answer="San Francisco",
             game_round="Double Jeopardy!",
             show_number="5826", category=category5)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="2002-10-24",
             question=("Depictions on this state capital\'s seal include"
                       " Nuuanu Pali & Diamond Head"),
             value="$200", answer="Honolulu", game_round="Jeopardy!",
             show_number="4174", category=category5)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="1999-01-05",
             question=("One of the Twin Cities, it was named"
                       " after a man from Tarsus"),
             value="$100", answer="St. Paul", game_round="Jeopardy!",
             show_number="3302", category=category5)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="2002-05-14",
             question=("There\'s a tomb of the unknown soldiers of the"
                       " Revolutionary War in this N.Y. city"
                       " that wasn\'t built in a day"),
             value="$800", answer="Rome, New York",
             game_round="Double Jeopardy!",
             show_number="4087", category=category5)

session.add(item6)
session.commit()


# Questions in the category of Foreign Words & Phrases
category6 = Category(name="Foreign Words & Phrases")

session.add(category6)
session.commit()

item1 = Item(user_id=1, air_date="2001-02-09",
             question=("It\'s the English meaning of the title of"
                       " Wayne Newton\'s hit song \"Danke Schoen\""),
             value="$200", answer="\"Thank You\"", game_round="Jeopardy!",
             show_number="3790", category=category6)

session.add(item1)
session.commit()

item2 = Item(user_id=1, air_date="1990-05-16",
             question="Literally \"To God\", it\'s Spanish for goodbye",
             value="$200", answer="Adios", game_round="Double Jeopardy!",
             show_number="1328", category=category6)

session.add(item2)
session.commit()

item3 = Item(user_id=1, air_date="2004-02-02",
             question="This 2-word Latin phrase means \"by the fact itself\"",
             value="$400", answer="ipso facto", game_round="Double Jeopardy!",
             show_number="4471", category=category6)

session.add(item3)
session.commit()

item4 = Item(user_id=1, air_date="2009-06-19",
             question=("In Dutch this holiday greeting is"
                       " \"Vrolijk Kerstfeest\""),
             value="$400", answer="Merry Christmas",
             game_round="Double Jeopardy!",
             show_number="5720", category=category6)

session.add(item4)
session.commit()

item5 = Item(user_id=1, air_date="1991-10-10",
             question=("If you can tell me what \"gelt\" means in Yiddish,"
                       " you\'ll earn some right now"),
             value="$100", answer="money", game_round="Jeopardy!",
             show_number="1634", category=category6)

session.add(item5)
session.commit()

item6 = Item(user_id=1, air_date="2004-09-24",
             question="It\'s the Turkish word for fate or destiny",
             value="$200", answer="kismet", game_round="Jeopardy!",
             show_number="4610", category=category6)

session.add(item6)
session.commit()

print "added items!"
