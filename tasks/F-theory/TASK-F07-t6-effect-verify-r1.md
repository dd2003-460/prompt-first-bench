【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

# T6 效果验证 r1：换域重跑首测（三盲点修订后）

## 背景
workspace commit 312efcaa 对 loop/prompt-first/ 做了三处修订（已同步本仓库 8d376c4）：
- 01「候选集冻结」：01 产出的候选类别清单为冻结集合，后续增删须 02 核验后显式记录
- 02「证据来源完备」：每条关键主张必附 URL/路径+快照时间戳，缺一降级为存在性断言-未核验
- 03「owner 类型标注」：每步标 owner=user/agent，防交互步骤与离线步骤混排

## 任务
选一个**新域**（不得复用会议室选型/27B 硬件选型），走完整 01→04.5 首测，验证三修订是否生效：
1. 01 阶段：列出候选类别清单 → 记录为冻结集合
2. 02 阶段：每条关键主张附来源（URL/路径+时间戳），无来源的标"存在性断言-未核验"
3. 03 阶段：每步标 owner=user/agent
4. 04/04.5：按标准 Reviewer 质检

## 验收
- 01 工件有显式"候选集冻结"声明
- 02 工件每条主张可追溯来源或显式降级标注
- 03 工件每步有 owner 字段
- reviewer verdict 记录在 loop-artifacts/stages/04.5/

## 失败降级
arena 不可用 → 报告 Lead，Lead 用本地 naive subagent 跑同任务卡，conf 降级标注。
