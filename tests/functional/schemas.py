WHOAMI = {
    "type": "object",
    "properties": {
        "namespace": {"type": "string"},
        "last_time_password_changed": {
            "type": "string",
            "format": "date-time"
        },
        "distinguished_name": {"type": "string"},
        "common_name": {"type": "string"},
        "roles": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 1
            },
            "minItems": 1,
            "uniqueItems": True
        }
    },
    "required": [
        "namespace",
        "last_time_password_changed",
        "distinguished_name",
        "common_name",
        "roles",
    ]
}

NAMESPACES = {
    "type": "object",
    "properties": {
        "namespace": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "link": {
                        "type": "object",
                        "properties": {
                            "rel": {"type": "string"},
                            "href": {"type": "string"}
                        },
                        "required": [
                            "rel",
                            "href"
                        ]
                    }
                },
                "required": [
                    "id",
                    "name",
                    "link"
                ]
            },
        }
    },
    "required": [
        "namespace"
    ]
}

NAMESPACE = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "id": {"type": "string"},
        "inactive": {"type": "boolean"},
        "is_stale_allowed": {"type": "boolean"},
        "is_encryption_enabled": {"type": ["string", "boolean"]},  # Workaround: The API returns a string instead of
        # a boolean
        "is_compliance_enabled": {"type": "boolean"},
        "global": {"type": ["string", "null"]},
        "remote": {"type": ["string", "null"]},
        "vdc": {"type": ["string", "null"]},
        "default_data_services_vpool": {"type": "string"},
        "allowed_vpools_list": {"type": "array"},
        "disallowed_vpools_list": {"type": "array"},
        "default_bucket_block_size": {"type": "number"},
        "user_mapping": {"type": "array"},
        "link": {
            "type": "object",
            "properties": {
                "rel": {"type": "string"},
                "href": {"type": "string"}
            },
            "required": [
                "rel",
                "href"
            ]
        }
    },
    "required": [
        "name",
        "id",
        "inactive",
        "is_stale_allowed",
        "is_encryption_enabled",
        "is_compliance_enabled",
        "global",
        "remote",
        "vdc",
        "default_data_services_vpool",
        "allowed_vpools_list",
        "disallowed_vpools_list",
        "default_bucket_block_size",
        "user_mapping",
        "link"
    ]
}

CERTIFICATE = {
    "type": "object",
    "properties": {
        "chain": {"type": "string"}
    },
    "required": [
        "chain",
    ]
}

LICENSE = {
    "type": "object",
    "properties": {
        "license_feature": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "product": {"type": "string"},
                    "version": {"type": "string"},
                    "model": {"type": "string"},
                    "licensed_ind": {"type": "boolean"},
                    "trial_license_ind": {"type": "boolean"},
                    "storage_capacity": {"type": "string"},
                    "notice": {"type": "string"},
                    "serial": {"type": "string"},
                    "expired_ind": {"type": "boolean"},
                    "issued_date": {"type": "string", "format": "date-time"},
                    "license_id_indicator": {"type": "string"},
                    "issuer": {"type": "string"},
                    "site_id": {"type": "string"}
                },
                "required": [
                    "product",
                    "version",
                    "model",
                    "licensed_ind",
                    "trial_license_ind",
                    "storage_capacity",
                    "notice",
                    "serial",
                    "expired_ind",
                    "issued_date",
                    "license_id_indicator",
                    "issuer",
                    "site_id"
                ]
            },
        },
        "license_text": {"type": "string"}
    },
    "required": [
        "license_feature",
        "license_text"
    ]
}

STORAGE_POOL = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "isProtected": {"type": "boolean"},
        "isColdStorageEnabled": {"type": "boolean"}
    },
    "required": [
        "id",
        "name",
        "isProtected",
        "isColdStorageEnabled"
    ]
}

STORAGE_POOLS = {
    "type": "object",
    "properties": {
        "varray": {
            "type": "array",
            "minItems": 1,
            "items": STORAGE_POOL
        }
    },
    "required": [
        "varray"
    ]
}
