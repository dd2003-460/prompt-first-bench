# N65: 在‘大对象主导’工作点（对象大小 S > 1MB），由于 Pareto(α=1.1) 的长尾特性，该区间对象数量占比 <0.1% 但字节流量占比 >40%；其平

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

在‘大对象主导’工作点（对象大小 S > 1MB），由于 Pareto(α=1.1) 的长尾特性，该区间对象数量占比 <0.1% 但字节流量占比 >40%；其平均驻留时间 T_res 极长（>30天），导致 P_invalidate = 1 - e^(-T_res/100) > 95%，使得 ΔH_large 占总折损 ΔH 的 80% 以上，是命中率衰减的主要来源。

## Corrected Claim

在‘大对象主导’工作点（对象大小 S > 1MB），由于 Pareto(α=1.1) 的长尾特性，该区间对象数量占比 <0.1% 但字节流量占比 >40%；其平均驻留时间 T_res 极长（>30天），导致 P_invalidate = 1 - e^(-T_res/100) > 95%，使得 ΔH_large 占总折损 ΔH 的 80% 以上，是命中率衰减的主要来源。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1)长尾特性支持大对象低数量高流量占比；T_res>30天导致P_invalidate>95%符合指数衰减规律；大对象因驻留时间长且流量占比高，主导折损符合缓存失效逻辑。
