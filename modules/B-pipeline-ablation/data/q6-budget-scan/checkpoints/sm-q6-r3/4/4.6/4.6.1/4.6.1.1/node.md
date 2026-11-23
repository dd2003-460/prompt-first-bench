# N286: 核心区域日均请求数 R_req_core = 320,000 次/日，计算过程：Traffic_TB_core (1.6TB) / s_avg (5MB) = 

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N89

## Claim

核心区域日均请求数 R_req_core = 320,000 次/日，计算过程：Traffic_TB_core (1.6TB) / s_avg (5MB) = 1600GB / 5MB = 320,000 次

## Corrected Claim

核心区域日均请求数 R_req_core = 320,000 次/日，计算过程：Traffic_TB_core (1.6TB) / s_avg (5MB) = 1600GB / 5MB = 320,000 次

## Evidence

先验知识/题面给定，逻辑校验通过：1.6TB = 1600GB，1600GB / 5MB = 1600 * 1024 MB / 5 MB = 327,680 次，与 320,000 次在工程估算精度内一致（若按 1TB=1000GB 计算则精确为 320,000 次），量纲与数值合理。
