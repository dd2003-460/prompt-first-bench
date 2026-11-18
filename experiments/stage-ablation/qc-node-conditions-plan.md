# 质检节点条件 — 完整规划

> 成璐 2026-11-18 指令：把质检做成 node 条件，分解里加入 4 个条件 + 信息搜索 2 个条件。
> 本文档是 cc 的执行对照表，每个节点/条件有明确定义、判据、验收标准。

## 一、节点与条件总览

### 分解质检（4 个，在 _decompose_layer 返回 kids 后、judge_necessary_batch 之前执行）

| # | 条件名 | 函数 | 判据 | 动作 | 验收标准 |
|---|--------|------|------|------|----------|
| Q1 | 可分解性 | `classify_edge`（已有） | contribution < threshold(0.10) 且非 high_var | 父节点标 degraded，不展开 | rounds_log 有 `n_contrib_pruned` |
| Q2 | 正交性 | `_check_orthogonality`（**新增**） | 同父节点下子节点两两 n-gram 重叠 > 0.5 → LLM 判"能否推出" | 能推出的子节点丢弃 | rounds_log 有 `n_orthogonal_dropped` |
| Q3 | 完备性 | `gap_check`（已有，s5_pipeline.py:323） | 维度枚举后补缺失维度 | 补充节点加入树 | rounds_log 有 `n_gap_added` |
| Q4 | 可压缩复杂度 | `_check_compression`（**新增**） | marginal_gain(子节点 claims, [父节点 claim]) < 0.3 | 丢弃所有子节点，父节点标 degraded | rounds_log 有 `n_compression_dropped` |

### 信息校验（2 个，在 VERIFY 阶段执行）

| # | 条件名 | 函数 | 判据 | 动作 | 验收标准 |
|---|--------|------|------|------|----------|
| Q5 | 矛盾校验 | `_scan_contradictions`（已有，D33） | verified 节点两两 LLM 判"数值/定义是否矛盾" | 矛盾对记入 contradiction_events，喂回下一轮 decompose | rounds_log 有 `contradictions_found` |
| Q6 | 信息校验 | `verify_node`（已有，s5_pipeline.py:410） | 三步：反方质询→逻辑校验→外部核验 | status ∈ {verified, degraded, failed}；failed → rework | rounds_log 有 `verified` 计数 |

### 停止/退出条件（已有，run() 方法 line 1100-1250）

| 条件 | 判据 | 位置 |
|------|------|------|
| R1 饱和 | 本轮新增节点 = 0 | line 1218 |
| R3 停滞 | 连续 N 轮 low-gain（necessary 通过率 < 0.3） | line 1210 |
| R4 硬上限 | max_nodes=150 或 max_depth=4 | line 1070-1076 |

## 二、新增函数规格

### _check_orthogonality（Q2）

```python
def _check_orthogonality(self, kids: list[NodeRecord], parent: NodeRecord) -> list[NodeRecord]:
    """正交性裁决：同父节点下子节点两两判'能否推出'。
    
    步骤:
    1. 对 kids 两两算 _ngram_overlap(claim_a, claim_b)
    2. 重叠 > 0.5 的对，收集起来
    3. 一次 LLM 调用（批量版，类似 judge_necessary_batch 的紧凑行格式）:
       prompt = "对下面每对子节点，判断 B 能否从 A 推出（即 B 的信息是否已被 A 覆盖）。
                格式: \"pair\":idx,\"derivable\":true/false"
       max_tokens = min(200 * len(pairs) + 200, 4096)  # E11 上限
       temperature = 0.0
    4. derivable=true 的 B → 丢弃，记入 self.orthogonal_dropped
    5. 返回存活 kids
    
    防泄漏: prompt 不得包含题目原文关键实体（过 _check_output_leak）
    带 _perturb()
    """
```

**LLM prompt 模板**（防泄漏：只用 claim，不喂题目）：
```
你是正交性审查员。下面是一组研究子节点（同一父节点下的分解结果）。
对每对子节点，判断第二个能否从第一个推出（即第二个的信息是否已被第一个覆盖）。
注意：口径不同不算可推出（如"按字节"vs"按请求"）；单位换算等价不算。
只报真可推出的对，没有就返回空。

【子节点列表】
[0] {claim_0}
[1] {claim_1}
...

【待判定对】
pair 0: A=[i] B=[j]
pair 1: A=[k] B=[m]
...

只输出这些行，不要其他文字:
"pair":0,"derivable":false
"pair":1,"derivable":true
```

### _check_compression（Q4）

```python
def _check_compression(self, kids: list[NodeRecord], parent: NodeRecord) -> tuple[bool, float]:
    """可压缩复杂度裁决：子节点集合相对父节点是否有信息增益。
    
    步骤:
    1. gain = marginal_gain([k.claim for k in kids], [parent.claim])
       （复用 line 145 的 marginal_gain，n-gram Jaccard）
    2. 如果 gain < 0.3:
       - 返回 (False, gain)  # 膨胀，应丢弃
    3. 否则:
       - 返回 (True, gain)   # 正常分解
    
    这是防 Goodhart 的核心：v17 爆炸到 1930 节点就是 S_α 单调增模型拼命拆。
    如果拆出来的子节点集合相对父节点几乎没有新信息（gain < 0.3），
    说明是冗余膨胀不是分解，S_α 不应该涨。
    """
```

