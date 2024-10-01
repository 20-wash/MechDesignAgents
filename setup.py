from setuptools import setup, find_packages

setup(
    name='mechdesignagents',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'autogen',
        'cadquery',
        'ocp_vscode',
        'chromadb',
        'streamlit',
        'fenics',
        'matplotlib',
        'numpy',
        'scipy',
        'sympy',
        'requests',
        'pydantic',
        'typing_extensions',
        'openai',
        'langchain',
        'pinecone-client',
        'transformers',
        'sentence_transformers',
        'fastapi',
        'uvicorn',
        'python-multipart',
        'Pillow',
    ]
)