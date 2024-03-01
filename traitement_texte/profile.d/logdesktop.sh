# jc 2012-12-16

# [ $UID -le 1000 ] && return

ident=$(getent passwd $USER | awk 'BEGIN {FS=":"} {print $1,$3,"\""$5"\""}')
logger -e -p info -t userland  "environment: $ident ${XDG_CURRENT_DESKTOP:-'-'}"

