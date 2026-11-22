# N53: N7 中提到的 '激活值缓冲' 不应计入静态 KV Cache 占用，因为激活值 (Activations) 是动态分配的，且通常不占用显存峰值的主要部分（相对

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

N7 中提到的 '激活值缓冲' 不应计入静态 KV Cache 占用，因为激活值 (Activations) 是动态分配的，且通常不占用显存峰值的主要部分（相对于 KV Cache 而言），其大小取决于 batch size 和中间层维度，需单独估算而非固定加 1.1 GB。

## Corrected Claim

N7 中提到的 '激活值缓冲' 不应计入静态 KV Cache 占用，因为激活值 (Activations) 是动态分配的，且通常不占用显存峰值的主要部分（相对于 KV Cache 而言），其大小取决于 batch size 和中间层维度，需单独估算而非固定加 1.1 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：激活值（Activations）确实是动态分配的中间变量，其大小随 batch size 和层维度变化，与静态 KV Cache 性质不同，不应简单固定加算。
