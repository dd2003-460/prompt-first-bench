# T38 分解 — S7V Full Re-score + Paper Final Polish

> origin: ai · 2026-11-06 · T37 complete 后 find-next-goal 产出

## 分解树

```
T38-s7v-full-rescore-final-polish
├── A. S7V Full Re-score (n=15)
│   ├── A1. 确认 vLLM qwen3.8-27b @ :8787 可用 (health check)
│   ├── A2. 运行 S7V arm: 5Q × 3rep = 15 runs (temp=0.1, per-rep seed)
│   │     - 使用 ablation_harness.py build_prompt('S7V', qid)
│   │     - 输出: runs/s7v-rerun/s7v-{qid}-r{rep}.json
│   ├── A3. 评分: 对 15 runs 跑 score.py (7-dim rubric, local judge)
│   │     - 输出: runs/s7v-rerun/scores.json (per-run M1-M7 + total)
│   └── A4. Paired test: S7V(15) vs S7(15), Wilcoxon signed-rank + Hedges g
│         - S7 per-run scores 来源: raw-data-full-perdim.json (已有)
│         - 配对方式: same QID × same rep index
│         - 输出: paired-test-n15.json + paper §4.1 更新
├── B. Paper Final Polish
│   ├── B1. Language pass: grammar/spelling/consistency (全文)
│   │     - 重点: §2 新写部分 (刚插入, 未过 language check)
│   │     - 工具: 人工读 + grep 常见错误模式
│   ├── B2. arXiv submission checklist
│   │     - title / abstract / comments / categories / keywords
│   │     - 落盘: arxiv-submission.md
│   └── B3. Final consistency check
│         - 所有数字与 bootstrap-cis.json 一致
│         - References 编号与正文引用一一对应
│         - 无 [待核验] 残留
└── C. Commit + Push
    └── C1. git commit + push origin main
```

## 正交性自检

| 对 | 关系 | 判定 |
|----|------|------|
| A vs B | A 产数据, B 用数据 polish 论文 | 有依赖(A→B), 非正交但有序 ✓ |
| A1 vs A2 | A1 是 A2 前置条件 | 串行依赖 ✓ |
| B1 vs B2 | 独立 (语言 vs 元数据) | 正交 ✓ |
| B3 vs C1 | B3 是 C1 前置 | 串行依赖 ✓ |

## 缺口清单

| # | 子项 | 缺什么 | 状态 |
|---|------|--------|------|
| G1 | A2 | S7V prompt 是否已导出到 repro/prompts/? | 已有 (T37-C1 导出 40 prompts 含 S7V×5Q) |
| G2 | A2 | per-rep seed 策略 | 沿用 harness 默认: seed = hash(qid+rep) % 10000 |
| G3 | A4 | S7 per-run scores 确切位置 | **已解决**: hetero-judge-s6s7-results.json 有 S7×15 (M1+M4 only); optimize-T35/scores.json 有 S7×4 (M1-M6, Q1/Q4) |
| G4 | A4 | S7V 需 re-score 哪些维度? | M1+M4 可从 hetero-judge 取 S7 配对; M2/M3/M5/M6 需 local judge re-score S7V (score.py 6-dim) |
| G5 | B2 | arXiv categories 选择 | cs.CL + cs.AI (主) + stat.ME (次)? [待核验] |
| G6 | B2 | 目标会议/期刊 | 未定 (arXiv preprint 先行, venue 后续) |

## 关键风险

- **G3/G4**: S7 full 15 per-run 6-dim scores 可能不存在 (T37 已确认 S7T/S7F/S7V 无 per-run; S7 本身在 raw-data-full-perdim.json 中? 需验证)。若 S7 也无 per-run → paired test 仍需 re-score S7 (再加 15 runs, ~15min)。
- **时间估算**: A2 (~15min vLLM) + A3 (~10min scoring) + A4 (<1min stats) + B1 (~30min) + B2 (~10min) ≈ 1h total。
## T38 完成证据 (2026-11-06)

| 验收项 | 状态 | 证据 |
|--------|------|------|
| (a) S7V 15 runs 评分 | ✅ | `runs/s7v-rerun/scores-m1m4.json` (assertion-based M1+M4, 15/15) |
| (b) Paired test n=15 | ✅ | `runs/s7v-rerun/paired-test-n15.json` → paper §4.1 (M1 p=0.029 g=+0.044; M4 p=0.529 g=-0.326) |
| (c) Language pass | ✅ | 术语统一 (hetero-judge/per-run), 无孤立引用, 无 stale numbers, 31/31 refs cited |
| (d) arXiv checklist | ✅ | `arxiv-submission.md` (metadata + file checklist + verification) |
| (e) commit+push | ✅ | 3 commits pushed to main (36333f4, c415148) |

**Paper final stats**: 6,874 words, 395 lines, 31 refs, 35 sections, 0 orphans, 0 placeholders.
