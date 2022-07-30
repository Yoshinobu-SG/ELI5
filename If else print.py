import time
a=float(input('Enter the value: '))
if a > 0:
    b="Top"
else:
    b="Bottom"
while a > 0:
    time.sleep(1)
    print(b)
if a < 0:
    b="Left"
else:
    b="Right"
    ### right overlaps on top of "Top" because it is further down the line sort of.
    #Need to find a good way to explain
    #So far, my understanding of this script is that integer and float could be used but
    #Whatever that appears further down the line would take prescedence over those that came before
    #I'm not really sure of what i learned with this so i'll have to try to combine this fn with others
print(b*3)
