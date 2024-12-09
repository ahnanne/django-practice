from item.models import Item


def inject_image(item: Item):
    if not item.image.name:
        item.image = 'item_images/no_image.jpg'

    return item
