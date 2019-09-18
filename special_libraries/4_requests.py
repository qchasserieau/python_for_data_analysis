
# coding: utf-8

# # Librairies spéciales
# ## 3. Requests
# 
# Le module `requests` permet d'envoyer des requêtes HTTP en python. Il peut être très utile pour automatiser les recherches d'adresses ou de coordonnées, les calculs d'itinéraires, …
# 
# Nous allons ici montrer un exemple d'utilisation de ce module avec les API `geocoding` et `geocoding-reverse` de Google, qui permettent respectivement de trouver des coordonnées à partir d'une adresse, et une adresse à partir de coordonnées.
# 
# https://developers.google.com/maps/documentation/geocoding/intro?hl=fr
# 
# https://developers.google.com/maps/documentation/geocoding/intro?hl=fr#ReverseGeocoding

# In[1]:

import requests


# ### 3.1 Geocoding API

# Exemple de requête:

# In[39]:

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Systra,+France,+Farman')


# In[48]:

r.status_code, r.json()


# Décomposistion de l'url d'appel
# 
# https://maps.googleapis.com/maps/api/geocode/json?address=Systra,+France,+Farman

# In[41]:

geocoding_api_url = 'https://maps.googleapis.com/maps/api/geocode/'
response_format = 'json'
address_key_words = ['Systra', 'France']

url = geocoding_api_url + response_format + '?address=' + '+'.join(address_key_words)
url


# Décomposition de la réponse:
# - un statut
# - un json

# In[45]:

r.status_code


# In[46]:

r.json()


# In[57]:

r.json().keys()


# In[58]:

r.json()['status']


# In[59]:

type(r.json()['results'])


# In[61]:

r.json()['results'][0]


# In[60]:

r.json()['results'][0].keys()


# In[64]:

r.json()['results'][0]['geometry']


# In[63]:

r.json()['results'][0]['geometry']['location']


# ### 3.2 Reverse geocoding API

# Exemple

# In[76]:

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=48.8333516,2.269852')


# In[80]:

(r.status_code, r.json())


# Décomposition de l'url d'appel

# In[83]:

reverse_geocoding_api_url = 'https://maps.googleapis.com/maps/api/geocode/'
response_format = 'json'
lat_lon = ['48.8333516', '2.269852']
url = reverse_geocoding_api_url + response_format + '?latlng=' + ','.join(lat_lon)
url


# Décomposition de la réponse

# In[84]:

r.status_code


# In[85]:

r.json()


# In[86]:

results = r.json()['results']
len(results)


# In[90]:

[result['geometry']['location_type'] for result in results]


# In[ ]:




# In[97]:

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=prefecture,+yvelines')


# In[98]:

r


# In[99]:


r.json()


# In[ ]:



