# N30: FP8量化在27B规模模型上通常导致Perplexity增加<1%，MMLU准确率下降<0.5%，因此被视为“无损”或“极低损”精度；而W4量化在相同模型上可能

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

FP8量化在27B规模模型上通常导致Perplexity增加<1%，MMLU准确率下降<0.5%，因此被视为“无损”或“极低损”精度；而W4量化在相同模型上可能导致MMLU下降2-4%，需引用Qwen官方技术报告或主流量化库（如GPTQ, AWQ）的评估表格

## Corrected Claim

FP8量化在27B规模模型上通常导致Perplexity增加<1%，MMLU准确率下降<0.5%，因此被视为“无损”或“极低损”精度；而W4量化在相同模型上可能导致MMLU下降2-4%，需引用Qwen官方技术报告或主流量化库（如GPTQ, AWQ）的评估表格

## Evidence

检索失败: no sources from any channel (all 5 failed)
