# N32: FP8 量化下的显存占用修正：FP8 权重占用 27.6GB (27e9 * 1 byte)，KV Cache 若保持 BF16 (通常推荐) 则仍为 8.6G

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

FP8 量化下的显存占用修正：FP8 权重占用 27.6GB (27e9 * 1 byte)，KV Cache 若保持 BF16 (通常推荐) 则仍为 8.6GB，若 KV 也量化为 FP8 则为 4.3GB。总需求分别为 36.2GB (KV-BF16) 或 31.9GB (KV-FP8)，需对比 32GB 卡片的实际可用显存 (通常 ~30-31GB 有效) 判断是否溢出。

## Corrected Claim

FP8 量化下的显存占用修正：FP8 权重占用 27.6GB (27e9 * 1 byte)，KV Cache 若保持 BF16 (通常推荐) 则仍为 8.6GB，若 KV 也量化为 FP8 则为 4.3GB。总需求分别为 36.2GB (KV-BF16) 或 31.9GB (KV-FP8)，需对比 32GB 卡片的实际可用显存 (通常 ~30-31GB 有效) 判断是否溢出。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为1字节，27e9参数对应27GB；KV Cache从BF16(2字节)降至FP8(1字节)减半，8.6GB->4.3GB符合量纲与算术逻辑；总显存计算及32GB卡有效显存约30-31GB的工程常识均自洽。

## Search Query

FP8 KV cache quantization memory saving LLM inference
