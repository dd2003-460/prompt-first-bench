# N163: NVIDIA A100 80GB (FP8) 运行 Qwen3-27B 的实测解码吞吐量 (Decode Throughput) 具体数值 (tokens/s,

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N47

## Claim

NVIDIA A100 80GB (FP8) 运行 Qwen3-27B 的实测解码吞吐量 (Decode Throughput) 具体数值 (tokens/s, batch=1)，需确认 A100 是否通过 TensorRT-LLM 或 vLLM 支持 FP8 内核加速，若不支持原生 FP8 硬件加速则需注明是软件模拟 FP8 导致的性能折损。

## Corrected Claim

NVIDIA A100 80GB 不支持原生 FP8 W8A8 硬件加速，运行 Qwen3-27B 时 FP8 通常仅支持权重-only 路径（软件模拟/兼容模式），具体解码吞吐量数值需参考特定框架（如 TensorRT-LLM/vLLM）的实测基准测试，现有来源未提供具体 tokens/s 数值。

## Evidence

[质询]陈述要求提供具体的实测解码吞吐量数值（tokens/s），但参考来源仅提供了定性结论（A100不支持原生FP8 W8A8，仅支持权重-only路径），未包含任何具体的吞吐量数值数据，导致无法验证具体数值。 | 来源[1]和[2]直接支持了'A100不支持原生FP8 W8A8计算，FP8多为权重-only路径'这一技术事实，但均未提供具体的解码吞吐量数值，属于经验事实且缺乏具体数值来源支持。

## Search Query

A100 80GB Qwen3-27B FP8 inference throughput tokens per second TensorRT vLLM

## Retrieval Sources

- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=e3cd8298d24ee38efaf6e83db008eeefc3c08b20cce58b5d0907c30b182ca289', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
- {'url': 'https://jishuzhan.net/article/2102237572693676033&rut=95b6da85ca8aa114a950546b026f40d1cadbc4a21cba1ca376353dbd38ce32ee', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选 - 技术栈'}
