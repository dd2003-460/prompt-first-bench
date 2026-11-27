# experiments/stage-ablation 索引（2026-11-27 迁移后）

> 1-loop 阶段消融实验。2026-11-27 布局迁移（LAYOUT-Reorg）后本目录只保留：
> 状态机核心脚本（排除清单，原地不动）+ gold/ + questions/（Q9G-V1 依赖）。
> 迁移映射：`tasks/layout-reorg-mapping.json`；迁移结果：`tasks/layout-reorg-migrate-result.json`。

## 留在本目录的
| 条目 | 说明 |
|---|---|
| s5_state_machine.py | 状态机主脚本（--anchor-file flag, @2409c88c5） |
| ablation_harness.py / research_hook.py / q9_budget_scan_queue.sh | 核心 harness / hook / 队列脚本 |
| gold/ | Q1-Q5 + Q9 gold 骨架（Q9G-V1 依赖，不动） |
| questions/ | Q1-Q5 + Q9 题面（Q9G-V1 依赖，不动） |
| runs-s5-sm-objfmt-*.json / runs-s5-sm-q9-agi.json | objfmt-hack / q9-agi 活动 run 产物（未跟踪，run 结束后随下一轮迁移） |

## 迁出的（指针）
| 去处 | 内容 |
|---|---|
| modules/D-decomp-state-machine/data/legacy-* | checkpoints/、runs-*/ 全部历史 run 数据 + spec/ + web-llm/ |
| modules/D-decomp-state-machine/scripts/ | 状态机相关 .py/.sh |
| modules/D-decomp-state-machine/reports/ | 状态机相关报告 |
| modules/A-eval-infra/{scripts,data,reports,research}/ | judge/rubric/scoring 相关（含原 INDEX.md legacy 版） |
| modules/B-pipeline-ablation/{scripts,data,reports,research,misc,legacy-*}/ | B 管线脚本/数据 + repro/ drb-pilot/ bench/ arms_new/ optimize-T35/ lit-survey/ loop-artifacts/ research/ social/ |
| modules/E-sota-benchmark/{scripts,data,reports,research,misc}/ | DRB/s10/SOTA 相关 |
| modules/F-theory/reports/ | production-final-report.md |
| archive/logs/ | 全部 .log（含原 logs/ 目录 7 文件） |
| archive/runtime-cache/ | .research-cache* 两个缓存目录 |
| tasks/stage-ablation/ | 原 tasks/ 子目录（59 文件） |
