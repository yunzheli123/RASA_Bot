from typing import Text, Dict, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.injuries import *

# 假设getInjuries定义在这个文件内
# 如果不是，请适当调整import语句
# from your_module import getInjuries

class ActionInjuriesRecord(Action):
    def name(self) -> Text:
        return "action_injuriesRecord"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("team")
        date = tracker.get_slot("date")
        
        print(f"Team: {name}, Date: {date}")
        text = getInjuries(name, date)

        dispatcher.utter_message(text)

        return []

# 模拟的Dispatcher, Tracker, 和 Domain对象
dispatcher = CollectingDispatcher()
tracker = Tracker(
    "default",
    {"team": "Manchester City", "date": "2023-10-01"},
    {},
    [],
    False,
    None,
    {},
    "action_listen",
)
domain = {}

# 实例化并运行动作
action = ActionInjuriesRecord()
action.run(dispatcher, tracker, domain)

# 输出dispatcher中收集到的消息
print(f"Messages: {dispatcher.messages}")