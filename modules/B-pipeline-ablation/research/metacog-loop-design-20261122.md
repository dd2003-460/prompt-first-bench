# 自我认识闭环：断点诊断 + 改进设计（2026-11-22）

> origin: ai · 全局地图"改进层"的设计文档
> 数据: budget-150-r1 gpu run（122 节点, source ① 刚算）

## 断点诊断（post_acc≈0 的根因）

**不是网络问题**（network_degraded=False, 检索全成功），是**质询-修复环全断**：

| 指标 | 值 | 来源 |
|---|---|---|
| search 节点 degraded 占比 | 36/55 ≈ 65% | budget-150-r1 |
| rework 尝试 | 46 节点 × 1 次 | rework_count 分布 |
| rework 救回 verified | **0/46 (fix rate 0%)** | 同上 |
| degraded 原因 top | 无法验证 / 缺具体数值 / 缺针对 Qwen3-27B 的来源 | evidence 正则分类 |

因果链：质询要求"具体数值支持" → 检索到通用来源（无该数值）→ 判 degraded → rework 换角度重搜 → 还是通用来源 → 再 degraded → max_rework=2 耗尽放弃。

## 关键区分（测量层修正）

degraded 里混了两类，语义完全不同：

1. **不可验证（unverifiable）**：来源不含该数值/该模型细节。这不是自我认识的失败——模型标了[待核验]、去查了、查完确认"查不到"，这是**健康的 monitoring**。
2. **矛盾（contradicted）**：来源与 claim 冲突。这才是 myopia 候选（知道有矛盾但修不好）。

现在 metacog_axis 的 post_acc 把两类都算失败 → **测的是核验严格度，不是自我认识**。

## metacog_axis v1.1 修正（机械，不依赖 LLM）

degraded 节点按 evidence 分类：
- 含"矛盾/不符/冲突" → contradicted（真失败）
- 含"无法验证/缺...支持/未找到" → unverifiable（健康缺口）

新指标：
- `healthy_gap_rate` = unverifiable / (unverifiable + contradicted)：查完能分清"查不到"和"查错了"的比例
- `post_acc` 只算 contradicted 为失败（unverifiable 不算）
- 自我认识最低线重定义：(a) 标缺口 + (b) 去查 + (b') 查完分类正确（unverifiable 不被当 verified 硬过，contradicted 触发修复）

## 改进闭环（"造"的部分）

```
测（metacog v1.1）→ 断点定位 → 针对性补 → 重测 → 显著性
```

候选干预（按性价比排，先做 1）：
1. **verify prompt 二分**：质询输出 verified / contradicted / unverifiable 三态（现在只有 verified/degraded 两态）。unverifiable 节点保留 claim + [待核验] 标记，不算失败。改动：verify prompt + status 枚举，~1h。
2. **rework 条件化**：只对 contradicted 触发 rework（现在 degraded 全触发，浪费预算在"查不到"上）。改动：_rework 入口判断，~30min。
3. **定向数值检索**：contradicted 且缺数值时，检索词带具体参数（"Qwen3-27B FP8 量化精度损失"而非泛化）。改动：_rework_directed query 生成，~1h。

验收（统计门禁，非单次）：干预前后各 ≥3 runs，metacog_total 差 + Welch t 检验 p<0.05。ε ≈ judge 噪声（~0.1，TRUST 2611.10787 经验）。

## v1.1 实测结果（2026-11-22, 83 runs, 结论反转）

| 指标 | v1.0 | v1.1 | 解读 |
|---|---|---|---|
| post_acc | ≈0 (0-0.08) | **0.587** (0-1.0) | 之前把"查不到"当失败, 27b 其实能分清 |
| healthy_gap_rate | — | **0.938** (0.667-1.0) | degraded 里 94% 是 unverifiable（健康缺口） |
| contradicted 占比 | 混在 degraded | ~6% | 真矛盾很少 |

**结论反转**: 27b 的 monitoring 是健康的（能分清"我不知道"vs"我错了"），比 2408.05568 的 myopia 描述乐观。断点不在分类，在 **rework 机制把 46 次重拆预算全浪费在 unverifiable 节点**（"查不到"重搜还是查不到, fix rate 0/46）。

**干预优先级重排**: 干预 2（rework 只对 contradicted 触发）升为**首要**——直接省预算 + 修复集中真问题。干预 1（verify 三态）降为次（分类能力已有, 只是 status 枚举没表达出来）。

"至少有自我认识" = 系统能分清"我不知道"（unverifiable，健康）和"我错了"（contradicted，需修）。27b 现状（v1.1 修正后）：知道去查（control 触发✅）+ 查完能分类（healthy_gap_rate 0.938✅），断点在**修复环**：rework 预算浪费在 unverifiable 上，contradicted 修复率 0。干预 2（rework 条件化）就是补这一环。
