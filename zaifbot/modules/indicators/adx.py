import time
import pandas as pd
from pandas import DataFrame, Series
from zaifbot.modules.api.wrapper import BotPublicApi


def get_adm(currency_pair, period='1d', count=5, length=14, to_epoch_time=int(time.time())):
    public_api = BotPublicApi()
    second_api_params = {'period': period, 'count': count + 2 * length - 1, 'to_epoch_time': to_epoch_time}
    price_infos = DataFrame(public_api.everything('ohlc_data', currency_pair, second_api_params))
    return _get_adm(price_infos[['high', 'low', 'time', 'close']].copy(), length, count)


def _get_adm(df, length, count):
    df = pd.concat([df, _get_dm(df)], axis=1)
    df['TR'] = _get_tr(df)
    df = _get_di(df, length, count)
    df['ADX'] = (abs(df['+DI'] - df['-DI']) / df['+DI'] - df['-DI']).rolling(window=length).mean()
    print(df)
    return df


def _get_dm(df):
    """引数にはhigh,low, closeをカラム名に持つDataFrameをとる"""
    def _calc_dm(row):
        high_dff = max(row['high'], 0)
        low_diff = min(row['low'], 0)

        if abs(high_dff) > abs(low_diff):
            return Series({'+DM': high_dff, '-DM': 0})
        elif abs(high_dff) < abs(low_diff):
            return Series({'+DM': 0, '-DM': abs(low_diff)})
        else:
            return Series({'+DM': 0, '-DM': 0})

    return df.diff().fillna(0).apply(_calc_dm, axis=1)


def _get_tr(df):
    """引数にはhigh, low, closeをカラム名に持つDataFrameをとる"""
    new_row = list()
    new_row.append(0)
    for i in range(1, len(df)):
        tdy_high_minus_ystday_high = df.ix[i, 'high'] - df.ix[i, 'low']
        tdy_high_minus_ystday_close = df.ix[i, 'high'] - df.ix[i - 1, 'close']
        ystday_close_minus_tdy_low = df.ix[i - 1, 'close'] - df.ix[i, 'low']
        new_row.append(max(tdy_high_minus_ystday_high, tdy_high_minus_ystday_close, ystday_close_minus_tdy_low))
    return new_row


# TODO: ロジック改善できそうな気がする
def _get_di(df, length, count):
    for i in range(count + length):
        df.ix[i + length - 1, '+DI'] = (df.ix[i:i + length - 1, '+DM'].sum() / df.ix[i:i + length - 1, 'TR'].sum()) * 100
        df.ix[i + length - 1, '-DI'] = (df.ix[i:i + length - 1, '-DM'].sum() / df.ix[i:i + length - 1, 'TR'].sum()) * 100
    return df.fillna(0)


if __name__ == '__main__':
    get_adm('btc_jpy')
