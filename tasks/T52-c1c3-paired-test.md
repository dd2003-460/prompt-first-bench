# T52: C1+C3 D1 扩 rep + 配对检验

【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

## 目标
D1 (GPT Researcher pipeline) 从 n=5 扩到 n=15（5题×3rep），与 S5 n=30 做 per-question 配对检验，产出 C-face 方向性结论。

## 执行步骤（Lead 本地执行）
| # | 动作 | 产出 |
|---|------|------|
| 1 | C2: grep research_hook 算单次搜索量，判断 duckduckgo 限额够不够 15 runs | tasks/C1C3-decomposition.md §C2 更新 |
| 2 | C1a: 选 5 道题（Q1/Q3/Q4/Q8/Q9 — 覆盖 GPU/推理/LLM评估/VLM/RLHF） | 记录在 run config |
| 3 | C1b: 跑 D1 × 5题 × 3rep = 15 runs（s10_runner.py --arms D1 或等效脚本） | s10-runs/D1-*.json × 15 |
| 4 | C1c: score_s10_v2.py 对 15 runs 打分 | runs/d1-rep15-v2.json |
| 5 | C3: Wilcoxon signed-rank + bootstrap CI(10000) + Cohen's d + per-dim Δ | runs/c1c3-paired-test.md |

## 验收标准
- [ ] 15 D1 runs 完成且全轮次文本保留
- [ ] v2 分数落盘（d1-rep15-v2.json）
- [ ] 配对检验报告含：per-question table + p + CI + d + 分项归因
- [ ] 限定声明："27b + duckduckgo + AI/ML 域 5 题"
- [ ] 若 p≥0.05：明确写"方向性证据，功效不足(n=5)，不宣称统计显著"

## 失败降级
- duckduckgo 限流 → 降为 1rep/题 + 声明"检索质量下限"
- D1 pipeline 报错 → 修 harness 后重跑，不跳过
- 统计库缺失 → pip install scipy numpy，不手算