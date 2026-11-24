#!/usr/bin/env python3
# origin: ai · 2026-11-25 · idea53 references merge (等 D "投" 后执行)
# 用法: python3 merge_references.py --dry-run   (只报告, 不改文件)
#       python3 merge_references.py            (执行 merge, 幂等: 已 merge 则跳过)
# 输入: merge-anchors.json (锚点映射, 15 bib key 全覆盖) + references.bib
# 输出: paper.tex 插入 \citep + bibliography 节 + submission/references.bib 拷贝
import json, os, sys, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(HERE, "..", "submission")
ANCHORS = json.load(open(os.path.join(HERE, "merge-anchors.json"), encoding="utf-8"))

def main():
    dry = "--dry-run" in sys.argv
    tex_path = os.path.join(SUB, "paper.tex")
    tex = open(tex_path, encoding="utf-8").read()
    if "\\bibliography{references}" in tex:
        print("SKIP: paper.tex 已有 \\bibliography (已 merge 过)"); return
    # 1) 锚点替换 (逐条断言恰好 1 次)
    for a in ANCHORS["anchors"]:
        n = tex.count(a["old"])
        if n != 1:
            print(f"ABORT: 锚点出现 {n} 次 (期望 1): {a['family']} :: {a['old'][:60]}...")
            sys.exit(1)
        if not dry:
            tex = tex.replace(a["old"], a["new"])
        print(f"{'OK ' if not dry else 'dry'} [{a['family']}] keys={len(a['keys'])}")
    # 2) bibliography 节
    if ANCHORS["bib_insert_before"] not in tex:
        print("ABORT: \\end{document} 未找到"); sys.exit(1)
    if not dry:
        tex = tex.replace(ANCHORS["bib_insert_before"],
                          ANCHORS["bib_block"] + ANCHORS["bib_insert_before"])
    if not dry:
        open(tex_path, "w", encoding="utf-8").write(tex)
        shutil.copy(os.path.join(HERE, "references.bib"), os.path.join(SUB, "references.bib"))
        print("WROTE paper.tex (+\\citep×4 组 + bibliography) + submission/references.bib")
    else:
        print("DRY-RUN: 全部锚点匹配, 未改文件")

if __name__ == "__main__":
    main()
