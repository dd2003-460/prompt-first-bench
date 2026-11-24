# N31: 自建POP的P99延迟构成项包括：用户到POP RTT (RTT_user_pop) + POP处理时间 (T_proc_pop) + 回源延迟 (若Miss:

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

自建POP的P99延迟构成项包括：用户到POP RTT (RTT_user_pop) + POP处理时间 (T_proc_pop) + 回源延迟 (若Miss: RTT_pop_origin + T_transfer_origin)，自建POP的RTT_user_pop通常低于公有云CDN（因物理距离更近或专用线路），但T_proc_pop可能高于公有云（因硬件性能差异）。

## Corrected Claim

自建POP的P99延迟构成项包括：用户到POP RTT (RTT_user_pop) + POP处理时间 (T_proc_pop) + 回源延迟 (若Miss: RTT_pop_origin + T_transfer_origin)，自建POP的RTT_user_pop通常低于公有云CDN（因物理距离更近或专用线路），但T_proc_pop可能高于公有云（因硬件性能差异）。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点准确拆解了父节点中提到的延迟构成项（RTT_user_pop, T_proc_pop, Miss概率, RTT_pop_origin, T_transfer_origin），各维度（物理距离、处理能力、缓存命中率、网络互联、带宽传输）相互独立且无重叠，完整覆盖了自建POP与公有云CDN在各项指标上的差异分析。）
