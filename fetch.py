try:
    import requests
except ImportError:
    print("please install the requests module.")
    exit()
from calendar import c
import json, sys
from re import M
from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

#from pprint import pprint

url = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/API-Dump.json"
version_url = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/version.txt"
version_guidurl = "https://raw.githubusercontent.com/MaximumADHD/Roblox-Client-Tracker/roblox/version-guid.txt"
r = requests.get(url)
version = requests.get(version_url)
version_guid = requests.get(version_guidurl)
data = r.json()

Version = str(data["Version"]) + " - " + version.text + " (" + version_guid.text + ")" + " | " + "Generated: " + formatted_now + ", using generator v1.1"
Classes = data["Classes"]
Enums = data["Enums"]

ManualMembers = {
    "RemoteFunction": [
        {
            "MemberType": "Property",
            "Name": "OnClientInvoke",
            "ValueType": {
                "Category": "Class",
                "Name": "Function"
            }
        },
        {
            "MemberType": "Property",
            "Name": "OnServerInvoke",
            "ValueType": {
                "Category": "Class",
                "Name": "Function"
            }
        }
    ],
}

API = {
    "Instance": {
        "Members": [
            {
                "MemberType": "Function",
                "Name": "new",
                "ReturnType": {
                    "Category": "Class",
                    "Name": "Instance"
                },
                "Parameters": [
                    {
                        "Name": "className",
                        "Type": {
                            "Category": "Enum",
                            "Name": "EnumItem"
                        }
                    },""" - Roll out with an optional update
                    {
                        "Name": "parent",
                        "Optional": True,
                        "Type": {
                            "Category": "Class",
                            "Name": "Instance"
                        }
                    }"""
                ]
            },
        ]
    },
}

def render(creator):
    file = creator.FileStart.format(Version=Version) + creator.PreDefined
    
    ### ENUMS ###
    file += creator.Section.format(Name="Enums")
    file += creator.EnumSection
    for i in Enums:
        Name = i["Name"]
        Data = i["Items"]
        
        file += creator.EnumCore.format(Name=Name)
        for item in Data:
            line = creator.EnumItem.format(Name=item["Name"], Value=item["Value"])
            if creator.EnumVerify(item["Name"], item["Value"]) != None:
                line = creator.EnumVerify(item["Name"], item["Value"])
            file += line
        file += creator.EnumCoreEnd.format(Name=Name)
        
    file += creator.EnumEnd.format(Name="Enums")
    
    ### CLASSES ###
    file += creator.Section.format(Name="Classes")
    file += creator.ClassSection
    classCache = []
    empties = []
    
    def getClassMembers(className):
        for i in Classes:
            if i["Name"] == className:
                members = i["Members"]
                if className in ManualMembers:
                    members += ManualMembers[className]
                return members
        print("members for class " + className + " not found")
        exit(1)
        
    for class_ in Classes:
        members = getClassMembers(class_["Name"])
        name = class_["Name"]
        if class_["Superclass"] == "<<<ROOT>>>": # Root class, held in Instance
            class_["Superclass"] = ""
        if members == []:
            file += creator.Skip.format(Name=name)
            empties.append(name)
        else:
            if class_["Superclass"] in empties:
                class_["Superclass"] = ""
            if class_["Superclass"] != "":
                file += creator.ClassSuperCore.format(Name=name, SuperClass=class_["Superclass"])
            else:
                file += creator.ClassCore.format(Name=name)
            for member in members:
                if member["MemberType"] == "Property":
                    file += creator.ClassProperty.format(Name=creator.fixKeyword(member["Name"]), Type=creator.typeCompiler(member["ValueType"]["Name"], classCache))
                elif member["MemberType"] == "Function":
                    args = "self"
                    for i, arg in enumerate(member["Parameters"]):
                        if i != len(member["Parameters"]):
                            args += ", "
                        args += creator.ArgFormat.format(Name=creator.fixKeyword(arg["Name"]), Type=creator.typeCompiler(arg["Type"]["Name"], classCache))
                    if type(member["ReturnType"]) == list:
                        file += creator.ClassFunction.format(Name=member["Name"], Args=args, ReturnType=creator.typeCompiler(member["ReturnType"][0]["Name"], classCache)) # TODO: Support multiple return values
                    else:
                        file += creator.ClassFunction.format(Name=member["Name"], Args=args, ReturnType=creator.typeCompiler(member["ReturnType"]["Name"], classCache))
                elif member["MemberType"] == "Event":
                    file += creator.ClassEvent.format(Name=member["Name"])
                        
            classCache.append(name)
            file += creator.ClassCoreEnd.format(Name=name)
            
    file += creator.ClassEnd.format(Name="Classes")
    
    ### SERVICES ###
    services = ["Players", "ReplicatedStorage", "StarterGui", "StarterPack", "StarterPlayer", "Lighting", "Workspace", "SoundService", "CoreGui", "CorePackages", "Chat", "LocalizationService", "TestService", "GuiService", "HttpService", "ContentProvider", "InsertService", "CollectionService", "PhysicsService", "RunService", "UserInputService", "ContextActionService", "Debris", "TweenService", "PathfindingService", "ServerScriptService", "ServerStorage", "Teams", "UserGameSettings", "SoundGroups", "LogService", "BadgeService", "AssetService", "MarketplaceService", "PointsService", "TeleportService", "DataStoreService", "GamePassService", "GroupService", "ImaginationService", "NotificationService", "PolicyService", "PublishService", "SocialService", "TextService", "AvatarEditorService", "ChatService", "CollectionService", "VoiceChatService", "VoiceChatManager", "VoiceChatInternalService", "VoiceChatInternalManager", "VoiceChatInternalClient"]
    file += creator.Section.format(Name="Services")
    file += creator.ServiceSection
    for service in services:
        file += creator.Service.format(Name=service)
    file += creator.ServiceEnd.format(Name="Services")
    
    ### END ###
    file += creator.End
    return file

