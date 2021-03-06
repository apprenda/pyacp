# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in version 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from .add_on import AddOn
from .add_on_creation_request import AddOnCreationRequest
from .application import Application
from .apprenda_file_system_file_system_uri import ApprendaFileSystemFileSystemUri
from .apprenda_rest_api_common_resources_paged_resource_base_application import ApprendaRestAPICommonResourcesPagedResourceBaseApplication
from .apprenda_rest_api_common_resources_paged_resource_base_version import ApprendaRestAPICommonResourcesPagedResourceBaseVersion
from .apprenda_rest_api_common_resources_resource_base import ApprendaRestAPICommonResourcesResourceBase
from .apprenda_soc_web_rest_api_resources_bootstrap_policy import ApprendaSOCWebRestAPIResourcesBootstrapPolicy
from .apprenda_utility_rest_api_common_resources_resource_base import ApprendaUtilityRestAPICommonResourcesResourceBase
from .audit_record import AuditRecord
from .cloud import Cloud
from .cluster import Cluster
from .cluster_report_card import ClusterReportCard
from .cluster_report_card_group import ClusterReportCardGroup
from .cluster_report_card_message import ClusterReportCardMessage
from .cluster_report_card_section import ClusterReportCardSection
from .component import Component
from .custom_property import CustomProperty
from .custom_property_applicability_option import CustomPropertyApplicabilityOption
from .custom_property_applicability_option_collection import CustomPropertyApplicabilityOptionCollection
from .custom_property_application_component_options import CustomPropertyApplicationComponentOptions
from .custom_property_application_options import CustomPropertyApplicationOptions
from .custom_property_developer_options import CustomPropertyDeveloperOptions
from .custom_property_update import CustomPropertyUpdate
from .custom_property_value import CustomPropertyValue
from .custom_property_value_options import CustomPropertyValueOptions
from .deployment_policy import DeploymentPolicy
from .encryption_request import EncryptionRequest
from .encryption_result import EncryptionResult
from .inline_response_200 import InlineResponse200
from .inline_response_200_1 import InlineResponse2001
from .inline_response_400 import InlineResponse400
from .node import Node
from .node_profile import NodeProfile
from .node_state import NodeState
from .paged_resource_base_audit_record import PagedResourceBaseAuditRecord
from .paged_resource_base_custom_property import PagedResourceBaseCustomProperty
from .paged_resource_base_node import PagedResourceBaseNode
from .paged_resource_base_registry_setting import PagedResourceBaseRegistrySetting
from .platform_database import PlatformDatabase
from .registry_setting import RegistrySetting
from .resource_allocation_report import ResourceAllocationReport
from .unpaged_resource_base_add_on import UnpagedResourceBaseAddOn
from .unpaged_resource_base_bootstrap_policy import UnpagedResourceBaseBootstrapPolicy
from .unpaged_resource_base_cloud import UnpagedResourceBaseCloud
from .unpaged_resource_base_cluster import UnpagedResourceBaseCluster
from .unpaged_resource_base_component import UnpagedResourceBaseComponent
from .unpaged_resource_base_custom_property_value import UnpagedResourceBaseCustomPropertyValue
from .unpaged_resource_base_deployment_policy import UnpagedResourceBaseDeploymentPolicy
from .unpaged_resource_base_platform_database import UnpagedResourceBasePlatformDatabase
from .unpaged_resource_base_workload import UnpagedResourceBaseWorkload
from .version import Version
from .visibility_options import VisibilityOptions
from .workload import Workload
from .workload_deployment_request import WorkloadDeploymentRequest
