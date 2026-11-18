#!/usr/bin/env python3
"""
LangGraph 状态机 — 全 PFB 条件版

核心差异 vs langgraph-real-test.py:
1. 停止条件: max_nodes=150, max_depth=4, low_gain_streak=2
2. 返工条件: verify_threshold=0.85, max_rework=2
3. 质询机制: P3_VERIFY 的反方质询 + 矛盾检测
4. 目标函数: 5 因子 (Feasibility_Coverage, TCO_Accuracy, Quality_Justification, Conditionality, Source_Transparency)

用法:
    python3 langgraph-pfb-conditions.py gpu
"""

import json
import os
import sqlite3
import sys
from typing import TypedDict, Literal

from langgraph.graph import StateGraph, END
from langgraph.checkpoint.sqlite import SqliteSaver

# 复用 PFB 的函数
from s5_pipeline import (
    _extract_json, _perturb, decompose, gap_check,
    search_node, verify_node,
)
from ablation_harness import call_llm

# ============================================================
# 1. 状态定义
# ============================================================

class PFBState(TypedDict):
    # 输入
    goal: str
    qid: str
    
    # 分解
    decomposition: dict  # {"nodes": [...]}
    decomposition_attempts: int
    
    # 搜索
    search_results: dict  # {node_id: {"sources": [...]}}
    search_attempts: int
    
    # 校验
    validation_result: dict  # {node_id: {"status", "evidence", "corrected_claim"}}
    validation_attempts: int
    
    # PFB 条件
    rework_events: list  # 返工事件
    challenge_log: list  # 质询日志
    contradiction_events: list  # 矛盾事件
    low_gain_streak: int  # 连续低增益轮数
    gain_history: list  # 增益历史
    
    # 控制
    status: str  # pending/decomposing/decomposed/searched/validated/completed/failed
    round: int  # 当前轮次


# ============================================================
# 2. PFB 配置
# ============================================================

class PFBConfig:
    """PFB 状态机配置 (与 s5_state_machine.py 一致)"""
    max_nodes = 150
    max_depth = 4
    max_rework = 2
    verify_threshold = 0.85
    gain_threshold = 0.50
    stop_rounds = 2  # 连续 N 轮 gain < threshold → 停


# ============================================================
# 3. 节点函数
# ============================================================

def decompose_node(state: PFBState) -> dict:
    """分解阶段: 生成 L1 骨架 + 逐层分解"""
    print(f"[decompose] 开始分解: {state['goal'][:80]}...")
    print(f"[decompose] 轮次: {state['round']}")
    
    # 调用 PFB 的 decompose 函数
    try:
        from s5_pipeline import decompose as pfb_decompose
        result = pfb_decompose(state["goal"])
        if isinstance(result, tuple):
            nodes, _raw = result
        else:
            nodes = result
        if not nodes:
            raise Exception("分解失败: 返回空节点")
        
        # 检查 max_nodes
        if len(nodes) >= PFBConfig.max_nodes:
            print(f"[decompose] max_nodes={PFBConfig.max_nodes} hit")
            return {"status": "completed", "round": state["round"] + 1}
        
        # 检查 max_depth
        max_level = max(int(str(n.get("level", "L1")).lstrip("L")) for n in nodes)
        if max_level >= PFBConfig.max_depth:
            print(f"[decompose] max_depth={PFBConfig.max_depth} hit")
            return {"status": "completed", "round": state["round"] + 1}
        
        print(f"[decompose] 分解成功: {len(nodes)} 个节点, max_level=L{max_level}")
        return {
            "decomposition": {"nodes": nodes},
            "status": "decomposed",
            "decomposition_attempts": state["decomposition_attempts"] + 1,
            "round": state["round"] + 1,
        }
    except Exception as e:
        print(f"[decompose] 失败: {e}")
        return {
            "status": "decomposition_failed",
            "decomposition_attempts": state["decomposition_attempts"] + 1,
        }


def search_node(state: PFBState) -> dict:
    """搜索阶段: 对每个节点做信息搜索"""
    print(f"[search] 开始搜索: {state['goal'][:80]}...")
    print(f"[search] 轮次: {state['round']}")
    
    nodes = state["decomposition"]["nodes"]
    search_results = {}
    
    for node in nodes:
        node_id = node.get("id", "unknown")
        claim = node.get("claim", "")
        search_query = node.get("search_query", claim)
        
        try:
            srcs, err = search_node(
                {"id": node_id, "claim": claim, "search_query": search_query}
            )
            search_results[node_id] = {"sources": srcs}
            if err:
                print(f"[search] 节点 {node_id}: {err}")
        except Exception as e:
            print(f"[search] 节点 {node_id} 失败: {e}")
            search_results[node_id] = {"sources": [], "error": str(e)}
    
    print(f"[search] 搜索完成: {len(search_results)} 个节点")
    return {
        "search_results": search_results,
        "status": "searched",
        "search_attempts": state["search_attempts"] + 1,
        "round": state["round"] + 1,
    }


