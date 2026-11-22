# N206: RTX 4090 24GB 显存下的总可用显存修正：24 GB 物理显存中，CUDA Context、驱动及系统保留开销通常占用 0.5-1.0 GB，vLLM

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

RTX 4090 24GB 显存下的总可用显存修正：24 GB 物理显存中，CUDA Context、驱动及系统保留开销通常占用 0.5-1.0 GB，vLLM/TensorRT 框架基础开销约 0.5 GB，因此实际可用于模型+KV 的显存约为 22.5-23.0 GB。

## Corrected Claim

RTX 4090 24GB 显存下的总可用显存修正：24 GB 物理显存中，CUDA Context、驱动及系统保留开销通常占用 0.5-1.0 GB，vLLM/TensorRT 框架基础开销约 0.5 GB，因此实际可用于模型+KV 的显存约为 22.5-23.0 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB显存扣除0.5-1.0GB系统/驱动开销及0.5GB框架开销后，剩余22.5-23.0GB符合工程常识与量级逻辑。

## Search Query

RTX 4090 usable VRAM after CUDA context overhead
