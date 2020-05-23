ORDERS = ["first", "second", "third", "fourth",
          "fifth", "sixth", "seventh", "eighth",
          "ninth", "tenth", "eleventh", "twelfth"]
GIFTS = ["a Partridge in a Pear Tree.",
         "two Turtle Doves",
         "three French Hens",
         "four Calling Birds",
         "five Gold Rings",
         "six Geese-a-Laying",
         "seven Swans-a-Swimming",
         "eight Maids-a-Milking",
         "nine Ladies Dancing",
         "ten Lords-a-Leaping",
         "eleven Pipers Piping",
         "twelve Drummers Drumming"]


def recite(start_verse, end_verse):
    return [create_song(num) for num in range(start_verse, end_verse + 1)]


def create_song(num):
    return "On the {} day of Christmas my true love gave to me: {}".format(
        ORDERS[num - 1], create_gifts(num))


def create_gifts(num):
    gifts = [GIFTS[i] for i in range(num - 1, -1, -1)]
    if num > 1:
        gifts[num - 1] = "and " + gifts[num - 1]
    return ", ".join(gifts)
