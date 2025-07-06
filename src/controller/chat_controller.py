import json
from typing import List, Dict

## Tools definition
from src.tools.main import tools

## import for LLm
from src.llms.openai_llm import OpenAILLM
from src.llms.gemini_llm import GeminiLLM

## importing all the functions
from src.tools.project_info_tool import project_info_tool
from src.tools.certificate_info_tool import certificate_info_tool
from src.tools.helper_tools import record_unknown_question, record_user_details

class ChatController:
    def __init__(self):
        self.openai = OpenAILLM()
        self.gemini = GeminiLLM()

        self.name = "Hitesh Solanki"

        with open("src/public/profile.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()

    def handle_tool_call(self, tool_calls: List) -> List[Dict]:
        results = []
        for tc in tool_calls:
            tool_name = tc.function.name
            args = json.loads(tc.function.arguments)
            tool = globals().get(tool_name)
            result = tool(**args) if tool else {}

            results.append({
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tc.id
            })
        return results

    def system_prompt(self) -> str:
        prompt = (
            f"You are acting as {self.name}. You are answering questions on {self.name}'s website, "
            f"particularly about {self.name}'s career, background, and skills. Use the provided summary to answer faithfully. "
            "If you don't know an answer, use the record_unknown_question tool. If the user provides their email or wants to stay in touch, use record_user_details."
            "provide proper formated answer in Markdown format."
        )
        prompt += f"\n\n## Summary:\n{self.summary}\n\n"

        return prompt

    def chat(self, message: str, history: List[Dict[str, str]]) -> str:
        messages = [{"role": "system", "content": self.system_prompt()}] + history + [{"role": "user", "content": message}]
        done = False
        while not done:
            response = self.openai.get_llm_model().chat.completions.create(model=self.openai.model_name, messages=messages, tools=tools)
            choice = response.choices[0]
            if choice.finish_reason == "tool_calls":
                messages.append(choice.message)
                print(choice.message.tool_calls)
                messages.extend(self.handle_tool_call(choice.message.tool_calls))
            else:
                done = True
        return response.choices[0].message.content