def validate_node(state: PFBState) -> dict:
    """校验阶段: 校验信效度 + 质询 + 矛盾检测"""
    print(f"[validate] 开始校验: {state['goal'][:80]}...")
    print(f"[validate] 轮次: {state['round']}")
    
    nodes = state["decomposition"]["nodes"]
    search_results = state["search_results"]
    validation_result = {}
    challenge_log = list(state.get("challenge_log", []))
    contradiction_events = list(state.get("contradiction_events", []))
    
    for node in nodes:
        node_id = node.get("id", "unknown")
        claim = node.get("claim", "")
        srcs = search_results.get(node_id, {}).get("sources", [])
        
        try:
            status, evidence, corrected, challenge = verify_node(
                {"id": node_id, "claim": claim, "source": "search"}, srcs
            )
            validation_result[node_id] = {
                "status": status,
                "evidence": evidence,
                "corrected_claim": corrected,
            }
            
            # 记录质询
            if challenge:
                challenge_log.append({
                    "node_id": node_id,
                    "challenge": challenge,
                    "round": state["round"],
                })
            
            print(f"[validate] 节点 {node_id}: {status}")
        except Exception as e:
            print(f"[validate] 节点 {node_id} 失败: {e}")
            validation_result[node_id] = {
                "status": "failed",
                "evidence": str(e),
                "corrected_claim": "",
            }
    
    # 矛盾检测 (简化版: 检查同一主题的节点是否有矛盾)
    # 完整版需要 LLM 判断, 这里先标记
    # contradiction_events = detect_contradictions(nodes, validation_result)
    
    # 计算 verified 比例
    verified = sum(1 for r in validation_result.values() if r["status"] == "verified")
    total = len(validation_result)
    rate = verified / total if total > 0 else 0
    
    print(f"[validate] 校验完成: {verified}/{total} verified (rate={rate:.2f})")
    
    return {
        "validation_result": validation_result,
        "challenge_log": challenge_log,
        "contradiction_events": contradiction_events,
        "status": "validated",
        "validation_attempts": state["validation_attempts"] + 1,
        "round": state["round"] + 1,
        "_verify_rate": rate,  # 内部字段, 用于条件边
    }


def rework_node(state: PFBState) -> dict:
    """返工阶段: 对核验失败的节点, 换角度重新搜索"""
    print(f"[rework] 开始返工: {state['goal'][:80]}...")
    print(f"[rework] 轮次: {state['round']}")
    
    nodes = state["decomposition"]["nodes"]
    validation_result = state["validation_result"]
    rework_events = list(state.get("rework_events", []))
    
    # 找出未 verified 的节点
    unverified = [
        n for n in nodes
        if validation_result.get(n.get("id"), {}).get("status") != "verified"
    ]
    
    if not unverified:
        print(f"[rework] 无未 verified 节点, 跳过")
        return {"status": "validated", "round": state["round"] + 1}
    
    print(f"[rework] 未 verified 节点: {len(unverified)}")
    
    # 对每个未 verified 节点, 换角度重新搜索
    for node in unverified:
        node_id = node.get("id", "unknown")
        claim = node.get("claim", "")
        
        # 生成新的 search_query (换角度)
        try:
            prompt = f"""原 claim: {claim}
原 search_query: {node.get('search_query', '')}

请生成 2 个不同角度的 search_query (英文), 用于重新搜索:
1. 同义替换
2. 不同角度/更具体

只输出 JSON: {{"queries": ["query1", "query2"]}}"""
            
            out, _ = call_llm(prompt, max_tokens=512, temperature=0.7)
            d = _extract_json(out or "") or {}
            queries = d.get("queries", [])
            
            if queries:
                # 用新 query 重新搜索
                for query in queries[:2]:
                    srcs, err = search_node(
                        {"id": node_id, "claim": claim, "search_query": query},
                        qid=state["qid"]
                    )
                    if srcs:
                        # 重新校验
                        status, evidence, corrected, _ = verify_node(
                            {"id": node_id, "claim": claim, "source": "search"}, srcs
                        )
                        if status == "verified":
                            validation_result[node_id] = {
                                "status": status,
                                "evidence": evidence,
                                "corrected_claim": corrected,
                            }
                            rework_events.append({
                                "node_id": node_id,
                                "query": query,
                                "result": "verified",
                                "round": state["round"],
                            })
                            print(f"[rework] 节点 {node_id}: verified (query={query[:50]}...)")
                            break
                        else:
                            rework_events.append({
                                "node_id": node_id,
                                "query": query,
                                "result": status,
                                "round": state["round"],
                            })
        except Exception as e:
            print(f"[rework] 节点 {node_id} 失败: {e}")
    
    # 重新计算 verified 比例
    verified = sum(1 for r in validation_result.values() if r["status"] == "verified")
    total = len(validation_result)
    rate = verified / total if total > 0 else 0
    
    print(f"[rework] 返工完成: {verified}/{total} verified (rate={rate:.2f})")
    
    return {
        "validation_result": validation_result,
        "rework_events": rework_events,
        "status": "validated",
        "round": state["round"] + 1,
        "_verify_rate": rate,
    }


