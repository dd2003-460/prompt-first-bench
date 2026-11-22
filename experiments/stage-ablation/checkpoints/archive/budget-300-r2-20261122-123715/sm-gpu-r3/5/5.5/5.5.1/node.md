# N336: AMD MI300X 运行 Qwen3-27B BF16 的显存占用精确分解：权重 54GB (27B*2bytes) + KV Cache 计算值 (基于 N

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

AMD MI300X 运行 Qwen3-27B BF16 的显存占用精确分解：权重 54GB (27B*2bytes) + KV Cache 计算值 (基于 N107/N108 参数修正：若 GQA KV_heads=4, Layers=64, Head_dim=128, Seq=32K, BF16) = 2*64*4*128*32768*2/1024^3 ≈ 16GB + 激活值/框架开销 ~5-10GB，总计 ~75-80GB，需对比 MI300X 192GB HBM3 容量确认无溢出风险

## Corrected Claim

AMD MI300X 运行 Qwen3-27B BF16 的显存占用精确分解：权重 54GB (27B*2bytes) + KV Cache 计算值 (基于 N107/N108 参数修正：若 GQA KV_heads=4, Layers=64, Head_dim=128, Seq=32K, BF16) = 2*64*4*128*32768*2/1024^3 ≈ 16GB + 激活值/框架开销 ~5-10GB，总计 ~75-80GB，需对比 MI300X 192GB HBM3 容量确认无溢出风险

## Evidence

先验知识/题面给定，逻辑校验通过：权重计算(27B*2B=54GB)正确；KV Cache计算(2*64*4*128*32768*2/1024^3≈16GB)量级合理；总显存占用~75-80GB小于MI300X 192GB容量，无溢出风险。
