#!/bin/bash
# Add to instance metadata with `gcloud compute instances add-metadata \
#   instance-name --metadata-from-file startup-script=idle-shutdown.sh` and reboot
# NOTE: requires `bc`, eg, sudo apt-get install bc
# Modified from https://stackoverflow.com/questions/30556920/how-can-i-automatically-kill-idle-gce-instances-based-on-cpu-usage

sudo apt-get install bc -y

# This is the CPU usage threshold. If activity falls below 10% for the specified time below, the VM shutsdown.
# If you want the shutdown to be more sensitive, you can set this higher, so that a smaller drop in CPU activity will cause shutdown.

threshold=0.1 

count=0
wait_minutes=60 ##### This is where you change the number of idle minutes before you want the VM to shutdown ####
while true
do

  load=$(uptime | sed -e 's/.*load average: //g' | awk '{ print $1 }') # 1-minute average load
  load="${load//,}" # remove trailing comma
  res=$(echo $load'<'$threshold | bc -l)
  if (( $res ))
  then
    echo "Idling.."
    ((count+=1))
  fi
  echo "Idle minutes count = $count"

  if (( count>wait_minutes ))
  then
    echo Shutting down
    # wait a little bit more before actually pulling the plug
    sleep 300
    sudo poweroff
  fi

  sleep 60

done
