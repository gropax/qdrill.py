from setuptools import setup

setup(name='qdrill',
      version='0.0.0',
      description='Generate drill audio file for language learning',
      url='http://www.github.com/gropax/qdrill.py.git',
      author='gropax',
      author_email='maximedelaudrin@gmail.com',
      license='MIT',
      packages=['qdrill'],
      scripts=['bin/qdrill', 'bin/qrec'],
      zip_safe=False)
