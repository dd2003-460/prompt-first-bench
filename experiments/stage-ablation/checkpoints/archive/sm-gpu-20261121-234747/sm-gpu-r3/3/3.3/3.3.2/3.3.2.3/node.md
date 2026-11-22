# N259: RTX 4090 INT8单卡 vs 2×RTX 3090 BF16双卡的TCO-性能比对比：RTX 4090 INT8吞吐约 20 tokens/s，功耗45

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

RTX 4090 INT8单卡 vs 2×RTX 3090 BF16双卡的TCO-性能比对比：RTX 4090 INT8吞吐约 20 tokens/s，功耗450W，3年TCO约 $5,000；$/token = 5000 / (20 * 3600 * 24 * 3) ≈ $0.00093；2×RTX 3090 BF16吞吐约 10 tokens/s（取实测中值），功耗700W，3年TCO约 $4,500（含额外冷却/维护）；$/token = 4500 / (10 * 3600 * 24 * 3) ≈ $0.00174；RTX 4090 INT8的$/token成本仅为双卡BF16的 53%，证明在同等预算下，单卡高带宽+低精度优于双卡低带宽+高精度

## Corrected Claim

RTX 4090 INT8 与 2×RTX 3090 BF16 的 TCO-性能比需基于具体模型大小、量化精度及实际电力成本进行实测评估，通用数值对比（如 20 vs 10 tokens/s）缺乏普遍适用性。

## Evidence

[质询]数值量级与硬件规格严重不符：RTX 4090 在主流 LLM（如 7B-13B）上的 INT8 推理吞吐通常远高于 20 tokens/s（可达 50-100+ tokens/s），而 2x RTX 3090 的 BF16 吞吐也通常高于 10 tokens/s。此外，RTX 4090 的 TCO 通常高于 2x RTX 3090（因单卡价格高且功耗大），此处 TCO 设定（$5000 vs $4500）与当前市场硬件价格及电费逻辑存在偏差，导致 $/token 对比结论缺乏实证基础。 | 经验事实，逻辑自洽但缺来源支持；数值量级与常见硬件基准测试不符，无法验证具体 TCO 和吞吐数据。

## Search Query

RTX 4090 INT8 vs dual RTX 3090 BF16 TCO per token cost comparison
