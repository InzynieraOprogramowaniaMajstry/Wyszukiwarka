import sys
import os
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.append(SCRIPT_DIR)

# from models.database import db, Planet, User

# def register(app):

#     @app.cli.command('db_create')
#     def db_create():
#         db.create_all()
#         print("Database created!")

#     @app.cli.command('db_drop')
#     def db_drop():
#         db.drop_all()
#         print("Database dropped!")

#     @app.cli.command("db_seed")
#     def db_seed():
#         mercury = Planet(planet_name = "Mercury", 
#                         planet_type ="Class D",
#                         home_star ="Sol",
#                         mass = 3.258e13,
#                         radius = 1516,
#                         distance = 35.98e6)
#         venus = Planet(planet_name = "Venus", 
#                         planet_type ="Class K",
#                         home_star ="Sol",
#                         mass = 4.123e24,
#                         radius = 2316,
#                         distance = 65.98e6)
#         earth = Planet(planet_name = "Earth", 
#                         planet_type ="Class M",
#                         home_star ="Sol",
#                         mass = 5.123e24,
#                         radius = 3333,
#                         distance = 82.98e6)

#         db.session.add(mercury)
#         db.session.add(venus)
#         db.session.add(earth)

#         test_user = User(first_name = "Will", 
#                         last_name="Wonka", 
#                         email = "test@test.com",
#                         password="zaq1@WSX")

#         db.session.add(test_user)
#         db.session.commit()
#         print("Database seeded")