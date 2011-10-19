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
#     This is a small and quite bad testprogram for the lirc module but
#     it's getting better...
#
#  $Id: pylirc_testUnExtended.py,v 1.1 2003/02/22 22:51:01 mccabe Exp $
#  $Log: pylirc_testUnExtended.py,v $
#  Revision 1.1  2003/02/22 22:51:01  mccabe
#  Previous, accidental commit:
#  Added Brian J. Murrell's code to fetch repeatcount
#
#  This commit:
#  Changed Brians code to return a dictionary instead of a list.
#  Removed lirc_nextcode_ext() and merged it with lirc_nextcode() - new optional argument controls return type. Old programs should work as
#  before and new programs can benefit the new behaviour by passing true as first argument.
#
#  Revision 1.6  2002/12/21 20:30:26  mccabe
#  Added id and log entries to most files
#
import pylirc, time

blocking = 0;

#
if(pylirc.init("pylirc", "./conf", blocking)):

   code = ""
   while(code != "quit"):

      # Very intuitive indeed
      if(not blocking):
         print "."

         # Delay...
         time.sleep(1)

      # Read next code
      s = pylirc.nextcode()

      # Loop as long as there are more on the queue
      # (dont want to wait a second if the user pressed many buttons...)
      while(s):
         print s
         # Print all the configs...
         for code in s:
            print code

            if(code == "blocking"):
               blocking = 1
               pylirc.blocking(1)

            elif(code == "nonblocking"):
               blocking = 0
               pylirc.blocking(0)

         # Read next code?
         if(not blocking):
            s = pylirc.nextcode()
         else:
            s = 0

   # Clean up lirc
   pylirc.exit()

   
