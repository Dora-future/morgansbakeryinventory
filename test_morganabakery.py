import unittest
from morganabakery import ingredients, sell_product, products, sales_log

class TestBakery(unittest.TestCase):


    def setUp(self):
        # Reset ingredient quantities before each test
        ingredients["Flour"]["quantity"] = 100       # refill Flour
        ingredients["Sugar"]["quantity"] = 50        # refill Sugar
        ingredients["Butter"]["quantity"] = 20       # refill Butter
        ingredients["Eggs"]["quantity"] = 100        # refill Eggs
        ingredients["Salt"]["quantity"] = 20         # refill Salt if needed
        ingredients["OliveOil"]["quantity"] = 1      # refill Olive Oil if needed
        ingredients["Milk"]["quantity"] = 50         # refill Milk if needed
        ingredients["Cinnamon"]["quantity"] = 10     # refill Cinnamon if needed
        ingredients["VanillaPod"]["quantity"] = 70   # refill VanillaPod if needed
        ingredients["Yeast"]["quantity"] = 10        # refill Yeast if needed

    # Clear the sales log before each test
    sales_log.clear()


    def test_sell_product_success(self):
        # Sell 2 Muffins
        sell_product("Muffin", 2)
        # Check that ingredients were deducted correctly
        self.assertEqual(ingredients["Flour"]["quantity"], 100 - 0.1*2)
        self.assertEqual(ingredients["Sugar"]["quantity"], 50 - 0.05*2)
        self.assertEqual(ingredients["Butter"]["quantity"], 20 - 0.05*2)
        self.assertEqual(ingredients["Eggs"]["quantity"], 100 - 1*2)
        # Check sales log
        self.assertEqual(len(sales_log), 1)
        self.assertEqual(sales_log[0]["product"], "Muffin")
        self.assertEqual(sales_log[0]["quantity"], 2)

    def test_sell_product_insufficient_stock(self):
        # Try selling more Bread than available stock
        ingredients["Flour"]["quantity"] = 0.1  # Not enough for 1 Bread
        sell_product("Bread", 1)
        # Ingredients should not change
        self.assertEqual(ingredients["Flour"]["quantity"], 0.1)
        # Sales log should remain empty
        self.assertEqual(len(sales_log), 0)

    def test_product_not_found(self):
        # Try selling a product that doesn't exist
        sell_product("Cupcake", 1)

        self.assertEqual(len(sales_log), 0)

if __name__ == "__main__":
    unittest.main()
