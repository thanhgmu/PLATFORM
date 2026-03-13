ROLE_PERMISSIONS = {
    "admin": ["tenant:create", "tenant:read", "plugin:manage", "marketplace:manage"],
    "tenant_admin": ["tenant:read", "plugin:read", "marketplace:read", "behavior:read"],
    "user": ["plugin:read", "marketplace:read"],
}

def has_permission(role: str, permission: str) -> bool:
    return permission in ROLE_PERMISSIONS.get(role, [])
