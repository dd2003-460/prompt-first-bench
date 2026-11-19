# T23 Semi-Hetero Judge Analysis (Qwen2.5-7B)

> origin: ai · 2026-11-05 · Lead 执行
> Judge: qwen2.5-7b-original (LM Studio, port 1234, temperature=0)
> Artifacts: 18 (A-E groups), Gold: Q1-Q5
> **局限声明**: 同族不同代际（Qwen2.5 vs Qwen3.8），非真异源。Conf cap 0.5。

## Per-Arm Results

| Arm | n | Mean Total | Range | Same-source (27B) |
|-----|---|-----------|-------|-------------------|
| S0  | 2 | 0.855 | [0.843, 0.868] | 0.374 |
| S1  | 4 | 0.896 | [0.877, 0.915] | 0.463 |
| S2  | 6 | 0.847 | [0.700, 0.922] | 0.535 |
| S3  | 2 | 0.915 | [0.900, 0.930] | 0.489 |
| S4  | 1 | 0.908 | [0.908, 0.908] | 0.528 |
| S5  | 1 | 0.908 | [0.908, 0.908] | 0.548 |
| D1  | 2 | 0.886 | [0.882, 0.890] | 0.409 |

## Hypothesis Verification

| Hypothesis | Same-source (27B) | Semi-hetero (7B) | Agreement |
|-----------|-------------------|-------------------|-----------|
| H1: S1>S0 (decomposition positive) | ✅ +0.089 | ✅ +0.041 | **AGREE** |
| H2: S1→S2 largest gain | ✅ +0.072 | ❌ -0.049 (S2→S3 is max +0.068) | **DISAGREE** |
| H3: S2→S3 negative effect | ✅ -0.046 | ❌ +0.068 | **DISAGREE** |
| H4: S4→S5 small positive | ✅ +0.020 | ⚠️ 0.000 | **WEAK** |

## Diagnosis

Qwen2.5-7B 作为 judge 存在两个系统性问题：

1. **区分度不足**：所有 arm 总分集中在 0.85-0.92 窄带（range=0.07），而同源 27B 在 0.37-0.55（range=0.18）。7B 模型对工件质量的感知粒度不够，把"还行"和"很好"都给了高分。

2. **宽松偏置**：绝对分数系统性偏高 ~0.4（7B mean 0.88 vs 27B mean 0.48）。7B 缺乏严格 fact-checking 能力，对 M1（事实准确率）和 M3（矛盾检测）的判断力明显弱于 27B。

## Conclusion

**半异源 judge 未能验证同源结论。** 但这不意味着同源结论错误——更可能是 7B judge 能力不足（区分度差 + 宽松偏置），而非工件质量真的如 7B 所判。

H1（分解正贡献）在两个 judge 下一致，这是最稳健的结论。
H2/H3（调研最大增益 / 规划负效应）仅在同源 27B 下成立，需要真异源 judge 确认。

## Next Steps

- P0: 获取外部 API key → 用 GPT-4o/Claude/Gemini 做真异源 judge（预计 conf 可升 0.8+）
- P1: Arena reCAPTCHA 冷却后重试 agent mode
- P2: 接受同源 27B 结果（conf 0.7），标注 "single-judge, same-family"，先推进论文/报告

## Raw Data

`hetero-scores-semihetero.jsonl` (108 dim-scores, 18 artifacts × 6 dims)
