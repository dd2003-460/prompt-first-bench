# T-JUDGE-1 校准检查：自评 status vs 机械来源核验（2026-11-23）

## 问题
模型自评的节点 status（verified/degraded/pending）和机械来源核验（数值真在来源页）
是否对齐？对齐 = 自我认识校准（正面证据）；脱节 = 自我认识失效（反面证据）。

## 口径
- 候选 = 所有带 ≥1 URL 且 claim 含 数值+单位 的节点（359 个，19 树）。
- 机械判定：复用 source_verify cache（key=url|num|unit），新抓 342 个 URL。
- 机械 verified = 数值+单位在页面 20 字符窗口共现（文本层）。
- 模型 status = 对整个 claim 的核验结论（语义层）。
- **粒度差**：机械 verified 只查 claim 第一个数值是否在第一个来源页；模型 status
  是对整个 claim（可能多数值/多来源）的判断。两者不是一回事。

## 结果（带数值+URL 的 359 节点）
| status | 机械verified | weak | not_verified | unreachable | 可达 | 可达内verified率 |
|---|---|---|---|---|---|---|
| verified | 7 | 2 | 0 | 9 | 9 | **0.778** |
| degraded | 106 | 45 | 40 | 114 | 191 | **0.555** |
| pending | 11 | 3 | 6 | 16 | 20 | **0.550** |

## 结论
1. **自评方向对但强度弱**：verified 组机械核验率最高（0.778 > 0.555/0.550），
   自评有校准方向——模型说 verified 的节点，机械核验也更倾向 verified。
   但 verified 组 n=9（可达），**不显著**。
2. **degraded 组 56% 机械 verified**（n=191，可靠）：模型把大量"数值在来源页"
   的节点标成 degraded。提示**降级偏保守**——但受粒度差限制（机械查第一个数值，
   模型判整个 claim），不全是"模型错"。
3. **degraded ≈ pending**（0.555 vs 0.550）：模型没区分"查完查不到"和"还没查"，
   两组机械核验率一样。

## 对 workshop 的意义
"自我认识是否校准"不是非黑即白，而是**方向对但强度弱 + degraded 降级偏保守**。
比"自我认识完美"或"自我认识失效"都更真实，符合 measurement+diagnosis 定位。

## 口径警告
1. verified 组 n=9（可达），0.778 不显著，仅方向参考。
2. 机械 verified（数值在页）≠ 来源支持 claim（语义）——56% 的 degraded 机械
   verified 不全是模型降级错，部分是粒度差（claim 多数值/多来源）。
3. 60.6% 无 URL 缺口 → 只在 URL 保留子集上算，跨 run 不可比。
4. 无数值节点可达性校准（n=507）：verified 0.450 / degraded 0.475 / pending 0.364
   ——可达性上 verified 组反而略低于 degraded 组（n 小，方向不稳）。

## 脚本
`calibration_check.py`（机械，无 LLM，cache-resume，MAX_NEW_FETCH=400）。
结果：`data/calibration-check.json`。
