# coding: utf-8

"""
    Kubeapps API

    [![CircleCI](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main.svg?style=svg)](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main)   [Kubeapps](https://github.com/vmware-tanzu/kubeapps) is a web-based UI for deploying and managing applications in Kubernetes clusters.   Note: this API documentation is still in an initial stage and is subject to change. Before coupling to it, please [drop us an issue](https://github.com/vmware-tanzu/kubeapps/issues/new/choose) or reach us [via Slack](https://kubernetes.slack.com/messages/kubeapps) to know more about your use case and see how we can assist you.  #### Developer Documentation  - The [Kubeapps Architecture Overview](https://kubeapps.dev/docs/latest/background/architecture/).  - The [Kubeapps Developer Documentation](https://kubeapps.dev/docs/latest/reference/developer/) for instructions on setting up the developer environment for developing on Kubeapps and its components.  - The [Kubeapps Build Guide](https://kubeapps.dev/docs/latest/reference/developer/build/) for instructions on setting up the build environment and building Kubeapps from source.   # noqa: E501

    OpenAPI spec version: 0.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.kapp_controller_packages_service_api import KappControllerPackagesServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestKappControllerPackagesServiceApi(unittest.TestCase):
    """KappControllerPackagesServiceApi unit test stubs"""

    def setUp(self):
        self.api = KappControllerPackagesServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_kapp_controller_packages_service_create_installed_package(self):
        """Test case for kapp_controller_packages_service_create_installed_package

        CreateInstalledPackage creates an installed package based on the request.  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_delete_installed_package(self):
        """Test case for kapp_controller_packages_service_delete_installed_package

        DeleteInstalledPackage deletes an installed package based on the request.  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_available_package_detail(self):
        """Test case for kapp_controller_packages_service_get_available_package_detail

        GetAvailablePackageDetail returns the package details managed by the 'kapp_controller' plugin  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_available_package_summaries(self):
        """Test case for kapp_controller_packages_service_get_available_package_summaries

        GetAvailablePackageSummaries returns the available packages managed by the 'kapp_controller' plugin  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_available_package_versions(self):
        """Test case for kapp_controller_packages_service_get_available_package_versions

        GetAvailablePackageVersions returns the package versions managed by the 'kapp_controller' plugin  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_installed_package_detail(self):
        """Test case for kapp_controller_packages_service_get_installed_package_detail

        GetInstalledPackageDetail returns the requested installed package managed by the 'kapp_controller' plugin  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_installed_package_resource_refs(self):
        """Test case for kapp_controller_packages_service_get_installed_package_resource_refs

        GetInstalledPackageResourceRefs returns the references for the Kubernetes resources created by an installed package.  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_get_installed_package_summaries(self):
        """Test case for kapp_controller_packages_service_get_installed_package_summaries

        GetInstalledPackageSummaries returns the installed packages managed by the 'kapp_controller' plugin  # noqa: E501
        """
        pass

    def test_kapp_controller_packages_service_update_installed_package(self):
        """Test case for kapp_controller_packages_service_update_installed_package

        UpdateInstalledPackage updates an installed package based on the request.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
