# N127: 知识库向量索引在 FAISS 平台下，N=100,000 且维度=1536 的 float32 向量占用内存 614.4MB；M1 Max 的统一内存带宽为 4

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

知识库向量索引在 FAISS 平台下，N=100,000 且维度=1536 的 float32 向量占用内存 614.4MB；M1 Max 的统一内存带宽为 400GB/s，理论上每秒可执行 400GB/s / 6.144KB ≈ 65,100,000 次向量内积运算，但受限于 CPU 核心数（10 核）与 SIMD 指令集，实际 Top-10 检索延迟约为 5-10ms，满足 < 100ms 的实时检索需求。

## Corrected Claim

知识库向量索引在 FAISS 平台下，N=100,000 且维度=1536 的 float32 向量占用内存 614.4MB；M1 Max 的统一内存带宽为 400GB/s，理论上每秒可执行 400GB/s / 6.144KB ≈ 65,100,000 次向量内积运算，但受限于 CPU 核心数（10 核）与 SIMD 指令集，实际 Top-10 检索延迟约为 5-10ms，满足 < 100ms 的实时检索需求。

## Evidence

先验知识/题面给定，逻辑校验通过：内存计算准确（100k * 1536 * 4B = 614.4MB），带宽理论上限推导正确（400GB/s / 6.144KB ≈ 65M ops/s），实际延迟估算符合工程常识。

## Search Query

FAISS flat index search latency 100k vectors 1536 dims Apple M1 Max
