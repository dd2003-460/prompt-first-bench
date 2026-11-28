# N117: Qwen3.8-27B 在 INT4 量化下的推理吞吐量受内存带宽限制，估算公式为 Throughput ≈ Memory_Bandwidth / (Model

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N37

## Claim

Qwen3.8-27B 在 INT4 量化下的推理吞吐量受内存带宽限制，估算公式为 Throughput ≈ Memory_Bandwidth / (Model_Size + KV_Cache_Size)；在 400GB/s 带宽下，若 Model_Size=14GB，理论最大吞吐约为 28 tokens/s，实际因 OS 开销降至 10-15 tokens/s，远低于 V100 集群的 50+ tokens/s，证实 Mac 仅适合编排。

## Corrected Claim

以 27B 参数大模型为例，在 INT4 量化下（模型权重约 14GB），受限于 400GB/s 内存带宽，理论最大推理吞吐量约为 28 tokens/s；实际部署中因计算效率、内存访问模式及系统调度等因素，实测吞吐量通常显著低于理论峰值（如 10-15 tokens/s），远低于高性能 GPU 集群（如 V100）的 50+ tokens/s，表明消费级 Mac 硬件更适合用于任务编排而非高吞吐推理。

## Evidence

[质询]模型名称 'Qwen3.8-27B' 疑似不存在或为虚构版本（当前主流为 Qwen2.5/Qwen3 系列，且 27B 参数在 INT4 下体积约 14GB 符合逻辑，但具体型号存疑）；此外，'OS 开销导致吞吐量从 28 降至 10-15' 的归因过于简化，实际瓶颈通常涉及计算单元效率、内存访问模式及调度延迟，而非单纯的 OS 开销。 | source=knowledge，逻辑校验通过：INT4 量化下 27B 模型权重约 13.5GB，加上 KV Cache 后总数据量约 14-16GB，400GB/s 带宽除以 14GB 确约为 28 tokens/s，量级合理；但具体型号及性能衰减归因缺乏外部来源直接支持，且 'Qwen3.8' 非标准公开型号名，故降级。

## Search Query

LLM inference throughput memory bound formula tokens per second
