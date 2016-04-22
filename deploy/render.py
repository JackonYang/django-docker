# -*- Encoding: utf-8 -*-
import codecs
from os.path import join, dirname, abspath, basename
from jinja2 import Environment, FileSystemLoader


PROJECT_DIR = dirname(dirname(abspath(__file__)))
project_name = basename(PROJECT_DIR)

template_dir = join(PROJECT_DIR, 'deploy/templates')
env = Environment(loader=FileSystemLoader(template_dir))


def render_nginx_conf(server_name, port):
    nginx_file = join('/etc/nginx/sites-enabled', '%s.conf' % project_name)
    params = {
        'server_name': server_name,
        'port': port,
        'uwsgi_params_file': join(PROJECT_DIR, 'deploy/uwsgi_params'),
        'static_root': join(PROJECT_DIR, 'backend/static'),
        'media_root': join(PROJECT_DIR, 'backend/media'),
        }

    template = env.get_template('nginx.conf')
    with codecs.open(nginx_file, 'w', 'utf8') as f:
        f.write(template.render(**params))


if __name__ == '__main__':
    render_nginx_conf(server_name='localhost', port=3011)
