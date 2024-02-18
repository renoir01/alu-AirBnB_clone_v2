0. Prepare your web servers
This task involves setting up your web servers for the deployment of web_static. It includes installing Nginx if not already installed, creating necessary folders, creating a fake HTML file for testing Nginx configuration, setting ownership, and updating Nginx configuration.

1. Compress before sending
Write a Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB Clone repo, using the function do_pack.

2. Deploy archive!
Write a Fabric script that distributes an archive to your web servers, using the function do_deploy.

3. Full deployment
Write a Fabric script that creates and distributes an archive to your web servers, using the function deploy.
