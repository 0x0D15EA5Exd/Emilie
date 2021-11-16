# Emilie


Emilie is my solution to prevent code/binary theft. It acts like a DRM. 
It conditions the access to the rest of the code as well as its decryption to the passage of a key, in argument of the executable. 

It is a dynamic library, which integrates the code allowing to validate the key, as well as functions to be called randomly in the program to condition its operation to a compilation including this library. The deletion of the functions call must totally prevent the program from working, or else indicate that the code used is a stolen version.
It must also prevent reverse engineering.

