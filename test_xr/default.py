"""
Here you can explain the purpose of your test file

"""
import pytest
from comfy.compliance import *  # noqa

# if all tests are for one platform: short-cut specification is like so:
# pytestmark = pytest.mark.platform('Cisco_IOS')

'''
# skeleton example of a rule function

@high(
    name='Arbitrary text describing this rule'
)
def rule_function(source: Source):
    # write here your assertions
    # assert 'ssh mgmt-auth public-key' in source.lines
    pass
'''


@medium(
    name='rule_connection',
    platform=['cisco_xr'],
    # commands=dict(version='show version')
)
def rule_connection(configuration, commands, device):
    assert 'aaa' in configuration
    # assert 'text' in commands.version
    # version = device.cli('show version')
    # assert 'text' in commands.version
    # version = device.cli('show version')