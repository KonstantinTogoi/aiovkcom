from setuptools import find_packages, setup


setup(
    name='aiovkcom',
    version='0.0.5',
    author='Konstantin Togoi',
    author_email='konstantin.togoi@protonmail.com',
    url='https://github.com/KonstantinTogoi/aiovkcom',
    description='vk.com Python REST API wrapper',
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires='aiohttp>=3.0.0',
    setup_requires=['pytest-runner'],
    tests_require=['pytest-asyncio', 'pytest-localserver'],
    keywords=['vk.com rest api asyncio'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
