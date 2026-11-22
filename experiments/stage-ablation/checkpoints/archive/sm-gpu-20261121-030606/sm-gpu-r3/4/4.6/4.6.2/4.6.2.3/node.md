# N330: NVFP4与标准INT4/W4在Qwen3-27B上的性能差异：NVFP4采用非均匀量化步长，需对比两者在相同比特数下的MMLU/GSM8K/HumanEval

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

NVFP4与标准INT4/W4在Qwen3-27B上的性能差异：NVFP4采用非均匀量化步长，需对比两者在相同比特数下的MMLU/GSM8K/HumanEval得分差异，判断N143中'NVFP4/W4'合并表述是否掩盖了NVFP4可能优于标准W4的事实。

## Corrected Claim

NVFP4在Qwen3-27B上展现出显著的速度优势（如更低的TTFT），但其与标准INT4/W4在MMLU/GSM8K/HumanEval等精度指标上的具体差异需进一步数据验证，不能仅凭速度优势断定其精度表现。

## Evidence

[质询]来源仅提供了速度（TTFT/tok/s）对比，未提供MMLU/GSM8K/HumanEval等精度指标，无法直接证实NVFP4在精度上优于或等同于标准W4，存在以速度优势掩盖精度差异的风险。 | 来源[1]直接支持NVFP4在速度上优于其他量化方案，但未覆盖精度指标，属于间接支持/部分支持，且NVFP4作为非均匀量化在理论上可能具有不同精度特性，需降级为定性表述。

## Search Query

NVFP4 vs INT4 quantization accuracy comparison LLM

## Retrieval Sources

- {'url': 'https://kaitchup.substack.com/p/fastest-qwen38-27b-quantization-benchmarking&rut=4b742f25c42a57c7f2f4041eab5408c561ceda5f3362db3b471d1d1938eb9a0e', 'type': 'ddg', 'title': 'Fastest Qwen3.8 27B Quantization? Benchmarking NVFP4, INT4, GSQ, and MTP'}
