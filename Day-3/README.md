# Day 2 Log

### PROBLEM STATEMENT
> Task 1: Learn the `rpm` package
> Task 2: Create a rpm package of the python code and install it in a specific directory

**METHODOLOGY**<br>
*Task 1*
1. Copy the code to a separate folder
2. Create a Docker container and run the `fedora` shell inside it
3. Installed necessary packages
4. Tested basic commands for querying, installing, updating, erasing. Also learned about writing a `.spec` file.

*Task 2*
1. Prepare a source directory by copying the contents of the file to be packaged.
2. Zip it using `tar`
3. Move it to the Docker container using `docker cp`
4. Move it to `~/rpmbuild/SOURCES/`
5. Create a .spec file inside `~/rpmbuild/SPECS/` using `vim`
6. Build the rpm using `rpm -ba ~/rpmbuild/SPECS/<package>.spec`
7. Install the rpm using `rpm -ivh ~/rpmbuild/RPMS/noarch/<package>.spec`
8. Run the Python file in `/opt/email-script/email_operations.py`


**WHAT I LEARNED**
1. What is RPM and its commands?
2. How to run Fedora inside Docker and get data from outside the container
3. How to package a folder into an RPM package
4. How to install it and run the contents

**REFERENCE MATERIAL**
1. https://man7.org/linux/man-pages/man8/rpm.8.html
2. https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/packaging_and_distributing_software/introduction-to-rpm_packaging-and-distributing-software
