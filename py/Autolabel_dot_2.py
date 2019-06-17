###    Auto Dot labeler when input is hidden
###    
###    Autolabel_dot.py v2
###    
###    xx/xx/xxxx // Andre F. Chaves

import nuke

#global
dotNodes = []

# check for nodes before current, returns first node that's not a Dot
def check(thisnode):
    for n in thisnode.dependencies():
        if n.Class() != 'Dot':
            dotNodes.append(n)
            break
        check(n)
    return n


# label magic
def DotLabel():

    # get the node
    node = nuke.thisNode()

    # user's label input value
    currentVal = node['label'].value()

    if node.Class() == "Dot":
        
        autoLabel = currentVal
        
        # if has input and it's hidden
        if node.inputs() == 1 and node['hide_input'].value() == 1:
            try:

                # get last node that's not a dot
                check(node)

                # get the name
                for x in dotNodes:
                    n = x['name'].value()

                # set the name + dot label
                autoLabel = (n + '\n' + currentVal)

            except:
                pass

        return autoLabel

nuke.addAutolabel(DotLabel, nodeClass = 'Dot')
