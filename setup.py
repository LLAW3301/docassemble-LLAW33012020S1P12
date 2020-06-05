import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012020S1P12',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# P12\r\nCode for Hutt Street Centre - NDIS Navigator \r\n\r\nThis application is created for Hutt Street Centre for the purpose of assisting staff members of the Hutt Street Centre in assessing the eligibility of those seeking to apply for the NDIS and guide them through a disability assessment (which will be the WHODAS assessment). This application will work as an online questionnaire, compiling data from the answered questions into an easy-to-read information sheet for the Hutt Street Centre staff to view. This information sheet will hold no legal value but will be of extreme value in having a more rigorous assessment for clients who have disabilities, by providing a formal and standardised process for staff members to follow and then determine the clients’ eligibility for the NDIS. The information sheet can also be used as a supporting evidence in clients’ NDIS application. By creating a simple questionnaire application, the Hutt Street Centre staff members will be able to reach a decision as to whether a client may or may not be eligible for the NDIS. \r\n',
      long_description_content_type='text/markdown',
      author='Mark Ferraretto',
      author_email='mark.ferraretto@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012020S1P12/', package='docassemble.LLAW33012020S1P12'),
     )

