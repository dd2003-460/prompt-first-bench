# N183: RTX 4080 Super (16GB) 在 27B INT8 精度下的显存占用为 16.43GB (13.5GB 权重 + 1.93GB KV + 1GB 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

RTX 4080 Super (16GB) 在 27B INT8 精度下的显存占用为 16.43GB (13.5GB 权重 + 1.93GB KV + 1GB 激活)，超出 16GB 物理显存 0.43GB，导致 OOM 错误或需启用 CPU Offload，后者会使 TPS 下降 50-70%，因此该配置在标准 INT8 下不可行。

## Corrected Claim

RTX 4080 Super (16GB) 在 27B INT8 精度下的显存占用为 16.43GB (13.5GB 权重 + 1.93GB KV + 1GB 激活)，超出 16GB 物理显存 0.43GB，导致 OOM 错误或需启用 CPU Offload，后者会使 TPS 下降 50-70%，因此该配置在标准 INT8 下不可行。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT8权重约13.5GB，加上KV Cache和激活值后总显存需求16.43GB，确实超出16GB物理显存，导致OOM或需Offload，符合GPU显存管理的基本逻辑。
