import os


def playerIcons(poi):
    if poi['id'] == 'Player':
        poi['icon'] = "https://overviewer.org/avatar/{}".format(poi['EntityId'])
        return "Last known location for {}".format(poi['EntityId'])


# Only signs with "-- RENDER --" in them, and no others. Otherwise, people
# can't have secret bases and the render is too busy anyways.
def signFilter(poi):
    if poi['id'] in ['Sign', 'minecraft:sign']:
        if '-- RENDER --' in poi.values():
            return "\n".join([poi['Text1'], poi['Text2'], poi['Text3'], poi['Text4']])


worlds['minecraft'] = "/home/minecraft/server/world"
outputdir = "/home/minecraft/render/"
texturepath = "/home/minecraft/{}.jar".format(os.environ['MINECRAFT_VERSION'])

markers = [
    dict(name="Players", filterFunction=playerIcons),
    dict(name="Signs", filterFunction=signFilter)
]

renders["day"] = {
    'world': 'minecraft',
    'title': 'Day',
    'rendermode': 'normal',
    "dimension": "overworld",
    'markers': markers
}

renders["nether"] = {
    "world": "minecraft",
    "title": "Nether",
    "rendermode": 'nether',
    "dimension": "nether",
    'markers': markers
}

renders["overlay_slime"] = {
    'world': 'minecraft',
    'rendermode': [ClearBase(), SlimeOverlay()],
    'title': "Slime Chunk Overlay",
    "dimension": "overworld",
    'overlay': ["day"]
}
