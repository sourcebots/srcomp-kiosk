package { "iceweasel":
  ensure => installed,
}

package { "unclutter":
  ensure => installed,
}

package { "python3-yaml":
  ensure => installed,
}

package { "x11-xserver-utils":
  ensure => installed,
}

file { "/etc/srcomp-kiosk":
  ensure => directory,
}

$url = hiera('url')

file { "/etc/srcomp-kiosk/config.yaml":
  ensure => file,
  content => "url: '${url}'",
}

file { "/home/pi/.config/autostart":
  ensure => directory,
  owner => "pi",
}

file { "/home/pi/.config/autostart/kiosk.desktop":
  ensure => link,
  target => "/home/pi/srcomp-kiosk/kiosk.desktop",
  owner => "pi",
}
