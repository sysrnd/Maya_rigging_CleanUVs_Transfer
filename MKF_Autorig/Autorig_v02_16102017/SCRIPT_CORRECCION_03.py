import maya.cmds as cmds
import maya.mel as mel

lado = 'IZQ'
var_lado = 0

while var_lado < 2:

	if var_lado == 1:
		lado = 'DER'


	#CREACION DE LOCATORS (COMIENZA)

	cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 0)

	cmds.spaceLocator(n='LOC_HOMBRO_%s_FK' %lado)
	cmds.spaceLocator(n='LOC_CODO_%s_FK' %lado)
	cmds.spaceLocator(n='LOC_MANO_%s_FK' %lado)

	cmds.parentConstraint('DRIVER_HOMBRO_%s_FK' %lado, 'LOC_HOMBRO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_HOMBRO_%s' %lado)
	cmds.parentConstraint('DRIVER_CODO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s' %lado)
	cmds.parentConstraint('DRIVER_MANO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

	cmds.delete('LOCATOR_CONSTRAIN_HOMBRO_%s' %lado, 'LOCATOR_CONSTRAIN_CODO_%s' %lado, 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

	cmds.select('LOC_HOMBRO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado)
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

	cmds.parent( 'LOC_MANO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado)
	cmds.parent( 'LOC_CODO_%s_FK' %lado, 'LOC_HOMBRO_%s_FK' %lado)

	cmds.parentConstraint('HOMBRO_%s_IK' %lado, 'LOC_HOMBRO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_HOMBRO_%s_ROTATE' %lado, mo =1)
	cmds.parentConstraint('CODO_%s_IK' %lado, 'LOC_CODO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_CODO_%s_ROTATE' %lado, mo =1)
	cmds.parentConstraint('MANO_%s_IK' %lado, 'LOC_MANO_%s_FK' %lado, st=["x","z","y"], name = 'LOCATOR_CONSTRAIN_MANO_%s_ROTATE' %lado, mo =1)



	cmds.setAttr('DRIVER_COLUMNA_TOP.SWITCH_IK_FK_%s' %lado, 1)

	cmds.spaceLocator(n='LOC_CODO_%s_IK' %lado)
	cmds.spaceLocator(n='LOC_MANO_%s_IK' %lado)

	cmds.parentConstraint('DRIVER_CODO_%s' %lado, 'LOC_CODO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s' %lado)
	cmds.parentConstraint('DRIVER_MANO_%s' %lado, 'LOC_MANO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

	cmds.delete('LOCATOR_CONSTRAIN_CODO_%s' %lado, 'LOCATOR_CONSTRAIN_MANO_%s' %lado)

	cmds.select('LOC_CODO_%s_IK' %lado, 'LOC_MANO_%s_IK' %lado)
	cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=0, pn=1) 

	cmds.pointConstraint('CODO_%s_FK' %lado, 'LOC_CODO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_CODO_%s_ROTATE_IK' %lado)
	cmds.parentConstraint('MANO_%s_FK' %lado, 'LOC_MANO_%s_IK' %lado, name = 'LOCATOR_CONSTRAIN_MANO_%s_ROTATE_IK' %lado, mo =1)

	cmds.editDisplayLayerMembers( 'no_tocar', 'LOC_HOMBRO_%s_FK' %lado, 'LOC_CODO_%s_FK' %lado, 'LOC_MANO_%s_FK' %lado, 'LOC_CODO_%s_IK' %lado, 'LOC_MANO_%s_IK' %lado)

	#CREACION DE LOCATORS (TERMINA)



	#CORRECION SWITCH RODILLA (COMIENZA)

	cmds.group('DRIVER_RODILLA_%s' %lado, n='GRP_DRIVER_RODILLA_%s' %lado)

	cmds.group('GRP_DRIVER_RODILLA_%s' %lado, n='GRP_PRC_DRIVER_RODILLA_%s' %lado)

	cmds.select('DRIVER_PIE_%s' %lado)

	cmds.addAttr(longName='SWITCH_RODILLA_%s' %lado, attributeType='enum', enumName='NONE:FOOT:MIDDLE', k=True)

	cmds.parentConstraint( 'DRIVER_PIE_%s' %lado, 'GRP_DRIVER_RODILLA_%s' %lado, mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_RODILLA_%s' %lado)

	cmds.parentConstraint( 'DRIVER_ROOT', 'GRP_PRC_DRIVER_RODILLA_%s' %lado, mo=1, name = 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s' %lado)


	cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
	cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 0)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))

	cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 1 )
	cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 1)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))

	cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 2 )
	cmds.setAttr( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), 0)
	cmds.setAttr( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, 1)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_RODILLA_%s.DRIVER_PIE_%sW0' %(lado, lado), cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))
	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CINTURA_RODILLA_%s.DRIVER_ROOTW0' %lado, cd='DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado))

	cmds.setAttr( 'DRIVER_PIE_%s.SWITCH_RODILLA_%s' %(lado, lado), 0 )

	#CORRECION SWITCH RODILLA (TERMINA)



	#CORRECION SWITCH HOMBROS (COMIENZA)

	cmds.spaceLocator(n='LOC_HOMBRO_%s' %lado)

	cmds.pointConstraint( 'HOMBRO_%s' %lado, 'LOC_HOMBRO_%s' %lado, name = 'POINT_CONSTRAIN_HOMBRO_%s' %lado)

	cmds.parent('DRIVER_HOMBRO_%s_FK' %lado, w=True)

	cmds.group('DRIVER_HOMBRO_%s_FK' %lado, n='GRP_DRIVER_HOMBRO_%s_FK' %lado)

	PX = cmds.getAttr('LOC_HOMBRO_%s.tx' %lado)
	PY = cmds.getAttr('LOC_HOMBRO_%s.ty' %lado)
	PZ = cmds.getAttr('LOC_HOMBRO_%s.tz' %lado)

	cmds.move(PX, PY, PZ, "GRP_DRIVER_HOMBRO_%s_FK.scalePivot" %lado,"GRP_DRIVER_HOMBRO_%s_FK.rotatePivot" %lado, absolute=True)

	cmds.parent( 'GRP_DRIVER_HOMBRO_%s_FK' %lado, 'DRIVER_COLUMNA_TOP')

	cmds.parentConstraint( 'LOC_HOMBRO_%s' %lado, 'GRP_DRIVER_HOMBRO_%s_FK' %lado, mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_HOMBRO_%s_TRANSLATE' %lado)

	cmds.parentConstraint( 'DRIVER_CLAVICULA_%s' %lado, 'GRP_DRIVER_HOMBRO_%s_FK' %lado, mo=1, st=["x","z","y"], name = 'PARENT_CONSTRAIN_HOMBRO_%s_ROTATE' %lado)

	cmds.select('DRIVER_HOMBRO_%s_FK' %lado)

	cmds.addAttr(longName='SWITCH', defaultValue=0, minValue=0, maxValue=1, k=True)


	cmds.setAttr( 'PARENT_CONSTRAIN_HOMBRO_%s_ROTATE.DRIVER_CLAVICULA_%sW0' %(lado,lado), 0)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_HOMBRO_%s_ROTATE.DRIVER_CLAVICULA_%sW0' %(lado,lado), cd='DRIVER_HOMBRO_%s_FK.SWITCH' %lado)

	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.SWITCH' %lado, 1 )
	cmds.setAttr( 'PARENT_CONSTRAIN_HOMBRO_%s_ROTATE.DRIVER_CLAVICULA_%sW0' %(lado,lado), 1)

	cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_HOMBRO_%s_ROTATE.DRIVER_CLAVICULA_%sW0' %(lado,lado), cd='DRIVER_HOMBRO_%s_FK.SWITCH' %lado)

	cmds.setAttr( 'DRIVER_HOMBRO_%s_FK.SWITCH' %lado, 0 )

	#CORRECION SWITCH HOMBROS (TERMINA)


	var_lado = var_lado+1

	pass



cmds.setAttr( 'DRIVER_HOMBRO_IZQ_FK.overrideEnabled', 1 )
cmds.setAttr( 'DRIVER_HOMBRO_IZQ_FK.overrideColor', 6 )

cmds.setAttr( 'DRIVER_HOMBRO_DER_FK.overrideEnabled', 1 )
cmds.setAttr( 'DRIVER_HOMBRO_DER_FK.overrideColor', 13 )

cmds.editDisplayLayerMembers( 'no_tocar', 'LOC_HOMBRO_IZQ', 'LOC_HOMBRO_DER')



#CORRECION SWITCH CABEZA (COMIENZA)

cmds.spaceLocator(n='LOC_CABEZA')

cmds.pointConstraint( 'DRIVER_CABEZA', 'LOC_CABEZA', name = 'POINT_CONSTRAIN_CABEZA')

cmds.parent('DRIVER_CABEZA', w=True)

cmds.group('DRIVER_CABEZA', n='GRP_DRIVER_CABEZA')

PX = cmds.getAttr('LOC_CABEZA.tx')
PY = cmds.getAttr('LOC_CABEZA.ty')
PZ = cmds.getAttr('LOC_CABEZA.tz')

cmds.move(PX, PY, PZ, "GRP_DRIVER_CABEZA.scalePivot","GRP_DRIVER_CABEZA.rotatePivot", absolute=True)

cmds.delete('LOC_CABEZA')

cmds.parent( 'GRP_DRIVER_CABEZA', 'MOVE_ALL')

cmds.parentConstraint( 'DRIVER_COLUMNA_TOP', 'GRP_DRIVER_CABEZA', mo=1, sr=["x","z","y"], name = 'PARENT_CONSTRAIN_CABEZA_TRANSLATE')

cmds.parentConstraint( 'DRIVER_COLUMNA_TOP', 'GRP_DRIVER_CABEZA', mo=1, st=["x","z","y"], name = 'PARENT_CONSTRAIN_CABEZA_ROTATE')

cmds.parentConstraint( 'MOVE_ALL', 'GRP_DRIVER_CABEZA', mo=1, st=["x","z","y"])

cmds.select('DRIVER_CABEZA')

cmds.addAttr(longName='SWITCH_CABEZA_FOLLOW', defaultValue=0, minValue=0, maxValue=1, k=True)

cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', 0)

cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', 1)

cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

cmds.setAttr( 'DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW' , 1 )
cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', 1)
cmds.setAttr( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', 0)

cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.DRIVER_COLUMNA_TOPW0', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

cmds.setDrivenKeyframe( 'PARENT_CONSTRAIN_CABEZA_ROTATE.MOVE_ALLW1', cd='DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW')

cmds.setAttr( 'DRIVER_CABEZA.SWITCH_CABEZA_FOLLOW' , 0 )

#CORRECION SWITCH CABEZA (TERMINA)

