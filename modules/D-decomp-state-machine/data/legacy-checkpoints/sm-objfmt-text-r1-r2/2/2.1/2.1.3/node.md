# N43: Qwen3-27B 在 W4 (NVFP4/AWQ/GPTQ) 精度下，复杂逻辑推理链 (Chain-of-Thought) 的连贯性评分下降超过 5%，且在长

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

Qwen3-27B 在 W4 (NVFP4/AWQ/GPTQ) 精度下，复杂逻辑推理链 (Chain-of-Thought) 的连贯性评分下降超过 5%，且在长上下文 (>16K) 场景下出现灾难性遗忘 (Catastrophic Forgetting) 的风险显著高于短上下文

## Corrected Claim

Qwen3-27B（或 Qwen3.6-27B）在 W4 (NVFP4) 精度下，通用基准测试（如 MMLU Pro）的精度损失控制在较小范围内（约 ±0.5），但在复杂逻辑推理链及超长上下文场景下的具体性能退化幅度需更多专项评测数据支持，现有证据表明其具备本地部署可行性，但未证实存在显著的灾难性遗忘风险。

## Evidence

[质询]来源中提到的模型版本为 'Qwen3.6-27B'，而事实节点声称的是 'Qwen3-27B'，存在版本不匹配风险；此外，来源仅提及 MMLU Pro 等基准测试精度差距在 ±0.5 以内，并未提供 'CoT 连贯性评分下降超过 5%' 的具体数据，也未明确证实 '长上下文下灾难性遗忘风险显著高于短上下文' 这一特定现象，属于缺乏直接定量支持的推断。 | 来源 [1] 和 [2] 确认了 NVFP4 量化在 27B 模型上的应用及显存优势，但仅指出通用基准测试精度损失较小（±0.5），未直接支持 CoT 连贯性大幅下降或长上下文灾难性遗忘的具体结论，属于间接相关但缺乏直接证据。

## Search Query

Qwen3-27B W4 quantization long context catastrophic forgetting CoT coherence loss

## Retrieval Sources

- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=ef98eea403d5bff14128be2d10e758d41cfa0d018fe3cfdd650cb45133acb313', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
- {'url': 'https://blog.csdn.net/weixin_42662605/article/details/162888699&rut=67681528273b08b00c7def1a7883ac98b3754ff87a192b5dcd57af1ea5e91aec', 'type': 'ddg', 'title': 'DGX Spark上部署Qwen3.6-27B-NVFP4实战指南 - CSDN博客'}
