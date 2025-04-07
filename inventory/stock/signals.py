from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from .models import StockTransaction, StockIn, StockOut
from inventory.parts.models import Part


def adjust_stock(part, quantity, transaction_type, reverse=False):
    """Helper to adjust stock quantity of a part."""
    if reverse:
        quantity = -quantity

    if transaction_type == 'IN':
        part.stock_quantity += quantity
    elif transaction_type == 'OUT':
        part.stock_quantity -= quantity

    # Ensure non-negative stock
    part.stock_quantity = max(part.stock_quantity, 0)
    part.save()


# === Handle CREATE and UPDATE ===
@receiver(pre_save, sender=StockIn)
def handle_stock_update(sender, instance, **kwargs):
    print("\nPre save")
    print(instance)
    print("\nPre save")
    if instance.pk:
        # It's an update, get the previous instance
        prev = StockIn.objects.get(pk=instance.pk)
        if prev.quantity != instance.quantity or prev.part != instance.part:
            # Reverse the old transaction
            adjust_stock(prev.part, prev.quantity, prev.transaction_type, reverse=True)
    # Else it's a new instance – will be handled in post_save


@receiver(post_save, sender=StockIn)
def handle_stock_create(sender, instance, created, **kwargs):
    # Whether new or updated, re-apply the current transaction
    adjust_stock(instance.part, instance.quantity, instance.transaction_type)


# === Handle DELETE ===
@receiver(post_delete, sender=StockIn)
def handle_stock_delete(sender, instance, **kwargs):
    adjust_stock(instance.part, instance.quantity, instance.transaction_type, reverse=True)



# stock out
@receiver(pre_save, sender=StockOut)
def handle_stock_update(sender, instance, **kwargs):
    print("\nPre save")
    print(instance)
    print("\nPre save")
    if instance.pk:
        # It's an update, get the previous instance
        prev = StockOut.objects.get(pk=instance.pk)
        if prev.quantity != instance.quantity or prev.part != instance.part:
            # Reverse the old transaction
            adjust_stock(prev.part, prev.quantity, prev.transaction_type, reverse=True)
    # Else it's a new instance – will be handled in post_save


@receiver(post_save, sender=StockOut)
def handle_stock_create(sender, instance, created, **kwargs):
    # Whether new or updated, re-apply the current transaction
    adjust_stock(instance.part, instance.quantity, instance.transaction_type)


# === Handle DELETE ===
@receiver(post_delete, sender=StockOut)
def handle_stock_delete(sender, instance, **kwargs):
    adjust_stock(instance.part, instance.quantity, instance.transaction_type, reverse=True)


# stock transaction
@receiver(pre_save, sender=StockTransaction)
def handle_stock_update(sender, instance, **kwargs):
    print("\nPre save")
    print(instance)
    print("\nPre save")
    if instance.pk:
        # It's an update, get the previous instance
        prev = StockTransaction.objects.get(pk=instance.pk)
        if prev.quantity != instance.quantity or prev.part != instance.part:
            # Reverse the old transaction
            adjust_stock(prev.part, prev.quantity, prev.transaction_type, reverse=True)
    # Else it's a new instance – will be handled in post_save


@receiver(post_save, sender=StockTransaction)
def handle_stock_create(sender, instance, created, **kwargs):
    # Whether new or updated, re-apply the current transaction
    adjust_stock(instance.part, instance.quantity, instance.transaction_type)


# === Handle DELETE ===
@receiver(post_delete, sender=StockTransaction)
def handle_stock_delete(sender, instance, **kwargs):
    adjust_stock(instance.part, instance.quantity, instance.transaction_type, reverse=True)
