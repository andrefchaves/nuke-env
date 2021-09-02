# Nuke-Env

## Python Scripts

### createExrRSCam
Create a camera node based on RS metadata.
I just did some really small UX fix and fixed the syntax to work with the latest RS versions 3.0.xx and Nuke 13 (Python 3)
All text and the main createExrCamVray translation comes from user JanB at Redshift/Maxon forum (https://redshift.maxon.net/topic/2249/exr-metadata-done/28)


### Autolabel_Dots v1.4
Automatically adds label to dot node when you hide the input. Label displays last connected node.
Useful to organize messy node trees.

### Autolabel_Dots v2 _ WIP
This is a work in progress. The plan is to display the last connected node ignoring dot nodes.
I'm having some errors when hiding and unhiding the input. It doesn't seem to refresh the input process.

### Autolabel_Grade v1.1
Automatically adds label with knobs that have changes.
Useful if you have multiple Grade nodes with different knob changes in each one. It's not the best workflow but useful if you do different color processes in different nodes, i.e. Black Point/White Point on one then Gamma on another..
