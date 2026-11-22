# 0.5184 Run 解剖（gpu_budget150_r3）

# origin: ai
# 日期: 2026-11-22 | 数据源: checkpoints/archive/budget-300-r1-20261122-114620/runs-s5-sm-gpu.json（错位映射，已验证 n_nodes=391 对应 gpu_budget150_r3）
# 目的: K7 计划内"0.5184 run anatomy"——历史最高 depth_score 的 run 为什么高

## 核心发现（按重要性）

### 1. depth_score ≈ 旧 LLM judge 的 rubric 覆盖分，不是树深度

| 变量 | 与 depth_score 的 Pearson r (n=13) |
|---|---|
| 旧 judge cov15（15 点 rubric 0/1 覆盖） | **0.861** |
| 答案长度（字符） | 0.351 |
| 节点数 | 0.228 |
| 树结构代理（L4 占比） | 0.334 |
| verified 占比 | 0.268 |
| quotient 边占比 | -0.118 |

depth_score 来自 judge_v2_depth（k·ln(k+1) 加权的 LLM 打分），与同族旧 judge 的
15 点 rubric coverage 高度共线（0.861）。**K7 Pareto 的"质量轴"实际是旧 LLM
judge 的分数**，不是独立于 judge 的树结构度量。

### 2. 150_r3 不是"结构特别深"，是旧 judge 打分最高

- 全场唯一 cov15 > 0.33 的 run（0.333 = 5/15 点）
- 结构并不突出：391 节点 / L4 276 / verified 180 / maxD=4，与 300_r3
  （381 节点 / L4 249 / verified 165 / maxD=4，depth 0.3516 全场最低）几乎同构
- 同构对 150_r3 vs 300_r3：结构距离小，depth Δ=0.167 —— 比预算档间差异
  （~0.05-0.09）大 2-3 倍
- 解释：synth 答案质量 / 旧 judge 判定的 run 间方差 >> 树结构差异

### 3. 与新 embedding judge 零相关（J6 首跑，n=13）

- 旧 cov15 vs 新 cov16（embedding, 16 gold 单元）: Spearman = -0.122
- depth_score vs 新 cov16: Spearman = 0.036
- 旧 judge 测"答案文本是否覆盖 rubric 点"（≈长度+质量的混合代理）
- 新 judge 测"输出树节点是否文本命中 gold 单元"（召回高、精度低，0.65 阈值松）
- 两者测不同构念 → 互补不冗余；任何单一 judge 都不足以当 K7 质量轴

### 4. 150_r3 树结构事实（备查）

- 391 节点 = L1×5 + L2×23 + L3×87 + L4×276（无 L5，max_depth=4 生效）
- 3 轮: r1 28 节点(gain 0.98) → r2 115(0.901) → r3 391(0.887)
- status: verified 180 / degraded 188 / pending 23
- edge_type: cartesian 337 / quotient 54
- 17 个根节点（N1-N5 初始 + 后续轮新增 N34/35/37/38/137/138/139/413-417）
- 关键路径（N1 起）: 可行性边界 → BF16 显存 54GB → 27.1B 精确参数量 → FFN 参数量公式
  （深度 4，纯数值精化链，无 L5）

## 对 K7 Pareto 的直接影响

1. **质量轴声明必须改**：k7_pareto.py 的 depth 轴 = 旧 LLM judge 分（与 cov15
   r=0.861），不是结构度量。报告里必须标注"质量轴 = 同族 LLM judge，存在
   self-judge 偏差"。
2. **run 间方差主因 = synth 答案质量 + judge 判定**，不是树结构。结构代理
   与 depth 的 r ≤ 0.334，解释不了 0.167 的同构对差异。
3. **新 embedding judge 不能替代 depth 轴**（零相关），只能作独立第二构念
   （gold 单元命中率）并行报告。
4. 0.5184 这个"历史最高"在换 judge 后可能不成立——它是旧 judge 尺度下的最高。

## 局限

- n=13（719_r2/r3 未完成），相关系数置信区间宽
- 旧 judge 15 点 rubric 与 depth_score 同源（同一次 LLM 调用的不同字段），
  0.861 部分来自同源共线，不完全是独立验证
- 树结构代理只有 3 个维度（L4/verified/quotient 占比），未穷尽结构自由度
