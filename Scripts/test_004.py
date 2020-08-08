import allure
class Test004:
    @allure.step('下单')
    def input_valuer(self):
        print('\ninput_valuer')

    @allure.step('登录')
    def test_001(self):
        self.input_valuer()
        print('\ntest_001')
        assert  True