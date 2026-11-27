# N158: RTX 4090 (Ada Lovelace) 原生 FP8 推理相比 BF16 的实测加速比：在 LLM Decode 阶段（内存受限），由于权重体积减半（2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

RTX 4090 (Ada Lovelace) 原生 FP8 推理相比 BF16 的实测加速比：在 LLM Decode 阶段（内存受限），由于权重体积减半（27.2B * 1 byte vs 2 bytes），理论带宽需求减半，但受限于 DRAM 控制器效率，实际 T_decode 加速比通常为 1.4x-1.8x；在 Prefill 阶段（计算受限），FP8 Tensor Core 峰值算力为 BF16 的 2 倍，但受 MFU 下降影响，实际加速比约为 1.5x-1.7x。

## Corrected Claim

RTX 4090 (Ada Lovelace) 原生 FP8 推理相比 BF16 的实测加速比受具体实现、模型大小及硬件配置影响较大，部分基准测试显示在特定条件下（如包含视觉模块或不同上下文长度）FP8 可能未表现出预期的 1.4x-1.8x 加速，甚至出现性能下降，需结合具体部署场景评估。

## Evidence

[质询]来源[1]提供的数据（BF16 178.72 tok/s vs FP8 136.47 tok/s）显示FP8速度反而更慢，这与陈述中声称的1.4x-1.8x加速比直接矛盾；且该来源可能涉及不同模型配置或包含视觉模块开销，无法直接支持纯LLM Decode的加速比结论。 | 逻辑上FP8在内存受限阶段因带宽减半应有加速，但参考来源[1]显示FP8吞吐量低于BF16，存在矛盾或特定条件限制，缺乏直接支持加速比数值的外部证据。

## Search Query

RTX 4090 FP8 vs BF16 LLM inference speedup benchmark

## Retrieval Sources

- {'url': 'https://github.com/AnnoyingTechnology/nvidia-4090-llm-inference&rut=cfa37504331b91f17b5db4873ad88d3d7f14b17b29af749ed1abe143534c5b87', 'type': 'ddg', 'title': 'NVIDIA RTX 4090 local inference - GitHub'}
