from setuptools import setup, find_packages

setup(
    name="wecom_rss",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "feedparser",
        "requests",
        "schedule",
    ],
    entry_points={
        'console_scripts': [
            'wecom_rss = wecom_rss.bot:main',
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="A bot for pushing RSS updates to WeCom (WeChat Work)",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/wecom_rss",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
