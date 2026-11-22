# N486: ΔPPL = PPL_FP8 - PPL_BF16，若官方未提供，则通过本地运行llama.cpp或vLLM加载FP8模型并执行标准PPL评估脚本计算，误差范围

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N154

## Claim

ΔPPL = PPL_FP8 - PPL_BF16，若官方未提供，则通过本地运行llama.cpp或vLLM加载FP8模型并执行标准PPL评估脚本计算，误差范围标注为±0.5%

## Corrected Claim

ΔPPL = PPL_FP8 - PPL_BF16，若官方未提供，则通过本地运行llama.cpp或vLLM加载FP8模型并执行标准PPL评估脚本计算，误差范围标注为±0.5%

## Evidence

先验知识/题面给定，逻辑校验通过
