import setuptools
setuptools.setup(
    name='cmlbootstrap',
    packages=setuptools.find_packages(),
    version='0.0.1',
    license='MIT',
    description='Wrapper class to launch jobs, experiments, applications and models on Cloudera Machine Learning',
    author='Cloudera',
    url='https://github.com/fastforwardlabs/cmlbootstrap',
    download_url='https://github.com/fastforwardlabs/cmlbootstrap/archive/v0.0.1.tar.gz',
    keywords=['CDSW', 'Cloudera', 'Machine Learning'],
    # install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Cloudera Machine Learning :: CDSWs',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
