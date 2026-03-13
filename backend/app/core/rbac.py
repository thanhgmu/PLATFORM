ROLE_PERMISSIONS = {
    "admin": [
        "tenant:create", "tenant:read",
        "plugin:read", "plugin:manage", "plugin:approve", "plugin:install",
        "marketplace:read", "marketplace:manage",
        "behavior:read", "behavior:ingest",
        "consent:read", "consent:manage",
        "openclaw:send", "openclaw:ingest", "openclaw:context",
    ],
    "tenant_admin": [
        "tenant:read",
        "plugin:read", "plugin:install",
        "marketplace:read",
        "behavior:read", "behavior:ingest",
        "consent:read", "consent:manage",
        "openclaw:send", "openclaw:ingest", "openclaw:context",
    ],
    "user": [
        "plugin:read",
        "marketplace:read",
        "behavior:ingest",
        "consent:read",
        "openclaw:send", "openclaw:context",
    ],
}

def has_permission(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, [])

def role_in(role: str, allowed_roles: list[str]) -> bool:
    return role in allowed_roles
