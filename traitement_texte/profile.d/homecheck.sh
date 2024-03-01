# jc 2012-12-16

# emerg, alert, crit, warning, notice, info, debug
#     1,     2,    3,       4,      5,    6,     7


[ $UID -le 1000 ] && return

homecheck()
{
  m=unset	 
  f=/tmp/.$UID.homecheck

  [ -e $f ] && { echo "alert already sent !" > $f ; return ; }

  if [[ $HOME =~ /tmp/ ]] 
  then
        m="no std homedir '$HOME' for user '$USER'"
        logger -e -p crit -t userland "$m"
        /usr/local/sbin/reportbymail "$m"
	at now +5minutes<< EOAT
	kdialog --ok-label "J'ai compris" --error \
"ATTENTION

Vous n'êtes pas autorisé à utiliser cet ordinateur. 
Vos données seront perdues à la fin de cette session.
"
EOAT
  fi

  if [ ! -d $HOME ] 
  then
        m="homedir '$HOME' not found for user '$USER'"
        logger -e -p alert -t userland "$m"
        /usr/local/sbin/reportbymail "$m"
  fi

  echo $m > $f
}

homecheck
unset homecheck
