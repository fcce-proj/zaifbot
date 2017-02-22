from zaifbot import ZaifBot
from zaifbot.modules.auto_trade import *


class MyLosCutProcess(LossCut):
    def execute(self):
        return True


class MyAdditionalPurchase(AdditionalPurchase):
    def execute(self):
        return True


class MyCustom(Custom):
    def execute(self):
        return True

    def is_started(self):
        return True


if __name__ == '__main__':
    bot = ZaifBot()
    bot.add_running_process(MyLosCutProcess)
    bot.add_running_process(MyAdditionalPurchase)
    bot.add_running_process(MyCustom)
    bot.start()
