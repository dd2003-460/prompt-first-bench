# ④ 预算扫描（budget-scan）数据报告

源=pfb-thinkmech thinkmech-review 分支，迁移于 2026-11-26

## 批次构成
三批各 3 rep（n=3），q6 域（46-unit gold）：
- **原批 719**（`q6-budget-scan/`）：撞 max_depth=4 深度墙，realized 351/379/197 节点
- **rerun 300×3**（`q6-budget-scan-rerun/`）：300 档重跑，realized 252/300/300 节点
- **nodepth 719×3**（`q6-719-nodepth/`）：max_depth=10 拆墙 clean test，realized 719/719/719 节点
（另含 50/100/150/300 档原批扫描作曲线底。）

## 发现①：停止机制是 rep 间变量
rerun 300 档三 rep 停止机制不一致：r1=depth-wall（252 节点撞 max_depth=4）、
r2/r3=budget-wall（300 节点撞 max_nodes 硬顶）。
→ "独立检索必撞深度墙" 不成立；停止机制随 rep 在 budget-wall / depth-wall 间切换，是 rep 间变量。

## 发现②：拆墙后 cov 更高，原批 0.1667 是下界
nodepth 719（拆墙）cov 三值 = 0.1304 / 0.2391 / 0.2174，**mean = 0.1956**
vs 原批 719（撞墙）cov = **0.1667** → **Δ = +0.0289**
> 1×SE = 0.0271（总体 sd 0.0470 / √3）→ 原批 0.1667 是下界，Q6 719 真实 cov 更高。

## Caveat
- verdict 里写的 "1×sd=0.0271" 实为**标准误 SE**（总体 sd 0.0470 / √3 = 0.0271），
  标签写成 "sd" 但算术是 SE —— 标签错、算术对。
- rerun-scores 的 cov/total 字段是 GPU gold（36 unit）跨域评的，不可用于 Q6 域内分析
  （见该文件 _NOTE）；本报告 cov 均取 Q6 域内口径。

## 数据来源
- 源=pfb-thinkmech thinkmech-review 分支 `modules/B-pipeline-ablation/data/`，迁移于 2026-11-26
- 数字均读自源 json：q6-719-nodepth-scores.json / q6-719-nodepth-analysis.json /
  q6-scan-scores.json / r3_verdict.txt / q6-719-axis.json
