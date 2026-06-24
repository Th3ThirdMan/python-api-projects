

def print_tenant_summary(summary, groups, licences, organization):
    org = organization[0]
    domain = org["verifiedDomains"][0]
    
    print()
    print("===================")
    print("Tenant Summary")
    print("===================")
    
    print()
    print("Organization")
    print("============")
    print(f"Name   : {org['displayName']}")
    print(f"Domain : {domain['name']}")
    print(f"Type   : {domain['type']}")

    print()
    print("Users")
    print("=====")
    print(f"Total      : {summary['total']}")
    print(f"Licensed   : {summary['licensed']}")
    print(f"Unlicensed : {summary['unlicensed']}")

    print()
    print("Groups")
    print("======")
    print(f"Total      : {len(groups)}")

    print()
    print("Licences")
    print("========")
    print(f"Total SKUs : {len(licences)}")

    print()
    print("Health")
    print("======")
    print(summary["tenant_health"])