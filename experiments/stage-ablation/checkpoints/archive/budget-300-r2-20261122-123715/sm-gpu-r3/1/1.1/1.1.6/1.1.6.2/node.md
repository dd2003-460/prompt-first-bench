# N137: RTX 4060 Ti 16GB 运行 W4 Qwen3-27B 时，若将部分权重 (如最后几层或特定模块) Offload 至 CPU，其吞吐将受限于 CPU

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N33

## Claim

RTX 4060 Ti 16GB 运行 W4 Qwen3-27B 时，若将部分权重 (如最后几层或特定模块) Offload 至 CPU，其吞吐将受限于 CPU 内存带宽 (DDR5 ~50-80 GB/s) 与 GPU 计算能力的同步开销，实测吞吐通常降至 5-10 tok/s，而非 N33 声称的 15-25 tok/s，除非仅 Offload 极少量非关键参数

## Corrected Claim

RTX 4060 Ti 16GB 运行 W4 Qwen3-27B 时，若将部分权重 Offload 至 CPU，其吞吐将受限于 CPU 内存带宽与 GPU 计算能力的同步开销，实测吞吐通常显著低于纯 GPU 推理（可能降至个位数或低两位数 tok/s），具体数值取决于 Offload 比例与策略。

## Evidence

[质询]具体吞吐数值（5-10 tok/s vs 15-25 tok/s）高度依赖具体的 Offload 策略（如仅 Offload 最后几层 vs 大量层）、CPU 内存带宽实际值（DDR5 双通道理论峰值可达 90+ GB/s，但有效带宽受延迟影响）以及模型量化精度细节，缺乏统一基准测试支持该特定数值区间为绝对事实。 | 先验知识/题面给定，逻辑校验通过：Offload 至 CPU 确实受限于内存带宽，导致吞吐显著低于纯 GPU 推理，但具体数值范围因配置而异，故降级为定性表述。

## Search Query

RTX 4060 Ti 16GB Qwen 27B W4 offload throughput tokens per second
