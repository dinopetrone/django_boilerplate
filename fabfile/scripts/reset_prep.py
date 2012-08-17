import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'www.settings'


from win8core.repos.django.models import Show, CastMember



s = Show()
s.title = 'soa'
s.twitter_hash = '#SOA'
s.getglue_id = 'tv_shows/american_horror_story'
s.facebook_id = '17432988290'
s.save()

c = CastMember()
c.name = 'Katey Sagal' 
c.twitter_handle = 'Kateylous'
c.show = s
c.save()

c = CastMember()
c.name = 'Ryan Hurst' 
c.twitter_handle = 'RamboDonkeyKong'
c.show = s
c.save()


