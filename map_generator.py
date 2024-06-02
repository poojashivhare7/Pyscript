import folium
import geopandas as gpd
from IPython.display import display
import os

# Load the world map
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filter for Europe
europe = world[world['continent'] == 'Europe']

# List of European countries
european_countries = europe['name'].tolist()

def generate_map(selected_countries):
    # Highlight selected countries
    highlight_countries = europe[europe['name'].isin(selected_countries)]
    
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
    
    # Save and display the map
    map_path = "interactive_map.html"
    m.save(map_path)
    display(m)
    return map_path

def save_map():
    map_path = "interactive_map.html"
    if os.path.exists(map_path):
        with open(map_path, 'r') as f:
            content = f.read()
        with open('/mnt/data/interactive_map.html', 'w') as f:
            f.write(content)
        print("Map saved successfully!")
    else:
        print("No map to save.")

# Populate dropdown with European countries
def populate_dropdown():
    import js
    select = js.document.getElementById("countrySelect")
    for country in european_countries:
        option = js.document.createElement("option")
        option.text = country
        option.value = country
        select.add(option)

populate_dropdown()
