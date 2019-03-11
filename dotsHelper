import nuke

def DotLabel():
    n = nuke.thisNode()
    currentVal = n['label'].value()
    if n.Class() == "Dot":
        autoLabel = ''
    try:
        if nuke.selectedNode().inputs() == 1 and nuke.thisNode()['hide_input'].value() == 1:
                autoLabel = nuke.tcl("value this.input.name") + '\n' + currentVal            
        else:
                autoLabel = currentVal
    except:
        autoLabel = currentVal

    return autoLabel
 
nuke.addUpdateUI(DotLabel)
nuke.addAutolabel(DotLabel, nodeClass = 'Dot')
