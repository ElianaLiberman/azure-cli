# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: skip-file
# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RepositoryProvisionResponseBase(Model):
    """RepositoryProvisionResponseBase.

    :param status: Possible values include: 'Provisioning', 'Provisioned',
     'Deleting', 'Deleted'
    :type status: str or ~digitaltwinrepositoryprovisioningservice.models.enum
    :param provisioning_state:
    :type provisioning_state: str
    :param id:
    :type id: str
    :param poll_back_uri:
    :type poll_back_uri: str
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'poll_back_uri': {'key': 'pollBackUri', 'type': 'str'},
    }

    def __init__(self, status=None, provisioning_state=None, id=None, poll_back_uri=None):
        super(RepositoryProvisionResponseBase, self).__init__()
        self.status = status
        self.provisioning_state = provisioning_state
        self.id = id
        self.poll_back_uri = poll_back_uri
