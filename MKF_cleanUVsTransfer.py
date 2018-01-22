#arturoalcibia@hotmail.com
from __future__ import division
import maya.cmds as cmds
def main():
	geometry = []
	contRigGeo = 0
	for g in cmds.ls(et='transform', l=True):
		if g.find('MD') != -1:
			if cmds.listRelatives(g, s=True) != None:
				geometry.append(g)
	for rigGeo in geometry:
		if rigGeo.find(':') == -1:
			contRigGeo += 1
			for sdGeo in geometry:
				if sdGeo.find(':') != -1:
					if rigGeo.split('|')[-1] == sdGeo.split('|')[-1].split(':')[-1]:
						origShape = getOrigShape(rigGeo)
						if origShape != 'error':
							sdGeoShape = cmds.listRelatives(sdGeo, s=True)
							toggleUseIntermediate(origShape)
							transferUVS(sdGeo, origShape)
							deleteHistory(origShape)
							toggleUseIntermediate(origShape)


	#unloadReference()
	return contRigGeo
def getOrigShape(geo):
	try:
		shapes = cmds.listRelatives(geo, s=True)
		origShape = ''
		boolOrigShape = False
		if len(shapes) > 1:
			for shape in shapes:
				if shape.find('Orig') != -1:
					origShape = shape
					boolOrigShape = True

		if boolOrigShape == True:
			return origShape
		else:
			return 'error'
	except:
		return 'error'
def toggleUseIntermediate(shape):
	state = cmds.getAttr(shape + '.intermediateObject')
	if state == True:
		state = cmds.setAttr(shape + '.intermediateObject', False)
	else:
		state = cmds.setAttr(shape + '.intermediateObject', True)
def deleteHistory(shape):


	cmds.delete(shape, ch = True)
def transferUVS(sd, rig):


	cmds.transferAttributes(sd, rig, transferUVs=2, sampleSpace=4)
def unloadReference():
	refs = cmds.file(q=True, r=True)
	for ref in refs:
		cmds.file(ref, removeReference=True)
geo = main()

print 'Se transfirieron UVs de ' + str(geo) + ' geometrias',