# N497: 对象大小分布对 P99 传输延迟的非线性影响：短视频对象大小 s 服从长尾分布，P99 对象大小 s_p99 通常为均值 s_avg 的 3-5 倍；因此 L_

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N159

## Claim

对象大小分布对 P99 传输延迟的非线性影响：短视频对象大小 s 服从长尾分布，P99 对象大小 s_p99 通常为均值 s_avg 的 3-5 倍；因此 L_trans_p99 = s_p99 / B_user_p99，而非 s_avg / B_avg。

## Corrected Claim

对象大小分布对 P99 传输延迟的非线性影响：短视频对象大小 s 服从长尾分布，P99 对象大小 s_p99 通常为均值 s_avg 的 3-5 倍；因此 L_trans_p99 = s_p99 / B_user_p99，而非 s_avg / B_avg。

## Evidence

先验知识/题面给定，逻辑校验通过：长尾分布下P99显著高于均值符合统计学常识，延迟计算逻辑自洽
