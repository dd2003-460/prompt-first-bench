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