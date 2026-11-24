# N573: 用户到最近节点的地理距离分布差异：阿里云用户平均最近节点距离 d_ali ≈ 50-100km（核心城市）/ 150-300km（长尾），Cloudflare 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N187

## Claim

用户到最近节点的地理距离分布差异：阿里云用户平均最近节点距离 d_ali ≈ 50-100km（核心城市）/ 150-300km（长尾），Cloudflare 用户平均最近节点距离 d_cf ≈ 100-200km（核心城市）/ 300-500km（长尾），导致 RTT_ali 比 RTT_cf 低 5-15ms。

## Corrected Claim

阿里云用户平均最近节点距离通常显著小于Cloudflare用户（尤其在核心城市），导致RTT_ali通常比RTT_cf低若干毫秒（具体数值随地区和测量条件波动）。

## Evidence

[质询]具体数值区间（如50-100km, 150-300km）及RTT差值（5-15ms）属于高度依赖具体网络拓扑、用户分布及测量时间的经验数据，缺乏公开权威统计支持，且不同地区/时期波动极大，精确区间断言风险高。 | 逻辑自洽：阿里云在中国大陆节点密度显著高于Cloudflare（主要面向全球/海外），因此用户平均距离更近、RTT更低符合物理直觉和工程常识；但具体数值区间为经验估计，无来源直接支持，且source为knowledge，依据规则中'经验事实排除条款'虽不适用knowledge节点直接降级，但鉴于数值过于具体且无外部验证，保守判定为degraded以反映不确定性（注：若严格遵循knowledge节点'逻辑自洽即verified'规则，此处应判verified，但考虑到数值的具体性远超一般'量级'描述，且提示词中强调'若攻击点成立且无法排除，判定应相应降档'，故选择degraded更为严谨）。

## Search Query

Alibaba vs Cloudflare CDN distance to nearest node China
