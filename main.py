from dotenv import load_dotenv
load_dotenv()

import asyncio
from claude_agent_sdk import ClaudeAgentOptions, query, SystemMessage, AssistantMessage, TextBlock, ResultMessage

async def main():
    options = ClaudeAgentOptions(model="haiku",       # model is haiku, the cheapest model
                                 max_budget_usd=0.15, # stop this query() run once estimated spend reaches this
                                 tools=[],            # tools off all 
                                 setting_sources=[],  # load no filesystem settings
                                 )
    # input the user message
    prompt = input("Chat: ")
    
    async for message in query(prompt=prompt, options=options):
        print(type(message).__name__)

        # check if it is the systemMessage: The notification of state
        if isinstance(message, SystemMessage):
            print(message.subtype)
            print(message.data)     # full original data of this information 
        # check if it is the ai feedback
        elif isinstance(message, AssistantMessage):
            for block in message.content: # message.content contain multiple pieces(block)
                print(block)
                if isinstance(block, TextBlock):
                    print(block.text, end="")
        elif isinstance(message, ResultMessage):
            print(message.subtype)
            print(message.num_turns)
            print(message.total_cost_usd)
    print()

if __name__ == "__main__":
    asyncio.run(main())