from dotenv import load_dotenv
load_dotenv()

import asyncio
from claude_agent_sdk import (ClaudeAgentOptions, query, SystemMessage, AssistantMessage, 
                              UserMessage, TextBlock, ToolUseBlock, ResultMessage, ToolResultBlock)
from check_tools import check_tool
from initialization import initialize_notes
from agents import researcher # subagents
from system_prompt import main_prompt

async def main():
    initialize_notes()

    options = ClaudeAgentOptions(model="haiku",                     # model is haiku, the cheapest model
                                 system_prompt=main_prompt,         # main agent's system prompt
                                 setting_sources=[],                # load no filesystem settings
                                 agents={"researcher": researcher}, # add subagents
                                 tools=["Read", "Write", "Agent"],  # this determine the tools be found by model
                                 can_use_tool=check_tool,           # if claude code not sure the tool can be called or not, it will check the tool function
                                 permission_mode="default",
                                 max_budget_usd=0.30,               # stop this query() run once estimated spend reaches this
                                 )
    # input the user message
    prompt = input("Chat: ")

    async for message in query(prompt=prompt, options=options):
        # check if it is the ai feedback (the model output)
        if isinstance(message, AssistantMessage):
            print("[main]" if message.parent_tool_use_id is None else f"[sub]: {message.parent_tool_use_id}")
            for block in message.content: # message contain multi pieces of information
                # the assistant response
                if isinstance(block, TextBlock):
                    print(block.text, end="")
                # Tool Requisition Form
                elif isinstance(block, ToolUseBlock):
                    print(block.name)  # tool name
                    print(block.input) # local file path
                    print(block.id) 
            print()
        
        # check if it is the system message, which will show model configuration
        elif isinstance(message, SystemMessage):
            if message.subtype == "init":
                print(f"CLI version: {message.data.get('claude_code_version')}") # add one line (the native CLI auto-updates, so record which version ran)
                print(f"Model: {message.data.get('model')}")
                print(f"Tools: {message.data.get('tools')}")
                print(f"Session_id: {message.data.get('session_id')}")
        
        # monitor claude code send model's feedback
        elif isinstance(message, UserMessage):
            print("[main]" if message.parent_tool_use_id is None else f"[sub]: {message.parent_tool_use_id}")
            if isinstance(message.content, list):
                for block in message.content:
                    if isinstance(block, ToolResultBlock):
                        print(f"is_error: {block.is_error}")
                        print(f"content: {str(block.content)[:200]}")
                        print(f"id: {block.tool_use_id}")
            elif isinstance(message.content, str):
                print(message.content)
        
        # check if it is the result data, which will show info like end type and costs
        elif isinstance(message, ResultMessage):
            print(f"Message subtype: {message.subtype}") # show how this agent endup
            print(f"Message number of turns: {message.num_turns}")
            print(f"Message duration: {message.duration_ms}")
            print("Total cost:","unknown" if message.total_cost_usd is None else message.total_cost_usd)
            if message.subtype == "success":
                print(message.result)

if __name__ == "__main__":
    asyncio.run(main())