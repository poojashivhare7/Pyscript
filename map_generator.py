import folium
import geopandas as gpd
 
# Load the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
 
# Filter for Europe and the specific countries
europe = world[world['continent'] == 'Europe']
highlight_countries = europe[europe['name'].isin(['Ireland', 'Latvia', 'Hungary'])]
 
# Create a folium map centered around Europe
m = folium.Map(location=[54.5260, 15.2551], zoom_start=4, tiles='cartodbpositron', control_scale=True)
 
# Add the countries boundaries to the map
folium.GeoJson(europe, style_function=lambda x: {'fillColor': 'lightgrey', 'color': 'black', 'weight': 0.5}).add_to(m)
folium.GeoJson(highlight_countries, style_function=lambda x: {'fillColor': 'yellow', 'color': 'blue', 'weight': 2}).add_to(m)
 
# Add a title
title_html = '''
<h3 align="center" style="font-size:20px"><b>Missing Footprints</b></h3>
             '''
m.get_root().html.add_child(folium.Element(title_html))
 
# Save the map to an HTML file
m.save('missing_footprints.html')
 
# Display the map (uncomment the following line if running in a Jupyter notebook)
#m
