# Use the Nginx image from Docker Hub
FROM nginx:alpine

# Remove the default nginx index page
RUN rm /etc/nginx/conf.d/default.conf

# Copy the custom nginx configuration
COPY client/nginx.conf /etc/nginx/conf.d

# Copy the static content (HTML, CSS, JS) to the Nginx server
COPY client/src/ /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx when the container has provisioned
CMD ["nginx", "-g", "daemon off;"]
