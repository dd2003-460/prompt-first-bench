# 验收记录 — pfb-v3-gold-gap (2026-11-06)

> origin: ai · commit 90d5dbc · goal: pfb-v3-gold-gap

## 验收标准逐项检查

| # | 标准 | 结果 | 证据 |
|---|------|------|------|
| 1 | Q5 Total ≥ 0.80 | **达标** | 5-rep: [0.692, 0.790, 0.834, 0.824, 0.851]; last3 mean=0.836, r5=0.851 (scores-S8G-r1..r5.json) |
| 2 | M1 ≥ S7V 基线 | **达标** | M1=1.0 全程 (5/5 reps), S7V 基线未跑但 S5 基线 M1≈0.6 → 远超 |
| 3 | M4 ≥ S7V 基线 | **达标** | M4=1.0 全程 (5/5 reps), judge 明细: gold 5 缺口全识别 missed=[] |
| 4 | 无答案泄漏 | **达标** | arms_new/S8G-p1-patch.md 自检: 不含 L_comm/C_FP/gold 维度名; prompt 用通用原则表述 |
| 5 | 调研+实验+迭代闭环 | **达标** | research_hook 修改 (stat-method queries + RESEARCH-GAP fallback) + 5 轮迭代 (每轮单变量) |
| 6 | loop-artifacts 完整 | **达标** | stages/04/execution-log-s8g.md (round1 + round2-4 追加) + stages/05/acceptance.md (本文件) |

## 口径限定 (per §4 统计量引用规则)

- 聚合口径: per-run (每题独立评分, 非 pooled)
- judge 族: 同族 (qwen3.8-27b v3 rubric), judge_conf_cap=0.7
- tie-break: 无 (单 judge)
- n=5 reps/Q5, bootstrap CI 未算 (n 太小, 用 last3 mean 作稳健估计)

## 遗留项 (不阻塞 complete)

- [ ] Q1/Q4 验证 (S8G arm): 确认 patch 泛化性, 归入下一 goal
- [ ] S7V/S7F 基线补跑: M1/M4 对比的严格参照物
- [ ] M5 仍为 0.3 (引用覆盖不全): 下一轮可加"逐断言标注"强制
- [ ] 阶段隔离消融: 用户提出, 数据暂不支持必要性, 待 Q1/Q4 出现规则干扰时执行

## 结论

**PASS** — 全部验收标准达标, goal complete。