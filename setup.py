from setuptools import setup, find_packages

setup(
    name="simple_seo_toolkit",
    version="1.0.0",
    author="Python 2.7",
    description="A comprehensive SEO optimization toolkit.",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    entry_points={
        "console_scripts": [
            "seo-toolkit = seo_toolkit.cli:main"
        ]
    }
)
