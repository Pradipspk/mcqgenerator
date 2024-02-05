from setuptools import find_packages, setup

setup(
    name = 'mcqgenerator',
    version = '0.0.1',
    author = 'Pradip Sapkota',
    author_email = 'sapkotapradip111@gmail.com',
    install_requires =['openai', 'langchain','streamlit','python-dotenv','PyPDF2'],
    packages = find_packages()   #responsible for finding out the local packages(__init__ file is considered as package)
)