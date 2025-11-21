FROM nginx:alpine

COPY default.conf /etc/nginx/conf.d/default.conf

VOLUME /etc/letsencrypt
VOLUME /var/www/certbot

CMD ["nginx", "-g", "daemon off;"]