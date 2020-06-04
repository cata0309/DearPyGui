import sandbox
import SandboxTheme

# create some menus
sandbox.addMenuBar("MenuBar")
sandbox.addMenu("MenuBar", "File")
sandbox.addMenu("File", "Callbacks")
sandbox.addMenuItem("Callbacks", "callback 1")
sandbox.addSeperator("Callbacks")
sandbox.addMenuItem("Callbacks", "callback 2")
sandbox.addMenuItem("Callbacks", "callback 3")
sandbox.endMenu("Callbacks")
sandbox.endMenu("File")
sandbox.addMenu("MenuBar", "Edit")
sandbox.endMenu("Edit")
sandbox.endMenuBar("MenuBar")

# various widgets
sandbox.addSpacing("", 10)
sandbox.addButton("", "Press me")
sandbox.addCombo("", "combo1", ("A", "B", "C"))
sandbox.addInputText("", "Testing", hint="a hint")
sandbox.addGroup("", "Group1")
sandbox.addRadioButton("Group1", "radiobutton1", ("First Option", "Second Option", "Third Option"))
sandbox.endGroup("Group1")
sandbox.addSameLine("")
sandbox.addChild("", "Child1", 300, 200)
sandbox.addRadioButton("Child1", "radiobutton2", ("First Option", "Second Option", "Third Option"))
sandbox.endChild("Child1")
sandbox.addSpacing("", 10)

sandbox.addCollapsingHeader("", "Themes")
sandbox.addButton("Themes", "Use Dark")
sandbox.addButton("Themes", "Use Light")
sandbox.addButton("Themes", "Use Classic")

# creating tabs
sandbox.addTabBar("", "TabBar1")

sandbox.addTab("TabBar1", "Tab1")
sandbox.addInputText("Tab1", "Testing1")
sandbox.addSameLine("Tab1", 0, 20)
sandbox.addInputText("Tab1", "Testing2")
sandbox.addColorEdit4("Tab1", "Color1", 1.0, 0, 0, 1.0)
sandbox.addInputInt("Tab1", "inputint1")
sandbox.addInputFloat("Tab1", "inputfloat1", default_value=117.0)
sandbox.addCheckbox("Tab1", "Logger", default_value=True)
sandbox.addCheckbox("Tab1", "checkbox2")
sandbox.addListbox("Tab1", "listbox1", ("First item", "Second item", "Third item"))
sandbox.addText("Tab1", "Some awesome regular text")
sandbox.addText("Tab1", "Some awesome red text", color=(1.0, 0, 0, 1.0), wrap=100)
sandbox.addLabelText("Tab1", "Output", "color value", color=(0.0, 1.0, 0, 1.0))
sandbox.endTab("Tab1")

sandbox.addTab("TabBar1", "Tab2")
sandbox.addInputText("Tab2", "Testing3")
sandbox.addSpacing("Tab2", count=10)
sandbox.addInputText("Tab2", "Testing4")

sandbox.addTooltip("Testing4", "Tooltip1")         # start tooltip
sandbox.addButton("Tooltip1", "A Fancy tooltip 1")
sandbox.addButton("Tooltip1", "A Fancy tooltip 2")
sandbox.endTooltip("Tooltip1")                     # end tooltip

sandbox.endTab("Tab2")

sandbox.endTabBar("TabBar1")

# setting call backs
sandbox.setItemCallback("Press me", "ItemCallback")
sandbox.setItemCallback("Testing", "ItemCallback")
sandbox.setItemCallback("Tab1", "ItemCallback")
sandbox.setItemCallback("callback 1", "ItemCallback")
sandbox.setItemCallback("callback 2", "ItemCallback")
sandbox.setItemCallback("callback 3", "ItemCallback")
sandbox.setItemCallback("Use Dark", "DarkTheme")
sandbox.setItemCallback("Use Light", "LightTheme")
sandbox.setItemCallback("Use Classic", "ClassicTheme")
sandbox.setItemCallback("Logger", "LoggerCallback")
sandbox.setItemCallback("listbox1", "ItemCallback")
sandbox.setItemCallback("combo1", "ItemCallback")

# setting a tip
sandbox.setItemTip("Button1", "A different tip")

# setting item widths
sandbox.setItemWidth("Testing1", 200)
sandbox.setItemWidth("Testing2", 200)

# setting main callback
#sandbox.setMainCallback("MainCallback")

def ItemCallback(sender):
    print("Called by ", sender)
    print("value is: ", sandbox.getValue(sender))
    value = sandbox.getValue("Color1")
    loglevel = sandbox.getValue("inputint1")
    sandbox.SetLogLevel(loglevel)
    sandbox.changeThemeItem("ImGuiCol_Tab", value[0], value[1], value[2], value[3])
    sandbox.updateTheme()
    sandbox.Log("log")
    sandbox.LogDebug("log")
    sandbox.LogInfo("log")
    sandbox.LogWarning("log")
    sandbox.LogError("log")

def LoggerCallback(sender):

    value = sandbox.getValue("Logger")
    if value == 0:
        sandbox.TurnOffLogger()
    else:
        sandbox.TurnOnLogger()

def DarkTheme(sender):
    sandbox.setTheme("dark")
def LightTheme(sender):
    sandbox.setTheme("light")
def ClassicTheme(sender):
    sandbox.setTheme("classic")

def MainCallback(sender):
    print(sender);