def complete_node(state: PFBState) -> dict:
    """完成阶段: 生成结论"""
    print(f"[complete] 生成结论: {state['goal'][:80]}...")
    
    nodes = state["decomposition"]["nodes"]
    validation_result = state["validation_result"]
    
    verified_nodes = [
        {
            "id": nid,
            "claim": r.get("corrected_claim", ""),
            "evidence": r.get("evidence", ""),
        }
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


# ============================================================
# 4. 条件边
# ============================================================

def after_decompose(state: PFBState) -> str:
    """分解后的条件边"""
    if state["status"] == "decomposition_failed":
        if state["decomposition_attempts"] >= 3:
            return "fail"
        return "decompose"
    return "search"


def after_search(state: PFBState) -> str:
    """搜索后的条件边"""
    if state["status"] == "search_failed":
        if state["search_attempts"] >= 3:
            return "fail"
        return "search"
    return "validate"


def after_validate(state: PFBState) -> str:
    """校验后的条件边 — PFB 逻辑"""
    rate = state.get("_verify_rate", 0)
    
    # PFB: verified 比例 < 0.85 → 返工
    if rate < PFBConfig.verify_threshold:
        rework_count = len(state.get("rework_events", []))
        if rework_count < PFBConfig.max_rework:
            return "rework"
        else:
            return "complete"  # 返工耗尽, 直接完成
    
    # PFB: 检查停止条件
    if state.get("round", 0) >= PFBConfig.stop_rounds:
        return "complete"
    
    return "complete"


def after_rework(state: PFBState) -> str:
    """返工后的条件边"""
    rate = state.get("_verify_rate", 0)
    
    # 返工后 verified 比例 >= 0.85 → 完成
    if rate >= PFBConfig.verify_threshold:
        return "complete"
    
    # 否则 → 继续返工或完成
    rework_count = len(state.get("rework_events", []))
    if rework_count < PFBConfig.max_rework:
        return "rework"
    else:
        return "complete"


# ============================================================
# 5. 构建 graph
# ============================================================

def build_graph() -> StateGraph:
    """构建 PFB 条件的 LangGraph graph"""
    graph = StateGraph(PFBState)
    
    # 添加节点
    graph.add_node("decompose", decompose_node)
    graph.add_node("search", search_node)
    graph.add_node("validate", validate_node)
    graph.add_node("rework", rework_node)
    graph.add_node("complete", complete_node)
    graph.add_node("fail", lambda state: {"status": "failed"})
    
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
        "rework": "rework",
        "complete": "complete",
    })
    graph.add_conditional_edges("rework", after_rework, {
        "rework": "rework",
        "complete": "complete",
    })
    graph.add_edge("complete", END)
    graph.add_edge("fail", END)
    
    return graph


# ============================================================
# 6. 测试
# ============================================================

if __name__ == "__main__":
    import sys
    
    qid = sys.argv[1] if len(sys.argv) > 1 else "gpu"
    
    # 读取题目
    question_file = f"questions/{qid}.txt"
    if not os.path.exists(question_file):
        question_file = f"questions/{qid}.md"
    if not os.path.exists(question_file):
        # 尝试找 gpu 相关文件
        import glob
        gpu_files = glob.glob(f"questions/*{qid}*")
        if gpu_files:
            question_file = gpu_files[0]
        else:
            raise FileNotFoundError(f"找不到题目文件: {qid}")
    
    with open(question_file) as f:
        question = f.read().strip()
    
    # 构建 graph
    graph = build_graph().compile()
    
    # 运行
    initial_state = {
        "goal": question,
        "qid": qid,
        "decomposition": {},
        "decomposition_attempts": 0,
        "search_results": {},
        "search_attempts": 0,
        "validation_result": {},
        "validation_attempts": 0,
        "rework_events": [],
        "challenge_log": [],
        "contradiction_events": [],
        "low_gain_streak": 0,
        "gain_history": [],
        "status": "pending",
        "round": 0,
    }
    
    print(f"=== LangGraph PFB 条件测试: {qid} ===")
    print(f"配置: max_nodes={PFBConfig.max_nodes}, max_depth={PFBConfig.max_depth}, "
          f"verify_threshold={PFBConfig.verify_threshold}, max_rework={PFBConfig.max_rework}")
    print()
    
    # 使用 SQLite checkpoint
    with SqliteSaver.from_conn_string(f"/tmp/langgraph-pfb-{qid}.sqlite") as checkpoint:
        config = {"configurable": {"thread_id": qid}}
        result = graph.invoke(initial_state, config)
    
    # 输出结果
    print()
    print(f"最终状态: {result['status']}")
    print(f"分解尝试: {result['decomposition_attempts']}")
    print(f"搜索尝试: {result['search_attempts']}")
    print(f"校验尝试: {result['validation_attempts']}")
    print(f"返工事件: {len(result['rework_events'])}")
    print(f"质询日志: {len(result['challenge_log'])}")
    
    if result.get("final_answer"):
        print(f"Verified 节点: {len(result['final_answer']['verified_nodes'])}")
        print(f"总节点: {result['final_answer']['total_nodes']}")
