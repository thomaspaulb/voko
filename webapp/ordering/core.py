from django.db import OperationalError
import models


def get_current_order_round():
    ## TODO: Get current order round based on current date
    ## If non existing, get_or_create?
    try:
        return models.OrderRound.objects.all().order_by("-pk")[0]
    except IndexError:
        print "INDEX FAIL"
        return
    except OperationalError:
        print "OPERATIONAL ERROR"
        pass


def get_or_create_order(user):
    try:
        return models.Order.objects.get_or_create(finalized=False,
                                                  user=user,
                                                  defaults={'order_round': models.OrderRound.objects.order_by('-pk')[0],
                                                            'user': user})[0]
    except IndexError:
        raise RuntimeError("Nog geen bestelronde aangemaakt!")


def get_order_product(product, order):
    existing_ops = models.OrderProduct.objects.filter(product=product, order=order)
    if existing_ops:
        return existing_ops[0]


def get_credit(user):
    credit = sum([b.amount for b in user.balance.filter(type="CR")])
    debit = sum([b.amount for b in user.balance.filter(type="DR")])

    return credit - debit


def get_debit(user):
    return -get_credit(user)