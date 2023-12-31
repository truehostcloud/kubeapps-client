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

class V1alpha1PackageRepositoryAuth(object):
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
        'type': 'PackageRepositoryAuthPackageRepositoryAuthType',
        'username_password': 'V1alpha1UsernamePassword',
        'tls_cert_key': 'V1alpha1TlsCertKey',
        'docker_creds': 'V1alpha1DockerCredentials',
        'header': 'str',
        'secret_ref': 'V1alpha1SecretKeyReference',
        'ssh_creds': 'V1alpha1SshCredentials',
        'opaque_creds': 'V1alpha1OpaqueCredentials',
        'pass_credentials': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'username_password': 'usernamePassword',
        'tls_cert_key': 'tlsCertKey',
        'docker_creds': 'dockerCreds',
        'header': 'header',
        'secret_ref': 'secretRef',
        'ssh_creds': 'sshCreds',
        'opaque_creds': 'opaqueCreds',
        'pass_credentials': 'passCredentials'
    }

    def __init__(self, type=None, username_password=None, tls_cert_key=None, docker_creds=None, header=None, secret_ref=None, ssh_creds=None, opaque_creds=None, pass_credentials=None):  # noqa: E501
        """V1alpha1PackageRepositoryAuth - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._username_password = None
        self._tls_cert_key = None
        self._docker_creds = None
        self._header = None
        self._secret_ref = None
        self._ssh_creds = None
        self._opaque_creds = None
        self._pass_credentials = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if username_password is not None:
            self.username_password = username_password
        if tls_cert_key is not None:
            self.tls_cert_key = tls_cert_key
        if docker_creds is not None:
            self.docker_creds = docker_creds
        if header is not None:
            self.header = header
        if secret_ref is not None:
            self.secret_ref = secret_ref
        if ssh_creds is not None:
            self.ssh_creds = ssh_creds
        if opaque_creds is not None:
            self.opaque_creds = opaque_creds
        if pass_credentials is not None:
            self.pass_credentials = pass_credentials

    @property
    def type(self):
        """Gets the type of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The type of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: PackageRepositoryAuthPackageRepositoryAuthType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1alpha1PackageRepositoryAuth.


        :param type: The type of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: PackageRepositoryAuthPackageRepositoryAuthType
        """

        self._type = type

    @property
    def username_password(self):
        """Gets the username_password of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The username_password of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1UsernamePassword
        """
        return self._username_password

    @username_password.setter
    def username_password(self, username_password):
        """Sets the username_password of this V1alpha1PackageRepositoryAuth.


        :param username_password: The username_password of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1UsernamePassword
        """

        self._username_password = username_password

    @property
    def tls_cert_key(self):
        """Gets the tls_cert_key of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The tls_cert_key of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1TlsCertKey
        """
        return self._tls_cert_key

    @tls_cert_key.setter
    def tls_cert_key(self, tls_cert_key):
        """Sets the tls_cert_key of this V1alpha1PackageRepositoryAuth.


        :param tls_cert_key: The tls_cert_key of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1TlsCertKey
        """

        self._tls_cert_key = tls_cert_key

    @property
    def docker_creds(self):
        """Gets the docker_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The docker_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1DockerCredentials
        """
        return self._docker_creds

    @docker_creds.setter
    def docker_creds(self, docker_creds):
        """Sets the docker_creds of this V1alpha1PackageRepositoryAuth.


        :param docker_creds: The docker_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1DockerCredentials
        """

        self._docker_creds = docker_creds

    @property
    def header(self):
        """Gets the header of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The header of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this V1alpha1PackageRepositoryAuth.


        :param header: The header of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def secret_ref(self):
        """Gets the secret_ref of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The secret_ref of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1SecretKeyReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """Sets the secret_ref of this V1alpha1PackageRepositoryAuth.


        :param secret_ref: The secret_ref of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1SecretKeyReference
        """

        self._secret_ref = secret_ref

    @property
    def ssh_creds(self):
        """Gets the ssh_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The ssh_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1SshCredentials
        """
        return self._ssh_creds

    @ssh_creds.setter
    def ssh_creds(self, ssh_creds):
        """Sets the ssh_creds of this V1alpha1PackageRepositoryAuth.


        :param ssh_creds: The ssh_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1SshCredentials
        """

        self._ssh_creds = ssh_creds

    @property
    def opaque_creds(self):
        """Gets the opaque_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The opaque_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: V1alpha1OpaqueCredentials
        """
        return self._opaque_creds

    @opaque_creds.setter
    def opaque_creds(self, opaque_creds):
        """Sets the opaque_creds of this V1alpha1PackageRepositoryAuth.


        :param opaque_creds: The opaque_creds of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: V1alpha1OpaqueCredentials
        """

        self._opaque_creds = opaque_creds

    @property
    def pass_credentials(self):
        """Gets the pass_credentials of this V1alpha1PackageRepositoryAuth.  # noqa: E501


        :return: The pass_credentials of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :rtype: bool
        """
        return self._pass_credentials

    @pass_credentials.setter
    def pass_credentials(self, pass_credentials):
        """Sets the pass_credentials of this V1alpha1PackageRepositoryAuth.


        :param pass_credentials: The pass_credentials of this V1alpha1PackageRepositoryAuth.  # noqa: E501
        :type: bool
        """

        self._pass_credentials = pass_credentials

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
        if issubclass(V1alpha1PackageRepositoryAuth, dict):
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
        if not isinstance(other, V1alpha1PackageRepositoryAuth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
