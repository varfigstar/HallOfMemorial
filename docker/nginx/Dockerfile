FROM nginx

COPY /images /images
COPY /docker/nginx/entry_point.sh /entry_point.sh

CMD nginx -t \
    # Forward nginx request and error logs to docker log collector
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["/entry_point.sh"]
