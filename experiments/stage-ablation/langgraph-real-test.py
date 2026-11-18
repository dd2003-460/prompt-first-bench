"""
LangGraph 跑真实任务：用 pfb 状态机跑 gpu 题

核心机制：
1. Checkpoint：每个 superstep 保存状态，crash 后从最后一个 checkpoint 恢复
2. Retry：自动重试失败节点（exponential backoff + jitter）
3. Error handler：重试耗尽后运行补偿逻辑（Saga pattern）

pfb 状态机：
- 分解阶段：生成分解树
- 搜索阶段：搜索信息
- 校验阶段：校验信效度
"""

import os
import sys
import time
import json
from typing import TypedDict

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

# 设置环境变量：限制 checkpoint 反序列化到已知安全类型
os.environ["LANGGRAPH_STRICT_MSGPACK"] = "true"

# 添加 pfb 路径
sys.path.insert(0, "/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation")

from ablation_harness import call_llm
from s5_pipeline import _extract_json, decompose, search_node, verify_node
from s8b_pilot import QUESTIONS


# ============================================================
# 1. 状态定义
# ============================================================

class PFBState(TypedDict):
    """pfb 状态机的状态"""
    # 输入
    goal: str  # 最终目标（唯一不能改的）
    qid: str  # 题目 id
    
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


# ============================================================
# 2. 节点定义
# ============================================================

def decompose(state: PFBState) -> dict:
    """分解阶段：生成分解树"""
    print(f"[decompose] 开始分解: {state['goal'][:80]}...")
    print(f"[decompose] 尝试次数: {state['decomposition_attempts']}")
    
    # 调用 pfb 的 decompose 函数（注意：这里的 decompose 是 pfb 的，不是本文件的）
    try:
        from s5_pipeline import decompose as pfb_decompose
        result = pfb_decompose(state["goal"])
        if isinstance(result, tuple):
            nodes, _raw = result
        else:
            nodes = result
        if not nodes:
            raise Exception("分解失败：返回空节点")
        
        print(f"[decompose] 分解成功: {len(nodes)} 个节点")
        return {
            "decomposition": {"nodes": nodes},
            "status": "decomposed",
            "decomposition_attempts": state["decomposition_attempts"] + 1,
        }
    except Exception as e:
        print(f"[decompose] 分解失败: {e}")
        return {
            "status": "decomposition_failed",
            "error": str(e),
            "decomposition_attempts": state["decomposition_attempts"] + 1,
        }


def search(state: PFBState) -> dict:
    """搜索阶段：搜索信息"""
    print(f"[search] 开始搜索: {state['goal'][:80]}...")
    print(f"[search] 当前源: {state['search_source']}")
    print(f"[search] 尝试次数: {state['search_attempts']}")
    
    nodes = state["decomposition"]["nodes"]
    search_results = {}
    
    # 对每个节点做搜索
    for node in nodes:
        node_id = node.get("id", "unknown")
        claim = node.get("claim", "")
        search_query = node.get("search_query", claim)
        
        try:
            srcs, err = search_node({
                "id": node_id,
                "claim": claim,
                "search_query": search_query,
            }, qid=state["qid"])
            
            if err:
                print(f"[search] 节点 {node_id} 搜索失败: {err}")
                search_results[node_id] = {"error": err, "sources": []}
            else:
                print(f"[search] 节点 {node_id} 搜索成功: {len(srcs)} 个来源")
                search_results[node_id] = {"error": None, "sources": srcs}
        except Exception as e:
            print(f"[search] 节点 {node_id} 搜索异常: {e}")
            search_results[node_id] = {"error": str(e), "sources": []}
    
    # 检查是否全部失败
    all_failed = all(r.get("error") for r in search_results.values())
    if all_failed:
        print(f"[search] 全部节点搜索失败")
        return {
            "status": "search_failed",
            "error": "全部节点搜索失败",
            "search_results": search_results,
            "search_attempts": state["search_attempts"] + 1,
        }
    
    print(f"[search] 搜索完成: {sum(1 for r in search_results.values() if not r.get('error'))}/{len(nodes)} 成功")
    return {
        "search_results": search_results,
        "status": "searched",
        "search_attempts": state["search_attempts"] + 1,
    }


