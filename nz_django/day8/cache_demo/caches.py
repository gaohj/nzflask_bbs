from django.core.cache import cache


def set(token,key,value,timeout=60*60*24*7):
    return cache.set(token,key,value)
