```python
from odoo.tests import common

class TestPcBuilder(common.TransactionCase):

    def setUp(self):
        super(TestPcBuilder, self).setUp()
        self.PcBuilder = self.env['custom_pc_odoo_17_v6.pc_builder']

    def test_component_selection(self):
        # Create a new PC Builder instance
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
            'cpu': 'Intel Core i7',
            'gpu': 'Nvidia RTX 3080',
            'ram': '16GB DDR4',
            'storage': '1TB SSD',
            'power_supply': '750W',
            'cooling_system': 'Liquid Cooling',
            'case': 'ATX Mid Tower',
        })

        # Check if the PC Builder instance was created
        self.assertEqual(pc_builder.name, 'Test PC Builder')

        # Check if the selected components are correct
        self.assertEqual(pc_builder.cpu, 'Intel Core i7')
        self.assertEqual(pc_builder.gpu, 'Nvidia RTX 3080')
        self.assertEqual(pc_builder.ram, '16GB DDR4')
        self.assertEqual(pc_builder.storage, '1TB SSD')
        self.assertEqual(pc_builder.power_supply, '750W')
        self.assertEqual(pc_builder.cooling_system, 'Liquid Cooling')
        self.assertEqual(pc_builder.case, 'ATX Mid Tower')

    def test_compatibility_logic(self):
        # Create a new PC Builder instance
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
            'cpu': 'Intel Core i7',
            'gpu': 'Nvidia RTX 3080',
            'ram': '16GB DDR4',
            'storage': '1TB SSD',
            'power_supply': '750W',
            'cooling_system': 'Liquid Cooling',
            'case': 'ATX Mid Tower',
        })

        # Check if the compatibility logic works correctly
        self.assertTrue(pc_builder.check_compatibility())

    def test_upgrade_recommendation(self):
        # Create a new PC Builder instance
        pc_builder = self.PcBuilder.create({
            'name': 'Test PC Builder',
            'cpu': 'Intel Core i5',
            'gpu': 'Nvidia GTX 1660',
            'ram': '8GB DDR4',
            'storage': '500GB SSD',
            'power_supply': '500W',
            'cooling_system': 'Air Cooling',
            'case': 'ATX Mid Tower',
        })

        # Check if the upgrade recommendation works correctly
        self.assertEqual(pc_builder.recommend_upgrade(), 'Upgrade to Intel Core i7 and Nvidia RTX 3080 for better performance')
```
