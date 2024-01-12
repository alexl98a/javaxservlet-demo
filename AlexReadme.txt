This is a demo program that runs on the OpenShift Websphere base image UBI.
Use this to see a Websphere EAR application file run on OpenShift Local

Installation details
https://www.redhat.com/en/blog/rehosting-traditional-websphere-application-on-openshift-container-platform-ocp-on-google-cloud-gcp
Walkthrough of app
https://www.youtube.com/watch?v=FVOkcTBchV4&list=PLNlfyBuM9nD8Y3R0VcqOESlKhJ_HyXMkI
Websphere Traditional container image info
https://catalog.redhat.com/software/containers/r/ibmcom/websphere-traditional/5d77b2e4702c566f4cbf438b?architecture=amd64&image=5d3f80fdd70cc5521dfeac6c&container-tabs=gti

Git clone from URL https://github.com/gskumar1010/TA-klp-demo/
Set port to 9080 instead of 8080
Set DeployContainer instead of Deploy
Go to https://ta-klp-demo2-websphere-test.apps-crc.testing/hitcount to start application

This project uses a Docker file and Python scripts located in src/config to set up the Websphere app
The project appears to use Transformation Advisor to generate Python scripts to migrate from Websphere to OpenShift
https://www.ibm.com/docs/en/SS5Q6W/pdf/cta-documentation.pdf

Developing WAS Servlets
https://www.ibm.com/docs/en/was/8.5.5?topic=wa-servlets
https://www.ibm.com/docs/en/was/8.5.5?topic=ds-developing-servlets-websphere-application-server-extensions
