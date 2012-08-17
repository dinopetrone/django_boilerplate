import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'www.settings'


from win8core import ioc
container = ioc.container
rs = container.WordCloudService()
rs.clear_cloud()