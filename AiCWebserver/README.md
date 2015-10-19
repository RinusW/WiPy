AiCWebserver
This is a simple webserver for the WiPy, aimed at control applications. The accompanian webpage consist of two input elements, one of type range and one of type number. Changing either of them will generate an Ajax GET to the server who responds with the value of the input element. That value is then imposed to the other element. The necessary javascript is in the header section of the webpage.
A standard GET request to the server will result in the server sending the AiCwebpage.htm html file. This file should be located in the default directory.

