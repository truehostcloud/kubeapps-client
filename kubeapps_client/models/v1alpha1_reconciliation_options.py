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

class V1alpha1ReconciliationOptions(object):
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
        'interval': 'str',
        'suspend': 'bool',
        'service_account_name': 'str'
    }

    attribute_map = {
        'interval': 'interval',
        'suspend': 'suspend',
        'service_account_name': 'serviceAccountName'
    }

    def __init__(self, interval=None, suspend=None, service_account_name=None):  # noqa: E501
        """V1alpha1ReconciliationOptions - a model defined in Swagger"""  # noqa: E501
        self._interval = None
        self._suspend = None
        self._service_account_name = None
        self.discriminator = None
        if interval is not None:
            self.interval = interval
        if suspend is not None:
            self.suspend = suspend
        if service_account_name is not None:
            self.service_account_name = service_account_name

    @property
    def interval(self):
        """Gets the interval of this V1alpha1ReconciliationOptions.  # noqa: E501

        The interval with which the package is checked for reconciliation (in time+unit)  # noqa: E501

        :return: The interval of this V1alpha1ReconciliationOptions.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this V1alpha1ReconciliationOptions.

        The interval with which the package is checked for reconciliation (in time+unit)  # noqa: E501

        :param interval: The interval of this V1alpha1ReconciliationOptions.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def suspend(self):
        """Gets the suspend of this V1alpha1ReconciliationOptions.  # noqa: E501

        Whether reconciliation should be suspended until otherwise enabled. This can be utilized to e.g. temporarily ignore chart changes, and prevent a Helm release from getting upgraded  # noqa: E501

        :return: The suspend of this V1alpha1ReconciliationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._suspend

    @suspend.setter
    def suspend(self, suspend):
        """Sets the suspend of this V1alpha1ReconciliationOptions.

        Whether reconciliation should be suspended until otherwise enabled. This can be utilized to e.g. temporarily ignore chart changes, and prevent a Helm release from getting upgraded  # noqa: E501

        :param suspend: The suspend of this V1alpha1ReconciliationOptions.  # noqa: E501
        :type: bool
        """

        self._suspend = suspend

    @property
    def service_account_name(self):
        """Gets the service_account_name of this V1alpha1ReconciliationOptions.  # noqa: E501

        A name for a service account in the same namespace which should be used to perform the reconciliation.  # noqa: E501

        :return: The service_account_name of this V1alpha1ReconciliationOptions.  # noqa: E501
        :rtype: str
        """
        return self._service_account_name

    @service_account_name.setter
    def service_account_name(self, service_account_name):
        """Sets the service_account_name of this V1alpha1ReconciliationOptions.

        A name for a service account in the same namespace which should be used to perform the reconciliation.  # noqa: E501

        :param service_account_name: The service_account_name of this V1alpha1ReconciliationOptions.  # noqa: E501
        :type: str
        """

        self._service_account_name = service_account_name

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
        if issubclass(V1alpha1ReconciliationOptions, dict):
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
        if not isinstance(other, V1alpha1ReconciliationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
