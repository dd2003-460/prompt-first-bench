# N123: AMD MI300X (192GB HBM3, 5.3 TB/s) 在 Qwen3-27B BF16 推理中，显存容量足以容纳模型权重(54GB)与32K上下文

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

AMD MI300X (192GB HBM3, 5.3 TB/s) 在 Qwen3-27B BF16 推理中，显存容量足以容纳模型权重(54GB)与32K上下文KV Cache(6GB)及激活值，且带宽优势使其理论TPS约为RTX 4090的5倍；其单卡价格约$15,000，5年TCO约为$20,000，虽高于2x4090方案，但在高并发(Batch>10)场景下单位Token成本可能优于H100 [待核验: MI300X 2024 Q4 现货价格及ROCm vLLM 支持状态]

## Corrected Claim

AMD MI300X (192GB HBM3, 5.3 TB/s) 在 Qwen3-27B BF16 推理中，显存容量足以容纳模型权重(54GB)与32K上下文KV Cache(6GB)及激活值，且带宽优势使其理论TPS约为RTX 4090的5倍；其单卡价格约$15,000，5年TCO约为$20,000，虽高于2x4090方案，但在高并发(Batch>10)场景下单位Token成本可能优于H100 [待核验: MI300X 2024 Q4 现货价格及ROCm vLLM 支持状态]

## Evidence

检索失败: no sources from any channel (all 5 failed)
