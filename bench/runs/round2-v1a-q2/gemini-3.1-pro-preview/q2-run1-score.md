# Q2 run1 评分 — gemini-3.1-pro-preview（V1a 普通任务拆解）— 状态：N/A（无模型输出，不可评分）

> origin: ai
> 评分时间：2026-10-23 04:15 Asia/Shanghai
> 评分人：route B 执行 subagent
> 评分依据：`rubric/scoring.md` D1–D4（100 分制）
> 评分对象：`q2-run1.md`
> 状态：**N/A — 无模型产出，不可评分**

## 判定

本 run 因 arena 平台层故障（连续 4 次发送/重试均返回 "Something went wrong" + reCAPTCHA 横幅，详见 `q2-run1.md` 尝试记录与证据文件）未产出任何模型答案。

按诚实原则：**不评分、不赋分、不以其他模型或 V0 输出顶替**。

## 分值

| 维度 | 得分 |
|------|------|
| D1 正确性 | N/A |
| D2 完备性 | N/A |
| D3 结构正交 | N/A |
| D4 置信度标注 | N/A |
| **总分** | **N/A** |

## 判定

**N/A（不可评分）** — 不计入 success/partial/fail 任何一类。

## 对汇总的影响

- 本 run 不计数（FINAL-VERIFY.md：每题×变体×模型 ≥3 runs 的下限要求下，失败 run 不计入有效 run）。
- V1a × Q2 × gemini 单元格在平台故障恢复后需重跑。
- round2-v1a-q2 的 3 格汇总中，gemini 格标记为 N/A，success 率统计的分母为实际完成 run 数（1/3），分子为其中 ≥80 分的 run 数（1/3），即 **success 率 = 100%（n=1，不做强结论）**；另两格（gemini、qwen）因平台故障 N/A。

## 参考

- 完整失败记录与证据：`q2-run1.md`（尝试记录表 + trace IDs + 截图路径）。
- V0 基线（round1-v0 gemini × Q2）= 93 分，仅作参考，不与本 run 对比（无同 run 输出）。
