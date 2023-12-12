```javascript
odoo.define('custom_pc_odoo_17_v6.order', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;

    $(document).ready(function () {

        // Event handler for placing an order
        $('#order-form').on('submit', function (event) {
            event.preventDefault();

            var orderData = {
                'product_id': $('#product-id').val(),
                'quantity': $('#quantity').val(),
                'custom_engraving': $('#custom-engraving').val(),
                'packaging': $('#packaging').val(),
                'gift_note': $('#gift-note').val()
            };

            ajax.jsonRpc("/api/orders", 'call', orderData)
                .then(function (data) {
                    if (data.success) {
                        alert(_t("Order placed successfully!"));
                    } else {
                        alert(_t("Failed to place order: ") + data.error);
                    }
                });
        });

        // Event handler for calculating shipping cost
        $('#shipping-form').on('submit', function (event) {
            event.preventDefault();

            var shippingData = {
                'order_id': $('#order-id').val(),
                'carrier_id': $('#carrier-id').val()
            };

            ajax.jsonRpc("/api/shipping", 'call', shippingData)
                .then(function (data) {
                    if (data.success) {
                        $('#shipping-cost').text(_t("Shipping Cost: ") + data.cost);
                    } else {
                        alert(_t("Failed to calculate shipping cost: ") + data.error);
                    }
                });
        });

    });

});
```