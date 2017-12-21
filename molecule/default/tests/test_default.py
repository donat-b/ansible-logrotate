import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_logrotate_conf(host):
    f = host.file('/etc/logrotate.conf')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o644

def test_logrotate_is_installed(host):
    logrotate = host.package("logrotate")
    assert logrotate.is_installed
