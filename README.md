# noise-loops
My experiments in using 4D Perlin noise to create looping GIFs.
Derived from and inspired by Étienne Jacob, in particular [this tutorial](https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/) in which he describes his techniques.
The 4D Perlin noise algorithm was copied, with only a couple alterations, from [Ken Perlin's webpage.](https://mrl.nyu.edu/~perlin/noise/ImprovedNoise4D.java) Do note that there's a typo in his posted source code; see my comments in source/perlin.c

REQUIREMENTS:
[PIL](https://pillow.readthedocs.io/en/stable/)
[tqdm](https://github.com/tqdm/tqdm)
[numpy](https://numpy.org/)

BUILDING THE PERLIN MODULE
Run "python setup.py" from the source directory.
