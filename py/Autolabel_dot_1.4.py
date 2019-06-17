###    Auto Dot labeler when input is hidden
###    
###    Autolabel_dot.py v1.4
###    
###    21/03/2019 // Andre F. Chaves

import nuke


def DotLabel():
    
    # get the node
    node = nuke.thisNode()

    if node.Class() == "Dot":

        # user's label input value
        if node['label'].value() == '':
            currentVal = node['label'].value()
        else:
            currentVal = ('<align=left>' + node['label'].value())

        
        # if dot has input
        if node.inputs() == 1:

            # if input is hidden
            if node['hide_input'].value() == 1:
                autoLabel = ('<b><i>' + nuke.tcl("value this.input.name") + '</i></b>' + '\n' + currentVal)
            else:
                autoLabel = currentVal
        else:
            autoLabel = currentVal
            
        return autoLabel


nuke.addAutolabel(DotLabel, nodeClass = 'Dot')
