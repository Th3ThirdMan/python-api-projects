

def create_summary(licensed_count, total_users, users):
    summary = {
        "licensed": licensed_count,
        "total": total_users,
        "unlicensed": total_users - licensed_count,
        "percentage": round((licensed_count / total_users) * 100, 2),
        "fully_licensed": licensed_count == total_users,
        "action_required": licensed_count < total_users,
        "average_licences_per_user": round(
            sum(len(user["assignedLicenses"]) for user in users)
            / total_users,
            2
        ),
        "tenant_health":
    "Good"
    if licensed_count / total_users >= 0.9
    else "Needs Attention"
    }

    return summary