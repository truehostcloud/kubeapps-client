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

class V1alpha1GetAvailablePackageSummariesResponse(object):
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
        'available_package_summaries': 'list[V1alpha1AvailablePackageSummary]',
        'next_page_token': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'available_package_summaries': 'availablePackageSummaries',
        'next_page_token': 'nextPageToken',
        'categories': 'categories'
    }

    def __init__(self, available_package_summaries=None, next_page_token=None, categories=None):  # noqa: E501
        """V1alpha1GetAvailablePackageSummariesResponse - a model defined in Swagger"""  # noqa: E501
        self._available_package_summaries = None
        self._next_page_token = None
        self._categories = None
        self.discriminator = None
        if available_package_summaries is not None:
            self.available_package_summaries = available_package_summaries
        if next_page_token is not None:
            self.next_page_token = next_page_token
        if categories is not None:
            self.categories = categories

    @property
    def available_package_summaries(self):
        """Gets the available_package_summaries of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501

        List of AvailablePackageSummary  # noqa: E501

        :return: The available_package_summaries of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
        :rtype: list[V1alpha1AvailablePackageSummary]
        """
        return self._available_package_summaries

    @available_package_summaries.setter
    def available_package_summaries(self, available_package_summaries):
        """Sets the available_package_summaries of this V1alpha1GetAvailablePackageSummariesResponse.

        List of AvailablePackageSummary  # noqa: E501

        :param available_package_summaries: The available_package_summaries of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
        :type: list[V1alpha1AvailablePackageSummary]
        """

        self._available_package_summaries = available_package_summaries

    @property
    def next_page_token(self):
        """Gets the next_page_token of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501

        This field represents the pagination token to retrieve the next page of results. If the value is \"\", it means no further results for the request.  # noqa: E501

        :return: The next_page_token of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
        :rtype: str
        """
        return self._next_page_token

    @next_page_token.setter
    def next_page_token(self, next_page_token):
        """Sets the next_page_token of this V1alpha1GetAvailablePackageSummariesResponse.

        This field represents the pagination token to retrieve the next page of results. If the value is \"\", it means no further results for the request.  # noqa: E501

        :param next_page_token: The next_page_token of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
        :type: str
        """

        self._next_page_token = next_page_token

    @property
    def categories(self):
        """Gets the categories of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501

        This optional field contains the distinct category names considering the FilterOptions.  # noqa: E501

        :return: The categories of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this V1alpha1GetAvailablePackageSummariesResponse.

        This optional field contains the distinct category names considering the FilterOptions.  # noqa: E501

        :param categories: The categories of this V1alpha1GetAvailablePackageSummariesResponse.  # noqa: E501
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
        if issubclass(V1alpha1GetAvailablePackageSummariesResponse, dict):
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
        if not isinstance(other, V1alpha1GetAvailablePackageSummariesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
