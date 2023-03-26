from setuptools import setup, find_packages

setup(name='aibou',
      description='A turn-based CLI monster battle game',
      url='https://github.com/jakekrol/aibou',
      author='Jake Krol',
      license='MIT',
      version='0.1',
      classifiers=[
          'Topic :: Games/Entertainment :: Turn Based Strategy',
          'Development Status :: 2 - Pre-Alpha'
          ],
      scripts=['src/aibou-game.py'],
      packages=find_packages(),
      include_package_data=True
      )
