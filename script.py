# python program
import urllib

source = 'https://unstats.un.org/unsd/amaapi/api/file/1'
archive = 'Download-GDPcurrent-NCU-countries.xlsx'

urllib.urlretrieve(source, archive)

