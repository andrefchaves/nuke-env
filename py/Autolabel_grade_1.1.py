###    Auto Grade labeler that displays which knobs have changes
###    
###    Autolabel_grade_v1_1.py
###    
###    15/03/2019 // Andre F. Chaves

import nuke

def GradeLabel():

    # keep node indicators
    ind = nuke.expression("(keys?1:0)+(has_expression?2:0)+(clones?8:0)+(viewsplit?32:0)")
    if int(nuke.numvalue("maskChannelInput", 0)) :
        ind += 4
    if int(nuke.numvalue("this.mix", 1)) < 1:
        ind += 16
    nuke.knob("this.indicators", str(ind))
    ###

    # get the node
    node = nuke.thisNode()
    
    if node.Class() == "Grade":

        # sets autolabel to node name
        autoLabel = node.name()

        # check if values are zero'ed or not
        BP = ('BP' if node['blackpoint'].value() != 0 else None)
        WP = ('WP' if node['whitepoint'].value() != 1 else None)
        Lift = ('Lift' if node['black'].value() != 0 else None)
        Gain = ('Gain' if node['white'].value() != 1 else None)
        Multiply = ('Multiply' if node['multiply'].value() != 1 else None)
        Offset = ('Offset' if node['add'].value() != 0 else None)
        Gamma = ('Gamma' if node['gamma'].value() != 1 else None)

        # creates list
        knobs = [BP, WP, Lift, Gain, Multiply, Offset, Gamma]

        # if value inside list != None, add to autoLabel
        for knob in knobs:
            if knob!=None:
                autoLabel = autoLabel + '\n' + knob

        # adds custom user label if exists
        if node['label'].value():
            autoLabel = autoLabel + '\n' + node['label'].value()
                
        return autoLabel


nuke.addAutolabel( GradeLabel, nodeClass= 'Grade' )
