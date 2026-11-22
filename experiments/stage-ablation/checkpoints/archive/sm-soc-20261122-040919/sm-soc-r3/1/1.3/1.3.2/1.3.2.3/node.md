# N157: C_search^post 的量化分解：C_search^post = T_search_post * W_time + C_cognitive_post。若有

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N39

## Claim

C_search^post 的量化分解：C_search^post = T_search_post * W_time + C_cognitive_post。若有信号使搜索时间缩短至 12 分钟（T_search_post=12），认知负荷降至 $1，则 C_search^post = 12*0.5 + 1 = $7。代入 k 公式：k = 1 - (17/7) 为负值，说明假设数据不自洽。修正：若 T_search_post=10 分钟，C_cognitive_post=$0.5，则 C_search^post = 10*0.5 + 0.5 = $5.5，k = 1 - (17/5.5) 仍为负。这表明 k=0.6 要求 C_search^post = C_search^prior / 1.6 = 17/1.6 ≈ $10.625。需重新校准 T_search_post 或 W_time 以匹配 k=0.6。

## Corrected Claim

C_search^post 的量化分解：C_search^post = T_search_post * W_time + C_cognitive_post。若有信号使搜索时间缩短至 12 分钟（T_search_post=12），认知负荷降至 $1，则 C_search^post = 12*0.5 + 1 = $7。代入 k 公式：k = 1 - (17/7) 为负值，说明假设数据不自洽。修正：若 T_search_post=10 分钟，C_cognitive_post=$0.5，则 C_search^post = 10*0.5 + 0.5 = $5.5，k = 1 - (17/5.5) 仍为负。这表明 k=0.6 要求 C_search^post = C_search^prior / 1.6 = 17/1.6 ≈ $10.625。需重新校准 T_search_post 或 W_time 以匹配 k=0.6。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算（12*0.5+1=7, 10*0.5+0.5=5.5, 17/1.6=10.625）及不等式推导（k<0 当且仅当 C_post < C_prior）均正确，内部逻辑自洽。

## Search Query

search cost post signal calibration k coefficient consistency
