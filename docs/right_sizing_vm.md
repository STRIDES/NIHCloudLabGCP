# Guide to right-sizing your VM

## Monitor your CPU usage on Compute Engine

1. Go to the Compute Engine console, and select the instance name of the instance you want to monitor. Filter the metrics on the left as desired. For example, here we could drill down into just CPU metrics.

<img src="/images/1_observability_compute_engine.png" width="550" height="125">

2. If you need to resize your instance based on over- or under-utilization, first make sure the instance is stopped. Then click **Edit** at the top of the page.

<img src="/images/2_edit_compute_engine.png" width="550" height="125">

3. Now scroll down to *Machine configuration* and change the machine type as needed. Then click **Save**.

<img src="/images/3_change_machine_type_compute_engine.png" width="550" height="125">

## Monitor your CPU usage on Vertex AI

1. Select the notebook instance your are interested in, and select the *Montoring* tab. Now you can view CPU metrics. You can also look at the instance in Compute Engine and follow the instructions above. 

<img src="/images/4_monitor_VertexAI.png" width="550" height="125">

2. If you need to resize your instance based on over- or under-utilization, first make sure the instance is stopped. Then click **Edit** at the top of the page. Scroll down to *Machine Configuration*, and select an appropriate machine type.

<img src="/images/5_edit_vertexai.png" width="550" height="125">