**阈值 0.3 的依据**：marginal_gain 范围 [0,1]，1 = 全新，0 = 完全重复。
0.3 意味着"子节点集合至少要有 30% 的信息是父节点没有的"。
这个值 [待标定]——cc 跑完 3 道题后看 gain 分布再调。

## 三、run() 方法修改点

在 `run()` 方法（line 952）里，`_decompose_layer` 返回 kids 后（约 line 1090），
`judge_necessary_batch` 之前（约 line 1130），插入：

```python
# ── Q2: 正交性裁决 ──
for p in batch:
    p_kids = [k for k in kids if p.id in (k.parent_ids or [])]
    if len(p_kids) >= 2:
        kids = [k for k in kids if k not in p_kids] + self._check_orthogonality(p_kids, p)

# ── Q4: 可压缩复杂度裁决 ──
for p in batch:
    p_kids = [k for k in kids if p.id in (k.parent_ids or [])]
    if p_kids:
        ok, gain = self._check_compression(p_kids, p)
        if not ok:
            kids = [k for k in kids if k not in p_kids]
            p.status = "degraded"
            self.compression_dropped.append({"parent": p.id, "gain": gain, "n_kids": len(p_kids)})
```

rounds_log 追加字段：
```python
"n_orthogonal_dropped": len(self.orthogonal_dropped) - prev_orth,
"n_compression_dropped": len(self.compression_dropped) - prev_comp,
```

## 四、LangGraph 侧对齐

文件：`/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation/langgraph-pfb-conditions.py`

当前 LangGraph 的条件边（line 350-432）只用了：
- `verify_threshold=0.85`（Q6 的一部分）
- `stop_rounds=2`（R3 的一部分）
- `max_nodes=150, max_depth=4`（R4）

**缺的**：Q1（contribution 剪枝）、Q2（正交性）、Q3（gap_check 已有但没在条件边里用）、Q4（可压缩复杂度）、Q5（矛盾扫描）

**改法**：
1. `decompose_node` 里，调 `pfb_decompose` 后，加 Q1+Q2+Q4 裁决（import s5_state_machine 的函数）
2. `validate_node` 里，加 Q5 矛盾扫描（import `_scan_contradictions` 的逻辑）
3. `after_decompose` 条件边：检查 Q4 是否触发（膨胀 → 不继续 decompose，直接 complete）
4. `after_validate` 条件边：检查 Q5 是否有未修复矛盾（有 → rework）

**不重写逻辑**——全部 import s5_state_machine 的函数，LangGraph 只做状态路由。

## 五、对比测试规格

### 题目
s8b_pilot.py QUESTIONS（line 40）里的 3 道：
- `nat`: 自然语言处理相关
- `soc`: 社会/经济相关
- `gpu`: GPU 硬件相关

每题 1 rep，共 3 题 × 2 臂 = 6 个 run。

### 臂
- **臂 A**: pfb 状态机（s5_state_machine.py，补完 Q2+Q4 后）
- **臂 B**: LangGraph 状态机（langgraph-pfb-conditions.py，条件边对齐 pfb 后）

### 指标
| 指标 | 来源 | 说明 |
|------|------|------|
| coverage | s8b_pilot.judge（line 157） | gold 要点覆盖率，与 S0-A4 同口径 |
| depth_score | judge_v2_depth.score_run（line 408） | 深度连续分，k·ln(k+1) 加权 |
| verified 率 | rounds_log.verified / n_nodes | 核验通过率 |
| 节点数 | len(nodes) | 最终树大小 |
| wall_time | time.time() - t0 | 总耗时（秒） |
| n_orthogonal_dropped | rounds_log 累计 | Q2 丢弃数 |
| n_compression_dropped | rounds_log 累计 | Q4 丢弃数 |
| contradictions_found | rounds_log 累计 | Q5 检出数 |

### 产出
- `runs-qc-compare/` 目录
- 每题每臂一个 JSON：`{arm}-{qid}-r1.json`
- 汇总表格：`runs-qc-compare/summary.md`（3 题 × 2 臂的指标对比）

## 六、约束

1. **8787 端点**：http://127.0.0.1:8787/v1/chat/completions, qwen3.8-27b, max_tokens ≤ 4096（E11）
2. **防泄漏**：新 prompt 过 `_check_output_leak`（s5_state_machine.py line 45-107 的 extract_entities + leak_check）
3. **_perturb()**：每个 LLM 调用带（s5_pipeline.py line 264）
4. **LangGraph 跑不通**：只跑臂 A，结果里标注"臂 B 未跑通，原因: ..."
5. **阈值 [待标定]**：Q4 的 0.3 是初始值，跑完看 gain 分布再调

## 七、执行顺序

1. 读 s5_state_machine.py 全文（重点：run() line 952-1250, _decompose_layer line 543-640, ObjectiveConfig line 107-134）
2. 读 s5_pipeline.py 的 gap_check（line 323）和 verify_node（line 410）
3. 读 langgraph-pfb-conditions.py 全文
4. 写 _check_orthogonality + _check_compression 到 s5_state_machine.py
5. 改 run() 方法，插入 Q2+Q4 调用
6. 改 langgraph-pfb-conditions.py，对齐 Q1-Q5
7. 跑臂 A（3 题 × 1 rep）
8. 跑臂 B（3 题 × 1 rep）
9. 写 summary.md
