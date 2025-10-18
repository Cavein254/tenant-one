from db_multitenant import mapper


class TenantMapper(mapper.TenantMapper):
    """
    Handles tenant resolution for db_multitenant.

    - During web requests: tenant name is derived from subdomain (shop1.example.com → 'shop1')
    - During migrations/shell/startup: defaults to 'default' tenant mapped to the base database ('tenants')
    """

    def get_tenant_name(self, request):
        # Used for Django shell, startup, or migrations
        if request is None:
            return "default"

        # Extract the first part of the hostname before any port
        hostname = request.get_host().split(":")[0].lower()
        return hostname.split(".")[0]

    def get_db_name(self, request, tenant_name):
        """
        Maps tenant_name to database name.

        For example:
            tenant_name='shop1' → db_name='tenant_shop1'
            tenant_name='default' → db_name='tenants'
        """

        if tenant_name == "default":
            return "tenants"  # Matches MARIADB_DATABASE in docker-compose.yml

        return f"tenant_{tenant_name}"

    def get_cache_prefix(self, request, tenant_name, db_name):
        """
        Used for caching. Keeps cache keys tenant-specific.
        """
        return f"tenants_{tenant_name or 'default'}"
