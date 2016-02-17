#!/usr/bin/env python


def main():
    from setuptools import setup, find_packages

    version_dict = {}
    init_filename = "wimpy/version.py"
    exec(compile(open(init_filename, "r").read(), init_filename, "exec"),
            version_dict)

    setup(name="wimpy",
          version=version_dict["VERSION_TEXT"],
          description="A data model for the description of "
          "(initial) boundary value problems, plus transformations",
          long_description=open("README.rst", "rt").read(),
          author="Test",
          author_email="test",
          license="test",
          url="http://wiki.tiker.net/IBVP",
          classifiers=[
              'Development Status :: 3 - Alpha',
              'Intended Audience :: Developers',
              'Intended Audience :: Other Audience',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Natural Language :: English',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2.5',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.3',
              'Programming Language :: Python :: 3.4',
              'Topic :: Scientific/Engineering',
              'Topic :: Scientific/Engineering :: Information Analysis',
              'Topic :: Scientific/Engineering :: Mathematics',
              'Topic :: Scientific/Engineering :: Visualization',
              'Topic :: Software Development :: Libraries',
              'Topic :: Utilities',
              ],

          packages=find_packages(),
          install_requires=[
              "numpy>=1.5",
              "pytools>=2014.1",
              "pymbolic>=2014.1",
              "pytest>=2.3",
              "six",
              ])


if __name__ == '__main__':
    main()
