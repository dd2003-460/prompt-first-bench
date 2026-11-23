#!/usr/bin/env python3
"""去脚手架 runner — 剥离 [待核验] 指示, 测自发监控 (补充45 后续实验)

设计: modules/B-pipeline-ablation/research/no-scaffold-experiment-design-20261123.md
用法:
  python3 no_scaffold_runner.py <qid> [--max-nodes N] [--max-depth N] [--out-tag TAG]
  # 例: python3 no_scaffold_runner.py gpu --max-nodes 150 --out-tag smoke

机制: 运行时 monkeypatch prompts.P1H_INDEX / P1_DECOMPOSE (剥离 [待核验] 指示句),
prompts.py 文件 byte-unchanged。patch s5_pipeline 模块对象 (from-import 绑定),
再 runpy 执行 s5_state_machine 入口 (import 缓存保证拿到已 patch 的模块)。
输出: runs-s5-sm-<qid>.json (stage-ablation 目录, 与常规 run 同路径) —
跑完后由调用方 cp 到 data/no-scaffold/ 存档 (不自动, 防覆盖)。
"""
import sys, os, runpy

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import prompts  # noqa: E402
import s5_pipeline  # noqa: E402


def strip_scaffold(p: str) -> str:
    """剥离 [待核验] 指示 (5 处), 保留 source/search_query 规则。"""
    p = p.replace(
        "若某事实确实只有定性结论，claim 末尾标 [待核验] 并给出最接近的量化形式（变量/参数化公式）。\n",
        "",
    )
    p = p.replace(
        "确实只有定性结论的标 [待核验] 并给出最接近的量化形式",
        "确实只有定性结论的给出最接近的量化形式",
    )
    p = p.replace(" [待核验] (L3)", " (L3)")
    p = p.replace("（[待核验]、[时效待核]、符号变量未实例化）", "（[时效待核]、符号变量未实例化）")
    return p


def main():
    out_tag = "no-scaffold"
    for k, v in enumerate(sys.argv[1:]):
        if v == "--out-tag" and k + 1 < len(sys.argv) - 1:
            out_tag = sys.argv[k + 2]

    # patch 两个模块对象的属性 (from-import 绑定在 s5_pipeline 命名空间)
    for mod in (prompts, s5_pipeline):
        for name in ("P1H_INDEX", "P1_DECOMPOSE"):
            orig = getattr(mod, name, None)
            if orig is None or "[待核验]" not in orig:
                continue
            stripped = strip_scaffold(orig)
            assert "[待核验]" not in stripped, f"{mod.__name__}.{name} 剥离不干净"
            for kw in ("source", "search_query", "given", "knowledge"):
                assert kw in stripped, f"{mod.__name__}.{name} 剥离误删 {kw}"
            setattr(mod, name, stripped)
            print(f"[no-scaffold] {mod.__name__}.{name}: 剥离 [待核验] ({len(orig)}→{len(stripped)} chars)", flush=True)

    # 验证 s5_state_machine 的局部 import 会拿到 patched 值
    # (line 503: from s5_pipeline import P1H_INDEX — 函数内 import, 调用时读模块属性)
    assert "[待核验]" not in s5_pipeline.P1H_INDEX
    assert "[待核验]" not in s5_pipeline.P1_DECOMPOSE

    # 输出隔离 (2026-11-23 15:53 事故修复):
    # ① checkpoint 目录重定向 (SM_CKPT_DIR), 不覆盖 checkpoints/sm-{qid}-r1 原始数据
    # ② 备份现有 run json (run 结束时 SM 固定写 runs-s5-sm-{qid}.json, 会覆盖)
    qid = "gpu"
    for a in sys.argv[1:]:
        if a in ("gpu", "nat", "soc"):
            qid = a
            break
    out_root = os.path.join(HERE, "data", "no-scaffold", out_tag)
    os.makedirs(out_root, exist_ok=True)
    os.environ["SM_CKPT_DIR"] = os.path.join(out_root, "checkpoints")
    run_json = os.path.join(HERE, f"runs-s5-sm-{qid}.json")
    if os.path.exists(run_json):
        import shutil
        shutil.copy2(run_json, os.path.join(out_root, f"runs-s5-sm-{qid}.pre-existing.bak.json"))
        print(f"[no-scaffold] 已备份原 run json → {out_root}/runs-s5-sm-{qid}.pre-existing.bak.json", flush=True)
    print(f"[no-scaffold] 输出隔离: ckpt={out_root}/checkpoints, tag={out_tag}, 开始 run", flush=True)

    # 执行 SM 入口 (run_name='__main__' 触发 if __name__ 块)
    runpy.run_path(os.path.join(HERE, "s5_state_machine.py"), run_name="__main__")

    # 跑完立刻 cp run json 到隔离目录 (rep-scan queue 的既有模式)
    if os.path.exists(run_json):
        import shutil, datetime
        ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        shutil.copy2(run_json, os.path.join(out_root, f"runs-s5-sm-{qid}.{out_tag}.{ts}.json"))
        print(f"[no-scaffold] run json 已存档 → {out_root}/runs-s5-sm-{qid}.{out_tag}.{ts}.json", flush=True)


if __name__ == "__main__":
    main()
