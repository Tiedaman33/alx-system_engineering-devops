#!/usr/bin/bash

exec { 'pkill_killmenow':
  path    => '/usr/bin:/usr/sbin:/bin',
}

