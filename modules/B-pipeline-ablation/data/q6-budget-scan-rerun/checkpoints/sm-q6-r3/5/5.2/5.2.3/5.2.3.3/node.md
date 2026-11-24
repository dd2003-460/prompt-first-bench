# N263: 城市流量占比 P_i 的计算公式：P_i = (DAU_i × ARPU_req_i) / Σ(DAU_j × ARPU_req_j)，其中DAU_i为城市i日

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N96

## Claim

城市流量占比 P_i 的计算公式：P_i = (DAU_i × ARPU_req_i) / Σ(DAU_j × ARPU_req_j)，其中DAU_i为城市i日活用户数，ARPU_req_i为人均请求数，需基于500万日活用户的地域分布数据（如北京5%、上海4.5%、广州3%等）及用户行为差异计算

## Corrected Claim

城市流量占比 P_i 的计算公式：P_i = (DAU_i × ARPU_req_i) / Σ(DAU_j × ARPU_req_j)，其中DAU_i为城市i日活用户数，ARPU_req_i为人均请求数，需基于500万日活用户的地域分布数据（如北京5%、上海4.5%、广州3%等）及用户行为差异计算

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

China internet user city distribution DAU ratio 2023
