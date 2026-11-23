# N41: 短视频大小分布 $P(s|vid)$ 呈右偏长尾分布，均值 7.5 MB，95% 分位数 $s_{vid,95}$ 约为 20 MB，99% 分位数 $s_{v

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

短视频大小分布 $P(s|vid)$ 呈右偏长尾分布，均值 7.5 MB，95% 分位数 $s_{vid,95}$ 约为 20 MB，99% 分位数 $s_{vid,99}$ 可能达到 50 MB，需考虑极端大文件对单流传输时间的影响。

## Corrected Claim

短视频大小分布 $P(s|vid)$ 呈右偏长尾分布，均值 7.5 MB，95% 分位数 $s_{vid,95}$ 约为 20 MB，99% 分位数 $s_{vid,99}$ 可能达到 50 MB，需考虑极端大文件对单流传输时间的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：短视频文件大小通常呈右偏长尾分布，均值7.5MB、95分位20MB、99分位50MB的量级符合常见视频编码与时长分布的工程经验，数值间逻辑自洽（均值<95分位<99分位），且无来源矛盾。

## Search Query

short video file size distribution long tail 99th percentile
