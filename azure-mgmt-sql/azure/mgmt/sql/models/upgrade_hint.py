# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpgradeHint(Model):
    """Represents a Upgrade Hint.

    :param target_service_level_objective: TargetServiceLevelObjective for
     upgrade hint.
    :type target_service_level_objective: str
    :param target_service_level_objective_id: TargetServiceLevelObjectiveId
     for upgrade hint.
    :type target_service_level_objective_id: str
    """

    _attribute_map = {
        'target_service_level_objective': {'key': 'targetServiceLevelObjective', 'type': 'str'},
        'target_service_level_objective_id': {'key': 'targetServiceLevelObjectiveId', 'type': 'str'},
    }

    def __init__(self, target_service_level_objective=None, target_service_level_objective_id=None):
        self.target_service_level_objective = target_service_level_objective
        self.target_service_level_objective_id = target_service_level_objective_id
