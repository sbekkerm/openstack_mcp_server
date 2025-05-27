"""Demo Openstack MCP client"""
import asyncio
import argparse
from agents.mcp import MCPServerSse
from agents.run import RunConfig
from agents import Agent, Runner
from agents.model_settings import ModelSettings
from agents.models.openai_provider import OpenAIProvider
from agents import set_tracing_disabled

set_tracing_disabled(True)


async def mcp_client(llm_api_url: str, llm_api_key: str, model_name: str, mcp_url: str):
    """Interacts with an Openstack MCP server"""
    llm_provider = OpenAIProvider(
        base_url=llm_api_url,
        api_key=llm_api_key,
        use_responses=False
    )
    run_config = RunConfig(
        model=model_name,
        model_provider=llm_provider,
    )
    settings = {
        "name": "Openstack mcp server",
        "params": {
            "url": mcp_url
        }
    }
    async with MCPServerSse(**settings) as server:
        agent = Agent(
            name="openstack-agent",
            instructions="Use the tools to answer the questions.",
            mcp_servers=[server],
            model_settings=ModelSettings(tool_choice="auto"),)

        queries = [
            "Are there flavors that supports GPU passthrough?",
            "List all servers",
            "List all networks",
            "What's the network type for the `management` network?",
            "Are there created keypairs?",
            "What images are available?",
            "What flavors exist?",
            "What keypairs have been created?",
            "What networks are available?",
            "What subnets are defined?",
            "What ports exist?",
            "What security groups are present?",
            "Which routers have been created?",
            "Are there any network agents running?"
        ]

        for message in queries:
            print(f"\n\nRunning: {message}")
            result = await Runner.run(starting_agent=agent, input=message, run_config=run_config)
            print(result.final_output)


def main():
    """Entry point"""
    parser = argparse.ArgumentParser(
        description="Openstack MCP client")

    parser.add_argument(
        "--llm_api_url",
        type=str,
        required=True,
        help="LLM API endpoint URL")

    parser.add_argument(
        "--llm_api_key",
        type=str,
        required=True,
        help="LLM API key")

    parser.add_argument(
        "--model_name",
        type=str,
        required=True,
        help="LLM model name")

    parser.add_argument(
        "--mcp_url",
        type=str,
        required=True,
        help="MCP server URL")

    args = parser.parse_args()

    asyncio.run(mcp_client(
        llm_api_url=args.llm_api_url,
        llm_api_key=args.llm_api_key,
        model_name=args.model_name,
        mcp_url=args.mcp_url,
    ))


if __name__ == "__main__":
    main()
