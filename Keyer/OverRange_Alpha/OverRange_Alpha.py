# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named ttExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from ttExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.OverRange_Alpha"

def getLabel():
    return "OverRange_Alpha"

def getVersion():
    return 1

def getIconPath():
    return "OverRange_Alpha.png"

def getGrouping():
    return "Community/Keyer"

def getPluginDescription():
    return "Generates an alpha channel based on overranged values."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "OverRange_Alpha")
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

    param = lastNode.createChoiceParam("SwitchDB", "")
    entries = [ ("Over bright", ""),
    ("Over dark", "")]
    param.setOptions(entries)
    del entries

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.SwitchDB = param
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

    param = lastNode.createColorParam("FillColor", "fill color : ", False)
    param.setMinimum(-2147483648, 0)
    param.setMaximum(2147483647, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)
    param.setMinimum(-2147483648, 1)
    param.setMaximum(2147483647, 1)
    param.setDisplayMinimum(0, 1)
    param.setDisplayMaximum(1, 1)
    param.setMinimum(-2147483648, 2)
    param.setMaximum(2147483647, 2)
    param.setDisplayMinimum(0, 2)
    param.setDisplayMaximum(1, 2)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.FillColor = param
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

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

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
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createSeparatorParam("Name", "OverRange_Alpha")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.Name = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

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
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("line03", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createSeparatorParam("FF", "(Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FF = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(1400, 905)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "getOverBright"
    lastNode = app.createNode("fr.inria.openfx.SeExprSimple", 2, group)
    lastNode.setScriptName("getOverBright")
    lastNode.setLabel("getOverBright")
    lastNode.setPosition(1140, 329)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupgetOverBright = lastNode

    param = lastNode.getParam("rExpr")
    if param is not None:
        param.setValue("1.0")
        del param

    param = lastNode.getParam("gExpr")
    if param is not None:
        param.setValue("0.0")
        del param

    param = lastNode.getParam("bExpr")
    if param is not None:
        param.setValue("0.0")
        del param

    param = lastNode.getParam("aExpr")
    if param is not None:
        param.setValue("clamp( ( r*(r>1) )-1, 0 ,1)")
        del param

    del lastNode
    # End of node "getOverBright"

    # Start of node "getOverDark"
    lastNode = app.createNode("fr.inria.openfx.SeExprSimple", 2, group)
    lastNode.setScriptName("getOverDark")
    lastNode.setLabel("getOverDark")
    lastNode.setPosition(1653, 325)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupgetOverDark = lastNode

    param = lastNode.getParam("rExpr")
    if param is not None:
        param.setValue("1.0")
        del param

    param = lastNode.getParam("gExpr")
    if param is not None:
        param.setValue("0.0")
        del param

    param = lastNode.getParam("bExpr")
    if param is not None:
        param.setValue("0.0")
        del param

    param = lastNode.getParam("aExpr")
    if param is not None:
        param.setValue("clamp( ( r*(r<0) )+1, 0 ,1)")
        del param

    del lastNode
    # End of node "getOverDark"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(1173, 186)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(1435, 186)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(1686, 187)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Switch"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch")
    lastNode.setLabel("Switch")
    lastNode.setPosition(1400, 574)
    lastNode.setSize(80, 48)
    lastNode.setColor(1, 1, 1)
    groupSwitch = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch"

    # Start of node "Input1"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Input1")
    lastNode.setLabel("Input1")
    lastNode.setPosition(1402, -210)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupInput1 = lastNode

    del lastNode
    # End of node "Input1"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(1140, 574)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.2941, 0.3686, 0.7765)
    groupPremult1 = lastNode

    del lastNode
    # End of node "Premult1"

    # Start of node "Premult2"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult2")
    lastNode.setLabel("Premult2")
    lastNode.setPosition(1653, 574)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.2941, 0.3686, 0.7765)
    groupPremult2 = lastNode

    del lastNode
    # End of node "Premult2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput1.connectInput(0, groupSwitch)
    groupgetOverBright.connectInput(0, groupDot1)
    groupgetOverDark.connectInput(0, groupDot3)
    groupDot1.connectInput(0, groupDot2)
    groupDot2.connectInput(0, groupInput1)
    groupDot3.connectInput(0, groupDot2)
    groupSwitch.connectInput(0, groupPremult1)
    groupSwitch.connectInput(1, groupPremult2)
    groupPremult1.connectInput(0, groupgetOverBright)
    groupPremult2.connectInput(0, groupgetOverDark)

    param = groupgetOverBright.getParam("rExpr")
    param.setExpression("myRed = thisGroup.FillColor.get()[0]\nret = str(myRed)", True, 0)
    del param
    param = groupgetOverBright.getParam("gExpr")
    param.setExpression("myGreend = thisGroup.FillColor.get()[1]\nret = str(myGreen)", True, 0)
    del param
    param = groupgetOverBright.getParam("bExpr")
    param.setExpression("myBlue = thisGroup.FillColor.get()[2]\nret = str(myBlue)", True, 0)
    del param
    param = groupgetOverDark.getParam("rExpr")
    param.setExpression("myRed = thisGroup.FillColor.get()[0]\nret = str(myRed)", True, 0)
    del param
    param = groupgetOverDark.getParam("gExpr")
    param.setExpression("myGreend = thisGroup.FillColor.get()[1]\nret = str(myGreen)", True, 0)
    del param
    param = groupgetOverDark.getParam("bExpr")
    param.setExpression("myBlue = thisGroup.FillColor.get()[2]\nret = str(myBlue)", True, 0)
    del param
    param = groupSwitch.getParam("which")
    param.setExpression("ret = thisGroup.SwitchDB.get()", False, 0)
    del param

    try:
        extModule = sys.modules["ttExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
