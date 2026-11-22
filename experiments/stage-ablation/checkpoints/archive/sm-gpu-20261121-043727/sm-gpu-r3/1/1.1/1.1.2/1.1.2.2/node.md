# N109: NVFP4 在 RTX 4090 (Ada Lovelace) 上的硬件支持可行性：RTX 4090 支持 FP8 Tensor Core 但不原生支持 FP4

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

NVFP4 在 RTX 4090 (Ada Lovelace) 上的硬件支持可行性：RTX 4090 支持 FP8 Tensor Core 但不原生支持 FP4 运算指令，需通过软件模拟 (如 TensorRT-LLM 的 FP4 模拟层) 或降级为 FP8 执行；若模拟，计算延迟预计增加 20-40% 相比原生 FP8，需对比 FP8 方案的性能优势是否被抵消 [待核验: 需确认 TensorRT-LLM 对 Ada 架构 FP4 的支持状态及性能开销数据]

## Corrected Claim

NVFP4 在 RTX 4090 (Ada Lovelace) 上无原生 FP4 硬件支持，需通过软件模拟或降级为 FP8 执行（如 AdaLLM 运行时）。现有基准测试显示，采用 NVFP4 权重配合 FP8 执行路径相比原生 FP8 方案，整体吞吐量约有 20-25% 的损失，具体计算延迟开销需进一步实测确认。

## Evidence

[质询]陈述中关于“计算延迟预计增加 20-40%”的具体数值缺乏来源直接支持，且来源[1]提到的“~20-25% throughput loss”是指整体吞吐量损失（包含内存带宽瓶颈等），不能直接等同于纯计算延迟的增加比例，存在口径混淆风险。 | 来源[1]和[2]证实了RTX 4090 (Ada Lovelace) 上存在NVFP4推理运行时（AdaLLM），且采用FP8执行路径（间接支持需软件模拟/降级执行），但未提供具体的“20-40%计算延迟增加”数据，仅提及整体吞吐量损失约20-25%，故降级为定性表述。

## Search Query

RTX 4090 Ada Lovelace FP4 TensorRT-LLM support performance overhead simulation

## Retrieval Sources

- {'url': 'https://github.com/BenChaliah/NVFP4-on-4090-vLLM&rut=11634a2155f2568a35529a67d3fa48b1b1d97e6614e0ad523daa41c056e4afba', 'type': 'ddg', 'title': 'GitHub - BenChaliah/NVFP4-on-4090-vLLM: AdaLLM is an NVFP4-first ...'}
- {'url': 'https://github.com/BenChaliah/NVFP4-on-4090-vLLM/tree/main/adallm&rut=f2dd4136d17303cb6e043d49e6a4423376d1c8fa55d7fc25035f21e2c25ec876', 'type': 'ddg', 'title': 'NVFP4-on-4090-vLLM/adallm at main - GitHub'}
