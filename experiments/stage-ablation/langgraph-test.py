"""
pfb 状态机 → LangGraph graph 映射测试

核心机制：
1. Checkpoint：每个 superstep 保存状态，crash 后从最后一个 checkpoint 恢复
2. Retry：自动重试失败节点（exponential backoff + jitter）
3. Error handler：重试耗尽后运行补偿逻辑（Saga pattern）

pfb 状态机：
- 分解阶段：分解树是"一次性生成"，没有"分解失败→回退→重新分解"的机制
- 搜索阶段：搜索失败（网络错误/超时/空结果）直接报错，没有"重试→换源→降级"的机制
- 校验阶段：校验失败（judge 偏松/数字矛盾）直接 abort，没有"校验失败→回退→重新搜索→重新校验"的机制

LangGraph 修复：
- 分解阶段：加上"分解失败→回退到上一个 checkpoint→重新分解"的循环边
- 搜索阶段：加上"搜索失败→重试 3 次→换源（arXiv→GitHub→ego-browser）→降级（标 [待核验]）"的补偿逻辑
- 校验阶段：加上"校验失败→回退到搜索阶段→重新搜索→重新校验"的循环边
"""

import os
import sys
import time
import random
import json
from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.errors import GraphRecursionError

# 设置环境变量：限制 checkpoint 反序列化到已知安全类型
os.environ["LANGGRAPH_STRICT_MSGPACK"] = "true"


# ============================================================
# 1. 状态定义
# ============================================================

class PFBState(TypedDict):
    """pfb 状态机的状态"""
    # 输入
    goal: str  # 最终目标（唯一不能改的）
    
    # 分解阶段
    decomposition: dict  # 分解树
    decomposition_attempts: int  # 分解尝试次数
    
    # 搜索阶段
    search_results: dict  # 搜索结果
    search_source: str  # 当前搜索源（arXiv/GitHub/ego-browser）
    search_attempts: int  # 搜索尝试次数
    
    # 校验阶段
    validation_result: dict  # 校验结果
    validation_attempts: int  # 校验尝试次数
    
    # 全局
    status: str  # 当前状态（decomposing/searching/validating/completed/failed）
    error: str  # 错误信息
    checkpoint_count: int  # checkpoint 计数


# ============================================================
# 2. 节点定义
# ============================================================

def decompose(state: PFBState) -> dict:
    """分解阶段：生成分解树"""
    print(f"[decompose] 开始分解: {state['goal']}")
    print(f"[decompose] 尝试次数: {state['decomposition_attempts']}")
    
    # 模拟分解：10% 概率失败
    if random.random() < 0.1:
        print("[decompose] 分解失败（模拟）")
        return {
            "status": "decomposition_failed",
            "error": "分解失败（模拟）",
            "decomposition_attempts": state["decomposition_attempts"] + 1,
        }
    
    # 成功：生成分解树
    decomposition = {
        "goal": state["goal"],
        "subtasks": [
            {"id": "1", "name": "搜索信息", "status": "pending"},
            {"id": "2", "name": "校验信效度", "status": "pending"},
            {"id": "3", "name": "生成结论", "status": "pending"},
        ],
        "gaps": ["[待核验] 搜索源可用性", "[待核验] 校验 judge 偏松"],
    }
    
    print(f"[decompose] 分解成功: {len(decomposition['subtasks'])} 个子任务")
    return {
        "decomposition": decomposition,
        "status": "decomposed",
        "decomposition_attempts": state["decomposition_attempts"] + 1,
    }


