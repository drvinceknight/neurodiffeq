import torch
import torch.autograd as autograd


def diff(x, t, order=1):
    """The derivative of a variable with respect to another.

    :param x: The :math:`x` in :math:`\\displaystyle\\frac{\\partial x}{\\partial t}`.
    :type x: `torch.tensor`
    :param t: The :math:`t` in :math:`\\displaystyle\\frac{\\partial x}{\\partial t}`.
    :type t: `torch.tensor`
    :param order: The order of the derivative, defaults to 1.
    :type order: int
    :returns: The derivative.
    :rtype: `torch.tensor`
    """
    ones = torch.ones_like(t)
    der, = autograd.grad(x, t, create_graph=True, grad_outputs=ones)
    for i in range(1, order):
        der, = autograd.grad(der, t, create_graph=True, grad_outputs=ones)
    return der
