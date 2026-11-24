# N317: 缓存预热时间（Cache_Warmup_Time）取决于回源带宽瓶颈与热门内容大小：Warmup_Time = (Top_K_Hot_Content_Size 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N123

## Claim

缓存预热时间（Cache_Warmup_Time）取决于回源带宽瓶颈与热门内容大小：Warmup_Time = (Top_K_Hot_Content_Size / Effective_Backhaul_Bandwidth)。若Top-1000热门内容总计5GB，回源带宽1Gbps（125MB/s），则Warmup_Time ≈ 40s；自建POP回源带宽若仅100Mbps，则Warmup_Time ≈ 400s。

## Corrected Claim

缓存预热时间（Cache_Warmup_Time）取决于回源带宽瓶颈与热门内容大小：Warmup_Time = (Top_K_Hot_Content_Size / Effective_Backhaul_Bandwidth)。若Top-1000热门内容总计5GB，回源带宽1Gbps（125MB/s），则Warmup_Time ≈ 40s；自建POP回源带宽若仅100Mbps，则Warmup_Time ≈ 400s。

## Evidence

先验知识/题面给定，逻辑校验通过：5GB / 125MB/s = 40s，5GB / 12.5MB/s = 400s，计算准确且符合物理直觉。
