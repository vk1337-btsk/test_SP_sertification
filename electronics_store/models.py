from django.db import models


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, "Завод"),
        (1, "Розничная сеть"),
        (2, "Индивидуальный предприниматель"),
    ]

    name = models.CharField(max_length=255, verbose_name="Название")
    email = models.EmailField(verbose_name="Эл. почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name="Уровень узла")
    supplier = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="clients", verbose_name="Поставщик"
    )
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Задолженность, руб")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    class Meta:
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=255, verbose_name="Модель")
    release_date = models.DateField(verbose_name="Дата выхода продукта")
    network_node = models.ForeignKey(
        NetworkNode, on_delete=models.CASCADE, related_name="products", verbose_name="Поставщик"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name} ({self.model})"
