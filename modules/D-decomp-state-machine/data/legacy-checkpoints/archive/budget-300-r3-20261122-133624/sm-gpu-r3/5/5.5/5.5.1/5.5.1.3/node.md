# N399: 若 FP8 不可行需回退至 BF16，显存需求从 27GB (INT8/FP8) 跃升至 54GB (BF16)，加上 32K 上下文的 KV Cache (约

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

若 FP8 不可行需回退至 BF16，显存需求从 27GB (INT8/FP8) 跃升至 54GB (BF16)，加上 32K 上下文的 KV Cache (约 4-6GB) 和框架开销 (2-4GB)，总需求约 60-64GB；这将排除所有单卡 < 64GB 的方案（如 4090 24GB, 5090 32GB, A100 40GB），仅保留 A100 80GB, H100 80GB, H200 141GB, MI300X 192GB 等数据中心级或高端专业卡。

## Corrected Claim

若 FP8 不可行需回退至 BF16，显存需求从 27GB (INT8/FP8) 跃升至 54GB (BF16)，加上 32K 上下文的 KV Cache (约 4-6GB) 和框架开销 (2-4GB)，总需求约 60-64GB；这将排除所有单卡 < 64GB 的方案（如 4090 24GB, 5090 32GB, A100 40GB），仅保留 A100 80GB, H100 80GB, H200 141GB, MI300X 192GB 等数据中心级或高端专业卡。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16权重显存约为INT8/FP8的2倍（27GB*2=54GB），加上KV Cache和框架开销后总需求60-64GB符合线性叠加逻辑，且该阈值正确排除了小于64GB显存的消费级/入门数据中心卡（如4090/5090/A100 40GB），保留了高端卡。

## Search Query

BF16 27B model memory requirement KV cache 32k context total VRAM usage
