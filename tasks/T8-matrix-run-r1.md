【执行前必读】
1. 本任务必须走 1-loop：先读 sop/arena-loop-pipeline.md + loop/prompt-first/00-common-review.md + 01..04.5（仓库内）。
2. 每阶段产出落盘 loop-artifacts/stages/<N>/，文件名带域后缀（N1 命名规范：<domain>-<file>.md），阶段判定 pass 才进下一阶段。
3. 完成后 commit + push（含全部 loop-artifacts/）。
4. 通道故障（403/沙箱）→ 报告 Lead，由 Lead 降级本地执行，不得静默跳过 loop。

# T8 矩阵实验 run r1：T-select × V-full × 新域首跑

## 背景
T8 prompt 消融研究（tasks/T8-prompt-ablation.md）Part C 定向 paired runs 的基线点。M8 口径已定（experiments/T8-audit/intermediate-rounds-audit.md §口径定义）：现有两点 = T6 r1 键盘域 0.93 + T7.1 会议室域 1.00，三点才能定趋势。本 run = 第三点。

## 任务
选一个**新域**（不得复用机械键盘/会议室系统/GPU 硬件选型），走完整 01→04.5，V-full（当前全量 pfb prompt，不做任何删改）：
1. 01：候选类别枚举 + 候选集冻结声明（修订①）
2. 02：每条关键主张附来源 URL/路径+时间戳，无法核验的显式标"存在性断言-未核验"（修订②）；ralph web-llm 不可用则记录失败原因后继续公开检索（既有规则）
3. 02.5：矛盾逐条登记处置（X 清单格式，参照 T7.1-02.5-crosscheck.md）
4. 03：每步标 owner=user/agent（修订③）
5. 04：真实执行可离线步骤，需用户交互的留默认假设并标注
6. 04.5：反方复核，verdict + repair_stage 落 loop-artifacts/stages/04.5/

## 验收标准（Lead 侧）
- 六阶段工件齐全于 loop-artifacts/stages/（域后缀命名）
- M8 按统一口径计分表落 experiments/T8-matrix/runs/tselect-vfull-<domain>/m8-scorecard.md
- verdict 记录在案；三盲点修订生效证据逐条核对

## 失败降级
arena 不可用 → 报告 Lead，Lead 本地 naive subagent 跑同任务卡，conf 降级标注。
