# Rubric v2 全量重放分析（r245 · 2026-11-02）

## 结果：overall_pass=False
- AC1 一致率 0.661 (84/127) < 0.85 ❌
- AC2 X5 双 fail ✅ (True)
- AC3 B-none J2 均值 0.533 ≥ 0.3 ❌
- AC4 A-full vs B-2del-eo 差值 < 0.3 ❌（J2 两组均 1.0）

## 分歧结构诊断
1. **J2 恒高分**：A-full/B-2del-eo/B-noowner 在 J2 下全是 1.0——硬地板 B-1/B-2/B-3 没起作用，宽松判官对"删了但没声明"不敏感。
2. **J1 对 B 系列打 0**：B-none/B-nofreeze/B-noowner 在 J1 下多为 0.0——严格判官的 source-truthfulness 硬测试过严。
3. **parse 失败 7/36 run**：拉低有效样本，需查失败原因（可能是 max_tokens 截断或 JSON 格式漂移）。
4. **逐项分歧热点**：X2/X3 (0.67)、G1-G8 (0.33-0.60) —— gap 类条目两判官标准不一。

## 下一步选项
- A. rubric v3：收紧 J2 的 B-1/B-2/B-3 地板（要求显式引用证据才算 pass），放宽 J1 的 truthfulness（区分"无证据"vs"证据错误"）
- B. 先修 parse 失败（7 run）再重放，看一致率能否自然回升
- C. 放弃同族双判路线，直接等异源 judge（与 T8 Part C 收口方案同一阻塞）
