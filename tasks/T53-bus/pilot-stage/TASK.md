# origin: ai (2026-11-28 状态机接入 CC 试点任务卡)
# 类型: 试点 — CC 首次通过状态机(stage 模式)跑具体任务

## 任务
为 sm-run6 写预注册草案。sm-run5 已收口(Δ=+0.67 不显著, G4 open), 复跑方向二选一:
(a) 更强假设层植入(让缺陷更难自驳, 拉开两臂差距)
(b) n≥5/臂(加样本量, 提高检验力)
你要做的是: 基于 sm-run5 的证据, 设计 sm-run6 预注册草案(不是直接跑实验)。

## 输入(只读)
- modules/G-think-mechanism/rsi-pilot/sm-run5-ab-preregistration.md (sm-run5 设计, 判据/臂/植入缺陷)
- modules/G-think-mechanism/rsi-pilot/sm-run5-scoring.md (sm-run5 结果: run-7/9/11=A, run-8/10/12=B, Δ=+0.67)
- modules/G-think-mechanism/rsi-pilot/sm-run5-ref-status.md (参考快照)

## 产出
- 写入 tasks/T53-bus/pilot-stage/sm-run6-preregistration-draft.md, 必含:
  1. 方向选择 (a 或 b 或混合) + 选择理由(引 sm-run5 具体数字)
  2. 植入缺陷设计(若选 a): 每条缺陷 + 为什么比 sm-run5 更难自驳
  3. 样本量与判决阈值(若选 b 或混合): n/臂, 预注册判决标准(成立/不显著/负结果), 方差估计怎么来
  4. 臂定义(A/B 任务卡差异) + 判分方法(binary, 谁判分, 盲判否)
  5. 风险与边界声明(和 sm-run5 一样的诚实标注要求)

## 边界(硬)
- 只写上面指定的产出文件; 不跑实验、不调 8787、不碰 sm-run5 已收口的任何文件
- git: 只 add 你自己写的产出文件; cc-state.json / cc-to-lead.md 是 Lead 管理的, 永不 add
- 卡住/需要 Lead 判断 → 写 tasks/T53-bus/pilot-stage/cc-to-lead.md 说明哪项过不了+原因, 然后停止

## 状态机
你在 stage 模式下运行: 每个 Stop 时 hook 会注入当前阶段的 reminder+gate。
执行 reminder → 逐项自检 gate → 全过 → 更新 cc-state.json 的 current_index += 1 并在 history 追加 {stage, evidence}(evidence 必须是可验证 handle: 文件路径/commit/数字) → 继续下一阶段。
reminder 里指向 md 文档的就 read_file 读全文, 不要凭指针猜。
