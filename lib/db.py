import dataset

# todo. read this from a config file
DB_NAME = "data.db"

db = dataset.connect("sqlite:///" + DB_NAME)
