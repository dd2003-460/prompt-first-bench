# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: rejudge-g1b 盲判 75 cell（arena judge 外包首跑）
- commit: b7+summary 已 push ralph/rv3g1-semantic-rejudge
- 验收自检: 75/75 cell 全量判定落盘 results/b1-b7.json + rejudge-g1b-summary.json；每批回执含 per-cell score+reason
- 结论: **单裁判 arena pass 完成**。分布 0x32/1x26/2x19；run 排名 run7(1.09)>run2(0.89)>run6(0.88)>run1(0.86)>run8(0.82)>run3(0.78)>run5(0.58)>run4(0.50)。系统性缺口（跨 run 全 0）：duty_demand(N-2.1)/util(N-2,N-2.2)/MFU(N-3.1.3)/prefill_flops(N-3.1.1)/cache_hit(N-5.3)/带宽准入(N-5.2)。**G1 审计的 3 个 flag 方向获支持**：judge 先验 p̃ 对"结构性缺失节点"确实高估了命中率。下一步：① dual-rater Battle 复核分歧大的 cell（runner v3.1 协议）；② 把 rejudge 结果回灌 G1 修正表。
