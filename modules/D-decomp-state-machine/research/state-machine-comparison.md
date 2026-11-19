# 状态机对比：PFB vs LangGraph

## 执行过程

### PFB (s5_state_machine.py)

**运行**: `sm-gpu-r1` (2026-11-18 13:05)

**状态轨迹**:
```
初始 → decomposing → decomposed (5 个 L1 节点)
     → 逐层分解 (L2, L3...)
     → 搜索 (arXiv/GitHub/ego-browser)
     → 校验 (verified/degraded/fail)
     → 质询 (challenge)
     → rework (4 次返工)
     → 最终状态: rework (未完成)
```

**节点分布**:
- 总节点: 28
- verified: 19 (68%)
- degraded: 4 (14%)
- pending: 5 (18%)

**Rework 事件** (4 次):
1. N25: LLM推理吞吐量与显存带宽的线性映射关系 — 数值计算错误 (RTX 4090 带宽 1008 GB/s, A100 2039 GB/s)
2. N26: 多卡PCIe互联对KV Cache同步延迟的影响 — 经验性断言缺乏来源
3. N27: Qwen3-27B FP8精度基准测试 — 来源讨论的是 Qwen3.8-27B (非 Qwen3-27B)
4. N28: W4A16精度质量退化阈值 — 具体数值缺乏来源支持

**特点**:
- 目标函数驱动 (5 个因子: Feasibility_Coverage, TCO_Accuracy, Quality_Justification, Conditionality, Source_Transparency)
- 质询机制 (challenge log)
- 返工机制 (rework events)
- 矛盾检测 (contradiction events)
- 网络降级检测 (network_degraded)

### LangGraph (langgraph-real-test.py)

**运行**: 2026-11-18 (刚完成)

**状态轨迹** (24 个 checkpoint):
```
Step 0:  decomposing → decomposed (30 节点)
Step 1:  searched
Step 2:  validated (30/30)
Step 3:  completed
Step 4:  (input, 新一轮)
Step 5:  decomposing → decomposed (31 节点)
Step 6:  searched
Step 7:  validated (31/31)
Step 8:  completed
Step 9:  (input, 新一轮)
Step 10: decomposing → decomposed (21 节点)
Step 11: (input, 中断)
Step 12: decomposing → decomposed (40 节点)
Step 13: (input, 中断)
Step 14: decomposing → decomposed (60 节点)
Step 15: searched
Step 16: validated (60/60)
Step 17: completed
```

**节点分布**:
- 总节点: 60
- verified: 8 (13%)
- degraded: 52 (87%)

**特点**:
- 固定管线: decompose → search → validate → complete
- 无质询机制
- 无返工机制
- 无矛盾检测
- 无目标函数
- 多轮运行 (5 轮, 节点数 30→31→21→40→60)

## 对比

| 指标 | PFB | LangGraph |
|------|-----|-----------|
| 节点数 | 28 | 60 |
| verified | 19 (68%) | 8 (13%) |
| degraded | 4 (14%) | 52 (87%) |
| pending | 5 (18%) | 0 |
| 状态 | rework (未完成) | completed |
| 质询 | 0 | 无机制 |
| 返工 | 4 | 无机制 |
| 矛盾检测 | 0 | 无机制 |
| 目标函数 | 5 因子 | 无 |
| 运行时间 | ~30 分钟 | ~2 分钟 |

## 关键差异

### 1. 分解粒度

**PFB**: 28 节点，L1→L2→L3 逐层分解，每个节点有明确的 claim + source + level
**LangGraph**: 60 节点，扁平分解，节点之间无层级关系

**分析**: PFB 的层级分解更结构化，但节点数少；LangGraph 节点多但粒度粗。

### 2. 验证质量

**PFB**: 68% verified，14% degraded，18% pending
**LangGraph**: 13% verified，87% degraded

**分析**: LangGraph 的 degraded 比例极高 (87%)，说明搜索质量差或验证标准过严。PFB 的 verified 比例高得多。

### 3. 质询与返工

**PFB**: 4 次 rework，每次都有明确的 reason (数值错误、来源不匹配、缺乏支持)
**LangGraph**: 无质询机制，无返工机制

**分析**: PFB 的质询机制能捕获具体错误 (如 N25 的带宽数值错误)，LangGraph 无法捕获这类错误。

### 4. 运行时间

**PFB**: ~30 分钟 (包含搜索、校验、质询、返工)
**LangGraph**: ~2 分钟 (固定管线，无质询)

**分析**: LangGraph 快 15 倍，但质量差 (verified 13% vs 68%)。

## 结论

**PFB 优势**:
- 验证质量高 (68% verified vs 13%)
- 质询机制能捕获具体错误
- 返工机制能修复错误
- 目标函数驱动，有明确的质量标准

**LangGraph 优势**:
- 运行速度快 (2 分钟 vs 30 分钟)
- 节点数多 (60 vs 28)，覆盖面广
- 固定管线，易于理解和调试

**建议**:
- 如果追求质量 → 用 PFB
- 如果追求速度 → 用 LangGraph
- 如果追求平衡 → 用 PFB 的质询机制 + LangGraph 的固定管线
