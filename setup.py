from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()



setup(
  name = 'fastencode',         # How you named your package folder (MyLib)
  packages = ['fastencode'],   # Chose the same as "name"
  version = '1.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An easy way to use different encoding: bytes, hex, ascii array, binary, long, base64',   # Give a short description about your library
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 'ES3',                   # Type in your name
  author_email = 'ourteamscare@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/elyassaf/Easy-Encoding/archive/refs/tags/v_1.3.tar.gz',    # I explain this later on
  keywords = ['encoding', 'hex', 'bytes', 'binary representation', 'decoding', 'ascii', 'base64'],   # Keywords that define your package best
  install_requires=['typing'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
