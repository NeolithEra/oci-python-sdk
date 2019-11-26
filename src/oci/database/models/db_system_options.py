# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DbSystemOptions(object):
    """
    The DB system options.
    """

    #: A constant which can be used with the storage_management property of a DbSystemOptions.
    #: This constant has a value of "ASM"
    STORAGE_MANAGEMENT_ASM = "ASM"

    #: A constant which can be used with the storage_management property of a DbSystemOptions.
    #: This constant has a value of "LVM"
    STORAGE_MANAGEMENT_LVM = "LVM"

    def __init__(self, **kwargs):
        """
        Initializes a new DbSystemOptions object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param storage_management:
            The value to assign to the storage_management property of this DbSystemOptions.
            Allowed values for this property are: "ASM", "LVM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type storage_management: str

        """
        self.swagger_types = {
            'storage_management': 'str'
        }

        self.attribute_map = {
            'storage_management': 'storageManagement'
        }

        self._storage_management = None

    @property
    def storage_management(self):
        """
        Gets the storage_management of this DbSystemOptions.
        The storage option used in DB system. For 1-node VM systems, you can specify either `Automatic Storage Management (ASM)`__ or `Logical Volume Manager (LVM)`__. For more information, see `Bare Metal and Virtual Machine DB Systems`__.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=OSTMG-GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5
        __ https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-57C50259-9472-4ED0-8818-DB9ABA96EC8E
        __ https://docs.cloud.oracle.com/Content/Database/Concepts/overview.htm#fastprovisioning

        Allowed values for this property are: "ASM", "LVM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The storage_management of this DbSystemOptions.
        :rtype: str
        """
        return self._storage_management

    @storage_management.setter
    def storage_management(self, storage_management):
        """
        Sets the storage_management of this DbSystemOptions.
        The storage option used in DB system. For 1-node VM systems, you can specify either `Automatic Storage Management (ASM)`__ or `Logical Volume Manager (LVM)`__. For more information, see `Bare Metal and Virtual Machine DB Systems`__.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=OSTMG-GUID-BC612D35-5399-4A35-843E-CF76E3D3CDB5
        __ https://www.oracle.com/pls/topic/lookup?ctx=en/database/oracle/oracle-database/19&id=ADMIN-GUID-57C50259-9472-4ED0-8818-DB9ABA96EC8E
        __ https://docs.cloud.oracle.com/Content/Database/Concepts/overview.htm#fastprovisioning


        :param storage_management: The storage_management of this DbSystemOptions.
        :type: str
        """
        allowed_values = ["ASM", "LVM"]
        if not value_allowed_none_or_none_sentinel(storage_management, allowed_values):
            storage_management = 'UNKNOWN_ENUM_VALUE'
        self._storage_management = storage_management

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
