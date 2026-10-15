from claude_agent_sdk import (ToolPermissionContext, PermissionResultAllow, PermissionResultDeny)
from path import notes_path, output_path
from pathlib import Path

def check_Write(input_data):
    absolute_path = output_path
    path_dir = Path(input_data['file_path'])

    path_check = False
    input_status = False
    
    # only check wether the Write is inside output/ .md file
    print(f"[check] input_data is: {input_data['file_path']}")

    # if the file path in root and in `output`
    if path_dir.resolve().parent.parent == absolute_path.resolve().parent and path_dir.resolve().parent.name == 'output':
        path_check=True

    if input_data.get("file_path", "").endswith(".md"):
        input_status = True

    if path_check and input_status:
        return PermissionResultAllow()
    return PermissionResultDeny(message="The mission must inside folder 'output' and only .md file permitted")

def check_Read(input_data):
    absolute_path = notes_path
    path_dir = Path(input_data["file_path"])

    path_check = False
    print(f"[check] input_data is: {input_data['file_path']}")

    # if the file path in root and in `notes`
    if path_dir.resolve().parent.parent == absolute_path.resolve().parent and path_dir.resolve().parent.name == 'notes':
        path_check=True

    if path_check:
        return PermissionResultAllow()
    return PermissionResultDeny(message="Only file in 'notes' permitted")

# check tool called function
async def check_tool(tool_name: str, input_data: dict, context: ToolPermissionContext):
    # tool_name: check which tool the agent used
    if tool_name in ["Write", "Read"]:
        if tool_name == "Write":
            permission = check_Write(input_data)

        if tool_name == "Read":
            permission = check_Read(input_data)

        return permission
    else:
        return PermissionResultDeny(message="'Write' and 'Read' tool allowed only")