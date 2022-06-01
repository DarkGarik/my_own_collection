#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Create file in your path

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    path:
        description: path in you file
        required: true
        type: str
    content:
        description: content in you file
        required: true
        type: str


author:
    - Sergey (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_own_module:
    path: /tmp/test.txt
    content: test string


'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.

'''

from ansible.module_utils.basic import AnsibleModule
import os.path


def create_file():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )
    result = dict(
        changed=False
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    if os.path.exists(module.params['path']) == False:
        with open(module.params['path'], 'w', encoding='utf-8') as f:
            f.write(module.params['content'])

        with open(module.params['path']) as f:
            read_content = f.read()
            if read_content == module.params['content']:
                result['changed'] = True
            else:
                module.fail_json(msg='ERROR: content does not match ', **result)

        module.exit_json(**result)
    else:
        module.exit_json(**result)

def main():
    create_file()


if __name__ == '__main__':
    main()
