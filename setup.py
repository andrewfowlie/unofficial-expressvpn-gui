from setuptools import setup

setup(
    name="xv",
    install_requires=['PySimpleGUI '],
    version="0.0.1",
    scripts=['xv'],
    data_files = [('share/applications', ['xv.desktop']), ('share/icons', ['Gnome-security-medium.svg'])]
)

