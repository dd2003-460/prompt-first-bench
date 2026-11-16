# T-soc-pending77-team-20261116 — pending 77 节点分类（core team · 双人独立分类）

**origin: ai** · 派发: zero (Hermes) · 2026-11-16 · 工作目录: /Users/a1-6/Desktop/workspace/pfb

## 背景（最小必要）
SOC 消融臂 gate 要求 cov ≥ 0.898，当前 checkpoint `experiments/stage-ablation/checkpoints/sm-soc-r1.json`：
verified=174, pending=77, degraded=31, failed=1, total=283 → cov=0.615。
Lead 的本地估算：「pending 77 中约 46 个是 knowledge/given 类可翻 verified，degraded 31 中约 10 个可救回」→ 现实上限 ~230/283=0.813。
**这个 46 是拍的，没有逐条核过。本任务就是把它核出来。**

## 任务
数据文件：`experiments/stage-ablation/checkpoints/sm-soc-r1.json`（nodes 列表，283 条；
每条含 id / claim / level / source / status / evidence / search_query / retrieval_sources）。

1. **逐条分类 pending 77**：对每个 status=pending 的节点，判它属于哪类：
   - `A-可翻`：source=given 且 claim 是可直接核验的事实断言（有明确数值/日期/定义，evidence 缺失但可补）
   - `B-需检索`：需要外部来源（search_query 非空或 retrieval_sources 为空的事实断言），来源存在但通道挂
   - `C-难核`：claim 本身模糊/复合/依赖主观判断，公开来源基本不存在
   每条给一行：`节点id | 分类 | 一句话理由`
2. **degraded 31 同样过一遍**：标 `D-可救`（evidence 部分存在、只差补强）/ `E-弃`（claim 本身站不住）
3. **汇总**：A/B/C/D/E 各多少条 → 现实上限 = (174 + A + D) / 283，和 0.813 比差多少

## 分工（lead 拆活，不要一个人闷头做）
- method-reviewer 和 logic-reviewer **各自独立**完成第 1-3 步，各写一份：
  `experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-pending77-<你的名字>.md`
- 两人完成后 lead 做**对比讨论**：分歧节点逐条列出来，各自给理由，lead 裁决并写进
  `experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-pending77-final.md`
  （含：最终 A/B/C/D/E 计数 + 分歧表 + 与 0.813 的对比结论）
- **不许把任何节点真的翻成 verified**——本任务只分类，不动 checkpoint。

## 约束
- 只读 checkpoint json + 写上面三个交付文件，不改其他文件。
- 分类依据必须引用节点字段（source/evidence/search_query），不许凭 claim 文字感觉拍。
- 完成 = 三个文件都存在且 final 文件有分歧表。缺文件 = 未完成。
- 完成后 commit 到 main（前缀 `soc:`），并更新本文件末尾「## 完成报告」。

## 完成报告

### method-reviewer（2026-11-16）

- 交付文件：`experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-pending77-method-reviewer.md`（已写入）
- 分类结果：A=0, B=7, C=70（pending 77）；D=13, E=18（degraded 31）
- 现实上限：(174+0+13)/283 = 187/283 = **0.661**（保守）；若 B 类 7 条检索通道修复后全补上，上限 (174+7+13)/283 = 194/283 = **0.686**（乐观）
- 与 lead 估算 0.813 差距：**0.152**（保守口径）/ **0.127**（乐观口径）
- 主因：lead 把 46 条 knowledge/given 当「可翻 verified」，逐条核后这些节点全是推导框架或自设参数（source=knowledge 45 条 + source=given 5 条 L1 任务描述），无一满足 A 类条件（「有明确数值/日期/定义且 evidence 缺失但可补」）
- checkpoint 未改动（只读），未把任何节点翻成 verified
- 待 logic-reviewer 完成后由 lead 做对比讨论，写 `soc-pending77-final.md`

### 补充：B 类 7 条检索通道实测（2026-11-16）

用 `research_hook` 对 B 类 7 条的 search_query 逐条实测（每条 20-60s 超时）：

| 节点 | 结果 | 耗时 | 说明 |
|------|------|------|------|
| N52 | FAILED | 58s | ResearchHookUnavailable（通道挂） |
| N69 | 3 sources | 0s | cache 命中 |
| N70 | 1 source | 0s | cache 命中 |
| N79 | FAILED | 29s | ResearchHookUnavailable（通道挂） |
| N84 | 3 sources | 0s | cache 命中 |
| N86 | 3 sources | 0s | cache 命中 |
| N87 | FAILED | 29s | ResearchHookUnavailable（通道挂） |

**结论**：4/7 条（N69/N70/N84/N86）检索通道正常（cache 命中），3/7 条（N52/N79/N87）通道挂（ResearchHookUnavailable）。
- 若通道修复后重跑，B 类 7 条理论上全部可补上来源 → 上限 (174+7+13)/283 = 0.686
- 若通道不修，B 类只有 4 条可补 → 上限 (174+4+13)/283 = 191/283 = 0.675
- **无论哪种情形，都远低于 gate 0.898**

### logic-reviewer（2026-11-16）

- 交付文件：`experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-pending77-logic-reviewer.md`（已写入）
- 分类结果：A=0, B=9, C=68（pending 77）；D=9, E=22（degraded 31）
- 现实上限：(174+0+9)/283 = 183/283 = **0.647**（保守）；若 B 类 9 条检索通道修复后全补上，上限 (174+9+9)/283 = 192/283 = **0.678**（乐观）
- 与 lead 估算 0.813 差距：**0.166**（保守口径）/ **0.135**（乐观口径）
- 主因：5 条 source=given 全是 L1 任务描述（非事实断言），45 条 source=knowledge 全是自设参数/推导框架/量化任务，A 类为 0；B 类 9 条（N35/N45/N52/N79/N84/N87/N93/N94/N99）是真正「来源存在但通道挂」的公开可检索事实（佣金率、转化率基线、分布统计）
- 数据口径：主 checkpoint `sm-soc-r1.json` 已被后续 verify-only 轮更新为 221-verified，本任务按任务书口径（174/77/31/1）只读 `sm-soc-r1.bak-verifyonly.json`，未改动任何 checkpoint，未把任何节点翻成 verified
- 边界标注：N250 的 claim 数值（-13.33）与公式代入结果（≈-0.70）不一致，归 D（可核验的算术错误，补 evidence+修正即可）；若 lead 认为算术错误=站不住可改 E，上限 0.647→0.636
- 待 lead 做对比讨论，写 `soc-pending77-final.md`