# 实验运行规范

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：pfb 实验的结论靠统计显著性支撑，而统计显著性依赖 run 数量和质量。跑崩一个 run、落盘格式不一致、或者 rep 数不够，都会让整批数据不可用。这份文件定义"怎么跑不翻车"。

## 实验矩阵

标准矩阵：**arm × question × rep**

| 维度 | 当前值 | 说明 |
|------|--------|------|
| Arms | S0, S1, S5（主）+ S10-A~E（tone 实验）+ D1-C1（baseline） | 新臂需过 prompt-design.md 检查清单 |
| Questions | Q1-Q5（AI/ML 域）+ Q6/Q7（跨域 limitation）+ Q8-Q10（B1 新题 [待建]） | 适用域声明：AI/ML |
| Reps | 6 per arm×question（n=30/arm for 5 questions） | n=30 是 bootstrap CI 的最小可靠样本量 |

**为什么 6 reps**：5 questions × 6 reps = 30 runs/arm。bootstrap 95% CI 在 n=30 时开始稳定；n<20 时 CI 宽度太大，Δ 不显著可能是样本量问题而不是效应不存在。

## 落盘格式

每个 run 一个 JSON 文件：`runs/<arm>-<qid>-r<rep>.json`

```json
{
  "arm": "S5",
  "qid": "Q1",
  "rep": 1,
  "model": "qwen3.8-27b",
  "timestamp": "2026-11-07T10:30:00+08:00",
  "rounds": 3,
  "rejections": 1,
  "soothed": false,
  "sources": ["https://arxiv.org/abs/..."],
  "final": "完整输出文本",
  "output_text": "同 final（兼容 score.py 旧格式）"
}
```

**字段说明**：
- `final`：模型最终输出（S10 系列用这个字段）
- `output_text`：同上，保留是为了兼容 score.py 的 `score_run()` 函数
- `sources`：模型实际引用的 URL 列表（S10 中为空 []，因为机械反馈下模型不引用）
- `rounds`：模型经历了多少轮 self-review
- `rejections`：被 reviewer 拒绝的次数
- `soothed`：是否触发了 soothe 路径（S10-D/E 专用）

**为什么两个字段都留**：score.py 读 `output_text`，score_s10.py 读 `final`。统一成一个字段需要改两个脚本，不如双写。等 v4 重构时再合并。

## Resume 机制

长时间跑（90 runs ≈ 30 min）中途可能断。所有 scorer 支持 `--resume`：
- 读已有 scores.json，跳过已打分的 run
- 从断点继续，不重复计算
- 日志追加到 `<name>-scoring.log`

```bash
python3 score_s10.py --resume > s10-scoring.log 2>&1 &
```

## Error Handling

- **单 run 失败**（timeout / API error）：记录 error 字段，继续下一个。最后汇总时报告 N/M 成功。
- **全部失败**（API down）：停。不要带着空数据出结论。
- **分数异常**（total > 1.0 或 < 0.0）：大概率是 judge 解析 bug，检查 raw response 再重跑该 run。
- **M5/M6 = 0 但输出有内容**：正常——模型没引用 URL 时 M6 就是 0，不是 bug。

## 并发控制

- ThreadPoolExecutor max_workers = 4（本地 vLLM 瓶颈在 GPU 显存，4 并发是甜点）
- 不要超过 6——vLLM 会 OOM
- arena 外包的 run 不受此限制（远端执行）

## 版本管理

- 每次修改 prompt / research_hook / scoring 逻辑 → git commit + tag
- run 文件名不含版本号（版本信息在 commit 里）
- 跨版本比较时标注 commit hash（如 "S5 @d20d4b0 vs S0 @d20d4b0"）
- **不同版本的 run 不能混在同一批评分里**——prompt 结构变了，分数不可比

## 当前状态快照（2026-11-07）

| 实验 | 状态 | Run 数 | 备注 |
|------|------|--------|------|
| S0/S1/S5 n=30 | ✅ 完成 | 150 (5 arms × 5 Q × 6 reps) | @d20d4b0 |
| S10 tone (A-E) | ✅ 完成 | 90 (5 arms × 3 Q × 6 reps) | @d20d4b0 |
| D1-C1 baseline | ✅ 完成 | 5 (1 arm × 5 Q × 1 rep) | self-judge only |
| D-face (Q6/Q7) | ✅ 完成 | 4 (v1-v3) | model ceiling confirmed |
| B1 new questions | 🔄 任务卡写好 | 0 | gold tree 未建 |