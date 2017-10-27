Logrotate
=========

Logrotate configuration deployment

Requirements
------------

None

Role Variables
--------------

    # keep 4 weeks of backlogs
    logrotate_rotate: 4
    logrotate_compress: yes
    logrotate_compresscmd: 'xz'
    logrotate_compressoptions: '-6 -T0'
    logrotate_size: '60M'

    logrotate_options:
      # rotate log files weekly.
      - daily
      # create new (empty) log files after rotating old ones.
      - create
      # compress rotated log files.
      - compress
      # use date as a suffix of the rotated file.
      - dateext
      - notifempty
      - nomail
      - noolddir


Dependencies
------------

None

Example Playbook
----------------

    - hosts: webservers
      roles:
         - { role: ansible-logrotate }

License
-------

BSD
