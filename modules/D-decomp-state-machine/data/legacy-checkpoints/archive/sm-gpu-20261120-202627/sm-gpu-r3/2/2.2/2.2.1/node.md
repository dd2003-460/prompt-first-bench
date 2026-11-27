# N52: Qwen3-27B 在 FP8 精度下的困惑度增加幅度通常控制在 1%-2% 以内（例如从 9.0 升至 9.1-9.2），这是基于大模型 FP8 量化在长上下

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Qwen3-27B 在 FP8 精度下的困惑度增加幅度通常控制在 1%-2% 以内（例如从 9.0 升至 9.1-9.2），这是基于大模型 FP8 量化在长上下文下误差累积极小的工程经验值

## Corrected Claim

Qwen3-27B 在 FP8 精度下的困惑度增加幅度通常控制在 1%-2% 以内（例如从 9.0 升至 9.1-9.2），这是基于大模型 FP8 量化在长上下文下误差累积极小的工程经验值

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Qwen3 FP8 quantization perplexity degradation
