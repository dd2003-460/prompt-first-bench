# Supplementary Index — workshop-draft-metacog-20261122.md

origin: ai (2026-11-24 07:35, 数字审计之"引用可追溯性"——draft §8 声明 "paths in the supplementary"，
但 repo 里此前没有索引文件；本文件补上。编号体系 = git commit 序列 "补充N"（见各 commit message）。
本索引只覆盖 draft 实际引用的 6 个编号；完整 1–46 序列见 `git log --grep=补充`。)

## 编号 → commit → 数据源

| 编号 | 定义 commit | 内容（一句话） | 脚本 / 数据 |
|------|------------|--------------|------------|
| 17 | `13a5a60a7` | r7 metacog 纠错：0.045→0.2912（mid-write 329 节点快照误评，最终 311 节点）；修正后 metacog total 平 | `modules/B-pipeline-ablation/land_rep_run.py` + `modules/B-pipeline-ablation/data/rep-scan/rep-scan-scores.json` |
| 37 | `4739f1768` | gap_rate 是 prompt-elicited 监控非自发——[待核验] 占 51–82%（GPU 82% / NAT 72% / SOC 51%） | `experiments/stage-ablation/prompts.py`（L78、L312 指令原文）+ `modules/B-pipeline-ablation/research/gap-detector-domain-bias.py` |
| 40 | `5a685393f` | claim/evidence 分离证明 (a)→(b) 触发链存在（prompt-elicited）；纠正补充 29/31/36 | `modules/B-pipeline-ablation/research/claim-evidence-separation.py` |
| 41 | `018ab6881` | 预算不变性 provenance gap——rep-scan 是软上限时代（commit 47a8543cd 前），realized 103–166/178–360/271–462 | `modules/B-pipeline-ablation/rep_scan_analyze.py`（rep-scan 15 runs 分析） |
| 42 | `0ca5a2c78` | 预算不变性对脏预算轴稳健：K7 时代 gap_rate~实际节点数 r=−0.209 ns，跨两时代 30 runs 不变性稳健 | `modules/B-pipeline-ablation/research/gap-rate-anova-rep-scan.py` |
| 43 | `db5ffa82b` | (a)→(b) 触发效应 source-mix 混杂——分层梯度 +12–30pp 是干净效应；触发链是梯度非二值 | `modules/B-pipeline-ablation/research/claim-evidence-separation.py`（source-mix 分层段） |
| 45 | `16c76bbb7` | knowledge 缺口内 [待核验] 标签是检索触发器（GPU 66% vs 14% z=+3.63, NAT 60% vs 0% z=+3.52, SOC ns） | `modules/B-pipeline-ablation/research/claim-evidence-separation.py`（tag-trigger 段） |

## 编号 → draft 位置（引用点）

| 编号 | draft 引用位置 |
|------|--------------|
| 17 | §4.1（r7 329 vs 311 快照纠错） |
| 37 | §4.1（spontaneous form 未实现，[待核验] scaffolding） |
| 40 | §4.1（claim/evidence field separation 的 net reading） |
| 41–42 | §4.2（rep-scan provenance caveat，软上限时代） |
| 43 | §4.1（within-source (a)→(b) effect 47–59% vs 18–40%） |
| 45 | §4.1（[待核验] tag 触发 66%/60% vs 14%/0%） |

## 验证记录（2026-11-24 07:35）

- 7 个数据源文件全部 `os.path.exists` 通过（land_rep_run.py / rep-scan-scores.json / prompts.py /
  claim-evidence-separation.py / rep_scan_analyze.py / gap-rate-anova-rep-scan.py /
  gap-detector-domain-bias.py）。
- commit hash 全部 `git show` 可查（pfb repo，tmp-lit-snowball 分支可达）。
- prompts.py 行号（L78/L312 [待核验] 指令）已独立验证（2026-11-24 07:25，sed 取行核对）。
- 编号体系来源：`git log --all --grep=补充`（补充 32–46 连续可见；补充 17 为早期编号）。