def isStatic(class_, member):
    """ Return whether or not if the member is static. Static is a `.` instead of a `:`. """
    pass
### EXAMPLES ###
class Python: # Python Example
    Section = """\n#### {Name} ####\n"""
    FileStart = """# Auto-Generated by RCC Bindings Engine\n# Dump Version: {Version}\n\nfrom typing import *\n\n"""
    Skip = """{Name} = {{}}\n"""
    
    ### PREDEF ###
    PreDefined = """### HANDWRITTEN ###
class RBXScriptSignal():
    def Disconnect(self):
        pass
    def Connect(self, fn: Callable):
        pass
    def Wait(self):
        pass
        
class NoneRobloxType:
    def __init__(self):
        return None
"""
    End = """### HANDWRITTEN ###
game = DataModel()
### END ###"""
    ### ENUMS ###
    EnumSection = """Enum = {\n"""
    EnumCore = """\t"{Name}": {{\n"""
    EnumItem = """\t\t"{Name}": {Value},\n"""
    EnumCoreEnd = """\t}},\n"""
    EnumEnd = """}}"""
    
    def EnumVerify(self, Name, Value):
        """ Verifies that the Enum is valid, if not fix and return the fixed Enum. """
        pass
    
    ### CLASSES ###
    ClassSection = """"""
    ClassCore = """class {Name}:\n"""
    ClassSuperCore = """class {Name}({SuperClass}):\n"""
    ClassProperty = """\t{Name}: {Type}\n"""
    ClassFunction = """\tdef {Name}({Args}) -> {ReturnType}:\n\t\treturn {ReturnType}()\n"""
    ArgFormat = """{Name}: {Type}"""
    ClassEvent = """\tdef {Name}(self, fn: Callable) -> RBXScriptSignal:\n\t\treturn RBXScriptSignal()\n"""
    ClassCoreEnd = """\n"""
    ClassEnd = """"""
    
    ### SERVICES ###
    ServiceSection = """services: Dict[str, Any] = {\n"""
    Service = """\t"{Name}": {{}},\n"""
    ServiceEnd = """}}"""
    
    ### TYPES ###
    def fixKeyword(self, Keyword): # TODO: Maybe use a dict instead of this?
        if Keyword in ["class", "def", "return", "from", "import", "pass", "if", "else", "elif", "for", "while", "in", "not", "and", "or", "is", "as", "with", "del", "assert", "raise", "try", "except", "finally", "continue", "break", "global", "nonlocal", "lambda", "yield", "True", "False", "None"]:
            Keyword += "_"
        Keyword = Keyword.replace(" ", "_").replace("/", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace(":", "_").replace(";", "_").replace(",", "_").replace("'", "_").replace('"', "_").replace("=", "_").replace("+", "_").replace("*", "_").replace("&", "_").replace("^", "_").replace("%", "_").replace("$", "_").replace("#", "_").replace("@", "_")
        return Keyword
    def typeCompiler(self, Type, cache):
        """ Compiles the C type into the target langauges type. """
        if Type == "null":
            Type = "NoneRobloxType"
        elif Type == "string":
            Type = "str"
        elif Type == "integer":
            Type = "int"
        elif Type == "int64":
            Type = "int"
        elif Type == "double":
            Type = "float"
        elif Type == "bool":
            Type = "bool"
        elif Type == "number":
            Type = "float"
        elif Type == "Array":
            Type = "list"
        elif Type == "Tuple":
            Type = "tuple"
        elif Type not in cache:
            Type = "Any"
            
        return Type
class Teal: # Teal Example
    Section = """\n--> {Name}\n"""
    FileStart = """-- Auto-Generated by RCC Bindings Engine\n-- Dump Version: {Version}\n\n"""
    Skip = """{Name} = {{}}\n"""
    
    ### PREDEF ###
    PreDefined = """--> HANDWRITTEN <--
local RBXScriptSignal = {
    Disconnect = function(self)
        
    end
    Connect = function(self, fn: Function)
        
    end
    Wait = function(self)
        
    end
}
local super = function(super, class)
    local new = super
    for i, v in pairs(class) do
        new[i] = v
    end
end
"""
    End = """--> HANDWRITTEN <--
global game = DataModel
--> END <--"""
    ### ENUMS ###
    EnumSection = """global Enum = {\n"""
    EnumCore = """\t["{Name}"] = {{\n"""
    EnumItem = """\t\t[\"{Name}\"] = {Value},\n"""
    EnumCoreEnd = """\t}},\n"""
    EnumEnd = """}}"""
    
    def EnumVerify(self, Name, Value):
        """ Verifies that the Enum is valid, if not fix and return the fixed Enum. """
        pass
    
    ### CLASSES ###
    ClassSection = """"""
    ClassCore = """global {Name} = ({{\n"""
    ClassSuperCore = """global {Name} = super({SuperClass}, {{\n"""
    ClassProperty = """\t[\"{Name}\"]: {Type} = nil,\n"""
    ClassFunction = """\t{Name} = function({Args}): {ReturnType}\n\tend\n"""
    ArgFormat = """{Name}: {Type}"""
    ClassEvent = """\tfunction {Name}(self, fn: Callable): RBXScriptSignal\n\tend\n"""
    ClassCoreEnd = """\n}})\n"""
    ClassEnd = """"""
    
    ### SERVICES ###
    ServiceSection = """services = {\n"""
    Service = """\t["{Name}"] = {{}},\n"""
    ServiceEnd = """}}"""
    
    ### TYPES ###
    def fixKeyword(self, Keyword): # TODO: Maybe use a dict instead of this?
        Keyword = Keyword.replace(" ", "_").replace("/", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace(":", "_").replace(";", "_").replace(",", "_").replace("'", "_").replace('"', "_").replace("=", "_").replace("+", "_").replace("*", "_").replace("&", "_").replace("^", "_").replace("%", "_").replace("$", "_").replace("#", "_").replace("@", "_")
        return Keyword
    def typeCompiler(self, Type, cache):
        """ Compiles the C type into the target langauges type. """
        if Type == "null":
            Type = "null"
        elif Type == "string":
            Type = "string"
        elif Type == "integer":
            Type = "number"
        elif Type == "int64":
            Type = "number"
        elif Type == "double":
            Type = "number"
        elif Type == "bool":
            Type = "bool"
        elif Type == "number":
            Type = "number"
        elif Type == "Array":
            Type = "table"
        elif Type == "Tuple":
            Type = "..."
        elif Type not in cache:
            Type = "any"
            
        return Type
    
class Rust:
    Section = """\n// {Name}\n"""
    FileStart = """// Auto-Generated by RCC Bindings Engine\n// Dump Version: {Version}\n\n"""
    Skip = """// {Name} is skipped\n"""
    
    ### PREDEF ###
    PreDefined = """// HANDWRITTEN
pub struct RBXScriptSignal;
impl RBXScriptSignal {
    pub fn disconnect(&self) {}
    pub fn connect(&self, fn: impl Fn()) {}
    pub fn wait(&self) {}
}

pub struct NoneRobloxType;
impl NoneRobloxType {
    pub fn new() -> Self { NoneRobloxType }
}

pub struct DataModel;
pub static GAME: DataModel = DataModel;

pub struct Instance;
impl Instance {
    pub fn new() -> Self { Instance }
}
"""
    End = """// HANDWRITTEN
pub static GAME: DataModel = DataModel;
// END"""
    
    ### ENUMS ###
    EnumSection = """pub mod enums {{\n"""
    EnumCore = """    pub enum {Name} {{\n"""
    EnumItem = """        {Name} = {Value},\n"""
    EnumCoreEnd = """    }}\n"""
    EnumEnd = """}}\n"""
    
    def EnumVerify(self, Name, Value):
        pass
    
    ### CLASSES ###
    ClassSection = """"""
    ClassCore = """pub struct {Name} {{\n"""
    ClassSuperCore = """pub struct {Name} {{\n    super_class: {SuperClass},\n"""
    ClassProperty = """    pub {Name}: {Type},\n"""
    ClassFunction = """    pub fn {Name}(&self, {Args}) -> {ReturnType} {{\n        {ReturnType}::new()\n    }}\n"""
    ArgFormat = """{Name}: {Type}"""
    ClassEvent = """    pub fn {Name}(&self, fn: impl Fn()) -> RBXScriptSignal {{\n        RBXScriptSignal::new()\n    }}\n"""
    ClassCoreEnd = """}}\n"""
    ClassEnd = """"""
    
    ### SERVICES ###
    ServiceSection = """pub mod services {{\n"""
    Service = """    pub struct {Name};\n"""
    ServiceEnd = """}}\n"""
    
    ### TYPES ###
    def fixKeyword(self, Keyword):
        Keyword = Keyword.replace(" ", "_").replace("/", "_").replace("-", "_").replace(".", "_").replace("(", "_").replace(")", "_").replace(":", "_").replace(";", "_").replace(",", "_").replace("'", "_").replace('"', "_").replace("=", "_").replace("+", "_").replace("*", "_").replace("&", "_").replace("^", "_").replace("%", "_").replace("$", "_").replace("#", "_").replace("@", "_")
        return Keyword
    
    def typeCompiler(self, Type, cache):
        if Type == "null":
            Type = "NoneRobloxType"
        elif Type == "string":
            Type = "String"
        elif Type == "integer":
            Type = "i32"
        elif Type == "int64":
            Type = "i64"
        elif Type == "double":
            Type = "f64"
        elif Type == "number":
            Type = "f64"
        elif Type == "Array":
            Type = "Vec<_>"
        elif Type == "Tuple":
            Type = "(Box<dyn Any>)"
        elif Type not in cache:
            Type = "Option<_>"
        return Type
    
Creator = Python # Default

### MAIN ###
def main():
    chosen = sys.argv[1]
    if chosen == "python":
        file = render(Python())
    elif chosen == "teal":
        file = render(Teal())
    elif chosen == "rust":
        file = render(Rust())
    else:
        print("invalid language")
        exit()
    print(file)
        
if __name__ == "__main__":
    main()
