import folium
MAPFILE='data\\map1.html'

if __name__ == '__main__':
    map = folium.Map(location=(35.61, -82.44), zoom_start=5)
    map.save(MAPFILE)


