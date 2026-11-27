#!/usr/bin/env python3
"""Q9 相关性门禁臂: monkeypatch P1H_INDEX + P15B_GAP_FILL 加节点相关性约束, 不改本体.
注入点修正 (2026-11-27 Lead 核主循环): P1_DECOMPOSE 是死路径, SM 主循环不调用;
真实生成路径 = ① 逐层展开 _decompose_layer → P1H_INDEX (函数内 from s5_pipeline import,
运行时读模块属性, patch s5_pipeline.P1H_INDEX 生效) ② gap 补全 gap_check → P15B_GAP_FILL
(s5_pipeline 顶部 from-import, patch s5_pipeline.P15B_GAP_FILL 生效).
入口: __main__ 内联块 (无 main()), 故 patch 后用 runpy 执行原文件.
"""
import sys, os, runpy
# 布局迁移 7283ae153 (2026-11-27 18:03) 把 s5_pipeline/prompts/judge_v2_depth 搬进 D,
# s8b_pilot 搬进 A; s5_state_machine.py 原地裸 import 无 sys.path 处理 → 须把三目录都入 path.
_D = '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/D-decomp-state-machine/scripts'
_A = '/Users/a1-6/Desktop/workspace/pfb-thinkmech/modules/A-eval-infra/scripts'
_E = '/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation'
for _p in (_D, _A, _E):
    sys.path.insert(0, _p)
import prompts

GATE = (
    "\n\n【节点相关性门禁（硬性约束）】每个子节点必须直接服务于本题的部署目标："
    "Qwen3.8-27B 在 4×V100-SXM2-32GB (TP=4, NVFP4/W4A16) 上的推理性能与显存。"
    "只允许以下三类节点：① 硬件参数及其对推理的影响（显存/带宽/L2/量化位宽/指令集）；"
    "② 推理计算或访存的逐步分解（KV cache/attention/TP 切分/decode 流水线）；"
    "③ 量化指标（tok/s/延迟/显存占用/吞吐的数值估计）。"
    "禁止与本题部署无关的子问题（其他硬件平台的性能、通用软件框架内部机制、"
    "任务队列/调度系统、与本部署无关的成本或工具链话题）。"
    "违反门禁的节点视为无效，宁可不生成。"
)

import s5_pipeline
s5_pipeline.P1H_INDEX = s5_pipeline.P1H_INDEX + GATE
s5_pipeline.P15B_GAP_FILL = s5_pipeline.P15B_GAP_FILL + GATE
assert "相关性门禁" in s5_pipeline.P1H_INDEX and "相关性门禁" in s5_pipeline.P15B_GAP_FILL, "GATE INJECT FAILED"

os.chdir('/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation')
sys.argv = ['s5_state_machine.py'] + sys.argv[1:]  # 透传 --question-file/--qid/--max-nodes/--max-depth
runpy.run_path('/Users/a1-6/Desktop/workspace/pfb-thinkmech/experiments/stage-ablation/s5_state_machine.py', run_name='__main__')
