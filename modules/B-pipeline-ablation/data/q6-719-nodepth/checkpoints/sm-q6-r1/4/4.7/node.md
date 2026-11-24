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

先验知识/题面给定，逻辑校验通过：延迟构成符合网络传输基本模型（RTT+处理+回源），且自建POP因物理距离近导致RTT低、因硬件规模小导致处理时间可能高的推断符合工程直觉。
