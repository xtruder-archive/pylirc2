#!/usr/bin/python
#
#    pyLirc, lirc (remote control) module for python
#    Copyright (C) 2003 Linus McCabe <pylirc.linus@mccabe.nu>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
##
#
#     This is a test to test pyLirc with multiple threads
#
#     This is NOT a good example of coding, it's merely a test of functionality!
#     Don't take too much inspitation from the way things are done here...
#
#  $Id: pylirc_testmultithread.py,v 1.1 2003/02/22 22:12:40 mccabe Exp $
#  $Log: pylirc_testmultithread.py,v $
#  Revision 1.1  2003/02/22 22:12:40  mccabe
#  Testprogram to test pylirc in multiple threads
#
#
import pylirc, time, select
from threading import Thread

blocking = 0;
code = ""



class Timer(Thread):
   def __init__(self):
      Thread.__init__(self)
      
   def run(self):
      import time
      i = 0
      while(i < 10):
         i = i + 1
         print "Time class is ticking..." + str(i)
         time.sleep(1)
      
class IRRec(Thread):
   def __init__(self, lirchandle):
      Thread.__init__(self)
      self.lirchandle = lirchandle

   def run(self):
      global code
      print "IRRrec awaits IR commands"
      
      if(select.select([self.lirchandle], [], [], 6) == ([], [], [])):
         print "IRRrec timed out"
      else:
         s = pylirc.nextcode()

         if(s):
            # Print all the configs...
            for code in s:
               print code


lirchandle = pylirc.init("pylirc", "./conf", blocking)
if(lirchandle):

   print "Succesfully opened lirc, handle is " + str(lirchandle)
   
   
   tim = Timer()
   tim.start()

   irrec = IRRec(lirchandle)
   irrec.start()
      
   code = ""
   while(code != "quit"):

      if(irrec.isAlive() == 0):
         irrec = IRRec(lirchandle)
         irrec.start()
         
      # Very intuitive indeed
      #if(not blocking):
      print "."

      # Delay...
      time.sleep(1)


   # Clean up lirc
   pylirc.exit()





    
    
         
         