import logging

from finder import find_fimg, find_parseval


def configure_logging(lvl, fmt, dfmt):
    logging.basicConfig(level=lvl, format=fmt, datefmt=dfmt)


configure_logging(logging.INFO,
                  '%(asctime)s - %(levelname)s - %(message)s',
                  '%Y-%m-%d %H:%M:%S')


def get_fs(function, a_b_pars: list):
    fs = []
    for i in range(len(a_b_pars)):
        fs.append(function(a_b_pars[i][0], a_b_pars[i][1]))
        logging.info(f'Got function #{i}')

    return fs


def get_fimgs(fs: list, interval: list):
    fimgs = []
    for i in range(len(fs)):
        fimgs.append(find_fimg(fs[i], interval[0], interval[1]))
        logging.info(f'Got Fourier image for function #{i}')

    return fimgs


def get_parsevals(fs: list, fimgs: list, interval: list):
    plpr = []
    for i in range(len(fs)):
        pl, pr = find_parseval(fs[i], fimgs[i], interval[0], interval[1])
        plpr.append((pl, pr))
        logging.info(f'Got parseval for function #{i}')

    return plpr


def print_parsevals(plpr: list):
    for i in range(len(plpr)):
        print(f'p_{i + 1}: {plpr[i][0]} ?= {plpr[i][1]}')