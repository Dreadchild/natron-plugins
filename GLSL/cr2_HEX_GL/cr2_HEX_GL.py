# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named cr2_HEX_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from cr2_HEX_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.cr2_HEX_GL"

def getLabel():
    return "cr2_HEX_GL"

def getVersion():
    return 1.0

def getIconPath():
    return "cr2_HEX_GL.png"

def getGrouping():
    return "Community/GLSL/Source"

def getPluginDescription():
    return "Creates a Hexagon Pattern."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("ASPECT", "Aspect")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.ASPECT = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Line thickness : ")
    param.setMinimum(0.02, 0)
    param.setMaximum(0.7999999999999999, 0)
    param.setDisplayMinimum(0.02, 0)
    param.setDisplayMaximum(0.7999999999999999, 0)
    param.setDefaultValue(0.15, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat4", "Shape width : ")
    param.setMinimum(0, 0)
    param.setMaximum(10.8, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10.8, 0)
    param.setDefaultValue(1.1547, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat4 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat5", "Shape height : ")
    param.setMinimum(0, 0)
    param.setMaximum(10.8, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(10.8, 0)
    param.setDefaultValue(1.49999, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat5 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("TRANSFORM", "Transform")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.TRANSFORM = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat2", "position X : ")
    param.setMinimum(-10000, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(-10000, 0)
    param.setDisplayMaximum(10000, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat2 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat3", "position Y : ")
    param.setMinimum(-10000, 0)
    param.setMaximum(10000, 0)
    param.setDisplayMinimum(-10000, 0)
    param.setDisplayMaximum(10000, 0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat3 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat0", "Scale : ")
    param.setMinimum(5, 0)
    param.setMaximum(499.9999999999999, 0)
    param.setDisplayMinimum(5, 0)
    param.setDisplayMaximum(499.9999999999999, 0)
    param.setDefaultValue(20, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat0 = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createSeparatorParam("COLOURS", "Colours")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.COLOURS = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createColorParam("Shadertoy1_2paramValueVec36", "Line color : ", False)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setDefaultValue(1, 1)
    param.restoreDefaultValue(1)
    param.setDefaultValue(1, 2)
    param.restoreDefaultValue(2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec36 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createColorParam("Shadertoy1_2paramValueVec37", "Back color : ", False)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueVec37 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    param = lastNode.createStringParam("sep19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep19 = param
    del param

    param = lastNode.createSeparatorParam("OPTIONS", "Options")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTIONS = param
    del param

    param = lastNode.createStringParam("sep20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep20 = param
    del param

    param = lastNode.createStringParam("sep21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep21 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool8", "Hard edge : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool8 = param
    del param

    param = lastNode.createStringParam("sep22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep22 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool9", "Invert matte : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool9 = param
    del param

    param = lastNode.createStringParam("sep23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep23 = param
    del param

    param = lastNode.createStringParam("sep24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep24 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "cr2_HEX_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3870)
    lastNode.setSize(80, 44)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueFloat0")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(0.15, 0)
        del param

    param = lastNode.getParam("paramValueFloat2")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat3")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramValueFloat4")
    if param is not None:
        param.setValue(1.1547, 0)
        del param

    param = lastNode.getParam("paramValueFloat5")
    if param is not None:
        param.setValue(1.49999, 0)
        del param

    param = lastNode.getParam("paramValueVec36")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    param = lastNode.getParam("paramValueVec37")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueBool8")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramValueBool9")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/run/media/ffernandez/FABRICE/PERSO/NATRON/GIT_DEV/natron-plugins/Shadertoy/cr2_HEX.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("/*\n\tHexagon Pattern Creator\n\tWritten by: Craig Russo\n\tEmail: craig@310studios.com\n\tWebsite: www.crusso.com\n\t\n\tDate Created: 5/10/2014\n\tversion: .02\n\n\tBased on : https://gist.github.com/rgngl/5565102\n\n\tCopyright (C) 2014 Craig P. Russo\n\n\tThis program is free software; you can redistribute it and/or\n\tmodify it under the terms of the GNU General Public License\n\tas published by the Free Software Foundation; either version 2\n\tof the License, or (at your option) any later version.\n\n\tThis program is distributed in the hope that it will be useful,\n\tbut WITHOUT ANY WARRANTY; without even the implied warranty of\n\tMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n\tGNU General Public License for more details.\n\n\tYou should have received a copy of the GNU General Public License\n\talong with this program; if not, write to the Free Software\n\tFoundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.\n\n\t\n*/\n\n\n\n\nuniform float scale = 20; // Scale : (scale), min=5, max=500\nuniform float lineThick = 0.15; // Line thickness : (line thickness), min=0.02, max=0.8\nuniform float posx = 0.0; // X : (x position), min=-10000, max=10000\nuniform float posy = 0.0; // Y : (y position), min=-10000, max=10000\nuniform float rotate = 0.0; // Rotate : (rotate), min=-10000, max=10000\nuniform float shapew = 1.1547; // Shape width : (shape width), min=0.0, max=10.80\nuniform float shapeh = 1.49999; // Shape height : (shape height), min=0.0, max=10.80\n\nuniform vec3 linecolor = vec3(1,1,1);\nuniform vec3 backcolor = vec3(0,0,0);\n\nuniform bool hardedge = false;\nuniform bool invertmatte = false;\n\n// 1 on edges, 0 in middle\nfloat hex(vec2 p) {\n  //p.x *= 0.57735*2.0;\n  p.x *= shapew;\n  p.x -= posx;\n\tp.y += (mod(floor(p.x), 2.0)*0.5);\n\tp.y -= posy;\n\n\t//p = abs((mod(p, 1.0) - 0.5));\n\tp = abs((mod(p, 1.0) - 0.5));\n\t//return abs(max(p.x*1.5 + p.y, p.y*2.0) - 1.0);\n\treturn abs(max(p.x*shapeh + p.y, p.y*2.0) - 1.0);\n}\n\n\n// Rotation Matix This doesn\'t work yet  I got this from here: http://www.neilmendoza.com/glsl-rotation-about-an-arbitrary-axis/\n//-----------------------------------------------------------\n\n\n\nmat4 rotationMatrix(vec3 axis, float angle)\n{\n    axis = normalize(axis);\n    float s = sin(angle);\n    float c = cos(angle);\n    float oc = 1.0 - c;\n    \n    return mat4(oc * axis.x * axis.x + c,           oc * axis.x * axis.y - axis.z * s,  oc * axis.z * axis.x + axis.y * s,  0.0,\n                oc * axis.x * axis.y + axis.z * s,  oc * axis.y * axis.y + c,           oc * axis.y * axis.z - axis.x * s,  0.0,\n                oc * axis.z * axis.x - axis.y * s,  oc * axis.y * axis.z + axis.x * s,  oc * axis.z * axis.z + c,           0.0,\n                0.0,                                0.0,                                0.0,                                1.0);\n}\n\n// -------------------------------------------------------------------\n\n\n\n\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n\n//normalize canvas coordinates\nvec2 st;\nst.x = fragCoord.x / iResolution.x;\nst.y = fragCoord.y / iResolution.y;\n\n//gl_TexCoord[ 0 ] = gl_MultiTexCoord0*rotationMatrix(st/2,rotate);\n\nvec2 pos = fragCoord.xy;\n\nvec2 p = pos/scale; \nvec4 color = vec4(smoothstep(0.0, lineThick, hex(p)));\n\t\t\n\t\n\n\tfragColor = color;\n\n\t\n\t//This inverts the colors\n\tfragColor.rgb = vec3(1.0, 1.0, 1.0) - fragColor.rgb;\n\n\t//Invert Alpha\n\tif(invertmatte == false){\n\tfragColor.a = 1.0 - fragColor.a;\n\t}\n\n\t\n\tif(hardedge){\n\n\t\t//This Colors Lines\n\t\tfragColor.rgb = fragColor.rgb * linecolor;\n\n\t\t//This Colors Fills\n\t\tif(fragColor.rgb == vec3(0)){\n\t\t\tfragColor.rgb = vec3(backcolor);\n\t\t}else{\n\t\t\tfragColor.rgb = vec3(linecolor);\n\t\t}\n\t\n\t}else{\n\n\t\t//This Colors Lines\n\t\tfragColor.rgb = fragColor.rgb * linecolor;\n\t\t//This Colors fills\n\t\tfragColor.rgb = fragColor.rgb + backcolor;\n\n\n\t}\n\n\t\n\t\n}\n\n\n\n \n\n")
        del param

    param = lastNode.getParam("inputEnable0")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Scale :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("scale")
        del param

    param = lastNode.getParam("paramDefaultFloat0")
    if param is not None:
        param.setValue(20, 0)
        del param

    param = lastNode.getParam("paramMinFloat0")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramMaxFloat0")
    if param is not None:
        param.setValue(499.9999999999999, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("lineThick")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Line thickness :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("line thickness")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(0.15, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0.02, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(0.7999999999999999, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("posx")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("X :")
        del param

    param = lastNode.getParam("paramHint2")
    if param is not None:
        param.setValue("x position")
        del param

    param = lastNode.getParam("paramMinFloat2")
    if param is not None:
        param.setValue(-10000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat2")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("posy")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Y :")
        del param

    param = lastNode.getParam("paramHint3")
    if param is not None:
        param.setValue("y position")
        del param

    param = lastNode.getParam("paramMinFloat3")
    if param is not None:
        param.setValue(-10000, 0)
        del param

    param = lastNode.getParam("paramMaxFloat3")
    if param is not None:
        param.setValue(10000, 0)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("shapew")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Shape width :")
        del param

    param = lastNode.getParam("paramHint4")
    if param is not None:
        param.setValue("shape width")
        del param

    param = lastNode.getParam("paramDefaultFloat4")
    if param is not None:
        param.setValue(1.1547, 0)
        del param

    param = lastNode.getParam("paramMinFloat4")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat4")
    if param is not None:
        param.setValue(10.8, 0)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("shapeh")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Shape height :")
        del param

    param = lastNode.getParam("paramHint5")
    if param is not None:
        param.setValue("shape height")
        del param

    param = lastNode.getParam("paramDefaultFloat5")
    if param is not None:
        param.setValue(1.49999, 0)
        del param

    param = lastNode.getParam("paramMinFloat5")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat5")
    if param is not None:
        param.setValue(10.8, 0)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("linecolor")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("linecolor")
        del param

    param = lastNode.getParam("paramDefaultVec36")
    if param is not None:
        param.setValue(1, 0)
        param.setValue(1, 1)
        param.setValue(1, 2)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("backcolor")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("backcolor")
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("hardedge")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("hardedge")
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("invertmatte")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("invertmatte")
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)

    param = groupShadertoy1_2.getParam("paramValueFloat0")
    group.getParam("Shadertoy1_2paramValueFloat0").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat2")
    group.getParam("Shadertoy1_2paramValueFloat2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat3")
    group.getParam("Shadertoy1_2paramValueFloat3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat4")
    group.getParam("Shadertoy1_2paramValueFloat4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat5")
    group.getParam("Shadertoy1_2paramValueFloat5").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec36")
    group.getParam("Shadertoy1_2paramValueVec36").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueVec37")
    group.getParam("Shadertoy1_2paramValueVec37").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool8")
    group.getParam("Shadertoy1_2paramValueBool8").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool9")
    group.getParam("Shadertoy1_2paramValueBool9").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["cr2_HEX_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
