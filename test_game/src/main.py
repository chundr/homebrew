import bge

#sample logic for controllers and collision
cont = bge.logic.getCurrentController()
own = cont.owner

if cont.sensors['Collision'].positive:
    cont.sensors['Collision'].hitObjectList[0].setParent(own.name, 1, 1)

