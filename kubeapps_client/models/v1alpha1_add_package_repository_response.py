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

class V1alpha1AddPackageRepositoryResponse(object):
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
        'package_repo_ref': 'V1alpha1PackageRepositoryReference'
    }

    attribute_map = {
        'package_repo_ref': 'packageRepoRef'
    }

    def __init__(self, package_repo_ref=None):  # noqa: E501
        """V1alpha1AddPackageRepositoryResponse - a model defined in Swagger"""  # noqa: E501
        self._package_repo_ref = None
        self.discriminator = None
        if package_repo_ref is not None:
            self.package_repo_ref = package_repo_ref

    @property
    def package_repo_ref(self):
        """Gets the package_repo_ref of this V1alpha1AddPackageRepositoryResponse.  # noqa: E501


        :return: The package_repo_ref of this V1alpha1AddPackageRepositoryResponse.  # noqa: E501
        :rtype: V1alpha1PackageRepositoryReference
        """
        return self._package_repo_ref

    @package_repo_ref.setter
    def package_repo_ref(self, package_repo_ref):
        """Sets the package_repo_ref of this V1alpha1AddPackageRepositoryResponse.


        :param package_repo_ref: The package_repo_ref of this V1alpha1AddPackageRepositoryResponse.  # noqa: E501
        :type: V1alpha1PackageRepositoryReference
        """

        self._package_repo_ref = package_repo_ref

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
        if issubclass(V1alpha1AddPackageRepositoryResponse, dict):
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
        if not isinstance(other, V1alpha1AddPackageRepositoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
