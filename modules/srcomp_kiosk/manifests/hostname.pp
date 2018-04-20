# Set the hostname on the Pis so that they can easily be identified when
# shelling in

class srcomp_kiosk::hostname ( $hostname = hiera('hostname') ) {

  if $::fqdn != $hostname {
    host { $::fqdn:
      ensure  => absent,
      before  => Exec['hostnamectl'],
    }

    if $::fqdn != $::hostname {
      host { $::hostname:
        ensure  => absent,
        before  => Exec['hostnamectl'],
      }
    }

    host { 'custom fqdn':
      ensure  => present,
      name    => $hostname,
      ip      => '127.0.1.1',
      before  => Exec['hostnamectl'],
    }

    file { '/etc/hostname':
      ensure  => present,
      owner   => 'root',
      group   => 'root',
      mode    => '0644',
      content => "${hostname}\n",
      notify  => Exec['hostnamectl'],
    }

    exec { 'hostnamectl':
      command     => "/usr/bin/hostnamectl set-hostname $hostname",
      refreshonly => true,
    }
  }
}