def search(state: PFBState) -> dict:
    """搜索阶段：搜索信息"""
    print(f"[search] 开始搜索: {state['goal']}")
    print(f"[search] 当前源: {state['search_source']}")
    print(f"[search] 尝试次数: {state['search_attempts']}")
    
    # 模拟搜索：20% 概率失败
    if random.random() < 0.2:
        print(f"[search] 搜索失败（模拟），源: {state['search_source']}")
        # 换源：arXiv→GitHub→ego-browser
        sources = ["arXiv", "GitHub", "ego-browser"]
        current_idx = sources.index(state["search_source"])
        next_source = sources[(current_idx + 1) % len(sources)]
        print(f"[search] 换源: {state['search_source']} → {next_source}")
        return {
            "status": "search_failed",
            "error": f"搜索失败（模拟），源: {state['search_source']}",
            "search_source": next_source,
            "search_attempts": state["search_attempts"] + 1,
        }
    
    # 成功：生成搜索结果
    search_results = {
        "source": state["search_source"],
        "results": [
            {"title": "结果 1", "url": "https://example.com/1", "confidence": 0.9},
            {"title": "结果 2", "url": "https://example.com/2", "confidence": 0.8},
            {"title": "结果 3", "url": "https://example.com/3", "confidence": 0.7},
        ],
        "gaps": ["[待核验] 结果 3 的信效度"],
    }
    
    print(f"[search] 搜索成功: {len(search_results['results'])} 个结果")
    return {
        "search_results": search_results,
        "status": "searched",
        "search_attempts": state["search_attempts"] + 1,
    }


def validate(state: PFBState) -> dict:
    """校验阶段：校验信效度"""
    print(f"[validate] 开始校验: {state['goal']}")
    print(f"[validate] 尝试次数: {state['validation_attempts']}")
    
    # 模拟校验：15% 概率失败
    if random.random() < 0.15:
        print("[validate] 校验失败（模拟）")
        return {
            "status": "validation_failed",
            "error": "校验失败（模拟）",
            "validation_attempts": state["validation_attempts"] + 1,
        }
    
    # 成功：生成校验结果
    validation_result = {
        "valid": True,
        "confidence": 0.85,
        "gaps": ["[待核验] 结果 3 的信效度"],
    }
    
    print(f"[validate] 校验成功: confidence={validation_result['confidence']}")
    return {
        "validation_result": validation_result,
        "status": "validated",
        "validation_attempts": state["validation_attempts"] + 1,
    }


def complete(state: PFBState) -> dict:
    """完成阶段：生成结论"""
    print(f"[complete] 生成结论: {state['goal']}")
    return {
        "status": "completed",
    }


def fail(state: PFBState) -> dict:
    """失败阶段：重试耗尽后运行补偿逻辑（Saga pattern）"""
    print(f"[fail] 重试耗尽，运行补偿逻辑")
    print(f"[fail] 错误: {state['error']}")
    
    # 补偿逻辑：降级（标 [待核验]）
    return {
        "status": "failed",
        "validation_result": {
            "valid": False,
            "confidence": 0.0,
            "gaps": ["[降级] 所有结果标 [待核验]"],
        },
    }


# ============================================================
# 3. 条件边定义
# ============================================================

def after_decompose(state: PFBState) -> str:
    """分解后的条件边"""
    if state["status"] == "decomposition_failed":
        if state["decomposition_attempts"] >= 3:
            return "fail"  # 重试耗尽
        return "decompose"  # 重新分解
    return "search"  # 进入搜索


def after_search(state: PFBState) -> str:
    """搜索后的条件边"""
    if state["status"] == "search_failed":
        if state["search_attempts"] >= 6:  # 3 个源 × 2 次
            return "fail"  # 重试耗尽
        return "search"  # 重新搜索（换源）
    return "validate"  # 进入校验


def after_validate(state: PFBState) -> str:
    """校验后的条件边"""
    if state["status"] == "validation_failed":
        if state["validation_attempts"] >= 3:
            return "fail"  # 重试耗尽
        return "search"  # 回退到搜索
    return "complete"  # 完成


# ============================================================
# 4. 构建 graph
# ============================================================

def build_graph() -> StateGraph:
    """构建 pfb 状态机的 LangGraph graph"""
    graph = StateGraph(PFBState)
    
    # 添加节点
    graph.add_node("decompose", decompose)
    graph.add_node("search", search)
    graph.add_node("validate", validate)
    graph.add_node("complete", complete)
    graph.add_node("fail", fail)
    
    # 添加边
    graph.set_entry_point("decompose")
    graph.add_conditional_edges("decompose", after_decompose, {
        "decompose": "decompose",
        "search": "search",
        "fail": "fail",
    })
    graph.add_conditional_edges("search", after_search, {
        "search": "search",
        "validate": "validate",
        "fail": "fail",
    })
    graph.add_conditional_edges("validate", after_validate, {
        "search": "search",
        "complete": "complete",
        "fail": "fail",
    })
    graph.add_edge("complete", END)
    graph.add_edge("fail", END)
    
    return graph


