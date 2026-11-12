# PFB 仓库重构方案（2026-11-12 · 成璐指令）

> origin: ai（用户指令："github 的 pfb 很乱，分支多，合并后按设想构建；子模块同类归一文件夹；
> 解析混合真实世界梯度 vs 纯真实世界梯度 → 同一层级的两个子模块，放在"梯度下降"分类下，可互相消融"）

## 0. 现状盘点（本轮 git 实测）

- 分支 58 个：ralph/* 30+ 全部已并入 main（0 未合并提交）；arena/* 6 个中 5 个被 main 完全覆盖。
- **唯一活分支** `sigma-nlnk-snowball`：11-04 老快照分叉（双向差 1144/1660 提交），独有资产仅 4 张任务书，
  其中 3 张（T49/T51/T52）已经由其他路径合入 main，唯一缺失的 `T53-longterm-vision-survey.md` 已于
  commit b8798649 恢复。**→ sigma 分支可安全删除。**
- 根目录 36 个文件：~20 个 runs-*.log/pid/json 是历史运行残留（pid 均已死），无活跃进程引用根目录路径
  （活跃 gpu run pid 68960 的 cwd 在 experiments/stage-ablation/，输出写相对路径）。
- stage-ablation 内 4914 文件：runs-* 数据目录占大头（含 2865 文件的 .research-cache-backup），代码/脚本约百余个。
- tasks/ 顶层 85 个任务卡平铺，无分类。

## 1. 目标结构

```
pfb/
├── README.md / CLAUDE.md / loop-state.json / INDEX.md   # 根只留导航 + 状态
├── modules/                              # 每个 idea 方向一个子模块（同类归一处）
│   ├── A-eval-infra/                     # 评测基建
│   │   ├── bench/                        # ← bench/ (questions, rubric-v3, r3, self-opt-tester)
│   │   └── judge/                        # ← 判分协议、judge payload、blindtest 任务
│   ├── B-pipeline-ablation/              # 管线消融（S 系列臂）
│   │   ├── arms/                         # ← s8g/s9h/s10 等臂设计与结果
│   │   ├── state-machine/                # ← s5_state_machine.py 及实现
│   │   └── runs/                         # ← 所有 runs-* 数据目录
│   ├── C-objective-goodhart/             # 目标函数与 Goodhart
│   │   └── (T-PR-15, v17-hier-decomposition-blowup, text-objective-goodhart-survey)
│   ├── D-decomp-state-machine/           # decomp 状态机（T53 主线）
│   │   └── (sm-* 调研, T53-* 任务卡, drb 泛化 bench)
│   ├── E-sota-benchmark/                 # SOTA 对标
│   │   └── (gptr 基准, drb-leaderboard, sm-bench-sota-*)
│   └── F-theory/                         # 理论框架
│       ├── gradient-descent/             # ★ 平行消融层（成璐点名）
│       │   ├── realworld-gradient/       #   纯真实世界迭代（D35 线: T53-D35-*, T53C-*）
│       │   ├── analytic-hybrid/          #   解析先验 + 混合梯度（longterm-vision-survey 线）
│       │   └── ablation.md               #   两臂对照实验协议（待设计）
│       └── compression/                  # 压缩/信息论 (information-theory/, theory-*)
├── sop/                                  # 保持原位（流程规范，不动）
├── loop/                                 # 保持原位（阶段定义，不动）
├── scripts/                              # 保持原位
└── archive/                              # 历史残留
    ├── root-runs/                        # ← 根目录 runs-*.log/pid/console.log（死进程产物）
    ├── legacy-docs/                      # ← BRIDGE-REPORT / CONTINUE_MSG / loop-events 等一次性文档
    └── research-cache-backup/            # ← .research-cache-backup-20261112-072330
```

### 关键决策记录

| 决策 | 理由 |
|---|---|
| gradient-descent 下两个子模块同级 | 成璐原话：两者同层级、可消融；ablation.md 放父目录做对照协议 |
| 根目录 runs-* 进 archive 而非删 | 保留可追溯性；r14_analysis.py 等分析脚本引用旧路径，archive 后需同步改 3 处引用 |
| active run 产物（stage-ablation 内）不动 | pid 68960 正在写该目录，git mv 会破坏其相对路径假设 |
| T53 活跃任务卡暂留 tasks/ | restructure 完成前不碰在途工作流；收尾时再按模块归档 |
| 模块命名 A-F 字母序 | 与 projects/D1-* 编号体系不冲突（pfb 是独立 repo，内部自治） |

## 2. 执行批次（每批一个 commit，失败可单独 revert）

1. **B0 分支清理**：删远程 57 个僵尸分支（保留 main + f65a5a27 活跃 arena 分支）。
2. **B1 根目录清场**：runs-*.log/pid/json/console.log → archive/root-runs/；一次性 md → archive/legacy-docs/；
   更新 3 处代码引用（r14_analysis.py, drb_judge.py, gptr_smoke.py 的路径常量）。
3. **B2 一级目录归位**：bench/ → modules/A-eval-infra/bench/；**litsurvey 按领域分进各子模块**（成璐 2026-11-12 指令："结果直接放在对应子模块的 litsurvey，根目录只当索引，描述被做过百分比和剩余内容"）：
   - lit-survey/ + research/ 中评测基准类调研 → modules/A-eval-infra/litsurvey/
   - sm-* 调研、decomp 状态机相关 → modules/D-decomp-state-machine/litsurvey/
   - SOTA 对标类（sm-bench-closed-sota-v3, drb-leaderboard-*）→ modules/E-sota-benchmark/litsurvey/
   - prompt 优化理论（text-objective-goodhart-survey 等）→ modules/F-theory/gradient-descent/litsurvey/
   - knowledge-base/ → modules/F-theory/compression/ 或 archive
   - outputs/ notes/ receipts/ checkpoints/ demo/ src/ → 对应模块或 archive
4. **B3 stage-ablation 拆分**：runs-* 数据目录 → modules/B-pipeline-ablation/runs/；
   代码/脚本按 arm 归类；sm-* 调研 → modules/D-decomp-state-machine/。
   ⚠️ 前置条件：gpu run (pid 68960) DONE。
5. **B4 tasks/ 归档**：已完成任务卡按模块移入 modules/*/tasks/；在途的（T53-*, current-goal, goal-queue）留根 tasks/。
6. **B5 索引**：各模块写 INDEX.md（纯索引，列下一层条目）；根 INDEX.md 指向 6 模块 + archive。

## 3. 风险与回滚

- 每批独立 commit → `git revert <batch>` 单批回滚。
- B3 前必须确认 gpu run 结束（`tail sm-gpu-d32.log` 出现 DONE 行）。
- 引用修复验证：每批后 `grep -rn "旧路径"` 确认零残留引用。
- 外部依赖：arena 分支 f65a5a27 上的任务书引用了 tasks/ 路径，B4 前需同步 push 一次 arena 分支。

## 4. 验收

- [ ] 根目录文件数 ≤ 8（README/CLAUDE/loop-state/INDEX/APPROVALS + 必要状态文件）
- [ ] 6 个模块各有 INDEX.md
- [ ] gradient-descent/ 下 realworld-gradient + analytic-hybrid + ablation.md 三件齐
- [ ] 分支数 = 2（main + 1 活跃 arena）
- [ ] 全仓 grep 旧路径零残留（排除 archive/ 内部）
- [ ] gpu run 结束后 B3 完成且新 run 能正常落盘到 modules/B-pipeline-ablation/runs/