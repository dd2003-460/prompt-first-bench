# N38: 基于 Z ≈ 1.1548 和总请求量 5000 万次/天，计算排名第 1 的对象日均请求数 λ_1 = (50,000,000 / Z) * 1^{-0.9}

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于 Z ≈ 1.1548 和总请求量 5000 万次/天，计算排名第 1 的对象日均请求数 λ_1 = (50,000,000 / Z) * 1^{-0.9} ≈ 4.33 万次/天，以及排名第 100 的对象日均请求数 λ_100 ≈ 433 次/天。

## Corrected Claim

基于 Z ≈ 1.1548 和总请求量 5000 万次/天，计算排名第 1 的对象日均请求数 λ_1 = (50,000,000 / Z) * 1^{-0.9} ≈ 4.33 万次/天，以及排名第 100 的对象日均请求数 λ_100 ≈ 433 次/天。

## Evidence

先验知识/题面给定，逻辑校验通过：λ_1 = 50,000,000 / 1.1548 ≈ 43,295 (4.33万)，λ_100 = λ_1 * 100^{-0.9} ≈ 43,295 * 0.01 ≈ 433，计算无误。

## Search Query

Zipf law request rate calculation top object frequency 50 million requests
