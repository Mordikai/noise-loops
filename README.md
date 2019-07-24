# noise-loops
My experiments in using 4D Perlin noise to create looping GIFs.
Derived from and inspired by Étienne Jacob, in particular [this tutorial](https://necessarydisorder.wordpress.com/2017/11/15/drawing-from-noise-and-then-making-animated-loopy-gifs-from-there/) in which he describes his techniques.

The 4D Perlin noise algorithm was copied, with only a couple alterations, from [Ken Perlin's webpage.](https://mrl.nyu.edu/~perlin/noise/ImprovedNoise4D.java) Do note that there's a typo in his posted source code; see my comments in source/perlin.c

The tracers.py script takes a while to run. If you don't have 5 hours to wait, I'd recommend changing some of the hardcoded options at the top of the file. Lower the resolution, increase the frame duration(AKA lowering the framerate), or decrease the number of frames. If you just want a test frame, change line 8 to "test_frame = True". I'll eventually implement some command flags to make all of this less clunky.

Plans for the next version are to move more of the implementation into C to try to speed up the rendering. It should benefit heavily from multithreading. I might also make a version that uses [AVX2 registers](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions#AVX2), though I am less certain as to how much that would help.

### REQUIREMENTS
[PIL](https://pillow.readthedocs.io/en/stable/)
[tqdm](https://github.com/tqdm/tqdm)
[numpy](https://numpy.org/)
[ImageMagick](https://imagemagick.org/index.php), at least until I fix the stitching error.

### BUILDING THE PERLIN MODULE

Run "python setup.py" from the source directory.
