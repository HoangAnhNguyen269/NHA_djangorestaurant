from django.db import models

# Create your models here.
class Ingredient(models.Model):
    """
    Represents a single ingredient in the restaurant's inventory
    """
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default="")
    quantity = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
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
    """
    Represents an entry off the restaurant's menu
    """
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100, default="")
    price= models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"title={self.name}; price={self.price}"

class RecipeRequirements(models.Model):
    """
    Represents an ingredient required for a recipe for a MenuItem
    """
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
    """
    Represents a purchase of a MenuItem
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"""
        menu_item={self.menu_item};
        qty={self.quantity};
        timestamp={self.timestamp}
        """
