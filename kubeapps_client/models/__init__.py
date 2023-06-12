# coding: utf-8

# flake8: noqa
"""
    Kubeapps API

    [![CircleCI](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main.svg?style=svg)](https://circleci.com/gh/vmware-tanzu/kubeapps/tree/main)   [Kubeapps](https://github.com/vmware-tanzu/kubeapps) is a web-based UI for deploying and managing applications in Kubernetes clusters.   Note: this API documentation is still in an initial stage and is subject to change. Before coupling to it, please [drop us an issue](https://github.com/vmware-tanzu/kubeapps/issues/new/choose) or reach us [via Slack](https://kubernetes.slack.com/messages/kubeapps) to know more about your use case and see how we can assist you.  #### Developer Documentation  - The [Kubeapps Architecture Overview](https://kubeapps.dev/docs/latest/background/architecture/).  - The [Kubeapps Developer Documentation](https://kubeapps.dev/docs/latest/reference/developer/) for instructions on setting up the developer environment for developing on Kubeapps and its components.  - The [Kubeapps Build Guide](https://kubeapps.dev/docs/latest/reference/developer/build/) for instructions on setting up the build environment and building Kubeapps from source.   # noqa: E501

    OpenAPI spec version: 0.1.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from kubeapps_client.models.a_reference_uniquely_identifying_the_installed_package_being_updated_required import AReferenceUniquelyIdentifyingTheInstalledPackageBeingUpdatedRequired
from kubeapps_client.models.a_reference_uniquely_identifying_the_package_repository_being_updated_the_only_required_field import AReferenceUniquelyIdentifyingThePackageRepositoryBeingUpdatedTheOnlyRequiredField
from kubeapps_client.models.installed_package_ref_identifier_rollback_body import InstalledPackageRefIdentifierRollbackBody
from kubeapps_client.models.installed_package_reference import InstalledPackageReference
from kubeapps_client.models.package_repository_auth_package_repository_auth_type import PackageRepositoryAuthPackageRepositoryAuthType
from kubeapps_client.models.protobuf_any import ProtobufAny
from kubeapps_client.models.rpc_status import RpcStatus
from kubeapps_client.models.stream_result_of_v1alpha1_get_resources_response import StreamResultOfV1alpha1GetResourcesResponse
from kubeapps_client.models.update_installed_package_request import UpdateInstalledPackageRequest
from kubeapps_client.models.update_package_repository_request import UpdatePackageRepositoryRequest
from kubeapps_client.models.v1alpha1_add_package_repository_request import V1alpha1AddPackageRepositoryRequest
from kubeapps_client.models.v1alpha1_add_package_repository_response import V1alpha1AddPackageRepositoryResponse
from kubeapps_client.models.v1alpha1_available_package_detail import V1alpha1AvailablePackageDetail
from kubeapps_client.models.v1alpha1_available_package_reference import V1alpha1AvailablePackageReference
from kubeapps_client.models.v1alpha1_available_package_summary import V1alpha1AvailablePackageSummary
from kubeapps_client.models.v1alpha1_can_i_response import V1alpha1CanIResponse
from kubeapps_client.models.v1alpha1_check_namespace_exists_response import V1alpha1CheckNamespaceExistsResponse
from kubeapps_client.models.v1alpha1_context import V1alpha1Context
from kubeapps_client.models.v1alpha1_create_installed_package_request import V1alpha1CreateInstalledPackageRequest
from kubeapps_client.models.v1alpha1_create_installed_package_response import V1alpha1CreateInstalledPackageResponse
from kubeapps_client.models.v1alpha1_create_namespace_response import V1alpha1CreateNamespaceResponse
from kubeapps_client.models.v1alpha1_create_secret_response import V1alpha1CreateSecretResponse
from kubeapps_client.models.v1alpha1_delete_installed_package_response import V1alpha1DeleteInstalledPackageResponse
from kubeapps_client.models.v1alpha1_delete_package_repository_response import V1alpha1DeletePackageRepositoryResponse
from kubeapps_client.models.v1alpha1_docker_credentials import V1alpha1DockerCredentials
from kubeapps_client.models.v1alpha1_filter_options import V1alpha1FilterOptions
from kubeapps_client.models.v1alpha1_get_available_package_detail_response import V1alpha1GetAvailablePackageDetailResponse
from kubeapps_client.models.v1alpha1_get_available_package_summaries_response import V1alpha1GetAvailablePackageSummariesResponse
from kubeapps_client.models.v1alpha1_get_available_package_versions_response import V1alpha1GetAvailablePackageVersionsResponse
from kubeapps_client.models.v1alpha1_get_configured_plugins_response import V1alpha1GetConfiguredPluginsResponse
from kubeapps_client.models.v1alpha1_get_installed_package_detail_response import V1alpha1GetInstalledPackageDetailResponse
from kubeapps_client.models.v1alpha1_get_installed_package_resource_refs_response import V1alpha1GetInstalledPackageResourceRefsResponse
from kubeapps_client.models.v1alpha1_get_installed_package_summaries_response import V1alpha1GetInstalledPackageSummariesResponse
from kubeapps_client.models.v1alpha1_get_namespace_names_response import V1alpha1GetNamespaceNamesResponse
from kubeapps_client.models.v1alpha1_get_package_repository_detail_response import V1alpha1GetPackageRepositoryDetailResponse
from kubeapps_client.models.v1alpha1_get_package_repository_permissions_response import V1alpha1GetPackageRepositoryPermissionsResponse
from kubeapps_client.models.v1alpha1_get_package_repository_summaries_response import V1alpha1GetPackageRepositorySummariesResponse
from kubeapps_client.models.v1alpha1_get_resources_response import V1alpha1GetResourcesResponse
from kubeapps_client.models.v1alpha1_get_secret_names_response import V1alpha1GetSecretNamesResponse
from kubeapps_client.models.v1alpha1_get_service_account_names_response import V1alpha1GetServiceAccountNamesResponse
from kubeapps_client.models.v1alpha1_installed_package_detail import V1alpha1InstalledPackageDetail
from kubeapps_client.models.v1alpha1_installed_package_reference import V1alpha1InstalledPackageReference
from kubeapps_client.models.v1alpha1_installed_package_status import V1alpha1InstalledPackageStatus
from kubeapps_client.models.v1alpha1_installed_package_status_status_reason import V1alpha1InstalledPackageStatusStatusReason
from kubeapps_client.models.v1alpha1_installed_package_summary import V1alpha1InstalledPackageSummary
from kubeapps_client.models.v1alpha1_maintainer import V1alpha1Maintainer
from kubeapps_client.models.v1alpha1_opaque_credentials import V1alpha1OpaqueCredentials
from kubeapps_client.models.v1alpha1_package_app_version import V1alpha1PackageAppVersion
from kubeapps_client.models.v1alpha1_package_repositories_permissions import V1alpha1PackageRepositoriesPermissions
from kubeapps_client.models.v1alpha1_package_repository_auth import V1alpha1PackageRepositoryAuth
from kubeapps_client.models.v1alpha1_package_repository_detail import V1alpha1PackageRepositoryDetail
from kubeapps_client.models.v1alpha1_package_repository_reference import V1alpha1PackageRepositoryReference
from kubeapps_client.models.v1alpha1_package_repository_status import V1alpha1PackageRepositoryStatus
from kubeapps_client.models.v1alpha1_package_repository_status_status_reason import V1alpha1PackageRepositoryStatusStatusReason
from kubeapps_client.models.v1alpha1_package_repository_summary import V1alpha1PackageRepositorySummary
from kubeapps_client.models.v1alpha1_package_repository_tls_config import V1alpha1PackageRepositoryTlsConfig
from kubeapps_client.models.v1alpha1_pagination_options import V1alpha1PaginationOptions
from kubeapps_client.models.v1alpha1_plugin import V1alpha1Plugin
from kubeapps_client.models.v1alpha1_reconciliation_options import V1alpha1ReconciliationOptions
from kubeapps_client.models.v1alpha1_resource_ref import V1alpha1ResourceRef
from kubeapps_client.models.v1alpha1_rollback_installed_package_response import V1alpha1RollbackInstalledPackageResponse
from kubeapps_client.models.v1alpha1_secret_key_reference import V1alpha1SecretKeyReference
from kubeapps_client.models.v1alpha1_secret_type import V1alpha1SecretType
from kubeapps_client.models.v1alpha1_ssh_credentials import V1alpha1SshCredentials
from kubeapps_client.models.v1alpha1_tls_cert_key import V1alpha1TlsCertKey
from kubeapps_client.models.v1alpha1_update_installed_package_response import V1alpha1UpdateInstalledPackageResponse
from kubeapps_client.models.v1alpha1_update_package_repository_response import V1alpha1UpdatePackageRepositoryResponse
from kubeapps_client.models.v1alpha1_username_password import V1alpha1UsernamePassword
from kubeapps_client.models.v1alpha1_version_reference import V1alpha1VersionReference
