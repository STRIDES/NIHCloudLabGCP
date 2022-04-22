### Using the Amazon Genomics CLI (agc) in Coud Lab

The following instructions follow the [AWS docs](https://aws.github.io/amazon-genomics-cli/docs/), but with some tips and tricks specific to Cloud Lab.

You can do all of the following from your local computer using the AWS SDK, but to ensure things go smoothly in the Cloud Lab environment, we recommend you spin up a VM and follow along from within your EC2 instance.
Because agc uses AWS Batch for computation, you can get away with spinning up a small VM, like the t2 micro for this tutorial. Once you VM is ready, ssh into it.

Make sure you install the `Prerequisites` page. Install the AWS CLI if running locally, and if on EC2, you just need to install nodejs.

Make sure you run `aws configure` and input your Short-term Access keys. Intramural users can access keys following [these instructions](/docs/STAKs_intramural.md).

Now run the install instructions and add agc to the path with `export PATH=$HOME/bin:$PATH`

If the install went well, go ahead and activate. Normally, agc will create a bucket and a virtual private cloud (VPC) for you to run your analyses. You are not allowed to create a new VPC in cloud lab, so you need to specify the existing VPC in the activate command. You can find this by searching `VPC` in the search bar, then go to the VPC for your project and then copy the VPC ID.
Now run `agc account activate --vpc <vcp-id>`. You can optionally specify a bucket with `--bucket <bucket-name>`

If for some reason the activation fails, you need to go to s3 and delete the bucket agc created and then try again.

If everything works, then it will take about 4 minutes to finish bootstrapping the infrastructure. 

Configure you email and you are all set up!

Now try running the examples. Note that the context name is in the yaml, and you need to deploy with the context name specified in the yaml for the specific example.

