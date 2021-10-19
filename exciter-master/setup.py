from setuptools import setup, find_packages

setup (name = "exciter",
       version = "0.3",
       license = "GPL",
       description='search, create, attack, force-in',
       author = "val (zvtyrdt.id)",
       author_email = "xnver404@gmail.com",
       url = "https://github.com/zevtyardt",
       install_requires=['requests'],
       packages=["exciter.lib", "exciter.removed", "exciter"],
       include_package_data=True,
       zip_safe=False,
       entry_points={'console_scripts': ['exciter=exciter.exciter:main']}
)

