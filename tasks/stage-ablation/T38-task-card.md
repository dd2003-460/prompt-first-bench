【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# T38: S7V Full Re-score + Paper Final Polish

## 背景
T37 完成（paper submission ready）。唯一统计缺口：S7V per-run scores (n=15) 用于 paired test。

## 任务
1. S7V 15 runs (5Q×3rep) 用 vLLM qwen3.8-27b 生成 (temp=0.1, per-rep seed)
2. Assertion-based M1 + gap-based M4 评分 (local judge = same 27B)
3. Paired test vs S7 (hetero-judge M1+M4): Wilcoxon signed-rank + Hedges g
4. 更新 paper §4.1 (n=4→n=15)
5. Language pass + arXiv checklist

## 验收
- [x] (a) 15/15 scored → runs/s7v-rerun/scores-m1m4.json
- [x] (b) Paired test n=15 in §4.1: M1 p=0.029 g=+0.044; M4 p=0.529 g=-0.326
- [x] (c) Language pass: 0 orphans, consistent terminology
- [x] (d) arxiv-submission.md created
- [x] (e) Commits pushed (36333f4, c415148, cbc8990)

## 失败降级
vLLM 不可用 → LM Studio (conf-0.2); arXiv blocked-on-human 不阻塞。
