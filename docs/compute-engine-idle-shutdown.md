# How to configure Compute Engine VM to auto-shutdown when idle

*Assumption: Your VM is already created.* 



## Step 1: Upload the idle-shutdown shell script to the VM instance. 

First, ssh into your vm 
To comply with this guide, upload the script in `/opt/deeplearning/bin` directory. Create the folders if not in existence:  `sudo mkdir –p /opt/deeplearning/bin`

```shell
curl https://gist.githubusercontent.com/justinshenk/312b5e0ab7acc3b116f7bf3b6d888fa4/raw/59f021c2bf0388ba36e5a589dba52e233ee84964/idle-shutdown.sh > /opt/deeplearning/bin/idle-shutdown.sh 
```

After saving idle-shutdown.sh file, run: 
```shell
sudo chmod +x idle-shutdown.sh        # make the script executable 
```

*Note:* *The* `/opt/deeplearning/bin` *directory is default path google uses to store system management scripts.*

---
## Step 2: Configure the Metadata of the instance 

Next, we need to add a metadata ***‘startup-script’*** through the VM instance edit mode. Scroll to the ***‘Custom metadata’*** section, click ***‘add item’***, enter the `startup-script` in the left box and `/opt/deeplearning/bin/idle-shutdown.sh` (the path to the script we saved in **step 1** in the right box. Save and Exit the instance edit mode. 

![VM Instance editing Metadata](./compute_engine.jpeg)

*Note:*

*The default settings in the start-up script is to shut-down the VM instance when the instance CPU usage has been 10% or less for one consecutive hour. You can customize the CPU usage threshold (10%) and/or idle time window (one hour).  But to make things easy, leave the default setting as it is.*

 

---
## Step 3: Install package `bc`

Package `bc` is required to check the instance cpu usage. You can install the packages on Linux VM instance as: 
```shell
sudo apt-get install bc 
```


---
## Step 4: Reboot your instance: 

```shell
sudo reboot 
```

With these steps, everything is ready.  Your VM should shut down automatically after 1 hour of no activity. 
