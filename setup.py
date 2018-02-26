from setuptools import setup
import glob
import os
import sys
from hera_analysis import version
import json

data = [version.git_origin, version.git_hash, version.git_description, version.git_branch]
with open(os.path.join('hera_analysis', 'GIT_INFO'), 'w') as outfile:
    json.dump(data, outfile)

def package_files(package_dir,subdirectory):
    # walk the input package_dir/subdirectory
    # return a package_data list
    paths = []
    directory = os.path.join(package_dir, subdirectory)
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            path = path.replace(package_dir + '/', '')
            paths.append(os.path.join(path, filename))
    return paths
data_files = package_files('hera_analysis','data')

setup_args = {
    'name': 'hera_analysis',
    'author': 'Nick Kern',
    'url': 'https://github.com/nkern/hera_analysis',
    'license': 'BSD',
    'description': 'Science-level code for HERA data analysis',
    'package_dir': {'hera_analysis': 'hera_analysis'},
    'packages': ['hera_analysis'],
    'include_package_data': True,
    'scripts': [],
    'version': version.version,
    'package_data': {'hera_analysis': data_files},
    'zip_safe': False,
}


if __name__ == '__main__':
    apply(setup, (), setup_args)
