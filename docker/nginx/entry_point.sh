#!/usr/bin/env sh

run_nginx() {
    nginx_pid=0

    # SIGTERM-handler
    term_handler() {
        # gracefully stopping nginx
        if [ $nginx_pid -ne 0 ]; then
            echo "Stopping nginx"
            kill -SIGQUIT "$nginx_pid"
            wait "$nginx_pid"
        fi

        exit 0; # or exit 143; 128 + 15 -- SIGTERM
    }

    # Trap terminating signals
    trap 'term_handler' USR1 INT TERM

    nginx -g 'daemon off;' &
    nginx_pid="$!"

    echo 'Server started...';
    wait ${nginx_pid}
}

run_nginx;