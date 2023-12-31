from django.core.management import BaseCommand

from online_store.models import CategoryProduct, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        category = CategoryProduct.objects.get(id=4)
        product_list = [
            {'title': 'Apple iMac 4.5K 24" (2021) Green (M1 8-Core CPU/8-Core GPU, 16GB, 2Tb)',
             'description': 'История дизайна устройств Apple довольно интересна, особенно своей цикличностью. '
                            'Самый известный пример – все iPhone 12-й серии, очень напоминающие iPhone 5, 5S и SE. '
                            'В далёком 1998 году были представлены iMac G3, поразившие всех своим дизайном и '
                            'разнообразием расцветок. В 2021 году Apple показали обновление линейки iMac на собственных '
                            'процессорах. Теперь моноблок удивляет не только многообразием расцветок, но и невероятно '
                            'тонким корпусом и приятные сюрпризы на этом только начинаются. 24-дюймовый дисплей iMac '
                            'можно назвать «золотой серединой», если сравнить первую линейку на M1 с предыдущими '
                            'моделями. Моноблок легко поместится на любом столе, а размеры экрана оптимальны для '
                            'большинства задач. Параметры встроенного дисплея Retina тоже впечатляют: разрешение 4,5K, '
                            'миллиард цветов, высокая яркость и отличная цветопередача. Стекло с минимальным отражением '
                            'света практически исключает блики. При необходимости, к компьютеру можно подключить '
                            'дополнительный монитор с разрешением до 6К. В 2021 году, на момент выхода iMac 24”, '
                            'возможности процессора M1 уже не вызывают сомнений. Компьютеры на базе чипа от Apple '
                            'побили множество рекордов производительности. Улучшенная оптимизация под фирменные '
                            'пакеты (например, Final Cut), возможность запуска ПО для iOS и множество приятных '
                            'особенностей, таких как моментальный выход из режима сна, сделали первый настольный '
                            'процессор Apple мечтой многих пользователей Mac. Встроенная многоядерная графика позволяет '
                            'наслаждаться современными играми, а для запуска старых приложений предусмотрен специальный '
                            'автоматический эмулятор, поэтому проблемы с совместимостью практически исключены. '
                            'Наработки Apple по улучшению динамиков в компактных устройствах добрались до iMac. '
                            'Моноблоки компании всегда отличались громким и насыщенным звуком, но модель 2021 года – '
                            'это новый шаг. Система из шести динамиков обеспечивает объёмный детализированный звук, '
                            'заполняющий окружающее пространство. Поддержка технологии Dolby Atmos позволит с в полной '
                            'мере насладиться кино и сериалами, не подключая наушники или внешнюю акустику. Встроенная '
                            'веб-камера iMac заметно отличается от аналогов во всех компьютерах Apple, выпущенных ранее.'
                            ' Она отличается не только более высоким разрешением, но и технологией шумоподавления, '
                            'которая делает изображение приятным, вне зависимости от окружающего освещения. Ваши '
                            'собеседники будут видеть вас практически как вживую.',
             'category': category,
             'price': 300990,
             },
        ]
        for product in product_list:
            Product.objects.create(**product)
