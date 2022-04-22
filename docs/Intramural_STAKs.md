### Obtaining your Short Term Access Keys for Intramural Cloud Lab Users
If you have an NIH identity, you can access your Short Term Access Keys (STAKs) at the same place you access the AWS console (https://iam.nih.gov, VPN or Campus only).

Click `Cloud Access` > [Account Number] > `Short-term access keys` and then you can authenticate using any of the three options. 
You can either paste in the text from Option 1 to your terminal window, or you can use `aws configure` and paste in the Access Key and Secret Access Keys individually. 

At some point you probably need to use aws configure to set your default region. You can also set your default region using `aws configure set region <region>`.

Note that if you get logged out, sometimes your STAKs will no longer be valid. If you get an unexpected error, check that you have CLI access with something like `aws s3 ls`. If you get an error, just log back in, retrieve new keys, and redo the authentication.
