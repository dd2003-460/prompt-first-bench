# N174: RTX 4080 Super 16GB 在 Qwen3-27B INT8 场景下的实际瓶颈机制：由于权重 (27GB) > 显存 (16GB)，推理过程必须将未

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

RTX 4080 Super 16GB 在 Qwen3-27B INT8 场景下的实际瓶颈机制：由于权重 (27GB) > 显存 (16GB)，推理过程必须将未访问的权重层从 CPU 内存 Swap 到 GPU，吞吐量受限于 PCIe 4.0 x16 带宽 (理论 ~32GB/s, 实际 ~25-28GB/s) 而非计算单元，导致 '10-15 tokens/s' 的吞吐量预测极可能严重高估，实际可能低于 5 tokens/s。

## Corrected Claim

RTX 4080 Super 16GB 在 Qwen3-27B INT8 场景下，由于模型权重（约13.5GB）加上KV Cache可能超出16GB显存，推理过程可能涉及CPU-GPU数据交换，吞吐量受限于PCIe带宽，实际吞吐量可能显著低于纯计算预测值，具体数值取决于内存管理策略和量化精度。

## Evidence

[质询]该陈述将‘权重总量大于显存’直接等同于‘必须Swap未访问层’，忽略了现代推理框架（如vLLM, llama.cpp）通常采用的‘部分层驻留+CPU卸载’或‘量化压缩’策略，且‘10-15 tokens/s’的预测来源不明，无法确认其是否基于错误的纯计算假设；此外，INT8下27B模型权重约为13.5GB，若配合KV Cache优化，可能无需频繁Swap全部未访问层，瓶颈机制描述过于绝对。 | 先验知识/题面给定，逻辑校验通过：PCIe 4.0 x16带宽限制确实会导致大模型在显存不足时吞吐量大幅下降，但具体数值和机制细节缺乏外部来源直接支持，且存在优化策略的可能性，故降级为定性表述。

## Search Query

RTX 4080 Super 16GB Qwen 27B INT8 offloading latency
