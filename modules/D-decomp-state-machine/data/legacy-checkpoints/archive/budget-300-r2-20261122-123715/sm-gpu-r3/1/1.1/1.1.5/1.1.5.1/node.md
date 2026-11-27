# N133: RTX 3090 在 W4 量化下的理论解码吞吐上限由显存带宽决定：Throughput_max = BW / (Weight_Size + KV_Cache_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

RTX 3090 在 W4 量化下的理论解码吞吐上限由显存带宽决定：Throughput_max = BW / (Weight_Size + KV_Cache_Size_Per_Token)，其中 Weight_Size=13.5GB，KV_Cache_Size_Per_Token ≈ 0.5MB (GQA INT8)，计算得 936 GB/s / 13.5 GB ≈ 69 tok/s (仅权重加载瓶颈)，实际受计算单元 (CUDA Cores) 限制

## Corrected Claim

RTX 3090 在 W4 量化下的理论解码吞吐上限由显存带宽决定：Throughput_max = BW / (Weight_Size + KV_Cache_Size_Per_Token)，其中 Weight_Size=13.5GB，KV_Cache_Size_Per_Token ≈ 0.5MB (GQA INT8)，计算得 936 GB/s / 13.5 GB ≈ 69 tok/s (仅权重加载瓶颈)，实际受计算单元 (CUDA Cores) 限制

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090显存带宽936GB/s，W4量化下13.5GB权重加载瓶颈计算936/13.5≈69tok/s，量纲与数值合理

## Search Query

RTX 3090 W4 inference theoretical throughput bandwidth bound calculation
