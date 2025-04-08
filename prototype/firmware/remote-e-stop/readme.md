The emergency stop (e-stop) is a panic button for cutting power to the robot's motors. It
has both a physical button and can also be triggered digitally, for instance as a button on
a remote controller. The physical and remote functionality are independent, so a software
failure will not prevent the physical e-stop from working. 

The e-stop makes use of a relay to switch the power circuit to the motor controller.
A relay is like an electrically controlled switch, where a low-power signal can be used to
switch a high-power circuit. The relay used is commonly open, single-pole double-throw.
A single-pole single-throw would make more sense, but this is the one we have available in
the lab. 

The code in this folder is merely a proof-of-concept for the remote control functionality.
When the `RELAY_INPUT_PIN` is set to LOW, the relay switches and interrupts the otherwise
closed circuit. As a stand-in for a remote controller, the code features a tiny web server
hosting a form. Using buttons on this form you can trigger or reset the e-stop.

To access the form, flash an ESP with this code, open a serial connection on your PC and hit
the reset button on the ESP. It will print the server's IP address over serial. The IP is
only reachable when connected to the WiFi network hosted by the ESP.
