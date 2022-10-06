import pixray
for i in range(100):
    pixray.run("a painting of a demon attacking a demon, by Simon S. Andersen, Doom1, #pixelart", drawer="pixel", quality="best", aspect="square", 
    save_intermediates=False, palette="red->white", outdir="outputs/pixel/", output="frame%03d.png"%i, iterations=10)
    palette: "[white,black,red]"
    size="[144, 144]"
   
