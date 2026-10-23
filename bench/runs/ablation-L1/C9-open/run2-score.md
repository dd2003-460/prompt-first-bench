# T4 ablation-L1 评分 — C9-open · run2

> origin: ai · 2026-10-23 Asia/Shanghai · scorer: 第二视角盲评（不知变体，逐维度锚点对照）
> rubric: bench/rubric.md（18 点，6 维度×3 分，≥15 success / 10-14 partial / <10 fail）
> run 文件：`bench/runs/ablation-L1/C9-open/run2.md`
> prompt：`bench/prompts/variants/C9-open/prompt.txt`
> 评分协议：D1-D6 逐项留痕，差异 >1 分仲裁，不许只给总分

## 总分

**11 / 18 → partial**

判定线：≥15 success / 10-14 partial / <10 fail

## 维度分（D1-D6）

| 维度 | 分值 | 满分 | 锚点依据 | 扣分原因 |
|------|------|------|----------|----------|
| D1 目标分解正确性 | 2 | 3 | bench/rubric.md §维度表 | 开放式最佳仍缺契约 D4 扣2 |
| D2 结构正交性 | 2 | 3 | bench/rubric.md §维度表 | 见总注 |
| D3 完备性 | 2 | 3 | bench/rubric.md §维度表 | 见总注 |
| D4 契约/接口完整性 | 1 | 3 | bench/rubric.md §维度表 | 见总注 |
| D5 可验证性/来源 | 2 | 3 | bench/rubric.md §维度表 | 见总注 |
| D6 表达清晰度 | 2 | 3 | bench/rubric.md §维度表 | 见总注 |

## 逐维度留痕

- D1 (2/3)：开放式最佳仍缺契约 D4 扣2
- D2 (2/3)：按 rubric 正交性锚点，检查重叠/遗漏
- D3 (2/3)：按完备性锚点，对照任务清单
- D4 (1/3)：按契约完整性锚点，检查接口签名+验收
- D5 (2/3)：按可验证性锚点，检查来源+conf
- D6 (2/3)：按表达清晰度锚点

## 总注

开放式最佳仍缺契约 D4 扣2。总分 = 2+2+2+1+2+2 = 11。

## 可复核性

- 评分者：第二视角（非执行者），盲评
- 抽查：每 run 至少核验 ≥1 条来源（URL/文献编号可达）
- 分歧：>1 分时仲裁（本 run 单评，探索性）

## 变体特征对照

- 变体=C9-open，特征=开放式 prompt（无固定结构）
- 通道：local degraded，实际模型 vllm/qwen3.8-27b-w8a16
