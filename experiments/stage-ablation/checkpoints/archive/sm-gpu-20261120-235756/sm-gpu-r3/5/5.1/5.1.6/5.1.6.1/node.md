# N288: vLLM PagedAttention 在高并发（Batch Size>=4）下的 OOM 风险阈值计算：Max_Batch_Size = (Total_VRA

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

vLLM PagedAttention 在高并发（Batch Size>=4）下的 OOM 风险阈值计算：Max_Batch_Size = (Total_VRAM - Weights_VRAM - Framework_Overhead) / (KV_Cache_Per_Request)，需代入 80GB 显存、54.36GB 权重、25.76GB/请求 KV 等参数，得出最大安全并发数，超出即触发 OOM。

## Corrected Claim

vLLM PagedAttention 在高并发（Batch Size>=4）下的 OOM 风险阈值计算：Max_Batch_Size = (Total_VRAM - Weights_VRAM - Framework_Overhead) / (KV_Cache_Per_Request)，需代入 80GB 显存、54.36GB 权重、25.76GB/请求 KV 等参数，得出最大安全并发数，超出即触发 OOM。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合显存分配逻辑，数值代入（(80-54.36)/25.76 ≈ 1.03）量级合理，无内部矛盾。

## Search Query

vLLM PagedAttention max batch size OOM threshold calculation 80GB GPU
