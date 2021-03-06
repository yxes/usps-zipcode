from distutils.core import setup

"""
  Latest Major Update
    * initial working commit
"""
setup(
    name="USPSZipCode",
    version="0.0.2",
    packages=[
        'yxes',
        'yxes.usps'
    ],
    install_requires=[
        'requests>=2.25.1',
        'xmltodict>=0.12.0',
        'yxes-config-find-dir@git+git://github.com/yxes/yxes-config-find_dir'
    ],
    include_package_data=True
)
