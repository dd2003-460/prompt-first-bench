# N123: BF16 权重加载时的峰值显存占用 = Weight_Size_GiB + Loader_Overhead，其中 Loader_Overhead 通常包含临时缓

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

BF16 权重加载时的峰值显存占用 = Weight_Size_GiB + Loader_Overhead，其中 Loader_Overhead 通常包含临时缓冲区，约为权重大小的 5-10% (即 2.5-5 GiB)，因此实际初始加载需预留 53-55 GiB 显存。

## Corrected Claim

BF16 权重加载时的峰值显存占用 = Weight_Size_GiB + Loader_Overhead，其中 Loader_Overhead 通常包含临时缓冲区，约为权重大小的 5-10% (即 2.5-5 GiB)，因此实际初始加载需预留 53-55 GiB 显存。

## Evidence

[质询]Loader_Overhead 的具体比例（5-10%）可能因加载策略（如是否启用 mmap、是否分块加载）而异，但在标准全量加载场景下，该量级符合工程经验。 | 先验知识/题面给定，逻辑校验通过：BF16 权重加载峰值显存通常由权重本体加上少量临时缓冲区（用于反序列化或类型转换）组成，5-10% 的开销在工程实践中是合理的量级估计，且无来源矛盾。
