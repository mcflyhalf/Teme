#Create Setup.py file to make the module installable
from setuptools import setup, find_packages
import configparser
import os


setup(
    name = "teme",
    version = "0.0.0",
    author = "Mcflyhalf",
    author_email = "mcflyhalf@live.com",
    description = ("Code autograding platform for teachers and students of programming"),
    keywords = "autograding programming cseducation",
    packages= find_packages(),
)

logger = get_logger("teme_setup")

logger.info("Teme python package successfuly installed")


class TemeConfig:
	#Create tables (DB needs to have been created in advance outside of python)

	def __init__(self,engine):
		# self.newconfig(engine)


	def create_tables(self, engine):
		# To be populated after schema already exists

		# tables = Base.metadata.sorted_tables
		#Create (but not populate all tables in the db schema)
		# logger.info("Attempting to create tables")
		# #Do stuff here using metadata from the classes in the schema
		# for table in tables:
		# 	logger.info("Creating table *{}*".format(table.name))
		# 	Base.metadata.create_all(engine, tables=[table])
		# 	logger.info("Table *{}* created successfully".format(table.name))

		# logger.info("Tables Created successfully!")

	#Delete all tables (DB should have been created in advance)
	def drop_tables(self, engine):
		# To be created after schema is made

		# tables = Base.metadata.sorted_tables
		# tables.reverse()
		# logger.warn("Deleting all tables")
		# #Do dangerous stuff here and log as each table is deleted
		# for table in tables:
		# 	logger.warn("Deleting table *{}*".format(table.name))
		# 	Base.metadata.drop_all(engine, tables=[table])
		# 	logger.info("Table *{}* deleted successfully".format(table.name))

		# logger.info("Tables deleted successfully!")

	def newconfig(self, engine):	#For a new install
		# self.drop_tables(engine)
		# self.create_tables(engine)

	def create_paths(self, rootpath ):	#Set default root path to the current directory
		pass

#Create your db for actual work and test db for integration tests
TemeConfig(production_engine)
TemeConfig(test_engine)

# populate_testdb()		#Put some data into the test db to be used for integration tests

config = configparser.ConfigParser()

config['DEFAULT'] = {}
default = config['DEFAULT']

default['Install Location'] = str(os.getcwd())	#Base install directory
default['config_file'] = os.path.join(os.getcwd(), CONFIG_FILENAME)


#Create config file
# with open(CONFIG_FILENAME, 'w') as configfile:
# 	config.write(configfile)

