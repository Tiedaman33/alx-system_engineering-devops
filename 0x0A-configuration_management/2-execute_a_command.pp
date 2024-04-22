#Using Puppet, create a manifest that kills a process named killmenow.
exec { 'pkill_killmenow':
	path => '/usr/bin:/usr/sbin:/bin',
}
