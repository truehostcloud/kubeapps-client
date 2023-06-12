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

class V1alpha1AvailablePackageSummary(object):
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
        'available_package_ref': 'V1alpha1AvailablePackageReference',
        'name': 'str',
        'latest_version': 'V1alpha1PackageAppVersion',
        'icon_url': 'str',
        'display_name': 'str',
        'short_description': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'available_package_ref': 'availablePackageRef',
        'name': 'name',
        'latest_version': 'latestVersion',
        'icon_url': 'iconUrl',
        'display_name': 'displayName',
        'short_description': 'shortDescription',
        'categories': 'categories'
    }

    def __init__(self, available_package_ref=None, name=None, latest_version=None, icon_url=None, display_name=None, short_description=None, categories=None):  # noqa: E501
        """V1alpha1AvailablePackageSummary - a model defined in Swagger"""  # noqa: E501
        self._available_package_ref = None
        self._name = None
        self._latest_version = None
        self._icon_url = None
        self._display_name = None
        self._short_description = None
        self._categories = None
        self.discriminator = None
        if available_package_ref is not None:
            self.available_package_ref = available_package_ref
        if name is not None:
            self.name = name
        if latest_version is not None:
            self.latest_version = latest_version
        if icon_url is not None:
            self.icon_url = icon_url
        if display_name is not None:
            self.display_name = display_name
        if short_description is not None:
            self.short_description = short_description
        if categories is not None:
            self.categories = categories

    @property
    def available_package_ref(self):
        """Gets the available_package_ref of this V1alpha1AvailablePackageSummary.  # noqa: E501


        :return: The available_package_ref of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: V1alpha1AvailablePackageReference
        """
        return self._available_package_ref

    @available_package_ref.setter
    def available_package_ref(self, available_package_ref):
        """Sets the available_package_ref of this V1alpha1AvailablePackageSummary.


        :param available_package_ref: The available_package_ref of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: V1alpha1AvailablePackageReference
        """

        self._available_package_ref = available_package_ref

    @property
    def name(self):
        """Gets the name of this V1alpha1AvailablePackageSummary.  # noqa: E501

        The name of the available package  # noqa: E501

        :return: The name of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1AvailablePackageSummary.

        The name of the available package  # noqa: E501

        :param name: The name of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def latest_version(self):
        """Gets the latest_version of this V1alpha1AvailablePackageSummary.  # noqa: E501


        :return: The latest_version of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this V1alpha1AvailablePackageSummary.


        :param latest_version: The latest_version of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._latest_version = latest_version

    @property
    def icon_url(self):
        """Gets the icon_url of this V1alpha1AvailablePackageSummary.  # noqa: E501

        A url for an icon.  # noqa: E501

        :return: The icon_url of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this V1alpha1AvailablePackageSummary.

        A url for an icon.  # noqa: E501

        :param icon_url: The icon_url of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def display_name(self):
        """Gets the display_name of this V1alpha1AvailablePackageSummary.  # noqa: E501

        A name as displayed to users  # noqa: E501

        :return: The display_name of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this V1alpha1AvailablePackageSummary.

        A name as displayed to users  # noqa: E501

        :param display_name: The display_name of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def short_description(self):
        """Gets the short_description of this V1alpha1AvailablePackageSummary.  # noqa: E501

        A short description of the app provided by the package  # noqa: E501

        :return: The short_description of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this V1alpha1AvailablePackageSummary.

        A short description of the app provided by the package  # noqa: E501

        :param short_description: The short_description of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def categories(self):
        """Gets the categories of this V1alpha1AvailablePackageSummary.  # noqa: E501

        A user-facing list of category names useful for creating richer user interfaces. Plugins can choose not to implement this  # noqa: E501

        :return: The categories of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1alpha1AvailablePackageSummary.

        A user-facing list of category names useful for creating richer user interfaces. Plugins can choose not to implement this  # noqa: E501

        :param categories: The categories of this V1alpha1AvailablePackageSummary.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

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
        if issubclass(V1alpha1AvailablePackageSummary, dict):
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
        if not isinstance(other, V1alpha1AvailablePackageSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other