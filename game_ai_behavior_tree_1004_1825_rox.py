# 代码生成时间: 2025-10-04 18:25:42
import tkinter as tk
from tkinter import messagebox

# 定义行为树节点基类
class BehaviorTreeNode:
    def evaluate(self):
        """评估节点状态

        Returns:
            bool: True表示节点成功执行，False表示失败。"""
        raise NotImplementedError

# 定义条件节点，检查是否满足特定条件
class ConditionNode(BehaviorTreeNode):
    def __init__(self, name, condition_func):
        self.name = name
        self.condition_func = condition_func

    def evaluate(self):
        """评估条件是否满足

        Returns:
            bool: True如果条件满足，False否则。"""
        try:
            return self.condition_func()
        except Exception as e:
            print(f"Error evaluating condition '{self.name}': {e}")
            return False

# 定义行为节点，执行特定行为
class ActionNode(BehaviorTreeNode):
    def __init__(self, name, action_func):
        self.name = name
        self.action_func = action_func

    def evaluate(self):
        """执行行为

        Returns:
            bool: True如果行为成功执行，False如果执行失败。"""
        try:
            return self.action_func()
        except Exception as e:
            print(f"Error executing action '{self.name}': {e}")
            return False

# 定义序列节点，按顺序执行子节点
class SequenceNode(BehaviorTreeNode):
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def evaluate(self):
        """按顺序评估子节点

        Returns:
            bool: True如果所有子节点都成功，False如果任一子节点失败。"""
        for child in self.children:
            if not child.evaluate():
                return False
        return True

# 定义选择节点，按优先级执行子节点
class SelectorNode(BehaviorTreeNode):
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def evaluate(self):
        """按优先级评估子节点

        Returns:
            bool: True如果找到成功执行的子节点，False如果所有子节点都失败。"""
        for child in self.children:
            if child.evaluate():
                return True
        return False

# 示例条件函数
def is_enemy_in_range():
    return True  # 假设敌人总是在范围内

# 示例行为函数
def attack_enemy():
    print("Attacking enemy...")
    return True  # 假设攻击总是成功

# 创建行为树节点
condition_node = ConditionNode("IsEnemyInRange", is_enemy_in_range)
action_node = ActionNode("AttackEnemy", attack_enemy)
sequence_node = SequenceNode("AttackSequence", [condition_node, action_node])
selector_node = SelectorNode("RootSelector", [sequence_node])

# 运行行为树
def run_behavior_tree():
    result = selector_node.evaluate()
    if result:
        print("Behavior tree executed successfully.")
    else:
        print("Behavior tree failed to execute.")

# 创建Tkinter GUI应用程序
class BehaviorTreeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game AI Behavior Tree")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        # 创建运行按钮
        self.run_button = tk.Button(self, text="Run Behavior Tree", command=run_behavior_tree)
        self.run_button.pack(pady=20)

def main():
    app = BehaviorTreeApp()
    app.mainloop()

if __name__ == "__main__":
    main()