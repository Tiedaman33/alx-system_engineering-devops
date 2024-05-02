#In an nginx configuration settings for servers(websites), the etc/nginx/sites-available/default is the file where the configuration is done, and then activated by creating a symbolic link between the etc/nginx/sites-enabled/default and etc/nginx/sites-available/default.

#If for some reason port 80 is refusing to bind to all ipv4 addresses, we could go back to etc/nginx/sites-available/default, reconfigure it and create another symbolic link or we could just go straight into etc/nginx/sites-enabled/default and modify it.

The etc/nginx/sites-enabled/default file looks typically like this:


server {
        listen 80 default_server;  # This is the line that binds port 80 to all ipv4 addresses
        listen [::]:80 default_server;  # This is the line that binds port 80 to all ipv6 addresses

        root /var/www/html;

        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
}

#If we look at this configuration file we will see that this line listen 80 default_server;   is the line that binds port 80 to all ipv4 addresses, so if port 80 is refusing to bind to all ipv4 addresses, its because of one of these many reasons:

1]
listen 80 default_server;   
missing or miss configured,
2]
 another web server like apache is active and using port 80,
3]
or etc/nginx/sites-enabled/default in nginx has the right configuration, but nginx itself is not run with sudo privileges,
4]
 the ufw firewall configuration might be restricting the nginx process from binding to port 80,


#Assuming the issue is one of these four, we will look at how to deal with each and automate a file to make it right. Create a file 0-nginx_likes_port_80 and add this to the file, after adding it, make it an executable and run it.
