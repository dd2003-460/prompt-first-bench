# E 块设计 — 自写目标函数进回路 + contribution 方差感知

> origin: ai (成璐 2026-11-12 追问触发；decomp 见 tasks/T53-decomp-state-machine.md §E)
> 状态：设计方案 v1，未实现。实现前需 smoke test 验证 EA1/EA2。
> 关联代码：s5_state_machine.py classify_edge (line ~250) / l1_frontier 循环 (line ~708) / ObjectiveConfig (line ~98)

## 问题定位（来源①，grep 实证）

当前 S5 的"目标函数"有三个脱节：

1. **Decision 19 objective 是装饰品**：模型 r1 自估一个 `Final_Score = Feasibility_Coverage × Recommendation_Conditionality × ...` 公式，随 ckpt 落盘（line 390/603/1032），但 `classify_edge`/`marginal_gain`/`_verify_batch` 全不读它。它不驱动任何展开/核验/停止决策。
2. **真正驱动力是两个拍脑袋阈值**：`gain_threshold=0.50`（n-gram Jaccard 边际增益）+ `contribution_threshold=0.10`（LLM 单点估 0-1）。
3. **contribution 无方差**：`classify_edge` 单次 LLM 调用 temperature=0.0 返回一个点值（line 255/274），全文件无 std/variance/多采样逻辑。"var" 仅以 `high_var` 布尔 flag 存在（定性二元，防黑天鹅被剪）。

成璐的判断精确命中："目标函数看起来确实可以激活，但我们几乎是拍脑袋随机赶着 AI"。

## 设计目标

| 子项 | 现状 | 目标 |
|------|------|------|
| E1 | objective 不进回路 | objective 分解成 per-edge 权重，实际影响 contribution 计算 |
| E2 | contribution 单点估计 | n 次采样（temp>0）取 mean±std，剪枝用 `mean - λ·std < θ` |
| E4 | J_stop 只看 gain 均值 | 加入 gain 方差项：方差大 = 还在探索，不该停 |

## E2 最小实现方案（先做这个，成本最低、收益最直接）

### 改动点 1：ObjectiveConfig 加参数

```python
# line ~98 ObjectiveConfig 内新增
contrib_samples: int = 5          # 每条 edge 采样次数（1 = 退化为现状）
contrib_temperature: float = 0.7  # 采样温度（0 = 退化为现状单点）
lambda_uncertainty: float = 1.0   # 不确定度折扣系数：判据 = mean - λ·std < θ
```

### 改动点 2：classify_edge 改成多采样

当前签名 `classify_edge(parent_claim, child_claims, cfg) -> (edge_type, reason, contribution, high_var)`。

改成内部采样 n 次，返回 contribution 的分布统计：

```python
def classify_edge(parent_claim, child_claims, cfg):
    """返回 (edge_type, reason, contrib_mean, contrib_std, high_var_any)"""
    samples = []
    for i in range(cfg.contrib_samples):
        # 每次调用独立 seed（None = 随机），temperature=cfg.contrib_temperature
        out, _ = call_llm(prompt, max_tokens=300, temperature=cfg.contrib_temperature, retries=2)
        contrib_i = parse_contrib(out)      # 现有正则解析
        high_var_i = parse_high_var(out)
        samples.append((contrib_i, high_var_i))
    contribs = [s[0] for s in samples]
    contrib_mean = sum(contribs) / len(contribs)
    contrib_std = (sum((c - contrib_mean)**2 for c in contribs) / len(contribs)) ** 0.5
    high_var_any = any(s[1] for s in samples)   # 任一样本标 high_var → 豁免
    # edge_type/reason 取众数（或第一次的值，temp>0 时可能漂移）
    return edge_type_mode, reason_first, contrib_mean, contrib_std, high_var_any
```

**成本**：每条 edge 从 1 次 LLM 调用变 5 次。L1 frontier 通常 6-10 个节点 → 每轮多 20-40 次调用。本地 27b proxy 下约 +2-4 min/轮。可接受（换 variance 信息）。

**退化安全**：`contrib_samples=1, contrib_temperature=0.0` 时行为与现状完全一致（std=0，判据退化为 `mean < θ`）。bench 扫参时这是 baseline 臂。

### 改动点 3：剪枝判据改成不确定度感知

当前（line ~716）：
```python
if contrib < self.cfg.contribution_threshold and not high_var:
```

改成：
```python
effective = contrib_mean - cfg.lambda_uncertainty * contrib_std
if effective < cfg.contribution_threshold and not high_var_any:
    # 剪枝
```

**语义**：`contrib_mean - λ·std` 是"考虑不确定度后的保守贡献估计"。方差大 → std 大 → effective 小 → 更容易被剪？不对——这里方向反了。

