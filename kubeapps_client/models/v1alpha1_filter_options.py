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

class V1alpha1FilterOptions(object):
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
        'query': 'str',
        'categories': 'list[str]',
        'repositories': 'list[str]',
        'pkg_version': 'str',
        'app_version': 'str'
    }

    attribute_map = {
        'query': 'query',
        'categories': 'categories',
        'repositories': 'repositories',
        'pkg_version': 'pkgVersion',
        'app_version': 'appVersion'
    }

    def __init__(self, query=None, categories=None, repositories=None, pkg_version=None, app_version=None):  # noqa: E501
        """V1alpha1FilterOptions - a model defined in Swagger"""  # noqa: E501
        self._query = None
        self._categories = None
        self._repositories = None
        self._pkg_version = None
        self._app_version = None
        self.discriminator = None
        if query is not None:
            self.query = query
        if categories is not None:
            self.categories = categories
        if repositories is not None:
            self.repositories = repositories
        if pkg_version is not None:
            self.pkg_version = pkg_version
        if app_version is not None:
            self.app_version = app_version

    @property
    def query(self):
        """Gets the query of this V1alpha1FilterOptions.  # noqa: E501

        Text query for the request  # noqa: E501

        :return: The query of this V1alpha1FilterOptions.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this V1alpha1FilterOptions.

        Text query for the request  # noqa: E501

        :param query: The query of this V1alpha1FilterOptions.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def categories(self):
        """Gets the categories of this V1alpha1FilterOptions.  # noqa: E501

        Collection of categories for the request  # noqa: E501

        :return: The categories of this V1alpha1FilterOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1alpha1FilterOptions.

        Collection of categories for the request  # noqa: E501

        :param categories: The categories of this V1alpha1FilterOptions.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def repositories(self):
        """Gets the repositories of this V1alpha1FilterOptions.  # noqa: E501

        Collection of repositories where the packages belong to  # noqa: E501

        :return: The repositories of this V1alpha1FilterOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this V1alpha1FilterOptions.

        Collection of repositories where the packages belong to  # noqa: E501

        :param repositories: The repositories of this V1alpha1FilterOptions.  # noqa: E501
        :type: list[str]
        """

        self._repositories = repositories

    @property
    def pkg_version(self):
        """Gets the pkg_version of this V1alpha1FilterOptions.  # noqa: E501

        Package version for the request  # noqa: E501

        :return: The pkg_version of this V1alpha1FilterOptions.  # noqa: E501
        :rtype: str
        """
        return self._pkg_version

    @pkg_version.setter
    def pkg_version(self, pkg_version):
        """Sets the pkg_version of this V1alpha1FilterOptions.

        Package version for the request  # noqa: E501

        :param pkg_version: The pkg_version of this V1alpha1FilterOptions.  # noqa: E501
        :type: str
        """

        self._pkg_version = pkg_version

    @property
    def app_version(self):
        """Gets the app_version of this V1alpha1FilterOptions.  # noqa: E501

        Packaged app version for the request  # noqa: E501

        :return: The app_version of this V1alpha1FilterOptions.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this V1alpha1FilterOptions.

        Packaged app version for the request  # noqa: E501

        :param app_version: The app_version of this V1alpha1FilterOptions.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

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
        if issubclass(V1alpha1FilterOptions, dict):
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
        if not isinstance(other, V1alpha1FilterOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
