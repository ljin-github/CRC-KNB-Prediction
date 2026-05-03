# 在Windows系统下，请为我写一个满足下列任务或要求的脚本：
# 提取表a中第一个_左侧的所有内容（提取的内容可参考下方表a处的内容，如C:\Users\Administrator\Desktop\test\data\topatches\negative\2001004-4\2001004-4）,若内容相同，则视为一组；
# 从提取的内容中再提取最后一个“\”右侧的内容，并与表b第一列中“.”左侧的内容进行匹配，参考表b中的内容先后顺序，将从表a中提取的各组进行排序；
# 能在PyCharm 2024.1中正常运行；
# 若有n个参数需要手动设置，则每个参数设置占一行。

# 表a:train.txt:
# C:\Users\Administrator\Desktop\test\data\topatches\negative\2001004-4\2001004-4_158208_78336_108544_75776_109056_76288.jpg	0
# C:\Users\Administrator\Desktop\test\data\topatches\negative\2210569-6\2210569-6_101376_76288_28672_53248_29184_53760.jpg	0
# C:\Users\Administrator\Desktop\test\data\topatches\pasitive\2111385-6\2111385-6_117760_94720_28672_39936_29184_40448.jpg	1
# 表b:train-RND-0.txt:
# 2025335-7.png   1
# 2030134-5.png   1
# 2109810-6.png   0
# 2116442-5.png   0

# 该脚本耗时近2d（10.17-10.18），经验总结：
# 当某一脚本ai生成后无法成功运行/生成的数据不是想要的数据，可先新建对话框再提问并生成脚本；
# 若还是不行，可将复杂的数据处理过程拆分为n个简单步骤并生成对应脚本（在新建的同一对话框a中进行），最后再将n个提问进行汇总为一个复制提问并再生成复制脚本（对话框a中进行）；
# 必要时可给出表格前几列内容、数据结构。

import os
from collections import defaultdict

# 参数设置
input_file_path_a = r'C:\Users\Administrator\Desktop\test\data\split_info\train-0-patches.txt'  # 表a文件路径（patches的label文件），RND：随机化
input_file_path_b = r'C:\Users\Administrator\Desktop\test\data\split_info\train-RND-0.txt'  # 表b的输入文件路径（wsi的label文件）
output_file_path = r'C:\Users\Administrator\Desktop\test\data\split_info\train-RND-0-patches.txt'  # 输出文件路径


def extract_and_group(file_path):
    """
    从文件中读取路径，提取并分组
    :param file_path: 输入文件路径
    :return: 分组后的数据
    """
    groups = defaultdict(list)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            path, label = line.strip().split('\t')
            base_name = os.path.basename(os.path.dirname(path))
            key = base_name
            groups[key].append((path, label))

    return groups


def load_order_from_file_b(file_path):
    """
    从表b中加载排序顺序
    :param file_path: 表b的输入文件路径
    :return: 排序顺序列表
    """
    order = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                base_name = line.strip().split('.')[0]
                order.append(base_name)

    return order


def sort_groups_by_order(groups, order):
    """
    按照表b中的顺序对分组后的数据进行排序
    :param groups: 分组后的数据
    :param order: 排序顺序列表
    :return: 排序后的数据
    """
    sorted_groups = []

    for key in order:
        if key in groups:
            sorted_groups.extend(groups[key])

    return sorted_groups


def write_to_file(sorted_groups, output_path):
    """
    将结果写入到输出文件
    :param sorted_groups: 排序后的数据
    :param output_path: 输出文件路径
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        for path, label in sorted_groups:
            file.write(f"{path}\t{label}\n")


if __name__ == "__main__":
    # 提取并分组
    groups = extract_and_group(input_file_path_a)
    # 加载表b中的排序顺序
    order = load_order_from_file_b(input_file_path_b)
    # 按照表b中的顺序对分组后的数据进行排序
    sorted_groups = sort_groups_by_order(groups, order)
    # 写入文件
    write_to_file(sorted_groups, output_file_path)