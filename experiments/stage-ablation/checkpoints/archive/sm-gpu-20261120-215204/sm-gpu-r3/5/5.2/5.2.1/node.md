# N125: 2×RTX 4090 (PCIe 4.0) 运行 W4 Qwen3-27B 的并行效率损耗：由于无 NVLink，KV Cache 跨卡同步带宽受限 (32 G

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

2×RTX 4090 (PCIe 4.0) 运行 W4 Qwen3-27B 的并行效率损耗：由于无 NVLink，KV Cache 跨卡同步带宽受限 (32 GB/s)，实测吞吐通常为单卡理想值的 60-70% (即 ~25-30 Tokens/s)，且 TTFT 因跨卡 AllReduce 增加 30-50%。

## Corrected Claim

2×RTX 4090 (PCIe 4.0) 运行 W4 27B 模型时，由于无 NVLink，KV Cache 跨卡同步受 PCIe 带宽限制，并行效率低于理想线性扩展。实测 Tensor Parallel 吞吐通常显著高于单卡串行处理，但低于理论峰值；具体吞吐取决于并发数和上下文长度，单并发下可达 100+ Tokens/s，而非仅 25-30 Tokens/s。

## Evidence

[质询]来源[2]明确测试了2x RTX 4090运行27B W4A16模型（与claim中的W4 Qwen3-27B高度相似），其Tensor Parallel实测吞吐在单并发下为110 tok/s，远高于claim中声称的25-30 tok/s。Claim中的数值量级与现有公开基准测试存在显著偏差，可能混淆了不同并发度、不同模型架构或特定极端配置下的数据，或者错误地高估了PCIe瓶颈对单流推理的影响。 | 来源[2]直接测试了2x RTX 4090 PCIe环境下的27B W4模型，显示Tensor Parallel吞吐显著高于claim所述的25-30 tok/s（实测110 tok/s @ 1 req），表明claim中的具体数值缺乏支持且与现有证据矛盾，但PCIe带宽受限导致效率低于理想值的定性逻辑成立。

## Search Query

2x RTX 4090 PCIe tensor parallelism efficiency loss LLM inference

## Retrieval Sources

- {'url': 'https://gigagpu.com/rtx-4090-24gb-multi-card-pairing/&rut=c56554f2fb848c6da7bd537dfee9bef3895c436ae0c094ad1e544903103a0848', 'type': 'ddg', 'title': '2x RTX 4090 24GB Pairing for Tensor Parallel Inference'}
- {'url': 'https://paraloncloud.com/resources/tensor-parallel-vs-data-parallel-2x-rtx-4090&rut=205573e96012e93ba110c601014924eceaa5691f7fdbfe316af86ebb9e7240c1', 'type': 'ddg', 'title': 'Tensor Parallel vs Data Parallel on 2x RTX 4090 (PCIe): vLLM Benchmarks ...'}
- {'url': 'https://willitrunai.com/blog/2x-rtx-4090-llm-guide&rut=2a2ace8a3a75d508f9bda9cef715e864c36bfea12d19c6612ff8965768afd830', 'type': 'ddg', 'title': '2x RTX 4090 for LLMs: Memory Limits, PCIe and Setup'}
