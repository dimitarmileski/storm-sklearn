{% set p  = salt['pillar.get']('storm', {}) %}

{%- set home           = p.get('home', default_dl_opts) %}
{%- set source_url     = p.get('source_url', default_dl_opts) %}
{%- set version_name   = p.get('version_name', default_dl_opts) %}
{%- set dl_opts        = p.get('dl_opts', default_dl_opts) %}
{%- set prefix         = p.get('prefix', default_prefix) %}

{%- set storm_real_home = prefix + '/' + version_name %}

{%- set storm = {} %}
{%- do storm.update( {'version_name'    : version_name,
                      'source_url'      : source_url,
                      'dl_opts'         : dl_opts,
                      'prefix'          : prefix,
                      'home'            : home,
                      'storm_real_home' : storm_real_home
                  }) %}