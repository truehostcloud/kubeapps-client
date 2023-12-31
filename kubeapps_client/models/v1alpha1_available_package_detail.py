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

class V1alpha1AvailablePackageDetail(object):
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
        'version': 'V1alpha1PackageAppVersion',
        'repo_url': 'str',
        'home_url': 'str',
        'icon_url': 'str',
        'display_name': 'str',
        'short_description': 'str',
        'long_description': 'str',
        'readme': 'str',
        'default_values': 'str',
        'additional_default_values': 'dict(str, str)',
        'values_schema': 'str',
        'source_urls': 'list[str]',
        'maintainers': 'list[V1alpha1Maintainer]',
        'categories': 'list[str]',
        'custom_detail': 'ProtobufAny'
    }

    attribute_map = {
        'available_package_ref': 'availablePackageRef',
        'name': 'name',
        'version': 'version',
        'repo_url': 'repoUrl',
        'home_url': 'homeUrl',
        'icon_url': 'iconUrl',
        'display_name': 'displayName',
        'short_description': 'shortDescription',
        'long_description': 'longDescription',
        'readme': 'readme',
        'default_values': 'defaultValues',
        'additional_default_values': 'additionalDefaultValues',
        'values_schema': 'valuesSchema',
        'source_urls': 'sourceUrls',
        'maintainers': 'maintainers',
        'categories': 'categories',
        'custom_detail': 'customDetail'
    }

    def __init__(self, available_package_ref=None, name=None, version=None, repo_url=None, home_url=None, icon_url=None, display_name=None, short_description=None, long_description=None, readme=None, default_values=None, additional_default_values=None, values_schema=None, source_urls=None, maintainers=None, categories=None, custom_detail=None):  # noqa: E501
        """V1alpha1AvailablePackageDetail - a model defined in Swagger"""  # noqa: E501
        self._available_package_ref = None
        self._name = None
        self._version = None
        self._repo_url = None
        self._home_url = None
        self._icon_url = None
        self._display_name = None
        self._short_description = None
        self._long_description = None
        self._readme = None
        self._default_values = None
        self._additional_default_values = None
        self._values_schema = None
        self._source_urls = None
        self._maintainers = None
        self._categories = None
        self._custom_detail = None
        self.discriminator = None
        if available_package_ref is not None:
            self.available_package_ref = available_package_ref
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if repo_url is not None:
            self.repo_url = repo_url
        if home_url is not None:
            self.home_url = home_url
        if icon_url is not None:
            self.icon_url = icon_url
        if display_name is not None:
            self.display_name = display_name
        if short_description is not None:
            self.short_description = short_description
        if long_description is not None:
            self.long_description = long_description
        if readme is not None:
            self.readme = readme
        if default_values is not None:
            self.default_values = default_values
        if additional_default_values is not None:
            self.additional_default_values = additional_default_values
        if values_schema is not None:
            self.values_schema = values_schema
        if source_urls is not None:
            self.source_urls = source_urls
        if maintainers is not None:
            self.maintainers = maintainers
        if categories is not None:
            self.categories = categories
        if custom_detail is not None:
            self.custom_detail = custom_detail

    @property
    def available_package_ref(self):
        """Gets the available_package_ref of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The available_package_ref of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: V1alpha1AvailablePackageReference
        """
        return self._available_package_ref

    @available_package_ref.setter
    def available_package_ref(self, available_package_ref):
        """Sets the available_package_ref of this V1alpha1AvailablePackageDetail.


        :param available_package_ref: The available_package_ref of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: V1alpha1AvailablePackageReference
        """

        self._available_package_ref = available_package_ref

    @property
    def name(self):
        """Gets the name of this V1alpha1AvailablePackageDetail.  # noqa: E501

        The name of the available package  # noqa: E501

        :return: The name of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1alpha1AvailablePackageDetail.

        The name of the available package  # noqa: E501

        :param name: The name of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The version of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: V1alpha1PackageAppVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1AvailablePackageDetail.


        :param version: The version of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: V1alpha1PackageAppVersion
        """

        self._version = version

    @property
    def repo_url(self):
        """Gets the repo_url of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The repo_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this V1alpha1AvailablePackageDetail.


        :param repo_url: The repo_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._repo_url = repo_url

    @property
    def home_url(self):
        """Gets the home_url of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The home_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._home_url

    @home_url.setter
    def home_url(self, home_url):
        """Sets the home_url of this V1alpha1AvailablePackageDetail.


        :param home_url: The home_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._home_url = home_url

    @property
    def icon_url(self):
        """Gets the icon_url of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A url for an icon.  # noqa: E501

        :return: The icon_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this V1alpha1AvailablePackageDetail.

        A url for an icon.  # noqa: E501

        :param icon_url: The icon_url of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._icon_url = icon_url

    @property
    def display_name(self):
        """Gets the display_name of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A name as displayed to users  # noqa: E501

        :return: The display_name of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this V1alpha1AvailablePackageDetail.

        A name as displayed to users  # noqa: E501

        :param display_name: The display_name of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def short_description(self):
        """Gets the short_description of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A short description of the app provided by the package  # noqa: E501

        :return: The short_description of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this V1alpha1AvailablePackageDetail.

        A short description of the app provided by the package  # noqa: E501

        :param short_description: The short_description of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def long_description(self):
        """Gets the long_description of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A longer description of the package, a few sentences.  # noqa: E501

        :return: The long_description of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this V1alpha1AvailablePackageDetail.

        A longer description of the package, a few sentences.  # noqa: E501

        :param long_description: The long_description of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def readme(self):
        """Gets the readme of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A longer README with potentially pages of formatted Markdown.  # noqa: E501

        :return: The readme of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this V1alpha1AvailablePackageDetail.

        A longer README with potentially pages of formatted Markdown.  # noqa: E501

        :param readme: The readme of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._readme = readme

    @property
    def default_values(self):
        """Gets the default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501

        An example of default values used during package templating that can serve as documentation or a starting point for user customization.  # noqa: E501

        :return: The default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this V1alpha1AvailablePackageDetail.

        An example of default values used during package templating that can serve as documentation or a starting point for user customization.  # noqa: E501

        :param default_values: The default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._default_values = default_values

    @property
    def additional_default_values(self):
        """Gets the additional_default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A package may contain additional default value files for specific scenarios, such as values_production.yaml or values_dev.yaml  # noqa: E501

        :return: The additional_default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._additional_default_values

    @additional_default_values.setter
    def additional_default_values(self, additional_default_values):
        """Sets the additional_default_values of this V1alpha1AvailablePackageDetail.

        A package may contain additional default value files for specific scenarios, such as values_production.yaml or values_dev.yaml  # noqa: E501

        :param additional_default_values: The additional_default_values of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: dict(str, str)
        """

        self._additional_default_values = additional_default_values

    @property
    def values_schema(self):
        """Gets the values_schema of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The values_schema of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: str
        """
        return self._values_schema

    @values_schema.setter
    def values_schema(self, values_schema):
        """Sets the values_schema of this V1alpha1AvailablePackageDetail.


        :param values_schema: The values_schema of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: str
        """

        self._values_schema = values_schema

    @property
    def source_urls(self):
        """Gets the source_urls of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The source_urls of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_urls

    @source_urls.setter
    def source_urls(self, source_urls):
        """Sets the source_urls of this V1alpha1AvailablePackageDetail.


        :param source_urls: The source_urls of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: list[str]
        """

        self._source_urls = source_urls

    @property
    def maintainers(self):
        """Gets the maintainers of this V1alpha1AvailablePackageDetail.  # noqa: E501

        List of Maintainer  # noqa: E501

        :return: The maintainers of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: list[V1alpha1Maintainer]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this V1alpha1AvailablePackageDetail.

        List of Maintainer  # noqa: E501

        :param maintainers: The maintainers of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: list[V1alpha1Maintainer]
        """

        self._maintainers = maintainers

    @property
    def categories(self):
        """Gets the categories of this V1alpha1AvailablePackageDetail.  # noqa: E501

        A user-facing list of category names useful for creating richer user interfaces. Plugins can choose not to implement this  # noqa: E501

        :return: The categories of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1alpha1AvailablePackageDetail.

        A user-facing list of category names useful for creating richer user interfaces. Plugins can choose not to implement this  # noqa: E501

        :param categories: The categories of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def custom_detail(self):
        """Gets the custom_detail of this V1alpha1AvailablePackageDetail.  # noqa: E501


        :return: The custom_detail of this V1alpha1AvailablePackageDetail.  # noqa: E501
        :rtype: ProtobufAny
        """
        return self._custom_detail

    @custom_detail.setter
    def custom_detail(self, custom_detail):
        """Sets the custom_detail of this V1alpha1AvailablePackageDetail.


        :param custom_detail: The custom_detail of this V1alpha1AvailablePackageDetail.  # noqa: E501
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
        if issubclass(V1alpha1AvailablePackageDetail, dict):
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
        if not isinstance(other, V1alpha1AvailablePackageDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
