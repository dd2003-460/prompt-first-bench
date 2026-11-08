# Goal: PFB Full-Run Production (2026-11-08)

**状态**: ACTIVE
**来源**: 成璐指令 "pfb本来就应该完整跑" + "现在可以跑并发了，并发就2-3"

## 目标

在 8787 (qwen3.8-27b) 上完成 pfb 全臂 × 全题 × 足够样本的量产数据，产出可发表级别的消融实验结果。

## 待跑矩阵

| 臂 | 题 | reps | 状态 | 备注 |
|---|---|---|---|---|
| S0 | nat | 500 | 🔄 r295/500 (PID 8166) | temp=0.7+top_p=0.95, 主进程 |
| S0 | soc | 500 | ⏳ 排队 | 主进程内排队 |
| A3 | nat | 500 | ⏳ 排队 | 主进程内排队 |
| A3 | soc | 500 | ⏳ 排队 | 主进程内排队 |
| A4 | nat | 500 | ⏳ 排队 | 主进程内排队 |
| A4 | soc | 500 | ⏳ 排队 | 主进程内排队 |
| S3 | nat | 30 | ⏳ 待启动 | 需 temp=0.7 重跑 (旧数据是 temp=0) |
| S3 | soc | 30 | ⏳ 待启动 | 同上 |
| S5 | gpu | 3 | 🔄 r1 进行中 (PID 49146) | 32 点 rubric, 5 通道研究 |
| S5 | nat | 100 | ⏳ 待启动 | 核心对比臂 |
| S5 | soc | 100 | ⏳ 待启动 | 核心对比臂 |

## 并发策略 (成璐 2026-11-08: "并发就2-3")

- **Slot 1**: 主进程 prod_run.py (S0/A3/A4 × nat/soc × 500) — 已在跑
- **Slot 2**: s5_pipeline.py S5 GPU (3 reps) — 已在跑
- **Slot 3**: s5_pipeline.py S5 nat/soc (100 reps each) — 待 S5 GPU 完成后启动
- **约束**: 8787 proxy 单模型，并发 2-3 安全；超过 3 可能 OOM 或超时

## 断点恢复协议

s5_pipeline.py 已有 `--start-rep` + 文件存在性检查（`if os.path.exists(fp): continue`）。
如果中途某 rep 失败（error in JSON），下次启动时该 rep 会跳过（因为文件已存在）。
**修复方式**: 删除失败的 JSON 文件 → 重新启动 → 自动从缺失处继续。

prod_run.py 同理：按 tag 检查文件存在性，跳过已完成的。

## 验收标准

1. 所有矩阵格子有 ≥ 指定 reps 的有效 JSON（无 error 字段）
2. judge_v2_depth.py 对所有 run 打分完成
3. 跨臂对比报告生成（S0 vs S5 核心对比 + S3/S0 辅助对比）
4. 报告含：覆盖率、深度分、[待核验] 计数、条件性指标（underdetermined 题）
5. 数据提交到 prompt-first-bench.git

## 风险

- 8787 推理引擎不能动（NINFER 红线）
- 同族判官偏差（qwen3.8-27b 评 qwen3.8-27b）→ 只作相对比较
- S5 每 rep ~4-8 min（含研究），100 reps ≈ 7-14h/arm
- 主进程 S0-nat 剩余 ~205 reps × ~30s ≈ 1.7h，之后还有 soc+A3+A4

## 时间线估计

- T+0 (now): S0-nat r295, S5-gpu r1
- T+~2h: S0-nat 完成 → 主进程切 S0-soc
- T+~30min: S5-gpu 完成 → 启动 S5 nat/soc (slot 3)
- T+~15h: 主进程全部完成 (S0/A3/A4 × 2 × 500)
- T+~20h: S5 nat/soc 完成 (100 reps × 2 arms, slot 3 串行)
- T+~22h: 全部数据就绪 → 打分 → 报告