from distutils.core import setup, Extension

perlin = Extension('perlin', sources = ['perlin.c', 'perlinmodule.c'])

setup (name = 'perlin',
       version = 'help',
       description = "C implementation of the 4D Perlin noise algorithm.\nex: perlin.noise(x,y,z,w)",
       ext_modules = [perlin])