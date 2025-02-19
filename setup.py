from setuptools import setup, find_packages

setup(
    name="ungoliant",
    version="0.1.0",
    packages=find_packages(),
    description="AI Agent for Investment Data",
    author="Korey Stafford",
    author_email="kmstafford1@gmail.com",
    url="https://github.com/PDXKor/ungoliant",  # Optional
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "langchain-openai",
        "langgraph",
        "polygon-api-client",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ungoliant=ungoliant.__main__:main",
        ],
    },
)