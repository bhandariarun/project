import random
from datetime import datetime, timedelta
from django.utils import timezone
from pytz import timezone as pytz_timezone

def save_log():
    logs = []
    asia_kathmandu_tz = pytz_timezone('Asia/Kathmandu')
    now = timezone.localtime(timezone.now(), timezone=asia_kathmandu_tz)

    # Example time ranges
    time_ranges = {
        'last_hour': now - timedelta(hours=1),
        'last_day': now - timedelta(days=1),
        'last_week': now - timedelta(weeks=1),
        'last_month': now - timedelta(days=30)
    }

    for _, start_time in time_ranges.items():
        for _ in range(10):  # Generate 5 logs for each time range
            # Generate a random timestamp between start_time and now
            random_seconds = random.randint(0, int((now - start_time).total_seconds()))
            log_timestamp = start_time + timedelta(seconds=random_seconds)
            awslog = [
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.logs.alerts-default-index-template] for index patterns [.internal.alerts-observability.logs.alerts-default-*]",
                	"ingestionTime": 1623324425850,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[WARN ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.uptime.alerts-default-index-template] for index patterns [.internal.alerts-observability.uptime.alerts-default-*]",
                	"ingestionTime": 1623324425889,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.slo.alerts-default-index-template] for index patterns [.internal.alerts-observability.slo.alerts-default-*]",
                	"ingestionTime": 1623324431506,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[WARN ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]",
                	"ingestionTime": 1623324435969,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection.alerts-default-*]",
                	"ingestionTime": 1623324436009,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-transform.health.alerts-default-index-template] for index patterns [.internal.alerts-transform.health.alerts-default-*]",
                	"ingestionTime": 1623324436022,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.apm.alerts-default-index-template] for index patterns [.internal.alerts-observability.apm.alerts-default-*]",
                	"ingestionTime": 1623324436038,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[ERROR ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-stack.alerts-default-index-template] for index patterns [.internal.alerts-stack.alerts-default-*]",
                	"ingestionTime": 1623324436052,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.uptime.alerts-default-index-template] for index patterns [.internal.alerts-observability.uptime.alerts-default-*]",
                	"ingestionTime": 1623324436066,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.metrics.alerts-default-index-template] for index patterns [.internal.alerts-observability.metrics.alerts-default-*]",
                	"ingestionTime": 1623324436072,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.logs.alerts-default-index-template] for index patterns [.internal.alerts-observability.logs.alerts-default-*]",
                	"ingestionTime": 1623324436134,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-security.alerts-default-index-template] for index patterns [.internal.alerts-security.alerts-default-*]",
                	"ingestionTime": 1623324436224,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-observability.threshold.alerts-default-index-template] for index patterns [.internal.alerts-observability.threshold.alerts-default-*]",
                	"ingestionTime": 1623324436269,
            	},
            	{
                	"logGroupName": "Elastic",
                	"logStreamName": "Elastic-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[ERROR ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]",
                	"ingestionTime": 1623324436431,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": '[WARN ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]',
                	"ingestionTime": 1623324436182,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-1",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": '[ERROR ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]',
                	"ingestionTime": 1623325946278,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": '[INFO ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]',
                	"ingestionTime": 1623326849292,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": '[ERROR ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]":0,"updating":0},"fleet_server":{"total_all_statuses":0,"total_enrolled":0,"healthy":0,"unhealthy":0,"offline":0,"updating":0,"inactive":0,"unenrolled":0,"num_host_urls":0},"license_issued_to":"elasticsearch"}',
                	"ingestionTime": 1623327752414,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[WARN ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]",
                	"ingestionTime": 1623328428416,
            	},
            	{
                	"logGroupName": "Kibana",
                	"logStreamName": "Kibana-2",
                	"owner": 1,
                	"timestamp": log_timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
                	"message": "[ERROR ][o.e.c.m.MetadataIndexTemplateService] [gr7me] updating index template [.alerts-ml.anomaly-detection-health.alerts-default-index-template] for index patterns [.internal.alerts-ml.anomaly-detection-health.alerts-default-*]",
                	"ingestionTime": 1623328431397,
            	},
        	]
            logs.extend(awslog)
    return logs
