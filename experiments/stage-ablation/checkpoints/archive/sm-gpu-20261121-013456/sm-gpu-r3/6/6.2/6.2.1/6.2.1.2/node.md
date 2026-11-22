# N247: NVIDIA A100 80GB PCIe 运行 Qwen3-27B (BF16) 的实测单流推理吞吐量（tokens/s），用于验证 N97 中 45 tok

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97

## Claim

NVIDIA A100 80GB PCIe 运行 Qwen3-27B (BF16) 的实测单流推理吞吐量（tokens/s），用于验证 N97 中 45 tokens/s 的估算值及临界吞吐量计算基础。

## Corrected Claim

NVIDIA A100 80GB PCIe 运行 Qwen3-27B (BF16) 的单流推理吞吐量估算约为 45 tokens/s，该数值与量化版本（如 Q4）下约 61 tokens/s 的估算值在量级上兼容，但缺乏 BF16 精度的直接实测数据佐证。

## Evidence

[质询]参考来源主要涉及 Qwen3.5/3.8 版本或 SXM 接口，且多为估算值或不同精度（Q4/FP8/INT8）下的数据，缺乏针对 Qwen3-27B BF16 在 PCIe 接口 A100 上的直接实测吞吐量数据，存在版本和硬件接口差异导致的数值偏差风险。 | 来源[1]提供了 A100 80GB PCIe 运行 27B 模型约 61 tok/s 的估算值（虽为 Q4 精度，但量级与 BF16 的 45 tok/s 估算相符，BF16 因显存带宽占用更高通常略低于量化版本），来源[2]和[3]确认了 A100 运行该规模模型的可行性，但无直接 BF16 PCIe 实测数据支持，故降级。

## Search Query

Qwen3-27B A100 80GB PCIe inference throughput tokens per second BF16 benchmark

## Retrieval Sources

- {'url': 'https://llmconfigurator.com/en/can-i-run/qwen3-5-27b-on-nvidia-a100-80gb&rut=a92b8fc3847d3059ea565a927ed6f5529548de7d0594cba3799a6181d115962b', 'type': 'ddg', 'title': 'Can I Run Qwen 3.5 27B on A100 80GB PCIe? | LLM Configurator'}
- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/166246073&rut=aa9cd260f6083109421d10da626cf8e35468718ee875d8897eb1b2d94d06853e', 'type': 'ddg', 'title': 'A100 跑 Qwen3.8-27B，FP8 还是 INT8？显存、速度、精度与微调兼容性怎么选_qwen3.8 27b'}
- {'url': 'https://henokb.github.io/blog/qwen-a100.html&rut=e0afef9395f2df50dc122bdad2f878893cb48a77ec9981db1c9cba0bd2e12ba8', 'type': 'ddg', 'title': 'Running Qwen3.5-27B on a Single A100 Henok Biadglign Ademtew'}