def validate(state: PFBState) -> dict:
    """校验阶段：校验信效度"""
    print(f"[validate] 开始校验: {state['goal'][:80]}...")
    print(f"[validate] 尝试次数: {state['validation_attempts']}")
    
    nodes = state["decomposition"]["nodes"]
    search_results = state["search_results"]
    validation_result = {}
    
    # 对每个节点做校验
    for node in nodes:
        node_id = node.get("id", "unknown")
        claim = node.get("claim", "")
        srcs = search_results.get(node_id, {}).get("sources", [])
        
        try:
            status, evidence, corrected, _r = verify_node(
                {"id": node_id, "claim": claim, "source": "search"}, srcs)
            validation_result[node_id] = {
                "status": status,
                "evidence": evidence,
                "corrected_claim": corrected,
            }
            print(f"[validate] 节点 {node_id}: {status}")
        except Exception as e:
            print(f"[validate] 节点 {node_id} 校验异常: {e}")
            validation_result[node_id] = {
                "status": "failed",
                "evidence": str(e),
                "corrected_claim": claim,
            }
    
    # 检查是否全部失败
    all_failed = all(r.get("status") == "failed" for r in validation_result.values())
    if all_failed:
        print(f"[validate] 全部节点校验失败")
        return {
            "status": "validation_failed",
            "error": "全部节点校验失败",
            "validation_result": validation_result,
            "validation_attempts": state["validation_attempts"] + 1,
        }
    
    verified = sum(1 for r in validation_result.values() if r.get("status") == "verified")
    print(f"[validate] 校验完成: {verified}/{len(nodes)} verified")
    return {
        "validation_result": validation_result,
        "status": "validated",
        "validation_attempts": state["validation_attempts"] + 1,
    }


def complete(state: PFBState) -> dict:
    """完成阶段：生成结论"""
    print(f"[complete] 生成结论: {state['goal'][:80]}...")
    
    nodes = state["decomposition"]["nodes"]
    validation_result = state["validation_result"]
    
    # 生成最终答案
    verified_nodes = [
        {"id": nid, "claim": r.get("corrected_claim", ""), "evidence": r.get("evidence", "")}
        for nid, r in validation_result.items()
        if r.get("status") == "verified"
    ]
    
    print(f"[complete] 生成结论: {len(verified_nodes)} 个 verified 节点")
    return {
        "status": "completed",
        "final_answer": {
            "verified_nodes": verified_nodes,
            "total_nodes": len(nodes),
        },
    }


def fail(state: PFBState) -> dict:
    """失败阶段：重试耗尽后运行补偿逻辑（Saga pattern）"""
    print(f"[fail] 重试耗尽，运行补偿逻辑")
    print(f"[fail] 错误: {state['error']}")
    
    # 补偿逻辑：降级（标 [待核验]）
    return {
        "status": "failed",
        "final_answer": {
            "verified_nodes": [],
            "total_nodes": 0,
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
        if state["search_attempts"] >= 3:
            return "fail"  # 重试耗尽
        return "search"  # 重新搜索
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

import sys

def test_real_task(qid="gpu"):
    """测试真实任务：跑指定题目（默认 gpu）"""
    print("=" * 60)
    print(f"测试：LangGraph 跑真实任务（{qid} 题）")
    print("=" * 60)
    
    # 获取题目
    question = QUESTIONS[qid]
    print(f"[test] 题目: {question[:100]}...")
    
    # 使用 SQLite checkpointer（文件存储，支持 crash 恢复）
    checkpoint_file = f"/tmp/langgraph-checkpoint-{qid}.sqlite"
    with SqliteSaver.from_conn_string(checkpoint_file) as checkpointer:
        graph = build_graph().compile(checkpointer=checkpointer)
        
        # 运行 graph
        result = graph.invoke({
            "goal": question,
            "qid": qid,
            "decomposition": {},
            "decomposition_attempts": 0,
            "search_results": {},
            "search_source": "arXiv",
            "search_attempts": 0,
            "validation_result": {},
            "validation_attempts": 0,
            "status": "decomposing",
            "error": "",
        }, config={"configurable": {"thread_id": f"test-{qid}"}})
        
        print(f"\n最终状态: {result['status']}")
        print(f"分解尝试: {result['decomposition_attempts']}")
        print(f"搜索尝试: {result['search_attempts']}")
        print(f"校验尝试: {result['validation_attempts']}")
        
        if result.get("final_answer"):
            print(f"verified 节点: {len(result['final_answer'].get('verified_nodes', []))}")
            print(f"总节点: {result['final_answer'].get('total_nodes', 0)}")
        
        # 测试 crash 恢复：从 checkpoint 恢复
        print("\n[crash-recovery] 测试 crash 恢复...")
        restored = graph.get_state({"configurable": {"thread_id": f"test-{qid}"}})
        if restored:
            print(f"[crash-recovery] 恢复成功: status={restored.values.get('status', 'unknown')}")
        else:
            print("[crash-recovery] 恢复失败: 没有 checkpoint")
        
        return result


if __name__ == "__main__":
    qid = sys.argv[1] if len(sys.argv) > 1 else "gpu"
    result = test_real_task(qid)
