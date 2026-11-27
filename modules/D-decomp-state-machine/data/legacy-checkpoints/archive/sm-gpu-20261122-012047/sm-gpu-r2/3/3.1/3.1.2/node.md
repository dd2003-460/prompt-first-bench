# N94: INT4 量化在 RTX 4090 上的实际加速比受限于反量化开销：INT4 权重加载带宽需求减半（27 GB），理论吞吐提升至 37.4 tokens/s，但

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

INT4 量化在 RTX 4090 上的实际加速比受限于反量化开销：INT4 权重加载带宽需求减半（27 GB），理论吞吐提升至 37.4 tokens/s，但反量化至 BF16 进行矩阵乘法需额外 2-3 个 CUDA 核心周期，实测加速比通常为 2.0-2.5 倍（而非 N22 中的 2.5-3.5 倍），修正后 INT4 吞吐约为 30-37.5 tokens/s，与 N44 中 25-30 tokens/s 的实测值基本吻合（考虑 KV Cache 计算开销）。

## Corrected Claim

INT4 量化在 RTX 4090 上通过减少权重加载带宽需求（约减半）显著提升推理吞吐。虽然反量化至 BF16 进行计算会引入额外开销，限制了理论加速比的完全实现，但实测加速比通常在 2.0-3.0 倍之间（具体取决于 Kernel 优化程度，如 Marlin 等），修正后 INT4 吞吐约为 30-40 tokens/s，与实测值基本吻合。

## Evidence

[质询]陈述中关于“反量化需额外 2-3 个 CUDA 核心周期”的具体微观机制描述缺乏通用性且可能不准确（实际开销取决于 Kernel 实现，如 Marlin 或 GPTQ 的融合程度，而非固定的核心周期数）；此外，来源 [1] 标题声称“快 3 倍”，与陈述中“实测加速比通常为 2.0-2.5 倍”存在数值上的潜在冲突，需区分理想/特定场景与通用场景。 | 来源 [1] 和 [3] 证实了 INT4 量化在 RTX 4090 上的应用及加速效果（[1] 提及 3 倍加速，[3] 提及 Marlin kernels 优化），支持了量化带来显著加速的逻辑；但来源未提供“2-3 个 CUDA 核心周期”这一具体微观开销数据，且 [1] 的 3 倍加速与陈述的 2.0-2.5 倍存在差异，故降级为定性表述。

## Search Query

RTX 4090 INT4 quantization LLM inference speedup factor AWQ GPTQ measured tokens/s

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_28706923/article/details/160810764&rut=88221c7c23f67f9f9a0c28a180841aca2ad0a658d8b5b420e479137fbc99e956', 'type': 'ddg', 'title': '告别臃肿模型：用NVIDIA ModelOpt的INT4量化，让LLaMA-7B在RTX 4090上推理快3倍'}
- {'url': 'https://developer.aliyun.com/article/1750752&rut=94392af20a3b37d50183ceb74ab2c2490e3919f953e14e0dcc613071c8606abb', 'type': 'ddg', 'title': 'RTX 4090显存终极优化：模型分层加载、CPU Offload显存和内存动态置换实践.179'}
- {'url': 'https://gigagpu.com/rtx-4090-24gb-awq-quantization-guide/&rut=6f5f7ffb55eae3c1870335b0381b0c9f3b90ef3c485d2b20af36e808fa4cf4e1', 'type': 'ddg', 'title': 'AWQ INT4 Deep Dive on RTX 4090 24GB: Marlin Kernels, Calibration, and ...'}
