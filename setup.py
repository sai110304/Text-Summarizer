import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
__version__ = "0.0.0"

REPONAME = "Text-Summarizer"
AUTHORNAME="sai110304"
SRCREPO="TextSummarizer"
AUTHOREMAIL="skr110304@gmail.com"

setuptools.setup(
    name=SRCREPO,
    version=__version__,
    author=AUTHORNAME,
    author_email=AUTHOREMAIL,
    description="small python package for NLP task",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHORNAME}/{REPONAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHORNAME}/{REPONAME}/issues",
    }
)
