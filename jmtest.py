import os
import os.path

check_file = os.path.isfile("HTTPRequest.jmx")
echo check_file
if check_file=="True":
  echo check_file
  y = os.path.abspath("./HTTPRequest.jmx")
  z = y.replace('\\','\\\\') 

  initial_path = "jmeter -Jjmeter.save.saveservice.output_format=xml -n -t"
  command = "-l HTTPRequest.jtl"


  final = initial_path + " " + z + " " + command

  os.system(final)
