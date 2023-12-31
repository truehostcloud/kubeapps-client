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

class V1alpha1InstalledPackageSummary(object):
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
        'installed_package_ref': 'V1alpha1InstalledPackageReference',
        'name': 'str',
        'pkg_version_reference': 'V1alpha1VersionReference',
        'current_version': 'V1alpha1PackageAppVersion',
        'icon_url': 'str',
        'pkg_display_name': 'str',
        'short_description': 'str',
        'latest_matching_version': 'V1alpha1PackageAppVersion',
        'latest_version': 'V1alpha1PackageAppVersion',
        'status': 'V1alpha1InstalledPackageStatus'
    }

    attribute_map = {
        'installed_package_ref': 'installedPackageRef',
        'name': 'name',
        'pkg_version_reference': 'pkgVersionReference',
        'current_version': 'currentVersion',
        'icon_url': 'iconUrl',
        'pkg_display_name': 'pkgDisplayName',
        'short_description': 'shortDescription',
        'latest_matching_version': 'latestMatchingVersion',
        'latest_version': 'latestVersion',
        'status': 'status'
    }

    def __init__(self, installed_package_ref=None, name=None, pkg_version_reference=None, current_version=None, icon_url=None, pkg_display_name=None, short_description=None, latest_matching_version=None, latest_version=None, status=None):  # noqa: E501
        """V1alpha1InstalledPackageSummary - a model defined in Swagger"""  # noqa: E501
        self._installed_package_ref = None
        self._name = None
        self._pkg_version_reference = None
        self._current_version = None
        self._icon_url = None
        self._pkg_display_name = None
        self._short_description = None
        self._latest_matching_version = None
        self._latest_version = None
        self._status = None
        self.discriminator = None
        if installed_package_ref is not None:
            self.installed_package_ref = installed_package_ref
        if name is not None:
            self.name = name
        if pkg_version_reference is not None:
            self.pkg_version_reference = pkg_version_reference
        if current_version is not None:
            self.current_version = current_version
        if icon_url is not None:
            self.icon_url = icon_url
        if pkg_display_name is not None:
            self.pkg_display_name = pkg_display_name
        if short_description is not None:
            self.short_description = short_description
        if latest_matching_version is not None:
            self.latest_matching_version = latest_matching_version
        if latest_version is not None:
            self.latest_version = latest_version
        if status is not None:
            self.status = status

    @property
    def installed_package_ref(self):
        """Gets the installed_package_ref of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The installed_package_ref of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1InstalledPackageReference
        """
        return self._installed_package_ref

    @installed_package_ref.setter
    def installed_package_ref(self, installed_package_ref):
        """Sets the installed_package_ref of this V1alpha1InstalledPackageSummary.


        :param installed_package_ref: The installed_package_ref of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1InstalledPackageReference
        """

        self._installed_package_ref = installed_package_ref

    @property
    def name(self):
        """Gets the name of this V1alpha1InstalledPackageSummary.  # noqa: E501

        A name given to the installation of the package (eg. \"my-postgresql-for-testing\").  # noqa: E501

        :return: The name of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1InstalledPackageSummary.

        A name given to the installation of the package (eg. \"my-postgresql-for-testing\").  # noqa: E501

        :param name: The name of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pkg_version_reference(self):
        """Gets the pkg_version_reference of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The pkg_version_reference of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1VersionReference
        """
        return self._pkg_version_reference

    @pkg_version_reference.setter
    def pkg_version_reference(self, pkg_version_reference):
        """Sets the pkg_version_reference of this V1alpha1InstalledPackageSummary.


        :param pkg_version_reference: The pkg_version_reference of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1VersionReference
        """

        self._pkg_version_reference = pkg_version_reference

    @property
    def current_version(self):
        """Gets the current_version of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The current_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this V1alpha1InstalledPackageSummary.


        :param current_version: The current_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._current_version = current_version

    @property
    def icon_url(self):
        """Gets the icon_url of this V1alpha1InstalledPackageSummary.  # noqa: E501

        A url for an icon.  # noqa: E501

        :return: The icon_url of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this V1alpha1InstalledPackageSummary.

        A url for an icon.  # noqa: E501

        :param icon_url: The icon_url of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def pkg_display_name(self):
        """Gets the pkg_display_name of this V1alpha1InstalledPackageSummary.  # noqa: E501

        The package name as displayed to users (provided by the package, eg. \"PostgreSQL\")  # noqa: E501

        :return: The pkg_display_name of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._pkg_display_name

    @pkg_display_name.setter
    def pkg_display_name(self, pkg_display_name):
        """Sets the pkg_display_name of this V1alpha1InstalledPackageSummary.

        The package name as displayed to users (provided by the package, eg. \"PostgreSQL\")  # noqa: E501

        :param pkg_display_name: The pkg_display_name of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: str
        """

        self._pkg_display_name = pkg_display_name

    @property
    def short_description(self):
        """Gets the short_description of this V1alpha1InstalledPackageSummary.  # noqa: E501

        A short description of the package (provided by the package)  # noqa: E501

        :return: The short_description of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this V1alpha1InstalledPackageSummary.

        A short description of the package (provided by the package)  # noqa: E501

        :param short_description: The short_description of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def latest_matching_version(self):
        """Gets the latest_matching_version of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The latest_matching_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._latest_matching_version

    @latest_matching_version.setter
    def latest_matching_version(self, latest_matching_version):
        """Sets the latest_matching_version of this V1alpha1InstalledPackageSummary.


        :param latest_matching_version: The latest_matching_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._latest_matching_version = latest_matching_version

    @property
    def latest_version(self):
        """Gets the latest_version of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The latest_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this V1alpha1InstalledPackageSummary.


        :param latest_version: The latest_version of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._latest_version = latest_version

    @property
    def status(self):
        """Gets the status of this V1alpha1InstalledPackageSummary.  # noqa: E501


        :return: The status of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :rtype: V1alpha1InstalledPackageStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1InstalledPackageSummary.


        :param status: The status of this V1alpha1InstalledPackageSummary.  # noqa: E501
        :type: V1alpha1InstalledPackageStatus
        """

        self._status = status

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
        if issubclass(V1alpha1InstalledPackageSummary, dict):
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
        if not isinstance(other, V1alpha1InstalledPackageSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
