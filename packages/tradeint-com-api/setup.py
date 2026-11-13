from setuptools import setup, find_packages

setup(
    name="tradeint-com-api",
    version="0.1.0",
    description="Python client and reference package for TradeInt Global Trade Intelligence (tradeint.com)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="TradeInt Global",
    author_email="dev@tradeint.com",
    url="https://www.tradeint.com",
    project_urls={
        "Homepage": "https://www.tradeint.com",
        "Resources": "https://www.tradeint.com/resources/",
        "Insights": "https://tradeint.com/insights/blogs/",
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
