# N240: Qwen3-27B W4 量化下的权重显存占用：27e9 * 0.5 bytes = 13.5 GB (假设使用 4-bit 量化，如 GPTQ/AWQ 或 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Qwen3-27B W4 量化下的权重显存占用：27e9 * 0.5 bytes = 13.5 GB (假设使用 4-bit 量化，如 GPTQ/AWQ 或 GGUF Q4_K_M)，加上量化校准数据 (Scale/Zero Point) 约 0.5-1 GB，总权重占用约 14-15 GB。

## Corrected Claim

Qwen3-27B W4 量化下的权重显存占用：27e9 * 0.5 bytes = 13.5 GB (假设使用 4-bit 量化，如 GPTQ/AWQ 或 GGUF Q4_K_M)，加上量化校准数据 (Scale/Zero Point) 约 0.5-1 GB，总权重占用约 14-15 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在4-bit量化下基础权重约13.5GB，加上Scale/Zero Point等元数据约0.5-1GB，总占用14-15GB符合工程常识与数学推导。
