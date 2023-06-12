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

class V1alpha1InstalledPackageDetail(object):
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
        'pkg_version_reference': 'V1alpha1VersionReference',
        'name': 'str',
        'current_version': 'V1alpha1PackageAppVersion',
        'values_applied': 'str',
        'reconciliation_options': 'V1alpha1ReconciliationOptions',
        'status': 'V1alpha1InstalledPackageStatus',
        'post_installation_notes': 'str',
        'available_package_ref': 'V1alpha1AvailablePackageReference',
        'latest_matching_version': 'V1alpha1PackageAppVersion',
        'latest_version': 'V1alpha1PackageAppVersion',
        'custom_detail': 'ProtobufAny'
    }

    attribute_map = {
        'installed_package_ref': 'installedPackageRef',
        'pkg_version_reference': 'pkgVersionReference',
        'name': 'name',
        'current_version': 'currentVersion',
        'values_applied': 'valuesApplied',
        'reconciliation_options': 'reconciliationOptions',
        'status': 'status',
        'post_installation_notes': 'postInstallationNotes',
        'available_package_ref': 'availablePackageRef',
        'latest_matching_version': 'latestMatchingVersion',
        'latest_version': 'latestVersion',
        'custom_detail': 'customDetail'
    }

    def __init__(self, installed_package_ref=None, pkg_version_reference=None, name=None, current_version=None, values_applied=None, reconciliation_options=None, status=None, post_installation_notes=None, available_package_ref=None, latest_matching_version=None, latest_version=None, custom_detail=None):  # noqa: E501
        """V1alpha1InstalledPackageDetail - a model defined in Swagger"""  # noqa: E501
        self._installed_package_ref = None
        self._pkg_version_reference = None
        self._name = None
        self._current_version = None
        self._values_applied = None
        self._reconciliation_options = None
        self._status = None
        self._post_installation_notes = None
        self._available_package_ref = None
        self._latest_matching_version = None
        self._latest_version = None
        self._custom_detail = None
        self.discriminator = None
        if installed_package_ref is not None:
            self.installed_package_ref = installed_package_ref
        if pkg_version_reference is not None:
            self.pkg_version_reference = pkg_version_reference
        if name is not None:
            self.name = name
        if current_version is not None:
            self.current_version = current_version
        if values_applied is not None:
            self.values_applied = values_applied
        if reconciliation_options is not None:
            self.reconciliation_options = reconciliation_options
        if status is not None:
            self.status = status
        if post_installation_notes is not None:
            self.post_installation_notes = post_installation_notes
        if available_package_ref is not None:
            self.available_package_ref = available_package_ref
        if latest_matching_version is not None:
            self.latest_matching_version = latest_matching_version
        if latest_version is not None:
            self.latest_version = latest_version
        if custom_detail is not None:
            self.custom_detail = custom_detail

    @property
    def installed_package_ref(self):
        """Gets the installed_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The installed_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1InstalledPackageReference
        """
        return self._installed_package_ref

    @installed_package_ref.setter
    def installed_package_ref(self, installed_package_ref):
        """Sets the installed_package_ref of this V1alpha1InstalledPackageDetail.


        :param installed_package_ref: The installed_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1InstalledPackageReference
        """

        self._installed_package_ref = installed_package_ref

    @property
    def pkg_version_reference(self):
        """Gets the pkg_version_reference of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The pkg_version_reference of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1VersionReference
        """
        return self._pkg_version_reference

    @pkg_version_reference.setter
    def pkg_version_reference(self, pkg_version_reference):
        """Sets the pkg_version_reference of this V1alpha1InstalledPackageDetail.


        :param pkg_version_reference: The pkg_version_reference of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1VersionReference
        """

        self._pkg_version_reference = pkg_version_reference

    @property
    def name(self):
        """Gets the name of this V1alpha1InstalledPackageDetail.  # noqa: E501

        The name given to the installed package  # noqa: E501

        :return: The name of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1InstalledPackageDetail.

        The name given to the installed package  # noqa: E501

        :param name: The name of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def current_version(self):
        """Gets the current_version of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The current_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        """Sets the current_version of this V1alpha1InstalledPackageDetail.


        :param current_version: The current_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._current_version = current_version

    @property
    def values_applied(self):
        """Gets the values_applied of this V1alpha1InstalledPackageDetail.  # noqa: E501

        The values applied currently for the installed package.  # noqa: E501

        :return: The values_applied of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._values_applied

    @values_applied.setter
    def values_applied(self, values_applied):
        """Sets the values_applied of this V1alpha1InstalledPackageDetail.

        The values applied currently for the installed package.  # noqa: E501

        :param values_applied: The values_applied of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: str
        """

        self._values_applied = values_applied

    @property
    def reconciliation_options(self):
        """Gets the reconciliation_options of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The reconciliation_options of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1ReconciliationOptions
        """
        return self._reconciliation_options

    @reconciliation_options.setter
    def reconciliation_options(self, reconciliation_options):
        """Sets the reconciliation_options of this V1alpha1InstalledPackageDetail.


        :param reconciliation_options: The reconciliation_options of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1ReconciliationOptions
        """

        self._reconciliation_options = reconciliation_options

    @property
    def status(self):
        """Gets the status of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The status of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1InstalledPackageStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1alpha1InstalledPackageDetail.


        :param status: The status of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1InstalledPackageStatus
        """

        self._status = status

    @property
    def post_installation_notes(self):
        """Gets the post_installation_notes of this V1alpha1InstalledPackageDetail.  # noqa: E501

        Optional notes generated by package and intended for the user post installation.  # noqa: E501

        :return: The post_installation_notes of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._post_installation_notes

    @post_installation_notes.setter
    def post_installation_notes(self, post_installation_notes):
        """Sets the post_installation_notes of this V1alpha1InstalledPackageDetail.

        Optional notes generated by package and intended for the user post installation.  # noqa: E501

        :param post_installation_notes: The post_installation_notes of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: str
        """

        self._post_installation_notes = post_installation_notes

    @property
    def available_package_ref(self):
        """Gets the available_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The available_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1AvailablePackageReference
        """
        return self._available_package_ref

    @available_package_ref.setter
    def available_package_ref(self, available_package_ref):
        """Sets the available_package_ref of this V1alpha1InstalledPackageDetail.


        :param available_package_ref: The available_package_ref of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1AvailablePackageReference
        """

        self._available_package_ref = available_package_ref

    @property
    def latest_matching_version(self):
        """Gets the latest_matching_version of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The latest_matching_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._latest_matching_version

    @latest_matching_version.setter
    def latest_matching_version(self, latest_matching_version):
        """Sets the latest_matching_version of this V1alpha1InstalledPackageDetail.


        :param latest_matching_version: The latest_matching_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._latest_matching_version = latest_matching_version

    @property
    def latest_version(self):
        """Gets the latest_version of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The latest_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        """Sets the latest_version of this V1alpha1InstalledPackageDetail.


        :param latest_version: The latest_version of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._latest_version = latest_version

    @property
    def custom_detail(self):
        """Gets the custom_detail of this V1alpha1InstalledPackageDetail.  # noqa: E501


        :return: The custom_detail of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :rtype: ProtobufAny
        """
        return self._custom_detail

    @custom_detail.setter
    def custom_detail(self, custom_detail):
        """Sets the custom_detail of this V1alpha1InstalledPackageDetail.


        :param custom_detail: The custom_detail of this V1alpha1InstalledPackageDetail.  # noqa: E501
        :type: ProtobufAny
        """

        self._custom_detail = custom_detail

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
        if issubclass(V1alpha1InstalledPackageDetail, dict):
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
        if not isinstance(other, V1alpha1InstalledPackageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other