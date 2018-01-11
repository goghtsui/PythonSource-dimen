#!/usr/bin/env python

import Type

"""   将dimens中数值根据对应的 density 和 dp、px 等单位 转换为相应值 """


def format_value(value, density, scale_density, xdpi):
    """  截取字符串中的数字, 单位，并做对应转换  """
    if Type.dip in value:
        unit = value[-3:]
        number = int(value[:-3])
        result = switch(unit, number, density, scale_density, xdpi)
        return str(result) + unit
    else:
        unit = value[-2:]
        number = int(value[:-2])
        result = switch(unit, number, density, scale_density, xdpi)
        return str(result) + unit


def switch(unit, value, density, scale_density, xdpi):
    """ 根据对应的单位，对数值做不同的值转换 """
    switcher = {
        Type.px: value,
        Type.dp: value * density,
        Type.dip: value * density,
        Type.sp: value * scale_density,
        Type.pt: value * xdpi * (1.0 / 72),
        Type.inch: value * xdpi,
        Type.mm: value * xdpi * (1.0 / 25.4),
    }

    return switcher.get(unit, 0)
