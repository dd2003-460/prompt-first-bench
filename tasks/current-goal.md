# Goal: T8-matrix-run-r1 — 矩阵实验第三点（T-select × V-full × 新域首跑）

> 创建：2026-10-30 · ralph loop runner（goal-queue 队首）
> 任务书：`tasks/T8-matrix-run-r1.md`（已 push，断点 B 过）
> 注：`sop/goal-template.md` 在仓库内不存在（grep 全仓仅被引用），本文件按 runner 协议 §A2 五字段格式落盘。

## 【目标】
为 T8 prompt 消融矩阵补第三个 M8 数据点：选一个**新域**（不复用机械键盘/会议室系统/GPU 硬件选型），走完整 01→04.5（V-full，当前全量 pfb prompt 不删改），产出六阶段工件 + M8 统一口径计分表，使三点（T6 r1 0.93 / T7.1 1.00 / 本 run）可定趋势。

## 【阶段】
T8 Part C 定向 paired runs 的基线点。M8 口径已定（`experiments/T8-audit/intermediate-rounds-audit.md` §口径定义 + `experiments/T8-matrix/design.md`）。前两点已落 design.md 表格。

## 【SOP 索引】
- `sop/arena-loop-pipeline.md`（唯一 SOP 入口；§4 loop 六阶段速览）
- `loop/prompt-first/00-common-review.md` + `01..04.5`（阶段定义，逐段读）
- `tasks/T8-matrix-run-r1.md`（任务书：三盲点修订①冻结②来源③owner + 验收标准）
- `experiments/T8-matrix/design.md`（run 目录结构约定 + M8 口径）
- 参照件：`loop-artifacts/stages/T7.1-*`（上一域命名与 X 清单格式范本）

## 【验收标准】
1. 六阶段工件齐全于 `loop-artifacts/stages/<N>/`，文件名带域后缀 `<domain>-*.md`（N1 规范）
2. 01：候选类别枚举 + **候选集冻结声明**（修订①）
3. 02：每条关键主张附来源 URL/路径+时间戳；无法核验显式标"存在性断言-未核验"（修订②）；ralph web-llm 不可用 → 记录失败原因后继续公开检索
4. 02.5：矛盾逐条登记处置（X 清单格式，参照 T7.1-02.5-crosscheck.md）+ 对抗核验停止理由
5. 03：每步标 owner=user/agent（修订③）
6. 04：可离线步骤真实执行并留命令/输出证据；需用户交互的步骤留默认假设并标注
7. 04.5：反方复核 verdict + repair_stage 落 `stages/04.5/`
8. M8 计分表落 `experiments/T8-matrix/runs/tselect-vfull-<domain>/m8-scorecard.md`，design.md 表格第 3 行回填
9. commit + push + ls-remote 验证落点

## 【失败降级】
- ralph web-llm 三 provider 均不可用（登录态失效）→ 按 02 规则记录失败回执后继续公开检索（WebSearch/WebFetch/curl），conf 相应降档，不阻塞
- 某候选价格/规格查不到 → 标"无现货数据"+区间估计+保守假设
- 需用户交互步骤 → 默认假设+显式标注，不伪造用户确认
- arena 通道不可用 → 本 run 即 Lead 本地自答（conf-0.2 标注，同 T7.1 先例）