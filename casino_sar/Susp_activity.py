# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Dependencies
import pandas as pd


# %%
sarstats = pd.read_csv('casino_sar/data/SARStats_casino.csv')
sw_countyloc = pd.read_csv('data/SW_countyloc.csv')
sarstats.head()


# %%
sarstats.count()


# %%
sarstats.drop(sarstats.loc[sarstats['Suspicious Activity']=='[Total]'].index, inplace=True)
sarstats.drop(sarstats.loc[sarstats['Year Month']== '2020'].index, inplace=True)
sarstats.rename(columns={"Year Month": "Year"}, inplace=True)
sarstats['Industry'] = sarstats['Industry'].str.split('\-+').str[1]

sarstats.head()


# %%
sarstats.count()


# %%
act_county = sarstats.groupby([ 'Industry', 'Suspicious Activity', 'State', 'Countym'])['Count'].count().reset_index()
act_county.head()


# %%
act_county['Count'] = act_county['Count'].astype(int)


# %%
act_county['Count'].max()


# %%
top_act = act_county.sort_values(by=['Count'], ascending=False)
top_act.head()


# %%
top_act.count()


# %%
act_state = sarstats.groupby(['Suspicious Activity','State'])['Count'].count().reset_index()
act_state.head()


# %%
act_state.count()


# %%
top_act_state = act_state.sort_values(by=['Count'], ascending=False)
top_act_state.head()


# %%
sw_countyloc.head()


# %%
sw_countyloc.drop(['GEOID', 'ANSICODE', 'NAME', 'ALAND', 'AWATER', 'ALAND_SQMI', 'AWATER_SQMI'], axis=1, inplace=True)
sw_county=sw_countyloc.rename(columns={"NAME":"Countym", "INTPTLAT":"Lat", "INTPTLONG                                                                                                               ":"Long" })
sw_county.head()


# %%
# top_act_county = pd.merge(top_act, sw_county, on='Countym', how='inner')
# top_act_county.head()


# %%
# del top_act_county['USPS']
# top_act_county['Countym'] = top_act_county['Countym'].str.split('\,+').str[0]
# top_act_county.head()


# %%
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///SW_fincrime_db', echo=False)
# sqlite_connection = engine.connect()


# %%
# sqlite_table = "topActivityCounty"
# top_act_county.to_sql(sqlite_table, sqlite_connection, if_exists='replace')


# %%
# engine.execute("SELECT * FROM topActivityState").fetchall()


# %%
# sqlite_table = "topActivityState"
# top_act_state.to_sql(sqlite_table, sqlite_connection, if_exists='replace')


# %%
# engine.execute("SELECT * FROM topActivityState").fetchall()


# %%
# sqlite_connection.close()


# %%
sarstats.head()


# %%
del sw_county['USPS']
sw_county.head()


# %%
casino_crime = pd.merge(sarstats, sw_county, on = 'Countym', how = 'inner' )
casino_crime['Countym'] = casino_crime['Countym'].str.split('\,+').str[0]
# casino_crime.set_index('State', inplace = True)
casino_crime.head()


# %%
casino_crime.index.name = 'Id'


# %%
casino_crime.head()


# %%
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from datetime import datetime
import sqlite3


# %%
engine = create_engine('sqlite:///data/Casino.sqlite', echo=False)
sqlite_connection = engine.connect()


# %%
sqlite_table = "casinoSW"
# casino_crime.to_sql(sqlite_table, sqlite_connection, if_exists='replace')


# %%
#  engine.execute('drop table casinoSW')


# %%
# inspector = inspect(engine)
# columns = inspector.get_columns('casinoSW')
# print(columns)


# %%
# engine.execute('''create table casinoSW(id int not null Primary key,
#               Year int,
#               State varchar(255),
#               Countym varchar(255),
#               Industry varchar(255),
#               "Suspicious Activity" varchar(500),
#               Count int not null,
#               Lat decimal,
#               Long decimal)
#               ''')


# %%



# %%
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)


# %%
Base.classes.keys()


# %%



# %%



# %%
# casino_crime.to_sql(sqlite_table, sqlite_connection, if_exists='append', index=True)

# with sqlite_connection() as con:
#     con.execute('ALTER TABLE `casinoSW` ADD PRIMARY KEY (`ID_column`);')


# %%
casinoSW = engine.execute("SELECT * FROM casinoSW LIMIT 5")


# %%
for item in casinoSW:
    print(item)


# %%
# con = sqlalchemy.create_engine(url, client_encoding= 'utf8')
# con.executor('alter table my_table add primary key(index)')


# %%
# engine.execute("ALTER TABLE casinoSW ADD PR KEY ('ID_column')")


# %%
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)


# %%
# Base.classes.keys()


# %%


