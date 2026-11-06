【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00..04.5
2. 每阶段产出落盘 loop-artifacts/stages/<N>/
3. 完成后 commit + push
4. 通道故障 → 报告 Lead 降级，不得静默跳过

# T43: Q3 Pricing-Enhanced Re-test

## 目标
重做 Q3（API 供应商选型），增加价格时效性强制段，验证 pricing-enhanced prompt 能否将 M1 从 0.53 提升到 ≥0.60。

## 题目
- Q3: 见 `experiments/stage-ablation/gold/Q3.md` 顶部的 question 字段（**不要读 gold 的其他内容**）

## 额外约束（vs T40/T41 的增量）
在 S8D prompt 基础上增加以下强制段：

```
## 价格数据规则（强制）
1. 所有价格/费率必须标注查询日期（格式：[as of YYYY-MM-DD]）
2. 每个价格至少 2 个独立来源交叉验证（不同网站/文档）
3. 无法确认的价格标 [UNVERIFIED] 并说明原因（如"仅单一来源"或"页面 404"）
4. 如果两个来源价格差异 >20%，标注 [CONTRADICTION: source_A=$X, source_B=$Y] 并给出你的判断
5. 优先使用官方定价页（groq.com/pricing, together.ai/pricing, fireworks.ai/pricing）
```

## 产出
- `loop-artifacts/stages/04/Q3-execution-log-r2.md`（r2 = 第二次跑）
- commit message: "T43: Q3 pricing-enhanced re-test"
- push 到当前分支

## 失败降级
- 官方定价页 404/改版 → 用第三方聚合源（OpenRouter, Artificial Analysis）+ [SECONDARY] 标注
- 单题超时 → 完成能完成的部分，标注 [INCOMPLETE]
