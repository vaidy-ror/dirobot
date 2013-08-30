import shutil
import os
pip_list_filename="pip_list.txt"

def make_index_file(filename,keywords):
    f=open("robot-indices/%s"   %   filename,'w')
    for keyword in keywords:
        f.write("%s\n"  %   keyword)
    f.close()

try:
    shutil.rmtree('robot-indices')
    print 'old robot-indices dir removed'
except:
    print 'robot-indices dir not found.  nothing to cleanup.'

print "creating robot-indices directory"
os.mkdir("robot-indices")

modules = [
           "Selenium2Library",
           "Rammbock",
           "AndroidLibrary",
           "HttpLibrary",
           "RequestsLibrary",           
           ]

for module in modules:
    os.system("python -m robot.libdoc %s list > robot-indices/%s.index"     %   (module,module))
    

builtin="Call Method|Catenate|Comment|Continue For Loop|Continue For Loop If|Convert To Binary|Convert To Boolean|Convert To Hex|Convert To Integer|Convert To Number|Convert To Octal|Convert To String|Create List|Evaluate|Exit For Loop|Exit For Loop If|Fail|Fatal Error|Get Count|Get Length|Get Library Instance|Get Time|Get Variable Value|Get Variables|Import Library|Import Resource|Import Variables|Keyword Should Exist|Length Should Be|Log|Log Many|Log Variables|No Operation|Pass Execution|Pass Execution If|Regexp Escape|Remove Tags|Repeat Keyword|Replace Variables|Return From Keyword|Return From Keyword If|Run Keyword|Run Keyword And Continue On Failure|Run Keyword And Expect Error|Run Keyword And Ignore Error|Run Keyword And Return Status|Run Keyword If|Run Keyword If All Critical Tests Passed|Run Keyword If All Tests Passed|Run Keyword If Any Critical Tests Failed|Run Keyword If Any Tests Failed|Run Keyword If Test Failed|Run Keyword If Test Passed|Run Keyword If Timeout Occurred|Run Keyword Unless|Run Keywords|Set Global Variable|Set Library Search Order|Set Log Level|Set Suite Documentation|Set Suite Metadata|Set Suite Variable|Set Tags|Set Test Documentation|Set Test Message|Set Test Variable|Set Variable|Set Variable If|Should Be Empty|Should Be Equal|Should Be Equal As Integers|Should Be Equal As Numbers|Should Be Equal As Strings|Should Be True|Should Contain|Should Contain X Times|Should End With|Should Match|Should Match Regexp|Should Not Be Empty|Should Not Be Equal|Should Not Be Equal As Integers|Should Not Be Equal As Numbers|Should Not Be Equal As Strings|Should Not Be True|Should Not Contain|Should Not End With|Should Not Match|Should Not Match Regexp|Should Not Start With|Should Start With|Sleep|Variable Should Exist|Variable Should Not Exist|Wait Until Keyword Succeeds"
builtin_keywords=builtin.split("|")
make_index_file("BuiltIn.index",builtin_keywords)

oslib="Append To File|Copy Directory|Copy File|Count Directories In Directory|Count Files In Directory|Count Items In Directory|Create Directory|Create File|Directory Should Be Empty|Directory Should Exist|Directory Should Not Be Empty|Directory Should Not Exist|Empty Directory|Environment Variable Should Be Set|Environment Variable Should Not Be Set|File Should Be Empty|File Should Exist|File Should Not Be Empty|File Should Not Exist|Get Binary File|Get Environment Variable|Get Environment Variables|Get File|Get File Size|Get Modified Time|Grep File|Join Path|Join Paths|List Directories In Directory|List Directory|List Files In Directory|Log Environment Variables|Log File|Move Directory|Move File|Normalize Path|Read Process Output|Remove Directory|Remove Environment Variable|Remove File|Remove Files|Run|Run And Return Rc|Run And Return Rc And Output|Set Environment Variable|Set Modified Time|Should Exist|Should Not Exist|Split Extension|Split Path|Start Process|Stop All Processes|Stop Process|Switch Process|Touch|Wait Until Created|Wait Until Removed"
os_keywords=oslib.split("|")
make_index_file("OperatingSystem.index",os_keywords)
    
sshot="Set Screenshot Directory|Take Screenshot|Take Screenshot Without Embedding"
sshot_keywords=sshot.split("|")
make_index_file("Screenshot.index", sshot_keywords)

telnet="Close All Connections|Close Connection|Execute Command|Login|Open Connection|Read|Read Until|Read Until Prompt|Read Until Regexp|Set Default Log Level|Set Encoding|Set Newline|Set Prompt|Set Timeout|Switch Connection|Write|Write Bare|Write Until Expected Output"
telnet_keywords=telnet.split("|")
make_index_file("Telnet.index", telnet_keywords)

stringlib="Decode Bytes To String|Encode String To Bytes|Fetch From Left|Fetch From Right|Generate Random String|Get Line|Get Line Count|Get Lines Containing String|Get Lines Matching Pattern|Get Lines Matching Regexp|Get Substring|Replace String|Replace String Using Regexp|Should Be Byte String|Should Be Lowercase|Should Be String|Should Be Titlecase|Should Be Unicode String|Should Be Uppercase|Should Not Be String|Split String|Split String From Right|Split String To Characters|Split To Lines"
stringlib_keywords=stringlib.split("|")
make_index_file("String.index", stringlib_keywords)

col="Append To List|Combine Lists|Convert To List|Copy Dictionary|Copy List|Count Values In List|Create Dictionary|Dictionaries Should Be Equal|Dictionary Should Contain Item|Dictionary Should Contain Key|Dictionary Should Contain Sub Dictionary|Dictionary Should Contain Value|Dictionary Should Not Contain Key|Dictionary Should Not Contain Value|Get Dictionary Items|Get Dictionary Keys|Get Dictionary Values|Get From Dictionary|Get From List|Get Index From List|Get Slice From List|Insert Into List|Keep In Dictionary|List Should Contain Sub List|List Should Contain Value|List Should Not Contain Duplicates|List Should Not Contain Value|Lists Should Be Equal|Log Dictionary|Log List|Remove Duplicates|Remove From Dictionary|Remove From List|Remove Values From List|Reverse List|Set List Value|Set To Dictionary|Sort List"
col_keywords=col.split("|")
make_index_file("Collections.index", col_keywords)

dialogs="Execute Manual Step|Get Selection From User|Get Value From User|Pause Execution"
dialogs_keywords=dialogs.split("|")
make_index_file("Dialogs.index", dialogs_keywords)

xml="Add Element|Clear Element|Copy Element|Element Attribute Should Be|Element Attribute Should Match|Element Should Exist|Element Should Not Exist|Element Should Not Have Attribute|Element Text Should Be|Element Text Should Match|Element To String|Elements Should Be Equal|Elements Should Match|Get Child Elements|Get Element|Get Element Attribute|Get Element Attributes|Get Element Count|Get Element Text|Get Elements|Get Elements Texts|Log Element|Parse Xml|Remove Element|Remove Element Attribute|Remove Element Attributes|Remove Elements|Save Xml|Set Element Attribute|Set Element Tag|Set Element Text"
xml_keywords=xml.split("|")
make_index_file("XML.index", xml_keywords)

process="Get Process Id|Get Process Object|Is Process Running|Process Should Be Running|Process Should Be Stopped|Run Process|Start Process|Switch Process|Terminate All Processes|Terminate Process|Wait For Process"
process_keywords=process.split("|")
make_index_file("Process.index", process_keywords)










