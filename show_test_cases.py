from number_patterns import STANDARD_1, STANDARD_7, VARIANTS_1, VARIANTS_7

def print_canvas(canvas, title=""):
    """用格子图打印画布内容"""
    print(f"\n{title}")
    print("┌───┬───┬───┐")
    
    for i, row in enumerate(canvas):
        cells = []
        for cell in row:
            if cell == 1:
                cells.append("█")
            else:
                cells.append(" ")
        print(f"│ {cells[0]} │ {cells[1]} │ {cells[2]} │")
        
        if i < len(canvas) - 1:
            print("├───┼───┼───┤")
        else:
            print("└───┴───┴───┘")

def show_all_test_cases():
    # 显示标准数字
    print("\n=== 标准数字 ===")
    print_canvas(STANDARD_1, "标准数字1")
    print_canvas(STANDARD_7, "标准数字7")
    
    # 显示数字1的变体
    print("\n=== 数字1的变体 ===")
    for name, canvas in VARIANTS_1.items():
        print_canvas(canvas, name)
    
    # 显示数字7的变体
    print("\n=== 数字7的变体 ===")
    for name, canvas in VARIANTS_7.items():
        print_canvas(canvas, name)

if __name__ == "__main__":
    show_all_test_cases() 