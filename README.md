# Purpose
Code to rip a sprite sheet from a directory of dota 2 images.

# Intro
This code expects a few things that are gitignored for simplicity:

1. A directory to look in for images ('items/' by default)
2. An output directory called ('assets/' by default)

These are adjustable at the top of the code.

Further, there are some hidden assumptions:

1. All images are the same height and width
2. You want all the images in the input directory included

You should probably hack at the code a bit if these assumptions are not suitable for you.

# Next Steps
Testing would probably be good.

Minification of png (resolution downsampling) is currently manual.  Manual things are bad.
