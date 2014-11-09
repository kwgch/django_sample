# -*- coding: utf-8 -*-

from django.template import RequestContext, loader

from django.http import HttpResponse

def main(request):
  return HttpResponse(u"焼肉食べたい！")

def harami(request):
  context = RequestContext(request, {})
  template = loader.get_template('yakiniku.html')
  return HttpResponse(template.render(context))