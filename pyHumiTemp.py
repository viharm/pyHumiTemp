#!/usr/bin/python3
# coding=utf-8

## @package   pyHumiTemp
#  \author    Vihar Malviya
#  \version   See VERSION
#  \brief     Program to provide numeric string output of humidity from DHT22
#  \details   Program to provide numeric string output of humidity from DHT22
#             by using tango's binary.
#             Depends on //tango// (http://blog.e-photographer.net/?p=927)
#  \copyright Copyright (C) 2015, Vihar Malviya;
#  \license   Modified BSD (3-clause) license
#             (see LICENSE or http://opensource.org/licenses/BSD-3-Clause)

## Description of variable prefixes
# st__ : String variable
# nm__ : Numeric (integer or float) variable
# ar__ : Array variable (associative arrays are dictionaries, non-associative are lists or tuples )
# ak__ : Array key
# ss__ : Status variable
# bl__ : Boolean variable
# ag__ : Arguments
# ob__ : Object

import sys , getopt
import time
import subprocess

# Initialise exit status
ss__ExitStatus = 1

# Define the main function
def main ( ag__ArgList ) :

  # Initialise the working variables, tweak as per need
  ar__Tango = {
    "ak__Bin" : "/home/odin/tango" ,
    "ak__Device" : "rht03" ,
    "ak__Gpio" : "27" }

  # Scan for script arguments
  try :
    # Parse the supplied arguments
    ar__ArgOption , ar__ArgRemainder = getopt.getopt ( ag__ArgList , "hp:" , [ "help" , "param=" ] )
    # Call help if no aruments supplied
    if len ( ar__ArgOption ) == 0 :
      fn__Help ( )
  # Call help if confused
  except getopt.GetoptError :
    fn__Help ( )

  # Check supplied arguments/parameters
  for st__ArgParam , st__ArgValue in ar__ArgOption :
    # Call help if requested so
    if st__ArgParam in ( "-h" , "--help" ) :
      fn__Help ( )
    # Read disk request
    elif st__ArgParam in ( "-p" , "--param" ) :
      st__ParamRequest = st__ArgValue
      # Check for qualifying arguments
      if ( st__ParamRequest != "temperature" and st__ParamRequest != "humidity" ) :
        fn__Help ( )

  # //tango// outputs errors liberally as it verifies checksum of DHT22's output
  # Check output at least five times before error.
  for nm__LoopCounter01 in range ( 5 ) :

    # Run //tango// using the supplied working variables
    ob__TangoProc = subprocess.Popen (
      [
        ar__Tango [ "ak__Bin" ] ,
        ar__Tango [ "ak__Device" ] ,
        ar__Tango [ "ak__Gpio" ] ] ,
      stdout = subprocess.PIPE ,
      stderr = subprocess.STDOUT ,
      universal_newlines = True )

    # Store the output of //tango//
    st__TangoRaw = ob__TangoProc.stdout.read ( )

    # If no error is found in the //tango// output then break out of the loop
    if st__TangoRaw.find ( "ERROR" ) == -1 :
      break

    # Wait for one second
    time.sleep ( 1 )

  # Notify if the error is found in the //tango// output even after five tries
  if st__TangoRaw.find ( "ERROR" ) != -1 :
    fn__Error ( )

  # Finally, start parsing the raw //tango// output
  else :
    # //tango// outputs in the following format
    # YYYY/mm/dd HH:MM:SS,θθ.θ,ɸɸ.ɸ,?
    # YYYY => year
    # mm   => month
    # dd   => date
    # HH   => hour
    # MM   => minute
    # SS   => second
    # θ    => temperature
    # ɸ    => relative humidity
    # ?    => unknown flag (possibly reading count)
    # use "," to split the output into list of disks
    ar__Dht22ParamList = st__TangoRaw.split ( "," )
    
    # The temperature is the second item
    nm__Temperature = ar__Dht22ParamList [ 1 ]

    # The humidity is the third item
    nm__Humidity = ar__Dht22ParamList [ 2 ]

    if st__ParamRequest == "temperature" :
      print ( nm__Temperature )
    elif st__ParamRequest == "humidity" :
      print ( nm__Humidity )
    else :
      fn__Help ( )

    # Set exit status success flag
    ss__ExitStatus = 0

  return ss__ExitStatus

def fn__Help ( ) :
  print ( "Usage:" , sys.argv [ 0 ] , "-p <parameter> (--param=<parameter>)" )
  sys.exit ( 2 )

def fn__Error ( ) :
  print ( "Error" )
  sys.exit ( 3 )

if __name__ == "__main__" :
  sys.exit ( main ( sys.argv [ 1: ] ) )
