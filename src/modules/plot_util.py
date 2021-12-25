import matplotlib.pyplot as plt
from numpy import ndarray
from os.path import join
from typing import Tuple, Any


def roc_plot(
    data: Tuple[ndarray, ndarray],
    auc: float,
    name: str
) -> None:
    f, a = simple_ax(figsize=(10, 6))
    plt.plot(data[0], data[1], linewidth=2)
    plt.plot([0, 1], [0, 1], color='r', linestyle='--')
    plt.xlabel('FPR')
    plt.ylabel('TPR')
    a.text(0.8, 0.1, 'AUC = %f' % auc, fontsize=12, bbox={
        'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
    plt.savefig(join('./data/processed/', name + '.png'))
    plt.show()


def prettify_ax(
    ax: plt.Axes
) -> None:
    ''' Make an axis pretty '''
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_frameon = True
    ax.patch.set_facecolor('#eeeeef')
    ax.grid('on', color='w', linestyle='-', linewidth=1)
    ax.tick_params(direction='out')
    ax.set_axisbelow(True)


def simple_ax(
    figsize: Tuple[float, float] = (6, 4),
    **kwargs: dict[str, Any]
) -> Tuple[plt.Figure, plt.Axes]:
    ''' Single prettified axis '''
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, **kwargs)
    prettify_ax(ax)
    return fig, ax
