# {{ ansible_managed }}

# jc 2022-12-16

[ $UID -le 1000 ] && return

change_cache()
{
  local d=/tmp/.cache$UID
  [ "$XDG_CACHE_HOME" == "$d" ] && return  # already done

  [ -d $d ] || mkdir -m 700 $d
  export XDG_CACHE_HOME=$d

  d=$HOME/.cache
  [ -d $d ] && rm -rf $d > /dev/null 2>&1

  ccache --clear > /dev/null 2>&1
}

change_cache