from setuptools import setup, find_packages

setup(
    name="tradeint-vn-api",
    version="0.1.0",
    description="Python client and reference package for TradeInt Vietnam (tradeint.vn)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="TradeInt Vietnam",
    author_email="dev@tradeint.vn",
    url="https://tradeint.vn",
    project_urls={
        "Homepage": "https://tradeint.vn",
        "Features": "https://tradeint.vn/features/",
        "News": "https://tradeint.vn/news/",
        "Source": "https://github.com/ttt-tom/tradeint-python-sdk",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
    python_requires=">=3.8",
)
