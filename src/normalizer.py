from datetime import datetime

class VulsDataNormalizer:
    def __init__(self):
        self.index_template = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 1
            },
            "mappings": {
                "properties": {
                    "scan_timestamp": {"type": "date"},
                    "host": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "keyword"},
                            "ip": {"type": "ip"}
                        }
                    },
                    "vulnerabilities": {
                        "type": "nested",
                        "properties": {
                            "cve_id": {"type": "keyword"},
                            "severity": {"type": "keyword"},
                            "cvss_score": {"type": "float"},
                            "affected_packages": {
                                "type": "nested",
                                "properties": {
                                    "name": {"type": "keyword"},
                                    "version": {"type": "keyword"},
                                    "fixed_version": {"type": "keyword"}
                                }
                            }
                        }
                    }
                }
            }
        }

    def normalize(self, vuls_data):
        normalized_data = []
        for host_data in vuls_data:
            for cve_id, cve_info in host_data.get("ScannedCves", {}).items():
                normalized_entry = {
                    "scan_timestamp": datetime.utcnow().isoformat(),
                    "host": {
                        "name": host_data.get("ServerName"),
                        "ip": host_data.get("ServerIP")
                    },
                    "vulnerabilities": {
                        "cve_id": cve_id,
                        "severity": cve_info.get("Severity"),
                        "cvss_score": cve_info.get("CVSS", {}).get("Score"),
                        "affected_packages": [
                            {
                                "name": pkg.get("Name"),
                                "version": pkg.get("Version"),
                                "fixed_version": pkg.get("FixedVersion")
                            }
                            for pkg in cve_info.get("AffectedPackages", [])
                        ]
                    }
                }
                normalized_data.append(normalized_entry)
        return normalized_data
    
# {
#   "aws_access_key_id": "AKIAFAKEEXAMPLE1234",
#   "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYFAKEKEYEXAMPLE"
# }

bitbucketClientSecret = "1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"

# BitbucketClientSecret = "17xjjdjqal9oje=ouibn-9yqn995cxbw1opd8zeefklb8pfi2ki3g3ojqrp1gc_v"