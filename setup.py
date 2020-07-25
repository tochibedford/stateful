from distutils.core import setup
setup(
  name = 'stateful',         # How you named your package folder (MyLib)
  packages = ['stateful'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='Apache License 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Implementing stateful objects in python',   # Give a short description about your library
  author = 'tochibedford',                   # Type in your name
  author_email = 'tochukwu.bedford@stu.cu.edu.ng',      # Type in your E-Mail
  url = 'https://github.com/tochibedford/stateful',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/tochibedford/stateful/archive/0.2.tar.gz',    # I explain this later on
  keywords = ['states', 'objects', 'new_types'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
