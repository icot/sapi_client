# coding: utf-8

"""
    CERN Unified Storage API

    A unified storage API for all data-storage back-ends.

    OpenAPI spec version: 2.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OptionalFromSnapshot(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, autosize_enabled=None, autosize_increment=None, max_autosize=None, active_policy_name=None, percentage_snapshot_reserve=None, compression_enabled=None, inline_compression=None, caching_policy=None, name=None, size_total=None, aggregate_name=None, junction_path=None, from_snapshot=None, from_volume=None):
        """
        OptionalFromSnapshot - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'autosize_enabled': 'bool',
            'autosize_increment': 'int',
            'max_autosize': 'int',
            'active_policy_name': 'str',
            'percentage_snapshot_reserve': 'int',
            'compression_enabled': 'bool',
            'inline_compression': 'bool',
            'caching_policy': 'str',
            'name': 'str',
            'size_total': 'int',
            'aggregate_name': 'str',
            'junction_path': 'str',
            'from_snapshot': 'str',
            'from_volume': 'str'
        }

        self.attribute_map = {
            'autosize_enabled': 'autosize_enabled',
            'autosize_increment': 'autosize_increment',
            'max_autosize': 'max_autosize',
            'active_policy_name': 'active_policy_name',
            'percentage_snapshot_reserve': 'percentage_snapshot_reserve',
            'compression_enabled': 'compression_enabled',
            'inline_compression': 'inline_compression',
            'caching_policy': 'caching_policy',
            'name': 'name',
            'size_total': 'size_total',
            'aggregate_name': 'aggregate_name',
            'junction_path': 'junction_path',
            'from_snapshot': 'from_snapshot',
            'from_volume': 'from_volume'
        }

        self._autosize_enabled = autosize_enabled
        self._autosize_increment = autosize_increment
        self._max_autosize = max_autosize
        self._active_policy_name = active_policy_name
        self._percentage_snapshot_reserve = percentage_snapshot_reserve
        self._compression_enabled = compression_enabled
        self._inline_compression = inline_compression
        self._caching_policy = caching_policy
        self._name = name
        self._size_total = size_total
        self._aggregate_name = aggregate_name
        self._junction_path = junction_path
        self._from_snapshot = from_snapshot
        self._from_volume = from_volume

    @property
    def autosize_enabled(self):
        """
        Gets the autosize_enabled of this OptionalFromSnapshot.

        :return: The autosize_enabled of this OptionalFromSnapshot.
        :rtype: bool
        """
        return self._autosize_enabled

    @autosize_enabled.setter
    def autosize_enabled(self, autosize_enabled):
        """
        Sets the autosize_enabled of this OptionalFromSnapshot.

        :param autosize_enabled: The autosize_enabled of this OptionalFromSnapshot.
        :type: bool
        """

        self._autosize_enabled = autosize_enabled

    @property
    def autosize_increment(self):
        """
        Gets the autosize_increment of this OptionalFromSnapshot.

        :return: The autosize_increment of this OptionalFromSnapshot.
        :rtype: int
        """
        return self._autosize_increment

    @autosize_increment.setter
    def autosize_increment(self, autosize_increment):
        """
        Sets the autosize_increment of this OptionalFromSnapshot.

        :param autosize_increment: The autosize_increment of this OptionalFromSnapshot.
        :type: int
        """

        self._autosize_increment = autosize_increment

    @property
    def max_autosize(self):
        """
        Gets the max_autosize of this OptionalFromSnapshot.

        :return: The max_autosize of this OptionalFromSnapshot.
        :rtype: int
        """
        return self._max_autosize

    @max_autosize.setter
    def max_autosize(self, max_autosize):
        """
        Sets the max_autosize of this OptionalFromSnapshot.

        :param max_autosize: The max_autosize of this OptionalFromSnapshot.
        :type: int
        """

        self._max_autosize = max_autosize

    @property
    def active_policy_name(self):
        """
        Gets the active_policy_name of this OptionalFromSnapshot.

        :return: The active_policy_name of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._active_policy_name

    @active_policy_name.setter
    def active_policy_name(self, active_policy_name):
        """
        Sets the active_policy_name of this OptionalFromSnapshot.

        :param active_policy_name: The active_policy_name of this OptionalFromSnapshot.
        :type: str
        """
        if active_policy_name is not None and len(active_policy_name) < 1:
            raise ValueError("Invalid value for `active_policy_name`, length must be greater than or equal to `1`")

        self._active_policy_name = active_policy_name

    @property
    def percentage_snapshot_reserve(self):
        """
        Gets the percentage_snapshot_reserve of this OptionalFromSnapshot.

        :return: The percentage_snapshot_reserve of this OptionalFromSnapshot.
        :rtype: int
        """
        return self._percentage_snapshot_reserve

    @percentage_snapshot_reserve.setter
    def percentage_snapshot_reserve(self, percentage_snapshot_reserve):
        """
        Sets the percentage_snapshot_reserve of this OptionalFromSnapshot.

        :param percentage_snapshot_reserve: The percentage_snapshot_reserve of this OptionalFromSnapshot.
        :type: int
        """

        self._percentage_snapshot_reserve = percentage_snapshot_reserve

    @property
    def compression_enabled(self):
        """
        Gets the compression_enabled of this OptionalFromSnapshot.

        :return: The compression_enabled of this OptionalFromSnapshot.
        :rtype: bool
        """
        return self._compression_enabled

    @compression_enabled.setter
    def compression_enabled(self, compression_enabled):
        """
        Sets the compression_enabled of this OptionalFromSnapshot.

        :param compression_enabled: The compression_enabled of this OptionalFromSnapshot.
        :type: bool
        """

        self._compression_enabled = compression_enabled

    @property
    def inline_compression(self):
        """
        Gets the inline_compression of this OptionalFromSnapshot.

        :return: The inline_compression of this OptionalFromSnapshot.
        :rtype: bool
        """
        return self._inline_compression

    @inline_compression.setter
    def inline_compression(self, inline_compression):
        """
        Sets the inline_compression of this OptionalFromSnapshot.

        :param inline_compression: The inline_compression of this OptionalFromSnapshot.
        :type: bool
        """

        self._inline_compression = inline_compression

    @property
    def caching_policy(self):
        """
        Gets the caching_policy of this OptionalFromSnapshot.

        :return: The caching_policy of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._caching_policy

    @caching_policy.setter
    def caching_policy(self, caching_policy):
        """
        Sets the caching_policy of this OptionalFromSnapshot.

        :param caching_policy: The caching_policy of this OptionalFromSnapshot.
        :type: str
        """

        self._caching_policy = caching_policy

    @property
    def name(self):
        """
        Gets the name of this OptionalFromSnapshot.
        The internal name of the volume

        :return: The name of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OptionalFromSnapshot.
        The internal name of the volume

        :param name: The name of this OptionalFromSnapshot.
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name

    @property
    def size_total(self):
        """
        Gets the size_total of this OptionalFromSnapshot.
        The total size of the volume,  in bytes. If creating, the size of the volume.

        :return: The size_total of this OptionalFromSnapshot.
        :rtype: int
        """
        return self._size_total

    @size_total.setter
    def size_total(self, size_total):
        """
        Sets the size_total of this OptionalFromSnapshot.
        The total size of the volume,  in bytes. If creating, the size of the volume.

        :param size_total: The size_total of this OptionalFromSnapshot.
        :type: int
        """

        self._size_total = size_total

    @property
    def aggregate_name(self):
        """
        Gets the aggregate_name of this OptionalFromSnapshot.
        If applicable, the aggregate to place the volume in (NetApp only). If not provided, will use the one with the most free space.

        :return: The aggregate_name of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._aggregate_name

    @aggregate_name.setter
    def aggregate_name(self, aggregate_name):
        """
        Sets the aggregate_name of this OptionalFromSnapshot.
        If applicable, the aggregate to place the volume in (NetApp only). If not provided, will use the one with the most free space.

        :param aggregate_name: The aggregate_name of this OptionalFromSnapshot.
        :type: str
        """
        if aggregate_name is not None and len(aggregate_name) < 1:
            raise ValueError("Invalid value for `aggregate_name`, length must be greater than or equal to `1`")

        self._aggregate_name = aggregate_name

    @property
    def junction_path(self):
        """
        Gets the junction_path of this OptionalFromSnapshot.

        :return: The junction_path of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._junction_path

    @junction_path.setter
    def junction_path(self, junction_path):
        """
        Sets the junction_path of this OptionalFromSnapshot.

        :param junction_path: The junction_path of this OptionalFromSnapshot.
        :type: str
        """
        if junction_path is not None and len(junction_path) < 1:
            raise ValueError("Invalid value for `junction_path`, length must be greater than or equal to `1`")

        self._junction_path = junction_path

    @property
    def from_snapshot(self):
        """
        Gets the from_snapshot of this OptionalFromSnapshot.
        The snapshot name to create from/restore

        :return: The from_snapshot of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._from_snapshot

    @from_snapshot.setter
    def from_snapshot(self, from_snapshot):
        """
        Sets the from_snapshot of this OptionalFromSnapshot.
        The snapshot name to create from/restore

        :param from_snapshot: The from_snapshot of this OptionalFromSnapshot.
        :type: str
        """

        self._from_snapshot = from_snapshot

    @property
    def from_volume(self):
        """
        Gets the from_volume of this OptionalFromSnapshot.
        When cloning a volume, use this volume as basis for the snapshot to start from

        :return: The from_volume of this OptionalFromSnapshot.
        :rtype: str
        """
        return self._from_volume

    @from_volume.setter
    def from_volume(self, from_volume):
        """
        Sets the from_volume of this OptionalFromSnapshot.
        When cloning a volume, use this volume as basis for the snapshot to start from

        :param from_volume: The from_volume of this OptionalFromSnapshot.
        :type: str
        """

        self._from_volume = from_volume

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, OptionalFromSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
