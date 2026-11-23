# origin: ai · 2026-11-23 21:40 · D2 gold 骨架 arena 任务卡（待 D 确认 Q9 题面 v1 后派发）

> 状态: 草稿就绪，派发前置 = D 确认 q9-agi-question-v0.md 的 3 项（预算 150 / 5 因子清单 / 排序键 post_acc）。
> 派发通道: arena agent mode（ego-browser），SOP 见 .claude/skills/arena-outsource/SKILL.md。
> 拆法: 按 SOP 3a，拆 2 个 subagent（主调研 + 交叉验证），并行。

## 任务卡 A（主调研）

```
[任务] 为"research-AGI 预算控制"题面建 gold 骨架：完整覆盖 5 项贡献因子
（模型能力轴/预算轴/检索质量轴/记忆轴/自我认识闭环）的分解树，
回答"在 150 节点预算内，性价比最高、最快且可靠地让 AI 获得自我认识能力
（gap 标记→补全→post_acc 闭环）的路径分解是什么"。

[背景]
- 题面（冻结版）: pfb/experiments/stage-ablation/tasks/q9-agi-question-v0.md
  的"题面 v1 草稿"段（D 确认后冻结，以届时版本为准）
- 硬件: 4× V100-SXM2-16GB (cc 7.0, TP=4), Qwen3-27B NVFP4 vLLM,
  不改权重只用 prompt+外部工具, 预算 150 研究节点（定值）
- 排序键: 单位预算闭环成功率 = gap 标记→补全→补全后 verified/degraded 占比 (post_acc)
- 参考格式: pfb/bench/rubric-v3/ablation/gold-tree.md（frozen ed552c4, 38 判定点格式）
- 三条硬规则（题面歧义审计结论, gold 必须遵守）:
  ① 每个参数定值或显式声明"模型自选且 gold 按模型选的值重算"
  ② 每个因子必须在题面可见（骨架结构/数值不泄露给被测模型）
  ③ 定稿后冻结, 改动需 D 确认

[约束] 中文; 每条结论标 conf(0-1); 给来源 URL; 不确定标"未验证";
  调研顺序: GitHub 开源实现 → arXiv/见刊 → 交叉验证 → 自己推

[交付] markdown 分解树: 根节点(排序键) → 5 因子分支 → 每因子 3-6 子节点,
  每节点一行: [因子] claim | 测量口径 | 来源 URL | conf
  另附: 因子间依赖/交互 1 张表（哪些因子互相耦合, 如预算轴×检索质量轴）

[长度] ≤50 行核心 + 附录
[落盘约束] 文件不存在=任务未完成
```

## 任务卡 B（交叉验证）

```
[任务] 独立回答任务卡 A 的同一问题（5 因子分解树），用于交叉验证门禁。
  不读任务卡 A 的交付物，独立调研后给同格式输出。
[背景] 同任务卡 A（题面/硬件/排序键/三条硬规则）
[约束] 同任务卡 A
[交付] 同任务卡 A 格式
[长度] ≤50 行
[落盘约束] 文件不存在=任务未完成
```

## 派发后

- 两卡交付 → Lead 对比矛盾点 → 交叉验证回执（≥2 successful_provider_ids）
- gold 骨架落 pfb/bench/rubric-v3/ablation/gold-Q9.md（格式同 gold-Q6.md）
- rubric 判定点 × 层级（D3）随 gold 一起出
- metacog_axis 在 Q9 上跑通（替换 TCO 题的测量对象）= ⑤ 子项完成判据
