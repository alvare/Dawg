from django import template
from django.conf import settings
from re import sub, search

register = template.Library()

@register.filter()
def img_tags(text, art):
	text = sub('\[TRUNC\]', '', text)
	verse_replace = text
	both_replace = text
	if art.verse:
		width = 500 if art.verse.width > 500 else art.verse.width
		verse_replace = sub('\[VERSE\]', '<img src="'+settings.MEDIA_URL+art.verse.name+'" width="'+str(width)+'" alt="'+search('\/(.+)\.', art.verse.name).group(1)+'" />', text)
	both_replace = verse_replace
	if art.coda:
		width = 500 if art.coda.width > 500 else art.coda.width
		both_replace = sub('\[CODA\]', '<img src="'+settings.MEDIA_URL+art.coda.name+'" width="'+str(width)+'" alt="'+search('\/(.+)\.', art.coda.name).group(1)+'" />', verse_replace)
	return both_replace

@register.filter()
def truncate_magic(text, article_id):
	return sub('\[TRUNC\].*', '<a class="continue" href="'+str(article_id)+'"> Continue ...</a>', text)
