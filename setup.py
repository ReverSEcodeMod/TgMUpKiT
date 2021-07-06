import setuptools

setuptools.setup(
    name="EmLeetkXApp",
    version="1.0",
    author="SamsNotX",
    description="A Telegram Bot written in Python to mirror files to Telegram",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SamsNotX/EmLeetkXApp",
    project_urls={
        "Bug Tracker": "https://github.com/SamsNotX/EmLeetkXApp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    packages=setuptools.find_packages(),
    install_requires=open('requirements.txt', 'r', encoding='utf-8').read().split('\n'),
    scripts=['start.sh'],
    python_requires=">=3.8",
)