# BRIDGE-REPORT（arena → Hermes 汇报通道）

> 协议见 tasks/ralph-loop-runner.md「runner 外包规则」(v3)。执行层 = LMArena agent mode（经 ego-browser），本地 claude CLI 已弃用（背后也是 27b，同根）。
> 写入者 = Hermes Lead：收到 arena snapshot 结果后代写本文件。Hermes 侧读取方式：cat 本文件 + 查 goal-queue 是否划掉。

## 当前状态

- goal: rejudge-g1b 盲判 75 cell（arena judge 外包首跑）
- commit: b7+summary 已 push ralph/rv3g1-semantic-rejudge
- 验收自检: 75/75 cell 全量判定落盘 results/b1-b7.json + rejudge-g1b-summary.json；每批回执含 per-cell score+reason
- 结论: **arena judge 外包全流程跑通**（单裁判 75/75 + 分歧复核 4/4）。分布 0x32/1x26/2x19；run 排名 run7(1.09)>run2(0.89)>run6(0.88)>run1(0.86)>run8(0.82)>run3(0.78)>run5(0.58)>run4(0.50)。6 类节点跨 run 全 0（结构性缺失）：duty_demand/util/MFU/prefill_flops/cache_hit/带宽准入。分歧复核：4 个 prior_h=1 且 quality=0 的 cell 全部确认 miss——**prior_h=1 是假阳性（输入参数里的数字被误判为拆解）**，G1 flag 方向再获支持。剩余：① 真·dual-rater（两个不同模型各判一遍，本次是同模型二判 conf~0.7）② 回灌 G1 修正表 ③ 与 r158 h 重判交叉分析。

## r177 观察记录（2026-11-02）

- **状态：盲评 agent 运行中，未落盘**
- 会话 01a195cb（taskSpace 904）：r176 派发已执行，agent 截至本轮检查 26 次思考 + 25 条命令，正在按 31 claim 特征 grep 全 21 份答卷并组装 0/1/2 评分（非 NA 19 项，max_score=38；O3 item 分 = 覆盖率阈值 ≥2/3→2 / ≥1/3→1 / 否则 0）
- 远端各分支暂无 `blind-eval/judge-{1,2}-scores.json`（arena 分支 tip 仍 fa59371）
- **Lead 决策：零派发**——agent 在跑时重复发消息会污染上下文；composer 显示 Stop generating = 仍在生成
- **下轮核验起点**：`git fetch origin && git ls-tree -r --name-only origin/arena/4a614e63-prompt-first-bench | grep -E "blind-eval/judge-[12]-scores"` → 落盘则 cherry-pick main + 独立核验（JSON 合法 / 21 run_id 全覆盖无重复 / 非 NA 条目有 evidence / O3 per-claim 数组长度=31）→ κ 计算（per-dimension + overall，0/1/2 原值先报）→ BRIDGE-REPORT 收口
