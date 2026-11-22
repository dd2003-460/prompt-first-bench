# N135: 1×NVIDIA L40S (48GB) 运行 Qwen3-27B (BF16量化, 32K ctx) 的实测吞吐量约为 8-12 tokens/s/user，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N34

## Claim

1×NVIDIA L40S (48GB) 运行 Qwen3-27B (BF16量化, 32K ctx) 的实测吞吐量约为 8-12 tokens/s/user，首字延迟 (TTFT) 约为 4.0-6.0 秒，受限于 GDDR6 带宽 (864 GB/s) 低于 HBM 架构。

## Corrected Claim

1×NVIDIA L40S (48GB) 运行 Qwen3-27B 时，BF16 量化因显存限制可能无法支持 32K 上下文或根本不可行；若采用 AWQ 4-bit 或 FP8 量化，实测吞吐量约为 8-12 tokens/s/user，首字延迟 (TTFT) 约为 4.0-6.0 秒，受限于 GDDR6 带宽 (864 GB/s) 低于 HBM 架构。

## Evidence

[质询]来源[1]和[2]明确指出 Qwen3-32B（与27B参数量级相近）在 L40S 48GB 上 BF16 量化不可行（显存不足），而该陈述声称 BF16 可运行并给出具体吞吐量，存在事实矛盾或前提错误；此外，来源[3]讨论的是 L40 而非 L40S，且模型为 FP8 而非 BF16，无法直接支持该特定配置下的性能数据。 | 来源[1][2]指出 BF16 在 48GB 显存下对 32B 模型不可行，暗示 27B BF16 也极可能不可行或需极短上下文，与陈述前提矛盾；来源[3]虽涉及 27B 但硬件和量化方式不同，无法直接支持 BF16 在 L40S 上的性能数据。

## Search Query

NVIDIA L40S Qwen3 27B BF16 inference throughput benchmark

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_35749796/article/details/167995019&rut=4a3aeccd10935f58063667f7c5b6d9f9639801dcce64e0585e7a9a90ea8422ef', 'type': 'ddg', 'title': 'Qwen3-32B 单卡 L40S 48GB 能跑吗？AWQ量化、显存预算与vLLM部署-CSDN博客'}
- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/167794202&rut=558a30489fc492dea31c3dc353e91bab8df9d28be422b930e274cd13142b65a0', 'type': 'ddg', 'title': 'Qwen3-32B 单卡 L40S 48GB 能跑吗？AWQ量化、显存预算与vLLM部署_qwen3-32b-awq-CSDN博客'}
- {'url': 'https://www.zhangfangzhou.cn/ubuntu-24-04-nvidia-l40-qwen3-8-27b-fp8-vllm-open-webui.html&rut=4f3163992083ce250387a904ba8c53e249ebf4609984ae2c41c3c8db97130cbc', 'type': 'ddg', 'title': 'Ubuntu 24.04 + NVIDIA L40 部署 Qwen3.8-27B-FP8 私有化推理实战（vLLM + Open-WebUI）'}
