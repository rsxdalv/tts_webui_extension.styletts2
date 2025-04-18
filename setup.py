import setuptools

setuptools.setup(
    name="extension_styletts2",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="StyleTTS2 is a text-to-speech model that generates high-quality speech with controllable style",
    url="https://github.com/rsxdalv/extension_styletts2",
    project_urls={},
    scripts=[],
    install_requires=[
        "styletts2 @ https://github.com/rsxdalv/StyleTTS2/releases/download/v0.1.8/styletts2-0.1.8-py3-none-any.whl",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
