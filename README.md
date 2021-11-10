# Automatic_Webpage_to_PROGMEM #  
ESP8266 project mostly involve the use of WiFi where the ESP8266 acts as a server hosting a webpage.  
This **Webpage or Web interface** in the Embedded C++ code is usually written in the form of a C++ rawliteral format where the webpage is written as it is without the use of any escape sequence and is strored in the PROGMEM to save SRAM.  
#### This is a python script which automatically detects code changes when saved and converts the html, css, js to header files containing webpage data in the form of PROGMEM constants making it very simple to deploy fresh changes onto the Prototype. ####
