from number_patterns import STANDARD_1, STANDARD_7, VARIANTS_1, VARIANTS_7

def validate_canvas(canvas):
    """验证输入画布的格式是否正确"""
    if not canvas or not canvas[0]:
        raise ValueError("画布不能为空")
    
    if len(canvas) != 5:
        raise ValueError("画布必须是5行")
    
    for row in canvas:
        if len(row) != 3:
            raise ValueError("画布每行必须是3列")
        
        for val in row:
            if val not in [0, 1]:
                raise ValueError("画布只能包含0或1")

def count_matches(canvas, pattern):
    """计算画布与模式的匹配程度，同时考虑1和0的匹配"""
    matches = 0
    total = 25  # 5x5的画布总点数
    
    for i in range(5):
        for j in range(3):
            # 同为1或同为0都算匹配
            if canvas[i][j] == pattern[i][j]:
                matches += 1
    
    return matches / total

def is_similar_to_pattern(canvas, pattern, threshold=0.85):
    """检查画布是否与某个模式相似，要求更高的匹配度"""
    # 计算整体匹配度
    match_score = count_matches(canvas, pattern)
    
    # 检查1的位置匹配情况
    ones_match = 0
    total_ones = 0
    for i in range(5):
        for j in range(3):
            if pattern[i][j] == 1:
                total_ones += 1
                if canvas[i][j] == 1:
                    ones_match += 1
    
    ones_score = ones_match / total_ones if total_ones > 0 else 0
    
    # 同时满足整体匹配度和1的位置匹配要求
    return match_score >= threshold and ones_score >= 0.8

def is_number1(canvas):
    """检查是否是数字1"""
    try:
        validate_canvas(canvas)
        
        # 检查是否与标准1匹配
        if is_similar_to_pattern(canvas, STANDARD_1):
            return True
            
        # 检查是否与任何1的变体匹配
        for pattern in VARIANTS_1.values():
            if is_similar_to_pattern(canvas, pattern):
                return True
                
        return False
        
    except ValueError:
        raise
    except Exception as e:
        return False

def is_number7(canvas):
    """检查是否是数字7"""
    try:
        validate_canvas(canvas)
        
        # 首先检查是否是1，如果是1就不可能是7
        if is_number1(canvas):
            return False
        
        # 检查是否与标准7匹配
        if is_similar_to_pattern(canvas, STANDARD_7):
            return True
            
        # 检查是否与任何7的变体匹配
        for pattern in VARIANTS_7.values():
            if is_similar_to_pattern(canvas, pattern):
                return True
                
        return False
        
    except ValueError:
        raise
    except Exception as e:
        return False

def main():
    # 测试用例
    test_cases = [
        # 标准数字1
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ],
        # 标准数字7
        [
            [1, 1, 1],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
    ]
    
    for i, canvas in enumerate(test_cases, 1):
        print(f"\n测试用例 {i}:")
        print("画布内容:")
        for row in canvas:
            print(row)
        print(f"是数字1? {is_number1(canvas)}")
        print(f"是数字7? {is_number7(canvas)}")

if __name__ == "__main__":
    main() 