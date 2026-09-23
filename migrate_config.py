import json

# --- SPKL-like Configuration (Simplified) ---
# This dictionary represents a simplified view of how plugin metadata
# might be structured or managed by a legacy tool like spkl.
# In a real scenario, this might come from XML files, project configurations, etc.
spkl_plugin_config = {
    "plugin_assembly": {
        "name": "MyOrg.Plugins",
        "path": "bin/Debug/MyOrg.Plugins.dll",
        "isolation_mode": "Sandbox",
        "source_type": "Database"
    },
    "plugin_types": [
        {
            "name": "MyOrg.Plugins.MyFirstPlugin",
            "assembly": "MyOrg.Plugins",
            "friendly_name": "My First Plugin",
            "workflow_activity_group_name": None
        },
        {
            "name": "MyOrg.Plugins.MySecondPlugin",
            "assembly": "MyOrg.Plugins",
            "friendly_name": "My Second Plugin",
            "workflow_activity_group_name": None
        }
    ],
    "sdk_message_processing_steps": [
        {
            "plugin_type": "MyOrg.Plugins.MyFirstPlugin",
            "message": "Create",
            "primary_entity": "account",
            "secondary_entity": None,
            "mode": "Synchronous",
            "stage": "PostOperation",
            "rank": 1,
            "filtering_attributes": [],
            "configuration": None
        },
        {
            "plugin_type": "MyOrg.Plugins.MyFirstPlugin",
            "message": "Update",
            "primary_entity": "contact",
            "secondary_entity": None,
            "mode": "Asynchronous",
            "stage": "PreOperation",
            "rank": 1,
            "filtering_attributes": ["firstname", "lastname"],
            "configuration": "Some config string"
        },
        {
            "plugin_type": "MyOrg.Plugins.MySecondPlugin",
            "message": "Delete",
            "primary_entity": "opportunity",
            "secondary_entity": None,
            "mode": "Synchronous",
            "stage": "PostOperation",
            "rank": 1,
            "filtering_attributes": [],
            "configuration": None
        }
    ]
}

def migrate_spkl_to_pillaro(spkl_data):
    """
    Simulates the migration of a simplified spkl-like plugin configuration
    to a Pillaro-like configuration.

    This function demonstrates how different tools might structure and manage
    the same underlying Dataverse plugin metadata. Pillaro often aims for
    a more consolidated and modern configuration style.
    """
    pillaro_data = {
        "solution_name": "MigratedSolution", # Placeholder for the solution name
        "assembly_path": spkl_data["plugin_assembly"]["path"], # Global assembly path
        "plugins": []
    }

    # Iterate through spkl's defined plugin types
    for spkl_type in spkl_data["plugin_types"]:
        plugin_entry = {
            "name": spkl_type["name"],
            "assembly_file": spkl_data["plugin_assembly"]["path"].split('/')[-1], # Just the DLL name
            "friendly_name": spkl_type["friendly_name"],
            "steps": []
        }

        # Find all steps associated with the current plugin type
        for spkl_step in spkl_data["sdk_message_processing_steps"]:
            if spkl_step["plugin_type"] == spkl_type["name"]:
                step_entry = {
                    "message": spkl_step["message"],
                    "entity": spkl_step["primary_entity"],
                    "stage": spkl_step["stage"],
                    "mode": spkl_step["mode"],
                    "rank": spkl_step["rank"],
                    "filtering_attributes": spkl_step["filtering_attributes"],
                    "configuration": spkl_step["configuration"]
                }
                plugin_entry["steps"].append(step_entry)
        pillaro_data["plugins"].append(plugin_entry)

    return pillaro_data

if __name__ == "__main__":
    print("--- Original SPKL-like Configuration ---")
    print(json.dumps(spkl_plugin_config, indent=2))
    print("\n" + "="*50 + "\n")

    # Perform the simulated migration
    # This is where the core concept of transitioning between tools is illustrated.
    # The output shows how Pillaro might consolidate information or use a different schema.
    pillaro_migrated_config = migrate_spkl_to_pillaro(spkl_plugin_config)

    print("--- Migrated Pillaro-like Configuration ---")
    print(json.dumps(pillaro_migrated_config, indent=2))
    print("\n" + "="*50 + "\n")

    print("Migration simulation complete.")
    print("Notice how plugin types and their steps are grouped under a single 'plugins' array,")
    print("reflecting a potentially more streamlined configuration approach.")
