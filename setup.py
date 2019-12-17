import setuptools

setuptools.setup(
    name="kinematics2d",
    version="0.1",
    description="A basic 2-dimensional point-kinematics library for Python 3.",
    url="https://gitlab.com/dagozilla/msl/kinematics2d",
    author="Faza Fahleraz",
    author_email="ffahleraz@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=["numpy"],
)

