# N283: 精度选择对显存利用率的敏感度分析：FP8 权重 (27GB) 允许最大 Batch=4 (KV 16.12GB)，INT4 权重 (13.5GB) 允许最大 B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N93

## Claim

精度选择对显存利用率的敏感度分析：FP8 权重 (27GB) 允许最大 Batch=4 (KV 16.12GB)，INT4 权重 (13.5GB) 允许最大 Batch=12 (KV 48.36GB > 48GB 不可行，实际 Batch=10, KV 40.3GB)，FP8 方案在质量损失与 Batch Size 间取得最佳平衡。

## Corrected Claim

INT4 权重 (13.5GB) 下，若 Batch=10 时 KV Cache 为 40.3GB，总显存需求 53.8GB 超过 48GB 限制，故 Batch=10 不可行；实际最大可行 Batch 应小于 10（例如 Batch=8，KV≈32.24GB，总显存≈45.74GB）。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算自洽（FP8: 27+16.12=43.12GB<48GB; INT4: 13.5+40.3=53.8GB>48GB，故Batch=10不可行需调整或原陈述中KV 40.3GB对应Batch=10时总显存超限，但陈述指出INT4允许最大Batch=12不可行，实际Batch=10，此处逻辑需细究：若INT4权重13.5GB，剩余34.5GB给KV。若Batch=10时KV=40.3GB，则13.5+40.3=53.8GB>48GB，说明Batch=10也不可行？或者陈述意思是INT4方案下，理论最大Batch=12对应KV 48.36GB（总61.86GB）不可行，而实际可行最大Batch=10对应KV 40.3GB（总53.8GB）仍不可行？这里存在逻辑矛盾。重新检查：通常KV Cache大小与Batch成正比。若Batch=12时KV=48.36GB，则每Batch KV=4.03GB。Batch=10时KV=40.3GB。INT4权重13.5GB。总显存=13.5+40.3=53.8GB > 48GB。所以Batch=10在48GB显存下也是不可行的。陈述说“实际 Batch=10”，暗示这是可行的，但数值上不可行。这是一个硬逻辑错误/数值矛盾。
