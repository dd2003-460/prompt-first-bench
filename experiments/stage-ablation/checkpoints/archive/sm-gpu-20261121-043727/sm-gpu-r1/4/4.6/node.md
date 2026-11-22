# N27: 数据中心 GPU (H100/H200) 内存带宽：H100 SXM 3.35TB/s, H200 4.8TB/s; 消费级 RTX 4090 1.0TB/s,

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

数据中心 GPU (H100/H200) 内存带宽：H100 SXM 3.35TB/s, H200 4.8TB/s; 消费级 RTX 4090 1.0TB/s, RTX 3090 936GB/s; 内存带宽直接决定 T_decode 上限，公式 T_decode_min = (L + KV_len) / (BW * MFU)

## Corrected Claim

数据中心 GPU (H100/H200) 内存带宽：H100 SXM 3.35TB/s, H200 4.8TB/s; 消费级 RTX 4090 1.0TB/s, RTX 3090 936GB/s; 内存带宽直接决定 T_decode 上限，公式 T_decode_min = (L + KV_len) / (BW * MFU)

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

H100 H200 RTX 4090 memory bandwidth LLM decode speed benchmark
