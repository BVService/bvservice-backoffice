from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='bvservice-backoffice',
      version='0.1',
      description='',
      long_description=readme(),
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering',
      ],
      keywords='',
      url='http://bvservice.fr',
      author='Jean-Christophe Fabre',
      author_email='jean-christophe.fabre@inra.fr',
      license='GPLv3',
      packages=['bvservice'],
      scripts=['BVservice-cli.py'],
      install_requires=['argparse','datetime'],
      package_data={
        'bvservice' : ['resources/templates/preparation/*','resources/templates/scenarios/*'],
      },
      include_package_data=True,
      zip_safe=False)
