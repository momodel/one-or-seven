import unittest
from main import is_number1, is_number7
from number_patterns import STANDARD_1, STANDARD_7, VARIANTS_1, VARIANTS_7

class TestNumberRecognition(unittest.TestCase):
    def setUp(self):
        self.standard_1 = STANDARD_1
        self.standard_7 = STANDARD_7

    def print_canvas(self, canvas):
        """用格子图打印画布内容"""
        print("\n画布内容:")
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

    def test_standard_numbers(self):
        """测试标准数字1和7的识别"""
        try:
            self.assertTrue(is_number1(self.standard_1), "标准数字1识别失败")
            self.assertTrue(is_number7(self.standard_7), "标准数字7识别失败")
            self.assertFalse(is_number7(self.standard_1), "数字1被错误识别为7")
            self.assertFalse(is_number1(self.standard_7), "数字7被错误识别为1")
        except AssertionError as e:
            self.print_canvas(self.standard_1 if "1" in str(e) else self.standard_7)
            raise e

    def test_number1_variants(self):
        """测试数字1的各种变体"""
        for name, canvas in VARIANTS_1.items():
            try:
                self.assertTrue(is_number1(canvas), f"{name}识别失败")
            except AssertionError as e:
                print(f"\n测试失败: {name}")
                self.print_canvas(canvas)
                raise e

    def test_number7_variants(self):
        """测试数字7的各种变体"""
        for name, canvas in VARIANTS_7.items():
            try:
                self.assertTrue(is_number7(canvas), f"{name}识别失败")
            except AssertionError as e:
                print(f"\n测试失败: {name}")
                self.print_canvas(canvas)
                raise e

if __name__ == '__main__':
    unittest.main(verbosity=2) 