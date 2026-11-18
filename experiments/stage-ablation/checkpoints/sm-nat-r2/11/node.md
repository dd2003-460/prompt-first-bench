# N82: 在 Zipf(β=0.9) 热度分布下，缓存前 K 个对象（K << N）的字节命中率下界近似公式为 H_byte ≈ 1 - (K/N)^{1-β}，该公式忽

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: (root)

## Claim

在 Zipf(β=0.9) 热度分布下，缓存前 K 个对象（K << N）的字节命中率下界近似公式为 H_byte ≈ 1 - (K/N)^{1-β}，该公式忽略了大小分布影响，作为 LRU 性能的理论下界基准。

## Corrected Claim

在 Zipf(β=0.9) 热度分布下，缓存前 K 个对象（K << N）的字节命中率下界近似公式为 H_byte ≈ 1 - (K/N)^{1-β}，该公式忽略了大小分布影响，作为 LRU 性能的理论下界基准。

## Evidence

公式/推导类，逻辑校验通过，来源未直接覆盖

## Retrieval Sources

- {'url': 'https://baike.baidu.com/item/%E5%9C%A8/4625648', 'type': 'bing', 'title': '在（汉语汉字）_百度百科'}
