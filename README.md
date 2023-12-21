onnx txt editor to delete a node or to replace the certain line by understand the name of the node


--nodename /teacher/Sub               Name of the node to delete")
--filename file.txt                   Name of file to edit")
--nodefile nodenamefile.txt           File of the nodename to delete")
--mode delete/replace                 Mode that delete nodes or replace a certain line
--replacefile                         File of the lines to replace")

***************************
when mode is set as delete
--nodefile nodenamefile.txt
#In this mode can delete the whole node

name: "/teacher/Sub"
name: "/teacher/Div"
***************************
when mode is set as replace
--replacefile line2replace.txt 
#In this mode can replace a certain with indicate the name of the name
#element of the last element of each line need space
#1st position is the node name which included the replace line
#2nd position is the the target to replace
#3nd position is the str that to replace 2nd position

"/teacher/Sub",input: "/teacher/Constant_output_0",    input: "input"
"/student/conv1/Conv",input: "student.conv1.weight",    input: "input"
"/ae/encoder/enconv1/Conv",input: "ae.encoder.enconv1.weight",    input: "input"
