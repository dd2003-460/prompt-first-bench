# T52: E3 双轨评分实验

> origin: ai · 2026-11-07 · C-face 完成后按 PFB-APPLY plan 排序的下一目标
> 来源：memory/insights/2026-11-07-mechanism-deepdive.md §E3 + T51 已知问题#3

## 要回答的问题

S5 vs S0 的 +0.235 总分差里，多少是"真减少幻觉"（final answer 更准），多少是"被拦截"（过程中发现错误并修正）？
如果全程断言评分（process track）和终态评分（final-only）差距大 → 说明 prompt-first 的价值主要在"过程纠错"而非"直接答对"。

## 改动

`score_s10_v2.py` 加 `--track {final,process,both}` 参数：
- final: 只评 `output_text`/`final` 字段（现状）
- process: 把 `rounds.r1-r4.output` 全部拼起来评 M1（断言数会多很多）
- both: 两个都算，输出 Δ = process_M1 - final_M1

## 数据源

已有 runs：S10-A~E 各 18 runs（含 rounds 字段）+ S5 27 runs（无 rounds，只有 final → process=final，Δ=0 作为对照）

## 验收

- [ ] score_s10_v2.py --track both 跑通 S10 90 runs
- [ ] 每臂输出 final_M1 / process_M1 / Δ 三列
- [ ] 报告：哪臂的 Δ 最大（= 过程纠错价值最高）
- [ ] 解读：prompt-first 的核心机制是"生成时防错"还是"生成后纠错"

## 预期耗时

~30 min（scorer 改 20 行 + 跑 90 runs ~15 min + 写报告）
