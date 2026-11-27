# N95: FP8/INT8 精度下最小显存门槛计算：权重 27GB + KV Cache (32K, 4GB, 假设 KV 也量化) + 激活值 (4GB) + 框架开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

FP8/INT8 精度下最小显存门槛计算：权重 27GB + KV Cache (32K, 4GB, 假设 KV 也量化) + 激活值 (4GB) + 框架开销 (2GB) = 37GB。因此，显存 >= 40GB 的 GPU 可行，包括 RTX 6000 Ada (48GB), A100 80GB。若 KV Cache 保持 BF16 (8GB)，则需 41GB，仍排除 24GB 卡。

## Corrected Claim

FP8/INT8 精度下最小显存门槛计算：权重 27GB + KV Cache (32K, 4GB, 假设 KV 也量化) + 激活值 (4GB) + 框架开销 (2GB) = 37GB。因此，显存 >= 40GB 的 GPU 可行，包括 RTX 6000 Ada (48GB), A100 80GB。若 KV Cache 保持 BF16 (8GB)，则需 41GB，仍排除 24GB 卡。

## Evidence

先验知识/题面给定，逻辑校验通过：算术求和正确（27+4+4+2=37），显存门槛推导符合工程常识，GPU型号显存规格（RTX 6000 Ada 48GB, A100 80GB）准确。
