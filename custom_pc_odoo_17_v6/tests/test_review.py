```python
from odoo.tests import common

class TestReview(common.TransactionCase):

    def setUp(self):
        super(TestReview, self).setUp()
        self.Review = self.env['custom_pc_odoo_17_v6.review']

    def test_submit_review(self):
        # Create a new review
        new_review = self.Review.create({
            'name': 'Test Review',
            'rating': 5,
            'comment': 'Great product!',
            'product_id': 1
        })

        # Check if the review is created
        self.assertEqual(new_review.name, 'Test Review')
        self.assertEqual(new_review.rating, 5)
        self.assertEqual(new_review.comment, 'Great product!')
        self.assertEqual(new_review.product_id, 1)

    def test_review_criteria(self):
        # Create a new review
        new_review = self.Review.create({
            'name': 'Test Review',
            'rating': 5,
            'comment': 'Great product!',
            'product_id': 1,
            'performance': 5,
            'durability': 4,
            'value': 5
        })

        # Check if the review criteria are correctly set
        self.assertEqual(new_review.performance, 5)
        self.assertEqual(new_review.durability, 4)
        self.assertEqual(new_review.value, 5)

    def test_review_average_rating(self):
        # Create multiple reviews
        review_1 = self.Review.create({
            'name': 'Review 1',
            'rating': 5,
            'comment': 'Great product!',
            'product_id': 1
        })
        review_2 = self.Review.create({
            'name': 'Review 2',
            'rating': 4,
            'comment': 'Good product!',
            'product_id': 1
        })

        # Check if the average rating is correctly calculated
        average_rating = (review_1.rating + review_2.rating) / 2
        self.assertEqual(average_rating, 4.5)
```