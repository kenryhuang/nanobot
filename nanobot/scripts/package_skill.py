#!/usr/bin/env python3
"""
简单的 skill 打包脚本
将 skill 目录打包成 .skill 文件（zip 格式）
"""

import sys
import os
import zipfile
from pathlib import Path

def package_skill(skill_path: str, output_dir: str = None):
    skill_path = Path(skill_path)
    
    if not skill_path.exists():
        print(f"错误：目录不存在 - {skill_path}")
        sys.exit(1)
    
    # 验证 SKILL.md 存在
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"错误：缺少 SKILL.md 文件")
        sys.exit(1)
    
    # 确定输出路径
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = skill_path.parent
    
    output_file = output_dir / f"{skill_path.name}.skill"
    
    # 创建 zip 文件
    print(f"打包 {skill_path.name}...")
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(skill_path):
            for file in files:
                file_path = Path(root) / file
                arcname = file_path.relative_to(skill_path.parent)
                zipf.write(file_path, arcname)
                print(f"  添加：{arcname}")
    
    print(f"\n完成！打包文件：{output_file}")
    print(f"大小：{output_file.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python package_skill.py <skill 目录路径> [输出目录]")
        sys.exit(1)
    
    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    package_skill(skill_path, output_dir)
