
# coding: utf-8

# # 2. Geopandas
# Geopandas est une extension de pandas, permettant d'effectuer des opérations sur des données géoréférencées grâce à shapely. On peut notamment l'utiliser pour:
# - importer / exporter des données géospatiales
# - faire des analyses géométriques sur ces données
# - visualiser des données
# 
# http://geopandas.org/index.html

# In[1]:

import geopandas as gpd
get_ipython().magic('matplotlib notebook')

training_folder = r'../'
gis_folder = training_folder +'gis/'
data_folder = training_folder + 'data/'


# ## 2.1 Structure de donnée
# Pandas --> Series / DataFrame
# 
# Geopandas --> GeoSeries / GeoDataFrame

# In[2]:

idf_geodf = gpd.read_file(gis_folder + 'idf/idf_geodf.shp')
idf_geodf.head()


# In[3]:

type(idf_geodf)


# In[4]:

type(idf_geodf['geometry'])


# In[5]:

type(idf_geodf['id'])


# Une GeoSeries est un vecteur composé de géométries shapely, toutes devant être de *même type*. Cet objet reprend la plupart des attributs et méthodes de shapely, qui sont ici appliqués élément par élément: une Series ou GeoSeries est ensuite renvoyée.
# 
# Exemples de méthodes et attributs:
# - `area`
# - `bounds`
# - `is_valid`
# - `centroid`
# 
# Un GeoDataFrame est un DataFrame contenant une colonne GeoSeries. Toute méthode spatiale appliquée au GeoDataFrame sera appliquée à la GeoSerie correspondante.

# In[6]:

idf_geodf.area


# In[7]:

type(idf_geodf.area)


# In[8]:

idf_geodf.centroid


# In[9]:

type(idf_geodf.centroid)


# ## 2.2 Importer des données et les visualiser

# Geopandas `read_file` method can read almost every vector-based data format (GeoJSON, shapefile, ...) and returns a GeoDataFrame object.

# In[10]:

idf_comm_geom = gpd.read_file(gis_folder + 'idf/idf_geom_only.shp')
idf_comm_geom.head()


# In[11]:

# Import Orly airport position
orly = gpd.read_file(gis_folder + r'idf/orly_airport.shp')
orly.head()


# In[12]:

idf_comm_geom.plot()


# In[13]:

orly.plot(marker='o', color='red',markersize=5)


# In[14]:

base = idf_comm_geom.plot()
orly.plot(ax=base, marker='o', color='red',markersize=10)


# ### 2.3 Analyser des données

# Calculer l'aire des géométries.

# In[15]:

idf_comm_geom['area'] = idf_comm_geom.area
idf_comm_geom.head()


# In[16]:

idf_comm_geom.head()


# In[17]:

idf_comm_geom.apply(
    lambda x: x['geometry'].area, 1
)


# Tester l'inclusion d'une géométrie dans une autre.

# In[18]:

orly_position = orly.geometry[0]
type(orly_position)


# In[19]:

idf_comm_geom.contains(orly_position)


# In[20]:

idf_comm_geom[idf_comm_geom.contains(orly_position)]


# Faire un merge avec une DataFrame

# In[22]:

import pandas as pd

# Import population file
idf_pop_data = pd.read_csv(data_folder + 'special_libraries/idf_pop.csv', index_col=0)
idf_pop_data.head()


# In[23]:

idf_comm = idf_comm_geom.merge(
    idf_pop_data,
    left_on='ID', right_on='DEPCOM',
    how='left'
)
idf_comm.head()


# Regrouper des entités

# In[24]:

idf_macro = idf_comm.dissolve(by='MACROZONE')[['geometry']]
idf_macro


# In[25]:

idf_macro.plot()


# ### 2.4 Changer de système de projection

# Les géométries d'une GeoSeries ou GeoDataFrame sont simplement des coordonnées dans un plan cartésien. Elles ne contiennent pas de notion de projection.
# 
# Ceci est géré par un attribut: crs

# In[26]:

idf_comm.crs


# On peut imposer un crs

# In[27]:

idf_macro.crs


# In[28]:

idf_macro.crs = idf_comm.crs


# On peut facilement changer de projection, en reprojetant l'ensemble des géométries

# In[29]:

idf_macro_lat_lon = idf_macro.to_crs({'init' :'epsg:4326'})


# In[30]:

idf_macro_lat_lon.head()


# In[31]:

idf_macro_lat_lon.plot()


# ### 2.5 Exporter des données

# L'export de données se fait simplement via la méthode:
# 
# to_file()

# In[33]:

idf_macro_lat_lon.to_file(
    gis_folder + r'idf/exported/idf_macrozones_latlon.shp'
)

