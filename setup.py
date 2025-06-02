from setuptools import setup, find_packages

setup(
    name='nicewoo',
    version='0.1.0',
    author='우성현',
    author_email='wshyun314@naver.com',
    description='A text processing utility package for stopword removal, keyword extraction, summarization, and language detection',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/WooMongGae/nicewoo',
    project_urls={
        'Documentation': 'https://woomonggae.github.io/nicewoo/',
        'Source': 'https://github.com/WooMongGae/nicewoo',
        'Tracker': 'https://github.com/WooMongGae/nicewoo/issues',
    },
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'nltk',
        'scikit-learn',
        'langdetect',
        'sumy',
        'numpy<2.0.0',
        'scipy<1.14.0',
        'gensim==4.3.3'
    ],
    include_package_data=True,
)
