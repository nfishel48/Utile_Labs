from django_hosts import patterns, host

host_patterns = patterns('',
    host('', 'main.urls', name = 'main'),
    host('support', 'support.urls', name = 'support'),
)
