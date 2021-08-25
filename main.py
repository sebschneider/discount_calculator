from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivmob import KivMob

class MainWindow(Screen):

    pass
class SecondWindow(Screen):

    def showbanner(self):
        self.ads = KivMob('*****')
        self.ads.new_banner('*****', top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()

    def on_resume(self):
        self.ads.request_banner()

    def on_pre_enter(self, *args):
        self.showbanner()

    def destroy(self):
        self.ads.destroy_banner()

    fullprice = ObjectProperty(None)
    discount = ObjectProperty(None)

    def button(self, fullprice, discount):
        if self.ids.calculate.text == 'Try Again?':
            self.ids.fullprice.text = ''
            self.ids.discount.text = ''
            self.ids.payment_result.text = ''
            self.ids.savings_result.text = ''
            self.ids.calculate.text = 'Calculate'
            self.destroy()
            self.showbanner()

        else:
            try:
                fullprice = float(fullprice.text)
                discount = float(discount.text)
                ruleofthree = (discount * fullprice) / 100
                realpay = fullprice - ruleofthree
                savings = fullprice - realpay
                self.ids.payment_result.text = str("$ {:.2f}".format(realpay))
                self.ids.savings_result.text = str("$ {:.2f}".format(savings))
                self.ids.calculate.text = str('Try Again?')

            except ValueError:
                pass

class WindowManager(ScreenManager):
    pass

class DiscountApp(App):

    def showads(self, *args):
        self.ads = KivMob('*****')
        self.ads.new_interstitial('*****')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def on_pre_enter(self):
         self.ads.request_interstitial()

    def build(self):
        self.showads()
        m = WindowManager()
        return m

if __name__ == "__main__":
    DiscountApp().run()