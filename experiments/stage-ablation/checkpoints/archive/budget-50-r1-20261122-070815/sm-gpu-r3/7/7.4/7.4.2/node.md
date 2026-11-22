# N382: RTX A6000 支持 FP8 精度（通过软件模拟或硬件支持需确认），FP8 权重质量损失相对于 BF16 通常 <1% MMLU 下降，但相对于 INT4 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RTX A6000 支持 FP8 精度（通过软件模拟或硬件支持需确认），FP8 权重质量损失相对于 BF16 通常 <1% MMLU 下降，但相对于 INT4 质量优势显著；需验证 Qwen3-27B 在 FP8 下的 MMLU/GSM8K 具体得分 [待核验: 官方技术报告或独立评测]

## Corrected Claim

RTX A6000 (Ampere架构) 硬件不支持 FP8 精度，需通过软件模拟实现；FP8 权重质量损失相对于 BF16 通常较小（具体数值依模型而定，<1% MMLU 下降为常见经验估计但非绝对），但相对于 INT4 质量优势显著；Qwen3-27B 在 FP8 下的具体 MMLU/GSM8K 得分需查阅官方技术报告或独立评测。

## Evidence

[质询]RTX A6000 (Ampere架构) 硬件原生不支持 FP8 精度（FP8 硬件支持始于 Ada Lovelace/Hopper 架构），因此‘硬件支持’这一说法存在事实错误；此外，‘FP8 相对 BF16 质量损失 <1% MMLU’是一个高度依赖具体模型和量化方法的经验性统计结论，并非普适物理定律，且缺乏当前来源支持。 | 经验事实，逻辑自洽但缺来源支持；RTX A6000 硬件不支持 FP8 为已知硬件规格事实，原陈述中‘硬件支持’部分有误，需修正为软件模拟或明确硬件限制。

## Search Query

Qwen3 27B FP8 quantization MMLU GSM8K benchmark quality loss
