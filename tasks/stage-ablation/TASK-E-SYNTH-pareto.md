# 任务卡 E-SYNTH：跨域 Pareto 综合 + 推荐操作点

# origin: ai · 2026-11-26 · Lead 规划 · sub 纯执行（离线综合，零 LLM，不碰 vLLM 8787）
# 上游: research-agi-budget goal 核心问题「D 硬件条件下性价比 + 最快可靠路径 → 预算控制在 Pareto 边界」
# 背景: E 分支数据已全收口（K7 GPU 15/15 + Q6 域 + Q7 跨题 + 719 nodepth + 300-r3 cache，11-24~11-25），
#       但结果散在 5+ 文件，且各域结论不一致（GPU cov ~300 饱和 vs Q6 到 719 仍在升），
#       没有一份文档回答 goal 本身：Pareto 边界在哪、推荐操作点是什么。本卡补这个真空。

## 只读这些输入（不读其他，不联网，不碰 vLLM 8787，不调任何 LLM）
1. `modules/B-pipeline-ablation/data/t53b/k7-pareto-newjudge-20261124.md` — GPU+Q6 域新口径 Pareto（judge_v1 + 域内 gold），含 Q6 第二域形状核验（cov 719 未饱和）
2. `modules/B-pipeline-ablation/data/t53b/k7_pareto-gpu-20261124.md` — 旧口径首跑（已作废，仅作口径伪影对照，不采信其结论）
3. `modules/B-pipeline-ablation/data/q6-719-nodepth/q6-719-nodepth-analysis.json` — Q6 719 nodepth 3 reps 独立检索分析（cov 0.1304/0.2391/0.2174）
4. `modules/B-pipeline-ablation/data/q7-budget-scan/q7-scan-scores.json` — Q7 完整预算扫描 5 档(50/100/150/300/719)×3 reps=15 条，每条含 budget/rep/wall_s/n_nodes/judge{total,depth,cov}/metacog{total,gap,ret,hg,post}（Q7 是三域里唯一有完整扫描+实际节点数的域，矛盾裁决时优先用它对齐实际节点数）
5. `modules/B-pipeline-ablation/data/q6-budget-scan-rerun/q6-300-r3-20261124-003532.json` — 300-r3 cache 对照（独立评分 0.3077 vs r1/r2 复制 0.2308）
6. `experiments/stage-ablation/tasks/decomposition-research-agi-budget.md` — 只读 E 行（~L208）+ ④ K7 收口行（~L265），取口径限定（judge 族/seed/n 口径）

## S1 提取三域预算-质量曲线（离线计算）
- 从上述文件提取每域（GPU/Q6/Q7）各预算档（50/100/150/300/719）的 cov/struct/depth 分数 + n + SE/CI（文件里有的直接引，没有的从 json 重算，口径=judge_v1+域内 gold，n<8 组标功效不足）。
- 落盘 `modules/B-pipeline-ablation/reports/t53b/e-synth-curves-20261126.json`（结构化，每域每档每轴一值+n+来源文件）。
- 增量 commit。

## S2 跨域矛盾裁决（本卡核心判断，要有依据不是拍脑袋）
- 矛盾：GPU cov ~300 饱和（300:0.358 vs 719:0.352）vs Q6 cov 719 仍在升（300→719 Δ+0.029 未饱和）。
- 裁决维度（逐一给证据）：
  a) 域难度/gold 规模差异（GPU gold 多少 units vs Q6 46 units vs Q7？）——gold 覆盖空间越大，饱和点越晚？
  b) n 与 CI 重叠（Q6 719 档 n=3，Δ+0.029 的 CI 是否与 0 重叠？重叠则"仍在升"不成立，降级为"未证饱和"）
  c) 实际节点数对齐（预算参数是下界非上限，比较必须用实际节点数不用 budget 参数——两域同 budget 档的实际节点数是否可比？）
- 结论形态：「饱和点是域属性（gold 覆盖空间函数）/ 还是普遍 ~300 / 还是现有 n 不足以定」三选一，带 conf + 证据引用。
- 落盘进 S3 文档。

## S3 综合文档 + 推荐操作点
- 产出 `modules/B-pipeline-ablation/reports/t53b/e-synth-pareto-20261126.md`：
  1. 三域曲线表（预算档 × 轴 × 分数 ±CI × n）
  2. 矛盾裁决（S2 结论 + 证据）
  3. **推荐操作点**：D 硬件条件（本地 27b + 现有 GPU 预算）下，给定"可靠性优先"（goal 原文：最快可靠路径），推荐 budget 档 + 理由（边际收益/边际成本比在哪档拐点后塌方）
  4. 口径限定段（judge 族 qwen3.8-27b ×1 non-IRR、seed、n 口径、max_nodes 是下界非上限的已知混淆）
  5. 缺口清单（哪域缺 n、哪轴没测、跨域 gold 不可比的部分）
- 增量 commit。

## 硬约束
- 全程离线：只读 6 个指定文件 + 重算 json，零 LLM 调用、不碰 8787。
- 不碰 tasks/think-trigger/ 下任何文件（另两个 sub 在写）。
- 数字必须带来源文件+行/键；文件里没有的数字不编，标 [待核验]。
- 增量 commit（S1 一个、S3 一个）。
- 最终汇报 ≤15 行：三域曲线是否齐全 + 矛盾裁决一句话（带 conf）+ 推荐操作点一句话 + 文档路径 + commit 链。

## 验收（Lead 对照核）
- [ ] e-synth-curves json 存在，3 域 × 5 档 × 3 轴，每值带 n+来源
- [ ] 矛盾裁决三选一明确，带证据引用（不是"可能/也许"糊过去）
- [ ] 推荐操作点有边际收益/成本论证，不是拍脑袋
- [ ] 口径限定段齐全（judge 族/seed/n/下界混淆）
- [ ] 无 LLM 调用痕迹，commit 链 ≥2
