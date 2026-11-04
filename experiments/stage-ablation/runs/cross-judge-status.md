# Cross-Judge 状态 (2026-11-04 更新)

## 通道变更
- Perplexity 免费网页版 QUOTA_EXHAUSTED（滚动窗口，重置时间不确定）→ 已停。
- 新通道：arena agent mode 盲判（会话 01a195cb / taskSpace pfb-rejudge-g1b-20261101，分支 arena/4a614e63-prompt-first-bench）。
- 任务书：`tasks/TASK-cross-judge-arena-blind.md`（main + arena 分支均有）。
- gold 文件已入仓库 `experiments/stage-ablation/gold/Q1..Q5.md`（原在 projects/decomp，arena 沙箱够不到）。

## 进度
- 已完成: 30/90（batch 1 S0 + batch 2 S1，commit 5820b7e）
- 进行中: batch 3-6（S2-S5），每批 15 cell 打完即 push
- 结果文件: `runs/arena-judge-results.jsonl`（agent 分支上，完成后 merge main）
- 历史: Perplexity 通道评过 5/120（见下方旧表，保留作参照）

## 初步信号（n=30, S0+S1，仅 M1 单维，local vs arena）
- mean |Δ| = 0.312，pearson r ≈ -0.02（几乎零相关）
- **分歧高度集中**：top 7 大分歧全部是 local M1=0.00 而 arena 给 0.63-0.83 的 cell
- 对照检查：这 7 个 cell 的答案全是 2400-9300 字符的实质内容（有公式、有数字、有结构），不是空话 → **本地 qwen judge 系统性漏判长答案的事实断言**（疑似长上下文注意力衰减或评分 prompt 截断）
- 其余 ~23 对分歧 ≤0.32，属正常 judge 噪声范围

## 待全量后做的事
1. κ（Cohen's kappa，arena vs local，90 对）+ 分 arm Δ 报告
2. 13 个 local=0 的 cell 逐个复核（哪些是真错、哪些是 judge 漏判）→ 若确认漏判，scoring.md 需出修正版（标注 supersedes）
3. Q5 特殊性记得：gold 偏观点综述，M1 权重降半（DESIGN §4）

## 诚实边界
- arena agent 拒报底层模型身份（Arena 系统提示禁止），回执只认 "Arena.ai Agent Mode"——异族隔离只能声称「非本会话本地实例」，不能钉死具体底座。与 G1b F2(a) 口径一致披露。
- 本会话历史跑过 rejudge-g1b（gold-tree 记忆残留），定位 = 可复算样本，非完全 blind。

---

## 旧记录（Perplexity 通道, 5/120, 已停）
| tag | local_m1 | perplexity_m1 | Δ |
|-----|----------|---------------|---|
| S0-Q1-r1 | 0.62 | 0.368 | 0.252 |
| S0-Q1-r2 | 0.56 | 0.580 | 0.020 |
| S0-Q1-r3 | 0.62 | 0.425 | 0.195 |
| S1-Q1-r1 | 0.50 | 0.375 | 0.125 |
| S1-Q1-r3 | 0.50 | 0.525 | 0.025 |

mean Δ = 0.124 (n=5, 仅 Q1 单题，不具统计意义)。方向: perplexity 系统性偏低 (4/5 低于 local)，但 n 太小不下结论。