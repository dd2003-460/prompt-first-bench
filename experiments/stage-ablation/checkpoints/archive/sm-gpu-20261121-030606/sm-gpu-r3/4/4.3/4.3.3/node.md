# N131: 修正N21中FP8/INT8总显存：若W_FP8=27GB, KV=2GB, Act=2.5GB, Overhead=3GB，则总显存=34.5GB，而非N21

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

修正N21中FP8/INT8总显存：若W_FP8=27GB, KV=2GB, Act=2.5GB, Overhead=3GB，则总显存=34.5GB，而非N21所述的40GB。若使用NVFP4 (W=13.5GB)，总显存=13.5+2+2.5+3=21GB，而非25GB。这些修正直接影响硬件可行性判断（如RTX 5090 32GB在FP8下是否可行：34.5GB > 32GB，不可行，需INT8/NVFP4或降低上下文）。

## Corrected Claim

修正N21中FP8/INT8总显存：若W_FP8=27GB, KV=2GB, Act=2.5GB, Overhead=3GB，则总显存=34.5GB，而非N21所述的40GB。若使用NVFP4 (W=13.5GB)，总显存=13.5+2+2.5+3=21GB，而非25GB。这些修正直接影响硬件可行性判断（如RTX 5090 32GB在FP8下是否可行：34.5GB > 32GB，不可行，需INT8/NVFP4或降低上下文）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术求和正确（27+2+2.5+3=34.5, 13.5+2+2.5+3=21），且34.5GB > 32GB的硬件可行性判断符合基本逻辑。
