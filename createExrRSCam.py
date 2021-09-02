''' 
I just fixed the syntax to work with the latest RS versions 3.0.xx and Nuke 13

The main createExrCamVray translation comes from user JanB at Redshift/Maxon forum (https://redshift.maxon.net/topic/2249/exr-metadata-done/28)
Original CamVRay.py: https://github.com/throb/vfxpipe/blob/master/nuke/fxpipenukescripts/createExrCamVray.py

-

Add to Menu.py:
import createExrRSCam
m = menubar.addMenu("RS")
m.addCommand('createExrRSCam', 'createExrRSCam.createExrRSCam()')
'''

import math
import nuke

#Create a camera node based on RS metadata.

def createExrRSCam():
    node = nuke.selectedNode()

    if "Read" not in node.Class():
        nuke.message('Please select a RS rendered EXR.')
        return
    
    mDat = node.metadata()
    reqFields = ['exr/rs/camera/%s' % i for i in ('fov', 'aperture', 'transform')]
    if not set( reqFields ).issubset( mDat ):
        print('no metadata for camera found')
        return
    
    first = node.firstFrame()
    last = node.lastFrame()
    ret = nuke.getFramesAndViews( 'Create Camera from Metadata', '%s-%s' %( first, last )  )
    fRange = nuke.FrameRange( ret[0] )
    
    cam = nuke.createNode( 'Camera2' )
    cam['useMatrix'].setValue( False )
    
    for k in ( 'focal', 'haperture', 'vaperture', 'translate', 'rotate'):
        cam[k].setAnimated()
    
    for curTask, frame in enumerate( fRange ):        
    
        # IB. If you get both focal and aperture as they are in the metadata, there's no guarantee
        # your Nuke camera will have the same FOV as the one that rendered the scene (because the render could have been fit to horizontal, to vertical, etc)
        # Nuke always fits to the horizontal aperture. If you set the horizontal aperture as it is in the metadata,
        # then you should use the FOV in the metadata to figure out the correct focal length for Nuke's camera
        # Or, you could keep the focal as is in the metadata, and change the horizontal_aperture instead.
        # I'll go with the former here. Set the haperture knob as per the metadata, and derive the focal length from the FOV
        
        val = node.metadata()['exr/rs/camera/aperture']
        
        #camera units are inches, mm in nuke
        valh = val[0]*25.4
        valv = val[1]*25.4

        cam['haperture'].setValueAt(float(valh),frame)
        cam['vaperture'].setValueAt(float(valv),frame)

        fov = node.metadata()['exr/rs/camera/fov'] # get camera FOV
        
        focal = (valh / (2 * math.tan(math.pi * fov / 360)))

        cam['focal'].setValueAt(float(focal),frame)
        cam['haperture'].setValueAt(float(valh),frame)
        cam['vaperture'].setValueAt(float(valv),frame)

        matrixCamera = node.metadata( 'exr/rs/camera/transform', frame) # get camera transform data

        #Create a matrix to shove the original data into 
        matrixCreated = nuke.math.Matrix4()
        
        for k,v in enumerate(matrixCamera):
            matrixCreated[k] = v
        
        matrixCreated.rotateY(math.radians(-180)) # backwards

        translate = matrixCreated.transform(nuke.math.Vector3(0,0,0))  # Get a vector that represents the camera translation   
        rotate = matrixCreated.rotationsZXY() # give us xyz rotations from cam matrix (must be converted to degrees)

        cam['translate'].setValueAt(float(translate.x),frame,0)
        cam['translate'].setValueAt(float(translate.y),frame,1)
        cam['translate'].setValueAt(float(translate.z),frame,2)
        cam['rotate'].setValueAt(float(math.degrees(rotate[0])),frame,0)
        cam['rotate'].setValueAt(float(math.degrees(rotate[1])),frame,1) 
        cam['rotate'].setValueAt(-float(math.degrees(rotate[2])),frame,2) 

#createExrRSCam()
