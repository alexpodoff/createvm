#!/bin/bash

list="
ald-client-common
ald-admin-common
fly-admin-ald-se
apache2
libapache2-mod-auth-kerb
libapache2-mod-auth-pam
libapache2-mod-php5
php5-pgsql
exim4-daemon-heavy
dovecot-imapd
dovecot-gssapi
postgresql-astra-full
"

apt-get -y install ${list}
apt-get clean
