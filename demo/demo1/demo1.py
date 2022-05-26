import backtrader as bt
from SampleStrategy import SampleStrategy
import datetime


if __name__ == '__main__':
    cerebro = bt.Cerebro()

    strats = cerebro.addstrategy(SampleStrategy)

    cerebro.addsizer(bt.sizers.FixedSize, stake=100)

    # 加载数据到模型中
    data = bt.feeds.GenericCSVData(
        dataname='600519.csv',
        fromdate=datetime.datetime(2010, 1, 1),
        todate=datetime.datetime(2020, 4, 12),
        dtformat='%Y%m%d',
        datetime=2,
        open=3,
        high=4,
        low=5,
        close=6,
        volume=10
    )

    cerebro.adddata(data)
    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(0.005)
    # 策略执行前的资金
    print('启动资金: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())