# ============================================================
# 5. 测试
# ============================================================

def test_basic_run():
    """测试基本运行"""
    print("=" * 60)
    print("测试 1: 基本运行（无 crash）")
    print("=" * 60)
    
    graph = build_graph().compile()
    
    # 运行 graph
    result = graph.invoke({
        "goal": "调研 LangGraph 的 checkpoint 机制",
        "decomposition": {},
        "decomposition_attempts": 0,
        "search_results": {},
        "search_source": "arXiv",
        "search_attempts": 0,
        "validation_result": {},
        "validation_attempts": 0,
        "status": "decomposing",
        "error": "",
        "checkpoint_count": 0,
    })
    
    print(f"\n最终状态: {result['status']}")
    print(f"分解尝试: {result['decomposition_attempts']}")
    print(f"搜索尝试: {result['search_attempts']}")
    print(f"校验尝试: {result['validation_attempts']}")
    
    return result


def test_crash_recovery():
    """测试 crash 恢复"""
    print("\n" + "=" * 60)
    print("测试 2: crash 恢复")
    print("=" * 60)
    
    # 使用 SQLite checkpointer
    with SqliteSaver.from_conn_string(":memory:") as checkpointer:
        # 第一次运行：跑一半 crash
        print("\n[run 1] 第一次运行（模拟 crash）")
        
        # 构建带 crash 的 graph
        graph_crash = StateGraph(PFBState)
        graph_crash.add_node("decompose", decompose)
        
        def crash_in_search(state: PFBState) -> dict:
            print("[crash] 模拟 crash（搜索阶段）")
            raise Exception("模拟 crash")
        
        graph_crash.add_node("search", crash_in_search)
        graph_crash.add_node("validate", validate)
        graph_crash.add_node("complete", complete)
        graph_crash.add_node("fail", fail)
        
        graph_crash.set_entry_point("decompose")
        graph_crash.add_conditional_edges("decompose", after_decompose, {
            "decompose": "decompose",
            "search": "search",
            "fail": "fail",
        })
        graph_crash.add_conditional_edges("search", after_search, {
            "search": "search",
            "validate": "validate",
            "fail": "fail",
        })
        graph_crash.add_conditional_edges("validate", after_validate, {
            "search": "search",
            "complete": "complete",
            "fail": "fail",
        })
        graph_crash.add_edge("complete", END)
        graph_crash.add_edge("fail", END)
        
        graph_crash_compiled = graph_crash.compile(checkpointer=checkpointer)
        
        try:
            graph_crash_compiled.invoke({
                "goal": "调研 LangGraph 的 checkpoint 机制",
                "decomposition": {},
                "decomposition_attempts": 0,
                "search_results": {},
                "search_source": "arXiv",
                "search_attempts": 0,
                "validation_result": {},
                "validation_attempts": 0,
                "status": "decomposing",
                "error": "",
                "checkpoint_count": 0,
            }, config={"configurable": {"thread_id": "test-crash"}})
        except Exception as e:
            print(f"[crash] 捕获异常: {e}")
        
        # 第二次运行：从 checkpoint 恢复
        print("\n[run 2] 第二次运行（从 checkpoint 恢复）")
        graph_normal = build_graph().compile(checkpointer=checkpointer)
        
        # 传 None，LangGraph 会从 checkpoint 加载状态
        result = graph_normal.invoke(None, config={"configurable": {"thread_id": "test-crash"}})
        
        print(f"\n最终状态: {result['status']}")
        print(f"分解尝试: {result['decomposition_attempts']}")
        print(f"搜索尝试: {result['search_attempts']}")
        print(f"校验尝试: {result['validation_attempts']}")
        
        return result


if __name__ == "__main__":
    # 测试 1: 基本运行
    result1 = test_basic_run()
    
    # 测试 2: crash 恢复
    result2 = test_crash_recovery()
    
    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)
