#!/bin/bash

echo "Importing..."


curl http://pixmatch-r.hackdays.tineye.com/rest/                  \
     -F "method=add"                                \
     -F "images[0]=@HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg;filename=gackers_HACKWATERLOO-Y-U-NO-ENJOY-SUNLIGHT.jpg" \
     -F "images[1]=@HackWaterloo-Y-U-NO-MAKE-RESERVATION-SYSTEM.jpg;filename=gackers_HackWaterloo-Y-U-NO-MAKE-RESERVATION-SYSTEM.jpg" \
     -F "images[2]=@HACKWATERLOO-Y-U-NO-USE-CASTROLLER.jpg;filename=gackers_HACKWATERLOO-Y-U-NO-USE-CASTROLLER.jpg" \
     -F "images[3]=@HACKWATERLOO-Y-U-NO-USE-FRESHBOOKS.jpg;filename=gackers_HACKWATERLOO-Y-U-NO-USE-FRESHBOOKS.jpg" \
     -F "images[4]=@HACKWATERLOO-Y-U-NO-USE-POSTRANK.jpg;filename=gackers_HACKWATERLOO-Y-U-NO-USE-POSTRANK.jpg" \
     -F "images[5]=@HACKWATERLOO-Y-U-NO-USE-YELLOWPAGES.jpg;filename=gackers_HACKWATERLOO-Y-U-NO-USE-YELLOWPAGES.jpg"
