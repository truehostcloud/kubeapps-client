# coding: utf-8

"""
    Kubeapps API

    [![CircleCI](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main.svg?style=svg)](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main)   [Kubeapps](https://github.com/vmware-tanzu/kubeapps) is a web-based UI for deploying and managing applications in Kubernetes clusters.   Note: this API documentation is still in an initial stage and is subject to change. Before coupling to it, please [drop us an issue](https://github.com/vmware-tanzu/kubeapps/issues/new/choose) or reach us [via Slack](https://kubernetes.slack.com/messages/kubeapps) to know more about your use case and see how we can assist you.  #### Developer Documentation  - The [Kubeapps Architecture Overview](https://kubeapps.dev/docs/latest/background/architecture/).  - The [Kubeapps Developer Documentation](https://kubeapps.dev/docs/latest/reference/developer/) for instructions on setting up the developer environment for developing on Kubeapps and its components.  - The [Kubeapps Build Guide](https://kubeapps.dev/docs/latest/reference/developer/build/) for instructions on setting up the build environment and building Kubeapps from source.   # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V1alpha1PackageRepositoryStatus(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ready': 'bool',
        'reason': 'V1alpha1PackageRepositoryStatusStatusReason',
        'user_reason': 'str'
    }

    attribute_map = {
        'ready': 'ready',
        'reason': 'reason',
        'user_reason': 'userReason'
    }

    def __init__(self, ready=None, reason=None, user_reason=None):  # noqa: E501
        """V1alpha1PackageRepositoryStatus - a model defined in Swagger"""  # noqa: E501
        self._ready = None
        self._reason = None
        self._user_reason = None
        self.discriminator = None
        if ready is not None:
            self.ready = ready
        if reason is not None:
            self.reason = reason
        if user_reason is not None:
            self.user_reason = user_reason

    @property
    def ready(self):
        """Gets the ready of this V1alpha1PackageRepositoryStatus.  # noqa: E501

        An indication of whether the repository is ready or not  # noqa: E501

        :return: The ready of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this V1alpha1PackageRepositoryStatus.

        An indication of whether the repository is ready or not  # noqa: E501

        :param ready: The ready of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def reason(self):
        """Gets the reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501


        :return: The reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :rtype: V1alpha1PackageRepositoryStatusStatusReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this V1alpha1PackageRepositoryStatus.


        :param reason: The reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :type: V1alpha1PackageRepositoryStatusStatusReason
        """

        self._reason = reason

    @property
    def user_reason(self):
        """Gets the user_reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501

        Optional text to return for user context, which may be plugin specific.  # noqa: E501

        :return: The user_reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :rtype: str
        """
        return self._user_reason

    @user_reason.setter
    def user_reason(self, user_reason):
        """Sets the user_reason of this V1alpha1PackageRepositoryStatus.

        Optional text to return for user context, which may be plugin specific.  # noqa: E501

        :param user_reason: The user_reason of this V1alpha1PackageRepositoryStatus.  # noqa: E501
        :type: str
        """

        self._user_reason = user_reason

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(V1alpha1PackageRepositoryStatus, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1alpha1PackageRepositoryStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
