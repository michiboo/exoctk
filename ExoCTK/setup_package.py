from distutils.extension import Extension

def get_package_data():
    return {'ExoCTK': ['data/*', 'data/images/*', 'data/core/*', 'data/core/modelgrid/*', 'data/contam_visibility/*']}
