# Copyright (c) 2022 Itz-fork

import os
from re import findall
from setuptools import setup, find_packages

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Readme
if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readmeh:
        big_description = readmeh.read()
else:
    big_description = "Asynchronous API wrapper for the Nexa API"

# Version (Ref: https://github.com/pyrogram/pyrogram/blob/97b6c32c7ff707fd2721338581e7dad5072f745e/setup.py#L30)
with open("nexa_api/__init__.py", encoding="utf-8") as f:
    v = findall(r"__version__ = \"(.+)\"", f.read())[0]


setup(name="nexa_api",
      version=v,
      description="Asynchronous API wrapper for the Nexa API",
      url="https://github.com/Itz-fork/Nexa-API",
      author="Itz-fork",
      author_email="itz-fork@users.noreply.github.com",
      license="MIT",
      packages=find_packages(),
      download_url=f"https://github.com/Itz-fork/Fake-agent/releases/tag/{v}",
      keywords=["api wrapper", "nexa api"],
      long_description=big_description,
      long_description_content_type="text/markdown",
      include_package_data=True,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Education',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
      ],
      )
