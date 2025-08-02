from setuptools import setup, find_packages

setup(
    name="cli-tool",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "cli-tool = cli_tool.__main__:main",
        ],
    },
    install_requires=[
        "googlesearch-python",
        "geopy",
        "requests",
    ],
    description="Multi‑command CLI tool: google search / location / weather",
)
