# 编号纪律 v2（decomp + 任务表）

> origin: ai · 2026-11-26 · D 指令「能不能完善编号和分类啊」
> 输入：`modules/D-decomp-state-machine/research/pfb-complete-history-20261126.md`（§0 五时代 / §5 四命名空间 / §6 五前缀速查）

## 分解树

1. **现状盘点** — 已由 lineage 报告完成（4 套 T 命名空间 + 5 前缀 + r 三命名空间）。无缺口。
2. **纪律设计（Lead 已定）** — 原则：历史零改名，只加映射 + 向前看规则。
   - T：全局递增不复用（主序列 T54 后 → T55+）；goal 内部子任务 = goal 前缀+序号（TT1-TT8 / CC1-CC6）；跨 goal 引用必须带前缀
   - r：三命名空间写明（runs/rep rN / 工程迭代 rN / 历史全局轮号 legacy 不再新增）
   - v/S/A：沿用 11-19 规则；E：冻结
   - 缺口 [待核验]：工程迭代 rN 与 runs/rep rN 撞形，是否引入 eng-N——sub 只 grep 确认引用范围，不改
3. **落盘实施（sub）** — 编辑 `exploration-history.md`：§0 加五时代总览表 + T 四命名空间表；§5 扩为全前缀纪律 v2；header 加 knowledgebase 镜像漂移警示
4. **验收** — 新节存在（grep）+ commit hash + 零文件改名（git status 无 rename）

## 任务表

| # | 任务 | 执行 | 验收 |
|---|------|------|------|
| N1 | exploration-history.md 三处编辑 + commit | sub | commit hash + 新节 grep 命中 + 无 rename |
