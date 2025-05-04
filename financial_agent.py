from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("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")
# websearch agent
web_search_agent = Agent(
    name= "Web Search Agent",
    role= "Search the web for the information",
    model= Groq(id= "llama3-groq-70b-8192-tool-use-preview"),
    tools= [DuckDuckGo()],
    instructions=["Always include the source of the information you find."],
    show_tools_calls=True,
    markdown=True,
)

# financial agent
finance_agent = Agent(
    name= "Finance AI Agent",
    role= "Answer financial questions",
    model= Groq(id= "llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, 
                         company_news=True, )],
    instructions=[
        "Use tables to display the data"
    ],
    show_tools_calls=True,
    markdown=True,
)
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=[
        "Always include sources","Use table to display the data"],
    show_tools_calls=True,
    markdown=True,
)
multi_ai_agent.print_response("summarize analyst recommendation and share the lates news for NVDA", stream=True)