**修正**：要的是"不确定就保留，防误剪"，所以应该是：
```python
# 方差大 = 不确定 = 保守地保留（不剪）
# 只有当"即使按最乐观解释（mean + std）也低于阈值"时才剪
pessimistic_for_prune = contrib_mean - cfg.lambda_uncertainty * contrib_std
if pessimistic_for_prune < cfg.contribution_threshold and not high_var_any:
    prune
```

等等，再想清楚：我们想避免的是"LLM 这次随口估了 0.08（< 0.10）就把真有用的分支剪了"。如果多次采样 std 大，说明 LLM 自己也不确定——这时候**不该**因为单次低值就剪。正确判据：

```python
# 剪枝条件：所有样本都低于阈值（即 max 样本仍 < θ）→ 才敢剪
# 等价于：mean + std < θ（近似，假设正态）
optimistic = contrib_mean + cfg.lambda_uncertainty * contrib_std
if optimistic < cfg.contribution_threshold and not high_var_any:
    prune  # 即使最乐观的估计都不够 → 真的没用
```

**最终判据**：`contrib_mean + λ·std < contribution_threshold` → 剪。λ=1 时 ≈ "95% 置信上界仍低于阈值才剪"。λ 越大越保守（越难剪）。

### 改动点 4：调用点适配

l1_frontier 循环（line ~708）和三边复核（line ~733）两处调用点，解包从 4 元组变 5 元组，存 `p.contrib_mean`/`p.contrib_std`（NodeRecord 加两个可选字段，向后兼容默认 None）。

## E1 设计（objective 进回路）— 比 E2 复杂，第二步做

核心问题：Decision 19 的 objective 是一个**全局公式**（Final_Score = 因子1 × 因子2 × ...），而 contribution 是**per-edge 局部量**。怎么桥接？

方案 A（推荐）：**objective 因子 → edge 相关度映射**
- r1 产出 objective 后，对每个 L1 edge 问一次 LLM："这个 edge 的维度对应 objective 的哪个因子？相关度 0-1？"
- contribution_effective = base_contribution × (1 + α_obj × obj_relevance)
- obj_relevance 高 → 该 edge 在目标里权重高 → 即使 base_contribution 偏低也保留
- 这样 objective 真的影响了剪枝：跟目标相关的分支不容易被剪掉

方案 B（更激进）：**objective 直接当 contribution 的来源**
- 不再单独调 classify_edge 估 contribution，而是让 LLM 直接对着 objective 公式估"删掉这个 edge 后 Final_Score 降多少"
- 风险：LLM 对抽象公式的数值估计更不可靠，方差更大
- 适合 E3（grounding 校验）通过后再接

**推荐路径**：先 E2（纯加方差，不动 objective）→ smoke test 看 EA2 → 再 E1 方案 A（objective 当权重调制）→ E3 grounding 校验 → 最后考虑 E1 方案 B。

## E4 设计（var-aware 停止判据）

当前 J_stop：`连续 stop_rounds 轮 marginal_gain < gain_threshold → 停`。

改成：
```python
# 每轮记录 marginal_gain 的均值和方差（跨该轮所有新 edge）
# 停止条件：mean_gain < ε 且 std_gain < σ_max（方差小 = 已收敛，不是还在探索）
if recent_gains_mean < cfg.gain_threshold and recent_gains_std < cfg.stop_std_max:
    stop_count += 1
else:
    stop_count = 0
if stop_count >= cfg.stop_rounds:
    STOP
```

`stop_std_max` 初值 0.15（需 bench 标定）。方差大 → 还有新维度在冒出来 → 不停。

## 验收标准对接

| AC | 怎么验 |
|----|--------|
| EA1 | objective 进回路后跑 GPU 单题，对比"objective 装饰"版本的节点数/正交维度——有可测差异 = 真的在驱动 |
| EA2 | drb-2 那批 degraded 节点用 E2 重跑 classify_edge，看"方差大的保留率"是否上升（误剪率下降） |
| EA3 | self-written objective 用 ≥1 道 gold 题反向校验：已知优劣的答案集，公式给出的排序是否正确 |

## 风险与回滚

- **成本 ×5**：contrib_samples=5 时每 edge 5 次 LLM 调用。若太慢，降到 3（std 估计精度略降但仍有效）。
- **temp>0 引入噪声**：edge_type 可能漂移（cartesian↔quotient）。缓解：edge_type 取众数，contribution 才用分布。
- **回滚**：`contrib_samples=1, contrib_temperature=0.0, lambda_uncertainty=0.0` 三参数归零 = 完全退回现状。git revert 整个 commit 也行。

## 下一步（本回合不做，留待执行）

1. 实现 E2 改动点 1-4（~40 行 diff），commit。
2. smoke test：GPU 单题跑 1 轮，对比 contrib_samples=1 vs 5 的剪枝决策差异。
3. 结果落盘 `experiments/stage-ablation/runs/e2-variance-smoke.json`。
4. EA2 验证：drb-2 degraded 节点重跑。
5. E1 方案 A 设计细化 + 实现。
6. E3 arena 交叉核验（等 T-PR-15 会话空闲后合并派发）。