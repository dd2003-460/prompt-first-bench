# S5 Pipeline 完整规格（2026-11-18）

来源：`s5_pipeline.py`（1325 行）+ `s5_state_machine.py`（1854 行）
状态机：`langgraph-pfb-full.py`（617 行，模块化版）

## 节点与转移

| 节点 | 函数 | 输入 | 输出 |
|------|------|------|------|
| probe | `probe()` | question | 网络可达性 + 初始状态 |
| decompose_l1 | `decompose_l1()` | question | L1 骨架（3-7 个正交维度） |
| decompose | `decompose()` | L1 节点 | L2/L3 子节点（逐层展开） |
| verify | `verify()` | 当前层节点 + 来源 | verified/degraded/failed 标记 |
| rework | `rework()` | failed 节点 | 换角度重新拆解（≤max_rework 次） |
| contradictions | `contradictions()` | 全树节点 | 矛盾对列表 |
| checkpoint | `checkpoint()` | 全树 | S_α 计算 + 停止判定 |
| stop | `stop()` | S_α + 轮次 | 最终答案（P4_SYNTHESIZE） |

## 转移条件

```
probe → decompose_l1（网络可达）
decompose_l1 → decompose
decompose → verify（当前层展开完）
verify → rework（verified_rate < 0.85）
verify → contradictions（verified_rate ≥ 0.85）
rework → decompose（换角度后重新展开）
contradictions → checkpoint（矛盾扫描完）
checkpoint → decompose（未收敛，继续下一轮）
checkpoint → stop（收敛：连续 stop_rounds 轮 gain < threshold）
```

## 完整 Prompt 清单

| Prompt | 行号 | 用途 | 关键约束 |
|--------|------|------|----------|
| P1_L1_SKELETON | 63 | L1 骨架 | 先估目标函数→导出 3-7 个正交维度；禁止下钻到具体数值 |
| P1_DECOMPOSE | 88 | 逐层分解 | 终点导向；source 标记（given/knowledge/search）；排除结论必须继续展开 |
| P15A_DIMENSIONS | 161 | 维度列表 | 只看问题文本；4-8 个正交维度 |
| P15B_GAP_FILL | 173 | 覆盖度补全 | ≥2 节点=已覆盖；0-1 定性=缺失需补 |
| P3_VERIFY | 192 | 事实核验 | 三步：反方质询→逻辑校验→外部核验 |
| P4_SYNTHESIZE | 229 | 综合推理 | 定量优先；溯源标注（[已核验]/[推导]/[凭记忆]）；口径分离 |
| P1_L1_TEXT | 780 | L1 文本模式 | objective_mode="text" 时用 |
| P1_L1_MINIMAL | 808 | L1 极简模式 | objective_mode="minimal" 时用 |
| P1_L1_METHOD | 831 | L1 方法模式 | objective_mode="method" 时用 |
| P1_L1_METHOD_CHALLENGE | 854 | L1 方法+质询 | objective_mode="method_challenge" 时用 |
| P1H_INDEX | 881 | 索引 | 辅助 |
| EDGE_TYPE_PROMPT | 230 | 边分类 | cartesian/quotient 判定 |
| EDGE_PREDICT_PROMPT | 251 | 边预判 | child_claims 为空时概念结构预判 |

## 核验方法（P3_VERIFY 三步）

1. **反方质询**：扮演反对者，找最强攻击点（数值量级？口径混淆？相关当因果？来源不可靠？）
2. **逻辑校验**：量纲/量级合理？内部矛盾？回应攻击点
3. **外部核验**：来源相关性→支持强度（直接/间接/无关/矛盾）

### 判定规则

| 状态 | 条件 |
|------|------|
| verified | 逻辑自洽 + (a) ≥1 来源直接支持 / (b) 第一性原理可推出且无矛盾 / (c) ≥2 独立来源一致 |
| degraded | 逻辑自洽但仅 1 个间接来源→保留但降级定性 |
| failed | 与来源明确矛盾 或 硬逻辑错误（量纲错/内部矛盾） |

### 特殊条款

- **经验事实排除**：硬件规格/市场价格/版本号等经验事实，仅逻辑自洽无来源→degraded（不适用条件 b）
- **公式/推导豁免**：含数学符号的推导类节点，逻辑自洽+量纲合理即 verified（不要求来源直接支持）
- **given/knowledge 豁免**：逻辑自洽即 verified，不引用经验事实排除条款

## 通过/返工条件

| 条件 | 阈值 | 动作 |
|------|------|------|
| 单批 verified 率 | < 0.85（verify_threshold） | 触发 rework |
| rework 次数 | ≤ 2（max_rework） | 超过则接受 degraded 继续 |
| 全局收敛 | 连续 2 轮（stop_rounds）gain < 0.50 | 停止，进 P4 综合 |
| 节点硬顶 | 150（max_nodes） | 强制停止 |
| 深度硬顶 | 4（max_depth） | 不再展开 |
| 单父子上限 | 8（max_kids_per_parent） | 超出不再添加 |
| 贡献剪枝 | 边际贡献 < 0.10（contribution_threshold） | 不展开该子项 |

## 目标函数

S_α = recall × precision 型（F_β, β=0.5 偏 precision）
- 结构分：层级贡献（L1 < L2 < L3）
- 冗余惩罚：β=3.0 × full-pair mean Jaccard
- 不确定度：剪枝判据 = mean + λ·std < θ（λ=1.0, stop_std_max=0.06）

## langgraph 模块化架构（langgraph-pfb-full.py）

```
build_graph():
  probe → decompose_l1 → decompose → verify → [rework|contradictions] → checkpoint → [decompose|stop]

route_after_probe(state) → "decompose_l1" | "stop"
route_after_checkpoint(state) → "decompose" | "stop"
```

每个节点是独立函数，接收 `PFBState`（TypedDict），返回 state 更新 dict。
主函数 `main()` 只调 `graph.invoke(initial_state)`，不做任何业务逻辑。
