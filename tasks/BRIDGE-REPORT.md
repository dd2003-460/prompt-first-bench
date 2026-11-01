# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: rejudge-g1b 盲判 75 cell（arena judge 外包首跑）
- commit: b7+summary 已 push ralph/rv3g1-semantic-rejudge
- 验收自检: 75/75 cell 全量判定落盘 results/b1-b7.json + rejudge-g1b-summary.json；每批回执含 per-cell score+reason
- 结论: **arena judge 外包全流程跑通**（单裁判 75/75 + 分歧复核 4/4）。分布 0x32/1x26/2x19；run 排名 run7(1.09)>run2(0.89)>run6(0.88)>run1(0.86)>run8(0.82)>run3(0.78)>run5(0.58)>run4(0.50)。6 类节点跨 run 全 0（结构性缺失）：duty_demand/util/MFU/prefill_flops/cache_hit/带宽准入。分歧复核：4 个 prior_h=1 且 quality=0 的 cell 全部确认 miss——**prior_h=1 是假阳性（输入参数里的数字被误判为拆解）**，G1 flag 方向再获支持。剩余：① 真·dual-rater（两个不同模型各判一遍，本次是同模型二判 conf~0.7）② 回灌 G1 修正表 ③ 与 r158 h 重判交叉分析。
