from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """

class MenuItem(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price= models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"title={self.title}; price={self.price}"

class RecipeRequirements(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return f"""
        menu_item={self.menu_item};
        ingredient={self.ingredient};
        qty={self.quantity}
        """

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"""
        menu_item={self.menu_item};
        qty={self.quantity};
        timestamp={self.timestamp}
        """
