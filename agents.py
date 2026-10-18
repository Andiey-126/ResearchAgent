from claude_agent_sdk import AgentDefinition
from system_prompt import researcher_prompt

# first agent: researcher
researcher = AgentDefinition(
    # for main agent to read
    description="This subagent is for information research, when user ask for data collection, need to call this agent to finish the task",
    # subagent's system prompt
    prompt=researcher_prompt,
    tools=["Read", "Write"], # should be WebSearch
    model="haiku"
)