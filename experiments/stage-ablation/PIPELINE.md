# stage-ablation 实验管线（模块与组合方式）

# origin: ai — 2026-11-21 D 指令"把 pipeline 分清楚，模块和结构化做好，方便一键组合消融实验"

## 一句话

**实验形状（跑什么）声明在 spec/，实验机制（怎么跑）在脚本里，两者正交。**
新实验 = 写一个 spec JSON + 复用现有脚本，不改脚本代码。

## 模块边界

```
experiments/stage-ablation/
├── spec/                    # 声明层：实验形状（每个实验一个 JSON）
│   └── t53b.json            #   qids/arms/rounds/seed/judge/输出路径
├── s5_state_machine.py      # 被测对象：S5 状态机（SM）
│                            #   臂参数 sm_obj_mode=formula|text 由 driver 注入
├── ablation_driver.sh       # 机制层①：单 run 执行器（读 spec，跑一个 qid×arm×round）
├── t53b-batch.sh            # 机制层②：批量调度（读 spec 枚举 run 名，断点续跑）
├── ablation_stats.py        # 机制层③：统计（读 spec 的 qids/arms + run 文件，出 t-test）
├── pipeline_snapshot.py     # 机制层④：快照/delta（cron 10min，幂等，跨会话）
├── ablation-runs/           # 数据层：run 文件 + judge 文件（原始数据，不可删）
├── ablation-notes/          # 数据层：judge 原始输出
└── ablation-results.json    # 数据层：统计结果
```

**依赖方向**（单向，无环）：
`spec/ → batch → driver → SM → run 文件 → stats/snapshot → results`

- spec 是唯一改实验形状的地方；脚本不硬编码 qid/臂/轮数/seed。
- run 文件是数据层，脚本只读不写（driver 写新 run，stats 只读）。
- judge 模块由 spec 指定（`judge_module` + `judge_func`），换 judge 不改 driver。

## 一键组合新实验（SOP）

1. **写 spec**：`spec/<exp-name>.json`，字段见 t53b.json。
   - 换题：改 `qids` + `run_name_pattern`。
   - 换臂：改 `arms`（每臂一个 SM 参数 dict，driver 注入为 env）。
   - 换轮数：改 `rounds`。
   - 换 judge：改 `judge_module`/`judge_func`（须有 `score_run(run_file)→dict` 接口）。
2. **跑**：`bash t53b-batch.sh <spec-name>`（断点续跑：已完成的 run 自动跳过）。
3. **统计**：`python3 ablation_stats.py --spec <spec-name>`。
4. **快照**：cron 3eae1ea698b3 已覆盖（读 spec 枚举，幂等）。

## 字段契约（run 文件）

| 字段 | 来源 | 用途 |
|---|---|---|
| `qid` / `arm` / `round` | driver 写 | 分组键 |
| `coverage` | SM 直接算 | 主指标之一 |
| `depth_score` | SM 写（= judge overall） | 主指标之二 |
| `*_judge.json` 的 `overall` | judge 模块写 | depth 的原始出处 |
| `nodes` | SM 写 | 深结构分析 |

**判分校准**（判分校准规则）：跨 run 比分数前先对齐 judge 档位；同族判官分数仅相对有效。

## 当前实验

| spec | 状态 | 结论 |
|---|---|---|
| t53b | 收口（11-21, 62/62） | nat depth p=0.008 / soc cov p=0.006，formula 优 |

下一批（I2 general fix）：spec 名待定，复用同一套脚本。
