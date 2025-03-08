import json

open_file = open("info.json", "r")
json_string=open_file.read()
open_file.close()

dictionary = json.loads(json_string)

go_code="package gogeInfo\n"
for key in dictionary:
    if type(dictionary[key]) is str:
        go_code+="""
func get"""+key+"""() string{
    return \""""+str(dictionary[key])+"""\"
}
        """
    elif type(dictionary[key]) is int:
        go_code+="""
func get"""+key+"""() int{
    return """+str(dictionary[key])+"""
}
"""
    elif type(dictionary[key]) is float:
        go_code+="""
func get"""+key+"""() float64{
    return """+str(dictionary[key])+"""
}
"""
    elif type(dictionary[key]) is bool:
        if dictionary[key]==True:
            dictionary[key]="true"
        else:
            dictionary[key]="false"
        go_code+="""
func get"""+key+"""() bool{
    return """+str(dictionary[key])+"""
}
"""

open_file = open("info.go", "w")
open_file.write(go_code)
open_file.close()