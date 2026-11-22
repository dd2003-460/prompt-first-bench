# N37: LRU字节命中率下界的具体数值估算：基于N_resident≈8000-10000个对象，覆盖Top 8%-10%对象，请求覆盖率P_access≈85%-90

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

LRU字节命中率下界的具体数值估算：基于N_resident≈8000-10000个对象，覆盖Top 8%-10%对象，请求覆盖率P_access≈85%-90%，字节命中率H_lru ≈ P_access * (S_hot_avg / E[S]) ≈ 0.87 * 0.6 ≈ 52%-55%（考虑大小加权后的保守下界）。

## Corrected Claim

LRU字节命中率下界的具体数值估算：基于N_resident≈8000-10000个对象，覆盖Top 8%-10%对象，请求覆盖率P_access≈85%-90%，字节命中率H_lru ≈ P_access * (S_hot_avg / E[S]) ≈ 0.87 * 0.6 ≈ 52%-55%（考虑大小加权后的保守下界）。

## Evidence

先验知识/题面给定，逻辑校验通过
